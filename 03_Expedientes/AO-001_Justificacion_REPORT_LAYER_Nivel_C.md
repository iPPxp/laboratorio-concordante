# AO-001 - Justificacion de estatus de REPORT_LAYER frente a Nivel C

Identificador: `AO-REPORT-LAYER-NIVEL-C-001`.

Estatus: justificacion documental local.

Fecha: 2026-07-06.

Decision asociada: `D-2026-07-06-014`.

## Pregunta

Determinar si `REPORT_LAYER` debe pasar a Nivel C o permanecer como capa local.

## Fuentes

- `02_Documentos/C-002_RFC_Operativo_Auditor_v0.md`.
- `03_Expedientes/AUD-001_Ficha_Alcance_REPORT_LAYER_Pre-C.md`.
- `03_Expedientes/AUD-001_REPORT_LAYER_Candidata.md`.
- `03_Expedientes/AUD-001_Compatibilidad_REPORT_LAYER_DO_CHECK.md`.
- `03_Expedientes/AO-001_Relacion_REPORT_LAYER_Doc04_Amplio.md`.
- `03_Expedientes/AO-001_Decision_Pruebas_AO-DOC04-WIDE_REPORT_LAYER.md`.

## Criterio para promocion a Nivel C

`REPORT_LAYER` solo deberia pasar a Nivel C si cumple simultaneamente:

1. contrato exportable independiente, no dependiente de `AUD-001` o `AO-001`;
2. serializacion estable de datos y campos obligatorios;
3. uso interfrente real, no solo referencia documental local;
4. necesidad normativa que no pueda resolverse como vocabulario local;
5. auditoria contra `M-000`, `M-001`, `NIVEL-C-001`, `C-001` y `C-002`;
6. candidata documental separada y decision explicita de promocion.

## Evidencia local actual

`C-002` ya menciona `REPORT_LAYER`, pero declara que no queda promovida a Nivel C como contrato independiente.

`AUD-001_Ficha_Alcance_REPORT_LAYER_Pre-C.md` fija `REPORT_LAYER` como capa local pre-C de `AUD-001`.

`AO-001_Relacion_REPORT_LAYER_Doc04_Amplio.md` permite usar `REPORT_LAYER` solo como entrada de `Pi_rep(REPORT_LAYER, C, W) -> R_rep | B`.

`AO-DOC04-WIDE-TEST-001` probo la relacion local con casos sinteticos, pero no demostro necesidad de contrato oficial nuevo.

La nueva compuerta `REPORT-LAYER-C002-GATE-001` valida que `REPORT_LAYER` puede tratarse de forma no mutante conforme a `C-002` sin elevarlo de estatus.

## Dictamen

`REPORT_LAYER` debe permanecer local por ahora.

La razon no es debilidad conceptual, sino falta de necesidad normativa para Nivel C. Su funcion actual queda cubierta por:

- `C-002`, como regla oficial del Auditor para reportes compatibles;
- `AUD-001`, como origen local de la capa;
- `AO-001`, como uso proyectivo local por `Pi_rep`;
- `REPORT-LAYER-C002-GATE-001`, como compuerta no mutante previa a cualquier modo mutante.

## Deuda que permanece

Permanece abierta solo una deuda condicional:

- si `REPORT_LAYER` empieza a gobernar herramientas, serializacion interfrente o decisiones fuera de `AUD-001` / `AO-001`, debe abrir candidata Nivel C separada.

## No cubre

No modifica `C-001`.

No modifica `C-002`.

No crea `C-003`.

No promueve `REPORT_LAYER`.

No autoriza transformaciones.

No cierra Confluencia global ni Equivalencia global.
