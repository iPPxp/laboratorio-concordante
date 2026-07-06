# AO-001 - Matriz consolidada AO-PPI-BRIDGE-004

Estatus: aceptada localmente.

Fecha: 2026-07-06.

ID: `AO-PPI-BRIDGE-004`.

Decision asociada: `D-2026-07-06-023`.

## Proposito

Recalcular las condiciones faltantes para cierre global despues de `AO-TCS-REL-001`, `AO-AUTH-GLOBAL-001` y `AO-EXT-COV-001`.

La matriz consolida evidencia local fuerte, pero mantiene `global_closure_authorized: false`.

## Matriz consolidada

| ID | Dominio | Estado posterior |
| --- | --- | --- |
| `AO-PPI-GC-001` | equivalencia | `satisfecha_local` |
| `AO-PPI-GC-002` | confluencia | `satisfecha_local` |
| `AO-PPI-GC-003` | `REPORT_LAYER` heterogeneo | `satisfecha_local` |
| `AO-PPI-GC-004` | serializacion `REPORT_LAYER` | `satisfecha_local` |
| `AO-PPI-GC-005` | autoridad | `parcial_local` |
| `AO-PPI-GC-006` | dominios externos | `parcial_local` |
| `AO-PPI-GC-007` | `AO/TCS` | `satisfecha_local` |
| `AO-PPI-GC-008` | alcance `P-PI` | `bloqueada_por_alcance` |
| `AO-PPI-GC-009` | exportacion R4/Gamma | `bloqueada_por_alcance` |
| `AO-PPI-GC-010` | reproducibilidad AO | `faltante_global` |
| `AO-PPI-GC-011` | promocion `REPORT_LAYER` | `bloqueada_por_alcance` |
| `AO-PPI-GC-012` | decision de cierre global | `faltante_global` |

## Herramienta

- Herramienta: `06_Automatizacion/ao_ppi_bridge_004.py`.
- Fixture: `06_Automatizacion/fixtures/ao_ppi_bridge_004_matrix.json`.
- Prueba: `06_Automatizacion/test_ao_ppi_bridge_004.py`.
- Reportes: `06_Automatizacion/reportes/ao_ppi_bridge_004_report.md` y `.json`.

## Resultado esperado

```text
conditions: 12
satisfied_local: 5
partial_local: 2
missing_global: 2
scope_blocked: 3
global_closure_authorized: false
global_export_authorized: false
report_layer_promoted: false
```

## Lectura operacional

`AO-PPI-BRIDGE-004` reduce deudas globales en grado local y deja visibles los faltantes que aun impiden cierre global.

No autoriza reapertura de `P-PI.0` / `P-PI.1`, promocion de `REPORT_LAYER`, exportacion R4/Gamma ni modificacion de Documento 04.

## Deudas abiertas

- Protocolo AO reproducible independiente.
- Promocion formal de `REPORT_LAYER`, solo si se abre una candidata posterior.
- Exportacion general de R4/Gamma, solo por compuerta nueva.
- Cierre global de Confluencia.
- Cierre global de Equivalencia de proyecciones.
