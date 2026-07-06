# AUT-003 - Herramienta REPORT_LAYER / C-002

Identificador: `REPORT-LAYER-C002-GATE-001`.

Estatus: herramienta no mutante.

Fecha: 2026-07-06.

Decision asociada: `D-2026-07-06-015`.

## Contrato

Entrada:

- fixture local de casos `REPORT_LAYER`;
- campos requeridos por `C-002`;
- declaracion de autoridad, fuente y permiso.

Salida:

- reporte Markdown;
- reporte JSON;
- resultado por caso;
- guardas de no promocion y no transformacion.

## Casos minimos cubiertos

- `RL-C002-001`: reporte completo local.
- `RL-C002-002`: recomendacion favorable sin decision.
- `RL-C002-003`: campo minimo ausente.
- `RL-C002-004`: recomendacion convertida en decision.
- `RL-C002-005`: intento de modo mutante.
- `RL-C002-006`: intento de promocion a Nivel C.
- `RL-C002-007`: historial usado como autoridad directa.
- `RL-C002-008`: decision de cambio acotado sin permiso material.

## Invariantes

- `transformacion_permitida = false`;
- `crea_nivel_c = false`;
- `promueve_report_layer = false`;
- `emite_decision_autoridad = false`;
- `usa_historial_como_autoridad = false`.

## Dictamen esperado

La herramienta debe emitir `resultado: ok` cuando todos los casos producen el bloqueo o compatibilidad esperados.

Una herramienta mutante futura solo puede discutirse despues de esta compuerta y con decision separada.
