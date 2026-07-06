# Estado actual del proyecto

Estatus: estado operativo vigente.

Fecha de inicializacion del repositorio: 2026-07-01.

## Documentos oficiales consolidados

- [x] Documento 00 - Naturaleza: consolidado desde fuentes previas por `D-2026-07-03-011`.
- [x] Documento 01 - Canon: consolidado desde fuentes previas por `D-2026-07-03-011`.
- [x] Documento 02 - Fundamentos Matematicos: consolidado desde fuentes previas por `D-2026-07-03-011`.
- [x] Documento 03 - Ontologia: consolidado desde fuentes previas por `D-2026-07-03-011`.
- [x] Documento 04 - Algebra Operacional: actualizado como version amplia v0 por `D-2026-07-06-006` sobre la consolidacion inicial de `D-2026-07-03-011`; probado localmente contra casos iniciales y precisado frente a `REPORT_LAYER` por `D-2026-07-06-007`; `REPORT_LAYER` queda local pre-C por `D-2026-07-06-014` y con compuerta no mutante `C-002` por `D-2026-07-06-015`.

## Documentos oficiales de Nivel C

- [x] `C-002_RFC_Operativo_Auditor_v0.md`: RFC operativo oficial del Auditor v0; complementa `C-001` y quedo alineado el 2026-07-03 con JSON, fixtures y adaptador no mutante.
- [x] `C-001_Especificacion_Tecnica_Auditor.md`: especificacion tecnica oficial inicial del Auditor.

## Consolidacion en este repositorio

- [x] Incorporar version completa del Documento 00 desde fuentes previas.
- [x] Incorporar version completa del Documento 01 desde fuentes previas.
- [x] Incorporar version completa del Documento 02 desde fuentes previas.
- [x] Incorporar version completa del Documento 03 desde fuentes previas.
- [x] Actualizar Documento 04 - Algebra Operacional desde `AO-001` y fuentes previas.

## Expedientes abiertos

- `MOC-001` (expediente integrador teorico-operativo abierto por `D-2026-07-05-011`; `Xi_eval`, metricas, protocolo, simulacion, diseno empirico futuro, rutas ejecutadas, puentes formales, paquete pre-ejecucion, paquete de registro/auditoria, rutas posteriores y relacion documental con `C-001` / `C-002` aceptadas por `D-2026-07-05-012` a `D-2026-07-06-013`; queda en `MOC-ROUTE-011`, mantenimiento teorico-operativo sin ejecucion, con `MOC-ROUTE-012` como puente documental local con Nivel C; no Canon, no clinico, no regulado)
- `TCS-001` (expediente teorico provisional; paquete minimo aceptado por `D-2026-07-03-019` y maduracion provisional `TCS-MAT-PROV-001` aceptada por `D-2026-07-05-010`; no Canon, no documento oficial)
- `AO-001` (expediente preparatorio abierto para Algebra Operacional; `AO-MARCO-001`, `GAMMA-EXT-AO-001`, `AO-CASE-BAT-001`, `AO-R4-GAMMA-USE-001`, `AO-PPI-BRIDGE-001`, `AO-DOC04-FORM-CHK-001`, `AO-CONF-EXT-OPTIONS-001`, `AO-EXT-CONF-EXEC-001`, `AO-DOC04-FORM-001`, `AO-R4-GAMMA-EXPORT-GATE-001`, `AO-DOC04-WIDE-001`, `AO-DOC04-WIDE-TEST-001`, `AO-REPORT-LAYER-BRIDGE-001` y `AO-REPORT-LAYER-NIVEL-C-001` aceptados localmente; sigue abierto para pruebas globales no resueltas)

## Expedientes transferidos

- `PSI-001` (independizado por `D-2026-07-03-006` como proyecto `Psicologia Concordante`; copia local de traspaso eliminada por `D-2026-07-03-012`, sin continuidad activa interna)

## Expedientes cerrados

- `DOCS-001`
- `P-PI.0` / `P-PI.1`
- `B-001`
- `CP-001`
- `EF-001`
- `DO-001`
- `RH-001`
- `RH-002`
- `REC-001`
- `AUT-001`
- `R001-001`
- `AUT-002`
- `AUD-001`
- `HXI-001`

## Expedientes congelados

- `B-001.5`
- `H-B.6` (brote alterno y original historico; congelado por `D-2026-07-03-013`)
- `H-B.7` (brote alterno y original historico; congelado por `D-2026-07-03-013`)

## Expedientes pendientes de clasificacion

- Ninguno registrado.

## Hipotesis activas

- Ninguna hipotesis `H-B` activa; `H-B.6` y `H-B.7` quedan congeladas como brotes alternos y originales historicos.

## Hipotesis externas materializadas no admitidas

- `H-Xi` en `03_Expedientes/H-Xi.md`: hipotesis externa no admitida; `HXI-001` queda cerrado en mantenimiento local por `D-2026-07-06-012`, con `Xi_eval` solo como herramienta local historica/auxiliar; fuente primaria historica `SRC-020`; no Canon, no documento oficial, no operador vigente.

## Problemas abiertos

- Maduracion de `MOC-001` en mantenimiento teorico-operativo sin ejecucion (`MOC-ROUTE-011`) despues de `D-2026-07-06-008`; no autoriza piloto, reclutamiento, respuestas reales, datos personales, canonizacion ni dominios clinicos o regulados.
- Confluencia.
- Equivalencia de proyecciones.
- Promocion o exportacion general fuera de `AUD-001` de `R4-FORMAL-AUD-001`; bloqueada provisionalmente por `D-2026-07-05-009`.
- Promocion o exportacion general fuera de pruebas locales controladas de `GAMMA-FORMAL-AUD-001`; bloqueada provisionalmente por `D-2026-07-05-009`.
- Pruebas heterogeneas adicionales de la formalizacion amplia v0 del Documento 04 si una decision futura exige mas cobertura; la prueba local inicial de `AO-DOC04-WIDE-001`, la relacion con `REPORT_LAYER`, la justificacion de no promocion a Nivel C y la compuerta no mutante conforme a `C-002` quedan atendidas por `D-2026-07-06-007`, `D-2026-07-06-014` y `D-2026-07-06-015`, sin cerrar Confluencia global, Equivalencia global ni posible especificacion tecnica posterior.
- Maduracion de `TCS-001` mas alla de `TCS-MAT-PROV-001`.
- Relacion global posterior entre `R001-TB-001`, Equivalencia global y Confluencia global.
- Pruebas externas adicionales no reguladas si una decision futura exige mas evidencia para fortalecer Confluencia o Equivalencia global.

## Contratos provisionales activos

- `AUD-001_Contrato_Reportes.md`: `OPERATOR_REPORT`, `MP_FAIL_REPORT`, `CR_FAIL_REPORT`, `TAU_REPORT`, `D_REPORT`, `TR_PROPOSAL_REPORT`, `TR_EXECUTION_REPORT`, `TR_EXECUTION_FAIL_REPORT` y `REVERSAL_REPORT`.
- `AUD-001_REPORT_LAYER_Candidata.md`: `REPORT-LAYER-CAND-001`, capa abstracta candidata para reportes equivalentes dentro de `AUD-001`.
- `AUD-001_SPEC-RFC-AUDITOR-V0_Candidata.md`: `SPEC-RFC-AUDITOR-V0`, candidata promovida a `C-002`.

## Propuestas provisionales promovidas o cerradas

- `DO-PROP-001`: propuesta provisional de automatizacion en `03_Expedientes/DO-001.md`; absorbida por `C-001`.
- `SPEC-AUD-001_Candidata`: especificacion tecnica candidata del Auditor en `03_Expedientes/DO-001_SPEC-AUD-001_Candidata.md`; promovida a `C-001`.
- `SPEC-RFC-AUDITOR-V0`: candidata tipo RFC en `03_Expedientes/AUD-001_SPEC-RFC-AUDITOR-V0_Candidata.md`; promovida a `C-002`.

## Marcos iniciales de expediente

- `AO-001_Marco_Inicial_Algebra_Operacional.md`: `AO-MARCO-001`, marco inicial provisional aceptado para formalizar operaciones sobre artefactos, estatus, evidencia, reportes, decisiones, permisos, invariantes, transformaciones y salidas de seguridad; incorporado al Documento 04 por `D-2026-07-03-011`.

## Pruebas externas locales

- `AO-001_Prueba_Gamma_Externa.md`: `GAMMA-EXT-AO-001`, primera prueba positiva externa local de `Gamma_1`; produce `G_AO_OP-GOV-001` como criterio formal local de expediente y no promueve `Gamma`.

## Baterias y puentes locales

