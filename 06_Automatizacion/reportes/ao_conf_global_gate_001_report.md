# AO_CONF_GLOBAL_GATE_001_REPORT

report_id: AO-CONF-GLOBAL-GATE-001-20260708-210446
expediente: AO-001
algoritmo: AO-CONF-GLOBAL-GATE-001
suite_id: AO-CONF-GLOBAL-GATE-MATRIX-001
resultado: ok
recomendacion: mantener_confluencia_global_no_autorizada
transformacion_permitida: false
global_confluence_authorized: false
global_closure_authorized: false
global_export_authorized: false
report_layer_promoted: false
r4_gamma_global_export_authorized: false

## Resumen

- conditions: 7
- satisfied_local: 3
- partial_local: 2
- missing_global: 1
- scope_blocked: 1
- global_blocking: 2
- failed: 0

## Matriz

- PASS `AO-CONF-GC-001` (estado_decision_reporte): satisfecha_local
  - gap: rutas locales coinciden bajo testigo compartido
  - evidence: AO-PPI-CONF-001, AO-PPI-BRIDGE-002
- PASS `AO-CONF-GC-002` (autoridad): parcial_local
  - gap: autoridad local comparable, no autoridad global
  - evidence: AO-AUTH-GLOBAL-001
- PASS `AO-CONF-GC-003` (report_layer_serializado): satisfecha_local
  - gap: serializacion local estable, no contrato global
  - evidence: AO-REPORT-SERIAL-001
- PASS `AO-CONF-GC-004` (protocolo_independiente): satisfecha_local
  - gap: reproducibilidad local sin validacion externa real
  - evidence: AO-PROTO-INDEP-001
- PASS `AO-CONF-GC-005` (cobertura_externa): parcial_local
  - gap: cobertura externa sintetica, no independiente
  - evidence: AO-EXT-COV-001
- PASS `AO-CONF-GC-006` (dominio_global): faltante_global
  - gap: no existe cobertura global independiente de dominios
  - evidence: AO-PPI-BRIDGE-004, AO-PPI-LOCAL-CLOSE-001
- PASS `AO-CONF-GC-007` (modo_mutante): bloqueada_por_alcance
  - gap: el laboratorio no autoriza rutas mutantes para cierre global
  - evidence: C-002, REPORT-LAYER-C002-GATE-001

## Guardas

- modifica_doc04: false
- modifica_canon: false
- modifica_nivel_c: false
- crea_nivel_c: false
- reabre_p_pi_0: false
- reabre_p_pi_1: false
- cierra_confluencia_global: false
- promueve_report_layer: false
- exporta_r4_gamma: false
- autoriza_transformacion: false

## Dictamen

- Sin hallazgos bloqueantes.
- La confluencia global permanece no autorizada por faltantes globales.
