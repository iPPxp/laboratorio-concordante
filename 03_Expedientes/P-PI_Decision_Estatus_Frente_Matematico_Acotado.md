# P-PI - Decision de estatus del frente matematico acotado

Estatus: decision provisional de expediente.

ID: `D-2026-07-03-001`.

Fecha: 2026-07-03.

Expedientes afectados:

- `P-PI.0`
- `P-PI.1`

Casos ejecutados asociados:

- `P-PI_PPI-EQ-001_REPORT_LAYER_DO_CHECK.md`
- `P-PI_PPI-EQ-002_Completitud_A_C002.md`
- `P-PI_PPI-CONF-001_Rutas_Estado_Operativo.md`

Marco asociado: `P-PI_Marco_Inicial_Confluencia_Equivalencia.md`.

Auditoria asociada: `P-PI_Auditoria_Marco_Inicial_Confluencia_Equivalencia.md`.

## Decision

Se confirma que `P-PI.0` y `P-PI.1` quedan activos de forma acotada.

Estatus asignado:

```text
P-PI.0 = activo acotado para Equivalencia de proyecciones
P-PI.1 = activo acotado para Confluencia
```

La decision no altera el marco, no modifica Canon y no convierte los tres casos locales en cierre general.

## Alcance permitido

La decision permite:

- mantener `PPI-EQ-001` como caso local de equivalencia minima;
- mantener `PPI-EQ-002` como caso local de equivalencia documental-operativa;
- mantener `PPI-CONF-001` como caso local de confluencia de continuidad operativa;
- usar esos tres casos como base para trabajo posterior acotado;
- actualizar el estado del proyecto para reflejar que el frente ya no esta en transicion.

## Alcance no permitido

La decision no permite:

- cerrar Confluencia;
- cerrar Equivalencia de proyecciones;
- cerrar `P-PI.0` o `P-PI.1`;
- declarar propiedades globales de `~_C`;
- promover el marco inicial al Documento 02;
- tratar `PPI-CONF-001` como confluencia formal general;
- tratar `PPI-EQ-001` o `PPI-EQ-002` como cierre del problema general.

## Motivo

Los tres casos locales ya fueron ejecutados y dejan suficiente continuidad operativa para que el frente quede estabilizado en estado acotado.

La decision evita mantener el estado del proyecto en una pseudo-pausa intermedia cuando ya hay casos ejecutados y relaciones contextuales disponibles.

## Consecuencia operativa

`P-PI.0` y `P-PI.1` siguen activos, pero ahora como frente estabilizado.

La ruta futura inmediata es de seguimiento, no de reactivacion:

1. consolidar si hace falta una formalizacion adicional;
2. conservar las deudas abiertas;
3. no reabrir la pausa por inercia;
4. no elevar el frente a cierre general sin otra decision.

## Deudas que permanecen

- Definir si `~_C` debe tener propiedades formales mas fuertes en algun contexto posterior.
- Decidir si el marco inicial debe permanecer local o migrar a una seccion futura de `02_Fundamentos_Matematicos.md`.
- Mantener Confluencia y Equivalencia de proyecciones como problemas abiertos.
- Mantener inactivos los vision papers.

## Veredicto

`P-PI.0`: activo acotado.

`P-PI.1`: activo acotado.

La decision queda registrada como cierre de transicion del frente, no como cierre de los problemas.
