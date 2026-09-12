# Matriz de roles y acceso

| Rol | Puede leer | No puede leer | Produce |
|---|---|---|---|
| WORLD_GENERATOR | preregistro | narrativas, anotaciones | mundo sellado + proyección |
| NARRATOR | proyección narrativa | slots, celdas, outcomes | texto crudo |
| OUTCOME_AUTHOR | mundo sellado | texto, anotaciones | outcomes genéricos |
| ANNOTATOR_A | texto crudo | mundo, outcomes, B | annotations A |
| ANNOTATOR_B | texto crudo | mundo, outcomes, A | annotations B |
| ADJUDICATOR | A+B+texto | mundo, outcomes | adjudicación |
| MODEL_BUILDER | nada en F0.1 | capas selladas | no aplica |
| EVALUATOR | todas tras freeze | edición de datos | audit/readiness |

```text
WORLD_GENERATOR != NARRATOR != OUTCOME_AUTHOR
ANNOTATOR_A != ANNOTATOR_B != ADJUDICATOR
DATASET_ROLES != MODEL_BUILDER != EVALUATOR
```

Las separaciones son de autoría y de acceso. Un digest posterior no demuestra
ceguera; cada rol declara inputs y el integrador conserva esas declaraciones.

