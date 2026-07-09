# LAB_EXECUTIVE_SUMMARY

report_id: DO-LAB-SUMMARY-20260708-210447
expediente: AUT-001
algoritmo: DO-LAB-SUMMARY-001
resultado: advertencia
recomendacion: mantener_cierre_operativo
transformacion_permitida: false

## Lectura ejecutiva

- Cierre operativo conservado con deuda documental visible.
- corrida unificada: advertencia / mantener_cierre_operativo
- clasificacion de riesgos: advertencia_clasificada / mantener_cierre_operativo

## Estado operativo

- frente activo: `AO-001` queda como frente operativo inmediato con `AO-GLOBAL-READINESS-001` aceptado como matriz de no autorizacion global, `AO-PPI-BRIDGE-004` fijado como estado actual local de deudas, `AO-EXT-INDEP-001` / `AO-EXT-EVID-GATE-001` preparados para admisibilidad externa y `AO-EXT-REAL-001` admitido preliminarmente como evidencia externa real. La siguiente ruta defensible requiere decision separada de reconsideracion; ninguna promocion, exportacion ni cierre global queda autorizado.
- ultima decision: `MOC-001_Decision_Aplicacion_Oficial_Canon_Doc04_001.md` (`D-2026-07-09-005`): acepta y ejecuta `MOC-CANON-DOC04-APPLY-001`; `M-001` adopta matriz de superficies para intervenciones de nivel sensible y Documento 04 adopta entrada auxiliar por traza local de grafo. `M-000` queda sin cambio textual; no hay modo mutante, uso externo, Nivel C, cierre global, promocion de `REPORT_LAYER` ni exportacion R4/Gamma.
- proximo objetivo: Conservar `AO-GLOBAL-READINESS-001` como matriz vigente de no autorizacion global y `AO-PPI-BRIDGE-004` como estado actual local de deudas `AO-PPI`.

## Riesgos clasificados

- riesgo_activo: 0
- advertencia_controlada: 29
- deuda_documental: 398
- advertencia_heredada: 63
- observacion: 61

## Contexto de riesgos

- bitacora_historica: 15
- control_auditoria: 1
- decision_registrada: 47
- guardrail: 104
- meta_check: 12
- riesgo_real: 372

## Severidad

- alta: 5
- media: 268
- baja: 278

## Riesgos activos principales

- Sin riesgos activos principales.

## Automatizacion

- DO-CHECK-MIN-001: advertencia (266 hallazgos)
- DO-CHECK-MED-001: advertencia (474 hallazgos)
- DO-STATE-BOARD-001: ok (0 hallazgos)
- DO-LAB-CONTINUITY-001: advertencia (474 hallazgos)
- DO-LAB-RISK-001: advertencia_clasificada (551 hallazgos)
- R001-TABLE-CHECK-001: ok (0 hallazgos)
- AO-EXT-CONF-001: ok (0 hallazgos)
- AO-DOC04-WIDE-TEST-001: ok (0 hallazgos)
- AO-PPI-BRIDGE-002: ok (0 hallazgos)
- AO-PPI-BRIDGE-003: ok (0 hallazgos)
- AO-REPORT-SERIAL-001: ok (0 hallazgos)
- AO-TCS-REL-001: ok (0 hallazgos)
- AO-AUTH-GLOBAL-001: ok (0 hallazgos)
- AO-EXT-COV-001: ok (0 hallazgos)
- AO-PPI-BRIDGE-004: ok (0 hallazgos)
- AO-PROTO-INDEP-001: ok (0 hallazgos)
- AO-EQ-GLOBAL-GATE-001: ok (0 hallazgos)
- AO-CONF-GLOBAL-GATE-001: ok (0 hallazgos)
- AO-REPORT-PROMO-GATE-001: ok (0 hallazgos)
- AO-R4-GAMMA-EXPORT-GATE-002: ok (0 hallazgos)
- AO-GLOBAL-READINESS-001: ok (0 hallazgos)
- AO-EXT-EVID-GATE-001: ok (0 hallazgos)
- AO-EXT-REAL-001: ok (0 hallazgos)
- REPORT-LAYER-C002-GATE-001: ok (0 hallazgos)
- MOC-EVAL-001: ok (0 hallazgos)
- MOC-EXP-GRAPH-CHECK-001: ok (0 hallazgos)
- MOC-GRAPH-CANON-DOC04-GATE-001: ok (0 hallazgos)
- MOC-CANON-DOC04-IMPACT-001: ok (0 hallazgos)
- MOC-CANON-DOC04-ADOPT-GATE-001: ok (0 hallazgos)
- MOC-CANON-DOC04-APPLY-CHECK-001: ok (0 hallazgos)

## Siguientes acciones

- Mantener cierre operativo de AUT-001 con deuda documental visible.
- Mantener advertencias controladas visibles en reportes.
- Mantener transformacion_permitida en false hasta decision explicita.
