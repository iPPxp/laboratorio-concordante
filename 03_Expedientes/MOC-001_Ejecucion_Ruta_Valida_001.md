# MOC-001 - Ejecucion de primera ruta valida

ID: `MOC-ROUTE-EXEC-001`.

Fecha: 2026-07-05.

Estatus: ejecucion local aceptable, no canonica.

## Ruta ejecutada

Se ejecuta la primera ruta valida declarada en `MOC-001`:

```text
probar Xi_eval, estados metricos, protocolo de evaluacion y software no mutante con casos sinteticos no clinicos
```

## Evidencia ejecutada

Reportes regenerados:

- `06_Automatizacion/reportes/moc_eval_report.md`.
- `06_Automatizacion/reportes/moc_eval_report.json`.
- `06_Automatizacion/reportes/lab_run_report.md`.
- `06_Automatizacion/reportes/lab_run_report.json`.
- `06_Automatizacion/reportes/lab_risk_report.md`.
- `06_Automatizacion/reportes/lab_risk_report.json`.

Pruebas ejecutadas:

- `06_Automatizacion/test_moc_eval.py`.
- `06_Automatizacion/lab_run.py`.

## Resultado MOC-EVAL-001

- casos ejecutados: 7.
- casos aprobados: 7.
- casos fallidos: 0.
- hallazgos: 0.
- transformacion permitida: false.

Cobertura de `Xi_eval_MOC`:

- `MOC-CASE-001`: `redundante`.
- `MOC-CASE-002`: `util_acotado`.
- `MOC-CASE-003`: `limitado`.
- `MOC-CASE-004`: `no_comparable`.
- `MOC-CASE-005`: `bloqueado`.
- `MOC-CASE-006`: `util_acotado`.
- `MOC-CASE-007`: `util_acotado`.

Cobertura de estados MOC:

- `concordancia_local`.
- `concordancia_parcial`.
- `friccion_operativa`.
- `discordancia_global`.
- `bloqueo_de_concordancia`.
- `no_comparable`.

Resultado de protocolo de evaluadores:

- coincidencia exacta: 4.
- coincidencia parcial: 3.
- desacuerdo justificado: 0.

## Resultado de corrida del Laboratorio

`DO-LAB-RUN-001` queda en `advertencia` con recomendacion `mantener_cierre_operativo`.

`MOC-EVAL-001` queda como paso `ok` con 0 hallazgos.

`DO-LAB-RISK-001` conserva `risk_blocks_closure: false`.

La advertencia restante pertenece a deuda documental y advertencias controladas del Laboratorio, no a bloqueo nuevo de `MOC-001`.

## Guardas verificadas

- No admite `H-Xi`.
- No canoniza `Xi`.
- No declara `Xi` operador general vigente.
- No evalua personas reales.
- No abre uso clinico.
- No reabre `PSI-001`.
- No modifica `Documento 04`.
- No crea Nivel C.
- No cierra `P-107`.
- No cierra Confluencia global.
- No cierra Equivalencia global.
- No autoriza transformaciones materiales.

## Lectura

La primera ruta valida queda ejecutada favorablemente como prueba local.

Esto prueba consistencia operativa inicial de `Xi_eval_MOC`, estados metricos, protocolo simulado y software no mutante. No prueba validez empirica general, no canoniza el MOC y no habilita dominios clinicos o regulados.

## Deudas abiertas

- incorporar casos con desacuerdo justificado no bloqueante;
- ampliar bateria sintetica no clinica;
- formalizar relacion `MOC` / `TCS`;
- formalizar relacion `MOC` / `AO`;
- precisar familias de salida frente a conflictos globales;
- mantener estudio empirico real bloqueado hasta decision posterior.
