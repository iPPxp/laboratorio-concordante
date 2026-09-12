# Intersticios, centros recursivos y capas triangulares/cuadrangulares

**Fecha:** 2026-09-12  
**Estatus:** investigación matemática y computacional independiente  
**Artefactos:** `src/spherepack/interstitial.py`, `src/spherepack/multilevel.py`,
`scripts/run_interstitial_multilevel.py`, pruebas y visualizaciones asociadas.

## 1. Resultado del centro intersticial plano

Para `n` círculos exteriores congruentes de radio `R`, colocados en un anillo
regular, cada exterior toca al centro y a sus dos vecinos. El radio central es:

\[
\frac{r_n}{R}=\csc\left(\frac{\pi}{n}\right)-1.
\]

| `n` | Organización exterior | `r_n/R` | Grafo de contacto con el centro |
|---:|---|---:|---|
| 3 | triángulo | `0.154700538...` | `K4` |
| 4 | cuadrado | `0.414213562...` | `C4 ∨ K1` |
| 5 | pentágono | `0.701301617...` | `C5 ∨ K1` |
| 6 | hexágono | `1` | `C6 ∨ K1` |

Tres es el número mínimo de exteriores que delimitan por sí solos una cavidad
plana acotada. El centro es especialmente pequeño en ese caso. Con dos
exteriores, la tangencia deja una familia continua de posiciones posibles y se
necesita otra relación o frontera para seleccionar una.

### 1.1 El caso de dos: burbuja positiva y límite puntual

El caso `n=2` ya pertenece a la familia centrada original. Sean dos bolas
anfitrionas congruentes de radio `R`, una bola central de radio `r`, y supóngase
que sus tres centros son colineales, con la central exactamente en el punto
medio. Si la central toca a ambas anfitrionas, la distancia `D` entre los
centros exteriores satisface:

\[
D=2(R+r),
\qquad
r=\frac{D-2R}{2}.
\]

Por tanto, para cada `r>0` existe una burbuja central positiva y las dos
anfitrionas quedan separadas por una holgura superficial `2r`. Si
`r=\varepsilon R`, entonces:

\[
D=2R(1+\varepsilon),
\qquad
\varepsilon\downarrow0
\Longrightarrow
D\downarrow2R.
\]

En el límite, las anfitrionas se tocan y la burbuja central se degenera en el
punto de tangencia. Una burbuja **minúscula pero positiva** corresponde a
`0<\varepsilon\ll1`; no es todavía el punto límite `\varepsilon=0`.

Esto no contradice el mínimo `n=3` anterior. Dos anfitrionas, tomadas por sí
solas, no delimitan una cavidad plana acotada ni determinan un radio único. La
solución anterior queda seleccionada al imponer simultáneamente centralidad,
colinealidad y la distancia `D`. Si las dos anfitrionas ya son tangentes y no
se impone colinealidad, existe una familia continua de bolas tangentes a ambas;
su tamaño y posición requieren información adicional.

Para radios exteriores desiguales `R_i`, la ecuación de cierre implementada es:

\[
\sum_i 2\arcsin\sqrt{
\frac{R_iR_{i+1}}
{(r+R_i)(r+R_{i+1})}}
=2\pi.
\]

El programa resuelve `r` por bisección y comprueba por separado los pares no
vecinos.

## 2. El centro que después forma nuevas cavidades

Con tres círculos mutuamente tangentes, el teorema de Descartes admite las dos
raíces:

\[
b_4=b_1+b_2+b_3\pm2\sqrt{b_1b_2+b_2b_3+b_3b_1}.
\]

El programa usa la raíz positiva para el círculo interior cuando las tres
curvaturas de entrada son positivas. Una vez insertado `b_4`, ese círculo
participa en tres nuevas ternas de frontera.
La reflexión

\[
b_i'=2\sum_{j\ne i}b_j-b_i
\]

produce el círculo que ocupa la cavidad vecina al sustituir `b_i`. Así se
formaliza la intuición recursiva: un objeto es **centro respecto de la cavidad
que lo genera** y se vuelve **parte de la frontera de cavidades hijas**.

Ésta es una relación de nivel, no una contradicción de rol.

## 3. Dos reglas dimensionales expresamente separadas

El motor usa ahora puntos de `R^d`, con la dimensión ambiente declarada por el
número de coordenadas. Se distinguen dos problemas que pueden compartir una
imagen de una esfera central, pero no el mismo contrato matemático.

### 3.1 Regla intersticial simplex `I(d)`

Para `d>=2`, sean `d+1` bolas anfitrionas congruentes de radio `R`, mutuamente
tangentes, cuyos centros forman un simplex regular. La bola intersticial
centrada en el circuncentro tiene radio:

\[
N_{\mathrm{hosts}}=d+1,
\qquad
\frac{r_{\mathrm{int}}}{R}
=\sqrt{\frac{2d}{d+1}}-1.
\]

