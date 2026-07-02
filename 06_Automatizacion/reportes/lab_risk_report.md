# LAB_RISK_REPORT

report_id: DO-LAB-RISK-20260701-205808
expediente: AUT-001
algoritmo: DO-LAB-RISK-001
resultado: advertencia_clasificada
recomendacion: preparar_cierre_tecnico_provisional
transformacion_permitida: false

## Resumen por categoria

- riesgo_activo: 0
- advertencia_controlada: 17
- deuda_documental: 18
- advertencia_heredada: 47
- observacion: 0

## Resumen por severidad

- alta: 2
- media: 31
- baja: 49

## Resumen por contexto

- bitacora_historica: 2
- control_auditoria: 1
- decision_registrada: 2
- guardrail: 29
- meta_check: 1
- riesgo_real: 47

## Riesgos activos

- Sin riesgos activos clasificados.

## Advertencias controladas

- [media] minimo 02_Documentos/C-001_Especificacion_Tecnica_Auditor.md - historial_como_autoridad_posible: controlado_por_guardrail | contexto: guardrail
- [media] minimo 06_Automatizacion/README.md - historial_como_autoridad_posible: controlado_por_guardrail | contexto: guardrail
- [alta] MED-NIVELES 01_Canon/M-001_Auditoria_Arquitectonica.md - accion_de_nivel_sensible: controlado_por_regla_de_auditoria | contexto: control_auditoria | evidencia: 8. Indicar si la intervencion modifica documentos, expedientes, estado o Canon.
- [media] MED-HISTORIAL 02_Documentos/C-001_Especificacion_Tecnica_Auditor.md - historial_como_autoridad: controlado_por_guardrail | contexto: guardrail | evidencia: - importacion de Registro Historico como autoridad vigente
- [media] MED-NIVELES 03_Expedientes/AUT-001.md - accion_de_nivel_sensible: controlado_por_guardrail | contexto: guardrail | evidencia: - modificar Canon o documentos oficiales;
- [media] MED-HISTORIAL 03_Expedientes/AUT-001_Mapa_Fase_Media_AAU.md - historial_como_autoridad: controlado_por_definicion_de_check | contexto: meta_check | evidencia: - `MED-HISTORIAL`: Registro Historico o `SRC-*` usado como autoridad vigente.
- [media] MED-NIVELES 03_Expedientes/AUT-001_Mapa_Fase_Media_AAU.md - accion_de_nivel_sensible: controlado_por_guardrail | contexto: guardrail | evidencia: - modificar Canon;
- [media] MED-NIVELES 03_Expedientes/H-Xi.md - accion_de_nivel_sensible: controlado_por_guardrail | contexto: guardrail | evidencia: - modificar Canon;
- [media] MED-NIVELES 05_Estado_Proyecto/DECISIONES.md - accion_de_nivel_sensible: controlado_por_decision_registrada | contexto: decision_registrada | evidencia: Se promueve `SPEC-AUD-001_Candidata` a documento oficial de Nivel C como `02_Documentos/C-001_Especificacion_Tecnica_Auditor.md`.
- [media] MED-NIVELES 05_Estado_Proyecto/DECISION_Siguiente_Frente_Activo_B-001.5.md - accion_de_nivel_sensible: controlado_por_guardrail | contexto: guardrail | evidencia: - modificar Canon o documentos oficiales
- [alta] MED-CERRADOS 05_Estado_Proyecto/DECISION_Siguiente_Frente_Activo_B-001.5.md - expediente_cerrado_afectado: controlado_por_guardrail | contexto: guardrail | evidencia: - reabrir `B-001`, `CP-001`, `EF-001`, Procedimiento o Auditoria
- [media] MED-NIVELES 05_Estado_Proyecto/DECISION_Siguiente_Frente_Activo_P-PI.md - accion_de_nivel_sensible: controlado_por_guardrail | contexto: guardrail | evidencia: - modificar Canon o documentos oficiales
- [media] MED-NIVELES 05_Estado_Proyecto/NIVEL_C_ESPECIFICACIONES.md - accion_de_nivel_sensible: controlado_por_guardrail | contexto: guardrail | evidencia: - modificar Canon
- [media] MED-HISTORIAL 06_Automatizacion/README.md - historial_como_autoridad: controlado_por_guardrail | contexto: guardrail | evidencia: - usar Registro Historico como autoridad directa;
- [media] MED-NIVELES 06_Automatizacion/README.md - accion_de_nivel_sensible: controlado_por_guardrail | contexto: guardrail | evidencia: - promover hipotesis;
- [media] MED-HISTORIAL CHANGELOG.md - historial_como_autoridad: controlado_por_historial | contexto: bitacora_historica | evidencia: - Actualizado el estado del proyecto: el siguiente objetivo es probar `R4-CANDIDATA` con un expediente que usa Registro Historico como autoridad directa.
- [media] MED-NIVELES CHANGELOG.md - accion_de_nivel_sensible: controlado_por_historial | contexto: bitacora_historica | evidencia: - Actualizado el estado del proyecto: el siguiente objetivo es decidir si `SPEC-AUD-001_Candidata` se promueve a documento oficial de Nivel C.

