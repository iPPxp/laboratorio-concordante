# AUT-001 - Comando Unico del Laboratorio

Estatus: especificacion provisional aceptada para corrida local unificada.

Fecha: 2026-07-02.

## Objeto

`DO-LAB-RUN-001` define un comando unico no mutante para ejecutar las herramientas activas de `AUT-001`.

## Alcance

- ejecutar `DO-CHECK-MIN-001`;
- ejecutar `DO-CHECK-MED-001`;
- ejecutar `DO-STATE-BOARD-001`;
- ejecutar `DO-LAB-CONTINUITY-001`;
- regenerar reportes Markdown y JSON;
- emitir `LAB_RUN_REPORT` como resumen de corrida.

## Fuera de alcance

- modificar Canon;
- modificar documentos oficiales;
- cerrar o reabrir expedientes;
- resolver hallazgos por si mismo;
- autorizar transformaciones.

## Artefacto ejecutable

- `06_Automatizacion/lab_run.py`

## Reportes esperados

- `06_Automatizacion/reportes/lab_run_report.md`
- `06_Automatizacion/reportes/lab_run_report.json`

## Uso esperado

```powershell
python 06_Automatizacion/lab_run.py
```

La salida esperada puede ser `ok`, `advertencia` o `bloqueado`. Mientras existan advertencias heredadas, el resultado debe conservar `advertencia` y recomendar `continuar_sin_transformar`.
