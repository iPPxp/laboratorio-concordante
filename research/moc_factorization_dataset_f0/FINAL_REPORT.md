# Cierre F0 — construcción y auditoría del corpus

F0 logró su objetivo instrumental: demostró que es posible separar texto crudo,
anotación MOC y outcomes con autorías y digests independientes. También cumplió
su función adversarial: encontró límites suficientes para impedir un entrenamiento
confirmatorio prematuro.

No se debe “arreglar” F0 después de ver sus huecos. Hacerlo convertiría el test en
un dataset optimizado para MOC. Los huecos se preservan como resultados y se
corrigen en una nueva versión F0.1 pre-registrada.

## Respuesta central

**¿Ya existe un corpus capaz de refutar MOC justamente?** No. Existe un buen
prototipo de instrumento, con negativos y ambigüedad, pero no suficiente para
comparar cinco factores: Eaf no tiene positivos, el test efectivo es pequeño y
los outcomes no son externos al diseño sintético.

**¿Puede entrenarse un modelo exploratorio?** Técnicamente sí, científicamente
sólo como prueba de plumbing. Cualquier score debe etiquetarse
`INSTRUMENT_ONLY_NOT_EVIDENCE`. Este frente no entrenó ninguno.

**¿Qué aprendimos?** Que la independencia de archivos y autores es necesaria pero
no suficiente. También importan la fuente del outcome, la variación efectiva,
cobertura por factor, negativos de intervención y acuerdo entre anotadores.

## Estado

DATASET_PHASE = F0_SYNTHETIC_ADVERSARIAL
RAW_LAYER = SUPPORTED
SEALED_TRAJECTORY_LAYER = SUPPORTED
MOC_ANNOTATION_LAYER = PARTIALLY_SUPPORTED
GENERIC_OUTCOME_LAYER = PARTIALLY_SUPPORTED
LAYER_ID_INTEGRITY = SUPPORTED
FAMILY_SPLIT_INTEGRITY = SUPPORTED
ROLE_SEPARATION = SUPPORTED
ADVERSARIAL_CASE_COVERAGE = PARTIALLY_SUPPORTED
EAF_POSITIVE_COVERAGE = NOT_SUPPORTED
INTER_RATER_RELIABILITY = NOT_APPLICABLE
OUTCOME_SOURCE_INDEPENDENCE = NOT_SUPPORTED
INTERVENTION_NEGATIVE_CONTROLS = NOT_SUPPORTED
POSSIBILITY_OUTCOME_COMPLETENESS = PARTIALLY_SUPPORTED
EFFECTIVE_TEST_SIZE = NOT_SUPPORTED
CONFIRMATORY_BENCHMARK_READINESS = NOT_SUPPORTED
MODEL_TRAINING_EXECUTED = NO
MOC_FACTOR_VALIDATION = INSUFFICIENT_EVIDENCE
HUMAN_EXPERIENCE_VALIDATION = NOT_APPLICABLE
CLINICAL_VALIDATION = NOT_APPLICABLE
CANONICAL_STATUS_CHANGE = NOT_AUTHORIZED

