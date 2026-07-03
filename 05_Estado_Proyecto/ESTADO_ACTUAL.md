# Estado actual del proyecto

Estatus: estado operativo vigente.

Fecha de inicializacion del repositorio: 2026-07-01.

## Documentos oficiales declarados completos en el punto de partida

- [x] Documento 00 - Naturaleza.
- [x] Documento 01 - Canon.
- [x] Documento 02 - Fundamentos Matematicos.
- [x] Documento 03 - Ontologia.
- [ ] Documento 04 - Algebra Operacional.

## Documentos oficiales de Nivel C

- [x] `C-002_RFC_Operativo_Auditor_v0.md`: RFC operativo oficial del Auditor v0; complementa `C-001`.
- [x] `C-001_Especificacion_Tecnica_Auditor.md`: especificacion tecnica oficial inicial del Auditor.

## Consolidacion en este repositorio

- [ ] Incorporar version completa del Documento 00 desde fuentes previas.
- [ ] Incorporar version completa del Documento 01 desde fuentes previas.
- [ ] Incorporar version completa del Documento 02 desde fuentes previas.
- [ ] Incorporar version completa del Documento 03 desde fuentes previas.

## Expedientes abiertos

- `HXI-001` (pausa operativa; reporte de consistencia aceptado y criterios de admision formal posterior preparados; no admite `H-Xi`)
- `PSI-001` (abierto; matriz de patrones no clinicos aceptada; `A-PSI-001`, `DEF-PSI-ORG-001`, `CRIT-PSI-TR-001`, `EX-PSI-001` a `EX-PSI-005`, `CAS-PSI-001` a `CAS-PSI-006` y `PSI-MAT-PAT-001` siguen provisionales dentro del expediente)
- `TCS-001` (expediente teorico provisional; `Concordance` tratada como propiedad auditable de gobernanza de sistemas; analisis de fondo registrado; no Canon, no documento oficial)
- `P-PI.0` (activo acotado para Equivalencia de proyecciones por `D-2026-07-02-032`)
- `P-PI.1` (activo acotado para Confluencia por `D-2026-07-02-032`)
- `AUD-001` (completo en version documental/operativa v0; produjo `C-002`; queda abierto solo para rutas posteriores como implementacion, R4 formal, `Gamma`, `REPORT_LAYER` Nivel C o cierre/pausa)

## Expedientes cerrados

- `B-001`
- `CP-001`
- `EF-001`
- `DO-001`
- `RH-001`
- `RH-002`
- `REC-001`
- `AUT-001`

## Expedientes congelados

- `B-001.5`

## Expedientes pendientes de clasificacion

- Ninguno registrado.

## Hipotesis activas

- `H-B.6` (alcance local minimo aceptado por `D-HB-ALC-001`; contenido sustantivo no materializado)
- `H-B.7` (alcance local minimo aceptado por `D-HB-ALC-001`; contenido sustantivo no materializado)

## Hipotesis externas materializadas no admitidas

- `H-Xi` en `03_Expedientes/H-Xi.md`: hipotesis externa en evaluacion con `HXI-001` abierto y ruta 3 preparada como compuerta futura; fuente primaria historica `SRC-020`; no Canon, no documento oficial, no operador vigente.

## Problemas abiertos

- Confluencia.
- Equivalencia de proyecciones.
- Definicion formal completa de `R4`.
- Construccion formal de `Gamma`.

## Contratos provisionales activos

- `AUD-001_Contrato_Reportes.md`: `OPERATOR_REPORT`, `MP_FAIL_REPORT`, `CR_FAIL_REPORT`, `TAU_REPORT`, `D_REPORT`, `TR_PROPOSAL_REPORT`, `TR_EXECUTION_REPORT`, `TR_EXECUTION_FAIL_REPORT` y `REVERSAL_REPORT`.
- `AUD-001_REPORT_LAYER_Candidata.md`: `REPORT-LAYER-CAND-001`, capa abstracta candidata para reportes equivalentes dentro de `AUD-001`.
- `AUD-001_SPEC-RFC-AUDITOR-V0_Candidata.md`: `SPEC-RFC-AUDITOR-V0`, candidata promovida a `C-002`.

