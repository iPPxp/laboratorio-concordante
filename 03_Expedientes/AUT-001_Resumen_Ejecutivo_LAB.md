# AUT-001 - Resumen Ejecutivo Automatico del Laboratorio

Estatus: especificacion provisional aceptada para sintesis ejecutiva no mutante.

Fecha: 2026-07-02.

## Objeto

`DO-LAB-SUMMARY-001` produce un resumen ejecutivo automatico a partir de `DO-LAB-RUN-001`, `DO-LAB-RISK-001`, el tablero de estado y el estado vigente del repositorio.

## Alcance

- leer reportes JSON existentes;
- leer `CURRENT_STATE.md` y `ESTADO_ACTUAL.md`;
- sintetizar estado operativo, riesgos, corrida y siguientes acciones;
- emitir salida Markdown o JSON;
- mantener `transformacion_permitida: false`.

## Fuera de alcance

- resolver hallazgos;
- cerrar `AUT-001`;
- autorizar transformaciones;
- modificar Canon o documentos oficiales.

## Artefacto ejecutable

- `06_Automatizacion/lab_executive_summary.py`

## Reportes esperados

- `06_Automatizacion/reportes/lab_executive_summary.md`
- `06_Automatizacion/reportes/lab_executive_summary.json`
