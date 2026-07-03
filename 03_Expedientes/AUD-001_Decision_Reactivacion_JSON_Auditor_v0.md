# AUD-001 - Decision de reactivacion JSON del Auditor v0

Estatus: decision operativa de expediente.

Fecha: 2026-07-03.

Expediente padre: `AUD-001`.

Implementacion: `06_Automatizacion/auditor_v0.py`.

## Decision

Se reactiva la salida JSON y la carga externa de casos JSON para `AUDITOR-V0-001`.

La reactivacion cubre:

- `--format json`;
- `--case-file` para archivos JSON dentro del repositorio;
- regeneracion de `06_Automatizacion/reportes/auditor_v0_report.json`;
- fixture externo `06_Automatizacion/fixtures/auditor_v0_cases.json`;
- pruebas unitarias de salida JSON y carga externa.

## Alcance

JSON vuelve a ser formato estructurado vigente del Auditor v0 no mutante.

La reactivacion no convierte JSON en autoridad decisional, no habilita `Tr_ejecucion`, no modifica Canon y no permite transformaciones sobre artefactos auditados.

## Condiciones

- Todo reporte JSON debe conservar `transformacion_permitida = false`.
- Los casos externos deben quedar dentro del repositorio.
- Los errores de forma de caso deben entrar en `schema_errors`.
- Una entrada mal formada puede emitir reporte seguro, pero no puede sostener `conforme_c002 = true`.

## Deuda posterior

- Definir esquema formal de casos externos.
- Ampliar fixtures documentales externos mas alla de la matriz minima.
- Separar contrato ejecutable de `OPERATOR_REPORT` si `AUD-001` lo requiere.
