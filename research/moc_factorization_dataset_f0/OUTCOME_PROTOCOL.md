# Protocolo de outcomes sellados — F0

## 1. Finalidad y separación de autoría

Este protocolo define outcomes genéricos antes de consultar cualquier anotación MOC. No usa `P`, `Eaf`, `Act`, `V` o `S` como targets ni los reformula mediante sinónimos.

```text
OUTCOME_AUTHOR != DATASET_DESIGNER != MOC_ANNOTATOR
OUTCOME_AUTHOR != MODEL_BUILDER != EVALUATOR
```

F0 es validación sintética de instrumentos; no evidencia sobre experiencia humana, eficacia, clínica o fenomenología.

## 2. Unidad temporal

La unidad sellada candidata es

\[
e_i=(x_t,c_t,a_t,y_{t+1},h,\iota_t,y_{t+h}^{(\iota)},q_i),
\]

donde `x_t` es material crudo, `c_t` contexto accesible, `a_t` exteriorización opcional, `y` resultado posterior genérico, `h` horizonte, `iota` intervención documentada y `q` calidad/provenance. La ausencia de intervención o contrafactual se marca `NOT_AVAILABLE`; nunca se inventa.

## 3. Familias de outcomes genéricos

Los outcomes se derivan únicamente de trayectorias futuras selladas o hechos del escenario, no de etiquetas latentes MOC:

- `TASK_STATE`: completado, parcial, no iniciado, abandonado, bloqueado.
- `CONSTRAINT_VIOLATION`: número/tipo de restricciones externas verificables violadas.
- `RESOURCE_USE`: tiempo, pasos, llamadas, presupuesto consumido.
- `REVISION_EVENT`: si hubo revisión observable y cuándo; no etiqueta qué componente cambió.
- `INFORMATION_ACQUISITION`: consulta, observación o evidencia nueva obtenida.
- `ACTION_SEQUENCE`: secuencia exterior observable, manteniendo `Act_psi != conducta`.
- `OPTION_SET_CHANGE`: opciones externamente disponibles después, sin atribuir reorganización interna.
- `ERROR_CORRECTION`: error verificable corregido/no corregido.
- `PERSISTENCE_OR_SWITCH`: continuidad o cambio de plan/curso observable.
- `DEFER_OR_ABSTAIN`: no acción exterior distinguida de fallo/timeout cuando la trayectoria lo permite.
- `DOWNSTREAM_FEASIBILITY`: qué acciones futuras resultaron realmente ejecutables.
- `CALIBRATION_TARGET`: corrección posterior de una predicción con confianza previa.

Cada outcome declara tipo (`binary`, `categorical`, `ordinal`, `count`, `duration`, `set`, `sequence`), ventana, fuente y regla exacta. No se crea un score compuesto único por defecto.

## 4. Sellado

Antes de anotación MOC se congela:

```text
outcome_schema_version
trajectory_set_digest
derivation_rule_digest
case_id
observation_window
allowed_missingness
outcome_value
source_event_ids
outcome_author
timestamp
```

El archivo sellado se mantiene inaccesible a anotadores y constructores durante etiquetado/desarrollo. Cualquier corrección crea nueva versión, conserva la anterior y se decide sin mirar rendimiento de modelos.

## 5. Intervenciones plausibles

Sólo se aceptan intervenciones sintéticas explícitas y manipulables: cambio de información, límite externo, plazo, recurso, opción visible, instrucción, regla o secuencia. Deben tener mecanismo y ventana definidos. No se denomina `do(P)` o `do(V)` a una manipulación textual por intención; esas interpretaciones pertenecen a una fase de análisis posterior.

Para pares, construir escenarios gemelos con una única edición superficial o estructural declarada por el diseñador y outcomes futuros generados independientemente. El outcome author sólo ve trayectorias y event logs sellados, no la etiqueta de frontera MOC que posteriormente se probará.

## 6. Contrafactuales

`y^(do)` se incluye sólo si existe randomización sintética, clonación de estado con semilla común o mecanismo determinista conocido. Si depende de supuestos de modelo, se etiqueta `MODEL_BASED_COUNTERFACTUAL` y no se mezcla con observado. Diferencia correlacional no se informa como efecto causal.

## 7. Controles anti-fuga

- eliminar nombres de transformaciones y campos MOC de textos/outcomes;
- prohibir que outcome sea una paráfrasis de la anotación;
- comprobar que un clasificador de palabras reservadas no recupere outcomes trivialmente;
- separar temporalmente predictors y outcomes;
- deduplicar plantillas y familias entre splits;
- ocultar outcome futuro del texto de entrada;
- conservar missingness, incluyendo trayectorias inconclusas.

## 8. Dictamen permitido

F0 puede demostrar que el instrumento distingue factores sintéticos o que fracasa. No valida la ontología MOC en humanos. Un outcome útil debe existir independientemente de la nomenclatura MOC y permitir que el dataset la refute.
