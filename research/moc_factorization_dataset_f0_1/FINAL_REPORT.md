# Cierre F0.1

F0.1 mejoró sustancialmente F0: aumentó a 60 familias independientes, creó un
mundo previo a la narración, separó outcome y texto, añadió 12 negativos de
intervención, dos anotadores y adjudicación. Esas mejoras son verificables.

El corpus aún no está listo para entrenamiento. La capa latente logró balancear
cinco slots neutrales y cuatro modos de señal, pero esa variación no se tradujo
en observabilidad MOC suficiente. No existe mapping preregistrado slot→factor,
Eaf y V siguen escasos, S está siempre presente y V no alcanza acuerdo.

La conclusión no es “MOC falló”. Falló otra versión del instrumento antes de
arriesgar un benchmark engañoso.

## Estado final

F0_1_WORLD_LAYER = SUPPORTED
F0_1_NARRATIVE_LAYER = SUPPORTED
F0_1_GENERIC_OUTCOMES = SUPPORTED
F0_1_OUTCOME_SOURCE_INDEPENDENCE = SUPPORTED
F0_1_INTERVENTION_NEGATIVE_CONTROLS = SUPPORTED
F0_1_TWO_BLIND_ANNOTATORS = SUPPORTED
F0_1_ADJUDICATION = SUPPORTED
F0_1_NEUTRAL_PAIRWISE_4_CELL_DESIGN = SUPPORTED
F0_1_MOC_PAIRWISE_MAPPING = NOT_SUPPORTED
F0_1_FACTOR_COVERAGE = NOT_SUPPORTED
F0_1_EAF_OBSERVABILITY = NOT_SUPPORTED
F0_1_V_AGREEMENT = NOT_SUPPORTED
F0_1_UNKNOWN_RATE = NOT_SUPPORTED
F0_1_S_VARIATION = NOT_SUPPORTED
F0_1_PRESENCE_CHANGE_SEPARATION = NOT_SUPPORTED
F0_1_TEMPLATE_AUDIT = SUPPORTED
F0_1_LABEL_PERMUTATION_MANIFEST = SUPPORTED
F0_1_LABEL_PERMUTATION_PERFORMANCE_CHECK = NOT_APPLICABLE
F0_1_GATE = FAILED
TRAINING_READINESS = NOT_SUPPORTED
MODEL_TRAINING_EXECUTED = NO
MOC_FACTORIZATION_VALIDATION = INSUFFICIENT_EVIDENCE
HUMAN_EXPERIENCE_VALIDATION = NOT_APPLICABLE
CLINICAL_VALIDATION = NOT_APPLICABLE
CANONICAL_STATUS_CHANGE = NOT_AUTHORIZED

