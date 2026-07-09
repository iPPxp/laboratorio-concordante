# AO_R4_GAMMA_EXPORT_GATE_002_REPORT

report_id: AO-R4-GAMMA-EXPORT-GATE-002-20260708-210446
expediente: AO-001
algoritmo: AO-R4-GAMMA-EXPORT-GATE-002
suite_id: AO-R4-GAMMA-EXPORT-GATE-CASES-002
resultado: ok
recomendacion: mantener_r4_gamma_sin_exportacion_general
transformacion_permitida: false
restricted_interoperable_profile_retained: true
r4_gamma_global_export_authorized: false
global_export_authorized: false
global_closure_authorized: false
report_layer_promoted: false

## Resumen

- cases: 7
- passed: 7
- failed: 0
- restricted_interoperable_cases: 1
- blocked_cases: 6

## Casos

- PASS `AO-R4G-EXP-001`: perfil_restringido_interoperable
- PASS `AO-R4G-EXP-002`: bloqueo_exportacion_general
  - blockers: exportacion_general
- PASS `AO-R4G-EXP-003`: bloqueo_semantica_dependiente_aud
  - blockers: semantica_dependiente_aud
- PASS `AO-R4G-EXP-004`: bloqueo_dominio_externo_insuficiente
  - blockers: dominio_externo_insuficiente
- PASS `AO-R4G-EXP-005`: bloqueo_cierre_global_implicito
  - blockers: cierre_global_implicito
- PASS `AO-R4G-EXP-006`: bloqueo_modo_mutante
  - blockers: modo_mutante
- PASS `AO-R4G-EXP-007`: bloqueo_cambio_nivel_c
  - blockers: cambio_nivel_c

## Guardas

- modifica_doc04: false
- modifica_canon: false
- modifica_nivel_c: false
- crea_nivel_c: false
- exporta_r4_gamma: false
- cierra_confluencia_global: false
- cierra_equivalencia_global: false
- promueve_report_layer: false
- autoriza_transformacion: false

## Dictamen

- Sin hallazgos bloqueantes.
- R4/Gamma conservan perfil restringido interoperable, no exportacion general.
