# AUT-001 - Decision de reactivacion de automatizacion

Estatus: decision provisional de expediente.

Fecha: 2026-07-02.

## Decision

Se reactiva `AUT-001` como frente activo inmediato del Laboratorio.

La reactivacion ocurre despues de pausar `HXI-001` y se mantiene dentro de automatizacion no mutante.

## Alcance

La decision permite:

- crear una herramienta de tablero operativo del laboratorio;
- conservar reportes en `06_Automatizacion/reportes`;
- leer estado, handoff y expedientes sin modificarlos;
- preparar una siguiente capa de visibilidad automatizada.

## No cubre

La decision no cubre:

- cierre de `AUT-001`;
- automatizacion completa del Auditor;
- transformaciones ejecutadas;
- autorizacion de cambios reales;
- modificacion de Canon o documentos oficiales;
- cierre o reapertura de expedientes;
- ejecucion directa local confirmada con `python`.

## Consecuencia

La accion inmediata es crear `DO-STATE-BOARD-001`, tablero no mutante de estado del laboratorio.