## Propuestas provisionales promovidas o cerradas

- `DO-PROP-001`: propuesta provisional de automatizacion en `03_Expedientes/DO-001.md`; absorbida por `C-001`.
- `SPEC-AUD-001_Candidata`: especificacion tecnica candidata del Auditor en `03_Expedientes/DO-001_SPEC-AUD-001_Candidata.md`; promovida a `C-001`.
- `SPEC-RFC-AUDITOR-V0`: candidata tipo RFC en `03_Expedientes/AUD-001_SPEC-RFC-AUDITOR-V0_Candidata.md`; promovida a `C-002`.

## Algoritmos provisionales activos

- `DO-CHECK-001`: verificador no mutante de trazabilidad y estatus en `03_Expedientes/DO-001_DO-CHECK-001.md`; validado inicialmente contra tres archivos locales.
- `DO-CHECK-MIN-001`: implementacion minima no mutante en `06_Automatizacion/do_check_min.py`; validada provisionalmente por ejecucion equivalente en `AUT-001`.
- `DO-CHECK-MED-001`: implementacion media no mutante en `06_Automatizacion/do_check_med.py`; validada provisionalmente por ejecucion equivalente en `AUT-001`.
- `DO-STATE-BOARD-001`: tablero no mutante en `06_Automatizacion/lab_status_board.py`; validado provisionalmente por ejecucion equivalente en `AUT-001`.
- `DO-LAB-CONTINUITY-001`: continuidad integrada no mutante en `06_Automatizacion/lab_continuity_report.py`; validada provisionalmente por reportes fuente en `AUT-001`.
- `DO-LAB-RUN-001`: comando unico no mutante en `06_Automatizacion/lab_run.py`; validado provisionalmente como corrida local unificada de `AUT-001`.
- `DO-LAB-RISK-001`: clasificador no mutante refinado en `06_Automatizacion/lab_risk_classifier.py`; separa riesgos activos, advertencias controladas, deuda documental y advertencias heredadas.
- `DO-LAB-SUMMARY-001`: resumen ejecutivo automatico no mutante en `06_Automatizacion/lab_executive_summary.py`; validado provisionalmente para sintetizar estado, riesgos y siguiente accion.
- `AUT-CLOSE-CRIT-001`: criterios de cierre de fase media en `03_Expedientes/AUT-001_Criterios_Cierre_Fase_Media.md`.
- `AUT-RISK-TREAT-001`: tratamiento inicial de riesgos altos en `03_Expedientes/AUT-001_Tratamiento_Riesgos_Altos.md`.
- `AUT-RISK-ACT-REVIEW-001`: matriz de revision de riesgos activos en `03_Expedientes/AUT-001_Matriz_Revision_Riesgos_Activos.md`.
- `AUT-RISK-REFINE-001`: refinamiento contextual de riesgos en `03_Expedientes/AUT-001_Refinamiento_DO-LAB-RISK.md`.
- `AUT-CLOSE-TECH-001`: cierre tecnico provisional en `03_Expedientes/AUT-001_Decision_Cierre_Tecnico_Provisional.md`.
- `PSI-MAP-CONT-001`: mapa de continuidad conceptual no clinica en `03_Expedientes/PSI-001_Mapa_Continuidad_Conceptual.md`.
- `PSI-CAS-TR-001`: serie de casos de transformacion no clinicos en `03_Expedientes/PSI-001_Casos_Transformacion_No_Clinicos.md`.
- `PSI-MAT-PAT-001`: matriz de patrones no clinicos en `03_Expedientes/PSI-001_Matriz_Patrones_Transformacion_No_Clinica.md`.

## Auditorias provisionales registradas

