# MOC-001 - Ejecucion de ruta 005

ID: `MOC-ROUTE-005`.

Fecha: 2026-07-05.

Estatus: ejecutada favorablemente en alcance local.

Decision asociada: `D-2026-07-05-024`.

## Objetivo

Refinar el protocolo de evaluadores usando `operator_trace`, `Pi_moc_trace` y `ao_bridge` como evidencia local de desempate, desacuerdo justificado y trazabilidad de regla ganadora.

## Documento producido

- `03_Expedientes/MOC-001_Protocolo_Evaluacion_v0_2.md`.

## Implementacion producida

- `06_Automatizacion/moc_eval.py`: agrega `protocol_v02` por caso y `protocol_v02_summary` por reporte.
- `06_Automatizacion/test_moc_eval.py`: agrega prueba de ruta 005.
- `06_Automatizacion/reportes/moc_eval_report.md`.
- `06_Automatizacion/reportes/moc_eval_report.json`.

## Resultado local

`MOC-EVAL-001` ejecuta 11 casos sinteticos no clinicos:

- casos: 11;
- aprobados: 11;
- fallos: 0;
- coincidencia exacta: 6;
- coincidencia parcial: 3;
- desacuerdo justificado: 2.

El protocolo v0.2 reporta:

- `resuelto`: 4;
- `resuelto_con_deuda`: 3;
- `resuelto_por_bloqueo`: 2;
- `revision_si_repite`: 2;
- `review_required`: 2;
- `blocked_positive_use`: 2.

## Criterio de aceptacion

La ruta se considera aceptada localmente porque:

- conserva el alcance sintetico no clinico;
- no modifica `Documento 04`;
- no convierte `operator_trace` en autoridad canonica;
- distingue desacuerdo por `Xi`, estado MOC, familia MOC y rol AO;
- conserva los desacuerdos justificados como deuda auditable;
- no fuerza unanimidad artificial;
- conserva bloqueos como bloqueos.

## No cubre

No valida empiricamente el MOC, no evalua personas reales, no abre uso clinico, no admite `H-Xi`, no canoniza `Xi`, no crea Nivel C, no modifica `Documento 04`, no cierra Confluencia global, no cierra Equivalencia global, no exporta R4/Gamma y no autoriza transformaciones materiales.

## Consecuencia

`MOC-ROUTE-005` queda ejecutada como refinamiento local no canonico del protocolo.

La siguiente ruta defendible es preparar `MOC-ROUTE-006`: protocolo documental de piloto empirico futuro, sin ejecucion real.
