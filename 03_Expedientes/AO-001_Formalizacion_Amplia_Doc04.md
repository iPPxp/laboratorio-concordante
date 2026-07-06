# AO-001 - Formalizacion Amplia del Documento 04

Identificador: `AO-DOC04-WIDE-001`.

Estatus: incorporacion documental amplia v0 aceptada.

Fecha: 2026-07-06.

Decision: `D-2026-07-06-006`.

Documento destino: `02_Documentos/04_Algebra_Operacional.md`.

## Proposito

Atender la deuda viva de formalizacion posterior amplia del Documento 04 sin cerrar por declaracion los problemas globales de Confluencia, Equivalencia de proyecciones, `P-107`, `P-200` ni la exportacion general de R4/Gamma.

La ruta elegida convierte formulas conceptuales y puentes locales ya aceptados en contratos operacionales mas ejecutables: entradas, salidas, reglas de prioridad, salidas seguras y trazas.

## Evidencia local usada

- `AO-MARCO-001`: marco inicial de Algebra Operacional.
- `AO-CASE-BAT-001`: casos operacionales minimos.
- `AO-R4-GAMMA-USE-001`: criterio de uso controlado de R4/Gamma fuera de `AUD-001`.
- `AO-PPI-BRIDGE-001`: puente local de Confluencia y Equivalencia de proyecciones.
- `R001-TB-001`: instancia tabular local conectada con `AO-PPI-BRIDGE-001`.
- `AO-EXT-CONF-EXEC-001`: dos pruebas externas no reguladas de Confluencia local.
- `AO-DOC04-FORM-001`: incorporacion acotada de `Pi_tb` / `Eq_tb`.
- `AO-R4-GAMMA-EXPORT-GATE-001`: bloqueo de exportacion general de R4/Gamma.
- `MOC-AO-BRIDGE-001`: uso local de `operator_trace` como evidencia de regla ganadora.

## Resultado incorporado

La formalizacion amplia v0 incorpora al Documento 04:

- contrato comun de operador operacional `Op_AO`;
- `operator_trace` como evidencia local de regla ganadora;
- familia minima de proyecciones `Pi_doc`, `Pi_rep` y `Pi_op`;
- equivalencia local `Eq_local` bajo testigo;
- confluencia local `Conf_local` bajo testigo;
- compuerta comun `Gate_AO`;
- perfiles restringidos `R4_AO_res` y `Gamma_AO_res`;
- reglas de prioridad ante conflicto;
- deudas explicitas cuando falta evidencia, alcance, testigo, permiso o autoridad.

## Contrato amplio v0

Un operador queda escrito como:

```text
Op_AO := <id, entrada, contexto, testigo, estatus_entrada,
          evidencia, permiso, invariantes, regla,
          salida, salida_segura, deuda, rho_op>
```

La salida no puede interpretarse sin `contexto`, `testigo`, `estatus_entrada`, `evidencia`, `salida_segura` y `deuda`.

## Regla de prioridad

Ante conflicto entre reglas candidatas:

1. si falta evidencia, contexto, testigo o estatus, se bloquea o registra deuda;
2. si falta permiso material, no se ejecuta transformacion;
3. si una regla aumenta autoridad, pierde contra una regla conservadora;
4. si una regla borra deuda, pierde contra una regla que preserve o refine deuda;
5. si no hay desempate local suficiente, la salida es `escalar`, `bloquear` o `registrar_problema_abierto`.

## Frontera

Esta incorporacion:

- no modifica Canon;
- no crea Nivel C;
- no autoriza transformaciones materiales;
- no admite `H-Xi`;
- no canoniza `Xi`;
- no reabre `P-PI.0` ni `P-PI.1`;
- no cierra `P-107`, `P-200`, Confluencia global ni Equivalencia global;
- no exporta R4/Gamma como operadores generales.

## Deudas que permanecen abiertas

- Confluencia global.
- Equivalencia global de proyecciones.
- Relacion completa entre `operator_trace` y `REPORT_LAYER`.
- Casos no triviales de `Eq_local` entre proyecciones heterogeneas.
- Criterio de cuando una parte de Documento 04 debe pasar a especificacion tecnica.
- Maduracion de `TCS-001`.
- Exportacion general de R4/Gamma, actualmente bloqueada.

## Estado

`AO-DOC04-WIDE-001` queda aceptado como formalizacion amplia v0 del Documento 04.

Su autoridad es documental y local al Laboratorio. No convierte las construcciones en Canon, Nivel C ni teoremas globales.
