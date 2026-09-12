# Validación estructural mínima de MOC y concordIA

**Fecha:** 2026-08-15  
**Estatus:** `RESEARCH_ONLY`, `NON_CANONICAL`, `NON_CLINICAL`, `NO_EMPIRICAL_VALIDATION`  
**Antecedente:** `INFORME_MOC_CONCORDIA_ESTRUCTURA_MATEMATICA_MINIMA_2026-08-15.md`  
**Regla:** ninguna relación se eleva por elegancia, frecuencia textual, pruebas locales o geometría previa.

## Escala de evidencia

| Nivel | Significado usado aquí |
|---:|---|
| 0 | consecuencia matemática general o coincidencia combinatoria |
| 1 | analogía o hipótesis estructural |
| 2 | compatible con documentación MOC |
| 3 | formalización computable y falsable |
| 4 | evidencia experimental reproducible |
| 5 | replicación independiente o evidencia externa suficiente |

Los documentos MOC pueden establecer nivel 2 sobre su semántica interna. No producen por sí mismos nivel 4–5. Los validadores actuales reproducen reglas declaradas sobre casos sintéticos/documentales; no prueban que la estructura describa experiencias reales.

## 1. Resumen ejecutivo

La investigación reduce la hipótesis anterior

\[
\mathfrak M=(P,X,\mathcal R,\Theta,\mathcal T,\mathcal I,\mathcal O)
\]

a un objeto matemático más simple:

\[
\boxed{\mathfrak L=(\mathcal S,A,\longrightarrow,\lambda)}
\]

