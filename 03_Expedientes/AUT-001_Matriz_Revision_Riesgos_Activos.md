# AUT-001 - Matriz de Revision de Riesgos Activos

Estatus: revision provisional no mutante.

Fecha: 2026-07-02.

## Objeto

Revisar los 17 riesgos activos emitidos por `DO-LAB-RISK-001` en `06_Automatizacion/reportes/lab_risk_report.json`, sin alterar el reporte generado ni los archivos fuente.

## Resultado corto

- Riesgos activos revisados: 17.
- Severidad alta: 2.
- Severidad media: 15.
- Riesgos que ejecutan o autorizan transformacion: 0.
- Riesgos altos no tratados: 0.
- Riesgos que bloquean cierre tecnico provisional: 0.
- Riesgo residual real: precision del detector ante frases de prohibicion, bitacora y definicion de checks.

## Criterio de lectura

- `controlado_por_guardrail`: la evidencia vive en una regla de proteccion, una prohibicion, un fuera de alcance o una compuerta.
- `controlado_por_decision_registrada`: la evidencia corresponde a una decision ya registrada, no a una accion nueva.
- `controlado_por_historial`: la evidencia vive en bitacora o changelog; conserva valor historico, no autoridad directa.
- `requiere_refinamiento_detector`: el detector debe distinguir mejor contexto, pero no hay transformacion activa.
- Ningun tratamiento habilita modificacion de Canon, documentos oficiales, expedientes cerrados o reportes fuente.

## Matriz

| ID | Severidad | Fuente | Lectura | Tratamiento |
| --- | --- | --- | --- | --- |
| `AUT-RISK-ACT-001` | media | `02_Documentos/C-001_Especificacion_Tecnica_Auditor.md:52` | `C-001` declara fuera de alcance la importacion del Registro Historico como autoridad vigente. | `controlado_por_guardrail`; sugerir rebaja a advertencia de control. |
| `AUT-RISK-ACT-002` | media | `06_Automatizacion/README.md:27` | El README dice que la herramienta no puede usar Registro Historico como autoridad directa. | `controlado_por_guardrail`; detector debe reconocer contexto "No puede". |
| `AUT-RISK-ACT-003` | alta | `01_Canon/M-001_Auditoria_Arquitectonica.md:20` | Regla de auditoria que exige indicar si una intervencion modifica documentos, expedientes, estado o Canon. | `controlado_por_guardrail`; ya tratado como riesgo alto controlado. |
| `AUT-RISK-ACT-004` | media | `02_Documentos/C-001_Especificacion_Tecnica_Auditor.md:52` | Duplicado operativo de `AUT-RISK-ACT-001` por otro check. | `controlado_por_guardrail`; consolidar en refinamiento. |
| `AUT-RISK-ACT-005` | media | `03_Expedientes/AUT-001.md:46` | El expediente declara que la automatizacion no puede modificar Canon o documentos oficiales. | `controlado_por_guardrail`; no hay accion real. |
| `AUT-RISK-ACT-006` | media | `03_Expedientes/AUT-001_Mapa_Fase_Media_AAU.md:43` | Es la descripcion del check `MED-HISTORIAL`, no un uso real del historial. | `requiere_refinamiento_detector`; excluir definiciones de checks. |
| `AUT-RISK-ACT-007` | media | `03_Expedientes/AUT-001_Mapa_Fase_Media_AAU.md:65` | La fase media declara que no puede modificar Canon. | `controlado_por_guardrail`; no bloquea cierre tecnico. |
| `AUT-RISK-ACT-008` | media | `03_Expedientes/H-Xi.md:77` | `H-Xi` declara que no puede usarse para modificar Canon. | `controlado_por_guardrail`; conserva proteccion de hipotesis externa. |
| `AUT-RISK-ACT-009` | media | `05_Estado_Proyecto/DECISIONES.md:99` | Registra una promocion ya decidida de `SPEC-AUD-001_Candidata` a `C-001`. | `controlado_por_decision_registrada`; no es accion nueva. |
| `AUT-RISK-ACT-010` | media | `05_Estado_Proyecto/DECISION_Siguiente_Frente_Activo_B-001.5.md:58` | La decision no permite modificar Canon o documentos oficiales. | `controlado_por_guardrail`; no hay permiso de transformacion. |
| `AUT-RISK-ACT-011` | alta | `05_Estado_Proyecto/DECISION_Siguiente_Frente_Activo_B-001.5.md:56` | La decision no permite reabrir expedientes cerrados. | `controlado_por_guardrail`; ya tratado como riesgo alto controlado. |
| `AUT-RISK-ACT-012` | media | `05_Estado_Proyecto/DECISION_Siguiente_Frente_Activo_P-PI.md:57` | La decision no permite modificar Canon o documentos oficiales. | `controlado_por_guardrail`; no hay accion real. |
| `AUT-RISK-ACT-013` | media | `05_Estado_Proyecto/NIVEL_C_ESPECIFICACIONES.md:84` | La definicion de Nivel C prohibe modificar Canon. | `controlado_por_guardrail`; es restriccion de diseno. |
| `AUT-RISK-ACT-014` | media | `06_Automatizacion/README.md:27` | Duplicado operativo de `AUT-RISK-ACT-002` por otro check. | `controlado_por_guardrail`; consolidar en refinamiento. |
| `AUT-RISK-ACT-015` | media | `06_Automatizacion/README.md:25` | El README dice que la herramienta no puede promover hipotesis. | `controlado_por_guardrail`; no hay promocion real. |
| `AUT-RISK-ACT-016` | media | `CHANGELOG.md:143` | Bitacora de un objetivo anterior sobre prueba con Registro Historico como caso problematico. | `controlado_por_historial`; debe rebajarse como traza historica. |
| `AUT-RISK-ACT-017` | media | `CHANGELOG.md:74` | Bitacora de un objetivo anterior sobre decidir promocion de `SPEC-AUD-001_Candidata`. | `controlado_por_historial`; no es accion vigente. |

## Diagnostico

Los 17 riesgos activos no muestran una transformacion en curso. El detector cumple como alarma conservadora, pero todavia mezcla tres superficies distintas:

- regla de proteccion o prohibicion;
- bitacora historica o decision ya registrada;
- definicion de los checks del propio detector.

## Accion recomendada

Crear una ronda breve `AUT-RISK-REFINE-001` para que `DO-LAB-RISK-001` reconozca:

1. contexto de prohibicion: "no puede", "no permite", "fuera de alcance", "contenido prohibido" y "no cubre";
2. contexto historico o de bitacora: `CHANGELOG.md` y decisiones registradas ya aceptadas;
3. contexto meta: documentos que describen checks del propio detector.

Despues de esa ronda, `AUT-001` puede decidir cierre tecnico provisional con menos ruido operativo.
