# AO-REPORT-PROMO-GATE-001 - Compuerta de promocion REPORT_LAYER

Fecha: 2026-07-06.

Estatus: aceptado local.

Expediente: `AO-001`.

## Objeto

Evaluar si `REPORT_LAYER` puede pasar de capa local pre-C a candidata formal exportable sin promoverla automaticamente.

## Bloqueos explicitos

La compuerta bloquea:

- promocion por repeticion;
- autoridad historica directa;
- cierre global implicito;
- modo mutante;
- cambio de Nivel C o Canon;
- contrato exportable incompleto.

## Evidencia local

- Herramienta: `06_Automatizacion/ao_report_promo_gate_001.py`.
- Fixture: `06_Automatizacion/fixtures/ao_report_promo_gate_001_cases.json`.
- Prueba: `06_Automatizacion/test_ao_report_promo_gate_001.py`.
- Reporte: `06_Automatizacion/reportes/ao_report_promo_gate_001_report.md`.

## Resultado esperado

```text
report_layer_candidate_future: true
report_layer_promoted: false
global_closure_authorized: false
global_export_authorized: false
r4_gamma_global_export_authorized: false
```

## Dictamen operativo

`REPORT_LAYER` puede quedar como candidata futura documentada. No pasa a Nivel C, no crea `C-003` y no se vuelve contrato global.

