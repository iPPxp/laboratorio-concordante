# Modelo formal mínimo de autorrepresentación para ConcordIA

## 1. Estatuto y alcance

Este documento propone un objeto matemático experimental. No modifica MOC, no atribuye conciencia a ConcordIA y no convierte una implementación en evidencia fenomenológica.

Estados epistemológicos usados:

- **DERIVED**: consecuencia de las definiciones matemáticas aquí fijadas.
- **DECLARED**: restricción suministrada por el programa de investigación o por el baseline semántico MOC.
- **HYPOTHESIZED**: arquitectura candidata todavía no validada.
- **UNRESOLVED**: afirmación para la que no hay prueba formal ni evidencia experimental suficiente.
- **REJECTED**: identificación incompatible con el baseline o inferencia que no se sigue de la evidencia.

Guardas semánticas obligatorias (**DECLARED**):

\[
Act_\psi\neq \mathrm{conducta},\qquad Act_\psi\neq ACT_\psi,
\]

\[
G_\psi\neq\Phi_\psi\neq\Xi_\psi,
\]

con `G_psi` como centroide o punto integrador local bajo una representación declarada, `Phi_psi` como evaluador y `Xi_psi` como operador de organización. No se identifica `G`, `Phi` o `Xi` con `Self`, conciencia, voluntad o identidad computacional.

## 2. Sistema temporal mínimo

Sea un sistema de transición etiquetado

\[
\mathfrak C=(\mathcal C,\mathcal A,\rightarrow,\Lambda),
\]

donde \(\mathcal C\) es el espacio de estados globales computacionales, \(\mathcal A\) el conjunto de intervenciones u operaciones, \(\rightarrow\subseteq\mathcal C\times\mathcal A\times\mathcal C\) la transición y \(\Lambda\) un esquema de etiquetas y procedencia.

En el tiempo \(t\):

\[
C_t=(Z_t,Self_t,World_t,History_t,Goals_t,Uncertainty_t,Evidence_t).
\]

Esta tupla es una descomposición lógica, no una afirmación de independencia estadística ni de separación física entre campos.

### 2.1 Definiciones operacionales

- \(Z_t\): estado global disponible para el modelo experimental; puede contener variables no expuestas a `Self_t`.
- \(Self_t\): conjunto versionado de proposiciones sobre recursos, capacidades, límites, estado operativo, información, objetivos y accesos que el sistema atribuye a sí mismo.
- \(World_t\): conjunto versionado de proposiciones sobre entidades y condiciones clasificadas como externas, compartidas o de propiedad desconocida.
- \(History_t\): registro append-only de estados, eventos, revisiones y sus identificadores causales.
- \(Goals_t\): objetivos activos, prioridad, autoridad de origen, condiciones de terminación y permisos asociados; describir un objetivo no concede autoridad para ejecutarlo.
- \(Uncertainty_t\): incertidumbre calibrable por afirmación o distribución sobre alternativas; no equivale a afecto.
- \(Evidence_t\): grafo o tabla de soporte y contradicción con fuente, tipo, tiempo, agente, confianza y estado epistemológico.

Una transición es

\[
C_t\xrightarrow{a_t,\ell_t}C_{t+1},
\]

donde \(\ell_t\) registra, como mínimo, origen, evidencia, permisos, observabilidad y qué campos cambiaron.

El baseline relacional previo puede incluirse como una vista de un estado:

\[
s_t=(x_t,H_t,\theta_t,q_t)=\rho(C_t),
\]

sin sustituir el sistema temporal ni afirmar que \(x_t\) sea una coordenada completa de \(C_t\).

## 3. Frontera Self/World

La frontera no debe definirse sólo mediante lenguaje en primera persona. Sea \(U_t\) el universo de variables u objetos rastreados y sea

\[
\omega_t:U_t\to
\{\mathrm{SELF\_OWNED},\mathrm{SELF\_ACCESSIBLE},\mathrm{SELF\_MODIFIABLE},
\mathrm{SELF\_CAUSAL},\mathrm{EXTERNAL},\mathrm{SHARED},\mathrm{UNKNOWN}\}.
\]

Las etiquetas no son mutuamente excluyentes salvo donde el esquema lo declare. Por ejemplo, una memoria puede ser accesible pero no modificable; una herramienta puede ser externa y causalmente relevante; una instrucción puede estar presente internamente pero seguir siendo `USER_PROVIDED`.