- `RH-001_Auditoria_Procesamiento.md`: auditoria favorable para cerrar el procesamiento de la transcripcion historica; no modifica Canon ni documentos oficiales.
- `RH-002_Auditoria_Procesamiento.md`: auditoria favorable para cerrar el procesamiento del lote historico de Descargas; no modifica Canon ni documentos oficiales.
- `REC-001_Auditoria_Reconciliacion.md`: auditoria favorable para cerrar la reconciliacion inicial de Canon/baselines; no modifica Canon ni documentos oficiales.
- `PSI-001_Auditoria_A-PSI-001.md`: auditoria favorable para aceptar `A-PSI-001` como axioma candidato operativo dentro de `PSI-001`.
- `PSI-001_Auditoria_Definicion_Organizacion.md`: auditoria favorable para aceptar `DEF-PSI-ORG-001` como definicion provisional operativa dentro de `PSI-001`.
- `PSI-001_Auditoria_Criterio_Transformacion.md`: auditoria favorable para aceptar `CRIT-PSI-TR-001` como criterio provisional operativo dentro de `PSI-001`.
- `PSI-001_Auditoria_Ejemplos_Conceptuales.md`: auditoria favorable para aceptar `EX-PSI-001` a `EX-PSI-005` como bateria conceptual provisional no clinica dentro de `PSI-001`.
- `PSI-001_Auditoria_Mapa_Continuidad_Conceptual.md`: auditoria favorable para aceptar `PSI-MAP-CONT-001` como mapa de continuidad no clinico.
- `PSI-001_Auditoria_Casos_Transformacion_No_Clinicos.md`: auditoria favorable para aceptar `CAS-PSI-001` a `CAS-PSI-006` como serie conceptual provisional no clinica.
- `PSI-001_Auditoria_Matriz_Patrones_Transformacion_No_Clinica.md`: auditoria favorable para aceptar `PSI-MAT-PAT-001` como matriz provisional no clinica.
- `HXI-001_Auditoria_Apertura.md`: auditoria favorable para abrir `HXI-001` como evaluacion separada no admisoria.
- `HXI-001_Auditoria_Mapa_Preliminar.md`: auditoria favorable para aceptar el mapa preliminar `H-Xi` / `R` como guia operativa no admisoria.
- `HXI-001_Auditoria_Matriz_Pruebas.md`: auditoria favorable para aceptar la matriz `HXI-R` como guia operativa no admisoria.
- `HXI-001_Auditoria_Dictamen_Utilidad_Local.md`: auditoria favorable para aceptar el dictamen de utilidad local de `Xi` como guia operativa no admisoria.
- `HXI-001_Auditoria_Notacion_Minima_Xi-R.md`: auditoria favorable para aceptar la notacion minima `Xi-R` como guia operativa no admisoria.
- `HXI-001_Auditoria_Criterios_Admision_Formal.md`: auditoria favorable para aceptar criterios de admision formal posterior como compuerta provisional no admisoria.
- `HXI-001_Auditoria_Reporte_Consistencia.md`: auditoria favorable para aceptar el reporte de consistencia de la notacion minima `Xi-R`.
- `AUT-001_Validacion_DO-STATE-BOARD.md`: validacion provisional favorable del tablero de estado no mutante.
- `AUT-001_Validacion_DO-LAB-CONTINUITY.md`: validacion provisional favorable de la continuidad integrada no mutante.
- `AUT-001_Validacion_DO-LAB-RUN.md`: validacion provisional favorable del comando unico no mutante.
- `AUT-001_Validacion_DO-LAB-RISK.md`: validacion provisional favorable del clasificador de advertencias y riesgos.
- `AUT-001_Validacion_DO-LAB-SUMMARY.md`: validacion provisional favorable del resumen ejecutivo automatico.
- `AUT-001_Validacion_Cierre_Riesgos.md`: validacion provisional favorable de criterios de cierre y riesgos altos.
- `AUT-001_Validacion_Revision_Riesgos_Activos.md`: validacion provisional favorable de la revision de 17 riesgos activos.
- `AUT-001_Validacion_Refinamiento_DO-LAB-RISK.md`: validacion provisional favorable del refinamiento de riesgos controlados.
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
- `AUD-001_Decision_Reactivacion_REPORT_LAYER.md` (`D-2026-07-02-025`): reactiva `AUD-001` de forma acotada para separar `REPORT_LAYER`.
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
- `PSI-001_Decision_Apertura.md`: abre `PSI-001` como frente psicologico inicial no clinico; no canoniza `A-PSI-001`.
- `PSI-001_Decision_Estatus_A-PSI-001.md`: acepta `A-PSI-001` como axioma candidato operativo dentro de `PSI-001`; no lo canoniza.
- `PSI-001_Decision_Estatus_Definicion_Organizacion.md`: acepta `DEF-PSI-ORG-001` como definicion provisional operativa dentro de `PSI-001`; no la canoniza.
- `PSI-001_Decision_Estatus_Criterio_Transformacion.md`: acepta `CRIT-PSI-TR-001` como criterio provisional operativo dentro de `PSI-001`; no lo canoniza.
- `PSI-001_Decision_Estatus_Ejemplos_Conceptuales.md`: acepta `EX-PSI-001` a `EX-PSI-005` como bateria conceptual provisional no clinica dentro de `PSI-001`; no la canoniza.
- `HXI-001_Decision_Apertura.md`: abre `HXI-001` como evaluacion separada de `H-Xi` frente a relaciones `R`; no admite `H-Xi`.
- `HXI-001_Decision_Estatus_Mapa_Preliminar.md`: acepta el mapa preliminar `H-Xi` / `R` como guia operativa de evaluacion; no admite `H-Xi`.
- `HXI-001_Decision_Estatus_Matriz_Pruebas.md`: acepta la matriz `HXI-R` como guia operativa de evaluacion; no admite `H-Xi`.
- `HXI-001_Decision_Estatus_Dictamen_Utilidad_Local.md`: acepta el dictamen de utilidad local de `Xi` como guia operativa de evaluacion; no admite `H-Xi`.
- `HXI-001_Decision_Ruta_Operativa.md`: elige continuidad acotada con notacion minima; no admite `H-Xi`.
- `HXI-001_Decision_Estatus_Notacion_Minima_Xi-R.md`: acepta la notacion minima `Xi-R` como guia operativa de evaluacion; no admite `H-Xi`.
- `HXI-001_Decision_Preparacion_Admision_Formal.md`: prepara ruta 3 de admision formal posterior de forma condicionada; no admite `H-Xi`.
- `HXI-001_Decision_Estatus_Criterios_Admision_Formal.md`: acepta criterios de admision formal posterior como compuerta provisional; no admite `H-Xi`.
- `HXI-001_Decision_Estatus_Reporte_Consistencia.md`: acepta el reporte de consistencia de `Xi_eval`; no admite `H-Xi`.
- `HXI-001_Decision_Pausa_Operativa.md`: pausa operativa de `HXI-001`; no admite `H-Xi`.
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
- `HB-001_Decision_Fichas_Alcance_H-B.md` (`D-2026-07-02-030`): acepta alcance local minimo de `H-B.6` y `H-B.7` sin contenido sustantivo materializado.
- `PSI-001_Decision_Estatus_Mapa_Continuidad_Conceptual.md` (`D-2026-07-02-022`): acepta `PSI-MAP-CONT-001` como mapa de continuidad no clinico.
- `PSI-001_Decision_Estatus_Casos_Transformacion_No_Clinicos.md` (`D-2026-07-02-023`): acepta `CAS-PSI-001` a `CAS-PSI-006` como serie conceptual provisional no clinica.
- `PSI-001_Decision_Estatus_Matriz_Patrones_Transformacion_No_Clinica.md` (`D-2026-07-02-024`): acepta `PSI-MAT-PAT-001` como matriz provisional no clinica.
- `AUT-001_Decision_Fase_Media.md`: acepta `DO-CHECK-MED-001` como automatizacion media provisional, sin cerrar `AUT-001`.

