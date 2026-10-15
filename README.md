# academia-ia-state

Estudio del estado de la academia (publicaciones, ayudas y becas) y del impacto de los LLM en todas las disciplinas.

## Contenido

| Ruta | Qué es |
|---|---|
| `docs/data-sources-report.md` | Catálogo de fuentes (en inglés): qué mide cada fuente, cobertura histórica, acceso, coste, rupturas conocidas y una estrategia para separar el efecto de los LLM de otros factores. |
| `docs/research-notes/` | Notas de investigación con todas las citas en las que se basa el informe. Las rutas a `/tmp/...` que aparecen en ellas son de la sesión de trabajo y no se conservan. |
| `dashboards/preprints-por-campo/` | Código del panel «Preprints por campo». |
| `data/raw/` | Datos descargados de las fuentes, sin transformar. |
| `data/processed/` | Series trimestrales listas para usar. |
| `scripts/` | Scripts para descargar y regenerar los datos. |

## Preprints nuevos por trimestre (desde 2020-T1)

`data/processed/preprints_por_campo_trimestral.csv` tiene una fila por trimestre completo.

| Columna | Fuente | Qué cuenta |
|---|---|---|
| `fisica` | arXiv | Envíos nuevos cuyo archivo principal es de física: astro-ph, cond-mat, gr-qc, hep-ex, hep-lat, hep-ph, hep-th, math-ph, nlin, nucl-ex, nucl-th, physics y quant-ph. |
| `matematicas` | arXiv | Envíos nuevos con archivo principal math. |
| `biologia_biorxiv` | bioRxiv | `new_papers` del resumen mensual oficial (sin revisiones). |
| `medicina_medrxiv` | medRxiv | `new_papers` del resumen mensual oficial (sin revisiones). |
| `ciencias_sociales` | Suma | psyarxiv + socarxiv + edarxiv + arxiv_econ_finanzas. |
| `psyarxiv`, `socarxiv`, `edarxiv` | OSF | Preprints nuevos (solo primeras versiones) por fecha de creación. |
| `arxiv_econ_finanzas` | arXiv | Envíos nuevos con archivo principal econ o q-fin. |
| `informatica_referencia` | arXiv | Envíos nuevos con archivo principal cs; solo como referencia. |

Los conteos de arXiv salen de las páginas de estadísticas anuales por archivo (`https://arxiv.org/year/<archivo>/<año>`), que dan envíos nuevos y listados cruzados por mes. Solo se usan los envíos nuevos.

### Advertencias

- **Un preprint no es una publicación.** La adopción del preprint varía mucho por campo (casi universal en física y matemáticas, parcial en biología y medicina, minoritaria en ciencias sociales). Compara la evolución de cada campo, no los niveles entre campos.
- **Ciencias sociales es una muestra pequeña.** Faltan SSRN y RePEc, porque no se pudieron obtener recuentos trimestrales fiables.
- **Alias de arXiv.** La suma de todos los archivos supera el total mensual oficial en torno a un 5 %, porque algunas categorías son alias entre dos archivos (math-ph/math.MP, cs.IT/math.IT, math.ST/stat.TH, cs.NA/math.NA, eess.SY/cs.SY, econ.GN/q-fin.EC). `parse_arxiv.py` imprime la diferencia mes a mes.
- **Versiones en OSF.** Desde principios de 2025, la API de OSF devuelve cada versión como un registro aparte (`<id>_vN`). `osf_quarterly.py` usa el total de la API hasta 2024 y, desde 2025, pagina los registros y cuenta solo `_v1`.
- **Rupturas conocidas.**
  - COVID-19 en 2020–2021, sobre todo en medRxiv.
  - Cambios de normas de arXiv entre octubre de 2025 y octubre de 2026:
    - artículos de revisión y de posición en informática;
    - aval de autores nuevos;
    - versión completa en inglés;
    - límite de envíos por persona desde el 1 de octubre de 2026.
  - Septiembre de 2026 es el mes récord de arXiv.
  - SocArXiv exigió ORCID y derivó las humanidades a otro repositorio en noviembre de 2025.

## Regenerar los datos

```bash
scripts/fetch_arxiv_years.sh /tmp/arxiv_years            # páginas anuales por archivo (no se versionan)
python3 scripts/parse_arxiv.py /tmp/arxiv_years data/raw/arxiv_archive_monthly.csv
cp /tmp/arxiv_years/monthly_submissions.csv data/raw/arxiv_monthly_submissions.csv
scripts/fetch_biorxiv_medrxiv.sh data/raw
python3 scripts/osf_quarterly.py data/raw/osf_quarterly.csv   # lento: pagina los registros desde 2025
python3 scripts/build_datasets.py data
```

`build_datasets.py` conserva solo trimestres completos, desde 2020-T1 hasta el último trimestre cerrado antes de la fecha en que se ejecuta. `scripts/osf_check_quarter.py <servidor> <desde> <hasta>` sirve para comprobar a mano un trimestre de OSF.
