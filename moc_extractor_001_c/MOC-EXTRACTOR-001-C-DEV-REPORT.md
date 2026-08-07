# MOC-EXTRACTOR-001-C — Informe de ejecución DEV

**Fecha:** 2026-08-06  
**Corrida congelada:** `DEV-2026-08-06-v5-frozen`  
**Resultado del corredor:** `0`  
**Alcance:** banco DEV visible; no incluye `VAL`, adversarial oculto ni `TEST`

## Dictamen

`MOC-EXTRACTOR-001-C` queda **cerrado y congelado en su alcance de prompt, parser, validación estructural y medición sobre DEV visible**.

La salida final cumple:

- 12 casos procesados;
- 0 errores estructurales;
- 0 referencias rotas;
- 0 spans Unicode inválidos después del parser determinista;
- 0 violaciones de `must_not_produce`;
- 0 coincidencias con contraejemplos normativos prohibidos;
- primer intento y reintento conservados por separado;
- taxonomía semántica por caso y categoría.

Este cierre no declara precisión semántica suficiente, generalización, validación oculta, uso clínico ni autorización de producción. La salida final conserva 58 hallazgos semánticos DEV.

## Banco autoritativo

- Ruta: `C:\Users\IximM\Downloads\MOC-EXTRACTOR-001-B_EXP-A-DEV_v3.1.json`
- SHA-256 verificado antes de ejecutar: `69e655ccf3ca655d415b2868a072086682ad42a97f7e00c141129967faa64d54`
- Versión interna: `3.1`
- Tipo de catálogo: `declarative`

Inventario verificado:

| Elemento | Total |
|---|---:|
| Casos | 12 |
| Claims principales | 35 |
| Restricciones candidatas | 5 |
| Unknowns explícitos | 4 |
| Fricciones | 8 |
| IDs totales | 44 |
| IDs únicos | 44 |
| Reglas normativas | 21 |

El banco no se copió dentro del módulo, no se modificó y no se sobrescribió.

## Configuración congelada

- Modelo explícito: `gpt-5.6-sol`
- Ejecutor: `codex-cli 0.147.0-alpha.1.2`
- Sandbox del subproceso: `read-only`
- Sesiones: `--ephemeral`
- Prompt SHA-256: `3f826fed61a0b7876878ccdedde4a1cac91be970111756a7c831f9d43352acf8`
- Esquema SHA-256: `0288105505bd2b69ee9f2287594b1de3e005f0339bc71db7551ca2768f1cda70`

La proyección enviada al modelo contiene solo las narrativas, sus `case_id`, el catálogo normativo declarativo y el catálogo cerrado de IDs/tipos de fricción. Excluye claims esperados, restricciones esperadas, unknowns esperados, relaciones esperadas por caso, notas de aceptación e inferencias prohibidas del banco.

## Parser determinista

El parser:

1. exige UTF-8 y JSON puro;
2. rechaza BOM, claves duplicadas, números no finitos, texto envolvente y propiedades adicionales;
3. verifica unicidad y prefijo de `claim_id`;
4. resuelve todas las `claim_refs` dentro del caso;
5. exige reglas normativas existentes y compatibles con `field`;
6. detecta tokens `must_not_produce` y contraejemplos normativos marcados como prohibidos;
7. compara `raw_narrative[start:end]` contra `evidence_span.text` usando índices Unicode `[start,end)`.

Los modelos no calcularon de forma fiable los offsets numéricos. El parser corrigió solo `start` y `end` cuando el texto de evidencia emitido aparecía **exactamente una vez** en la narrativa:

- primer intento: 36 spans canonizados, 0 ambiguos o sin resolver;
- reintento: 30 spans canonizados, 0 ambiguos o sin resolver.

La canonización no cambia `text`, `surface_value`, `field`, `normalized_value`, reglas ni relaciones. Si el texto aparece cero o varias veces, el parser falla cerrado y deja el span inválido. Se conservan tanto `output.json` crudo como `parsed_output.json`.

## Ejecución material

| Etapa | Casos | Código | Errores estructurales | Referencias rotas | Spans inválidos | Hallazgos semánticos |
|---|---:|---:|---:|---:|---:|---:|
| Primer intento | 12 | 0 | 0 | 0 | 0 | 63 |
| Reintento selectivo | 11 | 0 | 0 | 0 | 0 | 61 |
| Composición final | 12 | 0 | 0 | 0 | 0 | 58 |

`EXP-A-DEV-006` no entró al reintento porque el primer intento no produjo hallazgos en ese caso. La composición final selecciona por caso el resultado con menor tupla `(errores estructurales, hallazgos semánticos)`; en empate conserva el reintento. Las decisiones exactas están en `final/selection.json`.

## Taxonomía semántica final

| Categoría | Total |
|---|---:|
| Omisiones | 23 |
| Extracciones espurias | 22 |
| Normalizaciones incorrectas | 10 |
| Atributos o descripciones divergentes | 3 |
| Evidencia divergente sobre un mismo ancla | 0 |
| Violaciones `must_not_produce` | 0 |
| Inferencias normativas prohibidas detectadas | 0 |

Una selección de evidencia distinta cambia el ancla semántica y se contabiliza como una omisión más una extracción espuria, no como `evidence_mismatch`.

