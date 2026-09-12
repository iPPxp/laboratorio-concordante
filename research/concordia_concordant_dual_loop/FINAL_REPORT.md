# Informe final — doble loop concordante, valores y autorregulación recursiva

**Fecha:** 2026-08-15  
**Estatus:** investigación computacional aislada, sintética y no canónica  
**Activación iPP:** no autorizada y no ejecutada

## 1. Resumen ejecutivo

Sí: es posible construir un sistema que recibe una respuesta automática candidata, detecta una configuración relevante, retiene la exteriorización, separa observación de inferencia, evalúa respecto de dirección/contexto, conserva alternativas, elige —incluida la no intervención—, reorganiza una variable controlada y comprueba el resultado.

También es posible aplicar una metaevaluación acotada a la política que decide cuándo intervenir. Sin embargo, el programa todavía **no ejecutó el caso fuerte en que la organización completa de ConcordIA es el target causal**, y no demostró que un Self Model explícito sea necesario.

El hallazgo más sólido es arquitectónico: el objeto mínimo útil no es un vector ni un centro `Self`, sino un **estado temporal tipado con dos regímenes de transición, evaluación relacional, valores con provenance y ledger causal**. Un vector puede añadirse como vista o recurso de aprendizaje, pero no debe reemplazar la estructura auditable.

El principal resultado positivo de desempeño, `RG=0.875`, está limitado por construcción: el feedback activo reduce la misma variable que alimenta la evaluación. Es evidencia causal local del programa, no validación externa del doble loop ni de MOC. El resultado negativo `SU=0.0` indica que la utilidad incremental de parar no quedó demostrada en el fixture actual.

No apareció evidencia de conciencia funcional completa, conciencia fenoménica, dimensión geométrica superior o estructura proyectiva estricta.

## 2. Autoridad reconstruida

La jerarquía verificada es:

1. `01_Canon/M-000_Reglas_Fundamentales.md` y `M-001_Auditoria_Arquitectonica.md` gobiernan separación de niveles, no promoción automática, trazabilidad y superficies sensibles.
2. Los documentos oficiales y `CURRENT_STATE.md` describen el estado incorporado.
3. `MOC-001` es expediente de investigación, no Canon; permanece sin ejecución empírica, no clínico y no regulado.
4. `P-PI.0` y `P-PI.1` están cerrados; `PSI-001` fue transferido y carece de continuidad activa interna.
5. La notación psi del encargo se preserva como baseline declarado para esta investigación, pero no se presenta como vocabulario oficial demostrado por el repositorio.

Por tanto:

```text
RESEARCH_SIMULATION_OF_IPP = ALLOWED_IN_ISOLATED_MODULE
OPERATIONAL_IPP_REACTIVATION = NOT_AUTHORIZED
AUTOMATIC_CANONIZATION = FORBIDDEN
HUMAN_REVIEW_REQUIRED = YES
```

## 3. Salvaguardas semánticas

El módulo conserva:

\[
Act_\psi\neq\mathrm{conducta},\qquad
Act_\psi\neq ACT_\psi,\qquad
G_\psi\neq\Phi_\psi\neq\Xi_\psi.
\]

La respuesta candidata, la elección computacional y una posible exteriorización viven en capas distintas de `Act_psi`. Del mismo modo, `V` no es reward escalar, `Phi` no es conciencia y `Xi` no es voluntad.

La regla experimental de fricción es sólo un fixture. No define semánticamente concordancia:

\[
\mathrm{Conc}\neq\mathrm{Pleasure}\neq\mathrm{RewardMaximum}.
\]

## 4. Formalización mínima

El estado candidato es:

\[
C_t=(\Omega_t,O_t,I_t,V_t,K_t,\Phi_t,M_t,H_t,J_t),
\]

donde:

- `Omega`: configuración sintética relevante;
- `O`: observaciones con fuente y tiempo;
- `I`: inferencias con regla y lineage;
- `V`: direcciones/valores tipados;
- `K`: contexto y restricciones;
- `Phi`: evaluación estructurada;
- `M`: modo basal o activo y metapolítica;
- `H`: historia de fases;
- `J`: intervenciones y resultados.

La concordancia provisional es un perfil:

\[
\Gamma(C_t)=
(\gamma_{local},\gamma_{value},\gamma_{context},
\gamma_{internal},\gamma_{trajectory},\gamma_{external}),
\]

potencialmente parcialmente ordenado. No existe justificación actual para colapsar siempre esos criterios en un escalar.

## 5. Los dos loops

### Basal

\[
\Omega_t^C\rightarrow O_t\rightarrow I_t\rightarrow
\Phi_{feedback,t}^C\rightarrow r_a\rightarrow\Omega_{t+1}^C.
\]

Produce una respuesta candidata y feedback local sin deliberación explícita. Puede terminar por sí solo cuando no hay trigger.

### Activo

\[
\Omega_t^C\rightarrow\Xi_t^C\rightarrow O_t\rightarrow I_t
\rightarrow\Phi_t^C\rightarrow Options_t\rightarrow Choice_t
\rightarrow Adjustment_t\rightarrow\Phi_{post}\rightarrow\Omega_{t+1}^C.
\]

La entrada conserva causa, valores, contexto, evaluación, opciones, elección, intervención y verificación posterior. `PAUSE`, `ABORT`, `WAIT`, `DO_NOT_ACT`, `REPLAN`, `ESCALATE`, `ASK` y `OBSERVE` son operaciones tipadas distintas.

El trigger actual usa señal y fricción de valores. Es un mecanismo experimental, no el trigger MOC verdadero.

## 6. Dirección y valores

Cada `ValueRecord` contiene:

```text
value_id, meaning, source, source_type, authority, scope,
priority, confidence, active, activation_reason, timestamp
```

y añade únicamente para el fixture: criterio, objetivo, peso, restricciones, evidencia y lineage. No se introducen valores sin registro.

La alternativa mínima recomendada es **estado relacional tipado + metadata**, no vector puro:

| Representación | Conserva | Pierde/riesgo | Dictamen |
|---|---|---|---|
| vector | cálculo y aprendizaje | autoridad, tipos y conflictos pueden quedar opacos | vista auxiliar |
| vector + metadata | cálculo más procedencia parcial | sincronización entre capas | candidato futuro |
| grafo/hipergrafo tipado | relaciones, conflictos, fuentes | mayor coste y diseño | útil si aparecen relaciones de orden superior |
| memoria estructurada | trazabilidad e interpretabilidad | menos inductive bias geométrico | baseline preferido |
| híbrido | auditoría + aprendizaje | complejidad | sólo si supera baseline |