- `MOC-001_Formalizacion_Xi_eval.md`: `MOC-XI-EVAL-FORMAL-001`, formalizacion local de `Xi_eval` para casos sinteticos no clinicos; aceptada por `D-2026-07-05-012`.
- `MOC-001_Metricas_Estados.md` y `MOC-001_Protocolo_Evaluacion.md`: `MOC-METRIC-STATE-001` y `MOC-EVAL-PROTO-001`, metrica cualitativa ordinal y protocolo reproducible; aceptados por `D-2026-07-05-013`.
- `MOC-001_Casos_No_Clinicos.md`: `MOC-CASE-BAT-001`, bateria sintetica no clinica para `MOC-EVAL-001`; ampliada por `MOC-ROUTE-002` y aceptada por `D-2026-07-05-018`.
- `MOC-001_Disenio_Estudio_Empirico.md`: `MOC-EMP-STUDY-001`, diseno documental de comparacion empirica futura; aceptado por `D-2026-07-05-015`.
- `MOC-001_Ejecucion_Ruta_Valida_001.md`: `MOC-ROUTE-EXEC-001`, primera ruta valida ejecutada favorablemente; aceptada por `D-2026-07-05-016`.
- `MOC-001_Siguientes_Rutas_Validas.md`: `MOC-NEXT-ROUTES-001`, matriz de rutas posteriores; aceptada por `D-2026-07-05-017`.
- `MOC-001_Ejecucion_Ruta_002.md`: `MOC-ROUTE-002`, ampliacion de bateria sintetica no clinica con desacuerdos justificados y casos limite; aceptada por `D-2026-07-05-018`.
- `MOC-001_Rutas_Posteriores_Ruta_002.md`: `MOC-NEXT-ROUTES-002`, matriz posterior que recomienda `MOC-ROUTE-003`; aceptada por `D-2026-07-05-019`.
- `MOC-001_Puente_Formal_MOC_TCS.md`: `MOC-TCS-BRIDGE-001`, formalizacion ejecutable local de operadores `MOC/TCS`; aceptada por `D-2026-07-05-020`.
- `MOC-001_Rutas_Posteriores_Ruta_003.md`: `MOC-NEXT-ROUTES-003`, matriz posterior que recomienda `MOC-ROUTE-004`; aceptada por `D-2026-07-05-021`.
- `MOC-001_Puente_Formal_MOC_AO.md`: `MOC-AO-BRIDGE-001`, formalizacion local del puente `MOC/AO` mediante `operator_trace`, `Pi_moc_trace` y `ao_bridge`; aceptada por `D-2026-07-05-022`.
- `MOC-001_Rutas_Posteriores_Ruta_004.md`: `MOC-NEXT-ROUTES-004`, matriz posterior que recomienda `MOC-ROUTE-005`; aceptada por `D-2026-07-05-023`.
- `MOC-001_Protocolo_Evaluacion_v0_2.md`: `MOC-EVAL-PROTO-002`, protocolo v0.2 con ejes de desacuerdo y tratamiento por traza; aceptado por `D-2026-07-05-024`.
- `MOC-001_Ejecucion_Ruta_005.md`: `MOC-ROUTE-005`, refinamiento de protocolo ejecutado favorablemente; aceptado por `D-2026-07-05-024`.
- `MOC-001_Rutas_Posteriores_Ruta_005.md`: `MOC-NEXT-ROUTES-005`, matriz posterior que recomienda `MOC-ROUTE-006`; aceptada por `D-2026-07-05-025`.
- `MOC-001_Protocolo_Piloto_Empirico_Futuro.md`: `MOC-EMP-PILOT-PROTO-001`, protocolo documental de piloto empirico futuro preparado sin ejecucion real; aceptado por `D-2026-07-06-001`.
- `MOC-001_Rutas_Posteriores_Ruta_006.md`: `MOC-NEXT-ROUTES-006`, matriz posterior que recomienda `MOC-ROUTE-007`; aceptada por `D-2026-07-06-002`.
- `MOC-001_Compuerta_Autorizacion_Ejecucion_Piloto.md`: `MOC-GATE-PILOT-EXEC-001`, compuerta aplicada con resultado `no_autorizar_ejecucion`; aceptada por `D-2026-07-06-003`.
- `MOC-001_Semantica_Provisional.md`: `MOC-SEM-PROV-001`, semantica provisional local; aceptada por `D-2026-07-06-004`.
- `MOC-001_Tabla_Operaciones_Formales.md`: `MOC-OPS-FORMAL-001`, tabla de operaciones formales locales; aceptada por `D-2026-07-06-004`.
- `MOC-001_Casos_Congelados_Piloto.md`: `MOC-PILOT-CASE-FREEZE-001`, paquete congelado de 11 casos sinteticos; aceptado por `D-2026-07-06-004`.
- `MOC-001_Plantilla_Respuesta_Evaluadores.md`: `MOC-PILOT-RESPONSE-TPL-001`, plantilla sin datos personales; aceptada por `D-2026-07-06-004`.
- `MOC-001_Reglas_Protocolo_Congelados.md`: `MOC-PILOT-RULE-FREEZE-001`, version congelada de reglas/protocolo; aceptada por `D-2026-07-06-004`.
- `MOC-001_Paquete_PreEjecucion_Piloto.md`: `MOC-PREEXEC-PACK-001`, paquete documental pre-ejecucion; aceptado por `D-2026-07-06-004`.
- `MOC-001_Metodo_Registro_Sin_Datos_Personales.md`: `MOC-PILOT-NODATA-REG-001`, metodo documental de registro sin datos personales; aceptado por `D-2026-07-06-005`.
- `MOC-001_Matriz_Auditoria_Piloto.md`: `MOC-PILOT-AUDIT-MATRIX-001`, matriz documental de auditoria de piloto; aceptada por `D-2026-07-06-005`.
- `MOC-001_Paquete_Registro_Auditoria_Piloto.md`: `MOC-PILOT-REG-AUDIT-PACK-001`, paquete documental de registro y auditoria; aceptado por `D-2026-07-06-005`.
- `MOC-001_Rutas_Posteriores_Ruta_010.md`: `MOC-NEXT-ROUTES-010`, rutas posteriores decididas despues del paquete de registro/auditoria; aceptado por `D-2026-07-06-008`.
- `MOC-001_Auditoria_Rutas_Posteriores_Ruta_010.md`: auditoria favorable con limites de `MOC-NEXT-ROUTES-010`.
- `MOC-001_Decision_Rutas_Posteriores_Ruta_010.md`: decision que fija `MOC-ROUTE-011` como mantenimiento teorico-operativo sin ejecucion.
- `MOC-001_Relacion_Documental_C001_C002.md`: `MOC-C001-C002-REL-001`, puente documental local que lee `C-001` como frontera tecnica y `C-002` como secuencia operativa; aceptado por `D-2026-07-06-013`.
- `MOC-001_Auditoria_Relacion_Documental_C001_C002.md`: auditoria favorable con limites de `MOC-C001-C002-REL-001`.
- `MOC-001_Decision_Relacion_Documental_C001_C002.md`: decision que ejecuta `MOC-ROUTE-012` sin modificar Nivel C ni promover MOC.
- `AO-001_Casos_Prueba_Algebra_Operacional.md`: `AO-CASE-BAT-001`, casos `AO-CASE-001` a `AO-CASE-006` aceptados por `D-2026-07-03-016`.
- `AO-001_Criterios_Uso_R4_Gamma_Fuera_AUD.md`: `AO-R4-GAMMA-USE-001`, criterio local para referencia formal, prueba controlada o puente de problema; aceptado por `D-2026-07-03-017`.
- `AO-001_Puente_Confluencia_Equivalencia.md`: `AO-PPI-BRIDGE-001`, avance local con `AO-PPI-EQ-001` y `AO-PPI-CONF-001`; aceptado por `D-2026-07-03-018`.
- `TCS-001_Definiciones_Minimas.md`, `TCS-001_Tipologia_Fallos_Concordancia.md` y `TCS-001_Casos_Prueba.md`: paquete minimo teorico provisional aceptado por `D-2026-07-03-019`.
- `TCS-001_Maduracion_Provisional.md`: `TCS-MAT-PROV-001`, metrica cualitativa, casos externos no regulados y conflicto de autoridades; aceptado por `D-2026-07-05-010`.
- `R001-001_Integracion_Table_Checks.md`: `R001-TABLE-CHECK-001`, bateria tecnica local de 20 chequeos tabulares, aceptada por `D-2026-07-05-004`.
- `R001-001_Relacion_Formal_AO.md`: `R001-TB-001`, instancia tabular local conectada con `AO-PPI-BRIDGE-001`, aceptada por `D-2026-07-05-005`.
- `AO-001_Evaluacion_Formalizacion_Doc04_R001_TB.md`: `AO-DOC04-FORM-CHK-001`, candidata formal de `Pi_tb` / `Eq_tb` para Documento 04; continuada por `D-2026-07-05-008`.
- `AO-001_Opciones_Prueba_Confluencia_Externa.md`: `AO-CONF-EXT-OPTIONS-001`, opciones externas no reguladas; `EXT-CONF-001` queda ejecutada despues por `D-2026-07-05-007`.
- `AO-001_Pruebas_Externas_Confluencia.md`: `AO-EXT-CONF-EXEC-001`, ejecucion de `EXT-CONF-001` y `EXT-CONF-002`; aceptada por `D-2026-07-05-007`.
- `AO-001_Formalizacion_Acotada_Doc04_R001_TB.md`: `AO-DOC04-FORM-001`, incorporacion acotada de `Pi_tb` / `Eq_tb` al Documento 04; aceptada por `D-2026-07-05-008`.
- `AO-001_Compuerta_Exportacion_R4_Gamma.md`: `AO-R4-GAMMA-EXPORT-GATE-001`, compuerta que bloquea exportacion general y conserva perfil restringido interoperable; aceptada por `D-2026-07-05-009`.
- `AO-001_Formalizacion_Amplia_Doc04.md`: `AO-DOC04-WIDE-001`, formalizacion amplia v0 de Documento 04 con contrato comun de operador, `operator_trace`, proyecciones, `Eq_local`, `Conf_local`, `Gate_AO` y perfiles restringidos R4/Gamma; aceptada por `D-2026-07-06-006`.
- `AO-001_Pruebas_AO-DOC04-WIDE_REPORT_LAYER.md`: `AO-DOC04-WIDE-TEST-001`, prueba local no mutante de `AO-DOC04-WIDE-001` con 8 casos, 8 aprobados y 0 fallos; aceptada por `D-2026-07-06-007`.
- `AO-001_Relacion_REPORT_LAYER_Doc04_Amplio.md`: `AO-REPORT-LAYER-BRIDGE-001`, precision formal local de `REPORT_LAYER` como entrada de `Pi_rep(REPORT_LAYER, C, W) -> R_rep | B`, sin promocion a Nivel C.
- `AO-001_Justificacion_REPORT_LAYER_Nivel_C.md`: `AO-REPORT-LAYER-NIVEL-C-001`, justificacion formal de que `REPORT_LAYER` permanece local pre-C; aceptada por `D-2026-07-06-014`.

## Algoritmos provisionales activos

- `MOC-EVAL-001`: simulacion no mutante de `MOC-001` en `06_Automatizacion/moc_eval.py`; usa `06_Automatizacion/fixtures/moc_cases.json`, genera reportes Markdown/JSON, ejecuta 11 casos sinteticos, emite `operator_trace`, `Pi_moc_trace`, `ao_bridge` y `protocol_v02`, y no admite `H-Xi`, no canoniza `Xi` ni abre uso clinico.
- `R001-TABLE-CHECK-001`: chequeos tabulares no mutantes `R-001` / `Xi` en `06_Automatizacion/r001_table_checks.py`; aceptado por `D-2026-07-05-004`.
- `R001-TB-001`: relacion formal local entre `R001-TABLE-CHECK-001` y `AO-PPI-BRIDGE-001` en `03_Expedientes/R001-001_Relacion_Formal_AO.md`; aceptada por `D-2026-07-05-005`.
- `AO-EXT-CONF-001`: pruebas externas sinteticas no reguladas de Confluencia en `06_Automatizacion/ao_ext_confluence.py`; ejecuta `EXT-CONF-001` y `EXT-CONF-002`.
- `AO-DOC04-WIDE-TEST-001`: prueba no mutante de `AO-DOC04-WIDE-001` y `REPORT_LAYER` en `06_Automatizacion/ao_doc04_wide_tests.py`; usa `06_Automatizacion/fixtures/ao_doc04_wide_cases.json` y genera reportes Markdown/JSON.
- `REPORT-LAYER-C002-GATE-001`: compuerta no mutante conforme a `C-002` en `06_Automatizacion/report_layer_c002_gate.py`; usa `06_Automatizacion/fixtures/report_layer_c002_cases.json`, genera reportes Markdown/JSON y queda integrada a `DO-LAB-RUN-001` por `D-2026-07-06-015`.
- `DO-CHECK-001`: verificador no mutante de trazabilidad y estatus en `03_Expedientes/DO-001_DO-CHECK-001.md`; validado inicialmente contra tres archivos locales.
- `DO-CHECK-MIN-001`: implementacion minima no mutante en `06_Automatizacion/do_check_min.py`; validada provisionalmente por ejecucion equivalente en `AUT-001`.
- `DO-CHECK-MED-001`: implementacion media no mutante en `06_Automatizacion/do_check_med.py`; validada provisionalmente por ejecucion equivalente en `AUT-001`.
- `DO-STATE-BOARD-001`: tablero no mutante en `06_Automatizacion/lab_status_board.py`; validado provisionalmente por ejecucion equivalente en `AUT-001`.
- `DO-LAB-CONTINUITY-001`: continuidad integrada no mutante en `06_Automatizacion/lab_continuity_report.py`; validada provisionalmente por reportes fuente en `AUT-001`.
- `DO-LAB-RUN-001`: comando unico no mutante en `06_Automatizacion/lab_run.py`; validado provisionalmente como corrida local unificada de `AUT-001`.
- `DO-LAB-RISK-001`: clasificador no mutante refinado en `06_Automatizacion/lab_risk_classifier.py`; separa riesgos activos, advertencias controladas, deuda documental y advertencias heredadas.
- `DO-LAB-SUMMARY-001`: resumen ejecutivo automatico no mutante en `06_Automatizacion/lab_executive_summary.py`; validado provisionalmente para sintetizar estado, riesgos y siguiente accion.
- `referencia_historica_transferida`: clasificacion tecnica aceptada en `AUT-002` para referencias `PSI-001*` eliminadas por decision vigente.
- `AUT-CLOSE-CRIT-001`: criterios de cierre de fase media en `03_Expedientes/AUT-001_Criterios_Cierre_Fase_Media.md`.
- `AUT-RISK-TREAT-001`: tratamiento inicial de riesgos altos en `03_Expedientes/AUT-001_Tratamiento_Riesgos_Altos.md`.
- `AUT-RISK-ACT-REVIEW-001`: matriz de revision de riesgos activos en `03_Expedientes/AUT-001_Matriz_Revision_Riesgos_Activos.md`.
- `AUT-RISK-REFINE-001`: refinamiento contextual de riesgos en `03_Expedientes/AUT-001_Refinamiento_DO-LAB-RISK.md`.
- `AUT-RISK-REFINE-002`: refinamiento de contexto de guardrails en `03_Expedientes/AUT-001_Refinamiento_Contexto_Guardrails.md`.
- `AUT-CLOSE-TECH-001`: cierre tecnico provisional en `03_Expedientes/AUT-001_Decision_Cierre_Tecnico_Provisional.md`.
- No hay algoritmos, matrices ni compuertas PSI activas dentro del Laboratorio; el paquete local `PSI-001*` fue eliminado por `D-2026-07-03-012`.

## Auditorias provisionales registradas

