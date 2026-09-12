# MOC Factorization Dataset F0

Corpus sintético adversarial para validar instrumentos de factorización MOC. No
es evidencia sobre experiencias humanas, no es clínico, no es Canon y no está
autorizado para entrenar modelos confirmatorios.

## Capas y autores

```text
raw/model_input.jsonl              DATASET_DESIGNER_F0
sealed_design/trajectories.jsonl   DATASET_DESIGNER_F0, capa no visible
moc_annotations/annotations.jsonl  F0_MOC_ANNOTATOR_INDEPENDENT
outcomes/outcomes.jsonl            OUTCOME_AUTHOR_F0_INDEPENDENT
audit_dataset.py                   EVALUATOR/INTEGRATOR
```

El anotador sólo leyó `raw/model_input.jsonl`. El autor de outcomes sólo leyó la
trayectoria sellada y los IDs crudos. No se entrenó ningún modelo.

## Resultado

```text
HARD_INTEGRITY = SUPPORTED
INDEPENDENT_ROLE_IDENTIFIERS = SUPPORTED
CONFIRMATORY_BENCHMARK_READINESS = NOT_SUPPORTED
F0_INSTRUMENT_VALUE = PARTIALLY_SUPPORTED
```

El corpus tiene 72 textos, pero sólo 24 familias independientes. La integridad,
los digests y la separación por splits pasan. El benchmark confirmatorio queda
bloqueado por cobertura, outcomes sintéticos no externos, ausencia de controles
sin intervención, un solo anotador instrumental y test efectivo de cuatro
familias.

## Verificación

```text
python -m unittest -v test_dataset.py
python audit_dataset.py
```

