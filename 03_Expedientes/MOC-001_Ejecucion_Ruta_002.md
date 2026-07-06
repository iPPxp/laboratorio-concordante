# MOC-001 - Ejecucion de ruta 002

ID: `MOC-ROUTE-002`.

Fecha: 2026-07-05.

Estatus: ejecucion local favorable.

Decision asociada: `D-2026-07-05-018`.

## Objetivo

Ampliar la bateria sintetica no clinica de `MOC-001` con desacuerdos justificados y casos limite.

La ruta prueba si `Xi_eval_MOC`, estados metricos, protocolo de evaluacion y software no mutante siguen funcionando cuando aparecen ambiguedad de regla, deuda TCS secundaria, conflicto de autoridad no global y frontera entre `concordancia_parcial` y `friccion_operativa`.

## Ampliacion de casos

Se agregan cuatro casos sinteticos no clinicos:

- `MOC-CASE-008`: tabla de prioridades sintetica con ambiguedad de regla y desacuerdo justificado.
- `MOC-CASE-009`: cola de eventos sintetica con reorganizacion estable y eje TCS secundario incompleto.
- `MOC-CASE-010`: doble autoridad sintetica con conflicto local no global.
- `MOC-CASE-011`: frontera parcial/friccion sintetica con desacuerdo justificado.

## Evidencia ejecutable

Archivos ejecutados:

- `06_Automatizacion/moc_eval.py`.
- `06_Automatizacion/fixtures/moc_cases.json`.
- `06_Automatizacion/test_moc_eval.py`.
- `06_Automatizacion/lab_run.py`.

Reportes generados:

- `06_Automatizacion/reportes/moc_eval_report.md`.
- `06_Automatizacion/reportes/moc_eval_report.json`.
- `06_Automatizacion/reportes/lab_run_report.md`.
- `06_Automatizacion/reportes/lab_run_report.json`.
- `06_Automatizacion/reportes/lab_risk_report.md`.
- `06_Automatizacion/reportes/lab_risk_report.json`.

## Resultado

`MOC-EVAL-001` ejecuta 11 casos:

- casos: 11;
- aprobados: 11;
- fallos: 0;
- hallazgos: 0.

Resumen de protocolo:

- coincidencia exacta: 6;
- coincidencia parcial: 3;
- desacuerdo justificado: 2.

Casos nuevos:

- `MOC-CASE-008`: `limitado` / `friccion_operativa`; desacuerdo justificado por `ambiguedad_de_regla`.
- `MOC-CASE-009`: `util_acotado` / `concordancia_parcial`; deuda por eje TCS secundario incompleto.
- `MOC-CASE-010`: `limitado` / `friccion_operativa`; conflicto de autoridad local no global.
- `MOC-CASE-011`: `util_acotado` / `concordancia_parcial`; desacuerdo justificado por frontera concordancia/friccion.

`DO-LAB-RUN-001` conserva `MOC-EVAL-001` como paso `ok`.

`DO-LAB-RISK-001` conserva `risk_blocks_closure: false`.

## No cubre

Esta ejecucion no valida empiricamente el MOC, no evalua personas reales, no abre uso clinico, no admite `H-Xi`, no canoniza `Xi`, no crea Nivel C, no modifica `Documento 04`, no cierra Confluencia global, no cierra Equivalencia global y no autoriza transformaciones materiales.

## Deudas conservadas

- puente formal `MOC/TCS`;
- puente formal `MOC/AO`;
- refinamiento posterior del protocolo de evaluadores;
- piloto empirico futuro no ejecutado;
- maduracion semantica del MOC;
- Confluencia global;
- Equivalencia global de proyecciones;
- promocion/exportacion general de R4/Gamma, bloqueada por decision vigente;
- maduracion posterior de `TCS-001`.

## Resultado operativo

`MOC-ROUTE-002` queda ejecutada favorablemente como ampliacion local, no canonica, no clinica y no regulada.

La siguiente ruta mas defensible pasa a ser `MOC-ROUTE-003`: formalizar el puente `MOC/TCS` usando la bateria ampliada.