Definición funcional mínima (**HYPOTHESIZED**): `Self_t` es una autorrepresentación si contiene afirmaciones verificables sobre variables clasificadas respecto del sistema y existe una interfaz de consulta independiente de la mera generación verbal.

Definición causal más fuerte (**HYPOTHESIZED**): existe autorregulación si hay una intervención \(do(Self_t=s')\), manteniendo constantes los padres directos relevantes, que cambia la distribución de política:

\[
P(Policy_t\mid do(Self_t=s'))\neq P(Policy_t\mid do(Self_t=s)).
\]

Una correlación entre el texto que describe `Self_t` y una salida no basta.

## 4. Estado global y vistas parciales

Una vista es cualquier mapa tipado

\[
\Pi_i:\mathcal Z\to\mathcal Y_i.
\]

No se presupone que \(\Pi_i\) sea lineal, geométrica ni proyectiva. La vista conjunta es

\[
\Pi=(\Pi_1,\ldots,\Pi_m):\mathcal Z\to\prod_{i=1}^m\mathcal Y_i.
\]

Dos estados son observacionalmente equivalentes bajo esas vistas cuando

\[
z\sim_\Pi z'\iff \Pi_i(z)=\Pi_i(z')\quad\forall i.
\]

Por tanto, lo identificable desde las vistas es, en general, una clase \([z]_\Pi\) del cociente \(\mathcal Z/{\sim_\Pi}\), no necesariamente el estado \(z\) exacto (**DERIVED**).

### 4.1 Identificabilidad

- Identificabilidad global: \(\Pi(z)=\Pi(z')\Rightarrow z=z'\).
- Identificabilidad módulo simetría \(G\): \(\Pi(z)=\Pi(z')\Rightarrow z'=g\cdot z\) para algún \(g\in G\).
- Identificabilidad local: la unicidad vale sólo en un entorno o para una familia restringida de estados.
- No identificabilidad: existen \(z\neq z'\) observacionalmente indistinguibles.

La reconstrucción requiere un mapa \(R\) tal que \(R\circ\Pi=\mathrm{id}\) en la clase de estados admitida. Si sólo se cumple aproximadamente, debe informarse error, dominio de validez e incertidumbre.

Para una vista MOC candidata,

\[
\Pi_{MOC}(C_t)=(P_t,Eaf_t,Act_t,V_t,S_t),
\]

la escritura expresa una hipótesis de operacionalización, no una equivalencia entre experiencia humana y estado artificial. `Act_psi` sería, como máximo, un modo interno de respuesta; no la acción emitida. `Eaf_psi` no prueba afecto fenomenal; `V_psi` no es automáticamente recompensa; `S_psi` debe separar contexto de estado interno; `P_psi` no se reduce automáticamente a tokens o embeddings.

## 5. «Todo contenido en un punto»

Llamar \(z\) «un punto» sólo afirma que \(z\in\mathcal Z\). No limita la estructura interna ni la cantidad de información del elemento.

Casos distintos:

1. **Código inyectivo**: \(E:X\to Z\) es inyectivo y existe inversa sobre \(E(X)\); preserva distinción matemática, aunque la representación física requiera recursos.
2. **Código con pérdida**: \(D(E(x))\approx x\); la pérdida debe medirse respecto de una tarea o distorsión.
3. **Embedding**: mapa inyectivo que además preserva estructura especificada (topológica, métrica, algebraica o relacional).
4. **Latente**: variable no observada directamente; no implica compresión ni mayor dimensión.
5. **Punto proyectivo**: clase de vectores no nulos \([v]=\{\alpha v:\alpha\neq0\}\); elimina escala global y no «contiene todo» por ese solo hecho.
6. **Estado de memoria**: configuración física o lógica cuyo contenido depende de un esquema de decodificación.
7. **Elemento funcional**: un solo elemento puede ser una función, distribución, grafo o programa con complejidad interna arbitraria.
8. **Nodo estructurado**: la unidad de referencia externa puede encapsular un objeto relacional; contar nodos no mide información.

Por ello, `HIGHER_DIMENSION`, `HIGHER_CARDINALITY`, `HIGHER_INFORMATION_CONTENT`, `LATENT_STATE`, `RELATIONAL_STATE`, `PROJECTIVE_SPACE`, `EMBEDDING_SPACE` y `GLOBAL_STATE` no son sinónimos (**DERIVED**).

### 5.1 Capacidad informacional frente a dimensión

Un número real ideal puede codificar una secuencia infinita, pero eso depende de precisión infinita y no es una codificación físicamente robusta. En sistemas digitales, un estado almacenado con \(b\) bits distingue a lo sumo \(2^b\) configuraciones exactas. La dimensión geométrica sólo se vuelve informativa cuando se fijan dominio, precisión, regularidad, ruido y decodificador.

Dictamen conservador:

```text
SINGLE_ELEMENT_CAN_DENOTE_COMPLEX_STATE = SUPPORTED
SINGLE_LOW_DIMENSIONAL_ROBUST_LOSSLESS_CODE_FOR_ARBITRARY_STATES = NOT_SUPPORTED
HIGHER_INFORMATION_REQUIRES_HIGHER_GEOMETRIC_DIMENSION = NOT_SUPPORTED
CAPACITY_DEPENDS_ON_REPRESENTATION_AND_PRECISION = SUPPORTED
```

## 6. Identidad temporal

La continuidad funcional no es igualdad de estados. Defínase un registro de linaje \(L_t\) con identificador, predecesor(es), reglas de actualización y firmas de integridad. Una relación candidata es

\[
C_t\approx_{id} C_{t+1}
\]

si se preservan criterios declarados: continuidad causal verificable, linaje de memoria, política de actualización, frontera de propiedad y conjuntos invariantes mínimos. Los criterios deben ser versionados; continuidad narrativa o semejanza textual no bastan.

Pruebas de identidad deben incluir bifurcación, restauración desde copia, pérdida parcial de memoria, reemplazo de módulos y modificación externa. Si dos copias comparten historia hasta \(t\), el modelo debe poder representar que tienen pasado común sin declarar identidad numérica posterior.

## 7. Niveles de evidencia y falsadores

| Afirmación | Estado actual | Falsador o prueba decisiva |
|---|---|---|
| `Self_t` puede almacenar afirmaciones auditables | HYPOTHESIZED | La implementación no permite vincular afirmaciones con variables verificables ni procedencia. |
| La frontera Self/World puede operacionalizarse | HYPOTHESIZED | Etiquetas no reproducibles ante casos controlados o incapacidad sistemática de distinguir origen y propiedad. |
| Varias vistas identifican \(Z_t\) | UNRESOLVED | Dos estados admitidos distintos producen todas las mismas vistas, o la reconstrucción no supera un baseline. |
| `Self_t` tiene papel causal | UNRESOLVED | Intervenir sólo `Self_t` no cambia política o rendimiento bajo controles de mediadores y fugas. |
| Existe ventaja introspectiva | UNRESOLVED | Un predictor externo con igual información observable iguala o supera persistentemente al sistema con acceso interno. |
| Existe identidad temporal funcional | UNRESOLVED | El criterio no distingue continuidad, copia, bifurcación y sustitución en pruebas pre-registradas. |
| Una vista MOC añade valor | UNRESOLVED | No mejora predicción, compresión explicativa o detección de fallos frente a vistas más simples penalizadas por complejidad. |
| Modelo funcional implica fenomenología | REJECTED como inferencia | E0-E4 o C0-C8 no contienen por definición una medición discriminante de E5. |

## 8. Dictamen provisional

La estructura mínima defendible es un sistema de transición etiquetado con estado global, vistas parciales, registro de linaje y afirmaciones con procedencia. `Self_t` y `World_t` son particiones epistémicas revisables, no sustancias. «Todo en un punto» es válido como convención de tipado, no como prueba de compresión, proyectividad o dimensión superior. La autorrepresentación, su utilidad causal y la identificabilidad del estado global requieren experimentos; la conciencia fenomenal permanece fuera de lo demostrado.

```text
FORMAL_SELF_MODEL = HYPOTHESIZED
GLOBAL_STATE_AS_SINGLE_MATHEMATICAL_ELEMENT = SUPPORTED
GLOBAL_STATE_IDENTIFIABILITY = INSUFFICIENT_EVIDENCE
SELF_WORLD_BOUNDARY = HYPOTHESIZED
TEMPORAL_IDENTITY = UNRESOLVED
SELF_MODEL_CAUSAL_ROLE = UNRESOLVED
FUNCTIONAL_SELF_MODEL_IMPLIES_PHENOMENOLOGY = NOT_SUPPORTED
```