- `MOC-001_Auditoria_Apertura.md`: auditoria favorable de apertura de `MOC-001`.
- `MOC-001_Auditoria_Formalizacion_Xi_eval.md`: auditoria favorable de `MOC-XI-EVAL-FORMAL-001`.
- `MOC-001_Auditoria_Metricas_Protocolo.md`: auditoria favorable de metricas y protocolo.
- `MOC-001_Auditoria_Simulacion_Software.md`: auditoria favorable de casos sinteticos y `MOC-EVAL-001`.
- `MOC-001_Auditoria_Disenio_Estudio_Empirico.md`: auditoria favorable del diseno empirico futuro.
- `MOC-001_Auditoria_Ejecucion_Ruta_Valida_001.md`: auditoria favorable de `MOC-ROUTE-EXEC-001`.
- `MOC-001_Auditoria_Siguientes_Rutas_Validas.md`: auditoria favorable de `MOC-NEXT-ROUTES-001`.
- `MOC-001_Auditoria_Ejecucion_Ruta_002.md`: auditoria favorable de `MOC-ROUTE-002`.
- `MOC-001_Auditoria_Rutas_Posteriores_Ruta_002.md`: auditoria favorable de `MOC-NEXT-ROUTES-002`.
- `MOC-001_Auditoria_Puente_Formal_MOC_TCS.md`: auditoria favorable de `MOC-TCS-BRIDGE-001`.
- `MOC-001_Auditoria_Rutas_Posteriores_Ruta_003.md`: auditoria favorable de `MOC-NEXT-ROUTES-003`.
- `MOC-001_Auditoria_Puente_Formal_MOC_AO.md`: auditoria favorable de `MOC-AO-BRIDGE-001`.
- `MOC-001_Auditoria_Rutas_Posteriores_Ruta_004.md`: auditoria favorable de `MOC-NEXT-ROUTES-004`.
- `MOC-001_Auditoria_Ejecucion_Ruta_005.md`: auditoria favorable de `MOC-ROUTE-005`.
- `MOC-001_Auditoria_Rutas_Posteriores_Ruta_005.md`: auditoria favorable de `MOC-NEXT-ROUTES-005`.
- `MOC-001_Auditoria_Protocolo_Piloto_Empirico_Futuro.md`: auditoria favorable de `MOC-EMP-PILOT-PROTO-001`.
- `MOC-001_Auditoria_Rutas_Posteriores_Ruta_006.md`: auditoria favorable de `MOC-NEXT-ROUTES-006`.
- `MOC-001_Auditoria_Compuerta_Autorizacion_Ejecucion_Piloto.md`: auditoria favorable a no autorizacion de ejecucion real del piloto.
- `MOC-001_Auditoria_Paquete_PreEjecucion_Piloto.md`: auditoria favorable de `MOC-PREEXEC-PACK-001`.
- `MOC-001_Auditoria_Paquete_Registro_Auditoria_Piloto.md`: auditoria favorable de `MOC-PILOT-REG-AUDIT-PACK-001`.
- `MOC-001_Auditoria_Rutas_Posteriores_Ruta_010.md`: auditoria favorable de `MOC-NEXT-ROUTES-010`; fija mantenimiento sin ejecucion como ruta posterior.
- `MOC-001_Auditoria_Relacion_Documental_C001_C002.md`: auditoria favorable con limites de `MOC-C001-C002-REL-001`; acepta relacion documental local con `C-001` / `C-002` sin Nivel C nuevo.
- `AO-001_Auditoria_REPORT_LAYER_Nivel_C.md`: auditoria favorable de `AO-REPORT-LAYER-NIVEL-C-001`; mantiene `REPORT_LAYER` local pre-C.
- `AUT-003_Auditoria_Herramienta_REPORT_LAYER_C002.md`: auditoria favorable de `REPORT-LAYER-C002-GATE-001` como herramienta local no mutante.
- `RH-001_Auditoria_Reconciliacion_PM001.md`: auditoria favorable de `RH-PM-REC-001`; mantiene `PM-001` como deuda condicionada.
- `AO-001_Auditoria_Pruebas_Externas_Confluencia.md`: auditoria favorable de `AO-EXT-CONF-EXEC-001`; acepta ejecucion local sin cierre global.
- `AO-001_Auditoria_Formalizacion_Acotada_Doc04.md`: auditoria favorable de `AO-DOC04-FORM-001`; acepta incorporacion acotada sin cierre global.
- `AO-001_Auditoria_Compuerta_Exportacion_R4_Gamma.md`: auditoria favorable del bloqueo controlado de exportacion general R4/Gamma.
- `AO-001_Auditoria_Formalizacion_Amplia_Doc04.md`: auditoria favorable con limites de `AO-DOC04-WIDE-001`; acepta formalizacion amplia v0 sin cierre global ni Nivel C.
- `AO-001_Auditoria_Pruebas_AO-DOC04-WIDE_REPORT_LAYER.md`: auditoria favorable de `AO-DOC04-WIDE-TEST-001` y `AO-REPORT-LAYER-BRIDGE-001`; acepta prueba local y precision de `REPORT_LAYER` sin promocion ni permiso de transformacion.
- `AO-001_Auditoria_Formalizacion_Doc04_Confluencia_Externa.md`: auditoria favorable de la ruta defensiva; conserva candidata para Documento 04, pero exige pruebas externas antes de incorporar.
- `R001-001_Auditoria_Integracion_Table_Checks.md`: auditoria favorable de integracion tecnica local; no admite `H-Xi` ni cierra `P-200` / `P-107`.
- `R001-001_Auditoria_Relacion_Formal_AO.md`: auditoria favorable de `R001-TB-001` como relacion formal local con `AO-001`.
- `R001-001_Auditoria_Cierre_Tecnico.md`: auditoria favorable de cierre tecnico de `R001-001`.
- `TCS-001_Auditoria_Paquete_Minimo.md`: auditoria favorable con limites del paquete minimo provisional de `TCS-001`.
- `TCS-001_Auditoria_Maduracion_Provisional.md`: auditoria favorable de `TCS-MAT-PROV-001`; mantiene TCS abierto y no canonico.
- `AO-001_Auditoria_Puente_Confluencia_Equivalencia.md`: auditoria favorable como avance local, no como cierre global.
- `AO-001_Auditoria_Criterios_Uso_R4_Gamma_Fuera_AUD.md`: auditoria favorable de criterios de uso local controlado.
- `AO-001_Auditoria_Casos_Prueba_Algebra_Operacional.md`: auditoria favorable de `AO-CASE-BAT-001`.
- `AUT-002_Auditoria_Referencias_Historicas_Transferidas.md`: auditoria favorable del tratamiento de referencias historicas transferidas.
- `AUT-002_Auditoria_Cierre_Tecnico.md`: auditoria favorable de cierre tecnico de `AUT-002`.
- `DOCS-001_Auditoria_Consolidacion_Documentos_00-04.md`: auditoria favorable de consolidacion de documentos 00-03 y actualizacion del Documento 04.
- `AUD-001_Auditoria_R4_Gamma_Formal_Local.md`: auditoria favorable de `R4-FORMAL-AUD-001`, `GAMMA-FORMAL-AUD-001` y `VAL-031` como artefactos locales de `AUD-001`.
- `AUD-001_Auditoria_Cierre_Operativo_v0.md`: auditoria favorable de cierre operativo v0 de `AUD-001`.
- `AO-001_Auditoria_Prueba_Gamma_Externa.md`: auditoria favorable de `GAMMA-EXT-AO-001` como prueba externa local de `Gamma_1`.
- `AO-001_Auditoria_Marco_Inicial_Algebra_Operacional.md`: auditoria favorable de `AO-MARCO-001` como marco inicial provisional; su incorporacion documental queda decidida por `D-2026-07-03-011`.
- `AUD-001_Auditoria_Gamma_Ruta1_Definicion_Local.md`: auditoria favorable de `GAMMA-DEF-001` como definicion local provisional de ruta 1; no autoriza promocion formal.
- `RH-001_Auditoria_Procesamiento.md`: auditoria favorable para cerrar el procesamiento de la transcripcion historica; no modifica Canon ni documentos oficiales.
- `RH-002_Auditoria_Procesamiento.md`: auditoria favorable para cerrar el procesamiento del lote historico de Descargas; no modifica Canon ni documentos oficiales.
- `REC-001_Auditoria_Reconciliacion.md`: auditoria favorable para cerrar la reconciliacion inicial de Canon/baselines; no modifica Canon ni documentos oficiales.
- Auditorias `PSI-001`: transferidas fuera del Laboratorio; archivos locales eliminados por `D-2026-07-03-012`.
- `HXI-001_Auditoria_Apertura.md`: auditoria favorable para abrir `HXI-001` como evaluacion separada no admisoria.
- `HXI-001_Auditoria_Mapa_Preliminar.md`: auditoria favorable para aceptar el mapa preliminar `H-Xi` / `R` como guia operativa no admisoria.
- `HXI-001_Auditoria_Matriz_Pruebas.md`: auditoria favorable para aceptar la matriz `HXI-R` como guia operativa no admisoria.
- `HXI-001_Auditoria_Dictamen_Utilidad_Local.md`: auditoria favorable para aceptar el dictamen de utilidad local de `Xi` como guia operativa no admisoria.
- `HXI-001_Auditoria_Notacion_Minima_Xi-R.md`: auditoria favorable para aceptar la notacion minima `Xi-R` como guia operativa no admisoria.
- `HXI-001_Auditoria_Criterios_Admision_Formal.md`: auditoria favorable para aceptar criterios de admision formal posterior como compuerta provisional no admisoria.
- `HXI-001_Auditoria_Reporte_Consistencia.md`: auditoria favorable para aceptar el reporte de consistencia de la notacion minima `Xi-R`.
- `HXI-001_Auditoria_Reapertura_Operativa.md`: auditoria favorable para reabrir `HXI-001` como frente activo inmediato sin admision de `H-Xi`.
- `HXI-001_Auditoria_Compuerta_Admision_Formal.md`: auditoria favorable para aceptar `HXI-GATE-001` con resultado `mantener_Xi_eval`.
- `HXI-001_Auditoria_Mantenimiento_Local.md`: auditoria favorable para mantener `HXI-001` abierto en mantenimiento local.
- `HXI-001_Auditoria_Cierre_Mantenimiento_Local.md`: auditoria favorable para cerrar `HXI-001` en mantenimiento local, sin admitir `H-Xi`.
- `AUT-001_Validacion_DO-STATE-BOARD.md`: validacion provisional favorable del tablero de estado no mutante.
- `AUT-001_Validacion_DO-LAB-CONTINUITY.md`: validacion provisional favorable de la continuidad integrada no mutante.
- `AUT-001_Validacion_DO-LAB-RUN.md`: validacion provisional favorable del comando unico no mutante.
- `AUT-001_Validacion_DO-LAB-RISK.md`: validacion provisional favorable del clasificador de advertencias y riesgos.
- `AUT-001_Validacion_DO-LAB-SUMMARY.md`: validacion provisional favorable del resumen ejecutivo automatico.
- `AUT-001_Validacion_Cierre_Riesgos.md`: validacion provisional favorable de criterios de cierre y riesgos altos.
- `AUT-001_Validacion_Revision_Riesgos_Activos.md`: validacion provisional favorable de la revision de 17 riesgos activos.
- `AUT-001_Validacion_Refinamiento_DO-LAB-RISK.md`: validacion provisional favorable del refinamiento de riesgos controlados.
- `AUT-001_Validacion_Refinamiento_Contexto_Guardrails.md`: validacion favorable del refinamiento de guardrails.
- `AUT-001_Validacion_Cierre_Tecnico_Provisional.md`: validacion provisional favorable del cierre tecnico provisional.
- `AUT-001_Validacion_Cierre_Operativo_Completo.md`: validacion favorable del cierre operativo completo de `AUT-001`.
- `P-PI_Auditoria_Marco_Inicial_Confluencia_Equivalencia.md`: auditoria favorable del marco inicial `PPI-MARCO-CORE-001`; no resuelve Confluencia ni Equivalencia de proyecciones.
- `P-PI_Auditoria_Criterios_Cierre.md`: auditoria favorable de criterios de cierre; no cierra `P-PI.0` ni `P-PI.1`.
- `AUD-001_Auditoria_REPORT_LAYER_Candidata.md`: auditoria favorable de `REPORT-LAYER-CAND-001` como candidata provisional de expediente.
- `AUD-001_Auditoria_Completitud_Auditor_v0.md`: auditoria favorable de completitud documental/operativa v0 del Auditor.
- `AUD-001_Auditoria_SPEC-RFC-AUDITOR-V0_NIVEL-C.md`: auditoria favorable de la candidata tipo RFC contra `NIVEL-C-001`.
- `AUD-001_Auditoria_Criterios_Promocion_R4-CANDIDATA.md`: auditoria favorable de criterios como compuerta provisional; no autoriza promocion formal.
- `AUD-001_Auditoria_Post-No-Automata_R4-CANDIDATA.md`: auditoria favorable para cerrar provisionalmente la primera ronda no automata; no autoriza promocion formal.
- `AUD-001_Auditoria_R4-CANDIDATA.md`: auditoria favorable con deudas no bloqueantes para decision de estatus y bloqueantes para promocion formal.
- `DO-001_Auditoria_DO-PROP-001.md`: `DO-PROP-001` auditada favorablemente como propuesta provisional de expediente; no autoriza automatizacion ejecutable completa.
- `DO-001_Auditoria_SPEC-AUD-001_NIVEL-C.md`: `SPEC-AUD-001_Candidata` auditada favorablemente contra `NIVEL-C-001`; no promueve por si misma a documento oficial.

## Decisiones operativas de prioridad

- `DECISION_Desactivacion_Vision_Papers.md` (`D-2026-07-02-031`): desactiva `VISION_PAPER_PROPUESTA.md` y `VISION_PAPER_FINAL_REFERENCIAS.md` hasta nuevo aviso.
- `DECISION_Siguiente_Frente_Activo_P-PI.md`: elige `P-PI.0` / `P-PI.1` como siguiente frente activo inmediato para definir criterios de cierre.
- `DECISION_Siguiente_Frente_Activo_B-001.5.md`: elige `B-001.5` como siguiente frente activo inmediato para clasificacion.

## Decisiones provisionales de expediente

