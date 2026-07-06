# MOC-001 - Decision de puente formal MOC/TCS

ID: `D-2026-07-05-020`.

Fecha: 2026-07-05.

Estatus: decision provisional de expediente.

## Decision

Se acepta `MOC-TCS-BRIDGE-001` como formalizacion ejecutable local de `MOC-ROUTE-003`.

Documento base: `03_Expedientes/MOC-001_Puente_Formal_MOC_TCS.md`.

Auditoria: `03_Expedientes/MOC-001_Auditoria_Puente_Formal_MOC_TCS.md`.

## Alcance

La decision acepta cuatro operadores locales:

- `OP_MOC_XI`;
- `OP_MOC_TCS`;
- `OP_MOC_STATE`;
- `OP_MOC_AGREEMENT`.

Tambien acepta que `MOC-EVAL-001` emita `operator_trace` para conservar regla ganadora, prioridad aplicada y deudas TCS.

## Resultado

La formalizacion deja de depender de una formula conceptual sin criterio de combinacion.

Cada caso sintetico no clinico puede evaluarse mediante operadores con:

- entradas normalizadas;
- prioridad explicita;
- regla de conflicto;
- salida unica;
- traza auditable.

## No cubre

No valida empiricamente el MOC, no evalua personas reales, no abre uso clinico, no admite `H-Xi`, no canoniza `Xi`, no crea Nivel C, no modifica `Documento 04`, no cierra Confluencia global, no cierra Equivalencia global, no formaliza puente `MOC/AO` y no autoriza transformaciones materiales.

## Consecuencia

`MOC-ROUTE-003` queda aceptada como avance formal local.

La siguiente ruta recomendada pasa a `MOC-ROUTE-004`: formalizar puente `MOC/AO`.