## Mapas preliminares de expediente

- `HXI-001_Mapa_Preliminar_PSI-R.md`: mapa preliminar operativo no admisorio entre `H-Xi`, relaciones `R` y ejemplos de `PSI-001`; aceptado para guiar pruebas.

## Ejemplos conceptuales de expediente

- `PSI-001_Ejemplos_Conceptuales_No_Clinicos.md`: `EX-PSI-001` a `EX-PSI-005`, bateria conceptual provisional no clinica.
- `PSI-001_Casos_Transformacion_No_Clinicos.md`: `CAS-PSI-001` a `CAS-PSI-006`, serie breve de casos conceptuales no clinicos.
- `PSI-001_Matriz_Patrones_Transformacion_No_Clinica.md`: `PSI-MAT-PAT-001`, matriz provisional de patrones no clinicos de transformacion.
- `TCS-001_Teoria_Concordante_de_Sistemas.md`: propuesta teorica inicial para `Concordance Theory`.
- `TCS-001_Analisis_Fondo.md`: analisis provisional de fondo; identifica tensiones, supuestos ocultos, deudas conceptuales, fallos de concordancia y condiciones candidatas.

## Matrices provisionales de expediente

- `HXI-001_Matriz_Pruebas_HXI-R.md`: matriz provisional operativa sobre `EX-PSI-001` a `EX-PSI-005`; aceptada para preparar dictamen de utilidad local de `Xi`, sin admision de `H-Xi`.

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

