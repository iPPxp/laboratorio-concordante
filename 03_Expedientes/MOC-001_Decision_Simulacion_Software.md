# MOC-001 - Decision de simulacion y software

ID: `D-2026-07-05-014`.

Fecha: 2026-07-05.

Estatus: decision tecnica provisional.

## Decision

Se acepta `MOC-EVAL-001` como simulador no mutante de `MOC-001`.

Documento base: `03_Expedientes/MOC-001_Casos_No_Clinicos.md`.

Auditoria: `03_Expedientes/MOC-001_Auditoria_Simulacion_Software.md`.

Evidencia ejecutable:

- `06_Automatizacion/moc_eval.py`.
- `06_Automatizacion/fixtures/moc_cases.json`.
- `06_Automatizacion/test_moc_eval.py`.

Reportes:

- `06_Automatizacion/reportes/moc_eval_report.md`.
- `06_Automatizacion/reportes/moc_eval_report.json`.

## Alcance

La decision permite ejecutar casos sinteticos no clinicos, generar reportes y sumar `MOC-EVAL-001` a `DO-LAB-RUN-001` como paso de lectura.

## No cubre

No valida empiricamente el MOC, no evalua personas reales, no autoriza transformaciones, no modifica Canon ni documentos oficiales, no admite `H-Xi`, no canoniza `Xi` y no cierra deudas globales.

## Consecuencia

`MOC-001` cuenta con una superficie ejecutable provisional y no mutante.
