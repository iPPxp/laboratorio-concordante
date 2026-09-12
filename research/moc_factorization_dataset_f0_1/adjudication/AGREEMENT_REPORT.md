# Informe de acuerdo y adjudicación F0.1

## Resultado

La adjudicación se completó sobre 60 casos y 300 registros de componente. Los dos anotadores coincidieron exactamente en **251/300 estados (83.67%)** y en **268/300 decisiones binarias PRESENT frente a non-PRESENT (89.33%)**.

Los 49 desacuerdos de estado fueron revisados contra el texto visible y `ANNOTATION_MANUAL.md`. Todos pudieron resolverse con base textual o con la regla explícita del manual; **no se usaron cuotas** y **no quedaron componentes UNRESOLVED**. Esto describe consistencia de anotación, no validez del benchmark ni alineación con outcomes.

```text
ADJUDICATION_EXECUTED = YES
CASES = 60
UNIQUE_CASE_IDS = 60
COMPONENT_RECORDS = 300
RAW_STATUS_AGREEMENT = 251/300 = 0.8367
BINARY_PRESENT_AGREEMENT = 268/300 = 0.8933
STATUS_DISAGREEMENTS_RESOLVED = 49
UNRESOLVED_COMPONENTS = 0
QUOTAS_USED = NO
OUTCOMES_READ = NO
WORLD_READ = NO
PAIR_OR_CELL_REGISTRY_READ = NO
MODELS_READ = NO
```

## Acuerdo por factor

| Factor | Acuerdo bruto | Tasa | Acuerdo PRESENT vs non-PRESENT | Tasa | UNKNOWN A | UNKNOWN B |
|---|---:|---:|---:|---:|---:|---:|
| P | 44/60 | 73.33% | 47/60 | 78.33% | 20/60 (33.33%) | 20/60 (33.33%) |
| EAF | 57/60 | 95.00% | 58/60 | 96.67% | 35/60 (58.33%) | 36/60 (60.00%) |
| ACT | 57/60 | 95.00% | 59/60 | 98.33% | 38/60 (63.33%) | 36/60 (60.00%) |
| V | 35/60 | 58.33% | 46/60 | 76.67% | 33/60 (55.00%) | 51/60 (85.00%) |
| S | 58/60 | 96.67% | 58/60 | 96.67% | 0/60 (0.00%) | 0/60 (0.00%) |
| Total | 251/300 | 83.67% | 268/300 | 89.33% | 126/300 (42.00%) | 143/300 (47.67%) |

Las matrices A×B completas, con filas de A y columnas de B, están congeladas en `CONFUSION_MATRICES.json`.

## Lectura del desacuerdo

El principal foco es V: 25/60 casos tuvieron estados distintos. La divergencia se concentra en expresiones como “disposición” e “inclinación”, que pueden señalar dirección V o afecto sin formular una prioridad o criterio suficientemente separable. En esos casos se conservó `AMBIGUOUS` cuando había una señal textual real pero el constructo no podía distinguirse con seguridad; se usó `UNKNOWN` cuando faltaba una señal V suficiente.

En P, 13 desacuerdos `ABSENT/PRESENT` provenían de confundir estabilidad con ausencia. Frases como “conserva su interpretación” o “las opciones permanecen iguales” siguen expresando contenido P; que no cambie no lo vuelve ausente.

En EAF, un tono atribuible al sujeto se mantuvo como señal afectiva aunque fuera estable. Vocabulario como duda o desafío atribuido únicamente al gesto de otra persona no se convirtió en EAF del sujeto objetivo.

En ACT, “abandona el ensayo mental” conserva evidencia de un cambio del modo interno y se adjudicó `PRESENT`. La “disposición a participar/encabezar” se adjudicó `PRESENT` como disponibilidad interna para una respuesta concreta, sin convertir la conducta posible o ejecutada en ACT.

En S, la posibilidad de corregir un conteo o una etiqueta se consideró una condición funcional de la tarea; la ausencia de tensión personal no vuelve incidental esa condición.

## Resultado adjudicado

