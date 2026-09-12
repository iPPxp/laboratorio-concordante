# MOC — necesidad representacional y factorización

Programa de investigación aislado, no canónico, inactivo y no clínico. Cambia la
pregunta desde “¿existe una operación MOC irreducible?” hacia:

> ¿Los cinco componentes y sus relaciones constituyen una representación
> mínima, no redundante y predictivamente útil frente a representaciones
> genéricas aprendidas con el mismo presupuesto?

No contiene corpus experiencial ni resultados empíricos. El código sólo verifica
el contrato metodológico: diez fronteras por pares, veinte direcciones
contrafactuales, ausencia de leakage estructural, separación por familias,
igualdad de presupuesto y métricas no reducibles a accuracy.

## Estado

```text
PROGRAM_STATUS = DESIGN_READY_SYNTHETIC_ONLY
MOC_FACTOR_PREDICTIVE_VALUE = UNRESOLVED
MOC_MINIMALITY = UNRESOLVED
MOC_NON_REDUNDANCY = UNRESOLVED
D_AS_PRIMITIVE = UNRESOLVED
D_AS_OPERATION = HYPOTHESIS
EMPIRICAL_DATA = ABSENT
```

## Verificación

```text
python -m unittest -v test_protocol.py
```

Nada se incorpora a Canon o ConcordIA mediante este módulo.

