# MOC_EVAL_REPORT

report_id: MOC-EVAL-001-20260706-120317
expediente: MOC-001
algoritmo: MOC-EVAL-001
suite_id: MOC-SYN-001
resultado: ok
recomendacion: conservar_moc_provisional_no_canonico
transformacion_permitida: false

## Resumen

- cases: 11
- passed: 11
- failed: 0
- tests_executed: MOC-XI-EVAL-FORMAL-001, MOC-METRIC-STATE-001, MOC-EVAL-PROTO-001, MOC-EVAL-PROTO-002, MOC-TCS-BRIDGE-001, MOC-AO-BRIDGE-001

## Evaluadores simulados

- coincidencia_exacta: 6
- coincidencia_parcial: 3
- desacuerdo_justificado: 2

## Protocolo v0.2

- resuelto: 4
- resuelto_con_deuda: 3
- resuelto_por_bloqueo: 2
- revision_si_repite: 2
- review_required: 2
- axis_counts:
  - estado_moc: 5
  - familia_moc: 2
  - regla_xi: 2
  - rol_ao: 5
  - sin_desacuerdo: 6

## Guardas de alcance

- No admite `H-Xi`.
- No canoniza `Xi`.
- No evalua personas reales.
- No abre uso clinico.
- No modifica `Documento 04`, Canon ni Nivel C.
- No cierra Confluencia global ni Equivalencia global.

## Deudas conservadas abiertas

- moc_provisional_abierto: true
- tcs_no_canonico: true
- hxi_mantenimiento_local: true
- moc_ao_bridge_local: true
- protocolo_v02_no_canonico: true
- doc04_sin_modificar_por_moc_ao: true
- confluencia_global_abierta: true
- equivalencia_global_abierta: true
- exportacion_r4_gamma_bloqueada: true
- estudio_empirico_real_pendiente: true

## Resultados

- PASS `MOC-CASE-001`: Xi `redundante` / MOC `concordancia_local` (coincidencia_exacta)
  - operadores: XI-R6-PATRON-REDUNDANTE -> TCS-R3-EJES-COMPLETOS -> STATE-R5-CONCORDANCIA-LOCAL
  - puente_ao: evidencia_auxiliar_equivalencia_local
  - protocolo_v02: resuelto / aceptar_salida_local / ejes sin_desacuerdo
  - deuda: conservar_trazabilidad
- PASS `MOC-CASE-002`: Xi `util_acotado` / MOC `concordancia_local` (coincidencia_exacta)
  - operadores: XI-R4-REORGANIZACION-ESTABLE -> TCS-R3-EJES-COMPLETOS -> STATE-R5-CONCORDANCIA-LOCAL
  - puente_ao: evidencia_auxiliar_equivalencia_local
  - protocolo_v02: resuelto / aceptar_salida_local / ejes sin_desacuerdo
  - deuda: no_exportar_como_regla_global
- PASS `MOC-CASE-003`: Xi `limitado` / MOC `friccion_operativa` (coincidencia_parcial)
  - operadores: XI-R5-CONFLICTO-SIN-ESTABILIDAD -> TCS-R3-EJES-COMPLETOS -> STATE-R4-FRICCION-LOCAL
  - puente_ao: evidencia_friccion_confluencia_local
  - protocolo_v02: resuelto_con_deuda / aceptar_operator_trace_con_deuda_visible / ejes estado_moc, rol_ao
  - deuda: resolver_conflicto_de_regla_local
- PASS `MOC-CASE-004`: Xi `no_comparable` / MOC `no_comparable` (coincidencia_exacta)
  - operadores: XI-R3-UNIDAD-MINIMA -> TCS-R3-EJES-COMPLETOS -> STATE-R2-NO-COMPARABLE
  - puente_ao: bloqueo_comparabilidad_sin_uso_positivo
  - protocolo_v02: resuelto_por_bloqueo / aceptar_bloqueo_sin_uso_positivo / ejes sin_desacuerdo
  - deuda: redefinir_unidad_minima
