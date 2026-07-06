# MOC-001 - Rutas posteriores a ruta 003

ID: `MOC-NEXT-ROUTES-003`.

Fecha: 2026-07-05.

Estatus: matriz provisional de rutas posteriores.

Decision asociada: `D-2026-07-05-021`.

## Punto de partida

`MOC-ROUTE-003` queda aceptada por `D-2026-07-05-020`:

- `OP_MOC_XI` define salidas `Xi` por prioridad.
- `OP_MOC_TCS` distingue ejes nucleares y secundarios.
- `OP_MOC_STATE` emite un estado MOC unico con regla ganadora.
- `OP_MOC_AGREEMENT` clasifica coincidencia y desacuerdo.
- `MOC-EVAL-001` conserva `operator_trace`.

## Ruta recomendada inmediata

### Ruta 4 - Formalizar puente MOC/AO

ID sugerido: `MOC-ROUTE-004`.

Objetivo:

- conectar estados MOC con testigos de `AO-PPI-BRIDGE-001`;
- precisar cuando una salida MOC puede operar como evidencia auxiliar para Confluencia o Equivalencia local;
- usar `operator_trace` como testigo de regla ganadora;
- conservar `Documento 04` sin cambios.

Razon:

La relacion `MOC/TCS` ya queda suficientemente explicita para usar MOC como evidencia auxiliar. El siguiente puente debe decidir como se relaciona esa evidencia con `AO-001` sin cerrar problemas globales.

Resultado esperado:

- documento de puente `MOC-AO-BRIDGE-001`;
- auditoria local;
- decision provisional;
- pruebas adicionales solo si el puente exige cobertura nueva.

## Rutas validas posteriores

- `MOC-ROUTE-005`: refinar protocolo de evaluadores.
- `MOC-ROUTE-006`: preparar piloto empirico no ejecutado.

## Rutas bloqueadas

- Admision de `H-Xi`.
- Canonizacion de `Xi`.
- Promocion del MOC a Canon o Nivel C.
- Uso clinico, patologico, diagnostico o terapeutico.
- Evaluacion de personas reales.
- Reapertura de `PSI-001` dentro del Laboratorio.
- Modificacion de `Documento 04`.
- Cierre de Confluencia global o Equivalencia global.
- Exportacion general de R4/Gamma.

## Resultado operativo

La ruta mas defensible despues de `MOC-ROUTE-003` es `MOC-ROUTE-004`: puente formal `MOC/AO`, no canonico y no clinico.
