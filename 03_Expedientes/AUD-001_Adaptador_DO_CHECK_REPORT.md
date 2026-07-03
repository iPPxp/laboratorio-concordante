# AUD-001 - Adaptador DO_CHECK_REPORT

Estatus: especificacion operativa inicial.

Fecha: 2026-07-03.

Expediente padre: `AUD-001`.

Implementacion: `06_Automatizacion/auditor_do_check_adapter.py`.

Identificador operativo: `AUDITOR-DO-CHECK-ADAPTER-001`.

## Proposito

Materializar la compatibilidad minima `COMPAT-RL-DO-CHECK-001` como herramienta no mutante.

El adaptador lee un `DO_CHECK_REPORT` JSON y emite un reporte de adaptacion con `REPORT_ITEM`.

## Regla de frontera

El adaptador no absorbe `DO_CHECK_REPORT` en `OPERATOR_REPORT`.

La proyeccion conserva:

- `decision_emitida = no_aplica`;
- `transformacion_permitida = false`;
- `DO_CHECK_REPORT.recomendacion` solo como `decisiones_permitidas`;
- `DO_CHECK_REPORT.cambios_propuestos`, si existieran, solo como evidencia o deuda.

## Superficie implementada

`auditor_do_check_adapter.py` implementa:

- lectura de un reporte JSON dentro del repositorio;
- validacion minima de campos fuente;
- proyeccion de hallazgos a `REPORT_ITEM`;
- reporte Markdown o JSON;
- salida no mutante por consola o por `--output`.

## No autoriza

Esta herramienta no ejecuta cambios, no decide autoridad, no cierra expedientes, no actualiza estado y no modifica Canon.

## Comandos

```powershell
python 06_Automatizacion/auditor_do_check_adapter.py 06_Automatizacion/reportes/do_check_med_repo.json --format md --output 06_Automatizacion/reportes/auditor_do_check_adapter_report.md
python 06_Automatizacion/auditor_do_check_adapter.py 06_Automatizacion/reportes/do_check_med_repo.json --format json --output 06_Automatizacion/reportes/auditor_do_check_adapter_report.json
python -m unittest 06_Automatizacion/test_auditor_do_check_adapter.py
```

## Deuda posterior

- Probar con `do_check_min_repo.json` y reportes con hallazgos.
- Definir esquema formal para `REPORT_ITEM`.
- Decidir si el adaptador permanece operativo o se promueve a contrato propio.
