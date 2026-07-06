# Current State

Estamos aqui.

Ultimo expediente cerrado:

- `DOCS-001`

Ultimo expediente tecnico cerrado:

- `AUT-001`

Ultimo expediente tecnico aceptado:

- `R001-001` como integracion tecnica provisional de `R001-TABLE-CHECK-001` por `D-2026-07-05-004` y relacion formal local `R001-TB-001` por `D-2026-07-05-005`; no canoniza `Xi`, no admite `H-Xi`, no cierra `P-200` ni resuelve `P-107`.
- `AUT-002` como mantenimiento minimo de referencias historicas transferidas por `D-2026-07-03-015`; no reabre `AUT-001`.

Ultimo expediente transferido:

- `PSI-001` hacia proyecto independiente `Psicologia Concordante`; copia local de traspaso eliminada por `D-2026-07-03-012`.

Licencia y derechos:

- `Licencia_y_Derechos.md`: reserva de derechos del Modelo Operativo Concordante (MOC) y Concordante Lab; todos los derechos reservados.

Revision de formalizacion:

- `05_Estado_Proyecto/REVISION_FORMALIZACION_PENDIENTE.md`: no detecta deuda nueva bloqueante; conserva como pendientes vivos `MOC-ROUTE-010`, Documento 04 amplio, Confluencia global, Equivalencia global, exportacion R4/Gamma y maduracion de `TCS-001`.

Ultima decision arquitectonica:

- `C-002_RFC_Operativo_Auditor_v0.md` promovido como documento oficial de Nivel C en formato tipo RFC; complementa `C-001` y quedo alineado el 2026-07-03 con JSON, fixtures y adaptador no mutante.

Ultima decision operativa:

