# AO_EXT_CONFLUENCE_REPORT

report_id: AO-EXT-CONF-20260706-153515
expediente: AO-001
algoritmo: AO-EXT-CONF-001
suite_id: AO-EXT-CONF-SYN-001
resultado: ok
recomendacion: mantener_deudas_globales_abiertas
transformacion_permitida: false

## Resumen

- cases: 7
- passed: 7
- failed: 0
- tests_executed: EXT-CONF-001, EXT-CONF-002

## Guardas de alcance

- No modifica Documento 04.
- No modifica Canon ni Nivel C.
- No cierra Confluencia global.
- No cierra Equivalencia global.
- No promueve ni exporta R4/Gamma.
- No canoniza ni cierra `TCS-001`.
- No autoriza transformaciones materiales.

## Deudas conservadas abiertas

- confluencia_global_abierta: true
- equivalencia_global_abierta: true
- formalizacion_doc04_abierta: true
- exportacion_r4_gamma_abierta: true
- maduracion_tcs_abierta: true

## Resultados

- PASS `EXT-CONF-001A` (`EXT-CONF-001`): normalizacion_csv vs normalizacion_json => confluencia_local
- PASS `EXT-CONF-001B` (`EXT-CONF-001`): normalizacion_csv vs normalizacion_json => bloqueo_por_testigo
  - blockers_a: `row:1:missing:status`
  - blockers_b: `row:1:missing:status`
- PASS `EXT-CONF-001C` (`EXT-CONF-001`): normalizacion_csv vs normalizacion_json => equivalencia_bajo_testigo
  - warnings_a: `row:1:extra_ignored:debug`
  - warnings_b: `row:1:extra_ignored:debug`
- PASS `EXT-CONF-001D` (`EXT-CONF-001`): normalizacion_csv vs normalizacion_json => divergencia_clasificada
- PASS `EXT-CONF-002A` (`EXT-CONF-002`): manifiesto_paquete vs reporte_dependencias => confluencia_local
- PASS `EXT-CONF-002B` (`EXT-CONF-002`): manifiesto_paquete vs reporte_dependencias => bloqueo_por_testigo
  - blockers_a: `dep:toy-core:missing:license`
  - blockers_b: `dep:toy-core:missing:license`
- PASS `EXT-CONF-002C` (`EXT-CONF-002`): manifiesto_paquete vs reporte_dependencias => divergencia_clasificada

## Hallazgos

- Sin hallazgos bloqueantes.
