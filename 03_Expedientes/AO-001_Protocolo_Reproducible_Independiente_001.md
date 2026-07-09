# AO-PROTO-INDEP-001 - Protocolo AO reproducible independiente

Fecha: 2026-07-06.

Estatus: aceptado local.

Expediente: `AO-001`.

## Objeto

Abrir una ruta local no mutante para probar si distintos evaluadores pueden aplicar las mismas reglas AO sobre los mismos casos y llegar a resultados comparables sin forzar unanimidad.

## Alcance

El protocolo usa tres perfiles evaluadores sinteticos:

- `eval_documental`: lee consistencia de documentos, testigo y estado.
- `eval_operacional`: lee permiso, autoridad y ruta operacional.
- `eval_reporte`: lee salida de reporte, capa `REPORT_LAYER` y deuda declarada.

Todos los evaluadores reciben los mismos casos, la misma plantilla de entrada y las mismas reglas fijas.

## Salidas medidas

- `coincidencia_exacta`: todos emiten el mismo estado.
- `coincidencia_familia`: emiten estados distintos dentro de la misma familia.
- `desacuerdo_justificado`: no coinciden, pero cada discrepancia tiene deuda explicita.
- `bloqueo_protocolo`: faltan evaluadores, estado, familia, justificacion o se fuerza unanimidad.

## Evidencia local

- Herramienta: `06_Automatizacion/ao_protocol_independent_001.py`.
- Fixture: `06_Automatizacion/fixtures/ao_protocol_independent_001_cases.json`.
- Prueba: `06_Automatizacion/test_ao_protocol_independent_001.py`.
- Reporte: `06_Automatizacion/reportes/ao_protocol_independent_001_report.md`.

## Resultado esperado

```text
independent_protocol_accepted: true
global_closure_authorized: false
global_export_authorized: false
report_layer_promoted: false
r4_gamma_global_export_authorized: false
transformacion_permitida: false
```

## Limites

El protocolo no prueba independencia empirica externa real.

No autoriza cierre global de Confluencia ni Equivalencia.

No modifica Documento 04, Canon, Nivel C ni `C-002`.

No promueve `REPORT_LAYER`.

No exporta R4/Gamma.

