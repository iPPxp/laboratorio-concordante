# MOC-001 - Casos sinteticos no clinicos

ID: `MOC-CASE-BAT-001`.

Estatus: bateria provisional ampliada.

Decision asociada inicial: `D-2026-07-05-014`.

Ampliacion ruta 002: `D-2026-07-05-018`.

## Proposito

Registrar una bateria minima de casos sinteticos no clinicos para probar `Xi_eval_MOC`, los estados metricos y el protocolo de evaluacion.

Los casos no describen personas reales, no son clinicos y no pertenecen a dominios regulados.

## Casos

### MOC-CASE-001 - Redundancia de tablero

Dominio: tablero de tareas sintetico.

Lectura: `R1` renombra una columna sin cambiar relaciones, permisos, evidencia ni deuda.

Salida esperada:

- `Xi_eval_MOC`: `redundante`.
- Estado MOC: `concordancia_local`.

Deuda: conservar trazabilidad.

### MOC-CASE-002 - Reorganizacion estable de dependencias

Dominio: paquete de software de juguete.

Lectura: `R1` reorganiza dependencias en grupos estables sin perder evidencia ni permisos.

Salida esperada:

- `Xi_eval_MOC`: `util_acotado`.
- Estado MOC: `concordancia_local`.

Deuda: no exportar como regla global.

### MOC-CASE-003 - Friccion sin estabilidad nueva

Dominio: flujo editorial sintetico.

Lectura: `R1` introduce una restriccion incompatible con una ruta aprobada, sin nueva estabilidad relacional.

Salida esperada:

- `Xi_eval_MOC`: `limitado`.
- Estado MOC: `friccion_operativa`.

Deuda: resolver conflicto de regla o autoridad local.

### MOC-CASE-004 - Unidad minima perdida

Dominio: comparacion de registros abstractos.

Lectura: `R0` y `R1` dejan de compartir unidad minima comparable.

Salida esperada:

- `Xi_eval_MOC`: `no_comparable`.
- Estado MOC: `no_comparable`.

Deuda: redefinir unidad minima antes de continuar.

### MOC-CASE-005 - Fuera de alcance

Dominio: caso rechazado por alcance.

Lectura: el caso carece de evidencia suficiente o intenta entrar a un dominio no permitido.

Salida esperada:

- `Xi_eval_MOC`: `bloqueado`.
- Estado MOC: `bloqueo_de_concordancia`.

Deuda: abrir decision separada o retirar el caso.

### MOC-CASE-006 - Discordancia global conservada

Dominio: rutas de reporte sinteticas.

Lectura: dos rutas locales son validas bajo sus testigos, pero producen estados incompatibles al intentar una lectura global.

Salida esperada:

- `Xi_eval_MOC`: `util_acotado`.
- Estado MOC: `discordancia_global`.

Deuda: Confluencia global y Equivalencia global permanecen abiertas.

### MOC-CASE-007 - Concordancia parcial con deuda visible

Dominio: matriz de criterios sintetica.

Lectura: `R1` reorganiza criterios de forma util, pero queda deuda no bloqueante de trazabilidad secundaria.

Salida esperada:

- `Xi_eval_MOC`: `util_acotado`.
- Estado MOC: `concordancia_parcial`.

Deuda: completar trazabilidad secundaria antes de usar como apoyo fuerte.

### MOC-CASE-008 - Ambiguedad de regla en tabla de prioridades

Dominio: tabla de prioridades sintetica.

Lectura: `R1` preserva parte de la estructura de `R0`, pero introduce una regla de prioridad ambigua que distintos evaluadores pueden leer como friccion, seguridad o concordancia restringida.

Salida esperada:

- `Xi_eval_MOC`: `limitado`.
- Estado MOC: `friccion_operativa`.
- Protocolo: `desacuerdo_justificado`.

Clase de desacuerdo: `ambiguedad_de_regla`.

Deuda: precisar desempate entre lectura conservadora y lectura de utilidad acotada.

### MOC-CASE-009 - Eje TCS secundario incompleto

Dominio: cola de eventos sintetica.

Lectura: `R1` reorganiza dependencias en una secuencia estable, pero deja incompleto un eje TCS secundario de trazabilidad automatizable.

Salida esperada:

- `Xi_eval_MOC`: `util_acotado`.
- Estado MOC: `concordancia_parcial`.

Deuda: completar eje TCS secundario antes de usar el caso como evidencia fuerte.

### MOC-CASE-010 - Conflicto de autoridad local no global

Dominio: doble autoridad sintetica.

Lectura: dos autoridades locales validas sostienen criterios incompatibles sobre el mismo caso, sin generar todavia una discordancia global.

Salida esperada:

- `Xi_eval_MOC`: `limitado`.
- Estado MOC: `friccion_operativa`.

Clase de desacuerdo: `conflicto_de_autoridad_no_global`.

Deuda: decidir autoridad local o declarar puente formal posterior.

### MOC-CASE-011 - Frontera entre concordancia parcial y friccion

Dominio: flujo de aprobacion sintetico.

Lectura: `R1` estabiliza una reorganizacion util, pero deja tension interpretativa suficiente para que evaluadores razonables discrepen entre concordancia parcial y friccion operativa.

Salida esperada:

- `Xi_eval_MOC`: `util_acotado`.
- Estado MOC: `concordancia_parcial`.
- Protocolo: `desacuerdo_justificado`.

Clase de desacuerdo: `frontera_concordancia_friccion`.

Deuda: formalizar puente `MOC/TCS` para reducir ambiguedad de frontera.

## Resultado esperado de bateria

La bateria debe producir al menos:

- un caso `redundante`;
- un caso `util_acotado`;
- un caso `limitado`;
- un caso `no_comparable`;
- un caso `bloqueado`;
- un caso de `discordancia_global`;
- un caso de `concordancia_parcial`.
- al menos un caso con `desacuerdo_justificado`;
- al menos un caso limite entre `concordancia_parcial` y `friccion_operativa`;
- al menos un caso con conflicto de autoridad local no global;
- al menos un caso con deuda TCS secundaria.

La bateria no demuestra validez empirica general. Solo prueba que el protocolo local distingue salidas y deudas sin abrir dominios prohibidos.

## Resultado de ruta 002

La ejecucion `MOC-ROUTE-002` amplio la bateria a 11 casos y produjo:

- 11 casos aprobados;
- 0 fallos;
- 6 coincidencias exactas;
- 3 coincidencias parciales;
- 2 desacuerdos justificados.

La bateria alimento `MOC-ROUTE-003`, puente formal `MOC/TCS`, aceptado por `D-2026-07-05-020`.