- `MOC-001_Decision_Paquete_Registro_Auditoria_Piloto.md` (`D-2026-07-06-005`): acepta `MOC-PILOT-REG-AUDIT-PACK-001`; metodo de registro sin datos personales y matriz de auditoria quedan preparados documentalmente. La siguiente ruta recomendada es `MOC-ROUTE-010`, decidir rutas posteriores sin reclutamiento ni ejecucion.
- `MOC-001_Decision_Paquete_PreEjecucion_Piloto.md` (`D-2026-07-06-004`): acepta `MOC-PREEXEC-PACK-001`; semantica, operaciones formales, casos congelados, plantilla de respuesta y reglas/protocolo quedan preparados documentalmente. La siguiente ruta recomendada es `MOC-ROUTE-009`, metodo de registro sin datos personales y matriz de auditoria.
- `MOC-001_Decision_Compuerta_Autorizacion_Ejecucion_Piloto.md` (`D-2026-07-06-003`): acepta `MOC-GATE-PILOT-EXEC-001`; resultado `no_autorizar_ejecucion`, `piloto_autorizado = false`; la siguiente ruta recomendada es `MOC-ROUTE-008`, preparar paquete documental pre-ejecucion sin reclutamiento ni ejecucion.
- `MOC-001_Decision_Rutas_Posteriores_Ruta_006.md` (`D-2026-07-06-002`): acepta `MOC-NEXT-ROUTES-006`; la siguiente ruta recomendada es `MOC-ROUTE-007`, decidir compuerta de autorizacion o no autorizacion del piloto futuro sin ejecutarlo.
- `MOC-001_Decision_Protocolo_Piloto_Empirico_Futuro.md` (`D-2026-07-06-001`): acepta `MOC-EMP-PILOT-PROTO-001` como protocolo documental de piloto empirico futuro, sin ejecucion real.
- `MOC-001_Decision_Rutas_Posteriores_Ruta_005.md` (`D-2026-07-05-025`): acepta `MOC-NEXT-ROUTES-005`; la siguiente ruta recomendada es `MOC-ROUTE-006`, preparar protocolo documental de piloto empirico futuro sin ejecucion real.
- `MOC-001_Decision_Ejecucion_Ruta_005.md` (`D-2026-07-05-024`): acepta `MOC-ROUTE-005`; `MOC-EVAL-PROTO-002` refina el protocolo de evaluadores con `operator_trace`, `Pi_moc_trace`, `ao_bridge`, `protocol_v02` y `protocol_v02_summary`.
- `MOC-001_Decision_Rutas_Posteriores_Ruta_004.md` (`D-2026-07-05-023`): acepta `MOC-NEXT-ROUTES-004`; la siguiente ruta recomendada es `MOC-ROUTE-005`, refinar protocolo de evaluadores usando `operator_trace`, `Pi_moc_trace` y `ao_bridge`.
- `MOC-001_Decision_Puente_Formal_MOC_AO.md` (`D-2026-07-05-022`): acepta `MOC-AO-BRIDGE-001`; formaliza el puente local `MOC/AO` usando `operator_trace` como evidencia local de regla ganadora y `ao_bridge` como proyeccion operacional acotada.
- `MOC-001_Decision_Rutas_Posteriores_Ruta_003.md` (`D-2026-07-05-021`): acepta `MOC-NEXT-ROUTES-003`; la siguiente ruta recomendada es `MOC-ROUTE-004`, formalizar puente `MOC/AO` usando `operator_trace`.
- `MOC-001_Decision_Puente_Formal_MOC_TCS.md` (`D-2026-07-05-020`): acepta `MOC-TCS-BRIDGE-001`; formaliza `OP_MOC_XI`, `OP_MOC_TCS`, `OP_MOC_STATE` y `OP_MOC_AGREEMENT` como operadores ejecutables locales.
- `MOC-001_Decision_Rutas_Posteriores_Ruta_002.md` (`D-2026-07-05-019`): acepta `MOC-NEXT-ROUTES-002`; la siguiente ruta recomendada es `MOC-ROUTE-003`, formalizar puente `MOC/TCS` a partir de la bateria ampliada.
- `MOC-001_Decision_Ejecucion_Ruta_002.md` (`D-2026-07-05-018`): acepta `MOC-ROUTE-002`; `MOC-EVAL-001` queda con 11 casos aprobados, 0 fallos, 6 coincidencias exactas, 3 parciales y 2 desacuerdos justificados.
- `MOC-001_Decision_Siguientes_Rutas_Validas.md` (`D-2026-07-05-017`): acepta `MOC-NEXT-ROUTES-001`; la siguiente ruta recomendada es `MOC-ROUTE-002`, ampliar bateria sintetica no clinica con desacuerdos justificados y casos limite.
- `MOC-001_Decision_Ejecucion_Ruta_Valida_001.md` (`D-2026-07-05-016`): acepta `MOC-ROUTE-EXEC-001`; primera ruta valida ejecutada favorablemente con `MOC-EVAL-001`, 7 casos aprobados, 0 fallos y `risk_blocks_closure: false`.
- `MOC-001_Decision_Disenio_Estudio_Empirico.md` (`D-2026-07-05-015`): acepta `MOC-EMP-STUDY-001` como diseno documental de estudio empirico futuro, sin ejecucion real, sin personas reales, sin dominios clinicos o regulados y sin canonizar el MOC.
- `MOC-001_Decision_Simulacion_Software.md` (`D-2026-07-05-014`): acepta `MOC-EVAL-001` como simulador no mutante integrado a `DO-LAB-RUN-001`; genera reportes locales con casos sinteticos no clinicos y tres evaluadores simulados.
- `MOC-001_Decision_Metricas_Protocolo.md` (`D-2026-07-05-013`): acepta `MOC-METRIC-STATE-001` y `MOC-EVAL-PROTO-001` como metrica cualitativa ordinal y protocolo reproducible provisional.
- `MOC-001_Decision_Formalizacion_Xi_eval.md` (`D-2026-07-05-012`): acepta `MOC-XI-EVAL-FORMAL-001`; `Xi_eval` queda formalizado solo como operador local de `MOC-001`, sin admitir `H-Xi` ni canonizar `Xi`.
- `MOC-001_Decision_Apertura.md` (`D-2026-07-05-011`): abre `MOC-001` como expediente integrador teorico-operativo no canonico, no clinico y no regulado, conectado con `HXI-001`, `TCS-001` y `AO-001`.
- `TCS-001_Decision_Maduracion_Provisional.md` (`D-2026-07-05-010`): acepta `TCS-MAT-PROV-001` con metrica cualitativa provisional, casos externos no regulados y patron de conflicto entre autoridades validas; no canoniza `Concordance`, no crea Nivel C y no cierra la maduracion de TCS.
- `AO-001_Decision_Compuerta_Exportacion_R4_Gamma.md` (`D-2026-07-05-009`): acepta `AO-R4-GAMMA-EXPORT-GATE-001`; la exportacion general de R4/Gamma queda bloqueada y solo se conserva perfil restringido interoperable.
- `AO-001_Decision_Formalizacion_Acotada_Doc04.md` (`D-2026-07-05-008`): acepta `AO-DOC04-FORM-001`; incorpora `Pi_tb` / `Eq_tb` al Documento 04 en grado acotado bajo testigo, sin cerrar problemas globales.
- `AO-001_Decision_Estatus_Pruebas_Externas_Confluencia.md` (`D-2026-07-05-007`): acepta `AO-EXT-CONF-EXEC-001`; ejecuta `EXT-CONF-001`, agrega `EXT-CONF-002` como segunda prueba externa no regulada y queda continuada por `D-2026-07-05-008`, `D-2026-07-05-009` y `D-2026-07-05-010`.
- `AO-001_Decision_Ruta_Formalizacion_Doc04_Confluencia_Externa.md` (`D-2026-07-05-006`): acepta `AO-DOC04-FORM-CHK-001` y `AO-CONF-EXT-OPTIONS-001`; conserva una candidata `Pi_tb` / `Eq_tb` para Documento 04, ejecutada despues en grado acotado por `D-2026-07-05-008`.
- `R001-001_Decision_Relacion_Formal_AO.md` (`D-2026-07-05-005`): acepta `R001-TB-001` como relacion formal local entre `R001-TABLE-CHECK-001` y `AO-PPI-BRIDGE-001`; atiende la deuda local de relacion con `AO-001`, sin cerrar Equivalencia global ni Confluencia global.
- `R001-001_Decision_Integracion_Table_Checks.md` (`D-2026-07-05-004`): acepta `R001-TABLE-CHECK-001` como herramienta local no mutante; queda integrada a `06_Automatizacion` y a `DO-LAB-RUN-001`, sin canonizar `Xi`, admitir `H-Xi`, cerrar `P-200` ni resolver `P-107`.
- `HXI-001_Decision_Mantenimiento_Local.md` (`D-2026-07-05-003`): acepta `HXI-MAINT-001`; `HXI-001` queda abierto en mantenimiento local, conserva `Xi_eval` y deja de ser frente activo inmediato.
- `HXI-001_Decision_Resultado_Compuerta_Admision_Formal.md` (`D-2026-07-05-002`): acepta `HXI-GATE-001` con resultado `mantener_Xi_eval`; `H-Xi` no se admite y `Xi_eval` queda conservado solo como herramienta local de expediente.
- `HXI-001_Decision_Reapertura_Operativa.md` (`D-2026-07-05-001`): acepta `HXI-REOPEN-001` y reactiva `HXI-001` como frente activo inmediato para aplicar la compuerta de admision formal posterior; no admite `H-Xi`, no canoniza `Xi`, no reabre `PSI-001` ni autoriza transformaciones.
- `AUT-001_Decision_Refinamiento_Contexto_Guardrails.md` (`D-2026-07-03-020`): acepta `AUT-RISK-REFINE-002` y `AUT-VAL-012` para reclasificar falsos riesgos activos de guardrails como advertencias controladas; no reabre `AUT-001` ni borra hallazgos.
- `TCS-001_Decision_Estatus_Paquete_Minimo.md` (`D-2026-07-03-019`): acepta `TCS-DEF-MIN-001`, `TCS-FAIL-TYP-001` y `TCS-CASE-BAT-001` como paquete teorico minimo provisional; no canoniza `Concordance`, no crea Nivel C y no usa vision papers como fuente activa.
- `AO-001_Decision_Estatus_Puente_Confluencia_Equivalencia.md` (`D-2026-07-03-018`): acepta `AO-PPI-BRIDGE-001`, `AO-PPI-EQ-001` y `AO-PPI-CONF-001` como avance local sobre Confluencia y Equivalencia de proyecciones; no reabre `P-PI.0` / `P-PI.1` ni cierra problemas globales.
- `AO-001_Decision_Criterios_Uso_R4_Gamma_Fuera_AUD.md` (`D-2026-07-03-017`): acepta `AO-R4-GAMMA-USE-001` para usar R4/Gamma fuera de `AUD-001` solo como referencia formal local, prueba local controlada o puente de problema.
- `AO-001_Decision_Estatus_Casos_Prueba_Algebra_Operacional.md` (`D-2026-07-03-016`): acepta `AO-CASE-BAT-001` como bateria minima de casos operacionales para Documento 04.
- `AUT-002_Decision_Referencias_Historicas_Transferidas.md` (`D-2026-07-03-015`): acepta `referencia_historica_transferida` para `PSI-001*` eliminado y refina falsos bloqueos de historial en controles negativos; no restaura la copia local.
- `AO-001_Decision_Estatus_Prueba_Gamma_Externa.md` (`D-2026-07-03-014`): acepta `GAMMA-EXT-AO-001` como prueba positiva externa local de `Gamma_1` dentro de `AO-001`; no promueve `Gamma`, no modifica Documento 04 ni autoriza transformaciones materiales.
- `HB-001_Decision_Congelamiento_Brotes_Alternos.md` (`D-2026-07-03-013`): congela `H-B.6` y `H-B.7` como brotes alternos y originales historicos; dejan de figurar como hipotesis activas.
- `PSI-TRASPASO-001_Decision_Eliminacion_Copia.md` (`D-2026-07-03-012`): elimina la copia local de traspaso `PSI-001*`; psicologia permanece solo en el proyecto independiente `Psicologia Concordante`.
- `DOCS-001_Decision_Consolidacion_Documentos_00-04.md` (`D-2026-07-03-011`): incorpora versiones completas desde fuentes previas a los documentos 00-03 y actualiza el Documento 04 como version inicial consolidada de Algebra Operacional; no modifica `01_Canon`, no promueve R4/Gamma fuera de `AUD-001` y no autoriza transformaciones materiales.
- `AUD-001_Decision_Estatus_R4_Gamma_Formal_Local.md` (`D-2026-07-03-010`): acepta `R4-FORMAL-AUD-001` y `GAMMA-FORMAL-AUD-001` como construcciones formales locales de `AUD-001`, y `VAL-031` como segunda prueba positiva de `Gamma_1`; no promueve Canon, Nivel C ni transformaciones materiales.
- `AO-001_Decision_Estatus_Marco_Inicial_Algebra_Operacional.md` (`D-2026-07-03-009`): acepto `AO-MARCO-001` como marco inicial provisional; su incorporacion inicial al Documento 04 queda decidida posteriormente por `D-2026-07-03-011`.
- `AO-001_Decision_Apertura.md` (`D-2026-07-03-008`): abrio `AO-001` como expediente preparatorio del Documento 04; la reserva del documento quedo superada por `D-2026-07-03-011`.
- `AUD-001_Decision_Estatus_Gamma_Ruta1_Definicion_Local.md` (`D-2026-07-03-007`): `GAMMA-DEF-001` queda aceptada como definicion local provisional de `Gamma` en ruta 1 dentro de `AUD-001`; no construye `Gamma` formal, no modifica `C-001` / `C-002`, no promueve a Canon ni autoriza transformaciones materiales.
- `PSI-001` (`D-2026-07-03-003` a `D-2026-07-03-006`): decisiones historicas agregadas en `DECISIONES.md`; la copia local ya no existe en `03_Expedientes` por `D-2026-07-03-012`.
- `P-PI_Decision_Cierre_Frente_Matematico_Acotado.md` (`D-2026-07-03-002`): `P-PI.0` y `P-PI.1` quedan cerrados como frentes de trabajo; Confluencia y Equivalencia de proyecciones siguen abiertas como problemas de fondo.
- `P-PI_Decision_Reactivacion_Frente_Matematico.md` (`D-2026-07-02-032`): `P-PI.0` queda activo acotado para Equivalencia de proyecciones y `P-PI.1` queda activo acotado para Confluencia; `PPI-MARCO-CORE-001` aceptado como marco provisional sin resolver los problemas.
- `DECISION_Desactivacion_Vision_Papers.md` (`D-2026-07-02-031`): `VISION_PAPER_PROPUESTA.md` y `VISION_PAPER_FINAL_REFERENCIAS.md` quedan inactivos hasta nuevo aviso; no son autoridad ni agenda vigente.
- `HB-001_Decision_Fichas_Alcance_H-B.md` (`D-2026-07-02-030`): `H-B.6` y `H-B.7` quedaron con alcance local minimo aceptado; posteriormente fueron congeladas por `D-2026-07-03-013`.
- `AUT-001_Decision_Cierre_Operativo_Completo.md` (`D-2026-07-02-029`): `AUT-001` cerrado operativamente tras ejecucion directa local de `lab_run.py` en alcance clave; quedan herramientas conservadas y deuda documental visible.
- `AUD-001_Decision_Promocion_SPEC-RFC-AUDITOR-V0.md` (`D-2026-07-02-028`): `SPEC-RFC-AUDITOR-V0` promovida a `C-002_RFC_Operativo_Auditor_v0.md`, documento oficial de Nivel C tipo RFC.
- `AUD-001_Decision_Estatus_Auditor_v0.md` (`D-2026-07-02-027`): Auditor completo en version documental/operativa v0 dentro de `AUD-001`; despues se acepto la implementacion no mutante `AUDITOR-V0-001` y se reactivo JSON.
- `AUD-001_Decision_Estatus_Implementacion_No_Mutante_C002.md`: acepta `auditor_v0.py` como implementacion inicial no mutante de `AUDITOR-V0-001`.
- `AUD-001_Decision_Reactivacion_JSON_Auditor_v0.md`: reactiva la salida JSON y la carga externa `--case-file` para `AUDITOR-V0-001`.
- `AUD-001_Decision_Estatus_REPORT_LAYER_Candidata.md` (`D-2026-07-02-026`): `REPORT-LAYER-CAND-001` aceptada como candidata provisional de expediente; alcance local y puente conceptual cumplidos posteriormente por `ALC-REPORT-LAYER-001`, `COMPAT-RL-DO-CHECK-001`, `VAL-028` y `C-002`.
- `AUD-001_Decision_Reactivacion_REPORT_LAYER.md` (`D-2026-07-02-025`): `AUD-001` reactivado de forma acotada para separar `REPORT_LAYER`.
- `AUD-001_Origen_REPORT_LAYER.md`: mapa provisional de extraccion de `REPORT_LAYER` desde `M-000`, `M-001`, `C-001`, contratos de reportes, validaciones, simulaciones y frontera de permiso; no sale de `Gamma` ni de R4 formal.
- `PSI-001` (`D-2026-07-02-022` a `D-2026-07-02-024`): decisiones historicas previas a la independizacion; sin archivos locales activos despues de `D-2026-07-03-012`.
- `AUT-001_Decision_Cierre_Tecnico_Provisional.md` (`D-2026-07-02-021`): cierre tecnico provisional aceptado; cierre operativo completo cumplido posteriormente por `D-2026-07-02-029`.
- `AUT-001_Decision_Refinamiento_DO-LAB-RISK.md` (`D-2026-07-02-020`): `DO-LAB-RISK-001` refinado; `riesgo_activo` baja a 0 y `advertencia_controlada` queda en 17.
- `AUT-001_Decision_Revision_Riesgos_Activos.md` (`D-2026-07-02-019`): revision provisional de 17 riesgos activos aceptada; no hay transformacion real en curso; `AUT-001` sigue abierto.
- `AUT-001_Decision_Cierre_Riesgos.md`: criterios de cierre de fase media y tratamiento inicial de riesgos altos aceptados; `AUT-001` sigue abierto.
- `AUT-001_Decision_Resumen_Ejecutivo.md`: `DO-LAB-SUMMARY-001` aceptado como resumen ejecutivo automatico provisional; `AUT-001` sigue abierto.
- `AUT-001_Decision_Riesgos_Advertencias.md`: `DO-LAB-RISK-001` aceptado como clasificador provisional de advertencias y riesgos; `AUT-001` sigue abierto.
- `AUT-001_Decision_Comando_Unico_LAB.md`: `DO-LAB-RUN-001` aceptado como comando unico provisional; `AUT-001` sigue abierto.
- `AUT-001_Decision_Continuidad_Laboratorio.md`: `DO-LAB-CONTINUITY-001` aceptado como continuidad integrada provisional; `AUT-001` sigue abierto.
- `AUT-001_Decision_Tablero_Estado.md`: `DO-STATE-BOARD-001` aceptado como tablero de estado provisional no mutante; `AUT-001` sigue abierto.
- `AUT-001_Decision_Reactivacion_Automatizacion.md`: `AUT-001` reactivado como frente activo inmediato.
- `HXI-001_Decision_Mantenimiento_Local.md`: `HXI-001` queda abierto en mantenimiento local y deja de ser frente activo inmediato.
- `HXI-001_Decision_Resultado_Compuerta_Admision_Formal.md`: compuerta aplicada con resultado `mantener_Xi_eval`; `H-Xi` permanece no admitida.
- `HXI-001_Decision_Reapertura_Operativa.md`: `HXI-001` reabierto operativamente como frente activo inmediato, sin admision de `H-Xi`.
- `HXI-001_Decision_Pausa_Operativa.md`: decision historica de pausa operativa, superada como estado vigente por `D-2026-07-05-001`; no admitia `H-Xi`.
- `HXI-001_Decision_Estatus_Reporte_Consistencia.md`: reporte de consistencia de `Xi_eval` aceptado; cumple requisito previo sin admitir `H-Xi`.
- `HXI-001_Decision_Estatus_Criterios_Admision_Formal.md`: criterios de admision formal posterior aceptados como compuerta provisional; no admiten `H-Xi`.
- `HXI-001_Decision_Preparacion_Admision_Formal.md`: ruta 3 preparada de forma condicionada, sin admision formal.
- `HXI-001_Decision_Estatus_Notacion_Minima_Xi-R.md`: notacion minima `Xi-R` aceptada para continuidad acotada de `HXI-001`, sin admitir `H-Xi`.
- `HXI-001_Decision_Ruta_Operativa.md`: ruta 2 elegida, continuidad acotada con notacion minima de expediente.
- `HXI-001_Decision_Estatus_Dictamen_Utilidad_Local.md`: dictamen de utilidad local de `Xi` aceptado como guia operativa provisional; reconoce utilidad acotada, sin admitir `H-Xi`.
- `HXI-001_Decision_Estatus_Matriz_Pruebas.md`: matriz `HXI-R` aceptada como guia operativa provisional; favorece continuidad abierta de `HXI-001`, sin admitir `H-Xi`.
- `HXI-001_Decision_Estatus_Mapa_Preliminar.md`: mapa preliminar `H-Xi` / `R` aceptado como guia operativa de evaluacion, sin admitir `H-Xi`.
- `HXI-001_Decision_Apertura.md`: `HXI-001` abierto como evaluacion separada de `H-Xi` frente a relaciones `R`, sin admitir `H-Xi`.
- `PSI-001` decisiones iniciales: conservadas solo como historia agregada; los archivos locales de traspaso fueron eliminados por `D-2026-07-03-012`.
- `AUT-001_Decision_Fase_Media.md`: `DO-CHECK-MED-001` aceptado como fase media provisional sin cerrar `AUT-001`.
- `REC-001_Decision_Cierre.md`: reconciliacion inicial Canon/baselines cerrada sin modificar Canon ni documentos oficiales.
- `RH-002_Decision_Cierre.md`: lote historico de Descargas procesado y cerrado sin modificar Canon ni documentos oficiales.
- `AUT-001_Decision_Estatus_MVP.md`: automatizacion minima provisional aceptada sin cerrar `AUT-001`.
- `RH-001` queda cerrado como procesamiento de registro historico.
- `P-PI.0` / `P-PI.1` quedan cerrados como frentes de trabajo por `D-2026-07-03-002`; Confluencia y Equivalencia de proyecciones siguen abiertas como problemas de fondo.

