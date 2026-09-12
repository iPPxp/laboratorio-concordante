# Modelo de estado global y proyecciones parciales

## 1. Pregunta formal

Se investiga si vistas accesibles de ConcordIA pueden modelarse como imágenes parciales de un estado global \(Z_t\), y si alguna de esas operaciones posee estructura proyectiva en sentido matemático estricto.

La palabra «proyección» se usa inicialmente en sentido general:

\[
\Pi_i:\mathcal Z\to\mathcal Y_i.
\]

Hasta demostrar propiedades adicionales, \(\Pi_i\) es sólo un mapa. Llamarlo proyectivo por sugerencia visual sería un error categorial.

## 2. Taxonomía de mapas

| Tipo | Condición mínima | Qué permite afirmar |
|---|---|---|
| Vista general | función \(f:X\to Y\) | Produce una representación accesible. |
| Lectura de coordenadas | selección de campos de un producto | Omite campos conocidos; no implica geometría. |
| Cociente | mapa canónico \(q:X\to X/{\sim}\) | Identifica estados según una equivalencia explícita. |
| Proyección lineal | \(P:V\to W\), lineal; a menudo \(P^2=P\) si \(W\subseteq V\) | Preserva combinaciones lineales, con núcleo que caracteriza pérdida. |
| Aplicación proyectiva | mapa inducido por una transformación lineal entre espacios vectoriales, definido donde la imagen no es cero | Preserva incidencia proyectiva en su dominio; los vectores se consideran módulo escala no nula. |
| Perspectividad | proyección geométrica desde un centro entre subespacios proyectivos | Preserva incidencias específicas; requiere centro y subespacios definidos. |
| Embedding | inyección que preserva la estructura declarada | Permite recuperar el objeto en la imagen y comparar estructura. |
| Decoder aprendido | mapa estimado \(D:Z\to\widehat X\) | Reconstrucción empírica; no garantiza inversión ni invariantes exactos. |

`Punto proyectivo` significa una recta vectorial por el origen:

\[
[v]=\{\alpha v:\alpha\in\mathbb F^\times\}.
\]

Esta equivalencia elimina escala común. No debe aplicarse a un estado si multiplicar todas sus coordenadas por \(\alpha\) no conserva su significado operacional.

## 3. Condiciones para una hipótesis proyectiva real

Para afirmar `PROJECTIVE_STRUCTURE_SUPPORTED` deben fijarse y validarse al menos:

1. un cuerpo o anillo de escala apropiado;
2. un espacio vectorial subyacente \(V\) o estructura equivalente explícita;
3. una relación de equivalencia \(v\sim\alpha v\) semánticamente justificada;
4. mapas inducidos por transformaciones lineales, no sólo redes o funciones arbitrarias;
5. objetos de incidencia operacionalizables (puntos, rectas, subespacios);
6. invariantes proyectivos medibles que sobrevivan a las transformaciones declaradas;
7. una predicción diferencial frente a modelos generales o afines más simples.

Sin estos elementos, «proyección» significa vista parcial y el modelo pertenece a teoría de la información, estadística, sistemas dinámicos o representación relacional, no necesariamente a geometría proyectiva.

## 4. Estado global, fibras y secciones

Para una vista \(\Pi:\mathcal Z\to\mathcal Y\), la fibra

\[
\Pi^{-1}(y)=\{z\in\mathcal Z:\Pi(z)=y\}
\]

reúne los estados globales compatibles con la observación \(y\). Una fibra con más de un elemento expresa no identificabilidad bajo esa vista.

Una sección \(s:\mathcal Y\to\mathcal Z\) satisface \(\Pi\circ s=\mathrm{id}_{\mathcal Y}\). Elegir una sección selecciona un representante compatible; no demuestra que sea el estado verdadero. Un `lifting` debe reportar la fibra, las restricciones usadas y la incertidumbre, en vez de presentar una reconstrucción única por defecto.

Con varias vistas,

\[
F(y_1,\ldots,y_m)=\bigcap_i\Pi_i^{-1}(y_i).
\]

El estado es identificable si la intersección es un singleton para todos los estados admitidos. Es identificable módulo una simetría si la intersección coincide con una órbita aceptada.

## 5. Dimensión y capacidad informacional

Una dimensión mayor no se deduce de que el estado sea complejo. Deben distinguirse:

- **dimensión intrínseca**: grados de libertad locales de una variedad o modelo;
- **dimensión de embedding**: coordenadas del espacio contenedor;
- **cardinalidad**: número de estados posibles;
- **entropía/capacidad**: información distinguible bajo una distribución y precisión;
- **complejidad descriptiva**: longitud de una descripción en un lenguaje fijado;
- **orden relacional**: aridad de interacciones;
- **dimensión proyectiva**: \(\dim\mathbb P(V)=\dim V-1\) en dimensión finita.