- PASS `MOC-CASE-005`: Xi `bloqueado` / MOC `bloqueo_de_concordancia` (coincidencia_exacta)
  - operadores: XI-R1-ALCANCE-EVIDENCIA -> TCS-R1-EJE-NUCLEAR-FALTANTE -> STATE-R1-BLOQUEO-DOMINANTE
  - puente_ao: bloqueo_seguridad_sin_uso_positivo
  - protocolo_v02: resuelto_por_bloqueo / aceptar_bloqueo_sin_uso_positivo / ejes sin_desacuerdo
  - deuda: retirar_caso_o_abrir_decision_separada
- PASS `MOC-CASE-006`: Xi `util_acotado` / MOC `discordancia_global` (coincidencia_parcial)
  - operadores: XI-R4-REORGANIZACION-ESTABLE -> TCS-R3-EJES-COMPLETOS -> STATE-R3-CONFLICTO-GLOBAL
  - puente_ao: deuda_global_no_cierre
  - protocolo_v02: resuelto_con_deuda / aceptar_operator_trace_con_deuda_visible / ejes estado_moc, rol_ao
  - deuda: confluencia_y_equivalencia_global_abiertas
- PASS `MOC-CASE-007`: Xi `util_acotado` / MOC `concordancia_parcial` (coincidencia_parcial)
  - operadores: XI-R4-REORGANIZACION-ESTABLE -> TCS-R3-EJES-COMPLETOS -> STATE-R6-CONCORDANCIA-PARCIAL
  - puente_ao: evidencia_auxiliar_con_deuda
  - protocolo_v02: resuelto_con_deuda / aceptar_operator_trace_con_deuda_visible / ejes estado_moc, rol_ao
  - deuda: completar_trazabilidad_secundaria
- PASS `MOC-CASE-008`: Xi `limitado` / MOC `friccion_operativa` (desacuerdo_justificado)
  - operadores: XI-R5-CONFLICTO-SIN-ESTABILIDAD -> TCS-R3-EJES-COMPLETOS -> STATE-R4-FRICCION-LOCAL
  - puente_ao: evidencia_friccion_confluencia_local
  - protocolo_v02: revision_si_repite / mantener_desacuerdo_justificado_y_abrir_micro_revision_si_repite / ejes regla_xi, estado_moc, familia_moc, rol_ao
  - clase_desacuerdo: ambiguedad_de_regla
  - deuda: precisar_si_la_regla_es_friccion_o_bloqueo
- PASS `MOC-CASE-009`: Xi `util_acotado` / MOC `concordancia_parcial` (coincidencia_exacta)
  - operadores: XI-R4-REORGANIZACION-ESTABLE -> TCS-R2-EJE-SECUNDARIO-FALTANTE -> STATE-R6-CONCORDANCIA-PARCIAL
  - puente_ao: evidencia_auxiliar_con_deuda
  - protocolo_v02: resuelto / aceptar_salida_local / ejes sin_desacuerdo
  - deuda: completar_eje_tcs_secundario_automation_bounded
- PASS `MOC-CASE-010`: Xi `limitado` / MOC `friccion_operativa` (coincidencia_exacta)
  - operadores: XI-R5-CONFLICTO-SIN-ESTABILIDAD -> TCS-R3-EJES-COMPLETOS -> STATE-R4-FRICCION-LOCAL
  - puente_ao: evidencia_friccion_confluencia_local
  - protocolo_v02: resuelto / aceptar_salida_local / ejes sin_desacuerdo
  - deuda: resolver_autoridad_local_sin_invocar_confluencia_global
- PASS `MOC-CASE-011`: Xi `util_acotado` / MOC `concordancia_parcial` (desacuerdo_justificado)
  - operadores: XI-R4-REORGANIZACION-ESTABLE -> TCS-R3-EJES-COMPLETOS -> STATE-R6-CONCORDANCIA-PARCIAL
  - puente_ao: evidencia_auxiliar_con_deuda
  - protocolo_v02: revision_si_repite / mantener_desacuerdo_justificado_y_abrir_micro_revision_si_repite / ejes regla_xi, estado_moc, familia_moc, rol_ao
  - clase_desacuerdo: frontera_concordancia_friccion
  - deuda: precisar_umbral_entre_deuda_no_bloqueante_y_friccion

## Hallazgos

- Sin hallazgos bloqueantes.
