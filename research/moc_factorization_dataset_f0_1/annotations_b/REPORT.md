# Informe de anotación independiente B — F0.1

## Identidad y alcance

- Rol: `ANNOTATOR_B_F0_1`.
- Casos anotados: 60 de 60, con 60 `case_id` únicos.
- Componentes por caso: `P`, `EAF`, `ACT`, `V`, `S`.
- Estados permitidos: `PRESENT`, `ABSENT`, `AMBIGUOUS`, `UNKNOWN`.
- No se conocieron ni aplicaron cuotas de componentes, celdas contrafactuales o condiciones `DECOY`.

## Inputs declarados

| Input leído | Bytes | SHA-256 |
|---|---:|---|
| `raw/model_input.jsonl` | 20743 | `608d1c27c934da9476ffaf776925daa776edc144842671e86d48f153f17dfec4` |
| `ANNOTATION_MANUAL.md` | 1812 | `2aaf6eaad22b1d455d931a3e5c1bdb05ec7f8dd211d7645a12332f416829196a` |
| `ROLE_MATRIX.md` | 972 | `5229e3f63f018e3a813f8761218e929941e8ae5631e88bf5deb9bb505578a14c` |

No se leyeron `world/`, `outcomes/`, manifests ocultos, preregistros de pares o
celdas, anotaciones A, adjudicación ni modelos. Esta declaración registra el
acceso seguido durante la anotación; los hashes identifican contenidos, pero no
se presentan como prueba suficiente de ceguera.

## Criterio aplicado

- `P` se anotó cuando el texto atribuía a la persona alternativas consideradas,
  interpretación, evaluación, expectativa o regla. Una regla meramente externa
  no se trasladó automáticamente a `P`.
- `EAF` exigió una señal afectiva atribuible al sujeto. Expresiones genéricas
  como *disposición* o *inclinación* quedaron `AMBIGUOUS` cuando no permitían
  separar afecto, dirección y disponibilidad de respuesta.
- `ACT` se reservó para ensayo o disponibilidad interna. Las acciones posibles,
  conductas observadas y recursos de intervención no bastaron.
- `V` requirió dirección, prioridad o criterio. No se trató una valencia escalar
  ni un mero gusto como `V` inequívoco.
- `S` exigió relevancia funcional. Carteles incidentales fueron excluidos cuando
  cada escena ofrecía otra condición, restricción, pauta o recurso pertinente.
- No se anotaron relaciones: el texto permitía identificar coocurrencia o
  simultaneidad, pero no una relación tipada suficientemente segura sin inferirla.

## Distribución observada

| Componente | PRESENT | ABSENT | AMBIGUOUS | UNKNOWN |
|---|---:|---:|---:|---:|
| P | 38 | 0 | 2 | 20 |
| EAF | 3 | 0 | 21 | 36 |
| ACT | 12 | 9 | 3 | 36 |
| V | 3 | 0 | 6 | 51 |
| S | 60 | 0 | 0 | 0 |

Que `S` resulte `PRESENT` en los 60 casos no provino de una cuota: en cada texto
visible se identificó al menos una condición, restricción, pauta o posibilidad de
acceso funcional para la escena. Los detalles meramente llamativos no se usaron
como evidencia cuando no cumplían esa función.

Confianza de los 300 registros de componente: `HIGH=253`, `MEDIUM=43`, `LOW=4`.

## Verificación

- JSONL parseable: sí.
- Cobertura de IDs: exacta, `F01-WF001` a `F01-WF060`, sin faltantes, extras o duplicados.
- Cinco componentes completos por caso: sí.
- Valores de estado, confianza y alcance dentro de vocabulario: sí.
- Todos los `evidence_spans` son substrings literales del `raw_text` correspondiente: sí.
- Razones específicas por componente cuando se comparte un span: sí.
- Relaciones anotadas: 0.
- SHA-256 de `annotations.jsonl`: `96d0ca420f9b1c8e49a780122598938a8bd88e7016bb8ae6f3b3db4187d39e27`.

