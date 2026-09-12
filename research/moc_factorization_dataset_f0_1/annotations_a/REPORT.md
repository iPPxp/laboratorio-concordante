# Informe de ANNOTATOR_A — F0.1

## Estado

```text
ROLE = ANNOTATOR_A
ANNOTATOR_ID = ANNOTATOR_A
CASES_ANNOTATED = 60
UNIQUE_CASE_IDS = 60
EXPECTED_CASE_IDS_MATCH = TRUE
JSONL_PARSE_OK = TRUE
COMPONENT_SCHEMA_OK = TRUE
EVIDENCE_SPANS_LITERAL_MATCH = TRUE
RELATION_SPANS_LITERAL_MATCH = TRUE
ANNOTATION_COMPLETE = TRUE
```

Este informe documenta una anotación independiente del texto crudo. No evalúa
acuerdo entre anotadores, correspondencia con outcomes, celdas de diseño,
readiness del benchmark ni desempeño de modelos.

## Inputs declarados

Sólo se leyeron estos tres archivos:

| Input | SHA-256 |
|---|---|
| `raw/model_input.jsonl` | `608d1c27c934da9476ffaf776925daa776edc144842671e86d48f153f17dfec4` |
| `ANNOTATION_MANUAL.md` | `2aaf6eaad22b1d455d931a3e5c1bdb05ec7f8dd211d7645a12332f416829196a` |
| `ROLE_MATRIX.md` | `5229e3f63f018e3a813f8761218e929941e8ae5631e88bf5deb9bb505578a14c` |

No se consultaron mundo sellado, outcomes, anotaciones de otro evaluador,
adjudicaciones, modelos, cuotas, pares o celdas contrafactuales ni manifests
ajenos al rol.

## Procedimiento

- Se anotaron los 60 casos en el orden de la entrada cruda.
- Cada caso contiene `P`, `EAF`, `ACT`, `V` y `S`; cada componente incluye
  `status`, `evidence_spans`, `reason`, `confidence` y `scope`.
- `UNKNOWN` se usó cuando el texto no daba señal suficiente; no se transformó
  automáticamente en `ABSENT`.
- `ABSENT` se reservó para negativos explícitos o ausencia funcional indicada
  por el propio texto.
- Una acción ejecutable u observable no se tomó por sí sola como `ACT`.
- Una orientación o disposición no se tomó automáticamente como afecto.
- Un detalle visible no se tomó por sí solo como `S`; se exigió relevancia
  funcional para la configuración descrita.
- No se infirió causalidad por coaparición. Sólo se anotó una relación, en
  `F01-WF042`, porque el texto atribuye expresamente al ritmo colectivo la
  modificación de la disposición.

## Distribución descriptiva

Estas frecuencias son resultado de la lectura; no se usaron como cuotas.

| Componente | PRESENT | ABSENT | AMBIGUOUS | UNKNOWN |
|---|---:|---:|---:|---:|
| P | 25 | 15 | 0 | 20 |
| EAF | 1 | 3 | 21 | 35 |
| ACT | 13 | 8 | 1 | 38 |
| V | 15 | 9 | 3 | 33 |
| S | 58 | 2 | 0 | 0 |

Confianza en los 300 registros de componente:

```text
HIGH = 263
MEDIUM = 37
LOW = 0
```

Scopes:

```text
TARGET_SUBJECT = 171
OTHER_SUBJECT = 1
INCIDENTAL = 2
UNKNOWN = 126
```

## Decisiones difíciles

La formulación `disposición` o `inclinación` se anotó como `V` cuando expresaba
dirección personal. En `EAF` quedó `AMBIGUOUS` cuando podía tener valencia
afectiva pero no nombraba una emoción inequívoca. El único `EAF PRESENT` se
asignó a `F01-WF002`, donde una opción empieza a resultarle “más grata” a la
persona. Esta elección conserva la distinción entre señal afectiva y mera
orientación.

Las alternativas nuevas o perdidas se anotaron en `P` cuando cambiaban lo que
la persona representaba como posible. Los cambios explícitos de lectura o
comprensión también se anotaron en `P`, conforme al manual. Cuando una frase de
utilidad o favorabilidad podía ser a la vez lectura y criterio, se preservó la
ambigüedad en `V` en lugar de duplicar una conclusión segura.

En `F01-WF049` y `F01-WF059`, los detalles de clasificación mecánica se trataron
como incidentales para `S`; el texto niega una configuración o cambio
significativo ligado a una elección personal o grupal.

## Artefacto anotado

```text
annotations.jsonl SHA-256 = bcabdac35518f21a748eebacda7a9bd5f910d5684ba4bfea33f29ed3d14eeee1
```

La anotación queda lista para congelación e integración posterior por un rol
autorizado. Este rol no realizó adjudicación ni comparación con otras capas.
