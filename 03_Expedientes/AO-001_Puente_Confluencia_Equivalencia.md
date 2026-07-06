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
- `03_Expedientes/R001-001_Relacion_Formal_AO.md`

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

## Extension local R001-TB-001

ID: `R001-TB-001`.

`R001-TB-001` agrega una instancia tabular local del puente:

```text
Pi_tb(C, O_adm) = {(o, Phi(o)) | o en O_adm}
Eq_tb(C1, C2, O_adm) <=> Pi_tb(C1, O_adm) = Pi_tb(C2, O_adm)
```

Lectura para `AO-PPI-EQ-001`:

- `Pi_tb` funciona como una instancia local de `Pi_op`;
- `O_adm` funciona como testigo explicito;
- equivalencia trivial queda separada de equivalencia fuerte;
- no equivalencia y bloqueos se conservan como salidas seguras.

Lectura para `AO-PPI-CONF-001`:

- ruta de estado: `R001-001` como expediente tecnico provisional;
- ruta de decision: `R001-001_Decision_Integracion_Table_Checks.md` y decision posterior de `R001-TB-001`;
- ruta de reporte: `R001-TABLE-CHECK-001` con resultado `ok`;
- ninguna ruta aumenta autoridad ni habilita transformacion material.

Esta extension cierra solo la relacion formal local con `R001`. No cierra Confluencia global ni Equivalencia global de proyecciones.

## Ruta Doc04 y pruebas externas

ID: `AO-DOC04-FORM-CHK-001` / `AO-CONF-EXT-OPTIONS-001`.

La evaluacion posterior de `R001-TB-001` fija una ruta defensiva:

- `Pi_tb` y `Eq_tb` pueden conservarse como candidata formal para Documento 04;
- Documento 04 no se modifica todavia;
- `EXT-CONF-001` debe ejecutarse primero como prueba sintetica no mutante fuera del Laboratorio;
- una incorporacion documental posterior requiere auditoria y decision separadas.

La primera prueba externa recomendada es:

```text
EXT-CONF-001 = normalizacion CSV vs normalizacion JSON sobre tabla sintetica
```

El criterio esperado conserva testigo, proyeccion, salida segura y clasificacion de divergencia sin aumentar autoridad.

Ejecucion posterior:

- `AO-EXT-CONF-EXEC-001` ejecuta `EXT-CONF-001` sobre tabla sintetica CSV/JSON;
- agrega `EXT-CONF-002` sobre paquete de software de juguete como segunda prueba externa no regulada;
- reporta 7 casos aprobados y 0 fallos;
- mantiene abiertas Confluencia global, Equivalencia global, formalizacion posterior amplia de Documento 04, exportacion general de R4/Gamma y maduracion posterior de `TCS-001`.

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
- relacion futura entre `R001-TB-001` y una teoria general de proyecciones tabulares.
- decidir si se requieren mas pruebas externas antes de cualquier incorporacion documental;
- auditoria especifica del texto a incorporar si se abre una ruta futura de Documento 04.
