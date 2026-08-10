# Informe matematico inicial

## 1. Pregunta y limites

Este estudio pregunta por familias finitas de esferas exteriores unitarias que rodean una esfera central de radio `epsilon`, y por transiciones cuidadosamente tipadas entre representantes de cardinalidades distintas. El objeto no es una teoria de personas, lenguaje, clinica o eficacia; es geometria euclidea discreta.

**[DEFINICION_PROPUESTA]** Se fija `R = 1` para cada esfera exterior y se escribe

\[
C_n(\varepsilon)=(S_0(\varepsilon),S_1(1),\ldots,S_n(1)),\qquad \|p_i\|=1+\varepsilon.
\]

Las exteriores no se solapan cuando \(\|p_i-p_j\|\geq 2\). Para direcciones unitarias \(u_i=p_i/(1+\varepsilon)\), si \(d_{\min}=\min_{i<j}\|u_i-u_j\|\), el infimo permitido es

\[
\varepsilon_*=\max\{0,2/d_{\min}-1\}.
\]

La configuracion realizada requiere `epsilon > 0`; por ello, \(\varepsilon_*=0\) es un infimo, no una esfera central de radio cero aceptada por la definicion.

## 2. Contacto, holgura y codigo esferico

**[DEFINICION_PROPUESTA]** Para dos esferas, \(\delta_{ij}=\|p_i-p_j\|-(r_i+r_j)\):

| Valor de \(\delta_{ij}\) | Lectura geometrica |
|---:|---|
| \(>0\) | Separacion |
| \(=0\) | Tangencia exacta |
| \(<0\) | Solapamiento fisico |

**[DERIVACION_SIMBOLICA]** Si \(\theta_{ij}\) es el angulo entre direcciones,

\[
\|p_i-p_j\|=2(1+\varepsilon)\sin(\theta_{ij}/2),
\quad
\theta_{ij}\geq2\arcsin\!\left(\frac1{1+\varepsilon}\right).
\]

Por tanto cada configuracion inducida por direcciones unitarias es un problema de codigo esferico con umbral angular. Esta reduccion es exacta dentro del modelo cosferico definido; no clasifica todos los empaquetamientos locales no cosfericos.

## 3. Casos de arranque

**[DERIVACION_SIMBOLICA]** Los siguientes umbrales salen de las cuerdas minimas de representantes simetricos. Las cifras que aparecen al ejecutar el programa se etiquetan separadamente como `RESULTADO_COMPUTADO`.

| `n` | Representante | \(d_{\min}\) unitario | \(\varepsilon_*\) | Alcance |
|---:|---|---:|---:|---|
| 2 | Par antipodal | \(2\) | \(0\) | Centracion debil: rango affine 1 |
| 4 | Tetraedro regular | \(\sqrt{8/3}\) | \(\sqrt{3/2}-1\) | Centrado tridimensional |
| 4 | Cuadrado ecuatorial | \(\sqrt2\) | \(\sqrt2-1\) | Testigo de transicion; rango affine 2 |
| 6 | Octaedro regular | \(\sqrt2\) | \(\sqrt2-1\) | Entorno SC |
| 12 | Cuboctaedro | \(1\) | \(1\) | Primera capa FCC |
| 12 | Anticuboctaedro local HCP | \(1\) | \(1\) | Primera capa HCP |
| 12 | Icosaedro regular | \(4/\sqrt{10+2\sqrt5}\) | \(\sqrt{10+2\sqrt5}/2-1\) | Comparador de codigo, no capa de esferas unitarias en contacto entre si a \(\varepsilon=1\) |

La configuracion `n=12` no se reduce a una unica geometria: FCC y HCP tienen doce vecinos a distancia de contacto, pero sus grafos y apilamientos globales difieren. La etiqueta de `HCP` en este estudio es una red periodica con base, no una red de Bravais simple.

## 4. Redes reticulares y empaquetamientos periodicos

| Red | Tipo en el modelo | Coordinacion | Fraccion de empaquetamiento de esferas congruentes | Nota |
|---|---|---:|---:|---|
| SC | Bravais | 6 | \(\pi/6\) | Vecindad octaedrica |
| FCC | Bravais | 12 | \(\pi/(3\sqrt2)\) | Tiene primera capa cuboctaedrica |
| HCP | Periodica con base | 12 | \(\pi/(3\sqrt2)\) | Apilamiento ABAB; no se etiqueta como Bravais simple |
| BCC | Bravais | 8 | \(\sqrt3\pi/8\) | Referencia comparativa, no empaquetamiento maximo |

