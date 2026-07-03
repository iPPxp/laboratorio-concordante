# Automatizacion

Estatus: superficie ejecutable provisional.

Esta carpeta contiene herramientas no mutantes del Laboratorio Concordante.

## Herramienta inicial

- `do_check_min.py`: verificador minimo de lectura.
- `do_check_med.py`: verificador medio de riesgos, permisos, estado y puente funcional con AAU historico.
- `lab_status_board.py`: tablero no mutante de estado y continuidad del Laboratorio.
- `lab_continuity_report.py`: reporte combinado no mutante de continuidad y riesgos.
- `lab_risk_classifier.py`: clasificador no mutante de advertencias heredadas, deuda documental y riesgos activos.
- `lab_executive_summary.py`: resumen ejecutivo automatico no mutante del Laboratorio.
- `lab_run.py`: comando unico no mutante para corrida local de laboratorio.
- `auditor_v0.py`: implementacion inicial no mutante del Auditor v0 conforme `C-002`.
- `auditor_do_check_adapter.py`: adaptador no mutante de `DO_CHECK_REPORT` a `REPORT_ITEM`.

## Regla de uso

La herramienta puede leer archivos locales y emitir reportes.

No puede:

- modificar archivos objetivo;
- cerrar expedientes;
- promover hipotesis;
- modificar Canon o documentos oficiales;
- usar Registro Historico como autoridad directa;
- autorizar transformaciones.

## Uso esperado

Desde la raiz del repositorio:

```powershell
python 06_Automatizacion/do_check_min.py CURRENT_STATE.md
```

Para revisar todo el repositorio:

```powershell
python 06_Automatizacion/do_check_min.py --all --format md --output 06_Automatizacion/reportes/do_check_min_repo.md
```

Para ejecutar la fase media sobre archivos clave:

```powershell
python 06_Automatizacion/do_check_med.py CURRENT_STATE.md 03_Expedientes/AUT-001.md 02_Documentos/C-001_Especificacion_Tecnica_Auditor.md --format md --output 06_Automatizacion/reportes/do_check_med_claves.md
```

Para revisar el repositorio con la fase media:

```powershell
python 06_Automatizacion/do_check_med.py --all --format md --output 06_Automatizacion/reportes/do_check_med_repo.md
```

Para generar el tablero de estado:

```powershell
python 06_Automatizacion/lab_status_board.py --format md --output 06_Automatizacion/reportes/lab_status_board.md
```

Para generar continuidad integrada:

```powershell
python 06_Automatizacion/lab_continuity_report.py --format md --output 06_Automatizacion/reportes/lab_continuity_report.md
```

Para clasificar advertencias y riesgos:

```powershell
python 06_Automatizacion/lab_risk_classifier.py --format md --output 06_Automatizacion/reportes/lab_risk_report.md
```

Para generar resumen ejecutivo:

```powershell
python 06_Automatizacion/lab_executive_summary.py --format md --output 06_Automatizacion/reportes/lab_executive_summary.md
```

Para ejecutar la corrida unificada:

```powershell
python 06_Automatizacion/lab_run.py
```

Para ejecutar el Auditor v0 no mutante:

```powershell
python 06_Automatizacion/auditor_v0.py --format md --output 06_Automatizacion/reportes/auditor_v0_report.md
python 06_Automatizacion/auditor_v0.py --format json --output 06_Automatizacion/reportes/auditor_v0_report.json
python 06_Automatizacion/auditor_v0.py --format json --case-file 06_Automatizacion/fixtures/auditor_v0_cases.json
```

En el Auditor v0, la salida JSON y la carga externa por `--case-file` estan reactivadas en modo no mutante.

Para adaptar `DO_CHECK_REPORT` a `REPORT_ITEM`:

```powershell
python 06_Automatizacion/auditor_do_check_adapter.py 06_Automatizacion/reportes/do_check_med_repo.json --format md --output 06_Automatizacion/reportes/auditor_do_check_adapter_report.md
python 06_Automatizacion/auditor_do_check_adapter.py 06_Automatizacion/reportes/do_check_med_repo.json --format json --output 06_Automatizacion/reportes/auditor_do_check_adapter_report.json
```

Para validar la implementacion:

```powershell
python -m unittest 06_Automatizacion/test_auditor_v0.py
python -m unittest 06_Automatizacion/test_auditor_do_check_adapter.py
```

## Reportes iniciales

- `reportes/do_check_min_claves.md`: revision minima de archivos clave.
- `reportes/do_check_min_repo.md`: barrido informativo del repositorio.
- `reportes/do_check_min_repo.json`: barrido informativo en formato estructurado.
- `reportes/do_check_med_claves.md`: revision media de archivos clave.
- `reportes/do_check_med_repo.md`: barrido medio del repositorio.
- `reportes/do_check_med_repo.json`: barrido medio en formato estructurado.
- `reportes/lab_status_board.md`: tablero de estado en formato Markdown.
- `reportes/lab_status_board.json`: tablero de estado en formato estructurado.
- `reportes/lab_continuity_report.md`: continuidad integrada en formato Markdown.
- `reportes/lab_continuity_report.json`: continuidad integrada en formato estructurado.
- `reportes/lab_risk_report.md`: clasificacion de riesgos en formato Markdown.
- `reportes/lab_risk_report.json`: clasificacion de riesgos en formato estructurado.
- `reportes/lab_executive_summary.md`: resumen ejecutivo en formato Markdown.
- `reportes/lab_executive_summary.json`: resumen ejecutivo en formato estructurado.
- `reportes/lab_run_report.md`: corrida unificada en formato Markdown.
- `reportes/lab_run_report.json`: corrida unificada en formato estructurado.
- `reportes/auditor_v0_report.md`: reporte del Auditor v0 no mutante.
- `reportes/auditor_v0_report.json`: reporte estructurado del Auditor v0 no mutante.
- `reportes/auditor_do_check_adapter_report.md`: reporte del adaptador `DO_CHECK_REPORT`.
- `reportes/auditor_do_check_adapter_report.json`: reporte estructurado del adaptador `DO_CHECK_REPORT`.
- `fixtures/auditor_v0_cases.json`: matriz externa completa del Auditor v0.
- `fixtures/auditor_v0_case_schema.json`: esquema operativo inicial de casos externos del Auditor v0.

## Estado

Esta superficie pertenece a `AUT-001`.

`DO-CHECK-MIN-001` queda aceptado como MVP minimo provisional.

`DO-CHECK-MED-001` queda aceptado como fase media provisional. `DO-STATE-BOARD-001` queda aceptado como tablero de estado provisional. `DO-LAB-CONTINUITY-001` queda aceptado como continuidad integrada provisional. `DO-LAB-RUN-001` queda aceptado como comando unico provisional. `DO-LAB-RISK-001` queda aceptado como clasificador de riesgos provisional. `DO-LAB-SUMMARY-001` queda aceptado como resumen ejecutivo provisional. `AUDITOR-V0-001` queda aceptado como implementacion inicial no mutante conforme `C-002`. Ninguna herramienta transforma, autoriza cambios o cierra `AUT-001`.
