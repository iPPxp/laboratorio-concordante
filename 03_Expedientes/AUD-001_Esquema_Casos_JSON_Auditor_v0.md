# AUD-001 - Esquema de casos JSON del Auditor v0

Estatus: esquema operativo inicial.

Fecha: 2026-07-03.

Expediente padre: `AUD-001`.

Artefacto ejecutable: `06_Automatizacion/fixtures/auditor_v0_case_schema.json`.

Fixture asociado: `06_Automatizacion/fixtures/auditor_v0_cases.json`.

## Decision tecnica

Se declara `AUDITOR-V0-CASE-SCHEMA-001` como esquema inicial para archivos externos de casos del Auditor v0.

El esquema cubre:

- contenedor `{ "cases": [...] }`;
- `id` y `kind` obligatorios;
- tipos de caso `automaton`, `claim`, `authority`, `level_change` y `term`;
- forma minima de automatas;
- transiciones como triples de textos.

## Alcance

El esquema documenta la forma externa esperada.

La conformidad operativa sigue decidida por `auditor_v0.py`, que ademas registra `schema_errors` y mantiene `transformacion_permitida = false`.

## No autoriza

Este esquema no autoriza transformaciones, no cierra `AUD-001`, no promueve `REPORT_LAYER` y no sustituye `C-002`.

## Deuda posterior

- Endurecer variantes por `kind`.
- Agregar fixtures documentales externos.
- Decidir si el esquema debe promoverse a documento de Nivel C o permanecer como artefacto operativo.