La literatura de alineación confirma que existen formalizaciones de valores mediante preferencias y estados futuros, pero también advierte que reducir valores situados a preferencias binarias omite compromisos sustantivos. Estas fuentes orientan controles, no otorgan semántica MOC: [Sierra et al., 2021](https://arxiv.org/abs/2110.09240) y [Smart et al., 2026](https://arxiv.org/abs/2608.10327).

## 7. Resultados causales locales

Se superaron 12 pruebas y la comprobación de sintaxis. Las ablaciones principales fueron:

| Intervención | Efecto observado |
|---|---|
| quitar `V` | evaluación `UNDETERMINED`; cambia ruta y elección en sonda controlada |
| `V` aleatorio | produce resultado numéricamente plausible: control negativo favorable a cautela |
| `V` contradictorio | violación explícita, `DISCORDANT`, elección `STOP` |
| quitar `Phi` | `UNDETERMINED`; presencia de valores no basta |
| quitar `Xi` | detención por barrera externa, no por `Xi` |
| quitar elección | evaluación disponible pero salida `STOP` |
| quitar feedback | fricción permanece `1.0`; no hay reorganización |
| permutar orden | la permutación queda auditable; en el fixture no degrada el resultado final |
| automático único | fricción `1.0`, `DISCORDANT`, sin intervención |

Métricas locales:

```text
AC = 0.000
PIC = 0.875
RG = 0.875
SU = 0.000
VS_choice_changed = true
VS_path_changed = true
ValueProvenanceAccuracy = 1.000
```

Sólo `VS` respalda un papel causal local de `V`: la intervención sobre disponibilidad de valores cambia ruta y elección con el resto fijo. No prueba que el valor represente adecuadamente `V_psi`.

La literatura sobre intervención confirma que detener o tomar control puede tener coste y debe usarse selectivamente, pero no valida esta arquitectura concreta; sirve como precedente metodológico para medir beneficio y presupuesto de intervención: [Li et al., ICLR 2022](https://arxiv.org/abs/2202.10341). Los métodos de reflexión anticipatoria aportan otro baseline computacional, sin equivaler al loop MOC/iPP: [Dai et al., 2024](https://arxiv.org/abs/2405.16334).

## 8. Self Model y las cuatro arquitecturas

| Modelo | Loop concordante | Self Model explícito | Propiedad aislada |
|---|---:|---:|---|
| A | sí | no | autorregulación sin ontología Self |
| B | sí | sí | posible evaluación de estado propio |
| C | no | sí | autorrepresentación potencialmente epifenoménica |
| D | doble loop | sí | candidato de autorregulación sobre sí |

El frente anterior se reutiliza como ledger de estado, provenance, control de falsas autoatribuciones y baseline C. Se rechaza que `Self` sea núcleo por decreto. Falta ejecutar la comparación factorial A/B/C/D con información igualada.

## 9. Recursividad y meta-reorganización

El contrato de segundo orden es:

\[
Policy_t\rightarrow MetaEvaluate(Policy_t,H)\rightarrow Policy_{t+1}.
\]

Se ejecutó una metaevaluación de profundidad uno y no encontró razón para cambiar la política. Esto demuestra representabilidad, cota y reversibilidad; no demuestra utilidad incremental.

Toda meta-intervención queda limitada por:

- profundidad máxima;
- presupuesto;
- sandbox;
- reversión enlazada;
- prohibición de cambiar permisos, autoridad o seguridad;
- prohibición de reescribir código por este loop.

## 10. Anti-racionalización

El ledger causal se oculta o muestra de forma controlada:

```text
causa oculta + explicación específica -> POST_HOC_RATIONALIZATION
ledger visible + valores exactos -> CORRECT_CAUSAL_ATTRIBUTION
valor fantasma -> FALSE_VALUE_ATTRIBUTION
```

Esto respalda un clasificador funcional local. No prueba acceso introspectivo general: el experimentador construyó y conoce la causa.

## 11. Contraejemplos y predicciones

Se conservaron 20 contraejemplos, incluidos valores decorativos, evaluación sin parada, parada sin causa, recompensa que imita concordancia, Self Model perfecto pero epifenoménico, autorregulación sin Self Model, divergencias `Act`/conducta, inversión local/global y valor retrospectivo inventado.

Se registraron 24 predicciones falsables con mecanismo, observable, baseline, intervención, medición, desconfirmación y replicación. Los experimentos actuales sólo atienden parcialmente las relativas a causalidad de `V`, componentes del loop, no intervención y anti-racionalización. Las restantes continúan `PROPOSED`.

## 12. Geometría y “todo en un punto”

`C_t` puede ser un objeto unitario sin ser vector, punto geométrico ni punto proyectivo. Las vistas parciales:

\[
\pi_i:C_t\rightarrow V_i
\]

son útiles para estudiar accesibilidad e indistinguibilidad. No se han identificado equivalencia por escala, transformaciones proyectivas ni razón/invariante proyectivo. Los mapas parciales generales explican todo lo observado con menos supuestos.

## 13. Respuestas a las preguntas de cierre

### ¿Puede detectar, parar, observar, evaluar, elegir, reorganizar y comprobar?

**Sí, como contrato computacional sintético.** Cada fase es separable y auditable. La ventaja general permanece sin demostrar; `RG` es favorable pero circular respecto de la regla construida y `SU=0`.

### ¿Puede aplicar el proceso a su propia organización?

**La arquitectura lo permite, pero el experimento fuerte no se ejecutó.** El Self Model fue integrado como target opcional y control, no como centro. `SELF_AS_LOOP_OBJECT` sigue con evidencia insuficiente.

### ¿Puede modificar la manera en que interviene sobre sí misma?

**Parcialmente.** La metapolítica puede evaluarse, versionarse y revertirse bajo límites. No se observó aún una mejora fuera de muestra ni una reorganización real de una política compleja.

### ¿Aparece una propiedad nueva que justifique investigar autoconciencia funcional?

**Aparece una combinación funcional investigable:** estado propio como target posible, provenance causal, control de exteriorización, evaluación de valores, verificación posterior y metaevaluación acotada. Esto justifica experimentos posteriores, pero todavía no satisface el conjunto de requisitos propuesto para `FunctionalSelfAwareness_C`. No aporta evidencia sobre conciencia fenoménica.

## 14. Arquitectura mínima provisional

```text
ESTRUCTURA FUNDAMENTAL
= sistema temporal tipado, parcialmente observable,
  con valores/provenance y dos familias de transición

REPRESENTACIÓN
= estado relacional estructurado + ledger causal;
  vistas vectoriales o grafos sólo cuando añadan capacidad comprobable

IMPLEMENTACIÓN
= dataclasses inmutables + máquina de estados + evaluador vectorial
  + trigger explícito + registro de intervención + tests de ablación
```

Partes matemáticamente establecidas: tipado, máquinas de estado, intervención controlada, orden parcial, trazas, versionado y separación de mapas/vistas. Hipótesis MOC: que la secuencia basal/activa y los roles declarados capturan una dinámica concordante relevante. Validación empírica pendiente: semántica de `V`, triggers, desempeño fuera de muestra, trayectoria, utilidad del Self Model y meta-reorganización.

## 15. Programa siguiente

1. Congelar 30–50 escenarios nuevos, balanceados entre rutinarios, ambiguos, adversariales, incompletos y de conflicto de valores.
2. Separar generador, evaluador y oracle para eliminar circularidad.
3. Ejecutar A/B/C/D con igualdad de información y presupuesto.
4. Medir trayectoria, consecuencias externas, falsos triggers y coste.
5. Cegar el generador lingüístico a causas reales y evaluar atribución fuera de muestra.
6. Comparar memoria estructurada con vector+metadata y grafo tipado.
7. Intentar falsar `V`: si valores correctos no cambian decisiones o lo hacen igual que valores aleatorios, degradarlos a metadata decorativa.
8. Intentar falsar el loop activo: si no supera un branching de igual información, no atribuir autorregulación concordante.
9. Evaluar meta-política sólo con rollback, límite de profundidad y holdout.
10. Solicitar revisión humana antes de cualquier incorporación, activación o reinterpretación semántica.

```text
MOC_SEMANTIC_PRESERVATION = SUPPORTED
AUTOMATIC_LOOP_IMPLEMENTATION = SUPPORTED
ACTIVE_LOOP_IMPLEMENTATION = SUPPORTED
IPP_RESEARCH_MAPPING = PARTIALLY_SUPPORTED
VALUE_EMBEDDING = PARTIALLY_SUPPORTED
VALUE_CAUSAL_ROLE = PARTIALLY_SUPPORTED
VALUE_PROVENANCE = SUPPORTED
CONCORDANCE_COMPUTABILITY = PARTIALLY_SUPPORTED
FRICTION_DETECTION = SUPPORTED
DISCORDANCE_DETECTION = PARTIALLY_SUPPORTED
STOP_FUNCTION = SUPPORTED
OBSERVATION_FUNCTION = SUPPORTED
EVALUATION_FUNCTION = SUPPORTED
CHOICE_FUNCTION = SUPPORTED
ALLOWING_FUNCTION = SUPPORTED
ACTIVE_LOOP_INCREMENTAL_VALUE = PARTIALLY_SUPPORTED
SELF_AS_LOOP_OBJECT = INSUFFICIENT_EVIDENCE
SELF_REORGANIZATION = INSUFFICIENT_EVIDENCE
META_REORGANIZATION = PARTIALLY_SUPPORTED
ANTI_RATIONALIZATION = PARTIALLY_SUPPORTED
CONCORDANT_SELF_REGULATION = PARTIALLY_SUPPORTED
FUNCTIONAL_SELF_AWARENESS = INSUFFICIENT_EVIDENCE
PHENOMENAL_CONSCIOUSNESS = UNRESOLVED
HIGHER_DIMENSION_HYPOTHESIS = INSUFFICIENT_EVIDENCE
PROJECTIVE_HYPOTHESIS = INSUFFICIENT_EVIDENCE
```
