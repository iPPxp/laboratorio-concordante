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
- `r001_table_checks.py`: chequeos tabulares no mutantes para mini-pruebas locales `R-001` / `Xi`; declara la relacion formal local `R001-TB-001` con `AO-PPI-BRIDGE-001`.
- `ao_ext_confluence.py`: pruebas externas sinteticas no reguladas `EXT-CONF-001` y `EXT-CONF-002` para Confluencia local bajo `AO-001`; no cierra problemas globales.
- `ao_doc04_wide_tests.py`: pruebas sinteticas no reguladas `AO-DOC04-WIDE-TEST-001` para Documento 04 amplio v0 y la relacion local `REPORT_LAYER` / `Pi_rep`; no crea Nivel C ni cierra problemas globales.
- `ao_ppi_bridge_002.py`: bateria fuerte no mutante `AO-PPI-BRIDGE-002` para Confluencia y Equivalencia local de proyecciones; conserva abiertos los problemas globales.
- `ao_ppi_bridge_003.py`: matriz no mutante `AO-PPI-BRIDGE-003` de condiciones faltantes para cierre global, con casos heterogeneos de `REPORT_LAYER`; mantiene cierre global no autorizado.
- `report_layer_serialization.py`: serializacion local no mutante `AO-REPORT-SERIAL-001` de `REPORT_LAYER` entre frentes internos; conserva versionado, mapa de campos y campos protegidos sin promocion global.
- `report_layer_c002_gate.py`: compuerta no mutante `REPORT-LAYER-C002-GATE-001` para validar `REPORT_LAYER` como capa local pre-C conforme `C-002`; bloquea campos incompletos, promocion a Nivel C, recomendacion convertida en decision y cualquier modo mutante.
- `moc_eval.py`: simulacion no mutante `MOC-EVAL-001` para `MOC-001`; evalua `Xi_eval`, estados MOC, puente `MOC/TCS`, puente `MOC/AO`, `operator_trace`, `Pi_moc_trace`, `ao_bridge`, `protocol_v02` y concordancia entre evaluadores simulados con casos sinteticos no clinicos.

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
python 06_Automatizacion/auditor_v0.py --format json --case-file 06_Automatizacion/fixtures/auditor_v0_documental_cases.json
```

En el Auditor v0, la salida JSON y la carga externa por `--case-file` estan reactivadas en modo no mutante. El esquema externo declara variantes por `kind` y la implementacion bloquea casos documentales mal formados.

El fixture documental es una corrida parcial; debe conservar `transformacion_permitida = false` y no declara conformidad `C-002` completa.

Para adaptar `DO_CHECK_REPORT` a `REPORT_ITEM`:

```powershell
python 06_Automatizacion/auditor_do_check_adapter.py 06_Automatizacion/reportes/do_check_med_repo.json --format md --output 06_Automatizacion/reportes/auditor_do_check_adapter_report.md
python 06_Automatizacion/auditor_do_check_adapter.py 06_Automatizacion/reportes/do_check_med_repo.json --format json --output 06_Automatizacion/reportes/auditor_do_check_adapter_report.json
```

Para ejecutar los chequeos tabulares `R-001` / `Xi`:

```powershell
python 06_Automatizacion/r001_table_checks.py --format md --output 06_Automatizacion/reportes/r001_table_checks_report.md
python 06_Automatizacion/r001_table_checks.py --format json --output 06_Automatizacion/reportes/r001_table_checks_report.json
```

Para ejecutar las pruebas externas de Confluencia de `AO-001`:

```powershell
python 06_Automatizacion/ao_ext_confluence.py --format md --output 06_Automatizacion/reportes/ao_ext_confluence_report.md
python 06_Automatizacion/ao_ext_confluence.py --format json --output 06_Automatizacion/reportes/ao_ext_confluence_report.json
```

Para ejecutar las pruebas de Documento 04 amplio y `REPORT_LAYER`:

```powershell
python 06_Automatizacion/ao_doc04_wide_tests.py --format md --output 06_Automatizacion/reportes/ao_doc04_wide_report.md
python 06_Automatizacion/ao_doc04_wide_tests.py --format json --output 06_Automatizacion/reportes/ao_doc04_wide_report.json
```

Para ejecutar la bateria fuerte `AO-PPI-BRIDGE-002`:

```powershell
python 06_Automatizacion/ao_ppi_bridge_002.py --format md --output 06_Automatizacion/reportes/ao_ppi_bridge_002_report.md
python 06_Automatizacion/ao_ppi_bridge_002.py --format json --output 06_Automatizacion/reportes/ao_ppi_bridge_002_report.json
```

Para ejecutar la matriz `AO-PPI-BRIDGE-003`:

```powershell
python 06_Automatizacion/ao_ppi_bridge_003.py --format md --output 06_Automatizacion/reportes/ao_ppi_bridge_003_report.md
python 06_Automatizacion/ao_ppi_bridge_003.py --format json --output 06_Automatizacion/reportes/ao_ppi_bridge_003_report.json
```

Para ejecutar la serializacion local de `REPORT_LAYER`:

```powershell
python 06_Automatizacion/report_layer_serialization.py --format md --output 06_Automatizacion/reportes/report_layer_serialization_report.md
python 06_Automatizacion/report_layer_serialization.py --format json --output 06_Automatizacion/reportes/report_layer_serialization_report.json
```

Para ejecutar la relacion local `AO/TCS`:

```powershell
python 06_Automatizacion/ao_tcs_rel_001.py --format md --output 06_Automatizacion/reportes/ao_tcs_rel_001_report.md
python 06_Automatizacion/ao_tcs_rel_001.py --format json --output 06_Automatizacion/reportes/ao_tcs_rel_001_report.json
```

Para ejecutar el criterio local de autoridad entre niveles:

```powershell
python 06_Automatizacion/ao_authority_global_001.py --format md --output 06_Automatizacion/reportes/ao_authority_global_001_report.md
python 06_Automatizacion/ao_authority_global_001.py --format json --output 06_Automatizacion/reportes/ao_authority_global_001_report.json
```

Para ejecutar la cobertura externa amplia sintetica:

```powershell
python 06_Automatizacion/ao_ext_cov_001.py --format md --output 06_Automatizacion/reportes/ao_ext_cov_001_report.md
python 06_Automatizacion/ao_ext_cov_001.py --format json --output 06_Automatizacion/reportes/ao_ext_cov_001_report.json
```

Para ejecutar la matriz consolidada `AO-PPI-BRIDGE-004`:

```powershell
python 06_Automatizacion/ao_ppi_bridge_004.py --format md --output 06_Automatizacion/reportes/ao_ppi_bridge_004_report.md
python 06_Automatizacion/ao_ppi_bridge_004.py --format json --output 06_Automatizacion/reportes/ao_ppi_bridge_004_report.json
```

Para ejecutar la compuerta no mutante `REPORT_LAYER` / `C-002`:

```powershell
python 06_Automatizacion/report_layer_c002_gate.py --format md --output 06_Automatizacion/reportes/report_layer_c002_gate_report.md
python 06_Automatizacion/report_layer_c002_gate.py --format json --output 06_Automatizacion/reportes/report_layer_c002_gate_report.json
```

Para ejecutar la simulacion no mutante de `MOC-001`:

```powershell
python 06_Automatizacion/moc_eval.py --format md --output 06_Automatizacion/reportes/moc_eval_report.md
python 06_Automatizacion/moc_eval.py --format json --output 06_Automatizacion/reportes/moc_eval_report.json
```

Para validar la implementacion:

```powershell
python -m unittest 06_Automatizacion/test_auditor_v0.py
python -m unittest 06_Automatizacion/test_auditor_do_check_adapter.py
python -m unittest 06_Automatizacion/test_r001_table_checks.py
python -m unittest 06_Automatizacion/test_ao_ext_confluence.py
python -m unittest 06_Automatizacion/test_ao_doc04_wide_tests.py
python -m unittest 06_Automatizacion/test_ao_ppi_bridge_002.py
python -m unittest 06_Automatizacion/test_ao_ppi_bridge_003.py
python -m unittest 06_Automatizacion/test_report_layer_serialization.py
python -m unittest 06_Automatizacion/test_ao_tcs_rel_001.py
python -m unittest 06_Automatizacion/test_ao_authority_global_001.py
python -m unittest 06_Automatizacion/test_ao_ext_cov_001.py
python -m unittest 06_Automatizacion/test_ao_ppi_bridge_004.py
python -m unittest 06_Automatizacion/test_report_layer_c002_gate.py
python -m unittest 06_Automatizacion/test_moc_eval.py
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
- `reportes/r001_table_checks_report.md`: reporte de chequeos tabulares `R-001` / `Xi`.
- `reportes/r001_table_checks_report.json`: reporte estructurado de chequeos tabulares `R-001` / `Xi`.
- reportes/ao_ext_confluence_report.md: reporte de pruebas externas sinteticas de Confluencia `AO-EXT-CONF-001`.
- reportes/ao_ext_confluence_report.json: reporte estructurado de pruebas externas sinteticas de Confluencia.
- `reportes/ao_doc04_wide_report.md`: reporte de pruebas no mutantes de Documento 04 amplio y `REPORT_LAYER`.
- `reportes/ao_doc04_wide_report.json`: reporte estructurado de pruebas no mutantes de Documento 04 amplio y `REPORT_LAYER`.
- `reportes/ao_ppi_bridge_002_report.md`: reporte de bateria fuerte no mutante `AO-PPI-BRIDGE-002`.
- `reportes/ao_ppi_bridge_002_report.json`: reporte estructurado de bateria fuerte no mutante `AO-PPI-BRIDGE-002`.
- `reportes/ao_ppi_bridge_003_report.md`: reporte de matriz no mutante `AO-PPI-BRIDGE-003`.
- `reportes/ao_ppi_bridge_003_report.json`: reporte estructurado de matriz no mutante `AO-PPI-BRIDGE-003`.
- `reportes/report_layer_serialization_report.md`: reporte de serializacion local no mutante `AO-REPORT-SERIAL-001`.
- `reportes/report_layer_serialization_report.json`: reporte estructurado de serializacion local no mutante `AO-REPORT-SERIAL-001`.
- `reportes/ao_tcs_rel_001_report.md`: reporte de relacion local `AO/TCS`.
- `reportes/ao_tcs_rel_001_report.json`: reporte estructurado de relacion local `AO/TCS`.
- `reportes/ao_authority_global_001_report.md`: reporte de criterio local de autoridad entre niveles.
- `reportes/ao_authority_global_001_report.json`: reporte estructurado de criterio local de autoridad entre niveles.
- `reportes/ao_ext_cov_001_report.md`: reporte de cobertura externa amplia sintetica no regulada.
- `reportes/ao_ext_cov_001_report.json`: reporte estructurado de cobertura externa amplia sintetica no regulada.
- `reportes/ao_ppi_bridge_004_report.md`: reporte de matriz consolidada no mutante `AO-PPI-BRIDGE-004`.
- `reportes/ao_ppi_bridge_004_report.json`: reporte estructurado de matriz consolidada no mutante `AO-PPI-BRIDGE-004`.
- `reportes/report_layer_c002_gate_report.md`: reporte de compuerta no mutante `REPORT_LAYER` / `C-002`.
- `reportes/report_layer_c002_gate_report.json`: reporte estructurado de compuerta no mutante `REPORT_LAYER` / `C-002`.
- `reportes/moc_eval_report.md`: reporte de simulacion no mutante `MOC-EVAL-001` con trazas de operadores, rol local de puente AO y protocolo v0.2.
- `reportes/moc_eval_report.json`: reporte estructurado de simulacion no mutante `MOC-EVAL-001` con `operator_trace`, `ao_bridge` y `protocol_v02`.
- `fixtures/auditor_v0_cases.json`: matriz externa completa del Auditor v0.
- `fixtures/auditor_v0_case_schema.json`: esquema operativo inicial de casos externos del Auditor v0.
- `fixtures/auditor_v0_documental_cases.json`: fixture documental parcial no mutante.
- `fixtures/ao_ext_confluence_cases.json`: fixture sintetico no regulado para `EXT-CONF-001` y `EXT-CONF-002`.
- `fixtures/ao_doc04_wide_cases.json`: fixture sintetico no regulado para `AO-DOC04-WIDE-TEST-001`.
- `fixtures/ao_ppi_bridge_002_cases.json`: fixture sintetico fuerte para `AO-PPI-BRIDGE-002`.
- `fixtures/ao_ppi_bridge_003_matrix.json`: fixture de matriz de condiciones faltantes y casos heterogeneos `REPORT_LAYER` para `AO-PPI-BRIDGE-003`.
- `fixtures/report_layer_serialization_cases.json`: fixture de serializacion interfrente local `AO-REPORT-SERIAL-001`.
- `fixtures/ao_tcs_rel_001_cases.json`: fixture de relacion local `AO/TCS`.
- `fixtures/ao_authority_global_001_cases.json`: fixture de criterio local de autoridad entre niveles.
- `fixtures/ao_ext_cov_001_cases.json`: fixture de cobertura externa amplia sintetica.
- `fixtures/ao_ppi_bridge_004_matrix.json`: fixture de matriz consolidada posterior a las rutas AO defendibles.
- `fixtures/report_layer_c002_cases.json`: fixture sintetico para `REPORT-LAYER-C002-GATE-001`.
- `fixtures/moc_cases.json`: fixture sintetico no clinico para `MOC-EVAL-001`.

