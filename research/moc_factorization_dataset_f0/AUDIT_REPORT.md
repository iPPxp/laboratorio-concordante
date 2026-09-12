# Auditoría adversarial F0

## Integridad

```text
RAW_RECORDS = 72
ANNOTATIONS = 72
OUTCOMES = 72
ID_SET_MATCH = YES
VISIBLE_SCHEMA_EXACT = YES
FAMILY_LEAKAGE = NO
PRIMARY_DIGESTS = VALID
PROHIBITED_MOC_OUTCOME_KEYS = 0
ROLE_IDENTIFIERS_SEPARATE = YES
HARD_INTEGRITY_OK = YES
```

Hashes primarios:

```text
raw=d83c32a6571e4b6d46b9df79bb0359cd61d9192b96593618acd81bb6b34a46a5
sealed=f77bde50cc0d95c9694aee2df76d3abdc63a08436cb9336ccd0fa4097a3ef813
annotations=de72db413753ff7b98699ceb672e380e826482fca04af8c6b51f055e83a95c32
outcomes=50dbe67ba082d509917e1cf6d693b5ade2ea5cb1944ceb8ec1ae9f297c4c81b3
```

## Falsadores que bloquearon readiness

1. **Cobertura Eaf:** cero PRESENT. No puede estimarse una frontera de cinco
   factores cuando uno carece de positivos observados.
2. **Outcome no externo:** autor de codificación independiente, pero la
   trayectoria fuente procede del diseñador sintético del dataset.
3. **Intervención:** 72/72 disponibles; faltan negativos `NOT_AVAILABLE`.
4. **Tamaño efectivo:** test contiene 12 textos, pero sólo cuatro familias.
5. **Anotación:** un solo anotador instrumental; no hay acuerdo interevaluador ni
   adjudicación ciega.
6. **Posibilidades:** 30/72 outcomes son UNKNOWN.
7. **Evidencia duplicada:** 48/72 anotaciones reutilizan una misma frase para más
   de un componente. Puede reflejar solapamiento real o contaminación semántica;
   requiere adjudicación, no corrección automática.

## Dictamen

```text
F0_SCHEMA_INTEGRITY = SUPPORTED
F0_LAYER_SEPARATION = SUPPORTED
F0_ADVERSARIAL_COVERAGE = PARTIALLY_SUPPORTED
F0_ANNOTATION_COVERAGE = NOT_SUPPORTED
F0_OUTCOME_INDEPENDENCE = NOT_SUPPORTED
F0_INTERVENTION_NEGATIVE_CONTROLS = NOT_SUPPORTED
F0_CONFIRMATORY_READINESS = NOT_SUPPORTED
```

El resultado es útil precisamente porque refutó la idea de que un corpus íntegro
por hashes ya está listo para comparar representaciones.

