# AUT-001 - Decision tablero de estado

Estatus: decision provisional de expediente.

Fecha: 2026-07-02.

## Decision

Se acepta `06_Automatizacion/lab_status_board.py` como `DO-STATE-BOARD-001`, tablero no mutante de estado del Laboratorio.

`AUT-001` queda abierto.

## Alcance

La decision cubre:

- existencia de una tercera herramienta no mutante;
- reporte sintetico de continuidad del Laboratorio;
- reportes conservados en `06_Automatizacion/reportes`;
- visibilidad de siguiente objetivo, expedientes y automatizacion disponible;
- continuidad del frente `AUT-001` tras pausa operativa de `HXI-001`.

## No cubre

La decision no cubre:

- cierre de `AUT-001`;
- ejecucion directa local confirmada con `python`;
- automatizacion completa del Auditor;
- transformaciones ejecutadas;
- autorizacion de cambios reales;
- modificacion de Canon o documentos oficiales;
- cierre o reapertura de expedientes.

## Consecuencia

El siguiente objetivo es definir integracion entre `DO-STATE-BOARD-001` y `DO-CHECK-MED-001` para un reporte combinado de continuidad y riesgos.
