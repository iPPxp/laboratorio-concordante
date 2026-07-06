# MOC-001 - Rutas posteriores a ruta 002

ID: `MOC-NEXT-ROUTES-002`.

Fecha: 2026-07-05.

Estatus: matriz provisional de rutas posteriores.

Decision asociada: `D-2026-07-05-019`.

## Punto de partida

`MOC-ROUTE-002` queda ejecutada favorablemente:

- `MOC-EVAL-001`: 11 casos, 11 aprobados, 0 fallos.
- protocolo: 6 coincidencias exactas, 3 coincidencias parciales y 2 desacuerdos justificados.
- casos limite: ambiguedad de regla, eje TCS secundario incompleto, conflicto de autoridad no global y frontera entre concordancia parcial/friccion.
- guardas: sin admision de `H-Xi`, sin canonizacion de `Xi`, sin uso clinico y sin transformacion.

## Ruta recomendada inmediata

### Ruta 3 - Formalizar puente MOC/TCS

ID sugerido: `MOC-ROUTE-003`.

Objetivo:

- mapear salidas de `Xi_eval_MOC` contra ejes TCS;
- precisar cuando una deuda TCS degrada un estado MOC;
- definir reglas de desempate entre `bloqueo_de_concordancia`, `no_comparable`, `friccion_operativa`, `concordancia_parcial` y `discordancia_global`;
- usar `MOC-CASE-009` y `MOC-CASE-011` como casos guia.

Razon:

La ruta 002 ya produjo desacuerdos justificados y casos limite. La tension mas informativa ahora esta en la relacion entre estado MOC y deuda TCS.

Resultado esperado:

- documento de puente `MOC-TCS-BRIDGE-001`;
- auditoria local;
- decision provisional;
- pruebas adicionales solo si el puente exige cobertura nueva.

## Rutas validas posteriores

### Ruta 4 - Formalizar puente MOC/AO

ID sugerido: `MOC-ROUTE-004`.

Objetivo:

- conectar estados MOC con testigos de `AO-PPI-BRIDGE-001`;
- precisar cuando una salida MOC puede operar como evidencia auxiliar para Confluencia o Equivalencia local;
- conservar `Documento 04` sin cambios.

### Ruta 5 - Refinar protocolo de evaluadores

ID sugerido: `MOC-ROUTE-005`.

Objetivo:

- separar desacuerdo por friccion, falta de evidencia, ambiguedad de regla y conflicto de autoridad;
- definir formato minimo de justificacion;
- definir tratamiento de desacuerdo repetido.

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

La ruta mas defensible despues de `MOC-ROUTE-002` es `MOC-ROUTE-003`: puente formal `MOC/TCS`, no canonico y no clinico.
