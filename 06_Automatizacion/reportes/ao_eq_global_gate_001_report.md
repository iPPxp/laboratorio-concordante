# AO_EQ_GLOBAL_GATE_001_REPORT

report_id: AO-EQ-GLOBAL-GATE-001-20260708-210446
expediente: AO-001
algoritmo: AO-EQ-GLOBAL-GATE-001
suite_id: AO-EQ-GLOBAL-GATE-MATRIX-001
resultado: ok
recomendacion: mantener_equivalencia_global_no_autorizada
transformacion_permitida: false
global_equivalence_authorized: false
global_closure_authorized: false
global_export_authorized: false
report_layer_promoted: false
r4_gamma_global_export_authorized: false

## Resumen

- conditions: 8
- satisfied_local: 4
- partial_local: 2
- missing_global: 1
- scope_blocked: 1
- global_blocking: 2
- failed: 0

## Matriz

- PASS `AO-EQ-GC-001` (testigo): satisfecha_local
  - gap: testigo local compartido, no testigo universal
  - evidence: AO-PPI-BRIDGE-004, AO-PPI-STRONG-001
- PASS `AO-EQ-GC-002` (pi_doc_pi_rep_pi_op): satisfecha_local
  - gap: equivalencia local de proyecciones, no cobertura de todos los dominios
  - evidence: AO-DOC04-WIDE-TEST-001, AO-PPI-BRIDGE-002
- PASS `AO-EQ-GC-003` (report_layer): parcial_local
  - gap: serializacion local, no contrato exportable global
  - evidence: AO-REPORT-SERIAL-001, REPORT-LAYER-C002-GATE-001
- PASS `AO-EQ-GC-004` (autoridad): parcial_local
  - gap: autoridad local ordenada, no autoridad global autorizada
  - evidence: AO-AUTH-GLOBAL-001
- PASS `AO-EQ-GC-005` (protocolo_independiente): satisfecha_local
  - gap: reproducibilidad local, no validacion externa independiente
  - evidence: AO-PROTO-INDEP-001
- PASS `AO-EQ-GC-006` (cobertura_externa): faltante_global
  - gap: cobertura externa sigue sintetica y no independiente
  - evidence: AO-EXT-COV-001, AO-PPI-BRIDGE-004
- PASS `AO-EQ-GC-007` (dominio_universal): bloqueada_por_alcance
  - gap: el expediente no autoriza dominio universal
  - evidence: AO-PPI-LOCAL-CLOSE-001
- PASS `AO-EQ-GC-008` (no_promocion): satisfecha_local
  - gap: guardas locales vigentes
  - evidence: AO-REPORT-LAYER-NIVEL-C-001, AO-R4-GAMMA-EXPORT-GATE-001

## Guardas

- modifica_doc04: false
- modifica_canon: false
- modifica_nivel_c: false
- crea_nivel_c: false
- reabre_p_pi_0: false
- reabre_p_pi_1: false
- cierra_equivalencia_global: false
- promueve_report_layer: false
- exporta_r4_gamma: false
- autoriza_transformacion: false

## Dictamen

- Sin hallazgos bloqueantes.
- La equivalencia global permanece no autorizada por faltantes globales.
