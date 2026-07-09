# AO_PROTOCOL_INDEPENDENT_001_REPORT

report_id: AO-PROTO-INDEP-001-20260708-210446
expediente: AO-001
algoritmo: AO-PROTO-INDEP-001
suite_id: AO-PROTO-INDEP-CASES-001
resultado: ok
recomendacion: aceptar_protocolo_reproducible_local
transformacion_permitida: false
independent_protocol_accepted: true
global_closure_authorized: false
global_export_authorized: false
report_layer_promoted: false
r4_gamma_global_export_authorized: false

## Resumen

- cases: 4
- passed: 4
- failed: 0
- exact: 2
- family: 1
- justified_disagreement: 1

## Casos

- PASS `AO-PROTO-001`: coincidencia_exacta
  - states: equivalencia_local, equivalencia_local, equivalencia_local
  - families: equivalencia, equivalencia, equivalencia
  - debts: sin_deuda_local, sin_deuda_local, sin_deuda_local
- PASS `AO-PROTO-002`: coincidencia_familia
  - states: divergencia_clasificada, friccion_operativa, divergencia_reporte
  - families: divergencia_controlada, divergencia_controlada, divergencia_controlada
  - debts: deuda_report_layer, deuda_report_layer, deuda_report_layer
- PASS `AO-PROTO-003`: desacuerdo_justificado
  - states: bloqueo_por_testigo, bloqueo_por_autoridad, bloqueo_report_layer_incompleto
  - families: bloqueo_testigo, bloqueo_autoridad, bloqueo_reporte
  - debts: testigo_insuficiente, autoridad_excedida, report_layer_incompleto
- PASS `AO-PROTO-004`: coincidencia_exacta
  - states: no_comparable, no_comparable, no_comparable
  - families: no_comparabilidad, no_comparabilidad, no_comparabilidad
  - debts: unidad_minima, unidad_minima, unidad_minima

## Guardas

- modifica_doc04: false
- modifica_canon: false
- modifica_nivel_c: false
- crea_nivel_c: false
- fuerza_unanimidad: false
- cierra_confluencia_global: false
- cierra_equivalencia_global: false
- promueve_report_layer: false
- exporta_r4_gamma: false
- autoriza_transformacion: false

## Dictamen

- Sin hallazgos bloqueantes.
- El protocolo clasifica coincidencias y desacuerdos justificados sin forzar unanimidad.
- No autoriza cierre global ni promocion.
