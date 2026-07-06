# AO_TCS_REL_001_REPORT

report_id: AO-TCS-REL-001-20260706-153515
expediente: AO-001
algoritmo: AO-TCS-REL-001
suite_id: AO-TCS-REL-CASES-001
resultado: ok
recomendacion: mantener_tcs_provisional_no_canonico
transformacion_permitida: false
tcs_relation_local: true
tcs_canonical: false
global_closure_authorized: false

## Resumen

- cases: 10
- passed: 10
- failed: 0
- mapped_cases: 7
- blocked_cases: 3

## Casos

- PASS `AO-TCS-001`: falta_testigo -> TCS-F1 / bloqueo_de_concordancia (relacion_ao_tcs_local)
- PASS `AO-TCS-002`: aumento_autoridad -> TCS-F2 / bloqueo_de_concordancia (relacion_ao_tcs_local)
- PASS `AO-TCS-003`: conflicto_autoridades -> TCS-F9 / bloqueo_de_concordancia (relacion_ao_tcs_local)
- PASS `AO-TCS-004`: perdida_permiso -> TCS-F5 / bloqueo_de_concordancia (relacion_ao_tcs_local)
- PASS `AO-TCS-005`: divergencia_clasificada -> TCS-F10 / discordancia_global_controlada (relacion_ao_tcs_local)
- PASS `AO-TCS-006`: no_comparable -> TCS-F10 / no_comparable (no_comparable_clasificado)
- PASS `AO-TCS-007`: historial_autoridad -> TCS-F7 / bloqueo_de_concordancia (relacion_ao_tcs_local)
- PASS `AO-TCS-008`: falta_testigo ->  / bloqueo_de_concordancia (bloqueo_mapeo_incompleto)
  - blockers: witness:ausente
- PASS `AO-TCS-009`: aumento_autoridad ->  / bloqueo_de_concordancia (bloqueo_canonizacion_tcs)
  - blockers: canonizacion_tcs_no_autorizada
- PASS `AO-TCS-010`: bloqueo_concordancia ->  / bloqueo_de_concordancia (bloqueo_cierre_global)
  - blockers: cierre_global_no_autorizado

## Guardas

- modifica_doc04: false
- modifica_canon: false
- crea_nivel_c: false
- canoniza_tcs: false
- cierra_confluencia_global: false
- cierra_equivalencia_global: false
- autoriza_transformacion: false

## Dictamen

- Sin hallazgos bloqueantes.
- TCS clasifica fallos AO en grado local provisional; no se canoniza TCS ni se cierra ningun problema global.