- `RH-001_Decision_Reconciliacion_PM001.md` (`D-2026-07-06-016`): acepta `RH-PM-REC-001`; `PM-001` queda reconciliado solo como deuda historica condicionada, sin expediente activo ni protocolo materializado.
- `AUT-003_Decision_Herramienta_REPORT_LAYER_C002.md` (`D-2026-07-06-015`): acepta `REPORT-LAYER-C002-GATE-001` como herramienta local no mutante conforme a `C-002`, integrada a `DO-LAB-RUN-001` sin modo mutante.
- `AO-001_Decision_REPORT_LAYER_Nivel_C.md` (`D-2026-07-06-014`): acepta `AO-REPORT-LAYER-NIVEL-C-001`; `REPORT_LAYER` permanece local pre-C y no crea Nivel C nuevo ni `C-003`.
- `MOC-001_Decision_Relacion_Documental_C001_C002.md` (`D-2026-07-06-013`): acepta `MOC-C001-C002-REL-001`; ejecuta `MOC-ROUTE-012` como relacion documental local con `C-001` / `C-002`, sin modificar Nivel C ni promover MOC.
- `HXI-001_Decision_Cierre_Mantenimiento_Local.md` (`D-2026-07-06-012`): cierra `HXI-001` en mantenimiento local; `H-Xi` sigue no admitida y `Xi_eval` queda solo como herramienta local historica/auxiliar.
- `AUD-001_Decision_Cierre_Operativo_v0.md` (`D-2026-07-06-011`): cierra `AUD-001` como expediente completo en version documental/operativa v0; no exporta `REPORT_LAYER`, R4/Gamma ni la suite completa.
- `AUT-002_Decision_Cierre_Tecnico.md` (`D-2026-07-06-010`): cierra tecnicamente `AUT-002`; conserva `referencia_historica_transferida` como regla tecnica.
- `R001-001_Decision_Cierre_Tecnico.md` (`D-2026-07-06-009`): cierra tecnicamente `R001-001`; conserva `R001-TABLE-CHECK-001` y `R001-TB-001` como herramienta/relacion local.
- `MOC-001_Decision_Rutas_Posteriores_Ruta_010.md` (`D-2026-07-06-008`): acepta `MOC-NEXT-ROUTES-010`; fija `MOC-ROUTE-011` como mantenimiento teorico-operativo sin ejecucion.
- `AO-001_Decision_Pruebas_AO-DOC04-WIDE_REPORT_LAYER.md` (`D-2026-07-06-007`): acepta `AO-DOC04-WIDE-TEST-001` y `AO-REPORT-LAYER-BRIDGE-001`; prueba 8/8 casos y precisa `REPORT_LAYER` como entrada de `Pi_rep`.
- `AO-001_Decision_Formalizacion_Amplia_Doc04.md` (`D-2026-07-06-006`): acepta `AO-DOC04-WIDE-001` e incorpora Documento 04 amplio v0 con contratos ejecutables locales, proyecciones, equivalencia local, confluencia local, compuerta operacional y perfiles restringidos R4/Gamma.
- `MOC-001_Decision_Paquete_Registro_Auditoria_Piloto.md` (`D-2026-07-06-005`): acepta `MOC-PILOT-REG-AUDIT-PACK-001`; recomienda `MOC-ROUTE-010`.
- `MOC-001_Decision_Paquete_PreEjecucion_Piloto.md` (`D-2026-07-06-004`): acepta `MOC-PREEXEC-PACK-001`; recomienda `MOC-ROUTE-009`.
- `MOC-001_Decision_Compuerta_Autorizacion_Ejecucion_Piloto.md` (`D-2026-07-06-003`): acepta `MOC-GATE-PILOT-EXEC-001`; no autoriza ejecucion real y recomienda `MOC-ROUTE-008`.
- `MOC-001_Decision_Rutas_Posteriores_Ruta_006.md` (`D-2026-07-06-002`): acepta `MOC-NEXT-ROUTES-006`; recomienda `MOC-ROUTE-007`.
- `MOC-001_Decision_Protocolo_Piloto_Empirico_Futuro.md` (`D-2026-07-06-001`): acepta `MOC-EMP-PILOT-PROTO-001` sin ejecucion real.
- `MOC-001_Decision_Rutas_Posteriores_Ruta_005.md` (`D-2026-07-05-025`): acepta `MOC-NEXT-ROUTES-005`; recomienda `MOC-ROUTE-006`.
- `MOC-001_Decision_Ejecucion_Ruta_005.md` (`D-2026-07-05-024`): acepta `MOC-ROUTE-005` y `MOC-EVAL-PROTO-002`.
- `MOC-001_Decision_Rutas_Posteriores_Ruta_004.md` (`D-2026-07-05-023`): acepta `MOC-NEXT-ROUTES-004`; recomienda `MOC-ROUTE-005`.
- `MOC-001_Decision_Puente_Formal_MOC_AO.md` (`D-2026-07-05-022`): acepta `MOC-AO-BRIDGE-001` como puente formal local entre `MOC-001` y `AO-001`.
- `MOC-001_Decision_Rutas_Posteriores_Ruta_003.md` (`D-2026-07-05-021`): acepta `MOC-NEXT-ROUTES-003`; recomienda `MOC-ROUTE-004`.
- `MOC-001_Decision_Puente_Formal_MOC_TCS.md` (`D-2026-07-05-020`): acepta `MOC-TCS-BRIDGE-001`; formaliza operadores ejecutables locales.
- `MOC-001_Decision_Rutas_Posteriores_Ruta_002.md` (`D-2026-07-05-019`): acepta `MOC-NEXT-ROUTES-002`; recomienda `MOC-ROUTE-003`.
- `MOC-001_Decision_Ejecucion_Ruta_002.md` (`D-2026-07-05-018`): acepta `MOC-ROUTE-002`; bateria ampliada con 11/11 casos, 2 desacuerdos justificados y `risk_blocks_closure: false`.
- `MOC-001_Decision_Disenio_Estudio_Empirico.md` (`D-2026-07-05-015`): acepta `MOC-EMP-STUDY-001`; no ejecuta estudio empirico real ni canoniza el MOC.
- `MOC-001_Decision_Ejecucion_Ruta_Valida_001.md` (`D-2026-07-05-016`): acepta `MOC-ROUTE-EXEC-001`; primera ruta valida ejecutada favorablemente con 7/7 casos y `risk_blocks_closure: false`.
- `MOC-001_Decision_Siguientes_Rutas_Validas.md` (`D-2026-07-05-017`): acepta `MOC-NEXT-ROUTES-001`; recomienda `MOC-ROUTE-002`.
- `MOC-001_Decision_Simulacion_Software.md` (`D-2026-07-05-014`): acepta `MOC-EVAL-001` como simulador no mutante de `MOC-001`.
- `MOC-001_Decision_Metricas_Protocolo.md` (`D-2026-07-05-013`): acepta `MOC-METRIC-STATE-001` y `MOC-EVAL-PROTO-001`.
- `MOC-001_Decision_Formalizacion_Xi_eval.md` (`D-2026-07-05-012`): acepta `MOC-XI-EVAL-FORMAL-001` solo como operador local de evaluacion.
- `MOC-001_Decision_Apertura.md` (`D-2026-07-05-011`): abre `MOC-001` como expediente integrador provisional no canonico, no clinico y no regulado.
- `TCS-001_Decision_Maduracion_Provisional.md` (`D-2026-07-05-010`): acepta `TCS-MAT-PROV-001`; no canoniza `Concordance` ni cierra la maduracion de TCS.
- `AO-001_Decision_Compuerta_Exportacion_R4_Gamma.md` (`D-2026-07-05-009`): bloquea exportacion general de R4/Gamma y acepta solo perfil restringido interoperable.
- `AO-001_Decision_Formalizacion_Acotada_Doc04.md` (`D-2026-07-05-008`): incorpora `Pi_tb` / `Eq_tb` al Documento 04 en grado acotado bajo testigo.
- `AO-001_Decision_Estatus_Pruebas_Externas_Confluencia.md` (`D-2026-07-05-007`): acepta `AO-EXT-CONF-EXEC-001`; ejecuta `EXT-CONF-001` y agrega `EXT-CONF-002` sin cerrar problemas globales.
- `AO-001_Decision_Ruta_Formalizacion_Doc04_Confluencia_Externa.md` (`D-2026-07-05-006`): acepta `AO-DOC04-FORM-CHK-001` y `AO-CONF-EXT-OPTIONS-001`; queda continuada por `D-2026-07-05-007` y por la incorporacion acotada `D-2026-07-05-008`.
- `R001-001_Decision_Integracion_Table_Checks.md` (`D-2026-07-05-004`): acepta `R001-TABLE-CHECK-001` como herramienta local no mutante integrada a `DO-LAB-RUN-001`; no canoniza `Xi`, no admite `H-Xi`, no cierra `P-200` ni resuelve `P-107`.
- `R001-001_Decision_Relacion_Formal_AO.md` (`D-2026-07-05-005`): acepta `R001-TB-001` como relacion formal local entre `R001-TABLE-CHECK-001` y `AO-PPI-BRIDGE-001`; no cierra Equivalencia global ni Confluencia global.
- `HXI-001_Decision_Mantenimiento_Local.md` (`D-2026-07-05-003`): acepta `HXI-MAINT-001`; `HXI-001` queda abierto en mantenimiento local y deja de ser frente activo inmediato.
- `HXI-001_Decision_Resultado_Compuerta_Admision_Formal.md` (`D-2026-07-05-002`): acepta `HXI-GATE-001` con resultado `mantener_Xi_eval`; `H-Xi` permanece no admitida.
- `HXI-001_Decision_Reapertura_Operativa.md` (`D-2026-07-05-001`): reactiva `HXI-001` como frente activo inmediato para aplicar la compuerta de admision formal posterior; no admite `H-Xi`, no canoniza `Xi` y no reabre `PSI-001`.
- `AUT-001_Decision_Refinamiento_Contexto_Guardrails.md` (`D-2026-07-03-020`): acepta `AUT-RISK-REFINE-002` y `AUT-VAL-012`; no reabre `AUT-001`.
- `TCS-001_Decision_Estatus_Paquete_Minimo.md` (`D-2026-07-03-019`): acepta el paquete minimo provisional de `TCS-001`; no canoniza `Concordance`.
- `AO-001_Decision_Estatus_Puente_Confluencia_Equivalencia.md` (`D-2026-07-03-018`): acepta `AO-PPI-BRIDGE-001`, `AO-PPI-EQ-001` y `AO-PPI-CONF-001` como avance local.
- `AO-001_Decision_Criterios_Uso_R4_Gamma_Fuera_AUD.md` (`D-2026-07-03-017`): acepta `AO-R4-GAMMA-USE-001` como criterio local de uso controlado.
- `AO-001_Decision_Estatus_Casos_Prueba_Algebra_Operacional.md` (`D-2026-07-03-016`): acepta `AO-CASE-BAT-001`.
- `AUT-002_Decision_Referencias_Historicas_Transferidas.md` (`D-2026-07-03-015`): acepta `referencia_historica_transferida` y el refinamiento de falsos bloqueos de historial.
- `AO-001_Decision_Estatus_Prueba_Gamma_Externa.md` (`D-2026-07-03-014`): acepta `GAMMA-EXT-AO-001` como prueba positiva externa local de `Gamma_1`.
- `HB-001_Decision_Congelamiento_Brotes_Alternos.md` (`D-2026-07-03-013`): congela `H-B.6` y `H-B.7` como brotes alternos y originales historicos.
- `PSI-TRASPASO-001_Decision_Eliminacion_Copia.md` (`D-2026-07-03-012`): elimina la copia local de traspaso `PSI-001*`.
- `DOCS-001_Decision_Consolidacion_Documentos_00-04.md` (`D-2026-07-03-011`): incorpora documentos 00-03 desde fuentes previas y actualiza el Documento 04 como version inicial consolidada.
- `RH-001_Decision_Cierre.md`: `RH-001` queda cerrado como expediente de procesamiento de registro historico; no autoriza promocion ni reapertura de otros expedientes.
- `RH-002_Decision_Cierre.md`: `RH-002` queda cerrado como expediente de procesamiento del lote historico de Descargas; no autoriza canonizacion, reconciliacion ni apertura automatica de psicologia.
- `REC-001_Decision_Cierre.md`: `REC-001` queda cerrado como reconciliacion inicial de Canon/baselines; reemplaza la deuda amplia por deudas refinadas.
- `P-PI_Decision_Reactivacion_Frente_Matematico.md` (`D-2026-07-02-032`): reactiva `P-PI.0` / `P-PI.1` como frente matematico acotado y acepta `PPI-MARCO-CORE-001` como marco provisional.
- `P-PI_Decision_Ruta_Operativa.md`: decision previa de pausa operativa; superada operativamente por `D-2026-07-02-032` solo para trabajo acotado.
- `P-PI_Decision_Estatus_Criterios_Cierre.md`: acepta criterios de cierre como compuerta provisional de expediente; no cierra `P-PI.0` ni `P-PI.1`.
- `B-001.5_Decision_Clasificacion.md`: clasifica `B-001.5` como expediente congelado por falta de material local suficiente.
- `AUD-001_Decision_Estatus_REPORT_LAYER_Candidata.md` (`D-2026-07-02-026`): acepta `REPORT-LAYER-CAND-001` como candidata provisional de expediente.
- `AUD-001_Decision_Estatus_Auditor_v0.md` (`D-2026-07-02-027`): acepta al Auditor como completo en version documental/operativa v0.
- `AUD-001_Decision_Promocion_SPEC-RFC-AUDITOR-V0.md` (`D-2026-07-02-028`): promueve `SPEC-RFC-AUDITOR-V0` a `C-002_RFC_Operativo_Auditor_v0.md`.
- `AUD-001_Decision_Estatus_Implementacion_No_Mutante_C002.md`: acepta `auditor_v0.py` como implementacion inicial no mutante de `AUDITOR-V0-001`.
- `AUD-001_Decision_Reactivacion_REPORT_LAYER.md` (`D-2026-07-02-025`): reactiva `AUD-001` de forma acotada para separar `REPORT_LAYER`.
- `AUD-001_Origen_REPORT_LAYER.md`: fija el origen local de `REPORT_LAYER` desde `M-000`, `M-001`, `C-001`, contratos de reportes, validaciones, simulaciones y frontera de permiso; no depende de `Gamma` ni de R4 formal.
- `AUD-001_Decision_Reactivacion_JSON_Auditor_v0.md`: reactiva la salida JSON y la carga externa `--case-file` para `AUDITOR-V0-001`.
- `AO-001_Decision_Estatus_Marco_Inicial_Algebra_Operacional.md` (`D-2026-07-03-009`): acepta `AO-MARCO-001` como marco inicial provisional de Algebra Operacional; su incorporacion inicial al Documento 04 queda decidida posteriormente por `D-2026-07-03-011`.
- `AUD-001_Decision_Estatus_R4_Gamma_Formal_Local.md` (`D-2026-07-03-010`): acepta `R4-FORMAL-AUD-001`, `GAMMA-FORMAL-AUD-001` y `VAL-031` como artefactos locales de `AUD-001`; no promueve Canon, Nivel C ni transformacion material.
- `AO-001_Decision_Apertura.md` (`D-2026-07-03-008`): abre `AO-001` como expediente preparatorio del Documento 04; la reserva documental queda superada por `D-2026-07-03-011`.
- `AUD-001_Decision_Estatus_Gamma_Ruta1_Definicion_Local.md` (`D-2026-07-03-007`): acepta `GAMMA-DEF-001` como definicion local provisional de `Gamma` en ruta 1; no construye `Gamma` formal ni autoriza transformaciones.
- `AUD-001_Decision_Pausa_Operativa_R4-CANDIDATA.md`: deja `AUD-001` en pausa operativa; no cierra el expediente ni promueve `R4-CANDIDATA`.
- `AUD-001_Decision_Ruta_Siguiente_R4-CANDIDATA.md`: mantiene `R4-CANDIDATA` como hipotesis operativa robustecida dentro de `AUD-001`; no abre ruta de promocion formal.
- `AUD-001_Decision_Estatus_Criterios_Promocion_R4-CANDIDATA.md`: acepta criterios de promocion como compuerta provisional de expediente; no elige ruta futura.
- `AUD-001_Decision_Siguiente_Fase_R4-CANDIDATA.md`: decide fase de criterios de promocion y frontera formal; no autoriza promocion formal.
- `AUD-001_Decision_Cierre_Ronda_No_Automata_R4-CANDIDATA.md`: cierra provisionalmente la primera ronda no automata de `R4-CANDIDATA`; no autoriza promocion formal.
- `AUD-001_Decision_Auditoria_Post-No-Automata_R4-CANDIDATA.md`: procede una nueva auditoria limitada posterior a la ronda no automata; no autoriza promocion formal.
- `AUD-001_Decision_Capa_Reportes_R4-CANDIDATA.md`: nombres concretos de reportes permanecen locales a `AUD-001`; `R4-CANDIDATA` puede usar una capa abstracta equivalente `REPORT_LAYER`.
- `AUD-001_Decision_Estatus_R4-CANDIDATA.md`: `R4-CANDIDATA` aceptada como hipotesis operativa de expediente dentro de `AUD-001`; no Canon, no documento oficial, no Regla R4 formal.
- `DO-001_Decision_DO-CHECK-REPORT.md`: `DO_CHECK_REPORT` permanece como reporte propio de `DO-001`, con compatibilidad parcial futura con `OPERATOR_REPORT`.
- `DO-001_Decision_Modo_Operativo_Auditor.md`: `MODO-AUD-001` define al Auditor como modo mixto, ejecutable para calculo y reporte, asistido para autoridad y permiso.
- `DO-001_Decision_Alcance_SPEC-AUD-001.md`: `ALC-SPEC-AUD-001` define que parte de `DO-001` pasa a `SPEC-AUD-001_Candidata`.
- `DO-001_Decision_Promocion_SPEC-AUD-001.md`: `PROM-SPEC-AUD-001` promueve la candidata a `02_Documentos/C-001_Especificacion_Tecnica_Auditor.md`.
- `DO-001_Decision_Cierre_DO-001.md`: `CIERRE-DO-001` cierra el expediente de diseno de automatizacion.
- `AUT-001_Decision_Estatus_MVP.md`: acepta `DO-CHECK-MIN-001` como automatizacion minima provisional, sin cerrar `AUT-001`.
- Decisiones iniciales `PSI-001`: conservadas solo como historia agregada; los archivos locales fueron eliminados por `D-2026-07-03-012`.
- `HXI-001_Decision_Apertura.md`: abre `HXI-001` como evaluacion separada de `H-Xi` frente a relaciones `R`; no admite `H-Xi`.
- `HXI-001_Decision_Estatus_Mapa_Preliminar.md`: acepta el mapa preliminar `H-Xi` / `R` como guia operativa de evaluacion; no admite `H-Xi`.
- `HXI-001_Decision_Estatus_Matriz_Pruebas.md`: acepta la matriz `HXI-R` como guia operativa de evaluacion; no admite `H-Xi`.
- `HXI-001_Decision_Estatus_Dictamen_Utilidad_Local.md`: acepta el dictamen de utilidad local de `Xi` como guia operativa de evaluacion; no admite `H-Xi`.
- `HXI-001_Decision_Ruta_Operativa.md`: elige continuidad acotada con notacion minima; no admite `H-Xi`.
- `HXI-001_Decision_Estatus_Notacion_Minima_Xi-R.md`: acepta la notacion minima `Xi-R` como guia operativa de evaluacion; no admite `H-Xi`.
- `HXI-001_Decision_Preparacion_Admision_Formal.md`: prepara ruta 3 de admision formal posterior de forma condicionada; no admite `H-Xi`.
- `HXI-001_Decision_Estatus_Criterios_Admision_Formal.md`: acepta criterios de admision formal posterior como compuerta provisional; no admite `H-Xi`.
- `HXI-001_Decision_Estatus_Reporte_Consistencia.md`: acepta el reporte de consistencia de `Xi_eval`; no admite `H-Xi`.
- `HXI-001_Decision_Pausa_Operativa.md`: pausa operativa historica de `HXI-001`, superada como estado vigente por `D-2026-07-05-001`; no admite `H-Xi`.
- `HXI-001_Decision_Reapertura_Operativa.md`: reabre `HXI-001` operativamente como frente activo inmediato; no admite `H-Xi`.
- `HXI-001_Decision_Resultado_Compuerta_Admision_Formal.md`: aplica la compuerta con resultado `mantener_Xi_eval`; no admite `H-Xi`.
- `HXI-001_Decision_Mantenimiento_Local.md`: mantiene `HXI-001` abierto en mantenimiento local; no admite `H-Xi`.
- `AUT-001_Decision_Reactivacion_Automatizacion.md`: reactiva `AUT-001` como frente activo inmediato.
- `AUT-001_Decision_Tablero_Estado.md`: acepta `DO-STATE-BOARD-001` como tablero de estado provisional.
- `AUT-001_Decision_Continuidad_Laboratorio.md`: acepta `DO-LAB-CONTINUITY-001` como continuidad integrada provisional.
- `AUT-001_Decision_Comando_Unico_LAB.md`: acepta `DO-LAB-RUN-001` como comando unico provisional.
- `AUT-001_Decision_Riesgos_Advertencias.md`: acepta `DO-LAB-RISK-001` como clasificador provisional de advertencias y riesgos.
- `AUT-001_Decision_Resumen_Ejecutivo.md`: acepta `DO-LAB-SUMMARY-001` como resumen ejecutivo automatico provisional.
- `AUT-001_Decision_Cierre_Riesgos.md`: acepta criterios de cierre de fase media y tratamiento inicial de riesgos altos.
- `AUT-001_Decision_Revision_Riesgos_Activos.md` (`D-2026-07-02-019`): acepta la revision provisional de 17 riesgos activos sin cerrar `AUT-001`.
- `AUT-001_Decision_Refinamiento_DO-LAB-RISK.md` (`D-2026-07-02-020`): acepta `AUT-RISK-REFINE-001`; `riesgo_activo` baja a 0 y `advertencia_controlada` queda en 17.
- `AUT-001_Decision_Cierre_Tecnico_Provisional.md` (`D-2026-07-02-021`): acepta cierre tecnico provisional sin cierre operativo completo.
- `AUT-001_Decision_Cierre_Operativo_Completo.md` (`D-2026-07-02-029`): cierra operativamente `AUT-001`.
- `HB-001_Decision_Fichas_Alcance_H-B.md` (`D-2026-07-02-030`): acepta alcance local minimo de `H-B.6` y `H-B.7`; queda historicamente superada por el congelamiento de `D-2026-07-03-013`.
- Decisiones `PSI-001` de continuidad, frontera e independizacion: conservadas solo en `DECISIONES.md`; copia local eliminada por `D-2026-07-03-012`.
- `AUT-001_Decision_Fase_Media.md`: acepta `DO-CHECK-MED-001` como automatizacion media provisional, sin cerrar `AUT-001`.