## Deuda documental

- [media] 03_Expedientes/AUT-001.md - referencia_no_materializada: 06_Automatizacion/reportes/README.md
- [media] 03_Expedientes/AUT-001.md - referencia_no_materializada: 06_Automatizacion/reportes/do_check_min_claves.md
- [media] 03_Expedientes/AUT-001.md - referencia_no_materializada: 06_Automatizacion/reportes/do_check_min_repo.md
- [media] 03_Expedientes/AUT-001_Validacion_DO-CHECK-MIN.md - referencia_no_materializada: 06_Automatizacion/reportes/do_check_min_claves.md
- [media] 03_Expedientes/AUT-001_Validacion_DO-CHECK-MIN.md - referencia_no_materializada: 06_Automatizacion/reportes/do_check_min_repo.md
- [media] 05_Estado_Proyecto/ESTADO_ACTUAL.md - estatus_ausente: No hay campo Estatus en las primeras 30 lineas.
- [media] 06_Automatizacion/README.md - referencia_no_materializada: reportes/do_check_min_claves.md
- [media] 06_Automatizacion/README.md - referencia_no_materializada: reportes/do_check_min_repo.md
- [baja] 03_Expedientes/AUD-001_Casos_Prueba_Auditor.md - referencia_no_materializada: ROADMAP.md
- [baja] 03_Expedientes/AUD-001_Simulaciones.md - reporte_normalizado_incompleto: Faltan campos esperados en una definicion de reporte: descripcion, estatus_afirmacion, deudas_generadas
- [baja] 03_Expedientes/REC-001_Auditoria_Reconciliacion.md - referencia_no_materializada: v1.0.0/fase2
- [baja] 03_Expedientes/REC-001_Mapa_Reconciliacion_Canon_Baselines.md - referencia_no_materializada: v1.0.0/fase2
- [media] 05_Estado_Proyecto/DECISIONES.md - referencia_no_materializada: ROADMAP.md
- [media] 05_Estado_Proyecto/DECISION_Siguiente_Frente_Activo_B-001.5.md - referencia_no_materializada: ROADMAP.md
- [media] 05_Estado_Proyecto/DECISION_Siguiente_Frente_Activo_P-PI.md - referencia_no_materializada: ROADMAP.md
- [media] 05_Estado_Proyecto/ESTADO_ACTUAL.md - estatus_ausente: No hay campo Estatus en las primeras 30 lineas.
- [media] 05_Estado_Proyecto/ESTADO_ACTUAL.md - referencia_no_materializada: ROADMAP.md
- [media] HANDOFF.md - referencia_no_materializada: ROADMAP.md

## Advertencias heredadas

- total: 47

## Siguientes acciones

- Decidir cierre tecnico provisional si no quedan riesgos activos reales.
- Mantener advertencias heredadas como deuda historica sin transformar.
- Mantener advertencias controladas visibles; no borrarlas del reporte.
- Normalizar referencias o estatus faltantes solo mediante decision posterior.
