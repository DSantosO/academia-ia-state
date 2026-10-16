# Propuesta: cómo mejorar las gráficas de papers

16 de octubre de 2026.
- **Prototipos:** `docs/figures/proposal/`, generados con `scripts/analyze_trends.py` y `scripts/plot_proposal.py` a partir de datos reales: arXiv por archivo desde 2010, bioRxiv y PubMed.
- **Referencias:** las de la sección 1 se comprobaron en la fuente primaria salvo que se indique otra cosa.

## Resumen

**1. Hay tres preguntas distintas y cada una pide su métrica.** Con nuestros datos de enero a septiembre de 2026, dan respuestas distintas:

| Pregunta | Métrica de la literatura | Física | Matemáticas | Informática |
|---|---|---|---|---|
| ¿Crece más de lo que venía creciendo? | Exceso sobre la tendencia propia previa a ChatGPT | +31 % (+26 a +35) | +47 % (+27 a +60) | +5 % (−33 a +39) |
| ¿Crece más que el resto de arXiv, frente a lo habitual? | Brecha de crecimiento con el resto de arXiv, menos la brecha media de 2015–2022 | −4 pp | +21 pp | −8 pp |
| ¿Acelera más la teoría que el experimento? | Gradiente entre archivos (P3) | Teoría +16 % a +43 %; experimento +2 % a +14 % | | |

Entre paréntesis, el rango con tres ventanas de ajuste distintas.

**2. Lo que se mantiene de la hipótesis de la ola:**
- arXiv acelera en conjunto: la suma de archivos crece un 16 % en enero–septiembre de 2025 y un 30 % en enero–septiembre de 2026, siempre frente al mismo periodo del año anterior.
- 14 de los 20 archivos crecen más en 2026 que en 2025.
- Biología y medicina no aceleran, ni en preprints (bioRxiv +12 %) ni en artículos publicados (PubMed +5 %).

**3. Lo que no se sostiene:** que «informática va por delante porque es la más expuesta».
- Su crecimiento de 2023–2025 (+23 % a +28 % al año) es el mismo que en 2016–2020, antes de ChatGPT.
- En 2026 su ventaja sobre el resto de arXiv es menor que la habitual.
- Hay un matiz: desde el 31 de octubre de 2025 arXiv ya no acepta en informática artículos de revisión ni de posición sin revisión por pares previa, lo que resta artículos justo en el margen más sensible a los LLM.

**4. Lo que mejor encaja con los datos:** la aceleración va por tipo de trabajo antes que por campo.
- Primero el trabajo teórico, cuyo cuello de botella es razonar y escribir.
- Matemáticas es el único campo que destaca con las tres métricas.
- Encaja con Nee, Zhong y Ni (2026), que llaman al fenómeno «fiebre del oro» en la investigación teórica y computacional.

**5. Cambios en las gráficas, por orden de importancia:**
1. Gráfico principal: crecimiento frente al rango histórico de cada campo (P4). Es sencillo y no depende de un modelo.
2. Gráficos de apoyo:
   - el exceso sobre la tendencia propia, con intervalo (P1, P2);
   - la brecha con los demás campos (control sintético).
3. El gradiente dentro de cada campo (P3).
4. Separar la adopción del preprint de la producción, con PubMed y, si tenemos clave, OpenAlex.
5. Descomponer el crecimiento en autores × artículos por autor, con conteo fraccionario, y medir la concentración con los umbrales de la literatura.
6. Uso de LLM por campo, para cruzarlo con la aceleración.

**6. Para el ensayo:** la Figura 3 prevista es el índice 2022 = 100 (nuestra fig1). Por sí sola sugiere que informática es el campo más afectado. Recomiendo sustituirla por P4 o, como mínimo, añadir esta advertencia al pie.

## 1. Qué métricas usa la comunidad

