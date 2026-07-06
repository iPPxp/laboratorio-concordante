# Auditoria - Pruebas AO-DOC04-WIDE-001 y REPORT_LAYER

Objeto auditado: `AO-DOC04-WIDE-TEST-001` y `AO-REPORT-LAYER-BRIDGE-001`.

Fecha: 2026-07-06.

Resultado: favorable con limites.

Decision asociada: `D-2026-07-06-007`.

## Criterios

La auditoria revisa si:

- los casos prueban salidas positivas, bloqueos y divergencias;
- `REPORT_LAYER` queda como entrada de `Pi_rep`, no como operador;
- `REPORT_LAYER` no sustituye decision, permiso ni verificacion posterior;
- no se promueve `REPORT_LAYER` a Nivel C;
- no se cierra Confluencia global ni Equivalencia global;
- la herramienta no mutante conserva `transformacion_permitida = false`;
- R4/Gamma siguen bloqueados para exportacion general.

## Evidencia

- `06_Automatizacion/ao_doc04_wide_tests.py`.
- `06_Automatizacion/fixtures/ao_doc04_wide_cases.json`.
- `03_Expedientes/AO-001_Pruebas_AO-DOC04-WIDE_REPORT_LAYER.md`.
- `03_Expedientes/AO-001_Relacion_REPORT_LAYER_Doc04_Amplio.md`.
- `02_Documentos/04_Algebra_Operacional.md`.
- `03_Expedientes/AUD-001_REPORT_LAYER_Candidata.md`.
- `03_Expedientes/AUD-001_Compatibilidad_REPORT_LAYER_DO_CHECK.md`.

## Hallazgos

La bateria cubre ocho casos:

- equivalencia local positiva;
- confluencia local positiva;
- bloqueo por testigo ausente;
- no autorizacion por falta de permiso material;
- bloqueo por incremento de autoridad;
- divergencia clasificada;
- bloqueo de exportacion general R4/Gamma;
- bloqueo por `REPORT_LAYER` incompleto.

La relacion con `REPORT_LAYER` queda precisada sin promocion: `REPORT_LAYER` alimenta `Pi_rep`, pero no reemplaza `Op_AO`, decision, permiso, verificacion posterior ni Nivel C.

## Limites

La prueba usa casos sinteticos. No demuestra Confluencia global, Equivalencia global ni madurez de `REPORT_LAYER` para una serializacion interfrente.

La herramienta integrada a `DO-LAB-RUN-001` reporta evidencia local, pero no autoriza transformaciones ni modifica documentos.

## Resultado

Auditoria favorable.

`AO-DOC04-WIDE-TEST-001` y `AO-REPORT-LAYER-BRIDGE-001` pueden aceptarse como avance local de `AO-001`.
