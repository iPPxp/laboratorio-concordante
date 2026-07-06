# MOC-001 - Decision de puente formal MOC/AO

ID: `D-2026-07-05-022`.

Fecha: 2026-07-05.

Estatus: decision provisional de expediente.

## Decision

Se acepta `MOC-AO-BRIDGE-001` como formalizacion local de `MOC-ROUTE-004`.

Documento base: `03_Expedientes/MOC-001_Puente_Formal_MOC_AO.md`.

Auditoria: `03_Expedientes/MOC-001_Auditoria_Puente_Formal_MOC_AO.md`.

## Alcance

La decision acepta `Pi_moc_trace` y `ao_bridge` como proyeccion local desde `operator_trace` hacia roles AO.

Roles aceptados:

- `evidencia_auxiliar_equivalencia_local`;
- `evidencia_auxiliar_con_deuda`;
- `evidencia_friccion_confluencia_local`;
- `deuda_global_no_cierre`;
- `bloqueo_seguridad_sin_uso_positivo`;
- `bloqueo_comparabilidad_sin_uso_positivo`.

## Resultado

`MOC-EVAL-001` conserva `ao_bridge` en cada resultado y permite usar `operator_trace` como evidencia local de regla ganadora para `AO-PPI-BRIDGE-001`.

## No cubre

No valida empiricamente el MOC, no evalua personas reales, no abre uso clinico, no admite `H-Xi`, no canoniza `Xi`, no crea Nivel C, no modifica `Documento 04`, no cierra Confluencia global, no cierra Equivalencia global, no formaliza una semantica general de proyecciones y no autoriza transformaciones materiales.

## Consecuencia

`MOC-ROUTE-004` queda aceptada como avance formal local.

La siguiente ruta recomendada pasa a `MOC-ROUTE-005`: refinar protocolo de evaluadores.
