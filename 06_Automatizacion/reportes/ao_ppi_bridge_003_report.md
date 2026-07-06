# AO_PPI_BRIDGE_003_REPORT

report_id: AO-PPI-BRIDGE-003-20260706-153515
expediente: AO-001
algoritmo: AO-PPI-BRIDGE-003
suite_id: AO-PPI-BRIDGE-003-MATRIX
resultado: ok
recomendacion: mantener_cierre_global_no_autorizado
transformacion_permitida: false
global_closure_authorized: false

## Evidencia fuente

- AO-PPI-BRIDGE-002
- AO-DOC04-WIDE-TEST-001
- AO-REPORT-LAYER-BRIDGE-001
- REPORT-LAYER-C002-GATE-001

## Resumen

- conditions: 10
- local_satisfied: 3
- missing_or_blocking: 10
- report_layer_cases: 9
- report_layer_passed: 9
- report_layer_failed: 0

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

## Matriz de condiciones

- PASS `AO-PPI-GC-001` (equivalencia): satisfecha_local / aporta_evidencia_local
  - gap: Falta demostrar que el patron se conserva fuera de la familia local de AO-001.
- PASS `AO-PPI-GC-002` (confluencia): satisfecha_local / aporta_evidencia_local
  - gap: Falta probar estabilidad de rutas con dominios externos no disenados por el propio expediente.
- PASS `AO-PPI-GC-003` (report_layer): satisfecha_local / aporta_evidencia_local
  - gap: Falta serializacion interfrente exportable si se quiere usar fuera del perfil local pre-C.
- PASS `AO-PPI-GC-004` (report_layer): faltante_global / bloquea_cierre_global
  - gap: No hay contrato exportable con versionado, compatibilidad y mapa de campos entre frentes.
- PASS `AO-PPI-GC-005` (autoridad): faltante_global / bloquea_cierre_global
  - gap: Solo hay guardas locales de no aumento; falta criterio general de comparabilidad entre niveles.
- PASS `AO-PPI-GC-006` (dominios): faltante_global / bloquea_cierre_global
  - gap: Las pruebas externas son utiles pero todavia pocas y sinteticas.
- PASS `AO-PPI-GC-007` (tcs): faltante_global / bloquea_cierre_global
  - gap: No existe todavia una relacion AO/TCS aceptada para clasificar fallos globales de concordancia.
- PASS `AO-PPI-GC-008` (alcance): bloqueada_por_alcance / bloquea_reapertura_no_autorizada
  - gap: P-PI.0 y P-PI.1 permanecen cerrados como frentes; AO solo trabaja los problemas vivos.
- PASS `AO-PPI-GC-009` (exportacion): bloqueada_por_alcance / bloquea_cierre_por_exportacion
  - gap: La compuerta vigente bloquea exportacion general; REPORT_LAYER permanece local pre-C.
- PASS `AO-PPI-GC-010` (reproducibilidad): faltante_global / bloquea_cierre_global
  - gap: Existe protocolo MOC local, pero falta protocolo AO especifico para cierre global de proyecciones.

## Casos heterogeneos REPORT_LAYER

- PASS `RL-HET-001`: compatible_heterogeneo_no_mutante (esperado: compatible_heterogeneo_no_mutante)
- PASS `RL-HET-002`: compatible_heterogeneo_no_mutante (esperado: compatible_heterogeneo_no_mutante)
- PASS `RL-HET-003`: compatible_heterogeneo_no_mutante (esperado: compatible_heterogeneo_no_mutante)
- PASS `RL-HET-004`: compatible_heterogeneo_no_mutante (esperado: compatible_heterogeneo_no_mutante)
- PASS `RL-HET-005`: divergencia_clasificada (esperado: divergencia_clasificada)
  - warnings: `projection_family:diverge`
- PASS `RL-HET-006`: bloqueo_testigo (esperado: bloqueo_testigo)
  - blockers: `witness:ausente`
- PASS `RL-HET-007`: bloqueo_recomendacion_como_decision (esperado: bloqueo_recomendacion_como_decision)
  - blockers: `recomendacion_convertida_en_decision`
- PASS `RL-HET-008`: bloqueo_autoridad (esperado: bloqueo_autoridad)
  - blockers: `autoridad_no_autorizada:nivel_c`
- PASS `RL-HET-009`: bloqueo_modo_mutante (esperado: bloqueo_modo_mutante)
  - blockers: `modo_mutante_no_autorizado`

## Dictamen

- Sin hallazgos bloqueantes.
- La matriz acredita avance local fuerte, pero mantiene cierre global no autorizado.
- REPORT_LAYER queda ampliado con casos heterogeneos no mutantes y permanece local pre-C.
