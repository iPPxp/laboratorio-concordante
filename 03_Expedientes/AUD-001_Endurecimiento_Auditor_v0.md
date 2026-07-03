# AUD-001 - Endurecimiento del Auditor v0

Estatus: endurecimiento tecnico inicial.

Fecha: 2026-07-02.

Expediente padre: `AUD-001`.

Implementacion: `06_Automatizacion/auditor_v0.py`.

## Motivo

Despues de aceptar la implementacion no mutante inicial, el siguiente riesgo era que una entrada mal formada hiciera fallar el auditor antes de emitir reporte.

Este endurecimiento agrega validacion interna sin activar transformaciones y sin depender de nuevos fixtures JSON mientras esa salida queda en pausa temporal.

## Cambios

- Validacion de forma minima de casos antes de evaluarlos.
- Bloqueo seguro para casos mal formados.
- Validacion interna de campos de `OPERATOR_REPORT`.
- Deteccion de `case_id` duplicado.
- Registro de `schema_errors` en el resumen del reporte.
- Bloqueo temporal de salida JSON y carga externa JSON desde la interfaz de linea de comando.
- Pruebas unitarias para entradas mal formadas, duplicados y permiso indebido de transformacion.

## Invariantes conservadas

- `transformacion_permitida` permanece `false`.
- `Tr_ejecucion` no queda habilitado.
- Los diez casos obligatorios siguen cubiertos.
- Los reportes no cierran `AUD-001`.
- No se promueve `REPORT_LAYER`.
- No se crean, cargan ni emiten artefactos JSON durante la pausa temporal de JSON.

## Pruebas esperadas

```powershell
python -m unittest 06_Automatizacion/test_auditor_v0.py
python -m py_compile 06_Automatizacion/auditor_v0.py 06_Automatizacion/test_auditor_v0.py
python 06_Automatizacion/auditor_v0.py --format md
```

## Deuda siguiente

- Agregar fixtures externos cuando se reactive JSON.
- Separar esquema formal de reportes en documento propio si `AUD-001` lo requiere.
- Ampliar entradas documentales no automata.
