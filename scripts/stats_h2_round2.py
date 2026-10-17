"""Round 2 (item 7; review R1 N4): two checks of H2 in arXiv mathematics and physics theory (papers with at most 50
authors), from the same OAI harvests and name matching as stats_heavy_producers.py.

1. Classes ranked on an independent window. Names are ranked on their fractional output in the twelve months before
   the first compared window: Q3 of year y-1 to Q2 of year y for the third quarters of y and y+1, and calendar year y-1
   for January-August of y and y+1. The change between the two compared windows is then decomposed by those classes:
   top 1%, next 9% and bottom 90% of the names active in the ranking window, and names not active in it. Neither
   compared window overlaps the ranking window, so no class is selected on the outcome. Activity decays with time, so
   the top class is expected to grow less than the rest even under proportional growth; the pairs of years before
   ChatGPT's release show how much. Also reported: the share of the increase that came from names in the
   combined-output top 1% (the class of the main decomposition) that were not in the ranking window's top 1%.
2. Uniform-scaling simulation for the concentration shares. A pool of names with Gamma- or lognormal-distributed
   rates fills the author slots of papers whose numbers of distinct authors are drawn from the base window's
   distribution. The pool size and the distribution's parameter are calibrated to the base window's active names and
   top-1% share; the calibration record gives the fit. Scaling the number of
   papers by the observed growth, with the rates unchanged relative to one another, gives the change in the top-1% and
   top-10% shares of fractional output that proportional growth alone produces (mean and SD over replications).
Only aggregates are written; classes with fewer than ten names are suppressed.
Usage: python3 scripts/stats_h2_round2.py OAI_DIR [out.json]
"""
import json
import os
import sys
from collections import Counter

import numpy as np
from scipy.stats import gamma, norm

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from stats_heavy_producers import MIN_CELL, THEORY, load  # noqa: E402

RNG = np.random.default_rng(20261017)
# rate distributions of the name pool and their calibration grids (Gamma shape; lognormal sigma)
GRIDS = {"gamma": [0.01, 0.02, 0.03, 0.05, 0.08, 0.1, 0.13, 0.16, 0.2, 0.25, 0.3, 0.4, 0.5, 0.7, 1.0, 1.5],
         "lognormal": [0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0, 3.5]}


def months_between(a, b):
    y, m = int(a[:4]), int(a[5:])
    out = []
    while f"{y}-{m:02d}" <= b:
        out.append(f"{y}-{m:02d}")
        y, m = (y + 1, 1) if m == 12 else (y, m + 1)
    return set(out)


def frac_output(papers, keep, months):
    f = Counter()
    for p in papers:
        if p["month"] in months:
            ns = {a[0] for a in p["authors"] if keep(a)}
            for n in ns:
                f[n] += 1 / len(ns)
    return f


