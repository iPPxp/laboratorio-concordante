# REPORT_LAYER_C002_GATE_REPORT

report_id: REPORT-LAYER-C002-GATE-20260706-153515
expediente: AUT-003
algoritmo: REPORT-LAYER-C002-GATE-001
suite_id: REPORT-LAYER-C002-CASES-001
resultado: ok
recomendacion: mantener_report_layer_local_pre_c
transformacion_permitida: false
conforme_c002_no_mutante: true

## Resumen

- cases: 8
- passed: 8
- failed: 0

## Guardas

- modifica_c001: false
- modifica_c002: false
- crea_nivel_c: false
- promueve_report_layer: false
- autoriza_transformacion: false
- emite_decision_autoridad: false
- usa_historial_como_autoridad: false

## Casos

- PASS `RL-C002-001`: compatible_no_mutante (esperado: compatible_no_mutante)
- PASS `RL-C002-002`: compatible_no_mutante (esperado: compatible_no_mutante)
- PASS `RL-C002-003`: bloqueo_campos_minimos (esperado: bloqueo_campos_minimos)
  - bloqueos: missing:decision_emitida
- PASS `RL-C002-004`: bloqueo_recomendacion_como_decision (esperado: bloqueo_recomendacion_como_decision)
  - bloqueos: recomendacion_convertida_en_decision
- PASS `RL-C002-005`: bloqueo_modo_mutante (esperado: bloqueo_modo_mutante)
  - bloqueos: transformacion_permitida_true
- PASS `RL-C002-006`: bloqueo_promocion_nivel_c (esperado: bloqueo_promocion_nivel_c)
  - bloqueos: promocion_no_autorizada:nivel_c
- PASS `RL-C002-007`: bloqueo_historial_autoridad (esperado: bloqueo_historial_autoridad)
  - bloqueos: historial_como_autoridad:estado_vigente
- PASS `RL-C002-008`: bloqueo_permiso_material (esperado: bloqueo_permiso_material)
  - bloqueos: decision_mutante_sin_permiso_act_001

## Dictamen

- Sin hallazgos bloqueantes.
- REPORT_LAYER permanece como capa local pre-C; cualquier modo mutante futuro requiere decision separada.