## Tableros de automatizacion

- `06_Automatizacion/lab_status_board.py`: tablero no mutante `DO-STATE-BOARD-001`.
- `06_Automatizacion/reportes/lab_status_board.md`: reporte Markdown conservado.
- `06_Automatizacion/reportes/lab_status_board.json`: reporte JSON conservado.


- `EX-PSI-001` a `EX-PSI-005`: bateria conceptual no clinica en `03_Expedientes/PSI-001_Ejemplos_Conceptuales_No_Clinicos.md`; vigente solo dentro de `PSI-001`.

## Criterios de evaluacion de expediente

- `HXI-001_Criterios_Evaluacion.md`: compuertas para evaluar relacion local `H-Xi` / `R`; no admite `H-Xi`.

## Criterios provisionales de expediente

- `CRIT-PSI-TR-001`: criterio provisional de transformacion, reorganizacion, desorganizacion y disolucion en `03_Expedientes/PSI-001_Criterio_Transformacion_Experiencia_Psicologica.md`; vigente solo dentro de `PSI-001`.

## Definiciones provisionales de expediente

- `DEF-PSI-ORG-001`: definicion provisional de `organizacion de la experiencia psicologica` en `03_Expedientes/PSI-001_Definicion_Organizacion_Experiencia_Psicologica.md`; vigente solo dentro de `PSI-001`.

## Reglas provisionales activas

- `DO-001_Regla_Permiso_Actualizacion.md`: `PERMISO-ACT-001` define quien puede convertir una recomendacion o propuesta en cambio ejecutado; validado inicialmente contra tres casos locales.
- `NIVEL-C-001`: definicion local de `Nivel C - Especificaciones` en `05_Estado_Proyecto/NIVEL_C_ESPECIFICACIONES.md`.

## Validaciones provisionales activas

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
- `VAL-025`: uso formal indebido de `Gamma` validado provisionalmente contra `AUD-SIM-025`.
- `VAL-026`: separacion de niveles `AUD-T08` validada provisionalmente contra `AUD-SIM-026`.
- `VAL-027`: termino nuevo sin estatus `AUD-T09` validado provisionalmente contra `AUD-SIM-027`.
- `VAL-028`: puente `REPORT_LAYER` / `DO_CHECK_REPORT` validado provisionalmente contra `AUD-SIM-028`.
- `VAL-029`: proyeccion a documento tipo RFC validada provisionalmente contra `AUD-SIM-029`.
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

- `P-PI_PPI-CONF-001_Rutas_Estado_Operativo.md`: caso ejecutado provisional de Confluencia local.
- `P-PI_PPI-EQ-002_Completitud_A_C002.md`: caso ejecutado provisional de Equivalencia de proyecciones hacia `C-002`.
- `PSI-001_Mapa_Continuidad_Conceptual.md`: mapa provisional no clinico para continuidad conceptual de `PSI-001`.
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
- `HB-001_Ficha_Alcance_H-B.6.md`: ficha de alcance local minimo para `H-B.6`.
- `HB-001_Ficha_Alcance_H-B.7.md`: ficha de alcance local minimo para `H-B.7`.

