# AO-001 - Puente local de Confluencia y Equivalencia de proyecciones

Estatus: puente provisional aceptado.

Fecha: 2026-07-03.

ID: `AO-PPI-BRIDGE-001`.

Expediente padre: `AO-001`.

Antecedentes: `P-PI.0`, `P-PI.1`.

## Proposito

Avanzar los problemas de Confluencia y Equivalencia de proyecciones sin reabrir `P-PI.0` ni `P-PI.1`.

El puente usa `G_AO_OP-GOV-001`, `AO-CASE-BAT-001` y `AO-R4-GAMMA-USE-001` como evidencia local.

## Fuentes

- `03_Expedientes/P-PI_Marco_Inicial_Confluencia_Equivalencia.md`
- `03_Expedientes/P-PI_PPI-EQ-001_REPORT_LAYER_DO_CHECK.md`
- `03_Expedientes/P-PI_PPI-EQ-002_Completitud_A_C002.md`
- `03_Expedientes/P-PI_PPI-CONF-001_Rutas_Estado_Operativo.md`
- `03_Expedientes/AO-001_Prueba_Gamma_Externa.md`
- `03_Expedientes/AO-001_Casos_Prueba_Algebra_Operacional.md`
- `03_Expedientes/AO-001_Criterios_Uso_R4_Gamma_Fuera_AUD.md`

## Prueba local 1 - Equivalencia de proyecciones

ID: `AO-PPI-EQ-001`.

### Forma

```text
Pi_doc(A) ~ Pi_rep(A) ~ Pi_op(A)
```

donde:

- `Pi_doc` es proyeccion documental;
- `Pi_rep` es proyeccion de reporte;
- `Pi_op` es proyeccion operacional bajo `G_AO_OP-GOV-001`;
- `A` es un artefacto con estatus declarado.

### Criterio local

Las proyecciones son localmente equivalentes si conservan:

- identificador del artefacto;
- estatus;
- evidencia;
- decision asociada;
- permiso o ausencia de permiso;
- deuda resultante.

### Resultado

`AO-PPI-EQ-001` pasa en grado local para los casos `AO-CASE-001`, `AO-CASE-004` y `AO-CASE-006`.

No pasa como equivalencia global, porque faltan dominios externos y una semantica general de proyecciones.

## Prueba local 2 - Confluencia operacional

ID: `AO-PPI-CONF-001`.

### Forma

```text
ruta_estado(A) + ruta_decision(A) + ruta_reporte(A) -> salida compatible
```

### Criterio local

Hay confluencia local si las tres rutas:

- leen la misma evidencia;
- no aumentan autoridad;
- preservan restricciones;
- producen la misma clase de salida segura;
- registran deudas sin convertirlas en cierre.

### Resultado

`AO-PPI-CONF-001` pasa en grado local para:

- decision sin permiso de transformacion;
- deuda activa bloqueante;
- referencia historica transferida.

No pasa como confluencia global, porque no cubre rutas algebraicas generales ni casos externos.

## Uso de R4/Gamma

`R4-FORMAL-AUD-001` se usa solo como referencia formal local sobre trazas, decision fundada y ejecucion valida.

`GAMMA-FORMAL-AUD-001` se usa solo como prueba local controlada y puente de problema.

`G_AO_OP-GOV-001` provee el criterio local de operacion gobernada.

## Resultado

El puente produce avance sustantivo local:

- equivalencia local entre proyeccion documental, reporte y operacional;
- confluencia local entre ruta de estado, decision y reporte;
- separacion clara entre avance local y cierre global.

## No cubre

No reabre `P-PI.0`.

No reabre `P-PI.1`.

No cierra Confluencia global.

No cierra Equivalencia global de proyecciones.

No promueve R4/Gamma fuera de alcance local.

No modifica Documento 04.

No autoriza transformaciones materiales.

## Deudas abiertas

- semantica general de proyecciones;
- criterios de confluencia fuera del Laboratorio;
- relacion futura con `REPORT_LAYER`;
- posible formalizacion posterior en Documento 04.
