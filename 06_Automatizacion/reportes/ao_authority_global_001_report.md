# AO_AUTH_GLOBAL_001_REPORT

report_id: AO-AUTH-GLOBAL-001-20260706-153515
expediente: AO-001
algoritmo: AO-AUTH-GLOBAL-001
suite_id: AO-AUTH-GLOBAL-CASES-001
resultado: ok
recomendacion: mantener_criterio_autoridad_local
transformacion_permitida: false
authority_criterion_local: true
global_authority_authorized: false
global_closure_authorized: false

## Resumen

- cases: 12
- passed: 12
- failed: 0
- local_comparable: 5
- blocked_cases: 5

## Casos

- PASS `AO-AUTH-001`: canon -> documento = comparabilidad_local_autorizada (autoridad_superior_reconocida)
- PASS `AO-AUTH-002`: nivel_c -> expediente = comparabilidad_local_autorizada (autoridad_tecnica_acotada)
- PASS `AO-AUTH-003`: documento -> expediente = comparabilidad_local_autorizada (autoridad_documental)
- PASS `AO-AUTH-004`: expediente -> expediente = comparabilidad_local_autorizada (autoridad_local)
- PASS `AO-AUTH-005`: reporte_automatizado -> expediente = comparabilidad_local_autorizada (evidencia_tecnica_no_autoridad)
- PASS `AO-AUTH-006`: registro_historico -> expediente = evidencia_pasiva_no_autoridad (evidencia_pasiva_no_autoridad)
- PASS `AO-AUTH-007`: externo_sintetico -> expediente = evidencia_externa_no_autoridad (evidencia_externa_no_autoridad)
- PASS `AO-AUTH-008`: registro_historico -> expediente = bloqueo_historial_autoridad (evidencia_pasiva_no_autoridad)
  - blockers: historial_como_autoridad:estado_vigente
- PASS `AO-AUTH-009`: expediente -> expediente = bloqueo_autoridad_por_repeticion (autoridad_local)
  - blockers: autoridad_por_repeticion
- PASS `AO-AUTH-010`: reporte_automatizado -> expediente = bloqueo_recomendacion_como_decision (evidencia_tecnica_no_autoridad)
  - blockers: recomendacion_convertida_en_decision
- PASS `AO-AUTH-011`: expediente -> canon = bloqueo_autoridad_global_no_declarada (no_comparable)
  - blockers: autoridad_global_no_autorizada:autoridad_global
- PASS `AO-AUTH-012`: documento -> expediente = bloqueo_testigo (autoridad_documental)
  - blockers: witness:ausente

## Guardas

- modifica_canon: false
- modifica_nivel_c: false
- crea_nivel_c: false
- usa_historial_como_autoridad: false
- promueve_report_layer: false
- cierra_confluencia_global: false
- cierra_equivalencia_global: false
- autoriza_transformacion: false

## Dictamen

- Sin hallazgos bloqueantes.
- El criterio separa autoridad local, evidencia pasiva y bloqueos sin crear autoridad global.