**[RESULTADO_CLASICO]** La cota global de densidad de empaquetamientos congruentes en \(\mathbb R^3\) es \(\pi/\sqrt{18}=\pi/(3\sqrt2)\), alcanzada por empaquetamientos de tipo FCC (y dentro de la familia de apilamientos compactos pertinentes). La demostracion de Hales aborda densidad global; no implica que un representante local dado sea rigido ni que una transicion discreta este permitida.

## 5. Transiciones: una taxonomia que evita el salto indebido

**[DEFINICION_PROPUESTA]** Una expresion `n -> n+2` es incompleta hasta fijar una clase:

1. `INCLUSION_LITERAL_DE_DIRECCIONES`: las direcciones antiguas son un subconjunto del nuevo representante.
2. `INCLUSION_HASTA_ISOMETRIA`: existe una isometria que hace posible la inclusion.
3. `DEFORMACION_CONTINUA`: se permite mover centros siguiendo restricciones declaradas.
4. `REOPTIMIZACION_INDEPENDIENTE`: solo se comparan dos optimos o candidatos; no hay preservacion.

**[RESULTADO_COMPUTADO]** El script verifica un testigo de inclusion literal para `par antipodal -> cuadrado ecuatorial -> octaedro` cuando se usa el radio objetivo y se comprueba no solapamiento. Tambien informa que el tetraedro seleccionado no es subconjunto literal del octaedro seleccionado, ni el octaedro de la capa cuboctaedrica FCC seleccionada.

**[REFUTADO_POR_CONTRAEJEMPLO]** La proposicion fuerte “todo paso entre dos cardinalidades con diferencia dos preserva literalmente la configuracion simetrica escogida” es falsa: tetraedro regular `n=4` no aparece como subconjunto literal de los vertices del octaedro regular `n=6` del modelo. Esto no refuta transiciones con rotacion, deformacion o reoptimizacion.

**[PENDIENTE_DE_VERIFICACION]** Rigidez, jamming, conectividad de espacios de configuracion y criterios de estabilidad necesitan un marco adicional (contacto activo, restricciones infinitesimales y, si procede, una prueba o algoritmo certificado).

## 6. Vacios: resultados exactos y riesgos de analogia

**[DERIVACION_SIMBOLICA]** Si tres exteriores unitarias son mutuamente tangentes y sus centros forman un triangulo equilatero de lado 2, el radio de una esfera que cabe en el hueco tetraedrico respecto de cuatro centros equivalentes satisface

\[
r_{tetra}/R=\sqrt{3/2}-1.
\]

Para el hueco octaedrico regular, \(r_{octa}/R=\sqrt2-1\). Estas identidades son geometricas para modelos ideales de esferas congruentes; no autorizan a denominar “hueco” a toda separacion, ni a extrapolar a redes no regulares.

## 7. Que ha quedado demostrado, computado y abierto

| Etiqueta | En esta primera version |
|---|---|
| `DEMOSTRADO_EN_ESTE_TRABAJO` | Solo correccion de las identidades implementadas respecto de las pruebas unitarias, condicionado a la ejecucion mostrada. |
| `RESULTADO_COMPUTADO` | Valores para siete conjuntos finitos y cuatro consultas de transicion en `data/results_initial.*`. |
| `OBSERVACION_VISUAL` | Proyecciones SVG, sin inferencia de profundidad ni de rigidez. |
| `CONJETURA` | No se promueve ninguna como resultado. |
| `PENDIENTE_DE_VERIFICACION` | Optimos generales para cada familia, transiciones deformables, jamming, y pruebas asistidas/certificadas. |

## 8. Siguientes experimentos defendibles

1. Formular un problema de factibilidad semialgebraico para cada tipo de transicion, con tolerancias y certificado de error.
2. Implementar grafo de contactos, rango de rigidez y separacion entre rigidez infinitesimal y jamming colectivo.
3. Separar optimizacion de codigos esfericos de densidad de empaquetamiento periodico.
4. Introducir Voronoi/Delaunay solo con una biblioteca versionada y pruebas de degeneracion coplanar/cosferica.
5. Comparar HCP y FCC por grafos locales y por condiciones periodicas, sin colapsarlas en el mismo objeto.
