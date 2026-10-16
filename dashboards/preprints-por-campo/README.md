# Panel «Preprints by Field»

Panel publicado en Claude: https://claude.ai/artifact/TnuLTHyf9AnkWdJxBQPC58 (privado hasta que se comparta desde su menú Share).

`index.html` es la página del panel. Se ejecuta dentro del tipo de artifact «Dashboard» de Claude, que aporta `dash` (datos y fuentes) y `d3`, así que no funciona abierta como archivo suelto.

## Fuentes del panel

| Id en el panel | Archivo | Contenido |
|---|---|---|
| `arxiv_fields` | `data/processed/arxiv_fields_quarterly.json` | arXiv: física, matemáticas, economía y finanzas, informática |
| `biorxiv_medrxiv` | `data/processed/biorxiv_medrxiv_quarterly.json` | bioRxiv y medRxiv (total, COVID-19 y sin COVID-19) |
| `osf_social` | `data/processed/osf_social_quarterly.json` | PsyArXiv, SocArXiv y EdArXiv |
| `arxiv_cs_split` | `data/processed/arxiv_cs_ai_split_quarterly.csv` | Informática de arXiv: investigación en IA y resto |

Cálculos definidos en la página:

- `quarterly` une las tres fuentes.
- `index_2022` divide cada trimestre por la media trimestral de 2022 del mismo campo.
- `yoy_growth` compara cada trimestre con el mismo trimestre del año anterior.
- `change_vs_2022` compara los cuatro trimestres más recientes con el total de 2022.
- `cs_index_2022` pone en índice (2022 = 100) la informática con y sin IA, junto a física y matemáticas.

## Actualizar

Regenera los datos con los scripts de `scripts/` (ver el README principal) y pide a Claude que suba los tres JSON nuevos al panel.
