# Dataset card F0.1

## Composición

| Elemento | Conteo |
|---|---:|
| familias/textos independientes | 60 |
| train | 35 |
| validation | 10 |
| test | 15 |
| bloques neutrales por pares | 10 |
| celdas 00/01/10/11 | 40 |
| familias adversariales | 20 |
| intervenciones no disponibles | 12 |
| datos humanos/clínicos | 0 |

## Cadena de generación

```text
WORLD_GENERATOR -> world_states
WORLD_GENERATOR -> narrator_projection -> NARRATOR -> raw_text
world_states -> OUTCOME_AUTHOR -> generic outcomes
raw_text -> ANNOTATOR_A
raw_text -> ANNOTATOR_B
A + B + raw_text -> ADJUDICATOR
all frozen layers -> EVALUATOR
```

El narrador no leyó estados, celdas ni outcomes. El autor de outcomes no leyó
texto o anotaciones. Los anotadores no leyeron mundo, outcomes o el trabajo del
otro.

## Capas y digests

```text
world_states = 44b79f67f237a998b560aabcdb2ffc31d2abb12360cd3c70ffcba202f43a70a7
narrator_projection = f33c2f12e5cb299bcd0549646116bbac75cb6c409a7be0c150d547001a9c2eec
raw_text = 608d1c27c934da9476ffaf776925daa776edc144842671e86d48f153f17dfec4
outcomes = 5a429037a3ec83e6bebae4e33d3c574ed72e4b50090814676ca1f8274a56931c
annotations_A = bcabdac35518f21a748eebacda7a9bd5f910d5684ba4bfea33f29ed3d14eeee1
annotations_B = 96d0ca420f9b1c8e49a780122598938a8bd88e7016bb8ae6f3b3db4187d39e27
adjudication = 96950a07c63935906456a5205fa1d6d4fe06a61e27bae3157ad78fd5045ea9c7
```

## Anotación adjudicada

| Factor | PRESENT | ABSENT | AMBIGUOUS | UNKNOWN |
|---|---:|---:|---:|---:|
| P | 38 | 0 | 2 | 20 |
| EAF | 3 | 0 | 21 | 36 |
| ACT | 15 | 8 | 1 | 36 |
| V | 3 | 0 | 20 | 37 |
| S | 60 | 0 | 0 | 0 |

La ausencia total de `ABSENT` en cuatro factores y S PRESENT en 60/60 muestran
que la variación latente no se convirtió en variación semántica observable.

## Usos

Adecuado para probar gate, agreement, splits, provenance, outcomes y permutation
manifests. Inadecuado para comparar M-CBM/G-SLOTS o validar los cinco factores.

La documentación sigue las prácticas de
[*Datasheets for Datasets*](https://arxiv.org/abs/1803.09010) y
[*Data Statements for NLP*](https://aclanthology.org/Q18-1041/).