## Mapas preliminares de expediente

- `HXI-001_Mapa_Preliminar_PSI-R.md`: mapa preliminar operativo no admisorio entre `H-Xi`, relaciones `R` y ejemplos PSI ahora historicos; aceptado para guiar pruebas sin reactivar `PSI-001`.

## Ejemplos conceptuales de expediente

- No hay ejemplos ni matrices PSI activas dentro del Laboratorio; la copia local fue eliminada.
- `TCS-001_Teoria_Concordante_de_Sistemas.md`: propuesta teorica inicial para `Concordance Theory`.
- `TCS-001_Analisis_Fondo.md`: analisis provisional de fondo; identifica tensiones, supuestos ocultos, deudas conceptuales, fallos de concordancia y condiciones candidatas.

## Matrices provisionales de expediente

- `HXI-001_Matriz_Pruebas_HXI-R.md`: matriz provisional operativa historicamente apoyada en ejemplos PSI transferidos; aceptada para preparar dictamen de utilidad local de `Xi`, sin admision de `H-Xi`.

## Dictamenes provisionales de expediente

- `HXI-001_Dictamen_Utilidad_Local_Xi.md`: dictamen provisional operativo; reconoce utilidad local acotada de `Xi` en reorganizacion relacional estable, sin admision de `H-Xi`.

## Rutas operativas de expediente

- `HXI-001_Decision_Ruta_Operativa.md`: ruta 2 elegida, continuidad acotada con notacion minima.

## Notaciones provisionales de expediente

- `HXI-001_Notacion_Minima_Xi-R.md`: notacion provisional operativa para aplicar `Xi_eval(R0, R1)` a la matriz `HXI-R`, sin admision de `H-Xi`.

## Criterios de admision formal de expediente

- `HXI-001_Criterios_Admision_Formal_H-Xi.md`: compuerta provisional para admision formal posterior de `H-Xi`; no admite `H-Xi` y exige reporte de consistencia previo.

## Reportes de consistencia de expediente

- `HXI-001_Reporte_Consistencia_Notacion_Xi-R.md`: reporte favorable de aplicacion de `Xi_eval(R0, R1)` a `HXI-R-001` a `HXI-R-005`; cumple requisito previo sin admitir `H-Xi`.

## Reaperturas operativas de expediente

- `HXI-001_Reapertura_Operativa.md`: `HXI-REOPEN-001`, reapertura controlada de `HXI-001` para aplicar la compuerta de admision formal posterior sin admision automatica, sin canonizacion de `Xi` y sin reabrir `PSI-001`.

## Compuertas aplicadas de expediente

- `HXI-001_Evaluacion_Compuerta_Admision_Formal.md`: `HXI-GATE-001`, compuerta aplicada con resultado `mantener_Xi_eval`; conserva `Xi_eval` como herramienta local y mantiene `H-Xi` como hipotesis externa no admitida.

## Mantenimientos locales de expediente

- `HXI-001_Mantenimiento_Local.md`: `HXI-MAINT-001`, regimen de mantenimiento local; conserva `Xi_eval` y trazabilidad de `H-Xi`, sin frente activo de admision.

## Tableros de automatizacion

- `06_Automatizacion/lab_status_board.py`: tablero no mutante `DO-STATE-BOARD-001`.
- `06_Automatizacion/reportes/lab_status_board.md`: reporte Markdown conservado.
- `06_Automatizacion/reportes/lab_status_board.json`: reporte JSON conservado.


- `EX-PSI-001` a `EX-PSI-005`: antecedentes historicos transferidos; sin archivo local activo tras `D-2026-07-03-012`.

## Criterios de evaluacion de expediente

- `HXI-001_Criterios_Evaluacion.md`: compuertas para evaluar relacion local `H-Xi` / `R`; no admite `H-Xi`.

## Criterios provisionales de expediente

- No hay criterio PSI activo dentro del Laboratorio.

## Definiciones provisionales de expediente

- `GAMMA-DEF-001`: definicion local provisional de `Gamma` en ruta 1 dentro de `AUD-001`, segun `03_Expedientes/AUD-001_Gamma_Ruta1_Definicion_Local.md`; no es Canon, teorema, Nivel C ni Regla R4 formal.

## Construcciones formales locales de expediente

- `R4-FORMAL-AUD-001`: Regla R4 formal local en `03_Expedientes/AUD-001_R4_Formal_Local.md`; vigente solo dentro de `AUD-001`.
- `GAMMA-FORMAL-AUD-001`: operador formal local de `Gamma` en `03_Expedientes/AUD-001_Gamma_Formal_Local.md`; vigente solo dentro de `AUD-001`.

## Relaciones provisionales de expediente

- `REL-GAMMA-R4-001`: relacion provisional entre `Gamma_1`, `R4-CANDIDATA` y R4 formal en `03_Expedientes/AUD-001_Relacion_Gamma_Ruta1_R4_Formal.md`; no promueve R4 formal.

## Reglas provisionales activas

- `DO-001_Regla_Permiso_Actualizacion.md`: `PERMISO-ACT-001` define quien puede convertir una recomendacion o propuesta en cambio ejecutado; validado inicialmente contra tres casos locales.
- `NIVEL-C-001`: definicion local de `Nivel C - Especificaciones` en `05_Estado_Proyecto/NIVEL_C_ESPECIFICACIONES.md`.

## Validaciones provisionales activas

