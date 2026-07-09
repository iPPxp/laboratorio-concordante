# AO-R4-GAMMA-EXPORT-GATE-002 - Compuerta de exportacion R4/Gamma

Fecha: 2026-07-06.

Estatus: aceptado local.

Expediente: `AO-001`.

## Objeto

Evaluar si `R4-FORMAL-AUD-001` y `GAMMA-FORMAL-AUD-001` pueden exportarse de forma general fuera de `AUD-001`.

## Bloqueos explicitos

La compuerta bloquea:

- exportacion general;
- semantica dependiente de `AUD-001`;
- dominio externo insuficiente;
- cierre global implicito;
- modo mutante;
- cambio de Nivel C o Canon.

## Evidencia local

- Herramienta: `06_Automatizacion/ao_r4_gamma_export_gate_002.py`.
- Fixture: `06_Automatizacion/fixtures/ao_r4_gamma_export_gate_002_cases.json`.
- Prueba: `06_Automatizacion/test_ao_r4_gamma_export_gate_002.py`.
- Reporte: `06_Automatizacion/reportes/ao_r4_gamma_export_gate_002_report.md`.

## Resultado esperado

```text
restricted_interoperable_profile_retained: true
r4_gamma_global_export_authorized: false
global_export_authorized: false
global_closure_authorized: false
report_layer_promoted: false
```

## Dictamen operativo

R4/Gamma conservan solo perfil restringido interoperable. No hay exportacion general.

