# Estado actual del proyecto

Estatus: estado operativo vigente.

Fecha de inicializacion del repositorio: 2026-07-01.

## Documentos oficiales consolidados

- [x] Documento 00 - Naturaleza: consolidado desde fuentes previas por `D-2026-07-03-011`.
- [x] Documento 01 - Canon: consolidado desde fuentes previas por `D-2026-07-03-011`.
- [x] Documento 02 - Fundamentos Matematicos: consolidado desde fuentes previas por `D-2026-07-03-011`.
- [x] Documento 03 - Ontologia: consolidado desde fuentes previas por `D-2026-07-03-011`.
- [x] Documento 04 - Algebra Operacional: actualizado como version inicial consolidada por `D-2026-07-03-011`.

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

- `HXI-001` (pausa operativa; reporte de consistencia aceptado y criterios de admision formal posterior preparados; no admite `H-Xi`)
- `TCS-001` (expediente teorico provisional; paquete minimo `TCS-DEF-MIN-001`, `TCS-FAIL-TYP-001` y `TCS-CASE-BAT-001` aceptado por `D-2026-07-03-019`; no Canon, no documento oficial)
- `AUT-002` (mantenimiento tecnico minimo de referencias historicas transferidas; aceptado por `D-2026-07-03-015`; no reabre `AUT-001`)
- `AUD-001` (completo en version documental/operativa v0; implementacion no mutante `AUDITOR-V0-001` aceptada; JSON reactivado; `REPORT_LAYER` local y compatibilidad con `DO_CHECK_REPORT` definidas; suite ejecutable completa encuadrada en `AUD-001_Ficha_Alcance_Suite_Ejecutable_Completa.md`; parser real acotado en `AUD-001_Ficha_Alcance_Parser_Real.md`; `R4-FORMAL-AUD-001` construido localmente; `GAMMA-FORMAL-AUD-001` construido localmente; `Gamma_1` probado por `VAL-030`, `VAL-031` y `GAMMA-EXT-AO-001`)
- `AO-001` (expediente preparatorio abierto para Algebra Operacional; `AO-MARCO-001`, `GAMMA-EXT-AO-001`, `AO-CASE-BAT-001`, `AO-R4-GAMMA-USE-001` y `AO-PPI-BRIDGE-001` aceptados localmente; sigue abierto para formalizacion posterior y pruebas globales no resueltas)

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

## Expedientes congelados

- `B-001.5`
- `H-B.6` (brote alterno y original historico; congelado por `D-2026-07-03-013`)
- `H-B.7` (brote alterno y original historico; congelado por `D-2026-07-03-013`)

## Expedientes pendientes de clasificacion

- Ninguno registrado.

## Hipotesis activas

- Ninguna hipotesis `H-B` activa; `H-B.6` y `H-B.7` quedan congeladas como brotes alternos y originales historicos.

## Hipotesis externas materializadas no admitidas

- `H-Xi` en `03_Expedientes/H-Xi.md`: hipotesis externa en evaluacion con `HXI-001` abierto y ruta 3 preparada como compuerta futura; fuente primaria historica `SRC-020`; no Canon, no documento oficial, no operador vigente.

## Problemas abiertos

- Confluencia.
- Equivalencia de proyecciones.
- Promocion o exportacion general fuera de `AUD-001` de `R4-FORMAL-AUD-001`.
- Promocion o exportacion general fuera de pruebas locales controladas de `GAMMA-FORMAL-AUD-001`.
- Formalizacion posterior del Documento 04 - Algebra Operacional.
- Maduracion de `TCS-001` mas alla del paquete minimo provisional.

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

- `AO-001_Casos_Prueba_Algebra_Operacional.md`: `AO-CASE-BAT-001`, casos `AO-CASE-001` a `AO-CASE-006` aceptados por `D-2026-07-03-016`.
- `AO-001_Criterios_Uso_R4_Gamma_Fuera_AUD.md`: `AO-R4-GAMMA-USE-001`, criterio local para referencia formal, prueba controlada o puente de problema; aceptado por `D-2026-07-03-017`.
- `AO-001_Puente_Confluencia_Equivalencia.md`: `AO-PPI-BRIDGE-001`, avance local con `AO-PPI-EQ-001` y `AO-PPI-CONF-001`; aceptado por `D-2026-07-03-018`.
- `TCS-001_Definiciones_Minimas.md`, `TCS-001_Tipologia_Fallos_Concordancia.md` y `TCS-001_Casos_Prueba.md`: paquete minimo teorico provisional aceptado por `D-2026-07-03-019`.

## Algoritmos provisionales activos

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
- `AUT-CLOSE-TECH-001`: cierre tecnico provisional en `03_Expedientes/AUT-001_Decision_Cierre_Tecnico_Provisional.md`.
- No hay algoritmos, matrices ni compuertas PSI activas dentro del Laboratorio; el paquete local `PSI-001*` fue eliminado por `D-2026-07-03-012`.

## Auditorias provisionales registradas

- `TCS-001_Auditoria_Paquete_Minimo.md`: auditoria favorable con limites del paquete minimo provisional de `TCS-001`.
- `AO-001_Auditoria_Puente_Confluencia_Equivalencia.md`: auditoria favorable como avance local, no como cierre global.
- `AO-001_Auditoria_Criterios_Uso_R4_Gamma_Fuera_AUD.md`: auditoria favorable de criterios de uso local controlado.
- `AO-001_Auditoria_Casos_Prueba_Algebra_Operacional.md`: auditoria favorable de `AO-CASE-BAT-001`.
- `AUT-002_Auditoria_Referencias_Historicas_Transferidas.md`: auditoria favorable del tratamiento de referencias historicas transferidas.
- `DOCS-001_Auditoria_Consolidacion_Documentos_00-04.md`: auditoria favorable de consolidacion de documentos 00-03 y actualizacion del Documento 04.
- `AUD-001_Auditoria_R4_Gamma_Formal_Local.md`: auditoria favorable de `R4-FORMAL-AUD-001`, `GAMMA-FORMAL-AUD-001` y `VAL-031` como artefactos locales de `AUD-001`.
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