- `GAMMA-EXT-AO-001`: prueba positiva externa local de `Gamma_1` bajo `AO-001`; produce `G_AO_OP-GOV-001` como criterio formal local de expediente.
- `PPI-CONF-001`: confluencia local de continuidad operativa validada provisionalmente bajo contexto `C_PPI_CONTINUIDAD_OPERATIVA`.
- `PPI-EQ-002`: equivalencia documental-operativa entre completitud v0 del Auditor y `C-002` validada provisionalmente bajo contexto `C_AUD_RFC_OPERATIVO`.
- `VAL-001`: `MP_FAIL_REPORT` validado provisionalmente contra `AUD-SIM-001`.
- `VAL-002`: `CR_FAIL_REPORT` validado provisionalmente contra `AUD-SIM-002`.
- `VAL-003`: `TAU_REPORT` validado provisionalmente contra `AUD-SIM-003`.
- `VAL-004`: `D_REPORT` validado provisionalmente contra `AUD-SIM-004`.
- `VAL-005`: `TR_PROPOSAL_REPORT` validado provisionalmente contra `AUD-SIM-005`.
- `VAL-006`: `TR_EXECUTION_REPORT` validado provisionalmente contra `AUD-SIM-006`.
- `VAL-007`: `TR_EXECUTION_FAIL_REPORT` validado provisionalmente contra `AUD-SIM-007`.
- `VAL-008`: `REVERSAL_REPORT` validado provisionalmente contra `AUD-SIM-008`.
- `VAL-009`: `MP_FAIL_REPORT` validado provisionalmente contra `AUD-SIM-009`.
- `VAL-010`: `CR_FAIL_REPORT` validado provisionalmente contra `AUD-SIM-010`.
- `VAL-011`: `TAU_REPORT` validado provisionalmente contra `AUD-SIM-011`.
- `VAL-012`: `D_REPORT` validado provisionalmente contra `AUD-SIM-012`.
- `VAL-013`: `TR_PROPOSAL_REPORT` validado provisionalmente contra `AUD-SIM-013`.
- `VAL-014`: `TR_EXECUTION_REPORT` validado provisionalmente contra `AUD-SIM-014`.
- `VAL-015`: `TR_EXECUTION_FAIL_REPORT` validado provisionalmente contra `AUD-SIM-015`.
- `VAL-016`: `REVERSAL_REPORT` validado provisionalmente contra `AUD-SIM-016`.
- `VAL-017`: `R4-CANDIDATA` validada provisionalmente contra `AUD-SIM-017`.
- `VAL-018`: `R4-CANDIDATA` validada provisionalmente contra `AUD-SIM-018` usando `REPORT_LAYER`.
- `VAL-019`: `R4-CANDIDATA` validada provisionalmente contra `AUD-SIM-019` usando Registro Historico como caso de autoridad directa.
- `VAL-020`: `R4-CANDIDATA` validada provisionalmente contra `AUD-SIM-020` usando algoritmo textual sin condicion de parada.
- `VAL-021`: `R4-CANDIDATA` validada provisionalmente contra `AUD-SIM-021` usando documento oficial incompleto.
- `VAL-022`: `REPORT-LAYER-CAND-001` validada provisionalmente contra `AUD-SIM-022`.
- `VAL-023`: control positivo `AUD-T00` validado provisionalmente contra `AUD-SIM-023`.
- `VAL-024`: transformacion sin decision `AUD-T05` validada provisionalmente contra `AUD-SIM-024`.
- `VAL-025`: uso formal indebido de `Gamma` validado provisionalmente contra `AUD-SIM-025`; vigente con lectura posterior de `GAMMA-DEF-001` para bloquear usos de estatus excesivo.
- `VAL-026`: separacion de niveles `AUD-T08` validada provisionalmente contra `AUD-SIM-026`.
- `VAL-027`: termino nuevo sin estatus `AUD-T09` validado provisionalmente contra `AUD-SIM-027`.
- `VAL-028`: puente `REPORT_LAYER` / `DO_CHECK_REPORT` validado provisionalmente contra `AUD-SIM-028`.
- `VAL-029`: proyeccion a documento tipo RFC validada provisionalmente contra `AUD-SIM-029`.
- `VAL-030`: aplicacion positiva de `Gamma_1` validada provisionalmente contra `AUD-SIM-030`; no construye `Gamma` formal ni R4 formal.
- `VAL-031`: segunda prueba positiva de `Gamma_1` validada provisionalmente contra `AUD-SIM-031`, usando `REPORT_LAYER` / `DO_CHECK_REPORT`.
- `AUD-001_Validacion_Implementacion_No_Mutante_C002.md`: validacion ejecutada de la implementacion no mutante `AUDITOR-V0-001` y del fixture documental parcial.
- `DO-VAL-001`: `DO_CHECK_REPORT` validado provisionalmente contra `DO-001.md`.
- `DO-VAL-002`: `DO_CHECK_REPORT` validado provisionalmente contra `AUD-001_Casos_Prueba_Auditor.md`.
- `DO-VAL-003`: `DO_CHECK_REPORT` validado provisionalmente contra `CURRENT_STATE.md`.
- `PERM-VAL-001`: `PERMISO-ACT-001` validado provisionalmente contra actualizacion autorizada de estado operativo.
- `PERM-VAL-002`: `PERMISO-ACT-001` validado provisionalmente contra recomendacion sin autorizacion.
- `PERM-VAL-003`: `PERMISO-ACT-001` validado provisionalmente contra cambio de nivel superior o expediente cerrado con permiso insuficiente.
- `MODO-VAL-001` a `MODO-VAL-004`: `MODO-AUD-001` validado provisionalmente contra lectura no mutante, recomendacion sin autorizacion, ejecucion acotada autorizada y cambio de nivel superior.
- `SPEC-VAL-001` a `SPEC-VAL-004`: `SPEC-AUD-001_Candidata` validada provisionalmente como alcance tecnico exportable sin promocion oficial.
- `NIVEL-C-VAL-001` a `NIVEL-C-VAL-004`: `NIVEL-C-001` validado provisionalmente como definicion local de especificaciones.
- `AUT-VAL-001`: `DO-CHECK-MIN-001` validado provisionalmente contra archivos clave y barrido completo, con salvedad de ejecucion directa bloqueada por el entorno.
- `AUT-VAL-002`: `DO-CHECK-MED-001` validado provisionalmente contra archivos clave y barrido completo, con salvedad de ejecucion directa bloqueada por el entorno.
- `AUT-VAL-003`: `DO-LAB-CONTINUITY-001` validado provisionalmente como integracion no mutante; salvedad de ejecucion directa resuelta por `AUT-VAL-011`.
- `AUT-VAL-004`: `DO-LAB-RUN-001` validado provisionalmente como comando unico no mutante; salvedad de ejecucion directa resuelta por `AUT-VAL-011`.
- `AUT-VAL-005`: `DO-LAB-RISK-001` validado provisionalmente como clasificador no mutante; salvedad de ejecucion directa resuelta por `AUT-VAL-011`.
- `AUT-VAL-006`: `DO-LAB-SUMMARY-001` validado provisionalmente como resumen ejecutivo automatico; salvedad de ejecucion directa resuelta por `AUT-VAL-011`.
- `AUT-VAL-007`: criterios de cierre y tratamiento de riesgos altos validados provisionalmente como compuerta no mutante.
- `AUT-VAL-008`: revision de 17 riesgos activos validada provisionalmente como capa no mutante de tratamiento.
- `AUT-VAL-009`: refinamiento contextual de `DO-LAB-RISK-001` validado provisionalmente; 0 riesgos activos y 17 advertencias controladas.
- `AUT-VAL-010`: cierre tecnico provisional de `AUT-001` validado provisionalmente.
- `AUT-VAL-011`: cierre operativo completo de `AUT-001` validado favorablemente con ejecucion directa local.
- `PPI-EQ-001`: equivalencia minima `REPORT_LAYER` / `DO_CHECK_REPORT` validada provisionalmente bajo contexto `C_AUD_LECTURA_MIN`.

## Sintesis provisionales activas

- `MOC-001.md`: expediente integrador del Modelo Operativo de Concordancia, abierto como frente no canonico, no clinico y no regulado.
- `MOC-001_Formalizacion_Xi_eval.md`: formalizacion local de `Xi_eval` para `MOC-001`.
- `MOC-001_Metricas_Estados.md`: estados `concordancia_local`, `concordancia_parcial`, `friccion_operativa`, `discordancia_global`, `bloqueo_de_concordancia` y `no_comparable`.
- `MOC-001_Protocolo_Evaluacion.md`: protocolo de evaluadores independientes con coincidencia exacta, coincidencia parcial y desacuerdo justificado.
- `MOC-001_Casos_No_Clinicos.md`: bateria sintetica no clinica usada por `MOC-EVAL-001`.
- `MOC-001_Disenio_Estudio_Empirico.md`: diseno documental de comparacion futura con baselines.
- `MOC-001_Ejecucion_Ruta_Valida_001.md`: ejecucion local favorable de primera ruta valida.
- `MOC-001_Siguientes_Rutas_Validas.md`: siguientes rutas validas; `MOC-ROUTE-002` queda como recomendada.
- `MOC-001_Ejecucion_Ruta_002.md`: ejecucion local favorable de bateria ampliada con desacuerdos justificados y casos limite.
- `MOC-001_Rutas_Posteriores_Ruta_002.md`: siguientes rutas validas posteriores; `MOC-ROUTE-003` queda como recomendada.
- `MOC-001_Puente_Formal_MOC_TCS.md`: puente formal `MOC/TCS`; define operadores ejecutables locales con prioridad, conflicto, salida unica y traza auditable.
- `MOC-001_Rutas_Posteriores_Ruta_003.md`: siguientes rutas validas posteriores; `MOC-ROUTE-004` queda como recomendada.
- `MOC-001_Puente_Formal_MOC_AO.md`: puente formal `MOC/AO`; usa `operator_trace` como evidencia local de regla ganadora y emite `ao_bridge` para roles operacionales acotados.
- `MOC-001_Rutas_Posteriores_Ruta_004.md`: siguientes rutas validas posteriores; `MOC-ROUTE-005` queda como recomendada.
- `MOC-001_Protocolo_Evaluacion_v0_2.md`: protocolo v0.2; agrega ejes de desacuerdo, regla de desempate, tratamiento y revision si el desacuerdo se repite.
- `MOC-001_Ejecucion_Ruta_005.md`: ejecucion favorable de ruta 005 con 11 casos aprobados, 0 fallos y 2 revisiones si se repite desacuerdo.
- `MOC-001_Rutas_Posteriores_Ruta_005.md`: siguientes rutas validas posteriores; `MOC-ROUTE-006` queda como recomendada.
- `MOC-001_Protocolo_Piloto_Empirico_Futuro.md`: protocolo documental de piloto empirico futuro; define compuerta, tareas candidatas, baselines y prohibiciones sin ejecutar el piloto.
- `MOC-001_Rutas_Posteriores_Ruta_006.md`: siguientes rutas validas posteriores; `MOC-ROUTE-007` queda como recomendada.
- `MOC-001_Compuerta_Autorizacion_Ejecucion_Piloto.md`: compuerta aplicada; `piloto_autorizado = false` y siguiente ruta recomendada `MOC-ROUTE-008`.
- `MOC-001_Semantica_Provisional.md`: propuesta semantica provisional local para objetos, prioridad y salida MOC.
- `MOC-001_Tabla_Operaciones_Formales.md`: tabla formal de operaciones locales del MOC.
- `MOC-001_Casos_Congelados_Piloto.md`: paquete congelado documental de 11 casos sinteticos.
- `MOC-001_Plantilla_Respuesta_Evaluadores.md`: plantilla de respuesta sin datos personales.
- `MOC-001_Reglas_Protocolo_Congelados.md`: version congelada de reglas/protocolo.
- `MOC-001_Paquete_PreEjecucion_Piloto.md`: paquete pre-ejecucion; `MOC-ROUTE-009` queda como recomendada.
- `MOC-001_Metodo_Registro_Sin_Datos_Personales.md`: metodo documental para registrar respuestas sin datos personales ni metadatos identificables.
- `MOC-001_Matriz_Auditoria_Piloto.md`: matriz documental de auditoria con bloqueo por datos personales, caso real, perdida de trazabilidad o uso clinico.
- `MOC-001_Paquete_Registro_Auditoria_Piloto.md`: paquete de ruta 009; `MOC-ROUTE-010` queda como recomendada.
- `AUD-001_Gamma_Ruta1_Definicion_Local.md`: definicion local provisional `GAMMA-DEF-001` para usar `Gamma_1(E, C) = G` solo como salida acotada dentro de `AUD-001`.
- `AUD-001_Relacion_Gamma_Ruta1_R4_Formal.md`: relacion provisional `REL-GAMMA-R4-001` que separa evidencia `R4-CANDIDATA`, generalizacion `Gamma_1` y deuda de R4 formal.
- `AUD-001_R4_Formal_Local.md`: construccion formal local `R4-FORMAL-AUD-001`.
- `AUD-001_Gamma_Formal_Local.md`: construccion formal local `GAMMA-FORMAL-AUD-001`.
- `AO-001_Prueba_Gamma_Externa.md`: prueba externa local `GAMMA-EXT-AO-001` y criterio `G_AO_OP-GOV-001`.
- `AO-001_Casos_Prueba_Algebra_Operacional.md`: bateria local `AO-CASE-BAT-001`.
- `AO-001_Criterios_Uso_R4_Gamma_Fuera_AUD.md`: criterio local `AO-R4-GAMMA-USE-001`.
- `AO-001_Puente_Confluencia_Equivalencia.md`: puente local `AO-PPI-BRIDGE-001`.
- `AO-001_Evaluacion_Formalizacion_Doc04_R001_TB.md`: ruta candidata `AO-DOC04-FORM-CHK-001` para formalizacion futura de `Pi_tb` / `Eq_tb`.
- `AO-001_Opciones_Prueba_Confluencia_Externa.md`: opciones `AO-CONF-EXT-OPTIONS-001`; `EXT-CONF-001` queda ejecutada despues por `AO-EXT-CONF-EXEC-001`.
- `AO-001_Pruebas_Externas_Confluencia.md`: validacion ejecutada `AO-EXT-CONF-EXEC-001`, con `EXT-CONF-001` y `EXT-CONF-002`.
- `AO-001_Formalizacion_Acotada_Doc04_R001_TB.md`: incorporacion acotada `AO-DOC04-FORM-001` de `Pi_tb` / `Eq_tb` al Documento 04.
- `AO-001_Compuerta_Exportacion_R4_Gamma.md`: compuerta `AO-R4-GAMMA-EXPORT-GATE-001`; exportacion general bloqueada y perfil restringido interoperable conservado.
- `AO-001_Formalizacion_Amplia_Doc04.md`: formalizacion amplia v0 `AO-DOC04-WIDE-001` incorporada al Documento 04 por `D-2026-07-06-006`.
- `TCS-001_Definiciones_Minimas.md`, `TCS-001_Tipologia_Fallos_Concordancia.md` y `TCS-001_Casos_Prueba.md`: paquete teorico minimo provisional.
- `TCS-001_Maduracion_Provisional.md`: maduracion provisional `TCS-MAT-PROV-001` con metrica cualitativa, casos externos no regulados y conflicto de autoridades.
- `P-PI_PPI-CONF-001_Rutas_Estado_Operativo.md`: caso ejecutado provisional de Confluencia local.
- `P-PI_PPI-EQ-002_Completitud_A_C002.md`: caso ejecutado provisional de Equivalencia de proyecciones hacia `C-002`.
- `P-PI_PPI-EQ-001_REPORT_LAYER_DO_CHECK.md`: caso ejecutado provisional de Equivalencia de proyecciones.
- `P-PI_Marco_Inicial_Confluencia_Equivalencia.md`: marco provisional `PPI-MARCO-CORE-001` para Equivalencia de proyecciones y Confluencia.
- `P-PI_Criterios_Cierre.md`: criterios provisionales auditados y aceptados como compuerta para cerrar, pausar, congelar, absorber o mantener abiertos `P-PI.0` y `P-PI.1`; aplicada inicialmente en `P-PI_Decision_Ruta_Operativa.md`.
- `AUD-001_REPORT_LAYER_Candidata.md`: `REPORT-LAYER-CAND-001`, candidata provisional para capa abstracta de reportes dentro de `AUD-001`.
- `AUD-001_Criterios_Completitud_Auditor.md`: compuertas de completitud documental/operativa v0 del Auditor.
- `AUD-001_Sintesis_Completitud_Auditor_v0.md`: sintesis de cobertura v0 del Auditor.
- `AUD-001_Invariantes_R4-AUD.md`: invariantes comunes de `R4-AUD` extraidos de `AUD-SIM-001` a `AUD-SIM-016`.
- `AUD-001_R4-CANDIDATA.md`: hipotesis operativa de expediente basada en los invariantes de `R4-AUD`.
- `AUD-001_Criterios_Promocion_R4-CANDIDATA.md`: compuerta provisional aceptada para rutas futuras de estatus y promocion.
- `AUD-001_Sintesis_Cobertura_No_Automata_R4-CANDIDATA.md`: primera ronda no automata sintetizada para decidir auditoria posterior.
- `HB-001_Ficha_Alcance_H-B.6.md`: ficha historica congelada para `H-B.6`.
- `HB-001_Ficha_Alcance_H-B.7.md`: ficha historica congelada para `H-B.7`.

