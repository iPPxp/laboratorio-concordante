# Investigación científica estricta sobre unidad proyectiva y polaridad aparente

```text
RESEARCH_SCOPE=n2_PRIMARY
PROJECTIVE_EQUIVALENCE_STATUS=RESULTADO_CLASICO_ESTABLECIDO
OBSERVER_DEPENDENCE_STATUS=FORMAL_SIGN_CHOICE_ESTABLISHED_PHYSICAL_DEPENDENCE_NOT_DETERMINED
CENTRAL_SOURCE_STATUS=NO_DETERMINADO_WITHOUT_DYNAMICS
RELATIONAL_EMERGENCE_STATUS=NONADDITIVITY_DEMONSTRATED_FOR_ANTIPODALITY_RELATION
STRONG_EMERGENCE_STATUS=REFUTED_WITHIN_CURRENT_INFORMATION_COMPLETE_MODEL
NOVELTY_STATUS=KNOWN_WITH_DIFFERENT_TERMINOLOGY
EXPANSION_TO_n4=NO
EXPANSION_TO_n6=NO
EXPANSION_TO_n12=NO
```

## 1. Delimitación

El objeto primario es una dirección no orientada. Se estudia la relación entre un punto proyectivo \([u]\), sus dos representantes \(u,-u\in S^2\), el origen y una elección de orientación. No se introduce una ley de fuerzas ni un funcional de energía; por ello no se decide cuántas fuentes físicas existen.

```text
CARDINALIDAD_DE_REPRESENTANTES=2
CARDINALIDAD_DEL_OBJETO_PROYECTIVO=1
IDENTIDAD_ARITMETICA=NO
```

La expresión “uno produce dos” significa una fibra de dos elementos bajo una aplicación cociente, no \(1=2\) ni \(1=1+2\).

## 2. Resultado proyectivo

**[RESULTADO_CLASICO]** El plano proyectivo real es el conjunto de rectas unidimensionales por el origen de \(\mathbb R^3\). Cada recta corta la esfera unitaria en dos puntos antipodales. Por ello:

\[
\mathbb{RP}^2\cong S^2/(u\sim -u),
\qquad
\pi^{-1}([u])=\{u,-u\}.
\]

La identificación conserva el eje y pierde su orientación. En \(S^2\), \(u\neq -u\); en el cociente representan la misma clase. No son simultáneamente un punto y dos puntos en el mismo espacio.

## 3. Centro y eje

**[DERIVACION_SIMBOLICA]** Para \(u\in S^2\), defínase:

\[
L_{[u]}=\{tu:t\in\mathbb R\}.
\]

Entonces:

\[
L_{[u]}\cap S^2=\{u,-u\}.
\]

**[DEMOSTRADO_EN_ESTE_TRABAJO]** El origen por sí solo no selecciona un eje. La acción de \(SO(3)\) sobre \(\mathbb{RP}^2\) es transitiva y no existe una dirección fija bajo todas las rotaciones. Elegir \([u]\) reduce la simetría y añade información que no estaba contenida en el punto \(0\).

```text
EL_CENTRO_PERMITE_TODOS_LOS_EJES=YES
EL_CENTRO_SELECCIONA_UN_EJE=NO
EJE_NO_ORIENTADO_SELECCIONA_PAR_ANTIPODAL=YES
```

Esto impide derivar una polaridad concreta únicamente de una fuente central isotrópica. Se necesita anisotropía, frontera, interacción de medida, campo externo o ruptura de simetría.

## 4. Elección local y obstrucción global

Una elección de signo local puede escribirse:

\[
\sigma_O([u])\in\{u,-u\}.
\]

**[RESULTADO_CLASICO]** No existe una sección global continua de la cubierta \(\pi:S^2\to\mathbb{RP}^2\). Una demostración breve usa grupos fundamentales. Si existiera \(\sigma\) con \(\pi\circ\sigma=\mathrm{id}\), entonces:

