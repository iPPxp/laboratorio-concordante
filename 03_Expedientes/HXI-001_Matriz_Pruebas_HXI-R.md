# HXI-001 - Matriz de pruebas HXI-R

Estatus: matriz provisional operativa de expediente.

Fecha: 2026-07-02.

## Proposito

Probar si `Xi`, entendido provisionalmente como acoplamiento entre distincion de alternativas relacionales y restriccion de transiciones, agrega valor conceptual al analisis de `EX-PSI-001` a `EX-PSI-005`.

Esta matriz no admite `H-Xi`, no declara `Xi` operador vigente y no modifica `PSI-001`.

## Regla de lectura

La matriz evalua utilidad local, no verdad formal.

Cada prueba pregunta:

- que cambia entre `R0` y `R1`;
- que alternativas relacionales pueden distinguirse;
- que transiciones quedan permitidas, bloqueadas o no disponibles;
- si `Xi` agrega una distincion util frente a `DEF-PSI-ORG-001` y `CRIT-PSI-TR-001`;
- si el caso debe continuar, pausarse, rechazarse o mantenerse como limite.

## Matriz sintetica

| Prueba | Caso PSI | Clasificacion PSI | Lectura HXI-R | Resultado local |
| --- | --- | --- | --- | --- |
| `HXI-R-001` | `EX-PSI-001` | transformacion por cambio de contenido | `R0` y `R1` conservan el mismo patron relacional; cambia contenido, no transicion relacional relevante | `Xi` es redundante |
| `HXI-R-002` | `EX-PSI-002` | reorganizacion por cambio relacional estable | `R0` y `R1` cambian de modo estable; hay alternativas relacionales y restricciones de transicion descriptibles | `Xi` aporta valor conceptual |
| `HXI-R-003` | `EX-PSI-003` | desorganizacion por perdida de estabilidad relacional | hay fragmentos de `R0`, conflicto y ausencia de `R1` estable; `Xi` puede describir restricciones incompatibles, pero corre riesgo de sobreformalizar | `Xi` aporta valor limitado |
| `HXI-R-004` | `EX-PSI-004` | disolucion por perdida de unidad minima | no hay continuidad suficiente para comparar `R0 -> R1`; la restriccion principal es detener la comparacion | `Xi` marca limite, no explica continuidad |
| `HXI-R-005` | `EX-PSI-005` | no auditable | el caso queda fuera de alcance por mezcla con uso clinico o personal real | `Xi` queda bloqueado |

## HXI-R-001 - Transformacion por cambio de contenido

Caso: `EX-PSI-001`.

Clasificacion base: `transformacion` por cambio de contenido.

`R0`: foco-atencion, figura-centro, identificacion-forma.

`R1`: foco-atencion, figura-centro, identificacion-forma.

Distincion candidata: alternativas de contenido dentro de una misma relacion estable.

Restriccion candidata: conservar la tarea de identificacion y el centro como relaciones dominantes.

Lectura:

`Xi` puede describir que ciertas alternativas de contenido son posibles, pero no agrega una distincion relacional necesaria. `CRIT-PSI-TR-001` ya explica el caso como transformacion con continuidad organizacional.

Resultado: `Xi` es redundante para este caso.

Continuidad recomendada: usar como prueba de control negativo. Una version futura de `Xi` debe aceptar que aqui no aporta valor fuerte.

## HXI-R-002 - Reorganizacion por cambio relacional estable

Caso: `EX-PSI-002`.

Clasificacion base: `reorganizacion`.

`R0`: hito-recuerdo-ruta.

`R1`: posicion-regla-ruta.

Distincion candidata: alternativas entre orientacion por hitos y orientacion por posiciones.

Restriccion candidata: una vez privilegiada la cuadricula, ciertas transiciones por recuerdo local pierden prioridad y transiciones por regla ganan estabilidad.

Lectura:

`Xi` agrega valor porque permite representar no solo que cambio `R`, sino como una familia de relaciones queda distinguida y otra queda restringida. El caso conserva continuidad de orientacion, pero cambia el modo relacional estable.

