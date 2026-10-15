# Panel «Preprints por campo»

Panel publicado en Claude: https://claude.ai/artifact/TnuLTHyf9AnkWdJxBQPC58 (privado hasta que se comparta desde su menú Share).

`index.html` es la página del panel. Se ejecuta dentro del tipo de artifact «Dashboard» de Claude, que aporta `dash` (datos y fuentes) y `d3`, así que no funciona abierta como archivo suelto.

## Fuentes del panel

| Id en el panel | Archivo | Contenido |
|---|---|---|
| `arxiv_campos` | `data/processed/arxiv_campos_trimestral.json` | arXiv: física, matemáticas, economía y finanzas, informática |
| `biorxiv_medrxiv` | `data/processed/biorxiv_medrxiv_trimestral.json` | bioRxiv y medRxiv |
| `osf_sociales` | `data/processed/osf_sociales_trimestral.json` | PsyArXiv, SocArXiv y EdArXiv |

Cálculos definidos en la página:

- `trimestral` une las tres fuentes.
- `indice_2022` divide cada trimestre por la media trimestral de 2022 del mismo campo.
- `cambio_vs_2022` compara los cuatro trimestres más recientes con el total de 2022.

## Actualizar

Regenera los datos con los scripts de `scripts/` (ver el README principal) y pide a Claude que suba los tres JSON nuevos al panel.
