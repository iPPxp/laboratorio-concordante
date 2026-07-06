# LAB_EXECUTIVE_SUMMARY

report_id: DO-LAB-SUMMARY-20260706-134842
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

- frente activo: `AO-001` queda como frente operativo inmediato para profundizar `AO-PPI-BRIDGE-001`, mantener bloqueada la exportacion general de R4/Gamma, ampliar pruebas heterogeneas de `REPORT_LAYER` solo si una decision futura lo exige, conservar `AO-DOC04-WIDE-TEST-001` como evidencia local no mutante y usar `REPORT-LAYER-C002-GATE-001` solo como compuerta no mutante conforme a `C-002`.
- ultima decision: `RH-001_Decision_Reconciliacion_PM001.md` (`D-2026-07-06-016`): acepta `RH-PM-REC-001`; `PM-001` queda reconciliado solo como deuda historica condicionada, no como expediente activo ni protocolo materializado.
- proximo objetivo: Ampliar `AO-DOC04-WIDE-TEST-001` solo si se requieren casos heterogeneos adicionales de `REPORT_LAYER`, serializacion interfrente o nuevas rutas de `Pi_rep`; la prueba local inicial de 8 casos, la precision de `REPORT_LAYER`, su permanencia local pre-C y la compuerta no mutante `C-002` ya quedaron atendidas por `D-2026-07-06-007`, `D-2026-07-06-014` y `D-2026-07-06-015`.

## Riesgos clasificados

- riesgo_activo: 0
- advertencia_controlada: 25
- deuda_documental: 206
- advertencia_heredada: 62
- observacion: 61

## Contexto de riesgos

- bitacora_historica: 14
- control_auditoria: 1
- decision_registrada: 26
- guardrail: 83
- meta_check: 12
- riesgo_real: 218

## Severidad

- alta: 4
- media: 159
- baja: 191

## Riesgos activos principales

- Sin riesgos activos principales.

## Automatizacion

- DO-CHECK-MIN-001: advertencia (172 hallazgos)
- DO-CHECK-MED-001: advertencia (353 hallazgos)
- DO-STATE-BOARD-001: ok (0 hallazgos)
- DO-LAB-CONTINUITY-001: advertencia (353 hallazgos)
- DO-LAB-RISK-001: advertencia_clasificada (354 hallazgos)
- R001-TABLE-CHECK-001: ok (0 hallazgos)
- AO-EXT-CONF-001: ok (0 hallazgos)
- AO-DOC04-WIDE-TEST-001: ok (0 hallazgos)
- REPORT-LAYER-C002-GATE-001: ok (0 hallazgos)
- MOC-EVAL-001: ok (0 hallazgos)

## Siguientes acciones

- Mantener cierre operativo de AUT-001 con deuda documental visible.
- Mantener advertencias controladas visibles en reportes.
- Mantener transformacion_permitida en false hasta decision explicita.
