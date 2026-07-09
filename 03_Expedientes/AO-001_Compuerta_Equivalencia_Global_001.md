# AO-EQ-GLOBAL-GATE-001 - Compuerta de Equivalencia global

Fecha: 2026-07-06.

Estatus: aceptado local.

Expediente: `AO-001`.

## Objeto

Evaluar si la evidencia acumulada por `AO-PPI-BRIDGE-004`, `AO-PROTO-INDEP-001`, `Pi_doc`, `Pi_rep`, `Pi_op`, `REPORT_LAYER` y autoridad local alcanza para autorizar Equivalencia global de proyecciones.

## Matriz local

La compuerta separa condiciones en:

- `satisfecha_local`
- `parcial_local`
- `faltante_global`
- `bloqueada_por_alcance`

Solo las dos primeras cuentan como avance local. Ninguna autoriza por si misma cierre global.

## Evidencia local

- Herramienta: `06_Automatizacion/ao_eq_global_gate_001.py`.
- Fixture: `06_Automatizacion/fixtures/ao_eq_global_gate_001_matrix.json`.
- Prueba: `06_Automatizacion/test_ao_eq_global_gate_001.py`.
- Reporte: `06_Automatizacion/reportes/ao_eq_global_gate_001_report.md`.

## Resultado esperado

```text
global_equivalence_authorized: false
global_closure_authorized: false
global_export_authorized: false
report_layer_promoted: false
r4_gamma_global_export_authorized: false
```

## Dictamen operativo

La equivalencia global permanece no autorizada porque la cobertura externa sigue sintetica, el dominio universal no esta autorizado y `REPORT_LAYER` no tiene contrato exportable global.