## Ultima decision arquitectonica

`C-002_RFC_Operativo_Auditor_v0.md` promovido como RFC operativo oficial del Auditor v0; complementa `C-001`.

## Ultima decision operativa

`AO-001_Decision_Pruebas_AO-DOC04-WIDE_REPORT_LAYER.md` (`D-2026-07-06-007`): se acepta `AO-DOC04-WIDE-TEST-001` y `AO-REPORT-LAYER-BRIDGE-001`; `AO-DOC04-WIDE-001` queda probado localmente con 8/8 casos, `REPORT_LAYER` queda precisado como entrada de `Pi_rep(REPORT_LAYER, C, W) -> R_rep | B`, y no se promueve `REPORT_LAYER` a Nivel C ni se autorizan transformaciones.
`AO-001_Decision_Formalizacion_Amplia_Doc04.md` (`D-2026-07-06-006`): se acepta `AO-DOC04-WIDE-001`; Documento 04 queda actualizado a version amplia v0 con contratos ejecutables locales, `operator_trace`, proyecciones, equivalencia local, confluencia local, compuerta operacional y perfiles restringidos R4/Gamma; no cierra problemas globales ni crea Nivel C.
`MOC-001_Decision_Paquete_Registro_Auditoria_Piloto.md` (`D-2026-07-06-005`): se acepta `MOC-PILOT-REG-AUDIT-PACK-001`; quedan preparados metodo de registro sin datos personales y matriz de auditoria. La siguiente ruta recomendada es `MOC-ROUTE-010`, decidir rutas posteriores sin reclutamiento ni ejecucion.
`MOC-001_Decision_Paquete_PreEjecucion_Piloto.md` (`D-2026-07-06-004`): se acepta `MOC-PREEXEC-PACK-001`; quedan preparados semantica provisional, tabla de operaciones, casos congelados, plantilla y reglas/protocolo congelados. La siguiente ruta recomendada es `MOC-ROUTE-009`, metodo de registro sin datos personales y matriz de auditoria.
`MOC-001_Decision_Compuerta_Autorizacion_Ejecucion_Piloto.md` (`D-2026-07-06-003`): se acepta `MOC-GATE-PILOT-EXEC-001`; la ejecucion real del piloto no queda autorizada y la siguiente ruta recomendada es `MOC-ROUTE-008`, preparar paquete documental pre-ejecucion sin reclutamiento ni ejecucion.
`MOC-001_Decision_Rutas_Posteriores_Ruta_006.md` (`D-2026-07-06-002`): se acepta `MOC-NEXT-ROUTES-006`; la siguiente ruta recomendada es `MOC-ROUTE-007`, decidir compuerta de autorizacion o no autorizacion del piloto futuro sin ejecutarlo.
`MOC-001_Decision_Protocolo_Piloto_Empirico_Futuro.md` (`D-2026-07-06-001`): se acepta `MOC-EMP-PILOT-PROTO-001` como protocolo documental preparado para piloto empirico futuro, sin ejecucion real.
`MOC-001_Decision_Rutas_Posteriores_Ruta_005.md` (`D-2026-07-05-025`): se acepta `MOC-NEXT-ROUTES-005`; la siguiente ruta recomendada es `MOC-ROUTE-006`, preparar protocolo documental de piloto empirico futuro sin ejecucion real.
`MOC-001_Decision_Ejecucion_Ruta_005.md` (`D-2026-07-05-024`): se acepta `MOC-ROUTE-005`; `MOC-EVAL-PROTO-002` refina el protocolo de evaluadores con ejes de desacuerdo, regla de desempate y tratamiento por traza.
`MOC-001_Decision_Rutas_Posteriores_Ruta_004.md` (`D-2026-07-05-023`): se acepta `MOC-NEXT-ROUTES-004`; la siguiente ruta recomendada es `MOC-ROUTE-005`, refinar protocolo de evaluadores usando `operator_trace`, `Pi_moc_trace` y `ao_bridge`.
`MOC-001_Decision_Puente_Formal_MOC_AO.md` (`D-2026-07-05-022`): se acepta `MOC-AO-BRIDGE-001`; `MOC-ROUTE-004` queda como formalizacion local del puente `MOC/AO` con `operator_trace` como evidencia de regla ganadora y `ao_bridge` como proyeccion acotada hacia AO.
`MOC-001_Decision_Rutas_Posteriores_Ruta_003.md` (`D-2026-07-05-021`): se acepta `MOC-NEXT-ROUTES-003`; la siguiente ruta recomendada es `MOC-ROUTE-004`, formalizar puente `MOC/AO` usando `operator_trace` como evidencia local de regla ganadora.
`MOC-001_Decision_Puente_Formal_MOC_TCS.md` (`D-2026-07-05-020`): se acepta `MOC-TCS-BRIDGE-001`; `MOC-ROUTE-003` queda como formalizacion ejecutable local con `OP_MOC_XI`, `OP_MOC_TCS`, `OP_MOC_STATE` y `OP_MOC_AGREEMENT`.
`MOC-001_Decision_Rutas_Posteriores_Ruta_002.md` (`D-2026-07-05-019`): se acepta `MOC-NEXT-ROUTES-002`; la siguiente ruta recomendada es `MOC-ROUTE-003`, formalizar puente `MOC/TCS` a partir de la bateria ampliada.
`MOC-001_Decision_Ejecucion_Ruta_002.md` (`D-2026-07-05-018`): se acepta `MOC-ROUTE-002`; `MOC-EVAL-001` queda con 11 casos aprobados, 0 fallos, 6 coincidencias exactas, 3 parciales y 2 desacuerdos justificados.
`MOC-001_Decision_Siguientes_Rutas_Validas.md` (`D-2026-07-05-017`): se acepta `MOC-NEXT-ROUTES-001`; la siguiente ruta recomendada es `MOC-ROUTE-002`, ampliar bateria sintetica no clinica con desacuerdos justificados y casos limite.
`MOC-001_Decision_Ejecucion_Ruta_Valida_001.md` (`D-2026-07-05-016`): se acepta `MOC-ROUTE-EXEC-001`; primera ruta valida ejecutada favorablemente con `MOC-EVAL-001`, 7 casos aprobados, 0 fallos y `risk_blocks_closure: false`.
`MOC-001_Decision_Disenio_Estudio_Empirico.md` (`D-2026-07-05-015`): se acepta `MOC-EMP-STUDY-001`; el MOC queda avanzado con diseno empirico futuro, sin ejecucion real, sin personas reales, sin dominio clinico y sin canonizacion.
`MOC-001_Decision_Simulacion_Software.md` (`D-2026-07-05-014`): se acepta `MOC-EVAL-001` como simulador no mutante de casos sinteticos no clinicos.
`MOC-001_Decision_Metricas_Protocolo.md` (`D-2026-07-05-013`): se aceptan metricas ordinales cualitativas y protocolo reproducible provisional.
`MOC-001_Decision_Formalizacion_Xi_eval.md` (`D-2026-07-05-012`): se acepta `Xi_eval` solo como operador local de `MOC-001`, sin admision de `H-Xi`.
`MOC-001_Decision_Apertura.md` (`D-2026-07-05-011`): se abre `MOC-001` como expediente integrador provisional.
`TCS-001_Decision_Maduracion_Provisional.md` (`D-2026-07-05-010`): se acepta `TCS-MAT-PROV-001`; TCS gana metrica cualitativa, casos externos no regulados y conflicto de autoridades, sin canonizacion.
`AO-001_Decision_Compuerta_Exportacion_R4_Gamma.md` (`D-2026-07-05-009`): se acepta `AO-R4-GAMMA-EXPORT-GATE-001`; la exportacion general de R4/Gamma queda bloqueada y solo se conserva perfil restringido interoperable.
`AO-001_Decision_Formalizacion_Acotada_Doc04.md` (`D-2026-07-05-008`): se acepta `AO-DOC04-FORM-001`; `Pi_tb` / `Eq_tb` queda incorporado al Documento 04 solo en grado acotado bajo testigo.
`AO-001_Decision_Estatus_Pruebas_Externas_Confluencia.md` (`D-2026-07-05-007`): se acepta `AO-EXT-CONF-EXEC-001`; `EXT-CONF-001` queda ejecutado y `EXT-CONF-002` queda agregado como segunda prueba externa no regulada, sin cerrar Confluencia global ni Equivalencia global.
`AO-001_Decision_Ruta_Formalizacion_Doc04_Confluencia_Externa.md` (`D-2026-07-05-006`): se aceptan `AO-DOC04-FORM-CHK-001` y `AO-CONF-EXT-OPTIONS-001`; queda continuada por la ejecucion `D-2026-07-05-007` y por la incorporacion acotada `D-2026-07-05-008`.
`R001-001_Decision_Relacion_Formal_AO.md` (`D-2026-07-05-005`): se acepta `R001-TB-001` como relacion formal local entre `R001-TABLE-CHECK-001` y `AO-PPI-BRIDGE-001`; atiende la deuda local de relacion con `AO-001`, sin cerrar Equivalencia global ni Confluencia global.
`R001-001_Decision_Integracion_Table_Checks.md` (`D-2026-07-05-004`): se acepta `R001-TABLE-CHECK-001` como herramienta local no mutante integrada a `DO-LAB-RUN-001`; no canoniza `Xi`, no admite `H-Xi`, no cierra `P-200` ni resuelve `P-107`.
`HXI-001_Decision_Mantenimiento_Local.md` (`D-2026-07-05-003`): se acepta `HXI-MAINT-001`; `HXI-001` queda abierto en mantenimiento local, conserva `Xi_eval` y deja de ser frente activo inmediato.
`HXI-001_Decision_Resultado_Compuerta_Admision_Formal.md` (`D-2026-07-05-002`): se acepta `HXI-GATE-001` con resultado `mantener_Xi_eval`; `H-Xi` no se admite y `Xi_eval` queda conservado solo como herramienta local de expediente.
`HXI-001_Decision_Reapertura_Operativa.md` (`D-2026-07-05-001`): se acepta `HXI-REOPEN-001` y se reactiva `HXI-001` como frente activo inmediato para aplicar la compuerta de admision formal posterior; no admite `H-Xi`, no canoniza `Xi`, no reabre `PSI-001` y no autoriza transformaciones.
`AUT-001_Decision_Refinamiento_Contexto_Guardrails.md` (`D-2026-07-03-020`): se acepta `AUT-RISK-REFINE-002` para reclasificar falsos riesgos activos de guardrails como advertencias controladas; no borra hallazgos, no reabre `AUT-001` y no autoriza transformaciones.
`TCS-001_Decision_Estatus_Paquete_Minimo.md` (`D-2026-07-03-019`): se acepta el paquete minimo provisional de `TCS-001`; no canoniza `Concordance`, no crea Nivel C y no usa vision papers como fuente activa.
`AO-001_Decision_Estatus_Puente_Confluencia_Equivalencia.md` (`D-2026-07-03-018`): se acepta `AO-PPI-BRIDGE-001` como avance local sobre Confluencia y Equivalencia de proyecciones; no cierra problemas globales.
`AO-001_Decision_Criterios_Uso_R4_Gamma_Fuera_AUD.md` (`D-2026-07-03-017`): se acepta `AO-R4-GAMMA-USE-001` como criterio local de uso controlado fuera de `AUD-001`.
`AO-001_Decision_Estatus_Casos_Prueba_Algebra_Operacional.md` (`D-2026-07-03-016`): se acepta `AO-CASE-BAT-001` como bateria minima de casos operacionales.
`AUT-002_Decision_Referencias_Historicas_Transferidas.md` (`D-2026-07-03-015`): se acepta `referencia_historica_transferida` y el refinamiento de falsos bloqueos de historial; no restaura `PSI-001*`.
`AO-001_Decision_Estatus_Prueba_Gamma_Externa.md` (`D-2026-07-03-014`): `GAMMA-EXT-AO-001` queda aceptada como prueba positiva externa local de `Gamma_1`; no promueve `Gamma`, no modifica Documento 04 y no autoriza transformaciones materiales.
`HB-001_Decision_Congelamiento_Brotes_Alternos.md` (`D-2026-07-03-013`): `H-B.6` y `H-B.7` quedan congeladas como brotes alternos y originales historicos.
`PSI-TRASPASO-001_Decision_Eliminacion_Copia.md` (`D-2026-07-03-012`): la copia local de traspaso `PSI-001*` queda eliminada del Laboratorio.
`DOCS-001_Decision_Consolidacion_Documentos_00-04.md` (`D-2026-07-03-011`): documentos 00-03 quedan consolidados desde fuentes previas y Documento 04 queda actualizado como version inicial consolidada de Algebra Operacional; no modifica `01_Canon`, no exporta R4/Gamma fuera de `AUD-001` y no autoriza transformaciones materiales.
`AUD-001_Decision_Estatus_R4_Gamma_Formal_Local.md` (`D-2026-07-03-010`): `R4-FORMAL-AUD-001` y `GAMMA-FORMAL-AUD-001` quedan aceptadas como construcciones formales locales de `AUD-001`; `VAL-031` queda aceptada como segunda prueba positiva de `Gamma_1`; no promueve Canon, Nivel C ni transformaciones materiales.
`AO-001_Decision_Estatus_Marco_Inicial_Algebra_Operacional.md` (`D-2026-07-03-009`): se acepta `AO-MARCO-001` como marco inicial provisional de Algebra Operacional dentro de `AO-001`; incorporacion inicial decidida despues por `D-2026-07-03-011`.
`AO-001_Decision_Apertura.md` (`D-2026-07-03-008`): se abre `AO-001` como expediente preparatorio de la futura Algebra Operacional; la reserva del Documento 04 queda superada por `D-2026-07-03-011`.
`AUD-001_Decision_Estatus_Gamma_Ruta1_Definicion_Local.md` (`D-2026-07-03-007`): `GAMMA-DEF-001` queda aceptada como definicion local provisional de `Gamma` en ruta 1 dentro de `AUD-001`; no construye `Gamma` formal, no modifica `C-001` / `C-002`, no promueve a Canon ni autoriza transformaciones materiales.
`PSI-001` (`D-2026-07-03-003` a `D-2026-07-03-006`): decisiones historicas previas a la eliminacion de la copia local; no hay frente PSI activo dentro del Laboratorio.
`P-PI_Decision_Cierre_Frente_Matematico_Acotado.md` (`D-2026-07-03-002`): `P-PI.0` y `P-PI.1` quedan cerrados como frentes de trabajo; Confluencia y Equivalencia de proyecciones siguen abiertas como problemas de fondo.
`P-PI_Decision_Estatus_Frente_Matematico_Acotado.md` (`D-2026-07-03-001`): `P-PI.0` y `P-PI.1` quedaban confirmados como activos acotados tras los casos `PPI-EQ-001`, `PPI-EQ-002` y `PPI-CONF-001`; la decision estabilizo el frente sin cerrar Confluencia ni Equivalencia de proyecciones.

