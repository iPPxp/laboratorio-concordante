# AUT-001 - Tablero de estado del Laboratorio

Estatus: especificacion provisional de expediente.

Identificador: `DO-STATE-BOARD-001`.

Fecha: 2026-07-02.

## Proposito

Definir una herramienta no mutante que lea el estado vigente del Laboratorio y emita un tablero resumido de continuidad.

## Implementacion

- Script: `06_Automatizacion/lab_status_board.py`.
- Reporte Markdown: `06_Automatizacion/reportes/lab_status_board.md`.
- Reporte JSON: `06_Automatizacion/reportes/lab_status_board.json`.

## Entradas minimas

- `CURRENT_STATE.md`.
- `05_Estado_Proyecto/ESTADO_ACTUAL.md`.
- `HANDOFF.md`.
- `README.md`.

## Salida esperada

El tablero debe reportar:

- ultimo expediente cerrado;
- ultimo expediente tecnico cerrado;
- ultima decision operativa;
- proximo objetivo;
- expedientes abiertos, cerrados y congelados;
- herramientas de automatizacion existentes;
- transformacion permitida siempre en `false`.

## Fuera de alcance

La herramienta no puede:

- modificar archivos objetivo;
- decidir cierre o apertura de expedientes;
- promover hipotesis;
- modificar Canon o documentos oficiales;
- autorizar transformaciones;
- sustituir `DO-CHECK-MED-001`.

## Resultado esperado

`DO-STATE-BOARD-001` debe funcionar como capa de visibilidad operativa encima de `DO-CHECK-MIN-001` y `DO-CHECK-MED-001`.
