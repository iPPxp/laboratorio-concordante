# LAB_EXECUTIVE_SUMMARY

report_id: DO-LAB-SUMMARY-20260706-153516
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

- frente activo: `AO-001` queda como frente operativo inmediato con `AO-PPI-BRIDGE-004` aceptado como matriz consolidada local. La siguiente ruta defensible requiere decision separada: protocolo AO reproducible independiente, promocion formal de `REPORT_LAYER`, exportacion R4/Gamma o cierre global; ninguna queda autorizada.
- ultima decision: `AO-001_Decision_Matriz_Consolidada_Cierre_Global_004.md` (`D-2026-07-06-023`): acepta `AO-PPI-BRIDGE-004` como matriz consolidada local; deja cinco condiciones `satisfecha_local`, dos `parcial_local`, dos `faltante_global` y tres `bloqueada_por_alcance`, con `global_closure_authorized: false`.
- proximo objetivo: Conservar `AO-PPI-BRIDGE-004` como matriz consolidada aceptada; no usarla como cierre global.

## Riesgos clasificados

- riesgo_activo: 0
- advertencia_controlada: 25
- deuda_documental: 309
- advertencia_heredada: 63
- observacion: 61

## Contexto de riesgos

- bitacora_historica: 15
- control_auditoria: 1
- decision_registrada: 37
- guardrail: 95
- meta_check: 12
- riesgo_real: 298

## Severidad

- alta: 4
- media: 206
- baja: 248

## Riesgos activos principales

- Sin riesgos activos principales.

## Automatizacion

- DO-CHECK-MIN-001: advertencia (214 hallazgos)
- DO-CHECK-MED-001: advertencia (433 hallazgos)
- DO-STATE-BOARD-001: ok (0 hallazgos)
- DO-LAB-CONTINUITY-001: advertencia (433 hallazgos)
- DO-LAB-RISK-001: advertencia_clasificada (458 hallazgos)
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
- REPORT-LAYER-C002-GATE-001: ok (0 hallazgos)
- MOC-EVAL-001: ok (0 hallazgos)

## Siguientes acciones

- Mantener cierre operativo de AUT-001 con deuda documental visible.
- Mantener advertencias controladas visibles en reportes.
- Mantener transformacion_permitida en false hasta decision explicita.