Expediente teorico reciente:

- `MOC-001.md`: expediente integrador del Modelo Operativo de Concordancia; abierto por `D-2026-07-05-011` como frente no canonico, no clinico y no regulado.
- `MOC-001_Formalizacion_Xi_eval.md`: `MOC-XI-EVAL-FORMAL-001`, formalizacion local de `Xi_eval` con entradas, salidas, reglas e invariantes; aceptada por `D-2026-07-05-012`.
- `MOC-001_Metricas_Estados.md` y `MOC-001_Protocolo_Evaluacion.md`: `MOC-METRIC-STATE-001` y `MOC-EVAL-PROTO-001`; aceptados por `D-2026-07-05-013`.
- `MOC-001_Casos_No_Clinicos.md`: `MOC-CASE-BAT-001`, bateria sintetica no clinica cubierta por `MOC-EVAL-001`; ampliada por `MOC-ROUTE-002` y aceptada por `D-2026-07-05-018`.
- `MOC-001_Disenio_Estudio_Empirico.md`: `MOC-EMP-STUDY-001`, diseno documental de comparacion futura; aceptado por `D-2026-07-05-015`.
- `MOC-001_Ejecucion_Ruta_Valida_001.md`: `MOC-ROUTE-EXEC-001`, primera ruta valida ejecutada favorablemente; aceptada por `D-2026-07-05-016`.
- `MOC-001_Siguientes_Rutas_Validas.md`: `MOC-NEXT-ROUTES-001`, matriz de rutas posteriores; acepta `MOC-ROUTE-002` como siguiente ruta recomendada por `D-2026-07-05-017`.
- `MOC-001_Ejecucion_Ruta_002.md`: `MOC-ROUTE-002`, ampliacion de bateria sintetica no clinica con desacuerdos justificados y casos limite; aceptada por `D-2026-07-05-018`.
- `MOC-001_Rutas_Posteriores_Ruta_002.md`: `MOC-NEXT-ROUTES-002`, matriz posterior que recomienda `MOC-ROUTE-003` como puente formal `MOC/TCS`; aceptada por `D-2026-07-05-019`.
- `MOC-001_Puente_Formal_MOC_TCS.md`: `MOC-TCS-BRIDGE-001`, formalizacion ejecutable local de operadores `MOC/TCS`; aceptada por `D-2026-07-05-020`.
- `MOC-001_Rutas_Posteriores_Ruta_003.md`: `MOC-NEXT-ROUTES-003`, matriz posterior que recomienda `MOC-ROUTE-004` como puente formal `MOC/AO`; aceptada por `D-2026-07-05-021`.
- `MOC-001_Puente_Formal_MOC_AO.md`: `MOC-AO-BRIDGE-001`, formalizacion local del puente `MOC/AO` desde `operator_trace`, `Pi_moc_trace` y `ao_bridge`; aceptada por `D-2026-07-05-022`.
- `MOC-001_Rutas_Posteriores_Ruta_004.md`: `MOC-NEXT-ROUTES-004`, matriz posterior que recomienda `MOC-ROUTE-005` como refinamiento del protocolo de evaluadores; aceptada por `D-2026-07-05-023`.
- `MOC-001_Protocolo_Evaluacion_v0_2.md`: `MOC-EVAL-PROTO-002`, protocolo v0.2 con ejes de desacuerdo, regla de desempate y tratamiento por caso; aceptado por `D-2026-07-05-024`.
- `MOC-001_Ejecucion_Ruta_005.md`: `MOC-ROUTE-005`, refinamiento de protocolo ejecutado favorablemente; aceptado por `D-2026-07-05-024`.
- `MOC-001_Rutas_Posteriores_Ruta_005.md`: `MOC-NEXT-ROUTES-005`, matriz posterior que recomienda `MOC-ROUTE-006`; aceptada por `D-2026-07-05-025`.
- `MOC-001_Protocolo_Piloto_Empirico_Futuro.md`: `MOC-EMP-PILOT-PROTO-001`, protocolo documental de piloto empirico futuro preparado sin ejecucion real; aceptado por `D-2026-07-06-001`.
- `MOC-001_Rutas_Posteriores_Ruta_006.md`: `MOC-NEXT-ROUTES-006`, matriz posterior que recomienda `MOC-ROUTE-007`; aceptada por `D-2026-07-06-002`.
- `MOC-001_Compuerta_Autorizacion_Ejecucion_Piloto.md`: `MOC-GATE-PILOT-EXEC-001`, compuerta aplicada con resultado `no_autorizar_ejecucion`; aceptada por `D-2026-07-06-003`.
- `MOC-001_Semantica_Provisional.md`: `MOC-SEM-PROV-001`, propuesta semantica local provisional del MOC; aceptada por `D-2026-07-06-004`.
- `MOC-001_Tabla_Operaciones_Formales.md`: `MOC-OPS-FORMAL-001`, tabla de operaciones formales locales; aceptada por `D-2026-07-06-004`.
- `MOC-001_Casos_Congelados_Piloto.md`: `MOC-PILOT-CASE-FREEZE-001`, paquete congelado de 11 casos sinteticos; aceptado por `D-2026-07-06-004`.
- `MOC-001_Plantilla_Respuesta_Evaluadores.md`: `MOC-PILOT-RESPONSE-TPL-001`, plantilla documental sin datos personales; aceptada por `D-2026-07-06-004`.
- `MOC-001_Reglas_Protocolo_Congelados.md`: `MOC-PILOT-RULE-FREEZE-001`, version congelada de reglas/protocolo; aceptada por `D-2026-07-06-004`.
- `MOC-001_Paquete_PreEjecucion_Piloto.md`: `MOC-PREEXEC-PACK-001`, paquete documental pre-ejecucion; aceptado por `D-2026-07-06-004`.
- `MOC-001_Metodo_Registro_Sin_Datos_Personales.md`: `MOC-PILOT-NODATA-REG-001`, metodo documental de registro sin datos personales; aceptado por `D-2026-07-06-005`.
- `MOC-001_Matriz_Auditoria_Piloto.md`: `MOC-PILOT-AUDIT-MATRIX-001`, matriz documental de auditoria de piloto; aceptada por `D-2026-07-06-005`.
- `MOC-001_Paquete_Registro_Auditoria_Piloto.md`: `MOC-PILOT-REG-AUDIT-PACK-001`, paquete documental de registro y auditoria; aceptado por `D-2026-07-06-005`.
- `TCS-001_Teoria_Concordante_de_Sistemas.md`: propuesta teorica inicial para tratar `Concordance` como propiedad auditable de gobernanza de sistemas, no canonizada.
- `TCS-001_Analisis_Fondo.md`: analisis provisional de fondo; recomienda mantener `TCS-001` abierto y desarrollar definiciones minimas, tipologia de fallos y casos de prueba.
- `TCS-001_Definiciones_Minimas.md`, `TCS-001_Tipologia_Fallos_Concordancia.md` y `TCS-001_Casos_Prueba.md`: paquete minimo provisional aceptado por `D-2026-07-03-019`; no canonico.
- `TCS-001_Maduracion_Provisional.md`: `TCS-MAT-PROV-001`, metrica cualitativa, casos externos no regulados y conflicto de autoridades; aceptado por `D-2026-07-05-010`; no canonico.