## Estado

Esta superficie pertenece a `AUT-001`.

`DO-CHECK-MIN-001` queda aceptado como MVP minimo provisional.

`DO-CHECK-MED-001` queda aceptado como fase media provisional. `DO-STATE-BOARD-001` queda aceptado como tablero de estado provisional. `DO-LAB-CONTINUITY-001` queda aceptado como continuidad integrada provisional. `DO-LAB-RUN-001` queda aceptado como comando unico provisional. `DO-LAB-RISK-001` queda aceptado como clasificador de riesgos provisional. `DO-LAB-SUMMARY-001` queda aceptado como resumen ejecutivo provisional. `AUDITOR-V0-001` queda aceptado como implementacion inicial no mutante conforme `C-002`. `R001-TABLE-CHECK-001` queda integrado como prueba local no mutante y reporta `R001-TB-001` como relacion formal local con AO. `AO-EXT-CONF-001` queda integrado como prueba externa sintetica no regulada para `AO-001`; conserva abiertas Confluencia global, Equivalencia global, exportacion general de R4/Gamma y maduracion de `TCS-001`. `AO-DOC04-WIDE-TEST-001` queda integrado como prueba sintetica de Documento 04 amplio y `REPORT_LAYER`; conserva `REPORT_LAYER` como capa local pre-C y no crea Nivel C. `AO-PPI-BRIDGE-002` queda integrado como bateria fuerte no mutante de Confluencia y Equivalencia local; conserva abiertos los problemas globales. `AO-PPI-BRIDGE-003` queda integrado como matriz de condiciones faltantes para cierre global y ampliacion heterogenea de `REPORT_LAYER`; mantiene cierre global no autorizado. `AO-REPORT-SERIAL-001` queda integrado como serializacion local interfrente de `REPORT_LAYER`; atiende localmente `AO-PPI-GC-004` sin autorizar promocion global. `AO-TCS-REL-001`, `AO-AUTH-GLOBAL-001`, `AO-EXT-COV-001` y `AO-PPI-BRIDGE-004` quedan integrados como rutas locales no mutantes para relacion `AO/TCS`, autoridad entre niveles, cobertura externa y matriz consolidada; reducen deudas en grado local o parcial local, pero mantienen `global_closure_authorized: false`. `REPORT-LAYER-C002-GATE-001` queda integrado como compuerta no mutante previa a cualquier modo mutante de `REPORT_LAYER`. `MOC-EVAL-001` queda integrado como simulacion no mutante de `MOC-001` y emite `operator_trace` para `MOC-TCS-BRIDGE-001`, `Pi_moc_trace` / `ao_bridge` para `MOC-AO-BRIDGE-001` y `protocol_v02` para `MOC-EVAL-PROTO-002`; conserva `MOC-001` provisional, `TCS-001` no canonico y `H-Xi` no admitida. Ninguna herramienta transforma, autoriza cambios o cierra `AUT-001`.