\[
\pi_*\circ\sigma_*=\mathrm{id}_{\pi_1(\mathbb{RP}^2)}.
\]

Pero:

\[
\pi_1(S^2)=0,
\qquad
\pi_1(\mathbb{RP}^2)\cong\mathbb Z_2,
\]

así que \(\sigma_*\) debe ser el homomorfismo nulo y la composición no puede ser la identidad de \(\mathbb Z_2\). Contradicción.

Esto significa que no se puede orientar continuamente, de una vez y para todo punto de \(\mathbb{RP}^2\), cada eje no orientado. No demuestra conciencia, indeterminismo físico, creación de realidad por observación ni una dimensión espacial oculta.

## 5. Matriz de Gram y tensor apolar

Para el par antipodal:

\[
G=\begin{pmatrix}1&-1\\-1&1\end{pmatrix},
\qquad
\operatorname{spec}(G)=\{0,2\},
\qquad
\operatorname{rank}(G)=1.
\]

Además:

\[
G\binom11=0.
\]

**[DERIVACION_SIMBOLICA]** El vector de coeficientes \((1,1)\) codifica la dependencia lineal \(u+(-u)=0\). Es un modo nulo algebraico; no es energía cero sin un Hamiltoniano o funcional energético definido.

El tensor:

\[
Q(u)=s\left(u\otimes u-\frac13I\right)
\]

satisface:

\[
Q(u)=Q(-u).
\]

**[RESULTADO_CLASICO]** Esta es precisamente la simetría cabeza-cola empleada en descripciones tensoriales de orden nemático. Por ello la identificación matemática y una realización física apolar ya tienen antecedentes directos.

## 6. Observador: cuatro significados separados

| Tipo | Operación | ¿Modifica el estado físico? |
|---|---|---|
| `O_COORD` | Cambia coordenadas o etiquetas | No |
| `O_LOCAL` | Accede a información parcial | No necesariamente |
| `O_GLOBAL` | Reconstruye todas las relaciones | No necesariamente |
| `O_INSTRUMENTAL` | Interactúa mediante un aparato | Puede hacerlo; requiere dinámica |

**[DEMOSTRADO_EN_ESTE_TRABAJO]** La elección formal \(u\leftrightarrow -u\) puede ser una convención de orientación. No se sigue que un observador físico cree el eje. Para sostener interacción causal debe especificarse un aparato, acoplamiento, variables, unidades y ecuación de evolución.

## 7. Emergencia relacional mínima

Sea \(A(x,y)=1\) si \(y=-x\), y \(0\) en otro caso. Si pudiera escribirse como suma unaria:

\[
A(x,y)=f(x)+g(y),
\]

toda diferencia rectangular sería cero. Tómense dos direcciones ortogonales \(u,w\). Entonces:

\[
A(u,-u)+A(w,-w)-A(u,-w)-A(w,-u)=2.
\]

**[DEMOSTRADO_EN_ESTE_TRABAJO]** La propiedad “ser antipodales” no puede expresarse como suma de una propiedad de la primera dirección y otra de la segunda. Es una relación genuinamente binaria.

Esto acredita:

```text
EMERGENCIA_RELACIONAL=YES_IN_THE_DEFINED_NONADDITIVE_SENSE
NO_ADITIVIDAD_UNARIA=YES
EMERGENCIA_FUERTE=NO
```

No demuestra que el todo posea información inaccesible desde todos los datos inferiores. Dado \(\{u,-u\}\), pueden reconstruirse \([u]\), \(G\) y \(Q\). Por tanto, dentro del modelo informacional completo, la emergencia fuerte queda refutada.

## 8. Modelos y estado