## Ultima decision arquitectonica

`C-002_RFC_Operativo_Auditor_v0.md` promovido como RFC operativo oficial del Auditor v0; complementa `C-001`.

## Ultima decision operativa

`P-PI_Decision_Estatus_Frente_Matematico_Acotado.md` (`D-2026-07-03-001`): `P-PI.0` y `P-PI.1` quedan confirmados como activos acotados tras los casos `PPI-EQ-001`, `PPI-EQ-002` y `PPI-CONF-001`; la decision estabiliza el frente sin cerrar Confluencia ni Equivalencia de proyecciones.

## Ultimo expediente cerrado

`AUT-001`

Ultimo expediente tecnico cerrado: `AUT-001`

## Proximo objetivo

Mantener seguimiento acotado del frente `P-PI.0` / `P-PI.1` con los tres casos ejecutados y sus deudas abiertas.

## No volver a discutir sin reapertura explicita

- `EF-001`
- `CP-001`
- Procedimiento
- Auditoria

## Deudas conceptuales activas

- Si se busca implementacion, crear herramienta no mutante conforme a `C-002` antes de cualquier modo mutante.
- Si se busca promocion formal, justificar si `REPORT_LAYER` debe pasar a Nivel C o permanecer local.
- Conservar la deuda documental visible de `AUT-001` si se mantienen referencias a reportes generados excluidos del indice medio.
- Toda mejora futura de automatizacion debe abrir expediente, subexpediente o decision de reapertura.
- Deudas refinadas por `REC-001`: `REC-DEUDA-001` gobierno vs nucleo matematico; `REC-DEUDA-002` reglas metodologicas historicas; `REC-DEUDA-003` AAU historico atendida en grado operativo inicial por `AUT-001_Mapa_Fase_Media_AAU.md`; `REC-DEUDA-004` GDI/R4/Gamma; `REC-DEUDA-005` `H-Xi`, `P-107` y Concordancia.

- Consolidar contenido real de documentos 00, 01, 02 y 03 desde fuentes previas.
- Deudas condicionadas derivadas de `RH-001`: Protocolo de Admision/`PM-001`, Concordancia, Documento 04, arquitectura multiagente y adjuntos historicos requieren expediente o decision separada antes de usarse.
- `HXI-001`: en pausa operativa; no continuar admision sin reapertura explicita.
- `P-PI.0` / `P-PI.1`: activos de forma acotada; `PPI-EQ-001`, `PPI-EQ-002` y `PPI-CONF-001` ejecutados provisionalmente; falta decision de estatus acotado; Confluencia y Equivalencia de proyecciones permanecen abiertas.
- Vision papers: `VISION_PAPER_PROPUESTA.md` y `VISION_PAPER_FINAL_REFERENCIAS.md` quedan inactivos hasta nueva decision; no usarlos como autoridad, agenda o fuente para promocion.
- `PSI-001`: queda como base conceptual no clinica con matriz de patrones aceptada; no cerrar, promover, abrir psicopatologia ni vincular con `HXI-001` sin decision posterior.
- `AUD-001`: no promover `REPORT_LAYER`, `R4-CANDIDATA`, R4 formal ni `Gamma` sin decision posterior.
- `TCS-001`: desarrollar definiciones minimas, tipologia de fallos de concordancia y casos de prueba antes de cualquier promocion teorica.
- Completar ficha de trazabilidad de `EF-001` si existe material previo.
- `H-B.6` / `H-B.7`: alcance local minimo aceptado; falta fuente sustantiva o decision posterior de congelamiento, absorcion, cierre o apertura de expediente propio.
- Importar o formalizar el roadmap historico de `SRC-023`.
- Canon v0.1 reconciliado inicialmente por `REC-001`; pendiente solo si se abre `REC-DEUDA-001` o `REC-DEUDA-004`.
- Decalogo y Regla VII localizados en `SRC-023`; pendiente solo si se abre `REC-DEUDA-002`.
- Definir localmente `R4`.
- Definir localmente `Gamma`.
