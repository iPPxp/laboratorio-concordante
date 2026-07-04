# LAB_EXECUTIVE_SUMMARY

report_id: DO-LAB-SUMMARY-20260703-201432
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

- frente activo: `AO-001` queda como frente operativo principal para profundizar `AO-PPI-BRIDGE-001`, formalizacion posterior de Documento 04 y relacion eventual con `REPORT_LAYER`.
- ultima decision: `AUT-001_Decision_Refinamiento_Contexto_Guardrails.md` (`D-2026-07-03-020`): acepta `AUT-RISK-REFINE-002` y `AUT-VAL-012` para reclasificar falsos riesgos activos de guardrails como advertencias controladas; no reabre `AUT-001` ni borra hallazgos.
- proximo objetivo: Profundizar `AO-PPI-BRIDGE-001` hacia pruebas de Confluencia global y Equivalencia global de proyecciones sin reabrir `P-PI.0` / `P-PI.1`.

## Riesgos clasificados

- riesgo_activo: 0
- advertencia_controlada: 23
- deuda_documental: 108
- advertencia_heredada: 59
- observacion: 61

## Contexto de riesgos

- bitacora_historica: 9
- control_auditoria: 1
- decision_registrada: 21
- guardrail: 49
- meta_check: 12
- riesgo_real: 159

## Severidad

- alta: 3
- media: 117
- baja: 131

## Riesgos activos principales

- Sin riesgos activos principales.

## Automatizacion

- DO-CHECK-MIN-001: advertencia (139 hallazgos)
- DO-CHECK-MED-001: advertencia (237 hallazgos)
- DO-STATE-BOARD-001: ok (0 hallazgos)
- DO-LAB-CONTINUITY-001: advertencia (237 hallazgos)
- DO-LAB-RISK-001: advertencia_clasificada (251 hallazgos)

## Siguientes acciones

- Mantener cierre operativo de AUT-001 con deuda documental visible.
- Mantener advertencias controladas visibles en reportes.
- Mantener transformacion_permitida en false hasta decision explicita.
