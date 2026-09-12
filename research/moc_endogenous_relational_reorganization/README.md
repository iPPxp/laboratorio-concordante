# MOC / ConcordIA — reorganización relacional endógena

Módulo de investigación adversarial, sintético, no clínico, no canónico e
inactivo. Pregunta si una operación candidata `MOC_R` aporta valor incremental
frente a selección relacional (B4), replanning generativo (B5) y edición
estructural genérica (B6).

## Resultado en una frase

En los 12 fixtures congelados, `MOC_R` representa y ejecuta reorganizaciones,
pero B6 reproduce estados, campos, decisiones, provenance y coste mediante un
mapeo simple en 12/12 casos: no aparece unicidad algorítmica MOC.

## Independencia experimental

- Fixture: agente independiente, 12 casos (6 desarrollo, 6 holdout), SHA-256
  `da0575c27dc37d7eb7a2cc1811920b502ca0937641e78a89c2a758a3de590ea5`.
- Oracle: agente independiente y ciego a políticas, rubric SHA-256
  `c3d6754108884bd087057783ee8561e1de90d1174b3b80f70499295e7369def0`.
- B4/B5/B6: autor genérico que no leyó fixture, oracle ni MOC_R.
- MOC_R, evaluator e isomorfismo: integración posterior sobre interfaces
  congeladas.

El script de edición se deriva del par before/target y se entrega con igualdad de
información a los ejecutores estructurales. El benchmark prueba ejecución,
trazabilidad e isomorfismo; **no** prueba inferencia autónoma de la intervención
correcta desde lenguaje o experiencia.

## Ejecución

Desde esta carpeta:

```text
python -m unittest -v test_generic_contracts.py test_reorganization.py
python benchmark.py
```

## Límites de autoridad

```text
MOC_SEMANTIC_AUTHORITY = YES
CONCORDIA_SEMANTIC_AUTHORITY = NO
AUTOMATIC_CANONIZATION = FORBIDDEN
HUMAN_REVIEW_REQUIRED = YES
```

No se modificaron canon, contratos, código operativo, ramas o módulos previos.

## Contexto matemático externo

El modelo usa ideas estándar de reescritura tipada de grafos y equivalencia de
trazas sólo como contexto formal, no como evidencia sobre MOC: König et al.,
[*A tutorial on graph transformation*](https://research.utwente.nl/en/publications/a-tutorial-on-graph-transformation/);
Teru et al., [*Inductive Relation Prediction by Subgraph Reasoning*](https://proceedings.mlr.press/v119/teru20a.html);
y el trabajo de abstracción relacional para planificación
[*PARL*](https://arxiv.org/abs/2405.03864).

