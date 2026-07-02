# AUT-001 - Continuidad Integrada del Laboratorio

Estatus: especificacion provisional aceptada para automatizacion media inicial.

Fecha: 2026-07-02.

## Objeto

`DO-LAB-CONTINUITY-001` integra el tablero de estado `DO-STATE-BOARD-001` con el chequeo medio `DO-CHECK-MED-001` en un reporte unico de continuidad.

## Alcance

- leer estado operativo vigente;
- ejecutar lectura de tablero;
- ejecutar lectura media de riesgos;
- consolidar resultado, recomendacion y hallazgos;
- emitir salida Markdown o JSON;
- mantener `transformacion_permitida: false`.

## Fuera de alcance

- modificar Canon;
- modificar documentos oficiales;
- cerrar o reabrir expedientes;
- resolver advertencias por si mismo;
- admitir hipotesis externas;
- sustituir decisiones registradas.

## Artefacto ejecutable

- `06_Automatizacion/lab_continuity_report.py`

## Reportes esperados

- `06_Automatizacion/reportes/lab_continuity_report.md`
- `06_Automatizacion/reportes/lab_continuity_report.json`

## Resultado esperado

El resultado integrado puede ser `ok`, `advertencia` o `bloqueado`.

Mientras el chequeo medio herede advertencias historicas o documentales, el resultado integrado debe conservar `advertencia` y recomendar `continuar_sin_transformar`.