- `AUD-001_Gamma_Ruta1_Definicion_Local.md`: definicion local provisional `GAMMA-DEF-001` para usar `Gamma_1(E, C) = G` solo como salida acotada dentro de `AUD-001`.
- `AUD-001_Relacion_Gamma_Ruta1_R4_Formal.md`: relacion provisional `REL-GAMMA-R4-001` que separa evidencia `R4-CANDIDATA`, generalizacion `Gamma_1` y deuda de R4 formal.
- `AUD-001_R4_Formal_Local.md`: construccion formal local `R4-FORMAL-AUD-001`.
- `AUD-001_Gamma_Formal_Local.md`: construccion formal local `GAMMA-FORMAL-AUD-001`.
- `AO-001_Prueba_Gamma_Externa.md`: prueba externa local `GAMMA-EXT-AO-001` y criterio `G_AO_OP-GOV-001`.
- `AO-001_Casos_Prueba_Algebra_Operacional.md`: bateria local `AO-CASE-BAT-001`.
- `AO-001_Criterios_Uso_R4_Gamma_Fuera_AUD.md`: criterio local `AO-R4-GAMMA-USE-001`.
- `AO-001_Puente_Confluencia_Equivalencia.md`: puente local `AO-PPI-BRIDGE-001`.
- `TCS-001_Definiciones_Minimas.md`, `TCS-001_Tipologia_Fallos_Concordancia.md` y `TCS-001_Casos_Prueba.md`: paquete teorico minimo provisional.
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

`DOCS-001`

Ultimo expediente tecnico cerrado: `AUT-001`

Ultimo expediente tecnico aceptado: `AUT-002`

## Proximo objetivo

Profundizar `AO-PPI-BRIDGE-001` hacia pruebas de Confluencia global y Equivalencia global de proyecciones sin reabrir `P-PI.0` / `P-PI.1`.

Decidir en expediente separado si algun resultado de `AO-001` debe incorporarse formalmente al Documento 04 o a una especificacion futura de `REPORT_LAYER`.

Madurar `TCS-001` mas alla del paquete minimo con metrica, casos externos y tratamiento de conflicto entre autoridades validas.

`PSI-001` ya no se continua dentro del Laboratorio y no tiene copia local de traspaso; cualquier continuidad de psicologia vive en el proyecto independiente `Psicologia Concordante`.

`AUT-002` atiende el tratamiento minimo de referencias historicas transferidas. Si una ruta futura requiere contenido sustantivo de psicologia, debe abrir decision puente hacia el proyecto independiente.

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

- Deudas condicionadas derivadas de `RH-001`: Protocolo de Admision/`PM-001`, Concordancia, arquitectura multiagente y adjuntos historicos requieren expediente o decision separada antes de usarse.
- `HXI-001`: en pausa operativa; no continuar admision sin reapertura explicita.
- `P-PI.0` / `P-PI.1`: cerrados como frentes de trabajo; `PPI-EQ-001`, `PPI-EQ-002` y `PPI-CONF-001` quedan como evidencia ejecutada; Confluencia y Equivalencia de proyecciones permanecen abiertas como problemas de fondo.
- Vision papers: `VISION_PAPER_PROPUESTA.md` y `VISION_PAPER_FINAL_REFERENCIAS.md` quedan inactivos hasta nueva decision; no usarlos como autoridad, agenda o fuente para promocion.
- `PSI-001`: transferido a proyecto independiente; copia local eliminada; deuda restante: no usarlo como frente activo interno y abrir decision puente si se requiere dependencia externa.
- Automatizacion: `AUT-002` atiende el falso bloqueo por referencias historicas transferidas; permanece abierta la mejora futura del detector si aparecen dependencias activas nuevas.
- `AUD-001`: no promover `REPORT_LAYER`, `R4-CANDIDATA`, `R4-FORMAL-AUD-001` ni `GAMMA-FORMAL-AUD-001` fuera de `AUD-001` sin decision posterior.
- `AO-001`: profundizar el puente local hacia pruebas globales o decidir formalizacion posterior del Documento 04 en expediente separado.
- `TCS-001`: madurar metrica, casos externos, conflicto de autoridades y relacion con dominios regulados antes de cualquier promocion teorica.
- Completar ficha de trazabilidad de `EF-001` si existe material previo.
- `H-B.6` / `H-B.7`: congeladas como brotes alternos y originales historicos; falta fuente sustantiva solo si una decision futura quisiera reactivarlas.
- Importar o formalizar el roadmap historico de `SRC-023`.
- Canon v0.1 reconciliado inicialmente por `REC-001`; pendiente solo si se abre `REC-DEUDA-001` o `REC-DEUDA-004`.
- Decalogo y Regla VII localizados en `SRC-023`; pendiente solo si se abre `REC-DEUDA-002`.
- Usar o exportar `R4-FORMAL-AUD-001` solo con auditoria y decision posterior.
- Usar o exportar `GAMMA-FORMAL-AUD-001` solo con auditoria y decision posterior.
