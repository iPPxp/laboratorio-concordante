# LAB_RISK_REPORT

report_id: DO-LAB-RISK-20260706-153516
expediente: AUT-001
algoritmo: DO-LAB-RISK-001
resultado: advertencia_clasificada
recomendacion: mantener_cierre_operativo
transformacion_permitida: false

## Resumen por categoria

- riesgo_activo: 0
- advertencia_controlada: 25
- deuda_documental: 309
- advertencia_heredada: 63
- observacion: 61

## Resumen por severidad

- alta: 4
- media: 206
- baja: 248

## Resumen por contexto

- bitacora_historica: 15
- control_auditoria: 1
- decision_registrada: 37
- guardrail: 95
- meta_check: 12
- riesgo_real: 298

## Riesgos activos

- Sin riesgos activos clasificados.

## Advertencias controladas

- [media] minimo 02_Documentos/C-002_RFC_Operativo_Auditor_v0.md - historial_como_autoridad_posible: controlado_por_guardrail | contexto: guardrail
- [media] minimo 03_Expedientes/AUT-001_Mapa_Fase_Media_AAU.md - historial_como_autoridad_posible: controlado_por_guardrail | contexto: guardrail
- [media] minimo 03_Expedientes/AUT-001_Matriz_Revision_Riesgos_Activos.md - historial_como_autoridad_posible: controlado_por_guardrail | contexto: guardrail
- [media] minimo 06_Automatizacion/README.md - historial_como_autoridad_posible: controlado_por_guardrail | contexto: guardrail
- [media] minimo CHANGELOG.md - historial_como_autoridad_posible: controlado_por_historial | contexto: bitacora_historica
- [media] MED-NIVELES CHANGELOG.md - accion_de_nivel_sensible: controlado_por_historial | contexto: bitacora_historica | evidencia: - Actualizado el estado del proyecto: el siguiente objetivo es decidir si `SPEC-AUD-001_Candidata` se promueve a documento oficial de Nivel C.
- [alta] MED-CERRADOS CHANGELOG.md - expediente_cerrado_afectado: controlado_por_historial | contexto: bitacora_historica | evidencia: - Creado `HXI-001_Reapertura_Operativa.md` como `HXI-REOPEN-001`: `HXI-001` se reabre como frente activo inmediato para aplicar la compuerta de admision formal posterior.
- [alta] MED-NIVELES 01_Canon/M-001_Auditoria_Arquitectonica.md - accion_de_nivel_sensible: controlado_por_regla_de_auditoria | contexto: control_auditoria | evidencia: 8. Indicar si la intervencion modifica documentos, expedientes, estado o Canon.
- [alta] MED-NIVELES 02_Documentos/00_Naturaleza.md - accion_de_nivel_sensible: controlado_por_guardrail | contexto: guardrail | evidencia: Un expediente puede proponer. Una auditoria puede evaluar. Una decision puede aceptar, cerrar, congelar, rechazar o incorporar. Un documento oficial estabiliza contenido. El Canon limita como puede cambiar todo lo anterior.
- [alta] MED-NIVELES 02_Documentos/C-002_RFC_Operativo_Auditor_v0.md - accion_de_nivel_sensible: controlado_por_guardrail | contexto: guardrail | evidencia: - modificar Canon por inferencia;
- [media] MED-NIVELES 03_Expedientes/AO-001.md - accion_de_nivel_sensible: controlado_por_guardrail | contexto: guardrail | evidencia: - modificar Canon;
- [media] MED-NIVELES 03_Expedientes/AUT-001_Matriz_Revision_Riesgos_Activos.md - accion_de_nivel_sensible: controlado_por_definicion_de_check | contexto: meta_check | evidencia: | `AUT-RISK-ACT-003` | alta | `01_Canon/M-001_Auditoria_Arquitectonica.md:20` | Regla de auditoria que exige indicar si una intervencion modifica documentos, expedientes, estado o Canon. | `controlado_por_guardrail`; ya tratado como riesgo alto controlado. |
- [media] MED-NIVELES 03_Expedientes/AUT-001_Validacion_Cierre_Riesgos.md - accion_de_nivel_sensible: controlado_por_guardrail | contexto: guardrail | evidencia: - Ningun tratamiento modifica Canon, documentos oficiales o expedientes cerrados.
- [media] MED-NIVELES 03_Expedientes/AUT-001_Validacion_Revision_Riesgos_Activos.md - accion_de_nivel_sensible: controlado_por_guardrail | contexto: guardrail | evidencia: - Ningun tratamiento modifica Canon, documentos oficiales, expedientes cerrados ni reportes generados.
- [media] MED-NIVELES 03_Expedientes/H-Xi.md - accion_de_nivel_sensible: controlado_por_guardrail | contexto: guardrail | evidencia: - modificar Canon;
- [media] MED-NIVELES 03_Expedientes/HB-001_Deuda_Viva_H-B.md - accion_de_nivel_sensible: controlado_por_guardrail | contexto: guardrail | evidencia: - fundamento para modificar Canon;
- [media] MED-NIVELES 03_Expedientes/HXI-001_Criterios_Evaluacion.md - accion_de_nivel_sensible: controlado_por_guardrail | contexto: guardrail | evidencia: - modifica Canon o documentos oficiales;
- [media] MED-NIVELES 03_Expedientes/MOC-001_Auditoria_Siguientes_Rutas_Validas.md - accion_de_nivel_sensible: controlado_por_guardrail | contexto: guardrail | evidencia: - Ninguna ruta modifica Canon, Nivel C ni `Documento 04`.
- [media] MED-NIVELES 05_Estado_Proyecto/DECISIONES.md - accion_de_nivel_sensible: controlado_por_decision_registrada | contexto: decision_registrada | evidencia: Se promueve `SPEC-AUD-001_Candidata` a documento oficial de Nivel C como `02_Documentos/C-001_Especificacion_Tecnica_Auditor.md`.
- [media] MED-NIVELES 05_Estado_Proyecto/DECISION_Desactivacion_Vision_Papers.md - accion_de_nivel_sensible: controlado_por_guardrail | contexto: guardrail | evidencia: - usarlos como fuente para modificar Canon o documentos oficiales;
- [media] MED-NIVELES 05_Estado_Proyecto/DECISION_Siguiente_Frente_Activo_B-001.5.md - accion_de_nivel_sensible: controlado_por_guardrail | contexto: guardrail | evidencia: - modificar Canon o documentos oficiales
- [media] MED-NIVELES 05_Estado_Proyecto/DECISION_Siguiente_Frente_Activo_P-PI.md - accion_de_nivel_sensible: controlado_por_guardrail | contexto: guardrail | evidencia: - modificar Canon o documentos oficiales
- [media] MED-NIVELES 05_Estado_Proyecto/NIVEL_C_ESPECIFICACIONES.md - accion_de_nivel_sensible: controlado_por_guardrail | contexto: guardrail | evidencia: - modificar Canon
- [media] MED-HISTORIAL 06_Automatizacion/README.md - historial_como_autoridad_controlada: controlado_por_guardrail | contexto: guardrail | evidencia: - usar Registro Historico como autoridad directa;
- [media] MED-NIVELES 06_Automatizacion/README.md - accion_de_nivel_sensible: controlado_por_guardrail | contexto: guardrail | evidencia: - promover hipotesis;