def top_weight(values, share_div):
    """Membership weight in the top n // share_div names by value; names tied at the boundary share the places."""
    vals = sorted(values.values(), reverse=True)
    m = max(1, len(vals) // share_div)
    v = vals[m - 1]
    above, tied = sum(1 for x in vals if x > v), sum(1 for x in vals if x == v)
    wt = (m - above) / tied
    return lambda x: 0.0 if x not in values else 1.0 if values[x] > v else wt if values[x] == v else 0.0


def independent_window(papers, keep, rank_months, a_months, b_months):
    R, A, B = (frac_output(papers, keep, ms) for ms in (rank_months, a_months, b_months))
    w1, w10 = top_weight(R, 100), top_weight(R, 10)
    classes = {"top1pct": w1, "next9pct": lambda x: w10(x) - w1(x),
               "bottom90pct": lambda x: (1.0 - w10(x)) if x in R else 0.0,
               "not_active_in_ranking_window": lambda x: 0.0 if x in R else 1.0}
    names = set(A) | set(B)
    ta, tb = sum(A.values()), sum(B.values())
    out = {"total_a": ta, "total_b": tb, "growth": tb / ta - 1, "names_ranked": len(R)}
    for k, w in classes.items():
        ws = {x: w(x) for x in names}
        n_active = sum(ws.values())
        n_class = sum(w(x) for x in R) if k != "not_active_in_ranking_window" else None
        if n_active < MIN_CELL:
            out[k] = {"suppressed_lt10_names": True}
            continue
        oa, ob = sum(ws[x] * v for x, v in A.items()), sum(ws[x] * v for x, v in B.items())
        out[k] = {"names_in_class": n_class, "names_active_in_a_or_b": n_active, "output_a": oa, "output_b": ob,
                  "growth": ob / oa - 1 if oa else None, "share_of_output_a": oa / ta,
                  "share_of_change": (ob - oa) / (tb - ta) if tb != ta else None}
    comb = Counter(A)
    comb.update(B)
    c1 = top_weight(comb, 100)
    new = sum(c1(x) * (1.0 - w1(x)) * (B.get(x, 0) - A.get(x, 0)) for x in comb)
    old = sum(c1(x) * w1(x) * (B.get(x, 0) - A.get(x, 0)) for x in comb)
    out["combined_top1pct"] = {"share_of_change_from_names_not_in_ranking_top1pct": new / (tb - ta) if tb != ta else None,
                               "share_of_change_from_names_in_ranking_top1pct": old / (tb - ta) if tb != ta else None,
                               "names_also_in_ranking_top1pct": sum(c1(x) * w1(x) for x in comb),
                               "names": sum(c1(x) for x in comb)}
    return out


def shares(frac):
    fr = np.sort(frac[frac > 0])[::-1]
    n, tot = len(fr), fr.sum()
    return {"active": n, "top1": fr[: max(1, n // 100)].sum() / tot, "top10": fr[: max(1, n // 10)].sum() / tot}


def simulate(lam, team_sizes, n_papers, rng):
    """One period: n_papers papers, team sizes drawn from team_sizes, slots filled with probability proportional to
    lam (duplicates within a paper dropped); returns the shares of fractional output among active names."""
    s = rng.choice(team_sizes, size=n_papers)
    paper = np.repeat(np.arange(n_papers), s)
    name = rng.choice(len(lam), size=len(paper), p=lam / lam.sum())
    key = np.unique(paper.astype(np.int64) * len(lam) + name)
    paper, name = key // len(lam), key % len(lam)
    size = np.bincount(paper, minlength=n_papers)
    frac = np.bincount(name, weights=1.0 / size[paper], minlength=len(lam))
    return shares(frac)


def pool(model, k, n):
    q = (np.arange(n) + 0.5) / n
    return gamma.ppf(q, k) if model == "gamma" else np.exp(k * norm.ppf(q))


def calibrate(model, team_sizes, n_papers, active_obs, top1_obs, rng):
    """For each value of the rate distribution's parameter, the pool size that reproduces the expected number of active
    names; then the value whose simulated top-1% share is closest to the observed one (None if no value reproduces the
    active names within 3%)."""
    slots = n_papers * float(np.mean(team_sizes))
    best = None
    for k in GRIDS[model]:
        grid = pool(model, k, 20000)  # quantiles standing for equal shares of the pool, for the expected active count

        def exp_active(n):
            return n / len(grid) * float(np.sum(1 - np.exp(-slots * grid / (n * grid.mean()))))
        lo, hi = active_obs, 200 * active_obs
        while hi - lo > max(1, active_obs // 2000):
            n = (lo + hi) // 2
            lo, hi = (n, hi) if exp_active(n) < active_obs else (lo, n)
        lam = pool(model, k, hi)
        sims = [simulate(lam, team_sizes, n_papers, rng) for _ in range(5)]
        t1 = float(np.mean([x["top1"] for x in sims]))
        act = float(np.mean([x["active"] for x in sims]))
        if abs(act / active_obs - 1) > 0.03:  # the pool could not reproduce the active names at this shape
            continue
        if best is None or abs(t1 - top1_obs) < abs(best["top1_sim"] - top1_obs):
            best = {"model": model, "parameter": k, "pool": hi, "top1_sim": t1, "active_sim": act,
                    "top10_sim": float(np.mean([x["top10"] for x in sims]))}
    return best


def uniform_scaling(papers, keep, a_months, b_months, reps=100):
    """Observed shares in windows a and b, and their change under uniform scaling of every rate."""
    sel = {w: [p for p in papers if p["month"] in ms] for w, ms in (("a", a_months), ("b", b_months))}
    obs = {}
    for w, ps in sel.items():
        f = frac_output(ps, keep, a_months | b_months)
        obs[w] = shares(np.array(list(f.values())))
        obs[w]["papers"] = sum(1 for p in ps if any(keep(a) for a in p["authors"]))
    team = np.array([len({a[0] for a in p["authors"] if keep(a)}) for p in sel["a"]])
    team = team[team > 0]
    o1, o10 = obs["b"]["top1"] - obs["a"]["top1"], obs["b"]["top10"] - obs["a"]["top10"]
    out = {"observed": obs, "paper_growth": obs["b"]["papers"] / obs["a"]["papers"] - 1,
           "observed_change_top1": o1, "observed_change_top10": o10,
           "observed_active_growth": obs["b"]["active"] / obs["a"]["active"] - 1, "reps": reps}
    for model in GRIDS:
        cal = calibrate(model, team, obs["a"]["papers"], obs["a"]["active"], obs["a"]["top1"], RNG)
        if cal is None:
            out[model] = None
            continue
        lam = pool(model, cal["parameter"], cal["pool"])
        d1, d10, act = [], [], []
        for _ in range(reps):
            sa = simulate(lam, team, obs["a"]["papers"], RNG)
            sb = simulate(lam, team, obs["b"]["papers"], RNG)
            d1.append(sb["top1"] - sa["top1"])
            d10.append(sb["top10"] - sa["top10"])
            act.append(sb["active"] / sa["active"] - 1)
        out[model] = {"calibration": cal,
                      "null_change_top1": {"mean": float(np.mean(d1)), "sd": float(np.std(d1, ddof=1))},
                      "null_change_top10": {"mean": float(np.mean(d10)), "sd": float(np.std(d10, ddof=1))},
                      "null_active_growth": float(np.mean(act)),
                      "mechanical_fraction_top1": float(np.mean(d1)) / o1 if o1 else None,
                      "mechanical_fraction_top10": float(np.mean(d10)) / o10 if o10 else None}
    return out


def main():
    oai = sys.argv[1]
    out_path = sys.argv[2] if len(sys.argv) > 2 else "data/processed/stats/h2_round2.json"
    maths = load([os.path.join(oai, "oai_math_math.jsonl.gz")], lambda c: "maths" if c.startswith("math.") else None)
    phys = load([os.path.join(oai, f"oai_physics_{a}.jsonl.gz") for a in sorted(THEORY)],
                lambda c: "theory" if c in THEORY else None)
    groups = {"maths": maths, "theory_max50_authors": [p for p in phys if len(p["authors"]) <= 50]}
    results = {"notes": __doc__.split("Usage:")[0].strip()}
    for g, papers in groups.items():
        surnames = Counter(a[1] for p in papers for a in p["authors"])
        top1 = set(s for s, _ in surnames.most_common(max(1, len(surnames) // 100)))
        variants = {"all_names": lambda a: True,
                    "full_first_names_no_top1pct_surnames": lambda a, t=top1: a[2] and a[1] not in t}
        res = {}
        for vname, keep in variants.items():
            ind = {}
            for y in range(2020, 2026):
                ind[f"{y}-Q3_to_{y + 1}-Q3"] = independent_window(
                    papers, keep, months_between(f"{y - 1}-07", f"{y}-06"), months_between(f"{y}-07", f"{y}-09"),
                    months_between(f"{y + 1}-07", f"{y + 1}-09"))
                ind[f"{y}-JanAug_to_{y + 1}-JanAug"] = independent_window(
                    papers, keep, months_between(f"{y - 1}-01", f"{y - 1}-12"), months_between(f"{y}-01", f"{y}-08"),
                    months_between(f"{y + 1}-01", f"{y + 1}-08"))
            res[vname] = {"independent_window": ind}
            print(g, vname, "independent window done", flush=True)
        res["all_names"]["uniform_scaling"] = {
            "2025-Q3_to_2026-Q3": uniform_scaling(papers, lambda a: True, months_between("2025-07", "2025-09"),
                                                  months_between("2026-07", "2026-09")),
            "2025-JanAug_to_2026-JanAug": uniform_scaling(papers, lambda a: True, months_between("2025-01", "2025-08"),
                                                          months_between("2026-01", "2026-08"))}
        print(g, "simulation done", flush=True)
        results[g] = res
    json.dump(results, open(out_path, "w"), indent=1, default=float)
    print("written", out_path)


if __name__ == "__main__":
    main()
