# AUD-001 - Esquema de casos JSON del Auditor v0

Estatus: esquema operativo inicial.

Fecha: 2026-07-03.

Expediente padre: `AUD-001`.

Artefacto ejecutable: `06_Automatizacion/fixtures/auditor_v0_case_schema.json`.

Fixture asociado: `06_Automatizacion/fixtures/auditor_v0_cases.json`.

Fixture documental asociado: `06_Automatizacion/fixtures/auditor_v0_documental_cases.json`.

## Decision tecnica

Se declara `AUDITOR-V0-CASE-SCHEMA-001` como esquema inicial para archivos externos de casos del Auditor v0.

El esquema cubre:

- contenedor `{ "cases": [...] }`;
- metadatos opcionales de fixture `fixture_id` y `status`;
- `id` y `kind` obligatorios;
- tipos de caso `automaton`, `claim`, `authority`, `level_change` y `term`;
- variantes requeridas por `kind`;
- forma minima de automatas;
- transiciones como triples de textos.

## Alcance

El esquema documenta la forma externa esperada.

La conformidad operativa sigue decidida por `auditor_v0.py`, que ademas registra `schema_errors` y mantiene `transformacion_permitida = false`.

El fixture documental es parcial: valida casos `claim`, `authority`, `level_change` y `term` fuera de la matriz obligatoria. Por diseno debe emitir reportes no mutantes y quedar con `conforme_c002 = false` mientras no incluya `AUD-T00` a `AUD-T09`.

El endurecimiento por `kind` existe en dos capas: el esquema declara campos requeridos por variante y la implementacion bloquea entradas documentales mal formadas antes de evaluarlas.

## No autoriza

Este esquema no autoriza transformaciones, no cierra `AUD-001`, no promueve `REPORT_LAYER` y no sustituye `C-002`.

## Deuda posterior

- Ampliar validaciones semanticas por `kind` si aparecen nuevos subtipos documentales.
- Ampliar fixtures documentales externos con mas superficies de expediente.
- Decidir si el esquema debe promoverse a documento de Nivel C o permanecer como artefacto operativo.