## Deuda documental

- [baja] 03_Expedientes/AO-001_Auditoria_Cobertura_Externa_Amplia_001.md - estatus_ausente: No hay campo Estatus en las primeras 30 lineas.
- [baja] 03_Expedientes/AO-001_Auditoria_Cobertura_Externa_Amplia_001.md - referencia_no_materializada: 06_Automatizacion/reportes/ao_ext_cov_001_report.md
- [baja] 03_Expedientes/AO-001_Auditoria_Criterio_Autoridad_Global_001.md - estatus_ausente: No hay campo Estatus en las primeras 30 lineas.
- [baja] 03_Expedientes/AO-001_Auditoria_Criterio_Autoridad_Global_001.md - referencia_no_materializada: 06_Automatizacion/reportes/ao_authority_global_001_report.md
- [baja] 03_Expedientes/AO-001_Auditoria_Formalizacion_Amplia_Doc04.md - estatus_ausente: No hay campo Estatus en las primeras 30 lineas.
- [baja] 03_Expedientes/AO-001_Auditoria_Matriz_Condiciones_Cierre_Global_003.md - referencia_no_materializada: 06_Automatizacion/reportes/ao_ppi_bridge_003_report.md
- [baja] 03_Expedientes/AO-001_Auditoria_Matriz_Consolidada_Cierre_Global_004.md - estatus_ausente: No hay campo Estatus en las primeras 30 lineas.
- [baja] 03_Expedientes/AO-001_Auditoria_Matriz_Consolidada_Cierre_Global_004.md - referencia_no_materializada: 06_Automatizacion/reportes/ao_ppi_bridge_004_report.md
- [baja] 03_Expedientes/AO-001_Auditoria_Pruebas_AO-DOC04-WIDE_REPORT_LAYER.md - estatus_ausente: No hay campo Estatus en las primeras 30 lineas.
- [baja] 03_Expedientes/AO-001_Auditoria_Puente_Confluencia_Equivalencia_002.md - referencia_no_materializada: 06_Automatizacion/reportes/ao_ppi_bridge_002_report.md
- [baja] 03_Expedientes/AO-001_Auditoria_Relacion_AO_TCS_001.md - estatus_ausente: No hay campo Estatus en las primeras 30 lineas.
- [baja] 03_Expedientes/AO-001_Auditoria_Relacion_AO_TCS_001.md - referencia_no_materializada: 06_Automatizacion/reportes/ao_tcs_rel_001_report.md
- [baja] 03_Expedientes/AO-001_Auditoria_Serializacion_REPORT_LAYER_001.md - referencia_no_materializada: 06_Automatizacion/reportes/report_layer_serialization_report.md
- [baja] 03_Expedientes/AO-001_Cobertura_Externa_Amplia_001.md - referencia_no_materializada: 06_Automatizacion/reportes/ao_ext_cov_001_report.md
- [baja] 03_Expedientes/AO-001_Criterio_Autoridad_Global_001.md - referencia_no_materializada: 06_Automatizacion/reportes/ao_authority_global_001_report.md
- [baja] 03_Expedientes/AO-001_Decision_Cobertura_Externa_Amplia_001.md - estatus_ausente: No hay campo Estatus en las primeras 30 lineas.
- [baja] 03_Expedientes/AO-001_Decision_Criterio_Autoridad_Global_001.md - estatus_ausente: No hay campo Estatus en las primeras 30 lineas.
- [baja] 03_Expedientes/AO-001_Decision_Matriz_Condiciones_Cierre_Global_003.md - referencia_no_materializada: 06_Automatizacion/reportes/ao_ppi_bridge_003_report.md
- [baja] 03_Expedientes/AO-001_Decision_Matriz_Consolidada_Cierre_Global_004.md - estatus_ausente: No hay campo Estatus en las primeras 30 lineas.
- [baja] 03_Expedientes/AO-001_Decision_Puente_Confluencia_Equivalencia_002.md - referencia_no_materializada: 06_Automatizacion/reportes/ao_ppi_bridge_002_report.md
- ... 289 deudas documentales adicionales en JSON.

## Advertencias heredadas

- total: 63

## Siguientes acciones

- Mantener cierre operativo de AUT-001 con deuda documental visible.
- Mantener advertencias heredadas como deuda historica sin transformar.
- Mantener advertencias controladas visibles; no borrarlas del reporte.
- Normalizar referencias o estatus faltantes solo mediante decision posterior.