Aquí «intersticial» significa que el centro se encuentra en el interior del
simplex de centros y que la bola central toca todas las anfitrionas. No se usa
como afirmación adicional sobre componentes conexas del complemento.

El grafo de contacto de las anfitrionas es `K_(d+1)`. Al agregar la bola
intersticial, que toca a cada anfitriona, el grafo total es `K_(d+2)`.

En `d=4` se obtienen cinco anfitrionas y una bola central:

\[
\frac{r_{\mathrm{int}}}{R}
=\sqrt{\frac85}-1
\approx0.2649110640673518,
\]

\[
G_{\mathrm{hosts}}=K_5,
\quad |E_{\mathrm{hosts}}|=10,
\qquad
G_{\mathrm{total}}=K_6,
\quad |E_{\mathrm{total}}|=15.
\]

La implementación `regular_simplex(d)` construye coordenadas unitarias en
`R^d` mediante una base de Helmert. Para `d=4`, sus cinco filas satisfacen
`||u_i||=1` y `u_i . u_j=-1/4` cuando `i!=j`.

### 3.2 Regla de kissing `K(d)`

Sea una bola central de radio `R` y una familia de vecinas también de radio
`R`. El número de kissing `tau_d` es el máximo número de vecinas congruentes
que pueden tocar simultáneamente a la central sin solaparse. Si `u_i` son sus
direcciones unitarias, los centros vecinos son `p_i=2R u_i` y:

\[
u_i\cdot u_j\le\frac12
\quad\Longleftrightarrow\quad
\|p_i-p_j\|\ge2R.
\]

Dos vecinas se tocan exactamente cuando `u_i . u_j=1/2`. El grafo exterior no
tiene por qué ser completo y `tau_d` no cuenta los vértices de un simplex.

En `d=4`, `tau_4=24`. La realización incorporada usa las direcciones del
sistema de raíces `D4`, equivalentes a los vértices del 24-cell:

\[
\mathcal U_{24}
=\left\{
\frac{\sigma e_i+\tau e_j}{\sqrt2}:
1\le i<j\le4,\;\sigma,\tau\in\{-1,+1\}
\right\}.
\]

El grafo de contacto exterior es el 1-esqueleto del 24-cell: tiene 24 vértices,
es 8-regular y contiene 96 aristas. Incluyendo la bola central:

\[
G_{\mathrm{total}}=K_1\vee G_{24\text{-cell}},
\qquad
|E_{\mathrm{total}}|=96+24=120.
\]

La separación que debe conservarse en todo uso posterior es:

\[
\boxed{I(d):\ d+1\text{ anfitrionas alrededor de una bola desigual}}
\]

frente a:

\[
\boxed{K(d):\ \tau_d\text{ vecinas congruentes alrededor de una central congruente}.}
\]

En cuatro dimensiones: `5 != 24`, `0.264911...R != R` y
`K6 != K1 join G_24-cell`.

## 4. La igualdad de radios no implica igualdad de estructura

El hueco cuadrangular plano y el hueco octaédrico tridimensional comparten el
valor:

\[
\sqrt2-1.
\]

Sus grafos de contacto son distintos:

- cuadrado con centro: `C4 ∨ K1`;
- octaedro exterior: `K_{2,2,2}`;
- octaedro con esfera central: `K1 ∨ K_{2,2,2}`.

La coincidencia métrica es exacta; la identificación estructural no se sigue de
ella.

## 5. Prisma y octaedro como dos tipos de enlace sobre las mismas ternas

Sean `H={H0,H1,H2}` y `A={A0,A1,A2}`, cada una con sus tres aristas internas, y
sea `M` una correspondencia perfecta entre ambas. Entonces:

\[
P(M)=C3[H]\sqcup C3[A]\cup M,
\]

\[
O(M)=C3[H]\sqcup C3[A]\cup(K_{3,3}\setminus M).
\]

El complemento cruzado satisface:

\[
K_{3,3}\setminus M\cong C6.
\]

Para el mismo `M`:

\[
P(M)\cap O(M)=C3[H]\sqcup C3[A],
\qquad
P(M)\cup O(M)=K6.
\]

Hay exactamente `3! = 6` correspondencias etiquetadas. El cómputo enumera las
seis y verifica los conteos, grados, intersección, unión y ciclo cruzado.

Los invariantes finitos permiten distinguir los portadores incluso si una
proyección se parece visualmente:

| Grafo | `V` | `E` | grados | `β1` | `#C3,#C4,#C5,#C6` |
|---|---:|---:|---|---:|---|
| prisma triangular | 6 | 9 | `3^6` | 4 | `2,3,6,3` |
| octaedro | 6 | 12 | `4^6` | 7 | `8,15,24,16` |
| dos ternas `2C3` | 6 | 6 | `2^6` | 2 | `2,0,0,0` |
| cinturón cruzado `C6` | 6 | 6 | `2^6` | 1 | `0,0,0,1` |

