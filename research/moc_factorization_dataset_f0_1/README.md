# MOC Factorization Dataset F0.1

Segundo corpus sintético adversarial para validar el instrumento antes de
entrenar representaciones. F0.1 preserva F0 y añade mundo sellado, narrador
independiente, outcomes derivados del mundo, 60 familias, dos anotadores y
adjudicación.

## Resultado

```text
GATE_CHECKS_PASS = 12/17
GATE_CHECKS_FAIL = 5/17
ADDITIONAL_SEMANTIC_BLOCKERS = 2
TRAINING_READINESS = NOT_SUPPORTED
MODEL_TRAINING_EXECUTED = NO
```

F0.1 corrigió independencia de outcomes, tamaño test e intervenciones negativas.
Falló mapeo preregistrado de slots a factores, cobertura observada, observabilidad
Eaf, acuerdo V y límite UNKNOWN. Además reveló confusión `ABSENT`/`STABLE` y S
presente por construcción en todos los textos.

## Ejecución

```text
python -m unittest -v test_gate.py
python audit_gate.py
```

No es evidencia MOC, humana o clínica. No está incorporado ni activo.

