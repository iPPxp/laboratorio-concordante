# AO-001 - Bateria fuerte AO-PPI-BRIDGE-002

Estatus: bateria local no mutante.

Fecha: 2026-07-06.

ID: `AO-PPI-BRIDGE-002`.

Expediente padre: `AO-001`.

Decision asociada: `D-2026-07-06-017`.

## Proposito

Abrir una bateria fuerte no mutante para profundizar `AO-PPI-BRIDGE-001` hacia Confluencia y Equivalencia de proyecciones.

La bateria no reabre `P-PI.0` ni `P-PI.1`. Trabaja desde `AO-001` y usa evidencia local ya aceptada.

## Fuentes

- `03_Expedientes/AO-001_Puente_Confluencia_Equivalencia.md`.
- `03_Expedientes/AO-001_Formalizacion_Amplia_Doc04.md`.
- `03_Expedientes/AO-001_Pruebas_AO-DOC04-WIDE_REPORT_LAYER.md`.
- `03_Expedientes/AO-001_Relacion_REPORT_LAYER_Doc04_Amplio.md`.
- `03_Expedientes/R001-001_Relacion_Formal_AO.md`.
- `06_Automatizacion/ao_ppi_bridge_002.py`.
- `06_Automatizacion/fixtures/ao_ppi_bridge_002_cases.json`.
- `06_Automatizacion/reportes/ao_ppi_bridge_002_report.md`.

## Criterio fuerte local

Un caso cuenta como fuerte si preserva:

- testigo comun;
- evidencia;
- decision;
- ausencia de permiso mutante;
- deuda resultante;
- autoridad sin aumento;
- salida segura.

La equivalencia fuerte local exige que las proyecciones comparadas conserven la misma firma operacional bajo el mismo testigo.

La confluencia fuerte local exige que ruta de estado, ruta de decision y ruta de reporte produzcan una salida compatible sin aumentar autoridad ni ocultar deuda.

## Bateria

| Caso | Tipo | Salida esperada | Funcion |
| --- | --- | --- | --- |
| `AO-PPI-STRONG-001` | equivalence | `equivalencia_fuerte_local` | `Pi_doc`, `Pi_rep` y `Pi_op` coinciden bajo testigo comun. |
| `AO-PPI-STRONG-002` | equivalence | `equivalencia_fuerte_local` | `R001-TB-001` funciona como instancia local tabular de apoyo. |
| `AO-PPI-STRONG-003` | equivalence | `divergencia_clasificada` | Una proyeccion diverge, pero el testigo permite clasificar la divergencia. |
| `AO-PPI-STRONG-004` | confluence | `confluencia_fuerte_local` | Ruta de estado, decision y reporte convergen sin transformacion. |
| `AO-PPI-STRONG-005` | confluence | `divergencia_clasificada` | Las rutas divergen y la divergencia queda visible. |
| `AO-PPI-STRONG-006` | equivalence | `bloqueo_por_testigo` | Falta testigo comun suficiente. |
| `AO-PPI-STRONG-007` | confluence | `bloqueo_report_layer_incompleto` | La ruta de reporte no conserva `REPORT_LAYER` completo. |
| `AO-PPI-STRONG-008` | equivalence | `bloqueo_por_autoridad` | Una proyeccion intenta aumentar autoridad hasta Canon. |

Resultado automatizado: 8 casos, 8 aprobados, 0 fallos.

## Lectura operacional

`AO-PPI-BRIDGE-002` fortalece el puente local porque combina:

- proyecciones documentales, de reporte, operacionales y tabulares;
- rutas de estado, decision y reporte;
- casos positivos y negativos esperados;
- preservacion explicita de deudas globales;
- compuerta de autoridad y testigo.

El resultado local favorable autoriza tratar la bateria como evidencia de avance de `AO-001`.

No autoriza leer el resultado como teorema global.

## Guardas

La bateria:

- no modifica Documento 04;
- no modifica Canon;
- no crea Nivel C;
- no reabre `P-PI.0`;
- no reabre `P-PI.1`;
- no cierra Confluencia global;
- no cierra Equivalencia global;
- no promueve `REPORT_LAYER`;
- no promueve R4/Gamma;
- no autoriza transformaciones materiales.

## Deudas abiertas

- Confluencia global.
- Equivalencia global de proyecciones.
- Serializacion interfrente de `REPORT_LAYER` si una decision futura la exige.
- Relacion posterior con `TCS-001`.
- Exportacion general de R4/Gamma, bloqueada por compuerta vigente.

## Dictamen

`AO-PPI-BRIDGE-002` queda abierto como bateria fuerte local no mutante.

La evidencia favorece aceptar el avance local y mantener abiertos los problemas globales.