Esto hace innecesario tratar prisma y octaedro como figuras rivales. Son dos
selecciones tipadas de enlaces sobre el mismo soporte de seis posiciones:

- `M`: correspondencias directas del prisma;
- `K3,3 \ M`: enlaces cruzados del octaedro, que forman `C6`.

## 6. Celdas triangulares y cuadrangulares en distintos niveles

Se define una celda `Fk` por una frontera ordenada de `k` vértices y un nivel
`l`. La inserción estelar de un centro `g` genera:

\[
h_l:F_k^l\longrightarrow g^{l+1}
\]

y subdivide la celda en `k` triángulos del nivel siguiente.

- `F3^l` produce tres `F3^{l+1}`;
- `F4^l` produce cuatro `F3^{l+1}`.

La celda cuadrangular permanece registrada como padre en la jerarquía; los
cuatro triángulos son sus hijos en `l+1`. Por eso una retícula cuadrangular y
una triangular pueden coexistir en la misma estructura jerárquica sin ocupar
el mismo papel ni el mismo nivel.

En el complejo de un nivel, cuando una `Fk` que delimita un disco se retira y
se sustituye por un hub y `k` triángulos, el cambio es
`Δ(V,E,F)=(1,k,k-1)` y conserva Euler. Para `F3`, `Δ=(1,3,2)`; para `F4`,
`Δ=(1,4,3)`. El registro jerárquico padre-hijos es un objeto adicional y no se
cuenta como si todas esas caras pertenecieran simultáneamente al mismo nivel.

## 7. Cruces visibles y vértices reales

Una superposición proyectada conserva el tipo de cada segmento. Dos aristas de
capas distintas pueden:

1. compartir un vértice declarado;
2. cruzarse sólo en la proyección;
3. no incidir;
4. quedar colineales y requerir una decisión de tipado.

El cruce interior de dos segmentos con extremos distintos se clasifica como
`CRUCE_DE_PROYECCION_NO_VERTICE`. Sólo se convierte en vértice si la estructura
de incidencia lo declara. Esta distinción es necesaria para digitalizar las
fotografías de varillas sin convertir cada cruce visual en una unión.

## 8. Qué está establecido y qué queda abierto

| Afirmación | Estado |
|---|---|
| Fórmula del anillo regular | derivación exacta |
| Fórmula desigual y solución numérica | derivación exacta + cómputo reproducible |
| Recursión por reflexión de Descartes | resultado clásico implementado |
| Familia colineal `n=2`, `r>0`, y límite `r -> 0` | derivación exacta + caso computacional existente |
| Regla intersticial simplex `I(d)` | derivación exacta + implementación en `R^d` |
| Coordenadas y contactos del 4-simplex | construcción exacta + pruebas computacionales |
| Regla kissing `K(d)` y `tau_4=24` | resultado clásico + realización `D4` verificada |
| Grafo exterior del 24-cell: 24 vértices, grado 8 y 96 aristas | resultado computado a partir de coordenadas exactas |
| Seis matchings y descomposición prisma/octaedro | demostración combinatoria + pruebas exhaustivas finitas |
| Refinamiento `Fk -> k F3` | definición combinatoria verificada |
| Identificación de cruces en las cinco fotos | experimento de digitalización pendiente |
| Correspondencia de estos objetos con `C3_H`, `C3_A`, `C6` o Corazón | hipótesis semántica separada |

### Control documental R3

El bundle recuperado distingue cuatro predicados que no son intercambiables:

| Predicado en `R3_C6_cycles.csv` | Conteo R3 |
|---|---:|
| ciclo abstracto de longitud 6 | 16 |
| ciclo con seis esquinas geométricas | 7 |
| ciclo de seis esquinas convexo | 1 |
| hexágono regular | 1 |

`README_MASTER_RESULTS.md` identifica ese único hexágono regular como la
frontera de la estrella del centro de R3. El script `audit_r3_cycles.py`
reconstruye la malla triangular R3, enumera sus ciclos simples de longitud 6,
deriva esquinas, convexidad y regularidad desde las coordenadas baricéntricas,
y coteja el resultado con ambos CSV.
Una infografía generada que atribuye tres hexágonos regulares a ese mismo centro
no coincide con las tablas fuente y queda clasificada como visualización
derivada no utilizable para ese conteo.

## 9. Visualizaciones

- `visualizations/interstitial_regular_rings.svg`
- `visualizations/prism_octahedron_typed.svg`
- `visualizations/cell_refinement_levels.svg`
- `visualizations/resumen_interstitial_multinivel.png`

Las cifras proceden del JSON reproducible; los SVG sirven para inspección de la
estructura.