## Ultimo expediente cerrado

`HXI-001` (cerrado en mantenimiento local por `D-2026-07-06-012`); `AUD-001` (cerrado como version documental/operativa v0 por `D-2026-07-06-011`); `DOCS-001`.

Ultimo expediente tecnico cerrado: `AUT-002` por `D-2026-07-06-010`; `R001-001` por `D-2026-07-06-009`; `AUT-001`.

Ultimo expediente tecnico aceptado: `AUT-003` por `D-2026-07-06-015`; conserva `REPORT-LAYER-C002-GATE-001` como herramienta local no mutante conforme a `C-002`, integrada a `DO-LAB-RUN-001`.

## Proximo objetivo

Ampliar `AO-DOC04-WIDE-TEST-001` solo si se requieren casos heterogeneos adicionales de `REPORT_LAYER`, serializacion interfrente o nuevas variantes de `Pi_rep`; la prueba local inicial de `AO-DOC04-WIDE-001`, la precision de `REPORT_LAYER`, la justificacion de permanencia local pre-C y la compuerta no mutante `C-002` ya quedaron atendidas por `D-2026-07-06-007`, `D-2026-07-06-014` y `D-2026-07-06-015`.

Conservar `REPORT_LAYER` como capa local pre-C; cualquier promocion a Nivel C requiere candidata independiente, contrato exportable, serializacion estable, auditoria y decision nueva.

Conservar Documento 04 amplio v0 como formalizacion documental local, sin leerla como cierre global ni como Nivel C.

Mantener `MOC-ROUTE-011` como ruta vigente de mantenimiento teorico-operativo sin ejecucion; `MOC-ROUTE-010` ya quedo decidida por `D-2026-07-06-008`.

Conservar `MOC-ROUTE-012` como relacion documental local con `C-001` / `C-002`; no leerla como Nivel C, conformidad empirica, permiso de transformacion ni promocion del MOC.

Mantener bloqueada la exportacion general de R4/Gamma salvo nueva compuerta con dominio externo, semantica independiente del expediente y pruebas suficientes.

Profundizar `AO-PPI-BRIDGE-001` hacia pruebas de Confluencia global y Equivalencia global de proyecciones sin reabrir `P-PI.0` / `P-PI.1`.

Usar `R001-TB-001` solo como relacion formal local de apoyo a `AO-001`, no como cierre global.

Madurar `TCS-001` desde `TCS-MAT-PROV-001` hacia semantica formal, mas casos externos no regulados y relacion controlada con `AO-001` / `C-001`.

`PSI-001` ya no se continua dentro del Laboratorio y no tiene copia local de traspaso; cualquier continuidad de psicologia vive en el proyecto independiente `Psicologia Concordante`.

`AUT-002` queda cerrado tecnicamente; conserva el tratamiento minimo de referencias historicas transferidas. Si una ruta futura requiere contenido sustantivo de psicologia, debe abrir decision puente hacia el proyecto independiente.

`HXI-001` queda cerrado en mantenimiento local; solo se reabre por decision posterior con evidencia nueva, decision puente o promocion separada.

## No volver a discutir sin reapertura explicita

- `EF-001`
- `CP-001`
- Procedimiento
- Auditoria

## Deudas conceptuales activas

- `MOC-001`: mantener `MOC-ROUTE-011` como ruta teorico-operativa sin ejecucion, conservar `MOC-ROUTE-012` como relacion documental local con `C-001` / `C-002` y mantener cualquier estudio empirico real bloqueado hasta decision posterior; una especificacion tecnica futura de implementacion sigue condicionada a decision nueva.
- `REPORT_LAYER`: permanece local pre-C por `D-2026-07-06-014`; la herramienta no mutante conforme a `C-002` queda aceptada por `D-2026-07-06-015`; futura serializacion interfrente, promocion formal o modo mutante siguen condicionados a decision nueva.
- Conservar la deuda documental visible de `AUT-001` si se mantienen referencias a reportes generados excluidos del indice medio.
- Toda mejora futura de automatizacion debe abrir expediente, subexpediente o decision de reapertura.
- Deudas refinadas por `REC-001`: `REC-DEUDA-001` gobierno vs nucleo matematico; `REC-DEUDA-002` reglas metodologicas historicas; `REC-DEUDA-003` AAU historico atendida en grado operativo inicial por `AUT-001_Mapa_Fase_Media_AAU.md`; `REC-DEUDA-004` GDI/R4/Gamma; `REC-DEUDA-005` `H-Xi`, `P-107` y Concordancia.

- Deudas condicionadas derivadas de `RH-001`: `PM-001` queda revisado por `D-2026-07-06-016` y reconciliado solo como deuda historica condicionada, no como protocolo materializado; Concordancia, arquitectura multiagente y adjuntos historicos requieren expediente o decision separada antes de usarse.
- `HXI-001`: cerrado en mantenimiento local; conserva `Xi_eval` solo como herramienta local historica/auxiliar, mantiene `H-Xi` no admitida y no es frente activo inmediato.
- `P-PI.0` / `P-PI.1`: cerrados como frentes de trabajo; `PPI-EQ-001`, `PPI-EQ-002` y `PPI-CONF-001` quedan como evidencia ejecutada; Confluencia y Equivalencia de proyecciones permanecen abiertas como problemas de fondo.
- Vision papers: `VISION_PAPER_PROPUESTA.md` y `VISION_PAPER_FINAL_REFERENCIAS.md` quedan inactivos hasta nueva decision; no usarlos como autoridad, agenda o fuente para promocion.
- `PSI-001`: transferido a proyecto independiente; copia local eliminada; deuda restante: no usarlo como frente activo interno y abrir decision puente si se requiere dependencia externa.
- Automatizacion: `AUT-002` queda cerrado tecnicamente tras atender el falso bloqueo por referencias historicas transferidas; permanece abierta la mejora futura del detector si aparecen dependencias activas nuevas.
- `AUD-001`: cerrado como expediente completo en version documental/operativa v0; no promover `REPORT_LAYER`, `R4-CANDIDATA`, `R4-FORMAL-AUD-001` ni `GAMMA-FORMAL-AUD-001` fuera de su perfil local sin decision posterior; exportacion general de R4/Gamma queda bloqueada por `D-2026-07-05-009`.
- `AO-001`: mantener bloqueada la exportacion general de R4/Gamma, conservar `AO-DOC04-WIDE-TEST-001` como evidencia local no mutante y profundizar el puente local hacia pruebas globales.
- `AO-DOC04-WIDE-001`: formalizacion amplia v0 incorporada al Documento 04 y probada localmente por `D-2026-07-06-007`; quedan abiertas pruebas heterogeneas adicionales, posible serializacion de `REPORT_LAYER`, posible especificacion tecnica y cierres globales.
- `AO-CONF-EXT-OPTIONS-001`: `EXT-CONF-001` y `EXT-CONF-002` quedan ejecutados; pendiente decidir si se requieren mas pruebas externas para Confluencia o Equivalencia global.
- `TCS-001`: madurar semantica formal, mas casos externos no regulados, conflicto de autoridades y relacion controlada con `AO-001` / `C-001` antes de cualquier promocion teorica.
- Completar ficha de trazabilidad de `EF-001` si existe material previo.
- `H-B.6` / `H-B.7`: congeladas como brotes alternos y originales historicos; falta fuente sustantiva solo si una decision futura quisiera reactivarlas.
- Importar o formalizar el roadmap historico de `SRC-023`.
- Canon v0.1 reconciliado inicialmente por `REC-001`; pendiente solo si se abre `REC-DEUDA-001` o `REC-DEUDA-004`.
- Decalogo y Regla VII localizados en `SRC-023`; pendiente solo si se abre `REC-DEUDA-002`.
- Usar o exportar `R4-FORMAL-AUD-001` solo con auditoria y decision posterior.
- Usar o exportar `GAMMA-FORMAL-AUD-001` solo con auditoria y decision posterior.