Expediente preparatorio reciente:

- `AO-001.md`: expediente preparatorio de la futura Algebra Operacional.
- `AO-001_Marco_Inicial_Algebra_Operacional.md`: `AO-MARCO-001`, marco inicial provisional aceptado e incorporado al Documento 04 por `D-2026-07-03-011`; `AO-001` sigue abierto para formalizacion posterior y pruebas globales no resueltas.
- `AO-001_Prueba_Gamma_Externa.md`: `GAMMA-EXT-AO-001`, primera prueba positiva externa local de `Gamma_1`, aceptada por `D-2026-07-03-014`.
- `AO-001_Casos_Prueba_Algebra_Operacional.md`: `AO-CASE-BAT-001`, bateria minima aceptada por `D-2026-07-03-016`.
- `AO-001_Criterios_Uso_R4_Gamma_Fuera_AUD.md`: `AO-R4-GAMMA-USE-001`, criterios aceptados por `D-2026-07-03-017`.
- `AO-001_Puente_Confluencia_Equivalencia.md`: `AO-PPI-BRIDGE-001`, avance local aceptado por `D-2026-07-03-018`.
- `AO-001_Evaluacion_Formalizacion_Doc04_R001_TB.md`: `AO-DOC04-FORM-CHK-001`, evalua `R001-TB-001` como candidata futura para Documento 04; no modifica el documento oficial.
- `AO-001_Opciones_Prueba_Confluencia_Externa.md`: `AO-CONF-EXT-OPTIONS-001`, define opciones externas no reguladas; `EXT-CONF-001` queda ejecutada despues por `D-2026-07-05-007`.
- `AO-001_Pruebas_Externas_Confluencia.md`: `AO-EXT-CONF-EXEC-001`, ejecuta `EXT-CONF-001` y agrega `EXT-CONF-002`; aceptado por `D-2026-07-05-007`.
- `AO-001_Formalizacion_Acotada_Doc04_R001_TB.md`: `AO-DOC04-FORM-001`, incorpora `Pi_tb` / `Eq_tb` al Documento 04 en grado acotado; aceptado por `D-2026-07-05-008`.
- `AO-001_Compuerta_Exportacion_R4_Gamma.md`: `AO-R4-GAMMA-EXPORT-GATE-001`, bloquea exportacion general y conserva perfil restringido interoperable; aceptado por `D-2026-07-05-009`.

Expediente tecnico reciente:

- `R001-001_Integracion_Table_Checks.md`: `R001-TABLE-CHECK-001`, bateria local de 20 chequeos tabulares `R-001` / `Xi`, aceptada por `D-2026-07-05-004` como herramienta no mutante.
- `R001-001_Relacion_Formal_AO.md`: `R001-TB-001`, relacion formal local entre los chequeos tabulares y `AO-PPI-BRIDGE-001`, aceptada por `D-2026-07-05-005`.
- `R001-001_Auditoria_Integracion_Table_Checks.md`: auditoria favorable con limites; no canoniza `Xi`, no admite `H-Xi`, no cierra `P-200` ni resuelve `P-107`.
- `R001-001_Auditoria_Relacion_Formal_AO.md`: auditoria favorable de `R001-TB-001`.

Propuesta provisional promovida:

- `DO-PROP-001` en `03_Expedientes/DO-001.md`, absorbida por `C-001`.

Auditoria provisional registrada:

- `MOC-001_Auditoria_Apertura.md`.
- `MOC-001_Auditoria_Formalizacion_Xi_eval.md`.
- `MOC-001_Auditoria_Metricas_Protocolo.md`.
- `MOC-001_Auditoria_Simulacion_Software.md`.
- `MOC-001_Auditoria_Disenio_Estudio_Empirico.md`.
- `MOC-001_Auditoria_Ejecucion_Ruta_Valida_001.md`.
- `MOC-001_Auditoria_Siguientes_Rutas_Validas.md`.
- `MOC-001_Auditoria_Ejecucion_Ruta_002.md`.
- `MOC-001_Auditoria_Rutas_Posteriores_Ruta_002.md`.
- `MOC-001_Auditoria_Puente_Formal_MOC_TCS.md`.
- `MOC-001_Auditoria_Rutas_Posteriores_Ruta_003.md`.
- `AO-001_Auditoria_Pruebas_Externas_Confluencia.md`.
- `AO-001_Auditoria_Formalizacion_Acotada_Doc04.md`.
- `AO-001_Auditoria_Compuerta_Exportacion_R4_Gamma.md`.
- `AO-001_Auditoria_Formalizacion_Doc04_Confluencia_Externa.md`.
- `R001-001_Auditoria_Integracion_Table_Checks.md`.
- `R001-001_Auditoria_Relacion_Formal_AO.md`.
- `TCS-001_Auditoria_Maduracion_Provisional.md`.
- `TCS-001_Auditoria_Paquete_Minimo.md`.
- `AO-001_Auditoria_Puente_Confluencia_Equivalencia.md`.
- `AO-001_Auditoria_Criterios_Uso_R4_Gamma_Fuera_AUD.md`.
- `AO-001_Auditoria_Casos_Prueba_Algebra_Operacional.md`.
- `AUT-002_Auditoria_Referencias_Historicas_Transferidas.md`.
- `DOCS-001_Auditoria_Consolidacion_Documentos_00-04.md`.
- `AUD-001_Auditoria_R4_Gamma_Formal_Local.md`.
- `AO-001_Auditoria_Prueba_Gamma_Externa.md`.
- `AO-001_Auditoria_Marco_Inicial_Algebra_Operacional.md`.
- `AUD-001_Auditoria_Gamma_Ruta1_Definicion_Local.md`.
- `AUD-001_Auditoria_SPEC-RFC-AUDITOR-V0_NIVEL-C.md`.
- `AUD-001_Auditoria_Completitud_Auditor_v0.md`.
- `AUD-001_Auditoria_REPORT_LAYER_Candidata.md`.
- `RH-001_Auditoria_Procesamiento.md`.
- `RH-002_Auditoria_Procesamiento.md`.
- `REC-001_Auditoria_Reconciliacion.md`.
- Auditorias `PSI-001`: transferidas fuera del Laboratorio; los archivos locales fueron eliminados por `D-2026-07-03-012`.
- `HXI-001_Auditoria_Apertura.md`.
- `HXI-001_Auditoria_Mapa_Preliminar.md`.
- `HXI-001_Auditoria_Matriz_Pruebas.md`.
- `HXI-001_Auditoria_Dictamen_Utilidad_Local.md`.
- `HXI-001_Auditoria_Notacion_Minima_Xi-R.md`.
- `HXI-001_Auditoria_Criterios_Admision_Formal.md`.
- `HXI-001_Auditoria_Reporte_Consistencia.md`.
- `HXI-001_Auditoria_Reapertura_Operativa.md`.
- `HXI-001_Auditoria_Compuerta_Admision_Formal.md`.
- `HXI-001_Auditoria_Mantenimiento_Local.md`.
- `AUT-001_Validacion_DO-STATE-BOARD.md`.
- `P-PI_Auditoria_Marco_Inicial_Confluencia_Equivalencia.md`.
- `P-PI_Auditoria_Criterios_Cierre.md`.
- `DO-001_Auditoria_DO-PROP-001.md`.
- `DO-001_Auditoria_SPEC-AUD-001_NIVEL-C.md`.

Validacion provisional registrada:

- `MOC-EVAL-001`: simulacion no mutante de `MOC-001`; 11 casos sinteticos no clinicos, salidas `redundante`, `util_acotado`, `limitado`, `no_comparable` y `bloqueado`, estados MOC completos y tres evaluadores simulados por caso; incluye `operator_trace`, `Pi_moc_trace`, `ao_bridge`, `protocol_v02`, 2 desacuerdos justificados y no admite `H-Xi`, no canoniza `Xi`, no abre uso clinico y no cierra problemas globales.
- `MOC-ROUTE-006`: protocolo documental de piloto empirico futuro preparado; no ejecuta piloto, no recluta evaluadores, no usa personas reales, no recopila datos personales y no abre uso clinico.
- `MOC-ROUTE-007`: compuerta aplicada; el piloto empirico real no queda autorizado. Se permite solo preparar paquete documental pre-ejecucion sin reclutamiento, respuestas reales ni datos personales.
- `MOC-ROUTE-008`: paquete documental pre-ejecucion preparado; casos, plantilla y reglas/protocolo quedan congelados documentalmente. El piloto real sigue bloqueado.
- `MOC-ROUTE-009`: paquete documental de registro y auditoria preparado; metodo sin datos personales y matriz de auditoria quedan listos. El piloto real sigue bloqueado.
- `MOC-ROUTE-005`: protocolo v0.2 aceptado; distingue ejes de desacuerdo, regla de desempate, tratamiento local y revision si el desacuerdo se repite, sin canonizar ni abrir estudio empirico real.
- `MOC-ROUTE-004`: puente formal `MOC/AO` aceptado; `ao_bridge` proyecta el rastro ganador hacia roles locales de AO sin cerrar Confluencia global, Equivalencia global ni modificar `Documento 04`.
- `MOC-ROUTE-003`: puente formal `MOC/TCS` aceptado; define `OP_MOC_XI`, `OP_MOC_TCS`, `OP_MOC_STATE` y `OP_MOC_AGREEMENT` con prioridad, conflicto, salida unica y traza auditable.
- `MOC-ROUTE-002`: bateria ampliada ejecutada; `MOC-EVAL-001` 11/11, protocolo con 6 coincidencias exactas, 3 parciales y 2 desacuerdos justificados, `DO-LAB-RUN-001` con `MOC-EVAL-001: ok` y `risk_blocks_closure: false`.
- `MOC-ROUTE-EXEC-001`: primera ruta valida ejecutada; `MOC-EVAL-001` 7/7, protocolo con 4 coincidencias exactas y 3 parciales, `DO-LAB-RUN-001` con `MOC-EVAL-001: ok` y `risk_blocks_closure: false`.
- `AO-EXT-CONF-EXEC-001`: `EXT-CONF-001` y `EXT-CONF-002` ejecutados por `AO-EXT-CONF-001`; 7 casos, 7 aprobados, 0 fallos; deudas globales conservadas abiertas.
- `AO-DOC04-FORM-001`: `Pi_tb` / `Eq_tb` queda incorporado al Documento 04 en grado acotado bajo testigo; no cierra `P-200`, `P-107`, Confluencia global ni Equivalencia global.
- `AO-R4-GAMMA-EXPORT-GATE-001`: exportacion general de R4/Gamma bloqueada; perfil restringido interoperable aceptado como avance local.
- `TCS-MAT-PROV-001`: maduracion provisional de `TCS-001` con metrica cualitativa, casos externos no regulados y conflicto de autoridades.
- `AO-DOC04-FORM-CHK-001`: `R001-TB-001` queda madura como candidata formal de expediente para Documento 04; su incorporacion acotada se ejecuta despues por `D-2026-07-05-008`.
- `AO-CONF-EXT-OPTIONS-001`: las pruebas externas candidatas quedan acotadas a dominios sinteticos no regulados; `EXT-CONF-001` fue la primera prueba ejecutada y `EXT-CONF-002` la segunda agregada.
- `R001-TABLE-CHECK-001`: 20 chequeos tabulares locales, 20 aprobados y 0 fallos; no mutante, sin promocion de `Xi`.
- `R001-TB-001`: `Pi_tb(C, O_adm)` y `Eq_tb(C1, C2, O_adm)` como instancia local de `Pi_op`, `AO-PPI-EQ-001` y `AO-PPI-CONF-001`; no demuestra equivalencia o confluencia global.
- `AO-PPI-EQ-001`: equivalencia local entre proyeccion documental, proyeccion de reporte y proyeccion operacional bajo `G_AO_OP-GOV-001`; no demuestra equivalencia global.
- `AO-PPI-CONF-001`: confluencia local entre ruta de estado, decision y reporte; no demuestra confluencia global.
- `AO-CASE-001` a `AO-CASE-006`: casos minimos de Algebra Operacional aceptados como `AO-CASE-BAT-001`.
- `GAMMA-EXT-AO-001` en `03_Expedientes/AO-001_Prueba_Gamma_Externa.md`: prueba positiva externa local de `Gamma_1`; produce `G_AO_OP-GOV-001` como criterio formal local de expediente dentro de `AO-001`.
- `VAL-031` en `03_Expedientes/AUD-001_Validaciones.md`: segunda prueba positiva de `Gamma_1` con `REPORT_LAYER` / `DO_CHECK_REPORT`; produce `G_REPORT_READ-FORMAL-001` como criterio formal local no mutante.
- `VAL-030` en `03_Expedientes/AUD-001_Validaciones.md`: valida `Gamma_1` contra `AUD-SIM-030` como primer caso positivo acotado; no construye `Gamma` formal ni R4 formal.
- `P-PI_PPI-CONF-001_Rutas_Estado_Operativo.md`: confluencia local de continuidad operativa entre ruta de expedientes y ruta de estado bajo contexto `C_PPI_CONTINUIDAD_OPERATIVA`; no demuestra confluencia formal global.
- `P-PI_PPI-EQ-002_Completitud_A_C002.md`: equivalencia documental-operativa entre completitud v0 del Auditor y `C-002` bajo contexto `C_AUD_RFC_OPERATIVO`; no demuestra equivalencia formal total.
- `P-PI_PPI-EQ-001_REPORT_LAYER_DO_CHECK.md`: equivalencia minima `REPORT_LAYER` / `DO_CHECK_REPORT` bajo contexto `C_AUD_LECTURA_MIN`; no demuestra equivalencia fuerte de trazabilidad.
- `AUD-001_Validaciones_SPEC-RFC-AUDITOR-V0.md`.
- `AUD-001_Validacion_Implementacion_No_Mutante_C002.md`.
- `DO-001_Validaciones_DO-CHECK-001.md`.
- `DO-001_Validaciones_PERMISO-ACT-001.md`.
- `DO-001_Validaciones_MODO-AUD-001.md`.
- `DO-001_Validaciones_SPEC-AUD-001.md`.
- `DO-001_Validaciones_NIVEL-C-001.md`.
- `AUT-001_Validacion_DO-CHECK-MIN.md`.
- `AUT-001_Validacion_DO-CHECK-MED.md`.
- `AUT-001_Validacion_DO-STATE-BOARD.md`.
- `AUT-001_Validacion_DO-LAB-CONTINUITY.md`.
- `AUT-001_Validacion_DO-LAB-RUN.md`.
- `AUT-001_Validacion_DO-LAB-RISK.md`.
- `AUT-001_Validacion_DO-LAB-SUMMARY.md`.
- `AUT-001_Validacion_Cierre_Riesgos.md`.
- `AUT-001_Validacion_Revision_Riesgos_Activos.md`.
- `AUT-001_Validacion_Refinamiento_DO-LAB-RISK.md`.
- `AUT-001_Validacion_Refinamiento_Contexto_Guardrails.md`.
- `AUT-001_Validacion_Cierre_Tecnico_Provisional.md`.
- `AUT-001_Validacion_Cierre_Operativo_Completo.md`.

