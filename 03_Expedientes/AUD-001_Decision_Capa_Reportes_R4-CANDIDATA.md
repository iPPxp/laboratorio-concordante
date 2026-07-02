# AUD-001 - Decision sobre capa de reportes de R4-CANDIDATA

Estatus: decision provisional de expediente.

Expediente padre: `AUD-001`.

Identificador: `CAPA-REPORTES-R4-001`.

Fecha: 2026-07-01.

Objeto decidido: relacion entre reportes locales de `AUD-001` y `R4-CANDIDATA`.

## Proposito

Decidir si la capa de reportes validada en `AUD-001` debe generalizarse o permanecer local despues de la primera prueba no automata de `R4-CANDIDATA`.

Esta decision no promueve los reportes a Canon ni convierte `R4-CANDIDATA` en Regla R4 formal. `REPORT_LAYER` tampoco es Canon ni especificacion oficial.

## Fuentes locales

- `03_Expedientes/AUD-001_Contrato_Reportes.md`
- `03_Expedientes/AUD-001_Validaciones.md`
- `03_Expedientes/AUD-001_R4-CANDIDATA.md`
- `03_Expedientes/AUD-001_Decision_Estatus_R4-CANDIDATA.md`
- `03_Expedientes/AUD-001_Simulaciones.md`
- `01_Canon/M-000_Reglas_Fundamentales.md`
- `01_Canon/M-001_Auditoria_Arquitectonica.md`

## Decision

Los nombres concretos de reportes de `AUD-001` permanecen locales al Auditor.

Se acepta, sin embargo, una capa abstracta equivalente para trabajar con `R4-CANDIDATA` dentro de `AUD-001`.

Forma corta:

```text
MP_FAIL_REPORT, CR_FAIL_REPORT, TAU_REPORT, D_REPORT,
TR_PROPOSAL_REPORT, TR_EXECUTION_REPORT,
TR_EXECUTION_FAIL_REPORT y REVERSAL_REPORT
permanecen como contratos locales de AUD-001.

R4-CANDIDATA puede referirse a una capa abstracta equivalente:
REPORT_LAYER = reportes normalizados suficientes para fundar decision, permiso, ejecucion y recuperacion.
```

## Capa abstracta equivalente

Para sostener `R4-CANDIDATA`, una capa de reportes equivalente debe poder expresar como minimo:

- operador o fase que reporta
- resultado del operador o fase
- tipo de hallazgo o salida
- ubicacion o alcance del hallazgo
- evidencia
- estatus de la afirmacion afectada
- decisiones permitidas
- decision emitida, si aplica
- permiso o prohibicion de transformacion
- estado de terminacion
- dependencias usadas
- deudas generadas
- evidencia previa y posterior cuando exista ejecucion
- politica posterior cuando exista fallo de ejecucion

Esta lista es abstracta. No obliga a reutilizar los nombres exactos de `AUD-001` fuera del expediente.

## Alcance permitido

La decision permite:

- usar `REPORT_LAYER` como abreviatura dentro de trabajos futuros de `AUD-001`
- comparar objetos no automatas contra `R4-CANDIDATA` usando reportes equivalentes
- disenar una generalizacion futura de reportes como expediente separado

La decision no permite:

- mover `OPERATOR_REPORT` a Canon
- usar los nombres locales de `AUD-001` como vocabulario canonico
- tratar `REPORT_LAYER` como especificacion oficial
- modificar `C-001` sin decision de nivel
- promover `R4-CANDIDATA` a Regla R4 formal

## Motivo

`VAL-017` mostro que `R4-CANDIDATA` puede operar sobre un objeto documental no automata si existe una capa equivalente de reportes para estatus, autoridad, decision y transformacion.

Pero la validacion no demuestra que los contratos locales de `AUD-001` deban convertirse en Canon o en lenguaje general del Laboratorio.

Por eso la decision conserva los nombres locales y abstrae solo la funcion procedimental.

## Consecuencia para R4-CANDIDATA

`R4-CANDIDATA` puede formularse en terminos de reportes normalizados equivalentes, no necesariamente en terminos de los nombres concretos de `AUD-001`.

Lectura autorizada:

```text
decision fundada requiere reportes normalizados suficientes
```

Lectura no autorizada:

```text
toda instancia futura de R4 debe usar exactamente los reportes de AUD-001
```

## Deudas que permanecen

- Probar `R4-CANDIDATA` con objetos no automatas adicionales.
- Si se busca promocion formal, redactar una especificacion separada de `REPORT_LAYER`.
- Auditar cualquier generalizacion de reportes contra `M-000` y `M-001`.
- Decidir si `REPORT_LAYER` pertenece a `AUD-001`, a un futuro documento tecnico o a un expediente propio.

## Efectos sobre el repositorio

Esta decision afecta solo `AUD-001` y el estado operativo del proyecto.

No modifica Canon, documentos oficiales ni expedientes cerrados.

## Siguiente paso recomendado

Objetivo cumplido posteriormente por `AUD-001_Decision_Ruta_Siguiente_R4-CANDIDATA.md`.

Objetivo cumplido posteriormente por `AUD-001_Decision_Pausa_Operativa_R4-CANDIDATA.md`.