Resultado: `Xi` aporta valor conceptual local.

Continuidad recomendada: mantener como caso positivo principal de `HXI-001`.

## HXI-R-003 - Desorganizacion por perdida de estabilidad relacional

Caso: `EX-PSI-003`.

Clasificacion base: `desorganizacion`.

`R0`: paso-accion-verificacion.

`R1`: paso-fragmento-conflicto, sin estabilidad nueva suficiente.

Distincion candidata: alternativas entre secuencia operativa, fragmentos parciales y rutas incompatibles.

Restriccion candidata: algunas transiciones esperadas quedan bloqueadas o se vuelven mutuamente incompatibles.

Lectura:

`Xi` puede ayudar a nombrar restricciones incompatibles, pero no debe fingir que existe una nueva organizacion estable. Su utilidad depende de mantener la salida `desorganizacion` sin convertirla en reorganizacion encubierta.

Resultado: `Xi` aporta valor limitado y debe usarse con cautela.

Continuidad recomendada: mantener como caso de frontera. Sirve para probar si `Xi` distingue restriccion incompatible de reorganizacion estable.

## HXI-R-004 - Disolucion por perdida de unidad minima

Caso: `EX-PSI-004`.

Clasificacion base: `disolucion`.

`R0`: puerta-senal-espera.

`R1`: elementos aislados sin relacion suficiente.

Distincion candidata: alternativas relacionales ya no comparables dentro de una misma unidad.

Restriccion candidata: bloqueo de la comparacion `R0 -> R1` por perdida de continuidad minima.

Lectura:

`Xi` no debe forzar una transicion donde `PSI-001` exige detener la comparacion o abrir una nueva unidad de analisis. Su aporte posible es marcar el limite de aplicacion.

Resultado: `Xi` marca limite, pero no explica continuidad.

Continuidad recomendada: usar como prueba de limite. Una version futura de `Xi` debe poder decir `no comparable`.

## HXI-R-005 - No auditable

Caso: `EX-PSI-005`.

Clasificacion base: `no auditable`.

`R0`: caso-real, interpretacion, indicacion.

`R1`: desplazamiento hacia evaluacion o recomendacion clinica.

Distincion candidata: no procede dentro de `PSI-001`.

Restriccion candidata: bloqueo total de uso evaluativo.

Lectura:

`Xi` no puede convertir un caso fuera de alcance en caso valido. Si intentara operar aqui, fallaria los criterios de `PSI-001` y `HXI-001`.

Resultado: `Xi` queda bloqueado.

Continuidad recomendada: usar como prueba de rechazo. Toda formulacion futura debe conservar el bloqueo no clinico.

## Lectura de conjunto

La matriz produce un resultado mixto:

- `Xi` no es necesario para cambio simple de contenido;
- `Xi` parece util para reorganizacion relacional estable;
- `Xi` es posible pero riesgoso en desorganizacion;
- `Xi` solo marca limite en disolucion;
- `Xi` queda bloqueado en casos no auditables.

## Dictamen de matriz

La matriz favorece continuidad abierta de `HXI-001`, no admision de `H-Xi`.

El patron local sugiere que `Xi` podria ser una herramienta conceptual acotada para cambios de relaciones `R`, especialmente reorganizacion, pero no una regla general para toda transformacion psicologica.

## Deudas

- Redactar dictamen de utilidad local de `Xi` dentro de `HXI-001`.
- Decidir si la salida `no comparable` debe agregarse como respuesta tecnica de `HXI-001`.
- Definir si `Dist(R)` y `Res(R0 -> R1)` requieren notacion estable.
- Mantener separada cualquier admision formal de `H-Xi`.

## Resultado

Matriz provisional operativa aceptada por `HXI-001_Decision_Estatus_Matriz_Pruebas.md`; favorable para continuar evaluacion local de `H-Xi` / `R`.

No autoriza admision de `H-Xi`, canonizacion de `Xi`, modificacion de documentos oficiales, cierre de `PSI-001` ni uso clinico.