Decision provisional registrada:

- `MOC-001_Decision_Paquete_Registro_Auditoria_Piloto.md`: acepta `MOC-PILOT-REG-AUDIT-PACK-001` y recomienda `MOC-ROUTE-010`.
- `MOC-001_Decision_Paquete_PreEjecucion_Piloto.md`: acepta `MOC-PREEXEC-PACK-001` y recomienda `MOC-ROUTE-009`.
- `MOC-001_Decision_Compuerta_Autorizacion_Ejecucion_Piloto.md`: acepta `MOC-GATE-PILOT-EXEC-001`, no autoriza ejecucion y recomienda `MOC-ROUTE-008`.
- `MOC-001_Decision_Rutas_Posteriores_Ruta_006.md`: acepta `MOC-NEXT-ROUTES-006` y recomienda `MOC-ROUTE-007`.
- `MOC-001_Decision_Protocolo_Piloto_Empirico_Futuro.md`: acepta `MOC-EMP-PILOT-PROTO-001` sin ejecucion real.
- `MOC-001_Decision_Rutas_Posteriores_Ruta_005.md`: acepta `MOC-NEXT-ROUTES-005` y recomienda `MOC-ROUTE-006`.
- `MOC-001_Decision_Ejecucion_Ruta_005.md`: acepta `MOC-ROUTE-005` y `MOC-EVAL-PROTO-002`.
- `MOC-001_Decision_Rutas_Posteriores_Ruta_004.md`: acepta `MOC-NEXT-ROUTES-004` y recomienda `MOC-ROUTE-005`.
- `MOC-001_Decision_Puente_Formal_MOC_AO.md`: acepta `MOC-AO-BRIDGE-001` como formalizacion local de puente `MOC/AO`.
- `MOC-001_Decision_Rutas_Posteriores_Ruta_003.md`: acepta `MOC-NEXT-ROUTES-003` y recomienda `MOC-ROUTE-004`.
- `MOC-001_Decision_Puente_Formal_MOC_TCS.md`: acepta `MOC-TCS-BRIDGE-001` como formalizacion ejecutable local.
- `MOC-001_Decision_Rutas_Posteriores_Ruta_002.md`: acepta `MOC-NEXT-ROUTES-002` y recomienda `MOC-ROUTE-003`.
- `MOC-001_Decision_Ejecucion_Ruta_002.md`: acepta `MOC-ROUTE-002` como ampliacion favorable de bateria sintetica no clinica.
- `MOC-001_Decision_Disenio_Estudio_Empirico.md`: acepta `MOC-EMP-STUDY-001`; no ejecuta estudio empirico real ni canoniza el MOC.
- `MOC-001_Decision_Ejecucion_Ruta_Valida_001.md`: acepta `MOC-ROUTE-EXEC-001` como primera ruta valida ejecutada favorablemente.
- `MOC-001_Decision_Siguientes_Rutas_Validas.md`: acepta `MOC-NEXT-ROUTES-001` y recomienda `MOC-ROUTE-002`.
- `MOC-001_Decision_Simulacion_Software.md`: acepta `MOC-EVAL-001` como simulador no mutante de `MOC-001`.
- `MOC-001_Decision_Metricas_Protocolo.md`: acepta `MOC-METRIC-STATE-001` y `MOC-EVAL-PROTO-001`.
- `MOC-001_Decision_Formalizacion_Xi_eval.md`: acepta `MOC-XI-EVAL-FORMAL-001` solo como formalizacion local.
- `MOC-001_Decision_Apertura.md`: abre `MOC-001` como expediente integrador provisional.
- `TCS-001_Decision_Maduracion_Provisional.md`: acepta `TCS-MAT-PROV-001`; no cierra la deuda de maduracion de TCS.
- `AO-001_Decision_Compuerta_Exportacion_R4_Gamma.md`: bloquea exportacion general de R4/Gamma y acepta perfil restringido interoperable.
- `AO-001_Decision_Formalizacion_Acotada_Doc04.md`: incorpora `Pi_tb` / `Eq_tb` al Documento 04 solo en grado acotado bajo testigo.
- `AO-001_Decision_Estatus_Pruebas_Externas_Confluencia.md`: acepta `AO-EXT-CONF-EXEC-001` como validacion ejecutada; no cierra problemas globales.
- `AO-001_Decision_Ruta_Formalizacion_Doc04_Confluencia_Externa.md`: acepta la ruta defensiva para formalizacion futura de Documento 04 y pruebas externas de Confluencia; queda continuada por `D-2026-07-05-008`.
- `R001-001_Decision_Integracion_Table_Checks.md`: acepta `R001-TABLE-CHECK-001` como herramienta local no mutante integrada a `DO-LAB-RUN-001`.
- `R001-001_Decision_Relacion_Formal_AO.md`: acepta `R001-TB-001` como relacion formal local con `AO-PPI-BRIDGE-001`.
- `AO-001_Decision_Estatus_Prueba_Gamma_Externa.md`: acepta `GAMMA-EXT-AO-001` como prueba positiva externa local de `Gamma_1`.
- `HB-001_Decision_Congelamiento_Brotes_Alternos.md`: congela `H-B.6` y `H-B.7` como brotes alternos y originales historicos.
- `PSI-TRASPASO-001_Decision_Eliminacion_Copia.md`: elimina la copia local de traspaso `PSI-001*`.
- `DOCS-001_Decision_Consolidacion_Documentos_00-04.md`: incorpora documentos 00-03 desde fuentes previas y actualiza el Documento 04.
- `AUD-001_Decision_Estatus_R4_Gamma_Formal_Local.md`: acepta `R4-FORMAL-AUD-001`, `GAMMA-FORMAL-AUD-001` y `VAL-031` como artefactos locales de `AUD-001`.
- `AO-001_Decision_Estatus_Marco_Inicial_Algebra_Operacional.md`: acepta `AO-MARCO-001` como marco inicial provisional de Algebra Operacional.
- `AO-001_Decision_Apertura.md`: abre `AO-001` como expediente preparatorio del Documento 04; superada en su reserva documental por `D-2026-07-03-011`.
- `AUD-001_Decision_Estatus_Gamma_Ruta1_Definicion_Local.md`: acepta `GAMMA-DEF-001` como definicion local provisional de `Gamma` en ruta 1; no cierra `Gamma` formal ni autoriza promocion.
- `P-PI_Decision_Reactivacion_Frente_Matematico.md`: reactiva `P-PI.0` / `P-PI.1` de forma acotada para Equivalencia de proyecciones y Confluencia.
- `DECISION_Desactivacion_Vision_Papers.md`: desactiva ambos vision papers hasta nuevo aviso.
- `AUD-001_Decision_Promocion_SPEC-RFC-AUDITOR-V0.md`.
- `AUD-001_Decision_Estatus_Auditor_v0.md`.
- `AUD-001_Decision_Estatus_Implementacion_No_Mutante_C002.md`.
- `AUD-001_Decision_Estatus_REPORT_LAYER_Candidata.md`.
- `AUD-001_Decision_Reactivacion_REPORT_LAYER.md`.
- `AUD-001_Decision_Reactivacion_JSON_Auditor_v0.md`.
- `RH-001_Decision_Cierre.md`.
- `RH-002_Decision_Cierre.md`.
- `REC-001_Decision_Cierre.md`.
- `P-PI_Decision_Ruta_Operativa.md`: decision previa de pausa operativa; superada operativamente por `D-2026-07-02-032` solo para trabajo acotado.
- `P-PI_Decision_Estatus_Criterios_Cierre.md`.
- `DO-001_Decision_DO-CHECK-REPORT.md`.
- `DO-001_Decision_Modo_Operativo_Auditor.md`.
- `DO-001_Decision_Alcance_SPEC-AUD-001.md`.
- `DO-001_Decision_Promocion_SPEC-AUD-001.md`.
- `DO-001_Decision_Cierre_DO-001.md`.
- `AUT-001_Decision_Estatus_MVP.md`.
- `AUT-001_Decision_Fase_Media.md`.
- Decisiones `PSI-001` iniciales: conservadas solo en historia agregada; archivos locales eliminados por `D-2026-07-03-012`.
- `HXI-001_Decision_Apertura.md`.
- `HXI-001_Decision_Estatus_Mapa_Preliminar.md`.
- `HXI-001_Decision_Estatus_Matriz_Pruebas.md`.
- `HXI-001_Decision_Estatus_Dictamen_Utilidad_Local.md`.
- `HXI-001_Decision_Ruta_Operativa.md`.
- `HXI-001_Decision_Estatus_Notacion_Minima_Xi-R.md`.
- `HXI-001_Decision_Preparacion_Admision_Formal.md`.
- `HXI-001_Decision_Estatus_Criterios_Admision_Formal.md`.
- `HXI-001_Decision_Estatus_Reporte_Consistencia.md`.
- `HXI-001_Decision_Pausa_Operativa.md`.
- `HXI-001_Decision_Reapertura_Operativa.md`.
- `HXI-001_Decision_Resultado_Compuerta_Admision_Formal.md`.
- `HXI-001_Decision_Mantenimiento_Local.md`.
- `AUT-001_Decision_Reactivacion_Automatizacion.md`.
- `AUT-001_Decision_Tablero_Estado.md`.
- `AUT-001_Decision_Continuidad_Laboratorio.md`.
- `AUT-001_Decision_Comando_Unico_LAB.md`.
- `AUT-001_Decision_Riesgos_Advertencias.md`.
- `AUT-001_Decision_Resumen_Ejecutivo.md`.
- `AUT-001_Decision_Cierre_Riesgos.md`.
- `AUT-001_Decision_Revision_Riesgos_Activos.md`.
- `AUT-001_Decision_Refinamiento_DO-LAB-RISK.md`.
- `AUT-001_Decision_Cierre_Tecnico_Provisional.md`.
- `AUT-001_Decision_Cierre_Operativo_Completo.md`.
- `HB-001_Decision_Fichas_Alcance_H-B.md`.
- Decisiones `PSI-001` de continuidad, frontera e independizacion: conservadas solo en `DECISIONES.md`; copia local eliminada por `D-2026-07-03-012`.

