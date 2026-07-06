# AO_DOC04_WIDE_TEST_REPORT

report_id: AO-DOC04-WIDE-20260706-134840
expediente: AO-001
algoritmo: AO-DOC04-WIDE-TEST-001
suite_id: AO-DOC04-WIDE-CASES-001
resultado: ok
recomendacion: precisar_report_layer_sin_promocion
transformacion_permitida: false

## Resumen

- cases: 8
- passed: 8
- failed: 0

## Relacion REPORT_LAYER

- estatus: local_pre_c
- rol_ao: entrada_de_Pi_rep_y_evidencia_de_reporte
- no_sustituye: Op_AO, decision, permiso, verificacion_posterior, Nivel_C

## Guardas de alcance

- modifica_doc04: false
- modifica_canon: false
- crea_nivel_c: false
- promueve_report_layer: false
- cierra_confluencia_global: false
- cierra_equivalencia_global: false
- promueve_r4_gamma: false
- autoriza_transformacion: false

## Deudas conservadas abiertas

- confluencia_global_abierta: true
- equivalencia_global_abierta: true
- report_layer_nivel_c_abierto: true
- r4_gamma_exportacion_general_bloqueada: true
- tcs_maduracion_abierta: true

## Resultados

- PASS `AO-WIDE-001` (`Eq_local`): Eq_local => equivalencia_local
- PASS `AO-WIDE-002` (`Conf_local`): Conf_local => confluencia_local
- PASS `AO-WIDE-003` (`Eq_local`): Eq_local => bloqueo_por_testigo
  - blockers: `missing:witness, missing:witness, report_layer:missing`
- PASS `AO-WIDE-004` (`Gate_AO`): Gate_AO => no_autorizado_sin_transformar
  - blockers: `permission:transformacion_no_autorizada`
- PASS `AO-WIDE-005` (`Eq_local`): Eq_local => bloqueo_por_autoridad
  - blockers: `authority_increase:expediente->nivel_c`
- PASS `AO-WIDE-006` (`Eq_local`): Eq_local => divergencia_clasificada
  - warnings: `projection:signature_differs`
- PASS `AO-WIDE-007` (`R4Gamma_AO`): R4Gamma_AO => bloqueo_exportacion_r4_gamma
  - blockers: `r4_gamma:exportacion_general`
- PASS `AO-WIDE-008` (`Eq_local`): Eq_local => bloqueo_report_layer_incompleto
  - blockers: `report_layer:missing:decision_emitida, report_layer:missing:transformacion_permitida`

## Hallazgos

- Sin hallazgos bloqueantes.
