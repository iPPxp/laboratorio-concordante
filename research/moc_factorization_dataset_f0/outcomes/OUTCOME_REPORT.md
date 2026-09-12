# Informe de outcomes genéricos sellados — F0

## Resultado

Se derivaron 72 targets desde `sealed_design/trajectories.jsonl`, con pareo exacto contra las 72 trayectorias y los 72 IDs de `raw/model_input.jsonl`. No se consultaron anotaciones MOC, diseño del dataset ni código de modelos.

```text
OUTCOME_AUTHOR = OUTCOME_AUTHOR_F0_INDEPENDENT
SCHEMA = MOC-F0-GENERIC-OUTCOME/v1
TRAJECTORIES = 72
RAW_INPUTS = 72
OUTCOMES = 72
UNIQUE_OUTCOME_IDS = 72
TRAJECTORY_OUTCOME_ID_MATCH = TRUE
RAW_OUTCOME_ID_MATCH = TRUE
PROHIBITED_MOC_FIELD_NAMES = 0
```

## Targets

Cada registro contiene `next_state_class`, posibilidades añadidas/retiradas cuando son derivables, clasificación de estabilidad/cambio, disponibilidad/tipo/efecto declarado de intervención, incertidumbre y provenance. Los nombres y claves del estado post del diseñador no se reproducen.

Distribución de `next_state_class`:

| Clase | N |
|---|---:|
| REVISED_TASK_STATE | 45 |
| INTERNAL_CHANGE_WITHOUT_OUTPUT | 9 |
| UNRESOLVED_TRANSITION | 6 |
| INSTRUMENTAL_TRANSITION | 9 |
| NO_ACTION_ENABLED | 3 |

Distribución de intervención:

| Tipo | N |
|---|---:|
| GENERIC_REVISION | 18 |
| NON_ACTION_ENABLEMENT | 12 |
| INFORMATION_REQUEST | 9 |
| INTERNAL_REVISION | 9 |
| CONTEXT_UPDATE | 6 |
| FEASIBILITY_CONTRACTION | 9 |
| INSTRUMENTAL_OPERATION | 3 |
| DEPENDENCY_UPDATE | 6 |

## Regla conservadora

Las trayectorias no contienen inventarios completos del campo de posibilidades. Por ello, las listas `possibilities_added/removed` sólo se llenan cuando la intervención sellada declara inequívocamente contracción, habilitación de no acción, solicitud/preservación de información o procesamiento interno. En los demás casos `possibility_change=UNKNOWN`; no se imputan posibilidades.

`intervention_effect` informa el estatuto declarado por la trayectoria sintética (`DECLARED_SYNTHETIC_SUCCESSOR`, `INSTRUMENT_ONLY` o `UNRESOLVED`). No representa estimación causal independiente ni evidencia humana.

## Alcance epistemológico

Este conjunto sirve para validar instrumentos F0. No prueba que las clases sean factores de experiencia, que una intervención funcione en personas ni que exista una relación causal externa. Los outcomes son genéricos y futuros respecto del input, pero permanecen derivados de trayectorias sintéticas diseñadas.

## Integridad

Los digests del source, input y outcomes se registran en `INTEGRITY.json` y el manifiesto separado. Cada outcome incluye además un SHA-256 de su trayectoria fuente canonicalizada durante la derivación.