Regla provisional registrada:

- `DO-001_Regla_Permiso_Actualizacion.md`.

Definicion local registrada:

- `GAMMA-DEF-001` en `03_Expedientes/AUD-001_Gamma_Ruta1_Definicion_Local.md`, vigente solo dentro de `AUD-001` como definicion provisional de ruta 1; primer caso positivo validado por `VAL-030`.
- `NIVEL-C-001` en `05_Estado_Proyecto/NIVEL_C_ESPECIFICACIONES.md`.

Construccion formal local registrada:

- `R4-FORMAL-AUD-001` en `03_Expedientes/AUD-001_R4_Formal_Local.md`, vigente solo dentro de `AUD-001`.
- `GAMMA-FORMAL-AUD-001` en `03_Expedientes/AUD-001_Gamma_Formal_Local.md`, vigente solo dentro de `AUD-001`.

Relacion provisional registrada:

- `REL-GAMMA-R4-001` en `03_Expedientes/AUD-001_Relacion_Gamma_Ruta1_R4_Formal.md`: precisa que `R4-CANDIDATA` puede ser evidencia local para `Gamma_1`, pero no equivale a Regla R4 formal.

Criterio de evaluacion registrado:

- `HXI-001_Criterios_Evaluacion.md`, vigente solo dentro de `HXI-001`.

Criterio local registrado:

- Sin criterio local PSI activo dentro del Laboratorio; `PSI-001` fue transferido y su copia local eliminada.

Ejemplos conceptuales registrados:

- Sin ejemplos PSI activos dentro del Laboratorio; `PSI-001` fue transferido y su copia local eliminada.

Casos conceptuales de transformacion registrados:

- Sin casos PSI activos dentro del Laboratorio.

Matriz de patrones PSI registrada:

- Sin matriz PSI activa dentro del Laboratorio.

Compuerta de frontera PSI registrada:

- Sin compuerta PSI activa dentro del Laboratorio.

Casos de frontera PSI registrados:

- Sin casos de frontera PSI activos dentro del Laboratorio.

Matriz de frontera PSI registrada:

- Sin matriz de frontera PSI activa dentro del Laboratorio.

Mapa de continuidad PSI registrado:

- Sin mapa PSI activo dentro del Laboratorio.

Mapa preliminar registrado:

- `HXI-001_Mapa_Preliminar_PSI-R.md`, mapa preliminar operativo no admisorio entre `H-Xi` y relaciones `R`.

Matriz HXI-R registrada:

- `HXI-001_Matriz_Pruebas_HXI-R.md`, matriz provisional operativa historicamente construida sobre ejemplos PSI transferidos; aceptada sin admision de `H-Xi`.

Dictamen local registrado:

- `HXI-001_Dictamen_Utilidad_Local_Xi.md`, dictamen provisional operativo: `Xi` tiene utilidad local acotada en reorganizacion relacional estable; no admite `H-Xi`.

Ruta operativa HXI registrada:

- `HXI-001_Decision_Ruta_Operativa.md`, ruta 2: continuidad acotada con notacion minima de expediente.

Notacion minima registrada:

- `HXI-001_Notacion_Minima_Xi-R.md`, notacion provisional operativa para `Xi_eval(R0, R1)` y salidas `redundante`, `util_acotado`, `limitado`, `no_comparable` y `bloqueado`.

Preparacion de admision formal registrada:

- `HXI-001_Decision_Preparacion_Admision_Formal.md`, preparacion condicionada de ruta 3; no admite `H-Xi`.
- `HXI-001_Criterios_Admision_Formal_H-Xi.md`, compuerta provisional para admision formal posterior; aceptada sin admision.

Reporte de consistencia registrado:

- `HXI-001_Reporte_Consistencia_Notacion_Xi-R.md`, reporte favorable: `Xi_eval` emite `redundante`, `util_acotado`, `limitado`, `no_comparable` y `bloqueado` segun la matriz.

Reapertura operativa HXI registrada:

- `HXI-001_Reapertura_Operativa.md`, `HXI-REOPEN-001`: reabre `HXI-001` como frente activo inmediato para aplicar la compuerta de admision formal posterior; no admite `H-Xi` ni reabre `PSI-001`.

Compuerta HXI aplicada:

- `HXI-001_Evaluacion_Compuerta_Admision_Formal.md`, `HXI-GATE-001`: aplica la compuerta con resultado `mantener_Xi_eval`; conserva `Xi_eval` como herramienta local y mantiene `H-Xi` como hipotesis externa no admitida.

Mantenimiento local HXI registrado:

- `HXI-001_Mantenimiento_Local.md`, `HXI-MAINT-001`: mantiene `HXI-001` abierto en mantenimiento local; conserva `Xi_eval`, no admite `H-Xi` y retira el expediente del frente activo inmediato.

