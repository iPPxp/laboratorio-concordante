# AUT-001 - Decision de estatus MVP minimo

Estatus: decision provisional de expediente.

Fecha: 2026-07-01.

## Decision

Se acepta `06_Automatizacion/do_check_min.py` como automatizacion minima provisional del Laboratorio.

`AUT-001` queda abierto para endurecimiento y validacion directa local, pero el objetivo minimo de tener una herramienta no mutante con reporte conservado se considera cumplido provisionalmente.

## Alcance

La decision cubre:

- existencia de una herramienta ejecutable minima;
- reportes conservados en `06_Automatizacion/reportes`;
- lectura no mutante de archivos Markdown;
- resultado `ok` en archivos clave;
- resultado `advertencia` en barrido completo, sin permiso de transformacion.

## No cubre

La decision no cubre:

- automatizacion media o completa del Auditor;
- ejecucion directa confirmada desde terminal local;
- cierre de `AUT-001`;
- cierre o reapertura de expedientes;
- promocion de hipotesis;
- modificacion de Canon o documentos oficiales;
- paso automatico a psicologia.

## Consecuencia

El Laboratorio ya cuenta con una compuerta minima de lectura y reporte.

El siguiente objetivo recomendado es validar la ejecucion directa de `do_check_min.py` cuando el entorno lo permita y despues elegir si avanzar a psicologia u otro frente.
