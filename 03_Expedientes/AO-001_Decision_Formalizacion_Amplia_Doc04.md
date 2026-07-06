# Decision - Formalizacion Amplia del Documento 04

Identificador: `D-2026-07-06-006`.

Fecha: 2026-07-06.

Estatus: decision documental aceptada.

Expediente: `AO-001`.

Artefacto aceptado: `AO-DOC04-WIDE-001`.

## Decision

Se acepta `AO-DOC04-WIDE-001` como formalizacion amplia v0 del Documento 04 - Algebra Operacional.

Se actualiza `02_Documentos/04_Algebra_Operacional.md` para incorporar:

- contrato comun de operador operacional `Op_AO`;
- `operator_trace` como evidencia local de regla ganadora;
- proyecciones `Pi_doc`, `Pi_rep` y `Pi_op`;
- equivalencia local `Eq_local`;
- confluencia local `Conf_local`;
- compuerta operacional `Gate_AO`;
- perfiles restringidos `R4_AO_res` y `Gamma_AO_res`;
- reglas de prioridad y salidas seguras.

## Fundamento

La evidencia local acumulada en `AO-001`, `R001-001` y `MOC-001` permite pasar del grado acotado `Pi_tb` / `Eq_tb` a una formalizacion documental mas amplia.

La incorporacion es defensible porque no borra las fronteras anteriores: solo formaliza contratos locales y deja abiertas las deudas globales.

## No cubre

Esta decision no:

- modifica Canon;
- crea Nivel C;
- autoriza transformaciones materiales;
- admite `H-Xi`;
- canoniza `Xi`;
- reabre `P-PI.0` ni `P-PI.1`;
- cierra `P-107` ni `P-200`;
- cierra Confluencia global;
- cierra Equivalencia global de proyecciones;
- exporta R4/Gamma como operadores generales;
- madura `TCS-001` mas alla de su estado provisional.

## Consecuencia

Documento 04 queda en version amplia v0.

La deuda "Formalizacion posterior amplia del Documento 04" queda atendida en grado documental v0, pero permanecen abiertas las deudas de pruebas globales, relacion con `REPORT_LAYER`, maduracion de `TCS-001` y posible especificacion tecnica posterior.

El siguiente avance recomendado es probar `Eq_local` y `Conf_local` contra casos no triviales y precisar la relacion entre `operator_trace`, `REPORT_LAYER` y los reportes normalizados.
