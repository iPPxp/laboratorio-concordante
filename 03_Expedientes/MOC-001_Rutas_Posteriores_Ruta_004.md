# MOC-001 - Rutas posteriores a ruta 004

ID: `MOC-NEXT-ROUTES-004`.

Fecha: 2026-07-05.

Estatus: matriz provisional de rutas posteriores.

Decision asociada: `D-2026-07-05-023`.

## Punto de partida

`MOC-ROUTE-004` queda aceptada por `D-2026-07-05-022`:

- `operator_trace` se proyecta como `Pi_moc_trace`;
- `ao_bridge` clasifica roles AO locales;
- el puente no modifica `Documento 04`;
- el puente no cierra Confluencia global ni Equivalencia global.

## Ruta recomendada inmediata

### Ruta 5 - Refinar protocolo de evaluadores

ID sugerido: `MOC-ROUTE-005`.

Objetivo:

- incorporar `operator_trace` y `ao_bridge` a la plantilla de evaluacion;
- distinguir desacuerdo por regla `Xi`, regla `TCS`, regla de estado o rol AO;
- precisar el tratamiento de desacuerdo repetido;
- conservar el protocolo como no empirico y no canonico.

Razon:

Despues de formalizar `MOC/TCS` y `MOC/AO`, el punto mas debil ya no es la falta de operadores, sino la reproducibilidad del protocolo entre evaluadores.

Resultado esperado:

- protocolo v0.2 no canonico;
- auditoria local;
- decision provisional;
- pruebas adicionales solo si el protocolo exige nuevos casos.

## Ruta posterior valida

### Ruta 6 - Preparar piloto empirico no ejecutado

ID sugerido: `MOC-ROUTE-006`.

Objetivo:

- convertir `MOC-EMP-STUDY-001` en protocolo de piloto futuro;
- mantenerlo documental, sin reclutamiento y sin personas reales;
- definir criterios minimos para una decision posterior de ejecucion.

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

La ruta mas defensible despues de `MOC-ROUTE-004` es `MOC-ROUTE-005`: refinar protocolo de evaluadores con trazas y roles AO.
