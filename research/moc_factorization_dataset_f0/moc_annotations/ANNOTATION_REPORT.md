# Reporte de anotación independiente F0

## Alcance y cegamiento

Se anotaron exclusivamente los 72 registros de `raw/model_input.jsonl`, usando `raw_text` y `context_id`. No se consultaron `sealed_design/`, `outcomes/`, `DATASET_DESIGN.md`, código de modelos, predicciones ni hipótesis específicas del benchmark.

## Método

Cada caso recibió estados `PRESENT`, `ABSENT`, `AMBIGUOUS` o `UNKNOWN` para `P`, `EAF`, `ACT`, `V` y `S`, con evidencia textual acotada y confianza. La conducta se registró en campo separado y nunca se usó como sustituto de `ACT`. Las relaciones sólo se incluyeron cuando el mismo enunciado sostenía una asociación prudente; no se añadió causalidad, completitud ni simetría.

Guardas aplicadas:

```text
Act_psi != conducta
Act_psi != ACT_psi
V_psi != reward
S_RELECTURA != S_REAL
F0_ANNOTATION != HUMAN_VALIDATION
```

## Ambigüedad y desacuerdo

Los casos con varias lecturas compatibles conservan `AMBIGUOUS`; los casos sin información suficiente conservan `UNKNOWN`. `ABSENT` se utilizó sólo ante negación explícita o escenarios no experienciales cuyo texto completo excluye el componente dentro del alcance del caso.

La corrida tuvo un solo anotador instrumental independiente. Por ello no se reclama acuerdo interevaluador. El campo `disagreement` registra `INTERNAL_AMBIGUITY_RECORDED` cuando el propio texto sostiene lecturas múltiples y declara expresamente esta limitación.

## Provenance

Cada anotación contiene:

- `case_id` y `annotation_id`;
- identificador del anotador;
- archivo y campos fuente;
- SHA-256 del registro fuente individual;
- alcance epistemológico F0;
- guardas semánticas aplicadas.

## Verificación

```text
RAW_RECORDS = 72
ANNOTATION_RECORDS = 72
UNIQUE_CASE_IDS = 72
CASE_ID_SET_MATCH = YES
COMPONENT_STATUS_VOCABULARY_VALID = YES
RAW_SHA256 = d83c32a6571e4b6d46b9df79bb0359cd61d9192b96593618acd81bb6b34a46a5
ANNOTATIONS_SHA256 = de72db413753ff7b98699ceb672e380e826482fca04af8c6b51f055e83a95c32
```

## Límites

Las anotaciones no prueban que los componentes describan experiencias humanas, no validan MOC empíricamente, no autorizan uso clínico y no deben reinterpretarse a partir de outcomes futuros. Cualquier adjudicación posterior debe conservar esta primera pasada y registrar `supersedes` sin borrarla.
