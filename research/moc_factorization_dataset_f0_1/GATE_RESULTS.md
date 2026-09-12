# Resultados de Gate 0.1

## Condiciones aprobadas — 12

```text
EXACT_60_INDEPENDENT_FAMILIES = PASS
SPLITS_35_10_15 = PASS
ALL_10_PAIRWISE_4_CELL_BLOCKS_NEUTRAL = PASS
TEST_INDEPENDENT_FAMILIES_GE_15 = PASS
TWO_BLIND_ANNOTATORS = PASS
ADJUDICATION_COMPLETE = PASS
OUTCOME_SOURCE_INDEPENDENCE = PASS
INTERVENTION_UNAVAILABLE_GE_12 = PASS
INTERVENTION_NEGATIVES_EACH_SPLIT = PASS
TEMPLATE_CONTAMINATION_AUDIT = PASS
LABEL_PERMUTATION_MANIFEST = PASS
NO_HUMAN_OR_CLINICAL_DATA = PASS
```

## Condiciones fallidas — 5

```text
MOC_PAIR_TO_SLOT_MAPPING_PREREGISTERED = FAIL
ALL_5_FACTORS_HAVE_POSITIVE_NEGATIVE_AMBIGUOUS_COVERAGE = FAIL
EAF_EXPLICIT_IMPLICIT_ABSENT_DECOY_OBSERVABLE = FAIL
ANNOTATOR_AGREEMENT_THRESHOLDS = FAIL
UNKNOWN_RATE_WITHIN_LIMIT = FAIL
```

### Mapeo ausente

Los diez bloques cubren todos los pares de `U1..U5`, pero no existe un codebook
preregistrado que establezca qué slot corresponde a qué factor MOC. Inferirlo
después de leer textos/anotaciones sería post-hoc. Por tanto hay cobertura neutral,
no cobertura demostrada de las diez fronteras MOC.

### Acuerdo

| Factor | Acuerdo exacto | Acuerdo PRESENT/binario | UNKNOWN A/B |
|---|---:|---:|---:|
| P | 73.3% | 78.3% | 33.3% / 33.3% |
| EAF | 95.0% | 96.7% | 58.3% / 60.0% |
| ACT | 95.0% | 98.3% | 63.3% / 60.0% |
| V | **58.3%** | 76.7% | 55.0% / **85.0%** |
| S | 96.7% | 96.7% | 0% / 0% |

V incumple acuerdo exacto y límite UNKNOWN. La dificultad se concentra en
“disposición” e “inclinación”, confundibles con afecto u orientación.

## Bloqueantes semánticos adicionales

1. `ABSENT_VS_STABLE_SEMANTIC_CONFUSION`: 11 razones del anotador A usaron
   estabilidad/no cambio para justificar ausencia. La adjudicación las corrigió,
   pero el manual no separó adecuadamente presencia y dinámica.
2. `S_ALWAYS_PRESENT_BY_PROJECTION_DESIGN`: todas las proyecciones incluyen
   contexto funcional; S resulta PRESENT 60/60 y no puede probarse su frontera.

## Dictamen

```text
TRAINING_READINESS = NOT_SUPPORTED
```

El gate es conjuntivo; los 12 pases no compensan cinco fallas.

