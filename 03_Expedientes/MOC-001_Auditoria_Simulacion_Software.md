# MOC-001 - Auditoria de simulacion y software

ID: `MOC-AUD-SIM-SW-001`.

Fecha: 2026-07-05.

Resultado: favorable con restricciones.

## Objetos auditados

- `03_Expedientes/MOC-001_Casos_No_Clinicos.md`.
- `06_Automatizacion/moc_eval.py`.
- `06_Automatizacion/fixtures/moc_cases.json`.
- `06_Automatizacion/test_moc_eval.py`.

## Verificacion

- La bateria es sintetica y no clinica.
- El software es no mutante.
- Los reportes Markdown y JSON se generan en `06_Automatizacion/reportes`.
- La corrida no autoriza transformaciones.
- La integracion a `DO-LAB-RUN-001` queda como lectura/reporte.
- Se prueban salidas `redundante`, `util_acotado`, `limitado`, `no_comparable` y `bloqueado`.
- Se simulan al menos tres evaluadores por caso.

## Hallazgos

No hay hallazgos bloqueantes.

## Deudas

- Mantener `MOC-EVAL-001` como simulacion local, no como validez empirica general.
- Ampliar casos solo mediante decision posterior si se sale del dominio sintetico no clinico.

## Dictamen

Procede aceptar la simulacion no mutante `MOC-EVAL-001`.
