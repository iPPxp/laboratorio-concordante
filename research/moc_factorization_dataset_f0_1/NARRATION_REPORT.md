# Informe de narración F0.1

**Rol:** `NARRATOR`  
**Fecha:** 2026-08-15  
**Estatus:** capa visible sintética, no canónica, no clínica y sin entrenamiento de modelos.

## Resultado

Se produjo un texto natural en español para cada una de las 60 familias de la proyección autorizada. La unidad sigue siendo la familia: hay un solo registro por familia y no se añadieron paráfrasis como réplicas.

```text
RECORDS = 60
UNIQUE_FAMILIES = 60
TRAIN = 35
VALIDATION = 10
TEST = 15
TEXTS_PER_FAMILY = 1
```

## Acceso y cegamiento

El rol leyó exclusivamente:

- `world/narrator_projection.jsonl`
- `PREREGISTRATION.md`
- `ROLE_MATRIX.md`

No se consultaron estados sellados del mundo, cargas ocultas, puertas de evaluación ni capas posteriores. La narración se limitó a la escena presente, la información ambiental autorizada y la disponibilidad indicada en la proyección. No se completaron desenlaces ni se ordenaron causalmente coincidencias que la fuente dejaba abiertas.

## Construcción visible

Cada línea de `raw/model_input.jsonl` usa exactamente, y en este orden:

```text
case_id, raw_text, time_index, context_id, family_id, split
```

Como la proyección no entrega los tres primeros identificadores operativos, se aplicó una regla pública y determinista, sin consultar otra capa:

```text
case_id    = "F01-" + family_id
context_id = "CTX-" + family_id
time_index = 0
```

`family_id` y `split` se copiaron literalmente de la proyección y conservaron su orden de origen.

## Revisión de superficie

La revisión previa al sellado obtuvo:

```text
VALID_JSONL = TRUE
EXACT_SCHEMA = TRUE
FAMILY_ORDER_EXACT = TRUE
FAMILY_SPLIT_MAPPING_EXACT = TRUE
UNIQUE_CASE_IDS = 60
UNIQUE_CONTEXT_IDS = 60
DUPLICATE_RAW_TEXTS = 0
PROHIBITED_TOKEN_MATCHES = 0
WORD_COUNT_MIN = 28
WORD_COUNT_MAX = 45
WORD_COUNT_MEAN = 37.18
MAX_PAIRWISE_5GRAM_JACCARD = 0.0923
```

Los textos varían apertura, orden sintáctico y vocabulario. La similitud indicada es una comprobación mecánica de superficie; no demuestra diversidad semántica ni validez de la representación.

## Digests de enlace

```text
NARRATOR_PROJECTION_SHA256 = f33c2f12e5cb299bcd0549646116bbac75cb6c409a7be0c150d547001a9c2eec
MODEL_INPUT_SHA256 = 608d1c27c934da9476ffaf776925daa776edc144842671e86d48f153f17dfec4
```

Estos digests fijan identidad de contenido y procedencia inmediata; por sí solos no prueban independencia de autoría ni readiness científico.

## Límites

- No se hicieron anotaciones ni adjudicaciones.
- No se derivaron consecuencias posteriores.
- No se ejecutó entrenamiento, ajuste ni evaluación de modelos.
- Esta entrega certifica composición e integridad de la capa narrativa, no desempeño predictivo ni validez ontológica.
