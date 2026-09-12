# LAB-INC-SCI-000 — Registro de incorporación de familias científicas

Estatus: registro administrativo abierto; no decisorio y no semántico.

Fecha: 2026-09-12.

Base de apertura: `origin/main@f18aca0ae25dbe296d7938f74b680f5123b5389d`.

## Propósito

Abrir una ruta independiente de revisión e incorporación para cada familia
científica preservada en la rama local
`ipp/lab-primary-working-preserved-20260815`, sin incorporar todavía sus
payloads, canonizar claims, activar software ni convertir pruebas sintéticas en
validación empírica.

## Expedientes abiertos

| ID | Familia | Objetos manifestados | Estado de incorporación |
| --- | --- | ---: | --- |
| `LAB-INC-SCI-001` | factorización e identificabilidad MOC | 109 | pendiente |
| `LAB-INC-SCI-002` | geometría y observabilidad MOC/RC1 | 30 | pendiente; conflicto de variante registrado |
| `LAB-INC-SCI-003` | arquitecturas reflexivas ConcordIA | 84 | pendiente |
| `LAB-INC-SCI-004` | necesidad representacional y factorización | 19 | pendiente |
| `LAB-INC-SCI-005` | validación estructural mínima MOC/ConcordIA | 6 | pendiente |

Total manifestado: 248 objetos. Los cinco archivos de manifiesto son metadatos
de custodia adicionales y no se cuentan dentro de esos 248 objetos.

## Estado transversal

```text
FAMILY_SOURCE_PRESERVED_IN_LOCAL_COMMITS=YES
COMMITTED_BLOBS_VERIFIED_AGAINST_MANIFESTS=248/248
PAYLOAD_IN_ORIGIN_MAIN=NO
INCORPORATION_DECISIONS=PENDING
SCIENTIFIC_CLAIMS_CANONIZED=NO
EMPIRICAL_VALIDATION_GRANTED=NO
ACTIVATION=NO
MODEL_TRAINING_AUTHORIZED=NO
```

Las 97 pruebas disponibles pasan, pero están distribuidas de forma desigual y
demuestran solamente contratos computacionales locales. La familia 005 no tiene
suite ejecutable; se verificaron su JSON, CSV y hashes.

## Regla de incorporación

Cada familia requiere revisión individual de procedencia, licencia, alcance,
resultados negativos, rutas destino y compatibilidad con Canon. La futura
decisión puede aceptar, rechazar, dividir o solicitar reparación. No se permite
incorporar el historial completo de la rama por arrastre: sólo las rutas
enumeradas por el manifiesto aprobado.

La cápsula local `WORKSPACE-CLEANUP-2026-09-12-001` conserva el corte previo y
un bundle Git completo, pero permanece en el mismo disco y no sustituye un
respaldo independiente.