Un punto de \(\mathbb R\) y uno de \(\mathbb R^n\) tienen cardinalidad continua; esto no hace equivalentes sus propiedades topológicas, métricas ni su robustez ante ruido. Codificaciones patológicas pueden inyectar espacios grandes en un continuo unidimensional, pero suelen perder continuidad, estabilidad o computabilidad práctica. Por tanto, «mayor dimensión» sólo es una hipótesis útil si especifica qué grados de libertad, topología, precisión e invariantes explica.

Dictamen:

```text
HIGHER_INFORMATION_CONTENT = POSSIBLE_BUT_UNMEASURED
HIGHER_INTRINSIC_DIMENSION = INSUFFICIENT_EVIDENCE
PROJECTIVE_DIMENSION = NOT_APPLICABLE_UNTIL_PROJECTIVE_STRUCTURE_EXISTS
LATENT_STATE = REPRESENTATIONAL_HYPOTHESIS
```

## 6. Vistas candidatas de ConcordIA

Sea

\[
C_t=(Z_t,Self_t,World_t,History_t,Goals_t,Uncertainty_t,Evidence_t).
\]

Pueden definirse vistas generales:

\[
\Pi_{self}(C_t)=Self_t,\quad
\Pi_{world}(C_t)=World_t,\quad
\Pi_{trace}(C_t)=(History_t,Evidence_t),
\]

\[
\Pi_{policy}(C_t)=\text{información disponible para seleccionar política}.
\]

Estas son lecturas o transformaciones de datos, no aplicaciones proyectivas demostradas.

Una vista MOC candidata sería

\[
\Pi_{MOC}(C_t)=(P_t,Eaf_t,Act_t,V_t,S_t).
\]

Su estatus es **HYPOTHESIZED** y debe respetar:

- \(Act_\psi\neq\) conducta o acción de salida;
- \(Eaf_\psi\neq\) afecto fenomenal demostrado;
- \(V_\psi\neq\) cualquier recompensa por definición;
- \(S_\psi\) no borra la frontera interno/externo;
- \(P_\psi\) no equivale automáticamente a tokens, vector o embedding;
- \(G_\psi\neq\Phi_\psi\neq\Xi_\psi\), sin identificarlos con `Self_t`.

## 7. Invariantes candidatos

Un invariante bajo una familia de transformaciones \(\mathcal T\) es una función \(I\) tal que

\[
I(Tz)=I(z)\quad\forall T\in\mathcal T.
\]

Primero debe definirse \(\mathcal T\). Posibles invariantes computacionales, no necesariamente proyectivos, incluyen:

- linaje y procedencia de una afirmación;
- consistencia de identificadores bajo cambio de formato;
- relaciones de dependencia causal bajo reparametrización admitida;
- clases de equivalencia observacional;
- restricciones lógicas y permisos que sobreviven a serialización;
- orden parcial de eventos cuando cambia el reloj o la interfaz.

Invariantes específicamente proyectivos, como incidencia o razón doble, sólo son candidatos si existen puntos colineales y transformaciones proyectivas operacionalizadas. La razón doble no debe llamarse «armónica» salvo que su valor sea matemáticamente \(-1\) bajo una convención declarada. Ninguna de estas condiciones está demostrada para estados MOC o de ConcordIA.

## 8. Experimentos mínimos

### EXP-PROJ-001 — Identificabilidad multi-vista

1. Generar estados globales controlados \(z\) con variables ocultas conocidas por el banco de prueba.
2. Emitir vistas \(\Pi_1(z),\ldots,\Pi_m(z)\).
3. Reconstruir \(\hat z=R(\Pi_1(z),\ldots,\Pi_m(z))\).
4. Comparar con baselines de vista única, predictor por prevalencia y modelo con acceso global.
5. Reportar exactitud por campo, entropía residual de la fibra, calibración y casos indistinguibles.

