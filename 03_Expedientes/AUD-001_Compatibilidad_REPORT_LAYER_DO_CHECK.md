# AUD-001 - Compatibilidad minima entre REPORT_LAYER y DO_CHECK_REPORT

Estatus: puente conceptual provisional de expediente.

ID: `COMPAT-RL-DO-CHECK-001`.

Expediente padre: `AUD-001`.

Objeto: relacion entre `REPORT-LAYER-CAND-001` y `DO_CHECK_REPORT`.

## Proposito

Definir una compatibilidad minima de lectura entre `REPORT_LAYER` y `DO_CHECK_REPORT`.

Este puente no integra `DO_CHECK_REPORT` a `OPERATOR_REPORT`, no modifica `DO-001`, no amplia automaticamente `AUD-001_Contrato_Reportes.md` y no convierte `REPORT_LAYER` en especificacion oficial.

## Fuentes locales

- `03_Expedientes/AUD-001_REPORT_LAYER_Candidata.md`
- `03_Expedientes/AUD-001_Decision_Alcance_REPORT_LAYER.md`
- `03_Expedientes/DO-001_DO-CHECK-001.md`
- `03_Expedientes/DO-001_Decision_DO-CHECK-REPORT.md`
- `02_Documentos/C-001_Especificacion_Tecnica_Auditor.md`

## Decision de frontera

`DO_CHECK_REPORT` puede ser leido por `REPORT_LAYER` solo como evidencia documental no mutante.

No puede ocupar el lugar de:

- `OPERATOR_REPORT`;
- reporte de ejecucion;
- decision formal;
- permiso operativo;
- verificacion posterior de una transformacion.

## Lectura permitida

Una lectura futura puede proyectar `DO_CHECK_REPORT` a `REPORT_ITEM` si conserva esta restriccion:

```text
operador_abstracto = calculo
clase_reporte = sin_hallazgo_bloqueante | calculo_falla
transformacion_permitida = false
decision_emitida = no_aplica
```

El resultado puede informar a una decision posterior, pero no decide por si mismo.

## Mapa minimo de campos

| `DO_CHECK_REPORT` | `REPORT_ITEM` | Tipo de compatibilidad |
| --- | --- | --- |
| `report_id` | `report_id` | directa |
| `objetivo` | `objeto` | parcial |
| `resultado` | `resultado` | parcial |
| `tipo` | `tipo_hallazgo` | parcial |
| `ubicacion` | `ubicacion` | directa |
| `descripcion` | `descripcion` | directa |
| `evidencia` | `evidencia` | directa |
| `estatus_afirmacion` | `estatus_afirmacion` | directa |
| `fuentes_leidas` | `dependencias` | parcial |
| `dependencias` | `dependencias` | directa |
| `referencias_no_materializadas` | `deudas_generadas` | parcial |
| `deudas_generadas` | `deudas_generadas` | directa |
| `recomendacion` | `decisiones_permitidas` | parcial |
| `cambios_propuestos` | evidencia o deudas | parcial |
| `transformacion_permitida` | `transformacion_permitida` | directa |

Campos sin traslado directo:

- `modo`;
- `expedientes_cerrados_afectados`;
- `problemas_abiertos_afectados`.

Estos campos permanecen propios de `DO_CHECK_REPORT` y solo pueden citarse como evidencia.

## Reglas de compatibilidad

### 1. No absorcion

`REPORT_LAYER` no absorbe `DO_CHECK_REPORT`.

Solo puede leerlo como entrada documental si una decision posterior lo permite.

### 2. No permiso

Si `DO_CHECK_REPORT.transformacion_permitida = false`, el `REPORT_ITEM` derivado debe conservar `transformacion_permitida = false`.

### 3. No decision

`DO_CHECK_REPORT.recomendacion` puede proyectarse a `decisiones_permitidas`, pero no a `decision_emitida`.

### 4. No ejecucion

`DO_CHECK_REPORT.cambios_propuestos` puede registrarse como propuesta o deuda, pero no como transformacion ejecutada.

### 5. No promocion

Este puente no mueve `DO_CHECK_REPORT` a `AUD-001_Contrato_Reportes.md` ni a `C-001`.

## Uso permitido

El puente permite:

- comparar reportes documentales con `REPORT_LAYER`;
- preparar una validacion futura de herramienta no mutante;
- identificar que campos faltarian para una integracion real;
- conservar la frontera entre recomendacion y decision.

## Uso prohibido

El puente no permite:

- ejecutar cambios desde un `DO_CHECK_REPORT`;
- tratar `aprobar_lectura` como `aprobar`;
- convertir `cambios_propuestos` en `Tr_ejecucion`;
- cerrar expedientes;
- actualizar estado sin permiso;
- modificar documentos oficiales.

## Resultado

La compatibilidad actual queda limitada a lectura y comparacion.

No hay integracion contractual completa.

## Siguiente paso

Si se busca integracion real, abrir una decision separada para ampliar el contrato de `AUD-001` o crear una especificacion de adaptador.
