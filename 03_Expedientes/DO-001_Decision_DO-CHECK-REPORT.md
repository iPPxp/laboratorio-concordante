# DO-001 - Decision sobre DO_CHECK_REPORT

Estatus: decision provisional de expediente.

Expediente padre: `DO-001`.

Fecha: 2026-07-01.

Objeto: relacion entre `DO_CHECK_REPORT` y `OPERATOR_REPORT`.

## Decision

`DO_CHECK_REPORT` permanece como reporte propio de `DO-001`.

No se integra todavia a `OPERATOR_REPORT` y no amplia por si mismo el contrato provisional de `AUD-001`.

## Fundamento

- `DO-CHECK-001` opera como verificador documental no mutante de trazabilidad, estatus y permisos.
- `OPERATOR_REPORT` pertenece al contrato provisional del Auditor en `AUD-001`.
- Los operadores cubiertos por `OPERATOR_REPORT` son `Mp`, `Cr`, `D`, `Tr` y `tau`.
- `AUD-001_Contrato_Reportes.md` no define un operador `DO-CHECK`.
- Integrar `DO_CHECK_REPORT` sin ampliar el contrato mezclaria una superficie documental de `DO-001` con operadores internos del Auditor.

## Alcance

Esta decision cubre:

- estatus provisional de `DO_CHECK_REPORT`
- relacion actual con `OPERATOR_REPORT`
- compatibilidad parcial entre campos
- siguiente objetivo operativo de `DO-001`

Esta decision no cubre:

- ampliacion de `AUD-001_Contrato_Reportes.md`
- creacion de un operador `DO-CHECK` dentro de `AUD-001`
- autorizacion de `Tr_ejecucion`
- regla local para ejecutar actualizaciones de estado
- cierre de `DO-001`

## Mapa de compatibilidad parcial

Este mapa es conceptual. No transforma `DO_CHECK_REPORT` en `OPERATOR_REPORT`.

| Campo de DO_CHECK_REPORT | Compatibilidad con OPERATOR_REPORT | Nota |
| --- | --- | --- |
| `report_id` | compatible | identificador de reporte |
| `expediente` | compatible | expediente emisor |
| `objetivo` | parcial con `caso` | objetivo documental no equivale siempre a caso de prueba |
| `modo` | sin equivalente directo | no es operador `Mp`, `Cr`, `D`, `Tr` ni `tau` |
| `resultado` | parcial con `resultado` | vocabularios distintos |
| `tipo` | parcial con `tipo` | algunas categorias coinciden conceptualmente |
| `ubicacion` | compatible | lugar del hallazgo |
| `descripcion` | compatible | explicacion breve |
| `evidencia` | compatible | evidencia local o estructura minima |
| `estatus_afirmacion` | compatible | usa categorias de `M-000` |
| `fuentes_leidas` | parcial con `dependencias` | fuentes leidas no siempre son dependencias operativas |
| `dependencias` | compatible | fuentes o reglas usadas |
| `referencias_no_materializadas` | parcial con `deudas_generadas` | confirma o genera deuda conceptual |
| `expedientes_cerrados_afectados` | sin equivalente directo | campo propio de auditoria documental |
| `problemas_abiertos_afectados` | sin equivalente directo | campo propio de auditoria documental |
| `deudas_generadas` | compatible | deudas derivadas del reporte |
| `recomendacion` | parcial con `decision_permitida` | no equivale a `decision_emitida` |
| `cambios_propuestos` | parcial con `alternativas_no_decididas` | propuesta documental no ejecutada |
| `transformacion_permitida` | compatible | en `DO-CHECK-001` debe permanecer `false` |

## Reglas derivadas

- `DO_CHECK_REPORT` no puede ocupar el lugar de `OPERATOR_REPORT` en `AUD-001`.
- `DO_CHECK_REPORT` puede ser leido por una decision posterior como evidencia documental.
- `DO_CHECK_REPORT` no emite `decision_emitida` y no reemplaza a `D_REPORT`.
- `DO_CHECK_REPORT` no ejecuta `Tr` y no autoriza `Tr_ejecucion`.
- Cualquier integracion futura exige decision explicita y ampliacion del contrato de `AUD-001`.

## Consecuencia

`DO-CHECK-001` queda estabilizado provisionalmente como superficie documental no mutante de `DO-001`.

El siguiente objetivo operativo pasa a definir la regla local de permiso para pasar de propuesta de actualizacion a actualizacion ejecutada.

## Criterio de cierre

Esta decision queda registrada si:

- existe este archivo asociado a `DO-001`
- `DO-001` referencia la decision
- `DO-001_DO-CHECK-001.md` registra la relacion vigente con `OPERATOR_REPORT`
- el estado del proyecto registra el nuevo objetivo operativo

Estado actual: cumplido.