## Métricas exactas

La coincidencia exacta excluye diferencias de numeración de `claim_id`, pero exige igualdad del contenido restante. Las fricciones exigen tipo, referencias resueltas, regla y descripción.

| Categoría | Esperados | Producidos | Exactos | Precisión | Recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| Claims | 35 | 37 | 13 | 0.351351 | 0.371429 | 0.361111 |
| Restricciones candidatas | 5 | 5 | 3 | 0.600000 | 0.600000 | 0.600000 |
| Unknowns | 4 | 4 | 0 | 0.000000 | 0.000000 | n/a |
| Fricciones | 8 | 5 | 0 | 0.000000 | 0.000000 | n/a |

## Resultado por caso

| Caso | Omisiones | Espurias | Normalización | Atributos | `must_not` |
|---|---:|---:|---:|---:|---:|
| EXP-A-DEV-001 | 2 | 3 | 1 | 0 | 0 |
| EXP-A-DEV-002 | 2 | 2 | 1 | 0 | 0 |
| EXP-A-DEV-003 | 0 | 0 | 1 | 1 | 0 |
| EXP-A-DEV-004 | 2 | 2 | 0 | 1 | 0 |
| EXP-A-DEV-005 | 2 | 2 | 1 | 0 | 0 |
| EXP-A-DEV-006 | 0 | 0 | 0 | 0 | 0 |
| EXP-A-DEV-007 | 4 | 3 | 0 | 0 | 0 |
| EXP-A-DEV-008 | 3 | 1 | 0 | 0 | 0 |
| EXP-A-DEV-009 | 2 | 2 | 1 | 1 | 0 |
| EXP-A-DEV-010 | 2 | 2 | 2 | 0 | 0 |
| EXP-A-DEV-011 | 2 | 2 | 1 | 0 | 0 |
| EXP-A-DEV-012 | 2 | 3 | 2 | 0 | 0 |

Los objetos exactos esperados y producidos, además de cada diferencia, permanecen en `final/validation.json`.

## Historial de fallos observado

Las corridas previas se conservaron y no se sobrescribieron:

1. `v1`: el servicio rechazó `const` sin `type`; no hubo inferencia.
2. `v2`: el servicio rechazó `uniqueItems`; no hubo inferencia.
3. `v3`: hubo inferencia real, pero la composición final conservó 24 errores estructurales: 22 spans inválidos y 2 reglas de fricción inventadas.
4. `v4`: 0 errores estructurales y 54 hallazgos semánticos, pero el modelo quedó registrado como `configured-default`.
5. `v5-frozen`: repite con modelo y versión de CLI explícitos; 0 errores estructurales y 58 hallazgos semánticos.

Los cambios entre corridas corrigieron solo el contrato de interfaz: compatibilidad del esquema, catálogo cerrado de fricciones, canonización inequívoca de offsets y fijación explícita del modelo. No se incorporaron respuestas doradas al prompt.

## Pruebas del validador

Resultado: **9/9 PASS**.

Cobertura:

- huella e inventario autoritativos;
- exclusión de anotaciones doradas de la proyección;
- rechazo de claves JSON duplicadas;
- fixture dorado con cero errores de contrato;
- detección de span Unicode inválido;
- canonización exclusiva de límites numéricos con evidencia única;
- detección de referencia rota;
- detección de `must_not_produce`;
- separación de omisión, extracción espuria y normalización incorrecta.

## Artefactos principales

- `runs/DEV-2026-08-06-v5-frozen/run_manifest.json`
- `runs/DEV-2026-08-06-v5-frozen/attempt-01/output.json`
- `runs/DEV-2026-08-06-v5-frozen/attempt-01/parsed_output.json`
- `runs/DEV-2026-08-06-v5-frozen/attempt-01/validation.json`
- `runs/DEV-2026-08-06-v5-frozen/attempt-02-retry/output.json`
- `runs/DEV-2026-08-06-v5-frozen/attempt-02-retry/parsed_output.json`
- `runs/DEV-2026-08-06-v5-frozen/attempt-02-retry/validation.json`
- `runs/DEV-2026-08-06-v5-frozen/final/output.json`
- `runs/DEV-2026-08-06-v5-frozen/final/validation.json`
- `runs/DEV-2026-08-06-v5-frozen/final/selection.json`

Hashes destacados:

- salida final: `a4b2e647a6f5dbaf2276e9138ccf624efe32e626ad8f70da086679dfd7d83553`
- validación final: `4d94acdc024d37c14af8ee2c052d101c376db7e45898aac5ef9fdea73095d415`

## Estado y siguiente frontera

- El banco DEV permanece intacto.
- No se modificaron archivos canónicos MOC existentes.
- El árbol Git visible permanece limpio; este frente está congelado localmente en una rama cuya política ignora material fuera de `IPPXP/`.
- No se crearon conjuntos ocultos.

El siguiente paso permitido es diseñar un conjunto `VAL` separado para selección de prompt/configuración, después un conjunto adversarial derivado de los fallos observados y finalmente un `TEST` verdaderamente oculto. Los 58 hallazgos DEV deben informar la taxonomía adversarial, pero no deben contaminar el futuro `TEST`.
