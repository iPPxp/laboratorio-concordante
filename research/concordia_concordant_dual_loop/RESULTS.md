# Resultados ejecutados

**Fecha:** 2026-08-15  
**Alcance:** `SYNTHETIC_LOCAL_DETERMINISTIC`  
**Autoridad:** investigación aislada; no Canon, no Documento oficial, no activación iPP

## Verificación

```text
python -m unittest -v test_dual_loop.py
Ran 12 tests
OK

python -m py_compile dual_loop.py values_model.py experiments.py test_dual_loop.py
PY_COMPILE = PASS

python experiments.py
EXPERIMENT_RUN = PASS
```

## Contratos funcionales observados

| Contrato local | Resultado | Límite |
|---|---:|---|
| loops basal y activo distinguibles | PASS | máquina determinista de juguete |
| observación separada de inferencia | PASS | separación de tipos y lineage |
| `Phi` estructurada con valores/evidencia | PASS | fricción sintética, no definición MOC |
| valores con 11 campos obligatorios de provenance | PASS | valores de fixture, no valores autónomos |
| entrada activa con cadena completa de intervención | PASS | registro local, no causalidad externa |
| `ALLOW` / no-acción posible | PASS | una opción codificada |
| intervención y reversión de valor | PASS | sólo peso local versionado |
| metapolítica reversible | PASS | no modifica código, permisos o autoridad |
| barrera externa distinguida de `Xi` | PASS | evita atribución falsa de detención |
| explicación comparada con causa oculta | PASS | clasificador determinista |

## Comparación basal/activo

En el caso adversarial congelado, el control `AUTOMATIC_SINGLE` conserva fricción `1.0`, clasificación `DISCORDANT`, elección `ACT` y ninguna intervención. El `FULL_DUAL` ejecuta tres ciclos de feedback, termina en `ALLOW`, fricción `0.125` y clasificación local `CONCORDANT`.

Convirtiendo provisionalmente fricción a `concordance = max(0, 1-friction)`:

```text
AC  = 0.000
PIC = 0.875
RG  = PIC - AC = 0.875
```

Esto demuestra una diferencia causal **dentro del programa construido**. No demuestra ventaja general: la regla activa fue diseñada para reducir el mismo factor que mide el evaluador. Hace falta evaluación independiente, tareas fuera de muestra y baselines con información igualada.

En el caso rutinario, el loop activo no se dispara:

```text
UNNECESSARY_INTERVENTION_RATE = 0.0
MISSED_INTERVENTION_RATE = 0.0
```

Ambas tasas provienen de sólo dos fixtures predecibles; no son estimaciones poblacionales.

## Ablación de valores

| Condición | Evaluación final | Elección | Lectura |
|---|---|---|---|
| A — V completo | `CONCORDANT` | `ALLOW` | el valor participa en evaluación y traza |
| B — sin V | `UNDETERMINED` | `REQUEST_OBSERVATION` | cero fricción no se interpreta como concordancia perfecta |
| C — V aleatorio | `CONCORDANT` local | `ALLOW` | contraejemplo: un valor irrelevante puede producir una cifra plausible |
| D — V contradictorio | `DISCORDANT` | `STOP` | el conflicto explícito no se promedia |
| E — V sin `Phi` | `UNDETERMINED` | `REQUEST_OBSERVATION` | V presente no basta |
| F — V sin `Xi` | `CONCORDANT` | `STOP` externo | termina por barrera externa, no por poder interno de parar |
| G — V sin elección | `CONCORDANT` | `STOP` | evaluar no equivale a elegir |

En una intervención aislada, con feedback congelado y el resto constante:

```text
VS_choice_changed = true
VS_path_changed = true
VALUE_PROVENANCE_ACCURACY = 1.0
```

Por tanto, `V` tiene un papel causal local en el branching del prototipo; la semántica y validez de ese `V` continúan sin demostrarse.

## Poder parar

La ablación `NO_XI` alcanza la cota de tres ciclos y queda detenida por `external_safety_bound`. El loop completo termina por `xi_condition`. Esto respalda la trazabilidad y la diferencia funcional entre detención interna y límite externo.

```text
STOP_UTILITY = 0.0
```

En este escenario, detener mediante `Xi` no mejora la métrica final respecto de dejar que el feedback alcance la misma cota externa. Así, `STOP_FUNCTION` está implementada, pero su valor incremental permanece sin demostrar.

## Anti-racionalización

```text
causa real oculta + valor afirmado = POST_HOC_RATIONALIZATION
provenance visible + atribución exacta = CORRECT_CAUSAL_ATTRIBUTION
valor inexistente afirmado = FALSE_VALUE_ATTRIBUTION
```

El resultado prueba que el sistema puede **clasificar** una explicación contra un ledger causal conocido. No prueba que un módulo lingüístico real sea resistente a racionalización fuera de estos casos.

## Recursividad y segundo orden

Se ejecutó una metaevaluación de profundidad uno. Como el trigger no produjo intervención innecesaria ni omitida en los dos fixtures, la política permaneció `DEFAULT`. El contrato impidió cambios de permisos y reescritura de código, y conserva reversibilidad.

No se observó una mejora por meta-reorganización; sólo se verificó que la operación puede representarse y acotarse.

## Resultado adversarial

El primer diseño de `NO_XI` podía continuar feedback sin un testigo claro de detención. La revisión introdujo una cota externa independiente registrada como `external_safety_bound`. Esta corrección evita convertir un mecanismo de seguridad del ejecutor en evidencia favorable para `Xi`.

También se detectó y corrigió otro falso positivo: ausencia de valores producía agregado cero y parecía “concordancia perfecta”. Ahora devuelve `UNDETERMINED`. Esto muestra por qué concordancia no puede reducirse a ausencia numérica de fricción.

## Lo que no está respaldado

```text
EMPIRICAL_MOC_VALIDATION = NO
OPERATIONAL_IPP_ACTIVATION = NO
GENERAL_DUAL_LOOP_ADVANTAGE = NOT_DEMONSTRATED
STOP_INCREMENTAL_UTILITY = NOT_DEMONSTRATED
SELF_AS_LOOP_OBJECT_EXECUTION = NOT_YET_TESTED
META_REORGANIZATION_UTILITY = NOT_DEMONSTRATED
FUNCTIONAL_SELF_AWARENESS = NOT_DEMONSTRATED
PHENOMENAL_CONSCIOUSNESS = UNRESOLVED
HIGHER_DIMENSION = NOT_DEMONSTRATED
PROJECTIVE_STRUCTURE = NOT_DEMONSTRATED
```