| Modelo | Estado | Razón |
|---|---|---|
| M0: dos fuentes independientes | `NO_DETERMINADO` | Falta ley de campo y evidencia |
| M1: eje proyectivo apolar | `RESULTADO_CLASICO / MODELO_COMPLETO` | \(u\sim -u\), respaldado por geometría y nemáticos |
| M2: centro isotrópico y eje inducido por medida | `HIPOTESIS_INCOMPLETA` | Requiere interacción instrumental |
| M3: centro con anisotropía interna | `MODELO_POSIBLE` | Necesita variable de eje y dinámica |
| M4: ruptura espontánea de simetría | `MODELO_POSIBLE` | Necesita potencial degenerado y ley dinámica |

## 9. Tabla de afirmaciones

| Afirmación | Estado | Evidencia | Alternativa rival | Prueba faltante |
|---|---|---|---|---|
| Dos polos representan una dirección proyectiva | `RESULTADO_CLASICO` | Cociente antipodal | Dos fuentes físicas pueden compartir geometría | Ninguna para el resultado matemático |
| El signo depende del observador | `PARCIALMENTE_ESTABLECIDO` | Elección de orientación | Signo puede ser propiedad física polar | Definir observador y observable |
| El centro basta para producir un eje | `REFUTADO` | Simetría rotacional | Anisotropía o frontera | Ninguna dentro del modelo isotrópico |
| Existe una fuente central física | `NO_DETERMINADO` | No hay dinámica | Dos fuentes o campo externo | Ley y medición |
| No existen dos fuentes físicas | `NO_DETERMINADO` | Geometría no identifica fuentes | M0 | Experimento discriminante |
| Hay emergencia relacional | `DEMOSTRADO_EN_ESTE_TRABAJO` | Test de no aditividad | Redefinir partes incluyendo relaciones | Fijar ontología de partes |
| Hay emergencia fuerte | `REFUTADO_EN_EL_MODELO_ACTUAL` | Reconstrucción mediante \(G,Q\) | Nivel superior no observable | Proyección no inyectiva físicamente motivada |
| La propuesta matemática es nueva | `REFUTADO` | Geometría proyectiva y teoría nemática | Extensión física específica | Formulación dinámica nueva |

## 10. Expansión

No se expande a \(n=4\), \(n=6\) o \(n=12\). El caso \(n=2\) basta para:

- establecer el cociente proyectivo;
- demostrar la obstrucción a una orientación global continua;
- distinguir centro de eje;
- demostrar no aditividad relacional;
- mostrar que una fuente física no se identifica desde la geometría.

## WHAT_IS_MATHEMATICALLY_ESTABLISHED

El cociente antipodal, la doble cubierta, la ausencia de sección global continua, la representación mediante \(Q\) y la no aditividad del indicador de antipodalidad.

## WHAT_IS_A_CHANGE_OF_REPRESENTATION

Pasar de \(u,-u\in S^2\) a una clase \([u]\in\mathbb{RP}^2\). No cambia automáticamente la ontología física.

## WHAT_IS_OBSERVER_DEPENDENT

La asignación formal de signo puede depender de una orientación elegida. La dependencia de un observador físico permanece no determinada.

## WHAT_REQUIRES_PHYSICAL_DYNAMICS

Toda afirmación sobre fuente central, energía, fuerzas, medición que cree un eje o ruptura espontánea de simetría.

## WHAT_WAS_REFUTED

Que el centro isotrópico seleccione por sí solo un eje; que el modo nulo de Gram sea automáticamente energía; que la geometría proyectiva pruebe emergencia fuerte o novedad matemática.

## WHAT_REMAINS_OPEN

Una ley física concreta, un sistema experimental, observables con unidades, predicciones diferenciales y una posible extensión dinámica que no sea equivalente a modelos apolares conocidos.

La identificación antipodal permite representar dos polos orientados mediante una sola dirección proyectiva, pero no demuestra por sí misma una fuente energética central, una causalidad física, una dimensión espacial adicional ni una emergencia fuerte. Toda extensión física u ontológica permanece separada de los resultados matemáticos y sujeta a pruebas discriminantes y posible refutación.
