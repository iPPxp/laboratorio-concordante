# AO_PPI_BRIDGE_002_REPORT

report_id: AO-PPI-BRIDGE-002-20260706-153515
expediente: AO-001
algoritmo: AO-PPI-BRIDGE-002
suite_id: AO-PPI-BRIDGE-002-CASES
resultado: ok
recomendacion: mantener_deudas_globales_abiertas
transformacion_permitida: false

## Resumen

- cases: 8
- passed: 8
- failed: 0

## Criterios fuertes

- testigo_comun: true
- evidencia_preservada: true
- decision_preservada: true
- permiso_no_mutante: true
- deuda_preservada: true
- autoridad_no_aumentada: true
- salida_segura: true

## Guardas de alcance

- modifica_doc04: false
- modifica_canon: false
- crea_nivel_c: false
- reabre_p_pi_0: false
- reabre_p_pi_1: false
- cierra_confluencia_global: false
- cierra_equivalencia_global: false
- promueve_report_layer: false
- promueve_r4_gamma: false
- autoriza_transformacion: false

## Deudas conservadas abiertas

- confluencia_global_abierta: true
- equivalencia_global_abierta: true
- serializacion_report_layer_abierta: true
- relacion_tcs_abierta: true
- r4_gamma_exportacion_general_bloqueada: true

## Resultados

- PASS `AO-PPI-STRONG-001` (`equivalence`): equivalencia_fuerte_local (esperado: equivalencia_fuerte_local)
- PASS `AO-PPI-STRONG-002` (`equivalence`): equivalencia_fuerte_local (esperado: equivalencia_fuerte_local)
- PASS `AO-PPI-STRONG-003` (`equivalence`): divergencia_clasificada (esperado: divergencia_clasificada)
  - warnings: `signature:diverge_bajo_testigo`
- PASS `AO-PPI-STRONG-004` (`confluence`): confluencia_fuerte_local (esperado: confluencia_fuerte_local)
- PASS `AO-PPI-STRONG-005` (`confluence`): divergencia_clasificada (esperado: divergencia_clasificada)
  - warnings: `signature:diverge_bajo_testigo`
- PASS `AO-PPI-STRONG-006` (`equivalence`): bloqueo_por_testigo (esperado: bloqueo_por_testigo)
  - blockers: `witness:no_comun`
- PASS `AO-PPI-STRONG-007` (`confluence`): bloqueo_report_layer_incompleto (esperado: bloqueo_report_layer_incompleto)
  - blockers: `report_layer:incompleto`
- PASS `AO-PPI-STRONG-008` (`equivalence`): bloqueo_por_autoridad (esperado: bloqueo_por_autoridad)
  - blockers: `autoridad_aumentada:expediente->canon`

## Hallazgos

- Sin hallazgos bloqueantes.
- La bateria fortalece evidencia local, pero no cierra Confluencia global ni Equivalencia global.