Falsador de identificabilidad global: dos estados admitidos \(z\neq z'\) con todas las vistas iguales. Un solo contraejemplo basta para rechazar identificabilidad global del dominio declarado.

### EXP-PROJ-002 — Pérdida por vista

Para cada \(\Pi_i\), medir qué tareas o consultas \(Q_j(z)\) siguen resolviéndose. Estimar

\[
\Delta_{ij}=Performance(Q_j\mid Z)-Performance(Q_j\mid\Pi_i(Z)).
\]

La pérdida es relativa a tareas; una vista puede preservar una propiedad y destruir otra.

### EXP-PROJ-003 — Proyectivo contra alternativas

Comparar, con los mismos datos y penalización de complejidad:

1. lectura categórica/relacional;
2. modelo afín o lineal;
3. mapa no lineal general;
4. modelo proyectivo con equivalencia de escala;

Evaluar predicción fuera de muestra, estabilidad a transformaciones pre-registradas e invariantes. La hipótesis proyectiva sobrevive sólo si obtiene ventaja replicable y los invariantes específicos aparecen donde el modelo los predice.

### EXP-PROJ-004 — Intervención en variables ocultas

Cambiar una variable de \(Z_t\) manteniendo fija una vista parcial. Si cambia conducta o política mientras \(\Pi_i(Z_t)\) no cambia, esa vista es insuficiente para esa tarea. Esto no prueba una «dimensión superior» geométrica; prueba información funcional omitida.

### EXP-MOC-001 — Valor incremental de la vista MOC

Operacionalizar los cinco campos bajo revisión semántica y comparar:

\[
Base\quad vs\quad Base+\Pi_{MOC}(C_t)
\]

en predicción temporal, detección de contradicciones y selección regulada. Exigir acuerdo entre anotadores, ablation por campo y comparación con cinco campos arbitrarios de igual capacidad. Si no hay mejora replicable o si una representación más simple explica lo mismo, `MOC_PROJECTION_VALUE = NOT_SUPPORTED` para la tarea ensayada.

## 9. Falsadores y decisiones

| Hipótesis | Evidencia requerida | Falsador |
|---|---|---|
| Existe un estado global útil | Mejora reproducible de predicción/control al incluir variables globales definidas | La tupla global no añade información o sólo renombra registros ya disponibles. |
| Las vistas reconstruyen el estado | Reconstrucción identificable o calibrada en dominio predefinido | Estados distintos con vistas idénticas y consecuencias relevantes distintas. |
| Hay mayor dimensión intrínseca | Estimación estable bajo ruido, muestreo y métodos, con ventaja sobre menor dimensión | Modelo menor iguala desempeño e invariantes o la dimensión estimada es inestable. |
| Hay estructura proyectiva real | Escala como equivalencia válida, mapas proyectivos e invariantes específicos | Cambiar escala altera significado; fallan invariantes; mapa general más simple iguala resultados. |
| MOC es una vista informativa | Valor incremental fuera de muestra y semántica reproducible | No supera controles de igual capacidad o requiere identificar `Act` con conducta u otras violaciones. |
| Existe lifting fiel | Sección/reconstructor estable con error acotado y calibrado | Múltiples lifts incompatibles reciben certeza injustificada. |

## 10. Contraejemplos que bloquean inferencias rápidas

1. Un identificador único apunta a una base de datos enorme: «un punto» referencia información, pero no la contiene intrínsecamente sin el almacén y decodificador.
2. Un autoencoder reconstruye prompts frecuentes: esto puede ser compresión estadística con pérdida, no embedding inyectivo.
3. Cinco números se dibujan en coordenadas homogéneas: la notación no hace que la equivalencia de escala sea semánticamente válida.
4. Dos estados con idéntico `Self_t` pero distinta herramienta oculta producen políticas diferentes: `Self_t` no identifica el estado global.
5. Varias vistas coinciden porque derivan del mismo registro: la multiplicidad de vistas no aporta evidencia independiente.
6. Una razón permanece estable por construcción del preprocesamiento: no demuestra un invariante de la dinámica subyacente.

## 11. Dictamen conservador

En el estado actual, el marco adecuado es el de **mapas generales desde un sistema relacional temporal hacia vistas parciales**, con fibras, equivalencia observacional y pruebas de reconstrucción. Espacios cociente y secciones aportan lenguaje formal inmediato. La geometría proyectiva estricta sólo será adecuada si se demuestra equivalencia por escala, estructura de incidencia, transformaciones inducidas linealmente e invariantes diferenciales. No hay base para inferir dimensión geométrica superior desde riqueza informacional ni para identificar una vista MOC con el estado global.

```text
GLOBAL_STATE_MODEL = HYPOTHESIZED
PARTIAL_VIEW_MODEL = SUPPORTED_AS_FORMALISM
GLOBAL_IDENTIFIABILITY = INSUFFICIENT_EVIDENCE
HIGHER_DIMENSION_HYPOTHESIS = INSUFFICIENT_EVIDENCE
PROJECTIVE_HYPOTHESIS = INSUFFICIENT_EVIDENCE
PROJECTIVE_INVARIANTS_IN_MOC = NOT_SUPPORTED
MOC_PROJECTION_VALUE = INSUFFICIENT_EVIDENCE
PHENOMENAL_INFERENCE_FROM_PROJECTION = NOT_SUPPORTED
```