| Factor | PRESENT | ABSENT | AMBIGUOUS | UNKNOWN | UNRESOLVED |
|---|---:|---:|---:|---:|---:|
| P | 38 | 0 | 2 | 20 | 0 |
| EAF | 3 | 0 | 21 | 36 | 0 |
| ACT | 15 | 8 | 1 | 36 | 0 |
| V | 3 | 0 | 20 | 37 | 0 |
| S | 60 | 0 | 0 | 0 | 0 |

De los 49 desacuerdos, 32 se resolvieron conservando el registro de B, uno conservando el registro de A y 16 mediante síntesis explícita desde texto y manual. La procedencia de cada decisión está registrada por caso y componente en `adjudicated.jsonl`.

## Relaciones y spans compartidos

A anotó una relación y B ninguna. En `F01-WF042` se conservó `S → V / INFLUENCES / PRESENT` porque el texto expresa directamente que el ritmo colectivo “va modificando” la disposición; no se infirió causalidad de mera coaparición.

El resultado conserva 25 pares de componentes con algún span compartido, distribuidos en 21 casos. Esto es admisible porque sus razones son específicas para cada constructo. La búsqueda exacta normalizada no encontró razones clonadas sobre spans compartidos:

```text
SHARED_SPAN_COMPONENT_PAIRS = 25
CASES_WITH_SHARED_SPANS = 21
CLONED_REASON_FLAGS = 0
```

## Entradas declaradas y verificadas

Sólo se leyeron estas entradas autorizadas:

| Entrada | SHA-256 verificado |
|---|---|
| `raw/model_input.jsonl` | `608d1c27c934da9476ffaf776925daa776edc144842671e86d48f153f17dfec4` |
| `ANNOTATION_MANUAL.md` | `2aaf6eaad22b1d455d931a3e5c1bdb05ec7f8dd211d7645a12332f416829196a` |
| `annotations_a/annotations.jsonl` | `bcabdac35518f21a748eebacda7a9bd5f910d5684ba4bfea33f29ed3d14eeee1` |
| `annotations_a/INTEGRITY.json` | `5071e5477647784a26891dbff8b79d43cca6af58436a5d3da0f2563afb556cc3` |
| `annotations_a/MANIFEST.sha256` | `0bcce982b582ccb9dc12344568e7dc70d95ebe1bf5cce34ff788d6bef03047eb` |
| `annotations_b/annotations.jsonl` | `96d0ca420f9b1c8e49a780122598938a8bd88e7016bb8ae6f3b3db4187d39e27` |
| `annotations_b/INTEGRITY.json` | `fafd9b16ddc92f94587c132fdff166e77b9e139714f74e522e5d3ac4a4843f47` |
| `annotations_b/MANIFEST.sha256` | `1a787aba83abfddf73f1ad1ec60f9f89bb1dd6905f0f72747fae72a3f7f26ca3` |

Los digests de corpus, manual y anotaciones coinciden con las declaraciones de integridad de ambos anotadores. Los conjuntos de IDs raw/A/B/adjudicación son idénticos: 60 IDs únicos, sin faltantes, extras ni duplicados.

`ROLE_MATRIX.md` aparece como entrada declarada en las integridades de los anotadores, pero **no fue leído por el adjudicador**. Tampoco se leyeron `world/`, `outcomes/`, registros preregistrados de pares o celdas, GATE, código de modelos ni resultados de entrenamiento.

## Alcance epistémico

Este cierre sustenta únicamente la integridad de la adjudicación textual y cuantifica el acuerdo entre dos capas. No prueba independencia por hashes por sí solos, no evalúa outcomes, no autoriza entrenamiento y no declara readiness confirmatoria.

```text
TEXT_ADJUDICATION_INTEGRITY = SUPPORTED
INTER_ANNOTATOR_AGREEMENT = MEASURED
OUTCOME_ALIGNMENT = NOT_EVALUATED
CONFIRMATORY_BENCHMARK_READINESS = NOT_EVALUATED
MODEL_TRAINING = NOT_EXECUTED
```
