# AO-EXT-EVID-GATE-001 - Compuerta de evidencia externa

Fecha: 2026-07-06.

Estatus: preparada local.

Expediente: `AO-001`.

Nota posterior 2026-07-06: `AO-EXT-REAL-001` usa esta compuerta con un fixture de fuente real y produce `external_evidence_ready: true` sin ejecucion empirica ni autorizacion global. La compuerta base conserva `external_evidence_ready: false`.

## Objeto

Definir una compuerta documental y tecnica para evaluar manifiestos de evidencia externa independiente no sintetica antes de cualquier ejecucion real.

## Entradas

Cada manifiesto debe declarar:

- `manifest_id`;
- manifiesto de fuente y familia de fuente;
- tipo de artefacto;
- fuente identificable;
- si existe fuente externa real;
- unidad comparable;
- testigo;
- restricciones;
- autoridad declarada;
- trazabilidad;
- banderas de dominio clinico, dominio regulado y personas reales.

## Salidas

La compuerta solo puede emitir:

- `admisible_preliminar`;
- `pendiente_fuente_real`;
- `rechazada_por_alcance`;
- `rechazada_por_autoridad`;
- `rechazada_por_dominio`.

## Reglas de prioridad

1. Si el manifiesto declara dominio clinico, dominio regulado o personas reales, la salida es `rechazada_por_dominio`.
2. Si el manifiesto usa historial como autoridad directa, reclama Canon, Nivel C, autoridad global o convierte reporte en decision, la salida es `rechazada_por_autoridad`.
3. Si falta tipo de artefacto, unidad comparable, testigo, trazabilidad o restricciones, la salida es `rechazada_por_alcance`.
4. Si el manifiesto esta bien formado pero no aporta fuente externa real, la salida es `pendiente_fuente_real`.
5. Solo si fuente, unidad comparable, testigo, restricciones, autoridad y trazabilidad estan completos, la salida puede ser `admisible_preliminar`.

## Resultado inicial esperado

La tanda actual no aporta evidencia externa real. Por tanto, aunque exista un manifiesto de control completo para probar la regla, el resultado de readiness externa queda:

```text
external_evidence_ready: false
external_evidence_executed: false
global_closure_authorized: false
global_export_authorized: false
global_equivalence_authorized: false
global_confluence_authorized: false
report_layer_promoted: false
r4_gamma_global_export_authorized: false
```

## Evidencia tecnica

- Herramienta: `06_Automatizacion/ao_external_evidence_gate_001.py`.
- Fixture: `06_Automatizacion/fixtures/ao_external_evidence_gate_001_manifests.json`.
- Prueba: `06_Automatizacion/test_ao_external_evidence_gate_001.py`.
- Integracion esperada: despues de `AO-GLOBAL-READINESS-001` en `06_Automatizacion/lab_run.py`.

## Limites

No hay busqueda, descarga, reclutamiento, ejecucion empirica, uso de datos reales ni transformacion material.

No se modifican `01_Canon`, `02_Documentos`, Nivel C ni `C-002`.