Especificacion candidata de expediente registrada:

- `SPEC-RFC-AUDITOR-V0` en `03_Expedientes/AUD-001_SPEC-RFC-AUDITOR-V0_Candidata.md`, promovida a `C-002`.
- `REPORT-LAYER-CAND-001` en `03_Expedientes/AUD-001_REPORT_LAYER_Candidata.md`, aceptada como candidata provisional dentro de `AUD-001`; no es Canon, documento oficial ni Nivel C.
- `ALC-HB6-001` en `03_Expedientes/HB-001_Ficha_Alcance_H-B.6.md`, ficha historica congelada de `H-B.6`.
- `ALC-HB7-001` en `03_Expedientes/HB-001_Ficha_Alcance_H-B.7.md`, ficha historica congelada de `H-B.7`.

Algoritmo provisional activo:

- `MOC-EVAL-001` en `06_Automatizacion/moc_eval.py`.
- `R001-TABLE-CHECK-001` en `06_Automatizacion/r001_table_checks.py`.
- `R001-TB-001` en `03_Expedientes/R001-001_Relacion_Formal_AO.md`.
- `DO-CHECK-001` en `03_Expedientes/DO-001_DO-CHECK-001.md`.
- `DO-CHECK-MIN-001` en `06_Automatizacion/do_check_min.py`.
- `DO-CHECK-MED-001` en `06_Automatizacion/do_check_med.py`.
- `DO-STATE-BOARD-001` en `06_Automatizacion/lab_status_board.py`.
- `DO-LAB-CONTINUITY-001` en `06_Automatizacion/lab_continuity_report.py`.
- `DO-LAB-RISK-001` en `06_Automatizacion/lab_risk_classifier.py`.
- `DO-LAB-SUMMARY-001` en `06_Automatizacion/lab_executive_summary.py`.
- `AUT-CLOSE-CRIT-001` en `03_Expedientes/AUT-001_Criterios_Cierre_Fase_Media.md`.
- `AUT-RISK-TREAT-001` en `03_Expedientes/AUT-001_Tratamiento_Riesgos_Altos.md`.
- `AUT-RISK-ACT-REVIEW-001` en `03_Expedientes/AUT-001_Matriz_Revision_Riesgos_Activos.md`.
- `AUT-RISK-REFINE-001` en `03_Expedientes/AUT-001_Refinamiento_DO-LAB-RISK.md`.
- `AUT-RISK-REFINE-002` en `03_Expedientes/AUT-001_Refinamiento_Contexto_Guardrails.md`.
- `AUT-CLOSE-TECH-001` en `03_Expedientes/AUT-001_Decision_Cierre_Tecnico_Provisional.md`.
- `CIERRE-AUT-001` en `03_Expedientes/AUT-001_Decision_Cierre_Operativo_Completo.md`.
- `DO-LAB-RUN-001` en `06_Automatizacion/lab_run.py`.

Documento oficial de Nivel C activo:

- `C-002_RFC_Operativo_Auditor_v0.md` en `02_Documentos`, RFC operativo del Auditor v0.
- `C-001_Especificacion_Tecnica_Auditor.md` en `02_Documentos`.

Especificacion candidata promovida:

- `SPEC-AUD-001_Candidata` en `03_Expedientes/DO-001_SPEC-AUD-001_Candidata.md`.

Proximo objetivo:

- Avanzar `MOC-001` por `MOC-ROUTE-010`: decidir rutas posteriores despues del paquete de registro/auditoria, priorizando si el MOC permanece en simulacion documental, si se prepara criterio de evaluadores sin reclutamiento o si el frente entra en mantenimiento; sin respuestas reales, sin uso clinico y sin modificar `Documento 04`.
- Conservar `AO-DOC04-FORM-001` como incorporacion acotada de `Pi_tb` / `Eq_tb` al Documento 04, sin leerla como cierre global.
- Mantener bloqueada la exportacion general de R4/Gamma salvo nueva compuerta con dominio externo y semantica independiente de expediente.
- Profundizar `AO-PPI-BRIDGE-001` hacia pruebas de Confluencia global y Equivalencia global de proyecciones sin reabrir `P-PI.0` / `P-PI.1`.
- Usar `R001-TB-001` solo como relacion formal local de apoyo a `AO-001`; no tratarlo como cierre global.
- Madurar `TCS-001` desde `TCS-MAT-PROV-001` hacia semantica formal, mas casos externos no regulados y relacion controlada con `AO-001` / `C-001`.
- `HXI-001` queda abierto en mantenimiento local; solo sale de mantenimiento por decision posterior con evidencia nueva, decision puente, cierre o promocion separada.
- `PSI-001` ya no se continua dentro del Laboratorio y no tiene copia local de traspaso; cualquier continuidad de psicologia vive en el proyecto independiente `Psicologia Concordante`.
- Reportes automatizados regenerados en la verificacion local del 2026-07-05: `DO-LAB-RUN-001` queda en `advertencia` con recomendacion `mantener_cierre_operativo`; `DO-LAB-RISK-001` queda con `riesgo_activo: 0`, `risk_blocks_closure: false`, advertencias controladas y deuda documental visible.

Expediente activo inmediato:

- `MOC-001` queda como frente integrador teorico-operativo principal; primera ruta valida ejecutada por `MOC-ROUTE-EXEC-001`, bateria ampliada por `MOC-ROUTE-002`, puente formal `MOC/TCS` aceptado por `MOC-ROUTE-003`, puente formal `MOC/AO` aceptado por `MOC-ROUTE-004`, protocolo v0.2 aceptado por `MOC-ROUTE-005`, protocolo documental de piloto futuro preparado por `MOC-ROUTE-006`, compuerta de no autorizacion aplicada por `MOC-ROUTE-007`, paquete pre-ejecucion preparado por `MOC-ROUTE-008`, paquete de registro/auditoria preparado por `MOC-ROUTE-009` y siguiente ruta recomendada `MOC-ROUTE-010`; no canonico, no clinico, no regulado y sin admision de `H-Xi`.
- `AO-001` queda como frente operativo principal para profundizar `AO-PPI-BRIDGE-001`, conservar `AO-DOC04-FORM-001` como formalizacion acotada de `Pi_tb` / `Eq_tb`, mantener bloqueada la exportacion general de R4/Gamma y revisar despues su relacion eventual con `REPORT_LAYER`.
- `HXI-001` queda abierto en mantenimiento local; conserva `Xi_eval`, no admite `H-Xi`, no canoniza `Xi` y no reabre `PSI-001`.
- `R001-001` queda aceptado como integracion tecnica local y relacion formal local `R001-TB-001`; deudas vivas: Equivalencia global, Confluencia global, pruebas externas de Confluencia y eventual incorporacion al Documento 04.
- `TCS-001` queda como frente teorico provisional con `TCS-MAT-PROV-001` aceptado; sigue abierto para semantica formal, mas casos externos y relacion controlada con `AO-001` / `C-001`.
- `P-PI.0` / `P-PI.1` quedan cerrados como frentes de trabajo por `D-2026-07-03-002`; `AO-PPI-BRIDGE-001` avanza localmente Confluencia y Equivalencia sin cerrar problemas globales. `AUD-001` queda completo en version documental/operativa v0 y ya produjo `C-002`; permanece abierto solo para rutas posteriores no cubiertas; `R4-FORMAL-AUD-001` y `GAMMA-FORMAL-AUD-001` siguen como construcciones locales, con exportacion general bloqueada por `D-2026-07-05-009`. `H-B.6` y `H-B.7` quedan congeladas como brotes alternos y originales historicos. `PSI-001` queda transferido a proyecto independiente `Psicologia Concordante` y sin copia local de traspaso. `AUT-001` queda cerrado operativamente; `AUT-002` queda aceptado como mantenimiento tecnico minimo; `HXI-001` queda abierto en mantenimiento local, sin admision de `H-Xi`; `B-001.5` queda congelado.
- Vision papers: `VISION_PAPER_PROPUESTA.md` y `VISION_PAPER_FINAL_REFERENCIAS.md` quedan inactivos hasta nuevo aviso.

NO volver a discutir sin reapertura explicita:

- `EF-001`
- `CP-001`
- Procedimiento
- Auditoria

Entrada recomendada mientras `HANDOFF.md` y `HANDOFF_PACKAGE.md` estan inactivos:

1. `CURRENT_STATE.md`
2. `05_Estado_Proyecto/ESTADO_ACTUAL.md`
3. `README.md`
4. `INDEX.md`
5. `PROMPT_MAESTRO.md`
6. `01_Canon/M-000_Reglas_Fundamentales.md`
7. `01_Canon/M-001_Auditoria_Arquitectonica.md`
8. `02_Documentos/C-002_RFC_Operativo_Auditor_v0.md`
9. `03_Expedientes/AUD-001_Decision_Promocion_SPEC-RFC-AUDITOR-V0.md`