un **sistema de transición etiquetado con estados relacionales tipados**. Cada estado (s\in\mathcal S) contiene una asignación parcial de valores a cinco tipos de componente, afirmaciones relacionales, contexto y provenance. (A) contiene operadores; (s\xrightarrow{a}s') registra una transición; (\lambda) etiqueta lo observado, declarado, inferido, derivado, hipotético o rechazado.

Esta reducción no elimina información: (P,X,\mathcal R,\Theta) se incorporan al esquema del estado; (\mathcal T) se vuelve la relación de transición; (\mathcal I) se expresa como predicados sobre estados/transiciones; (\mathcal O) se expresa mediante (\lambda) y provenance. En software conviene mantener esos campos separados para auditar, aunque matemáticamente sean absorbibles.

Hallazgos:

1. **M0 no basta para el MOC documentado:** los cinco tipos aislados pierden relaciones, contexto y bucles. Sí sirve como baseline obligatorio.
2. **Las diez parejas tienen soporte documental nominal**, porque los desarrollos de componentes describen cada cruce. Todas son contextuales y tipadas; ninguna posee evidencia observacional externa. El soporte simple es completo, pero no justifica diez copias de una única relación simétrica. (K_5) asciende a `SUPPORTED_SUBSTRUCTURE` sólo como esqueleto no tipado de relaciones declaradas (nivel 2).
3. **Ninguna de las diez ternas está demostrada como interacción irreducible.** Los casos narrativos combinan varios componentes, pero no comparan un término ternario contra todos los términos binarios. No deben crearse 2-símplices semánticos.
4. **Las cinco cuaternas carecen de estatuto MOC especial demostrado.** Su valor actual es experimental: ablación, reconstrucción y detección de asimetrías.
5. **El cierre simplicial no está justificado.** Que el Pentacoro se evalúe como configuración completa no implica que cada subconjunto sea una unidad relacional válida. El hipergrafo es más conservador que el complejo simplicial.
6. **La temporalidad es esencial documentalmente:** los bucles basal y activo distinguen observación, evaluación, elección, ajuste y nueva experiencia. Por ello M5 aporta estructura que M0–M4 estáticos pierden.
7. **La geometría proyectiva no tiene todavía observable elegible.** Se mantiene como módulo hipotético, no como estructura central.
8. **El 4-símplex no vuelve como candidato estructural fuerte.** Clasificación actual: `SUPPORTED_SUBSTRUCTURE` para su 1-esqueleto abstracto únicamente; `REPRESENTATIONAL_ONLY` para caras de orden 2–4 y realización geométrica.

Conclusión estricta:

\[
\boxed{\text{mínimo justificable hoy}=\text{sistema de transición etiquetado}}
\]

\[
\boxed{\text{estado mínimo}=\text{registro tipado de cinco componentes + relaciones afirmadas + contexto + provenance}}
\]

\[
\boxed{\text{estructura superior ganada}=\text{soporte binario documental completo, no }K_5\text{ homogéneo}}
\]

## 2. Estructura mínima revisada

### 2.1 Reducción término por término

| Término anterior | ¿Indispensable? | Reducción | Observable/computable | Pérdida si se elimina |
|---|---|---|---|---|
| (P) | sí, semánticamente | tipos dentro del esquema de estado | identificadores computables; contenido interpretado | se pierde la distinción de los cinco roles |
| (X) | sí | asignación tipada (x_s:p\mapsto X_p\cup\{\bot\}) | estados categóricos/estructurados; algunos atributos | sólo quedarían nombres sin estado |
| (\mathcal R) | sí para M1+ | afirmaciones relacionales dentro de (s) | aridad, tipo, dirección, evidencia | se confunden configuraciones con iguales marginales |
| (\Theta) | semánticamente sí; matemáticamente absorbible | atributos/nodos contextuales de (s) | parcialmente observable e inferido | se confunden casos con iguales componentes y distinto alcance |
| (\mathcal T) | sí para MOC dinámico | relación etiquetada (\to\) | secuencias y operadores | se confunden estados con procesos |
| (\mathcal I) | no como conjunto primitivo | predicados sobre (s\) y (s\to s') | validadores | no se pierde si los predicados se conservan |
| (\mathcal O) | no como conjunto primitivo, sí como interfaz empírica | etiquetado (\lambda), medición y provenance | observaciones/anotaciones | sin él no puede contrastarse el modelo |

### 2.2 Forma mínima

Un estado se representa como:

\[
s=(x,H,\theta,q),
\]

donde (x) es una asignación parcial tipada; (H) un conjunto de afirmaciones relacionales; (\theta) el contexto delimitado; (q) evidencia/provenance. Una transición:

\[
(x_t,H_t,\theta_t,q_t)\xrightarrow{a_t}
(x_{t+1},H_{t+1},\theta_{t+1},q_{t+1}).
\]

El hipergrafo no es la ontología: es una codificación posible de (H). Si (H=\varnothing), se recupera M0. Si todas las afirmaciones son binarias, M1/M2. Si aparecen aridades superiores, M3. Si además existe cierre descendente, M4. La temporalidad agrega M5; M6 requiere coordenadas adicionales.

**Nivel:** la definición es nivel 3; la afirmación de que corresponde a MOC real permanece en nivel 2.

## 3. Operacionalización de los cinco componentes

Fuente semántica principal: `MOC-PENT-001` define (P_\psi,Eaf_\psi,Act_\psi,V_\psi,S_\psi). Las columnas siguientes son especificaciones de medición propuestas, no escalas validadas.

| Componente | Tipo/dominio | Observable candidato | Inferido/interpretado | Representación segura inicial | Incertidumbre crítica |
|---|---|---|---|---|---|
| (P_\psi) | pensamiento, definición, interpretación | enunciado delimitado, reformulación, selección entre etiquetas | significado operativo implícito | texto + categoría nominal + múltiples etiquetas | discrepancia entre definición declarada y operativa |
| (Eaf_\psi) | emoción/afecto situado | autoetiqueta o etiqueta del caso sintético, intensidad sólo si escala definida | tono implícito y función informativa | conjunto nominal/ordinal con confianza | no confundir emoción con verdad o mandato |
| (Act_\psi) | acción, no acción, pauta expresiva interna | evento/omisión/pausa delimitada y secuencia | patrón y relación con elección | evento categórico + tiempo + observabilidad | conducta exteriorizada es derivada, no el mismo objeto |
| (V_\psi) | valores/dirección | valor nombrado y criterio situado | valor implícito/prestado/conflicto | conjunto nominal jerárquico + prioridad contextual, no escalar global | inferir valores desde emoción o conducta puede ser circular |
| (S_\psi) | situación encarnada: cuerpo, contexto, recursos, límites, tiempo/espacio | hechos contextuales declarados, disponibilidad, restricciones | pertinencia y suficiencia contextual | objeto estructurado con campos y desconocidos | no reducir encarnación a una sola variable “contexto” |

### Prueba de acuerdo propuesta

Unidad: caso sintético congelado, sin dictamen previo visible. Cada evaluador produce por componente:

```text
span_evidence
semantic_label
state_label
direct_or_inferred
confidence_0_1
alternative_labels
missing_information
```

Medidas: acuerdo exacto para campos nominales; Krippendorff (\alpha) o kappa apropiado para múltiples evaluadores; correlación/clasificación ordinal sólo donde la escala se justifique; calibración de confianza; adjudicación ciega de desacuerdos. Falla inicial si un componente no alcanza acuerdo por encima de un baseline de prevalencia en dos conjuntos independientes o si los desacuerdos provienen de definiciones MOC incompatibles.

## 4. Auditoría de las diez parejas

“Definida” significa que existe una regla/pregunta documental explícita. No significa relación observada, causal, simétrica ni estable.

| ID | Pareja | Soporte documental resumido | Estado primario | Nivel | Decisión |
|---|---|---|---|---:|---|
| B01 | (P-Eaf) | definición puede organizar/ser cuestionada por emoción | `CONTEXT_DEPENDENT` | 2 | arista tipada candidata |
| B02 | (P-Act) | definición abre/cierra acción; acción revela definición | `CONTEXT_DEPENDENT` | 2 | posiblemente dirigida en ambos sentidos |
| B03 | (P-V) | significado puede conservar o contradecir dirección | `CONTEXT_DEPENDENT` | 2 | arista tipada candidata |
| B04 | (P-S) | definición reconoce o niega condiciones situadas | `CONTEXT_DEPENDENT` | 2 | arista tipada candidata |
| B05 | (Eaf-Act) | acción expresa/modula/descarga emoción; emoción no decide acción | `CONTEXT_DEPENDENT` | 2 | no causalizar sin diseño |
| B06 | (Eaf-V) | emoción informa que un valor fue tocado; no lo sustituye | `CONTEXT_DEPENDENT` | 2 | arista tipada candidata |
| B07 | (Eaf-S) | afecto es situado; contexto limita lectura/acción | `CONTEXT_DEPENDENT` | 2 | arista tipada candidata |
| B08 | (Act-V) | acción puede encarnar, tensionar o contradecir dirección | `CONTEXT_DEPENDENT` | 2 | salida exterior puede ser derivada |
| B09 | (Act-S) | toda acción/no acción ocurre bajo recursos y límites | `CONTEXT_DEPENDENT` | 2 | arista tipada candidata |
| B10 | (V-S) | contexto habilita/limita dirección; valor abstracto puede negar límites | `CONTEXT_DEPENDENT` | 2 | arista tipada candidata |

Evidencia documental directa: `MOC-VPSI-001` enumera valor–definición, valor–emoción, valor–conducta y valor–contexto; `MOC-DPSI-001`, `MOC-EPSI-001` y `MOC-CON-001` contienen secciones explícitas para los cruces restantes.

### ¿Es (E=\binom P2)?

- **Sí**, si (E) significa únicamente “existe al menos una afirmación documental que vincula esos dos tipos”.
- **No demostrado**, si (E) significa “existe una relación observada reproducible”.
- **No**, si (E) significa “las diez parejas instancian una misma relación homogénea, simétrica y no contextual”.

Por tanto:

\[
G_{support}\cong K_5 \quad\text{(nivel 2, soporte documental no tipado)}
\]

pero la estructura fiel es un multigrafo dirigido/contextual con etiquetas, no (K_5) simple. Cualquier arista concreta debe portar `DECLARED` y su fuente; no `OBSERVED`.

## 5. Auditoría de las diez ternas

Definición operacional de interacción ternaria irreducible. Para un objetivo (Y), contexto (\theta) y terna (i,j,k), existe evidencia ternaria si el mejor modelo con términos de orden (\le2):

\[
\hat Y=f_i+f_j+f_k+f_{ij}+f_{ik}+f_{jk}
\]

es superado fuera de muestra por:

\[
\hat Y'=\hat Y+f_{ijk},
\]

con ganancia preregistrada, calibración aceptable, penalización de complejidad y replicación. Alternativamente puede medirse sinergia informacional, pero la elección de descomposición debe fijarse antes; la PID distingue información única, redundante y sinérgica, y muestra que la “sinergia” no se reduce a información mutua marginal ([Wollstadt, Schmitt y Wibral, JMLR 2023](https://www.jmlr.org/papers/v24/21-0482.html)).

| ID | Terna | Evidencia de coaparición | Prueba de irreducibilidad | Estado | Decisión |
|---|---|---|---|---|---|
| T01 | P–Eaf–Act | casos narrativos integrados | no | `INSUFFICIENT_EVIDENCE` | no hiperarista aún |
| T02 | P–Eaf–V | casos narrativos integrados | no | `INSUFFICIENT_EVIDENCE` | no hiperarista aún |
| T03 | P–Eaf–S | casos narrativos integrados | no | `INSUFFICIENT_EVIDENCE` | no hiperarista aún |
| T04 | P–Act–V | casos narrativos integrados | no | `INSUFFICIENT_EVIDENCE` | no hiperarista aún |
| T05 | P–Act–S | casos narrativos integrados | no | `INSUFFICIENT_EVIDENCE` | no hiperarista aún |
| T06 | P–V–S | casos narrativos integrados | no | `INSUFFICIENT_EVIDENCE` | no hiperarista aún |
| T07 | Eaf–Act–V | casos narrativos integrados | no | `INSUFFICIENT_EVIDENCE` | no hiperarista aún |
| T08 | Eaf–Act–S | casos narrativos integrados | no | `INSUFFICIENT_EVIDENCE` | no hiperarista aún |
| T09 | Eaf–V–S | casos narrativos integrados | no | `INSUFFICIENT_EVIDENCE` | no hiperarista aún |
| T10 | Act–V–S | casos narrativos integrados | no | `INSUFFICIENT_EVIDENCE` | no hiperarista aún |

Coaparición en una ficha de cinco campos no es interacción. Los validadores actuales reciben métricas ya asignadas y aplican reglas; no estiman (f_{ijk}) ni comparan órdenes.

## 6. Auditoría de las cinco cuaternas

| Cuaterna | Ausente | Posible función experimental | Evidencia especial actual | Estado |
|---|---|---|---|---|
| Eaf–Act–V–S | P | reconstruir interpretación activa | ninguna | `INSUFFICIENT_EVIDENCE` |
| P–Act–V–S | Eaf | restringir etiqueta afectiva | ninguna | `INSUFFICIENT_EVIDENCE` |
| P–Eaf–V–S | Act | predecir acción/no acción | ninguna | `INSUFFICIENT_EVIDENCE` |
| P–Eaf–Act–S | V | inferir dirección/valor | ninguna; alto riesgo de circularidad | `INSUFFICIENT_EVIDENCE` |
| P–Eaf–Act–V | S | inferir contexto ausente | probablemente no identificable sin datos externos | `INSUFFICIENT_EVIDENCE` |

No hay base para tratar las cinco cuaternas como equivalentes. (S_\psi) contiene restricciones exógenas que pueden no deducirse de los otros cuatro; (V_\psi) y (P_\psi) pueden ser parcialmente inferidos pero con múltiples explicaciones; (Act_\psi) puede ser observable más directamente; (Eaf_\psi) puede quedar subdeterminado. Estas son hipótesis de asimetría, no resultados.

## 7. Experimento de ablación (5\leftrightarrow4)

Para cada (i):

\[
H_{0,i}:I(X_i;X_{-i},\Theta)\le I(X_i;B_i)
\]

frente a

\[
H_{1,i}:I(X_i;X_{-i},\Theta)>I(X_i;B_i),
\]

donde (B_i) es un baseline preregistrado (prevalencia, contexto solo o mejor componente único). En práctica no se requiere estimar información mutua si el tamaño muestral es bajo: puede compararse log-loss/Brier para etiquetas, MAE ordinal cuando proceda y cobertura/calibración de conjuntos predictivos.

### Protocolo

1. Congelar ontología, etiquetas y unidad OLC.
2. Dividir por familia narrativa/contexto, no por frases aleatorias, para evitar fuga léxica.
3. Ocultar toda evidencia directa de (p_i), incluidos sinónimos.
4. Comparar baseline, contexto solo, mejores pares, cuatro componentes y texto completo.
5. Igualar presupuesto de parámetros o penalizar por MDL/BIC; MDL formaliza la preferencia por modelos que comprimen datos y modelo sin favorecer complejidad gratuita ([Grünwald y Roos](https://arxiv.org/abs/1908.08484)).
6. Evaluar predicción, calibración, abstención e intervalos/conjuntos de incertidumbre.
7. Repetir por componente y contexto en conjunto externo congelado.

### Refutación exacta de (H_{1,i})

(H_{1,i}) se refuta provisionalmente si el modelo (X_{-i}+\Theta) no supera al baseline preregistrado por el margen mínimo (\delta) en el conjunto externo, el intervalo de confianza de la diferencia incluye cero y no aparece ventaja calibrada en una réplica independiente. Una mejora sólo en entrenamiento, sólo en una familia léxica o perdida al controlar contexto no cuenta.

### Resultado agregado

La “correspondencia elemento–cuaterna” gana contenido sólo para los (i) que superen ese protocolo. Si cuatro de cinco lo hacen, no se sigue que la quinta cuaterna tenga el mismo estatuto.

## 8. Análisis temporal

Una representación estática pierde al menos:

- orden entre descomposición (\Xi_\psi), evaluación (\Phi_\psi), elección (C_\psi) y ajuste;
- diferencia entre retroalimentación basal y bucle activo;
- cambio de estado frente a cambio de relación o de contexto;
- deuda/evidencia acumulada;
- no conmutatividad potencial de operaciones;
- reversibilidad y pérdida de información.

Tipos de evento propuestos:

| Evento | Cambia | Debe conservar |
|---|---|---|
| `OBSERVE` | evidencia/confianza | estado fuente y provenance |
| `REINTERPRET` | (P), quizá relaciones | evidencia previa, no sobrescribirla |
| `AFFECT_UPDATE` | (Eaf) | tiempo/contexto |
| `ACT_OR_PAUSE` | (Act), salida derivada | distinción elección/conducta |
| `CONTEXT_CHANGE` | (S/\theta) | componentes no observados como desconocidos |
| `VALUE_CLARIFY` | representación de (V) | valor previo como antecedente, no error borrado |
| `RELATION_UPDATE` | (H) | estado epistemológico de cada arista |
| `EVIDENCE_UPDATE` | (q,\lambda) | claim original y fuente |

Invariantes candidatos nivel 2: identidad de los cinco tipos; conducta no se vuelve sexto componente; (\Xi_\psi\ne\Phi_\psi); alcance y provenance no desaparecen. Invariantes empíricos: ninguno demostrado.

## 9. Hipergrafo frente a complejo simplicial

| Pregunta | Hipergrafo | Complejo simplicial | Evidencia MOC actual |
|---|---|---|---|
| ¿permite una terna sin pares? | sí | no | no probado, pero debe poder representarse |
| ¿impone cierre por caras? | no | sí | no documentado como regla |
| ¿distingue una relación conjunta de sus subrelaciones? | sí | requiere pesos/cochains adicionales | necesario para probar irreducibilidad |
| ¿admite tipos/dirección fácilmente? | sí | requiere estructura enriquecida | MOC usa tipos y procesos dirigidos |
| ¿es más parsimonioso con pocas hiperaristas? | sí | no siempre | favorecido provisionalmente |

Contraejemplo MOC-compatible: una regla “la definición (P), el contexto (S) y el valor (V) conjuntamente hacen elegible una acción” puede depender de los tres sin afirmar que (P-V), (P-S) y (V-S) tengan cada una el mismo efecto aislado. Si datos apoyaran esa regla pero no sus caras, un complejo simplicial semántico sería falso y un hipergrafo correcto.

La literatura confirma que redes de hipergrafos pueden codificar correlaciones superiores, mientras redes simpliciales añaden estructura de caras y mayor expresividad que message passing sobre grafos; esto es capacidad matemática general, no evidencia MOC ([Feng et al.](https://arxiv.org/abs/1809.09401); [Bodnar et al.](https://arxiv.org/abs/2103.03212)).

**Veredicto:** M3 es contenedor extensible; M4 permanece hipótesis sin soporte.

## 10. Competencia completa entre modelos

Todos los modelos reciben exactamente las mismas particiones, etiquetas y atributos permitidos.

| Modelo | Entrada adicional | Hipótesis comprada | Criterio de victoria | Estado actual |
|---|---|---|---|---|
| M0 componentes | cinco estados | independencia/concatenación | baseline | necesario, no suficiente |
| M1 grafo parcial | aristas declaradas | pares específicos | mejora externa penalizada | nivel 2–3 |
| M2 (K_5) | diez pares | completitud de soporte | mejora sobre M1 sin sobreajuste | soporte documental; efecto no probado |
| M3 hipergrafo | hiperrelaciones elegidas | orden superior irreducible | mejora sobre todos los términos inferiores | no probado |
| M4 simplicial | cierre por caras | jerarquía descendente | mejora/estabilidad sobre M3 | no probado |
| M5 dinámico | secuencia y operadores | dependencia temporal | mejora sobre instantáneas y orden permutado | nivel 2; probar |
| M6 proyectivo | coordenadas/homografías | invariancia proyectiva | cross-ratio estable y predictivo | sin observable |
| vector plano | embedding marginal | relaciones absorbibles | baseline ML | útil pero potencialmente lossy |

Métricas primarias: log-loss o Brier; exactitud/F1 como secundarias; calibration error y curvas de riesgo-cobertura; MDL/BIC o complejidad efectiva; prueba de permutación emparejada; estabilidad entre semillas; evaluación por familia/contexto; latencia/memoria; completitud de provenance. La incertidumbre predictiva debe evaluarse como propiedad del modelo y aproximación, no como un número universal ([Schweighofer et al., UAI 2025](https://proceedings.mlr.press/v286/schweighofer25a.html)).

Regla de selección:

\[
\text{elegir el modelo menos complejo cuyo beneficio externo replicado}\ge\delta.
\]

## 11. Contraejemplos adversariales

1. **Cinco sin (K_5):** P y Eaf están documentados; Act desconocido; V no declarado; S sólo limita. Un grafo parcial es válido, (K_5) inventa seis aristas del caso.
2. **Hipergrafo sin complejo:** salida cambia sólo cuando P, V y S aparecen conjuntamente; ninguno de los tres pares predice. La hiperarista existe, sus caras predictivas no.
3. **Cuatro no predicen quinto:** mismo P/Eaf/Act/V bajo dos restricciones externas S incompatibles. (S) no es identificable desde la cuaterna.
4. **Asimetría fuerte:** Act es observable como pausa; V permanece indeterminado. Reconstruir Act desde cuatro puede ser fácil, reconstruir V no.
5. **Vector pierde relación:** dos casos comparten exactamente los mismos cinco histogramas de etiquetas, pero uno tiene P→Act y otro S→Act. Concatenación marginal idéntica, estructura distinta.
6. **Geometría añade información:** ubicar cinco etiquetas en pentágono regular introduce ciclo, distancias, ángulos y simetría (D_5) ausentes.
7. **Superficie distinta, estructura igual:** “pospongo por perfeccionismo” y “no envío hasta que sea impecable” codifican la misma relación P→Act bajo V/S equivalentes.
8. **Superficie similar, estructura distinta:** “pauso para revisar” puede ser Act concordante con límite temporal o evitación sin borde; palabras similares, transición distinta.
9. **(K_5) no mejora:** todos los targets dependen de P y S; nueve aristas adicionales ajustan ruido.
10. **Dinámica necesaria:** mismo estado final, pero una ruta conserva provenance/elección y otra borra evidencia; una instantánea las iguala indebidamente.
11. **Proyectivo espurio:** un embedding elegido después de ver etiquetas produce cross-ratio estable in-sample y falla al cambiar narrativas.
12. **Causalidad espuria:** Eaf y Act covarían porque S causa ambos; la arista Eaf→Act desaparece al intervenir/controlar S.

## 12. Predicciones estructurales falsables

### SP-01 — Valor de relaciones binarias

```text
ID: SP-01
CLAIM: M1 supera M0 en casos con iguales componentes marginales y distinta relación.
MODEL: M1
OBSERVABLE: etiqueta de estado MOC y relación activa
DATA_REQUIRED: pares contrafactuales estructurales, >=2 familias externas
BASELINE: M0 con igual presupuesto
MEASUREMENT: delta log-loss, calibración y exactitud emparejada
ALTERNATIVE_EXPLANATION: fuga léxica
DISCONFIRMING_RESULT: delta <= 0 o desaparece al parafrasear
REPLICATION_CRITERION: misma dirección en conjunto externo congelado
STATUS: HYPOTHESIZED
```

### SP-02 — Completitud útil de (K_5)

```text
ID: SP-02
CLAIM: M2 mejora M1 porque relaciones omitidas contienen señal.
MODEL: M2
OBSERVABLE: predicción fuera de muestra
DATA_REQUIRED: casos que cubran las 10 parejas
BASELINE: M1 seleccionado sólo por evidencia
MEASUREMENT: MDL y delta log-loss penalizado
ALTERNATIVE_EXPLANATION: mayor capacidad paramétrica
DISCONFIRMING_RESULT: M2 no mejora o empeora calibración
REPLICATION_CRITERION: beneficio en dos particiones por contexto
STATUS: HYPOTHESIZED
```

### SP-03 — Reconstrucción de (P_\psi)

```text
ID: SP-03
CLAIM: Eaf,Act,V,S restringen P por encima de baseline.
MODEL: ablación Q_P
OBSERVABLE: etiqueta/conjunto de interpretaciones P
DATA_REQUIRED: P anotado con alternativas y evidencia
BASELINE: prevalencia + S solo
MEASUREMENT: log-loss, cobertura y tamaño del conjunto predictivo
ALTERNATIVE_EXPLANATION: palabras que revelan P
DISCONFIRMING_RESULT: sin mejora tras eliminar pistas directas
REPLICATION_CRITERION: réplica ciega por familia narrativa
STATUS: HYPOTHESIZED
```

### SP-04 — Reconstrucción de (Eaf_\psi)

```text
ID: SP-04
CLAIM: P,Act,V,S restringen Eaf por encima de baseline.
MODEL: ablación Q_Eaf
OBSERVABLE: etiqueta afectiva multilabel
DATA_REQUIRED: afecto anotado independientemente
BASELINE: prevalencia + P solo
MEASUREMENT: proper score y calibración
ALTERNATIVE_EXPLANATION: estereotipos narrativos
DISCONFIRMING_RESULT: no mejora externa o alta sobreconfianza
REPLICATION_CRITERION: segundo conjunto con vocabulario distinto
STATUS: HYPOTHESIZED
```

### SP-05 — Reconstrucción de (Act_\psi)

```text
ID: SP-05
CLAIM: P,Eaf,V,S predicen Act mejor que baseline.
MODEL: ablación Q_Act
OBSERVABLE: acción/no acción/pausa delimitada
DATA_REQUIRED: transición o acción oculta
BASELINE: frecuencia por contexto
MEASUREMENT: log-loss y exactitud temporal
ALTERNATIVE_EXPLANATION: guion del caso determina acción
DISCONFIRMING_RESULT: múltiples acciones equivalentes no calibradas
REPLICATION_CRITERION: generalización a acciones no vistas
STATUS: HYPOTHESIZED
```

### SP-06 — Reconstrucción de (V_\psi)

```text
ID: SP-06
CLAIM: P,Eaf,Act,S restringen V sin circularidad.
MODEL: ablación Q_V
OBSERVABLE: conjunto de valores/direcciones admisibles
DATA_REQUIRED: V declarado y V inferido por evaluadores distintos
BASELINE: frecuencia + P solo
MEASUREMENT: cobertura, precisión y calibración
ALTERNATIVE_EXPLANATION: evaluadores proyectan valores desde conducta
DISCONFIRMING_RESULT: acuerdo no supera prevalencia o depende de Act
REPLICATION_CRITERION: anotadores independientes y auditoría de circularidad
STATUS: HYPOTHESIZED_HIGH_RISK
```

### SP-07 — Reconstrucción de (S_\psi)

```text
ID: SP-07
CLAIM: P,Eaf,Act,V no reconstruyen completamente S.
MODEL: ablación Q_S
OBSERVABLE: restricciones contextuales ocultas
DATA_REQUIRED: pares con componentes iguales y S distinto
BASELINE: mejor modelo de cuatro componentes
MEASUREMENT: error y entropía residual
ALTERNATIVE_EXPLANATION: S filtrado en el lenguaje
DISCONFIRMING_RESULT: S se predice de forma calibrada tras quitar pistas
REPLICATION_CRITERION: contextos contrafactuales controlados
STATUS: HYPOTHESIZED
```

### SP-08 — Asimetría de ablaciones

```text
ID: SP-08
CLAIM: las cinco pérdidas de ablación difieren establemente.
MODEL: cinco Q_i
OBSERVABLE: delta de rendimiento por componente
DATA_REQUIRED: mismo corpus con máscaras equivalentes
BASELINE: pérdidas intercambiables bajo S5
MEASUREMENT: contraste global + intervalos simultáneos
ALTERNATIVE_EXPLANATION: distintas dificultades de etiquetado
DISCONFIRMING_RESULT: perfiles intercambiables tras controlar fiabilidad
REPLICATION_CRITERION: orden parcial repetido en conjunto externo
STATUS: HYPOTHESIZED
```

### SP-09 — Interacción ternaria irreducible

```text
ID: SP-09
CLAIM: al menos una terna añade señal sobre todos sus términos <=2.
MODEL: M3
OBSERVABLE: target preregistrado
DATA_REQUIRED: diseño factorial o corpus suficiente por combinación
BASELINE: modelo jerárquico hasta pares
MEASUREMENT: delta log-loss penalizado y prueba de permutación
ALTERNATIVE_EXPLANATION: regularización distinta
DISCONFIRMING_RESULT: ninguna terna replica la ganancia mínima
REPLICATION_CRITERION: misma terna y signo en conjunto independiente
STATUS: HYPOTHESIZED
```

### SP-10 — Rechazo del cierre simplicial

```text
ID: SP-10
CLAIM: existe una hiperarista útil cuya al menos una cara no es útil.
MODEL: M3 vs M4
OBSERVABLE: utilidad predictiva por subconjunto
DATA_REQUIRED: casos factoriales de la hiperarista candidata
BASELINE: cierre por caras M4
MEASUREMENT: efectos e intervalos por cara
ALTERNATIVE_EXPLANATION: potencia insuficiente para las caras
DISCONFIRMING_RESULT: toda hiperarista replicada tiene todas sus caras útiles
REPLICATION_CRITERION: patrón en dos conjuntos con potencia preregistrada
STATUS: HYPOTHESIZED
```

### SP-11 — Valor de temporalidad

```text
ID: SP-11
CLAIM: M5 supera modelos estáticos en transiciones y salidas.
MODEL: M5
OBSERVABLE: siguiente estado/relación y deuda
DATA_REQUIRED: secuencias con marcas de operador
BASELINE: bolsa de estados sin orden
MEASUREMENT: log-loss y consistencia de trazas
ALTERNATIVE_EXPLANATION: más observaciones, no orden
DISCONFIRMING_RESULT: permutar tiempos no reduce rendimiento
REPLICATION_CRITERION: efecto en bucle basal y activo
STATUS: HYPOTHESIZED
```

### SP-12 — No conmutatividad

```text
ID: SP-12
CLAIM: al menos dos operadores documentados producen resultados distintos al invertir orden.
MODEL: M5
OBSERVABLE: estado/relación final bajo ab y ba
DATA_REQUIRED: casos sintéticos contrabalanceados
BASELINE: operador conmutativo
MEASUREMENT: tasa de divergencia preregistrada
ALTERNATIVE_EXPLANATION: cambios de contexto entre pasos
DISCONFIRMING_RESULT: ab y ba equivalentes bajo contexto controlado
REPLICATION_CRITERION: misma pareja en segunda batería
STATUS: HYPOTHESIZED
```

### SP-13 — Invariancia narrativa

```text
ID: SP-13
CLAIM: estructura igual bajo paráfrasis produce salida equivalente.
MODEL: sistema relacional tipado
OBSERVABLE: isomorfismo y salida MOC
DATA_REQUIRED: paráfrasis ciegas + adversariales
BASELINE: similitud léxica/vectorial
MEASUREMENT: consistencia intraestructura y discriminación interestructura
ALTERNATIVE_EXPLANATION: plantillas de generación
DISCONFIRMING_RESULT: salida sigue superficie más que estructura
REPLICATION_CRITERION: paráfrasis humanas independientes
STATUS: HYPOTHESIZED
```

### SP-14 — Valor de provenance

```text
ID: SP-14
CLAIM: provenance explícito mejora calibración de abstención y auditoría.
MODEL: concordIA con lambda/q
OBSERVABLE: errores aceptados, abstenciones correctas, trazabilidad
DATA_REQUIRED: claims con fuentes de calidad variable
BASELINE: mismas entradas sin provenance
MEASUREMENT: riesgo-cobertura y recuperación de fuente
ALTERNATIVE_EXPLANATION: provenance actúa como etiqueta de calidad directa
DISCONFIRMING_RESULT: no reduce riesgo ni mejora auditoría
REPLICATION_CRITERION: fuentes no vistas y auditor independiente
STATUS: HYPOTHESIZED
```

### SP-15 — Hipótesis proyectiva

```text
ID: SP-15
CLAIM: un observable específico conserva razón doble bajo reencuadres definidos.
MODEL: M6
OBSERVABLE: cross-ratio de cuatro anclas del mismo observable
DATA_REQUIRED: anclas, coordenadas y homografías preregistradas
BASELINE: modelos afín, monótono y no paramétrico
MEASUREMENT: error de invariancia y predicción externa
ALTERNATIVE_EXPLANATION: ajuste post hoc del embedding
DISCONFIRMING_RESULT: invarianza no supera baselines o falla fuera de muestra
REPLICATION_CRITERION: nuevo conjunto de reencuadres y anclas
STATUS: HYPOTHESIZED_LOW_PRIORITY
```

### SP-16 — Simetría (S_5) frente a tipos

```text
ID: SP-16
CLAIM: modelo tipado supera uno equivariante a permutaciones S5.
MODEL: M1/M5 tipado
OBSERVABLE: predicción y calibración
DATA_REQUIRED: casos balanceados por componente
BASELINE: parámetros compartidos S5
MEASUREMENT: delta MDL/log-loss
ALTERNATIVE_EXPLANATION: desbalance de etiquetas
DISCONFIRMING_RESULT: S5 igual o mejor tras balanceo
REPLICATION_CRITERION: resultado en corpus externo
STATUS: HYPOTHESIZED
```

## 13. Arquitectura provisional de concordIA

El archivo `esquema_concordia_experiencia_v0.schema.json` materializa una arquitectura append-only conceptual:

```text
ExperienceRecord
  components[5]
  relations[0..n]
  context
  transition?
  constraints[]
  observations[]
  provenance[]
```

Cada claim conserva:

```text
OBSERVED | DECLARED | INFERRED | DERIVED | HYPOTHESIZED | REJECTED
evidence_level: 0..5
provenance_ids[]
```

Reglas:

1. una inferencia crea un claim nuevo; no reescribe la observación;
2. una geometría se añade como claim/transformación hipotética, no como coordenadas “verdaderas” del dato original;
3. aristas e hiperaristas tienen aridad, tipo, dirección, contexto, nivel y prueba de irreducibilidad;
4. embeddings son artefactos derivados versionados;
5. una transición registra campos cambiados, predicados preservados y reversibilidad desconocida cuando no se demuestre;
6. los cinco componentes se mantienen tipados; conducta derivada puede almacenarse como observación/salida, no sexto componente.

## 14. Requisitos de datos

| Dataset | Unidad | Mínimo necesario | Riesgo principal |
|---|---|---|---|
| D0 ontología | definición/ejemplo/contraejemplo | aprobación semántica por componente | circularidad documental |
| D1 acuerdo | caso sintético × evaluador | etiquetas independientes + confianza + spans | pseudoindependencia |
| D2 pares | casos factoriales | variar una relación conservando marginales | fuga de superficie |
| D3 ablación | registros completos | máscaras sin sinónimos + targets | target inferido por mismo anotador |
| D4 orden superior | diseño factorial | cobertura de combinaciones y potencia | explosión combinatoria |
| D5 temporal | secuencia | operador, tiempo, estado pre/post, contexto | confundir observación con intervención |
| D6 invariancia | familias de narrativas | equivalencias/adversariales | plantillas triviales |
| D7 proyectivo | observable específico | anclas y transformaciones | embedding post hoc |

No se recomienda comenzar con personas reales. Primero: datos sintéticos congelados, anotación independiente, conjunto adversarial y comparación de modelos. Cualquier expansión empírica requiere autorización, ética, privacidad y diseño separados.

## 15. Experimentos computacionales propuestos

1. **E-CENSUS:** registrar las 25 combinaciones auditadas con status/provenance; entregable ya iniciado en CSV.
2. **E-IAA:** medir acuerdo de componentes y relaciones activas con paquete ciego.
3. **E-PAIR:** generar pares contrafactuales con marginales iguales y arista distinta.
4. **E-ABL5:** ejecutar cinco máscaras y baselines calibrados.
5. **E-TRI10:** modelos jerárquicos por cada terna con control de falsos descubrimientos.
6. **E-HYP-SIM:** dataset sintético que contenga hiperaristas con y sin cierre; verificar que el selector recupere la clase generadora.
7. **E-DYN:** comparar secuencial vs estático y orden real vs permutado.
8. **E-NONCOMM:** batería contrabalanceada de composición de operadores.
9. **E-NARR:** equivalencias y adversariales de superficie/estructura.
10. **E-PROV:** ablación de provenance y evaluación de riesgo-cobertura.
11. **E-MODEL-LADDER:** M0–M6 con presupuesto/penalización común.
12. **E-PROJ:** sólo después de aprobar observable y anclas.

Orden recomendado: E-CENSUS → E-IAA → E-PAIR/E-ABL5 → E-DYN → E-TRI10 → E-HYP-SIM → E-NARR/E-PROV. M6 queda al final.

## 16. Resultados positivos y negativos

### Positivos

- Cinco roles canónicos diferenciados: nivel 2.
- Todas las parejas poseen al menos una relación documental explícita: nivel 2.
- El soporte binario no tipado es completo: consecuencia del inventario documental, nivel 2.
- Existen bucles y operadores temporales documentados: nivel 2.
- Puede construirse ya una representación computable que preserve hipótesis y provenance: nivel 3 como ingeniería.
- Existe un protocolo local de acuerdo A1–A6 que puede reutilizarse y endurecerse.

### Negativos

- Cero parejas con evidencia observacional externa identificada.
- Cero ternas con irreducibilidad demostrada.
- Cero cuaternas con poder reconstructivo demostrado.
- Cero evidencia de cierre simplicial.
- Cero observable proyectivo operacionalizado.
- Cero justificación de métricas entre los cinco componentes en un espacio común más allá de proyecciones auxiliares declaradas.
- Las pruebas actuales validan contratos/reglas contra casos preparados; no seleccionan entre M0–M6.

## 17. Estructuras descartadas

| Estructura | Clasificación | Motivo |
|---|---|---|
| pentágono/pentagrama regular | `REPRESENTATIONAL_ONLY` | introduce ciclo, orden, métrica y simetría |
| razón áurea | `UNSUPPORTED` | no derivada ni predictiva |
| geometría sagrada | `UNSUPPORTED` | no falsable/operacionalizada |
| números piramidales | `UNSUPPORTED` | coincidencia enumerativa |
| tetrakis hexaedro | `UNSUPPORTED` | combinatoria ajena a los cinco roles |
| tetraedro 4+1 interno | `WEAK_CANDIDATE` | (V) es tipo especial pero sigue siendo componente |
| complejo simplicial completo | `REPRESENTATIONAL_ONLY` | cierre no demostrado |
| 4-símplex geométrico | `REPRESENTATIONAL_ONLY` | coordenadas/métrica/simetría no justificadas |

## 18. Estructuras que ganaron evidencia

| Estructura | Evidencia ganada | Nivel/estatus |
|---|---|---|
| cinco componentes tipados | canon/documentación | nivel 2 |
| multigrafo relacional contextual | diez parejas documentadas | nivel 2, `SUPPORTED_SUBSTRUCTURE` |
| (K_5) como soporte no tipado | inventario completo de parejas | nivel 2, sólo esqueleto |
| sistema de transición etiquetado | bucles + reducción matemática + esquema | nivel 2 MOC / nivel 3 computable |
| hipergrafo como contenedor | parsimonia y extensibilidad | nivel 1–3 de arquitectura, no evidencia de hiperaristas |
| provenance explícito | exigencia de autoridad/trazabilidad | nivel 2–3 |

## 19. ¿Qué tendría que demostrarse para que vuelva el 4-símplex?

| Condición | Evidencia requerida | Estado actual |
|---|---|---|
| completitud binaria | diez pares definidos/observados | definidos sí; observados no |
| ternas | diez interacciones o regla que justifique caras | ninguna irreducible |
| cierre por caras | toda interacción superior relevante conserva subinteracciones relevantes | no probado; contraejemplos plausibles |
| cinco cuaternas | función reconstructiva/restrictiva replicada | no probado |
| sistema completo | efecto de orden 5 no reducible | no probado |
| simetría | equivalencia o grupo de automorfismos justificado | contradicha parcialmente por tipos/asimetrías |
| temporalidad | dinámica compatible con caras/operadores del símplex | no especificada |
| geometría | coordenadas, métrica o estructura afín justificadas | ausente |
| predicción | ventaja sobre hipergrafo/sistema dinámico más simple | no evaluada |

Clasificación final desagregada:

```text
4-simplex 1-skeleton as untyped declared support: SUPPORTED_SUBSTRUCTURE
4-simplex face lattice: REPRESENTATIONAL_ONLY
4-simplex geometric realization: REPRESENTATIONAL_ONLY
4-simplex as strong MOC structure: REJECTED at current evidence
```

Para ascender a `STRONG_STRUCTURAL_CANDIDATE` tendría que: (a) replicar interacciones de órdenes 2–5; (b) demostrar cierre por caras; (c) explicar asimetrías mediante tipos/pesos sin vaciar la hipótesis; (d) incorporar transiciones; y (e) superar un hipergrafo dinámico tipado bajo penalización de complejidad.

## 20. Programa siguiente y regla de cierre

### Qué sabemos

\[
\boxed{\text{cinco tipos + diez vínculos documentales contextuales + dinámica declarada}}
\]

### Qué hemos descartado

\[
\boxed{\text{geometría concreta como necesidad actual; cierre simplicial; simetría homogénea}}
\]

### Qué puede computarse ya

\[
\boxed{\text{registros tipados, provenance, grafos parciales, transiciones y competencia M0–M5}}
\]

El esquema JSON y el inventario CSV adjuntos permiten comenzar sin alterar evidencia original ni canonizar hipótesis.

### Qué dato falta

\[
\boxed{\text{anotaciones independientes por componente/relación y secuencias pre/post}}
\]

También faltan casos factoriales que separen efectos marginales, pares, ternas y contexto.

### Qué experimento debe hacerse después

\[
\boxed{\text{E-IAA seguido de E-PAIR y E-ABL5}}
\]

No conviene entrenar una red hipergrafo/simplicial antes de demostrar que las etiquetas y relaciones pueden anotarse reproduciblemente.

### Abandono de hipótesis

| Hipótesis | Observación que obliga a abandonarla |
|---|---|
| relaciones aportan sobre M0 | M1 no mejora en casos relacionalmente contrastados |
| (K_5) útil | M2 no supera M1 parcial o empeora calibración/MDL |
| cuaternas reconstructivas | ninguna ablación supera baseline externo |
| orden superior | ninguna terna/hiperarista replica ganancia penalizada |
| cierre simplicial | aparece hiperarista replicada con cara ausente/no útil |
| temporalidad esencial | permutar/eliminar orden no cambia rendimiento ni trazas |
| tipos asimétricos | modelo (S_5) iguala/supera tipos en datos balanceados |
| invariancia narrativa | predicciones siguen vocabulario más que estructura |
| provenance útil | no mejora riesgo-cobertura ni auditabilidad |
| proyectividad | razón doble no se conserva mejor que baselines externos |
| 4-símplex fuerte | no supera hipergrafo dinámico o falla cualquiera de cierre/órdenes |

La respuesta mínima actual no es “hipergrafo” en abstracto, porque incluso una hiperarista sería todavía una afirmación no demostrada. Es un sistema de transición etiquetado capaz de contener desde M0 hasta M6 sin confundir capacidad representacional con verdad.

## Fuentes internas examinadas

- `INFORME_MOC_CONCORDIA_ESTRUCTURA_MATEMATICA_MINIMA_2026-08-15.md`
- `v.1.5.2/psicologia/MOC-PENT-001_Pentacoron_Centroide_Oscilacion.md`
- `v.1.5.2/psicologia/MOC-AX-001_Axiomas_Base.md`
- `v.1.5.2/psicologia/MOC-CANON-001_Acta_Canonizacion_Pentacoron_Phi_Ejes.md`
- `v.1.5.2/psicologia/MOC-MATH-AUD-001_Auditoria_Canon_Matematico.md`
- `v.1.5.2/psicologia/MOC-VPSI-001_Valores_Direccion_Prismatica.md`
- `v.1.5.2/psicologia/MOC-DPSI-001_Definicion_Prismatica.md`
- `v.1.5.2/psicologia/MOC-EPSI-001_Emocion_Prismatica.md`
- `v.1.5.2/psicologia/MOC-CON-001_Conducta_Prismatica.md`
- `v.1.5.2/psicologia/MOC-METR-001_Metricas_No_Clinicas_Validacion.md`
- `v.1.5.2/psicologia/MOC-GEO-METR-001_Metricas_Geometricas_Casos.md`
- `v.1.5.2/psicologia/MOC-REPRO-001_Protocolo_Reproducibilidad_Interevaluador.md`
- `Concordante Lab/03_Expedientes/MOC-EXP-GRAPH-001_Grafo_Experiencia_Local.md`
- `Concordante Lab/03_Expedientes/MOC-001_Semantica_Provisional.md`
- `Concordante Lab/03_Expedientes/MOC-001_Tabla_Operaciones_Formales.md`
- `Concordante Lab/06_Automatizacion/moc_experience_graph_001.py`
- `Concordante Lab/06_Automatizacion/fixtures/moc_experience_graph_cases.json`

## Bibliografía externa esencial

- M. Bronstein et al., [*Geometric Deep Learning*](https://arxiv.org/abs/2104.13478).
- Y. Feng et al., [*Hypergraph Neural Networks*](https://arxiv.org/abs/1809.09401).
- C. Bodnar et al., [*Message Passing Simplicial Networks*](https://arxiv.org/abs/2103.03212).
- P. Grünwald y T. Roos, [*Minimum Description Length Revisited*](https://arxiv.org/abs/1908.08484).
- P. Wollstadt, S. Schmitt y M. Wibral, [PID y selección de variables](https://www.jmlr.org/papers/v24/21-0482.html).
- K. Schweighofer et al., [medidas de incertidumbre predictiva](https://proceedings.mlr.press/v286/schweighofer25a.html).
- R. Schultz, [*Essential Concepts of Projective Geometry*](https://math.ucr.edu/~res/progeom/pg-all.pdf).
- [*Cross ratio*](https://encyclopediaofmath.org/wiki/Cross_ratio), Encyclopedia of Mathematics.