| Familia | Qué se mide | Referencias | Uso aquí |
|---|---|---|---|
| Crecimiento a largo plazo | Tasa anual y tiempo de duplicación con regresión log-lineal por tramos y rupturas estimadas a partir de los datos. La ciencia crece en torno al 4 % al año y se duplica cada 17 años; la tasa depende de la ventana. | Bornmann y Mutz 2015 ([JASIST](https://doi.org/10.1002/asi.23329)); Bornmann, Haunschild y Mutz 2021 ([HSSC](https://doi.org/10.1057/s41599-021-00903-w)) | P1 ajusta tendencias log-lineales. Falta estimar la fecha de ruptura de cada campo en vez de imponerla. |
| Unidad y método de recuento | Recuento completo frente a fraccionario: con recuento completo no hay normalización por campo correcta. NSF cuenta por fracción de autores, publica un índice por campo (2010 = 100) y cuotas del total mundial. | Waltman y van Eck 2015 ([JoI](https://doi.org/10.1016/j.joi.2015.08.001)); [NSF Indicators 2026](https://ncses.nsf.gov/pubs/nsb20257/publication-output-by-geography-and-scientific-field) | Ya contamos cada artículo una vez, por archivo principal y solo primeras versiones. Los alias de arXiv suman ~5 % de más. |
| Exceso sobre lo esperado | Observado / esperado − 1, con la lógica del exceso de mortalidad. | Kobak et al. 2025 ([Sci. Adv.](https://doi.org/10.1126/sciadv.adt3813)); Nee, Zhong y Ni 2026 ([arXiv 2609.04872](https://arxiv.org/abs/2609.04872)) | P1 y P2. Nee et al. ajustan una tendencia log-lineal con efectos de mes entre enero de 2018 y noviembre de 2022. |
| Series temporales interrumpidas | Regresión segmentada con cambio de nivel y de pendiente, modelo de Poisson para recuentos, términos estacionales, errores robustos a autocorrelación y una serie de control. | Bernal, Cummins y Gasparrini 2017 ([IJE](https://doi.org/10.1093/ije/dyw098)) | Falta pasar P1 a Poisson o binomial negativa con errores HAC. |
| Brecha comparativa | Control sintético: compara el campo con una combinación ponderada de otros campos que lo imitaba antes. | Abadie, Diamond y Hainmueller 2010 ([JASA](https://doi.org/10.1198/jasa.2009.ap08746)); Nee et al. 2026 | Nee et al. dan a matemáticas una brecha de +11,9 % en enero–agosto de 2026 (rango 9,6–14,9 %; placebo p = 1/15). Aquí hay una versión simple frente al resto de arXiv (sección 3.3). |
| Productividad y equipos | Artículos por autor con recuento fraccionario. Con ese recuento, la productividad individual no subió en un siglo. Los equipos de ciencia e ingeniería pasaron de 1,9 a 3,5 autores. | Fanelli y Larivière 2016 ([PLoS ONE](https://doi.org/10.1371/journal.pone.0149504)); Wuchty, Jones y Uzzi 2007 ([Science](https://doi.org/10.1126/science.1136099)) | Falta. Requiere autores por artículo (descarga OAI). |
| Productividad extrema | Autores con más de 72 artículos en un año (2018) o más de 60 (2024). Nee et al. miden la cuota de autores de matemáticas con 5 o más envíos (2,45 % → 3,80 %) y con 10 o más (0,21 % → 0,49 %). | Ioannidis, Klavans y Boyack 2018 ([Nature](https://doi.org/10.1038/d41586-018-06185-8)); Ioannidis, Collins y Baas 2024 ([Scientometrics](https://doi.org/10.1007/s11192-024-05117-w)) | Nuestro indicador (artículos con un autor de 5 o más en el trimestre) no es comparable. Propongo cuotas de autores con ≥5, ≥10 y >15 artículos por trimestre (este último equivale a >60 al año). |
| Presión sobre el sistema | Artículos por investigador o por doctor, números especiales, tiempos de revisión, tasas de rechazo. Entre 2016 y 2022, los artículos de Scopus y WoS crecieron un 47 %. | Hanson, Barreiro, Crosetto y Brockington 2024 ([QSS](https://doi.org/10.1162/qss_a_00327)) | Sin denominadores trimestrales por campo. Para arXiv, lo más parecido es la carga de moderación que publica arXiv. |
| Adopción del preprint | Preprints / (preprints + artículos), o porcentaje de artículos con preprint. Este último, en 2021–2022 (subestimado según sus autores): matemáticas 27 %, física 20 %, informática 12 %, biología 9 %, psicología 7 %, medicina 4–5 %, economía 4 %. En ciencias de la vida, los preprints pasaron de menos del 1 % (2016) al 10,7 % (2023). | Xie, Shen y Wang 2021 ([arXiv](https://arxiv.org/abs/2102.09066)); Abdill y Blekhman 2019 ([eLife](https://doi.org/10.7554/eLife.45133)); Rzayeva, Pinfield y Waltman 2025–26 ([SocArXiv](https://doi.org/10.31235/osf.io/xdwc4_v2)); Levchenko et al. 2024 ([PLoS ONE](https://doi.org/10.1371/journal.pone.0303005)) | Con PubMed ya descargado se puede calcular para biomedicina. |
| Uso de LLM | Vocabulario en exceso: al menos el 13,5 % de los resúmenes de PubMed de 2024. Contenido modificado por LLM: hasta un 22 % en informática. Uso sustancial declarado en matemáticas: del 1,4 % al 14,1 % entre marzo y agosto de 2026. | Kobak et al. 2025; Liang et al. 2025 ([NHB](https://doi.org/10.1038/s41562-025-02273-8)); Jin, Ke y Sui 2026 ([arXiv 2608.24961](https://arxiv.org/abs/2608.24961)) | Falta. Sería el eje de «exposición» por campo. |
| Efecto por autor | Diferencias en diferencias con autores que adoptan LLM: +36 % de artículos en arXiv, +53 % en bioRxiv, +60 % en SSRN. Hay una crítica metodológica: datar la adopción por la primera detección selecciona meses de alta producción, y los placebos reproducen el efecto. Con IA en sentido amplio, los científicos que la usan publican 3,02 veces más, pero el conjunto de temas estudiados se estrecha un 4,6 %. | Kusumegi et al. 2025 ([Science](https://doi.org/10.1126/science.adw3000)); Renault, Bergeaud y Bosquet 2026 ([arXiv](https://arxiv.org/abs/2605.17979)); Hao et al. 2026 ([Nature](https://doi.org/10.1038/s41586-025-09922-y)) | Son multiplicadores por persona, no crecimiento agregado. |
| Principios | Manifiesto de Leiden: tener en cuenta las diferencias entre campos (P6); mostrar la incertidumbre y evitar la falsa precisión (P8); los indicadores cambian conductas (P9), como hacen los límites de envío. | Hicks et al. 2015 ([Nature](https://doi.org/10.1038/520429a)) | Intervalos en P1 y P2. Aviso del 1 de octubre ya añadido. |

**Cómo grafican los productores de indicadores** (solo lo que se pudo ver):
- **NSF:** recuentos anuales, un índice por campo (2010 = 100) y cuotas del total mundial.
- **Stanford AI Index:** escala lineal con cuotas.
- **arXiv:** recuentos mensuales sin ajuste estacional, omitiendo el mes en curso.

Ninguno usa ajuste estacional; la práctica habitual es comparar con el mismo periodo del año anterior. El índice es, por tanto, un formato aceptado para describir. Lo que no permite es atribuir.

## 2. Qué falla en las gráficas actuales

| Gráfico | Problema | Mejora |
|---|---|---|
| Fig. 1, índice 2022 = 100 | Sirve para describir (NSF usa uno igual), pero mezcla la tendencia previa con el cambio. Depende del año base (en medicina, 2022 está deprimido por la COVID-19). No muestra incertidumbre. | Como gráfico principal, el crecimiento frente al rango histórico (P4). El índice puede quedarse como gráfico descriptivo, en escala logarítmica y desde 2015. |
| Fig. 2, crecimiento interanual | Es la métrica que más se usa, pero sin referencia no dice si un +26 % es normal en ese campo. Los efectos base de 2020–2021 dominan el principio. | La banda del rango previo de cada campo, como en P4, y sumas móviles de cuatro trimestres para quitar ruido. |
| Fig. 3, recuentos por campo | Escalas lineales distintas en cada panel. Empieza en 2020, sin historia. | Escala logarítmica, en la que la pendiente es la tasa de crecimiento, desde 2015 y con la tendencia previa (P1). |
| Fig. 4–6, matemáticas | Sin referencia histórica por subárea. El umbral de autor prolífico es propio. | Crecimiento previo de cada subárea (como P3) y los umbrales de la literatura (sección 1). |
| Fig. 7, informática con y sin IA | No hay tendencia previa de la informática sin IA porque la serie empieza en 2020. La clasificación por vocabulario se desplaza: cuantos más artículos mencionan LLM, más pasan al grupo de IA. | Ampliar la descarga a 2015 y calcular el exceso de cada grupo. Repetir con la clasificación solo por categoría. |
| Todos | Las líneas de lanzamientos sugieren causa. | Bandas para los regímenes de reglas (octubre 2025 – octubre 2026) y una marca donde la serie sale de su intervalo de predicción. |

## 3. Prototipos con datos reales

### 3.1 Crecimiento frente al rango histórico (P4)

Crecimiento anual de cada campo frente a su rango hasta 2022. No necesita modelo.

| Campo | Rango hasta 2022 | 2023 | 2024 | 2025 | 2026* |
|---|---|---|---|---|---|
| Física | −1 % a +7 % (2011–2022) | +5 % | +8 % | +12 % | +20 % |
| Matemáticas | −2 % a +14 % (2011–2022) | +5 % | +9 % | +6 % | +43 % |
| Informática | +5 % a +40 % (2011–2022) | +24 % | +28 % | +23 % | +35 % |
| Biomedicina (PubMed) | 0 % a +15 % (2016–2022) | −3 % | +4 % | +11 % | +5 % |

\*Enero–septiembre frente a enero–septiembre de 2025.

![Crecimiento frente al rango histórico](figures/proposal/p4_growth_corridor.png)

### 3.2 Exceso sobre la tendencia propia (P1, P2)

**Método** (el de Nee et al. 2026, con trimestres en vez de meses):
- regresión del logaritmo de los papers por trimestre sobre una tendencia lineal y efectos de trimestre;
- ajuste antes de ChatGPT, dejando fuera los trimestres de la COVID-19 (2020-T2 a 2021-T1), y proyección hacia delante;
- exceso = observado / esperado − 1, con intervalo de predicción del 95 %;
- tres ventanas de ajuste: 2015–2022 (principal), 2015–2019 y 2018–2022.

| Campo | Enero–septiembre 2026 | Solo T3 2026 (intervalo, ventana principal) | Tendencia 2015–2022 |
|---|---|---|---|
| Física | +31 % (+26 a +35) | +44 % [+36, +52] | +2,9 % al año |
| Matemáticas | +47 % (+27 a +60) | +92 % [+78, +108] | +3,0 % al año |
| Informática | +5 % (−33 a +39) | +12 % [−11, +40] | +22,5 % al año |
| Biología (bioRxiv)† | −15 % | −15 % [−47, +35] | — |
| Biomedicina (PubMed) | −5 % (−15 a +15) | −8 % [−18, +3] | +5,5 % al año |

†Solo con la ventana 2018–2022. Antes, bioRxiv aún se estaba adoptando y los preprints nuevos se duplicaban cada año, así que no hay tendencia que extrapolar.

**Comparación con Nee et al.** Con el mismo método, dan a matemáticas en enero–agosto de 2026 un exceso del 36,8 % si ajustan desde 2018 y del 62,1 % si ajustan desde 2020. Nuestro rango es del 27 % al 60 %.

**Cuándo sale cada serie de su intervalo** (primer trimestre desde el que el límite inferior queda siempre por encima de cero):

| Campo | 2015–2022 | 2015–2019 | 2018–2022 |
|---|---|---|---|
| Física | 2025-T1 | 2025-T3 | 2024-T2 |
| Matemáticas | 2025-T3 | 2026-T2 | 2024-T1 |
| Informática | no sale | no sale | 2026-T1 |
| bioRxiv | — | — | no sale |
| PubMed | no sale | 2025-T1 | no sale |

![Tendencia propia por campo](figures/proposal/p1_trend_by_field.png)

![Exceso sobre la tendencia](figures/proposal/p2_excess_over_trend.png)

### 3.3 Brecha con el resto de arXiv

Crecimiento de cada campo menos el del resto de arXiv, en puntos porcentuales. La versión rigurosa es el control sintético de Nee et al.; esta es una aproximación simple.

| Campo | Media 2015–2022 (sin 2020–21) | 2023 | 2024 | 2025 | 2026* | 2026 frente a la media |
|---|---|---|---|---|---|---|
| Física | −10 | −11 | −14 | −6 | −14 | −4 |
| Matemáticas | −5 | −9 | −10 | −12 | +16 | +21 |
| Informática | +17 | +19 | +18 | +12 | +9 | −8 |

\*Enero–septiembre frente a enero–septiembre de 2025.

**Lectura.**
- Gran parte del exceso de física es común a todo arXiv.
- Matemáticas es el único campo que en 2026 rompe su relación habitual con el resto.
- Informática pesa casi la mitad de arXiv, así que «el resto» no es un control neutro para los demás campos. Por eso hace falta el control sintético.

### 3.4 Gradiente por archivo de arXiv (P3)

Crecimiento de enero–septiembre de 2026 frente al mismo periodo de 2025, con el de 2025 y el crecimiento anual compuesto de 2017–2022 como referencia.

- **Teóricos (lápiz y papel):**
  - matemáticas +43 %;
  - física matemática +39 %;
  - teoría de altas energías +24 %;
  - relatividad general +21 %;
  - fenomenología +18 %;
  - teoría nuclear +16 %.
- **Experimentales:** altas energías +14 %, nuclear +2 %.
- **Computacional:** teoría de campos en el retículo +6 %.
- **Otros:**
  - física cuántica +39 %;
  - estadística +38 %;
  - informática +35 %;
  - materia condensada +18 %;
  - astrofísica +15 %;
  - biología cuantitativa −7 %.

Todos los archivos teóricos crecen más que los dos experimentales, aunque la diferencia entre teoría nuclear y altas energías experimental es pequeña (+16 % frente a +14 %). Los seis archivos que crecen menos en 2026 que en 2025 son aplicados, experimentales o computacionales:
- economía;
- finanzas cuantitativas;
- teoría de campos en el retículo;
- ingeniería eléctrica;
- física nuclear experimental;
- biología cuantitativa.

**Límites.**
- Los archivos experimentales son pequeños: 346 y 933 artículos en 2026.
- Física matemática comparte categorías alias con matemáticas.
- Estadística incluye aprendizaje automático (stat.ML).
- Física cuántica vive su propio auge.
- La división entre teóricos y experimentales es una hipótesis mía, no una categoría oficial.

![Crecimiento por archivo](figures/proposal/p3_growth_by_archive.png)

## 4. Qué cambia en la conclusión de la ola

- **Se mantiene:**
  - hay una aceleración amplia en arXiv: 14 de 20 archivos crecen más en 2026 que en 2025;
  - matemáticas y física teórica la muestran con claridad;
  - biología y medicina no la muestran, ni en preprints ni en PubMed.
- **No se sostiene con estos datos:** que informática vaya por delante.
  - Su agregado sigue la tendencia que traía del aprendizaje profundo.
  - Frente al resto de arXiv, su ventaja en 2026 es menor que la habitual. Parte de eso puede deberse a la regla de arXiv de octubre de 2025 sobre artículos de revisión y de posición.
  - La prueba buena es la informática sin IA con una tendencia previa larga, que exige ampliar la descarga a 2015.
- **Más precisa:** el orden parece ir por tipo de trabajo:
  - primero la teoría, que es el trabajo de lápiz y papel;
  - el trabajo experimental o de cálculo intensivo, después o todavía no.
- **Por separar:** la aceleración común de arXiv (+30 % en 2026) puede ser la propia ola o deberse a factores de la plataforma. El informe anual de arXiv cita más envíos de estudiantes y más contenido de baja calidad generado con IA.

## 5. Plan propuesto

| # | Cambio | Datos | Esfuerzo | Estado |
|---|---|---|---|---|
| 1 | Crecimiento frente al rango histórico (P4) como gráfico principal | Ya descargados | Bajo | Prototipo hecho |
| 2 | Exceso sobre la tendencia (P1, P2), pasado a Poisson o binomial negativa con errores HAC y fecha de ruptura estimada | Ya descargados | Bajo-medio | Prototipo hecho |
| 3 | Control sintético por archivo, como Nee et al., con placebos | Ya descargados (20 archivos desde 2010) | Medio | — |
| 4 | Gradiente por archivo (P3) y, después, por subárea de matemáticas e informática; contrastes dentro de biología y física | Ya descargados | Bajo | Hecho para bioRxiv, medRxiv y física (fig8, fig9) |
| 5 | Cociente entre preprints y artículos en biomedicina, con PubMed | Ya descargados | Bajo | Datos listos |
| 6 | Informática sin IA desde 2015, con exceso sobre tendencia | Descarga OAI de cs desde 2015 (horas) | Medio | — |
| 7 | Autores × artículos por autor (fraccionario), tamaño de equipo y cuotas de autores con ≥5, ≥10 y >15 artículos por trimestre | Descarga OAI de math, cs y física (horas) | Medio-alto | — |
| 8 | Uso de LLM por campo (vocabulario en exceso) y gráfico de dosis y respuesta: uso frente a exceso de crecimiento | Resúmenes de arXiv (OAI) y de bioRxiv y medRxiv (API) | Medio-alto | — |
| 9 | Artículos publicados en todas las disciplinas (OpenAlex) | Clave de API, que requiere tu correo | Medio | Pendiente de tu decisión |
| 10 | Ciencias sociales: SSRN desde Crossref, con sus rupturas documentadas | Crossref, sin clave | Medio | — |

## 6. Decisiones

1. ¿Uso P4 como gráfico principal del panel y del ensayo, con el exceso sobre tendencia y la brecha comparativa como apoyo? Recomiendo que sí.
2. ¿Aviso a la sesión del ensayo de que su Figura 3 (índice 2022 = 100) sugiere que informática es el campo más afectado y que P4 lo evita?
3. ¿Hago la versión para publicación de fig7 que pide la sesión del ensayo?
4. ¿Lanzo las descargas largas de los puntos 6 a 8? Corren en segundo plano durante horas.
5. Si vas a preparar un Registered Report, conviene fijar las hipótesis a nivel de autor (punto 7) antes de mirar esos datos.
6. OpenAlex: ¿creas tú la clave o me autorizas a pedirla con tu correo?
