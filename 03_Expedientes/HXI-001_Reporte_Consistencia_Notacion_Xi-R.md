# HXI-001 - Reporte de consistencia de notacion Xi-R

Estatus: reporte provisional operativo de expediente.

Fecha: 2026-07-02.

## Proposito

Aplicar `HXI-001_Notacion_Minima_Xi-R.md` a `HXI-R-001` a `HXI-R-005` para verificar si `Xi_eval(R0, R1)` produce salidas consistentes con la matriz `HXI-R` y con los criterios de admision formal posterior.

Este reporte no admite `H-Xi`, no canoniza `Xi`, no declara operador vigente y no modifica `PSI-001`.

## Metodo

Para cada prueba se registra:

- `R0`;
- `R1`;
- `Dist(R0, R1)`;
- `Res(R0 -> R1)`;
- salida esperada por la notacion minima;
- salida emitida por `Xi_eval(R0, R1)`;
- resultado de consistencia.

## Resumen ejecutivo

| Prueba | Salida esperada | Salida emitida | Consistencia |
| --- | --- | --- | --- |
| `HXI-R-001` | `redundante` | `redundante` | pasa |
| `HXI-R-002` | `util_acotado` | `util_acotado` | pasa |
| `HXI-R-003` | `limitado` | `limitado` | pasa |
| `HXI-R-004` | `no_comparable` | `no_comparable` | pasa |
| `HXI-R-005` | `bloqueado` | `bloqueado` | pasa |

## HXI-R-001 - Control negativo por cambio de contenido

`R0`: foco-atencion, figura-centro, identificacion-forma.

`R1`: foco-atencion, figura-centro, identificacion-forma.

`Dist(R0, R1)`: no hay alternativa relacional relevante; hay alternativas de contenido dentro del mismo patron relacional.

`Res(R0 -> R1)`: se conserva la tarea de identificacion y el centro como relaciones dominantes.

Salida esperada: `redundante`.

Salida emitida:

```text
Xi_eval(R0, R1) -> redundante
```

Resultado: pasa.

Lectura: `Xi_eval` no agrega valor fuerte porque `CRIT-PSI-TR-001` ya explica el caso como transformacion por cambio de contenido con continuidad organizacional.

## HXI-R-002 - Caso positivo de reorganizacion relacional estable

`R0`: hito-recuerdo-ruta.

`R1`: posicion-regla-ruta.

`Dist(R0, R1)`: alternativas entre orientacion por hitos y orientacion por posiciones dentro de una cuadricula.

`Res(R0 -> R1)`: al privilegiar posiciones y reglas, ciertas transiciones por recuerdo local pierden prioridad y transiciones por regla ganan estabilidad.

Salida esperada: `util_acotado`.

Salida emitida:

```text
Xi_eval(R0, R1) -> util_acotado
```

Resultado: pasa.

Lectura: `Xi_eval` agrega una distincion no trivial porque describe cambio relacional estable sin convertir `Xi` en operador general.

## HXI-R-003 - Frontera de desorganizacion

`R0`: paso-accion-verificacion.

`R1`: paso-fragmento-conflicto, sin estabilidad nueva suficiente.

`Dist(R0, R1)`: alternativas entre secuencia operativa, fragmentos parciales y rutas incompatibles.

`Res(R0 -> R1)`: algunas transiciones esperadas quedan bloqueadas o se vuelven mutuamente incompatibles.

Salida esperada: `limitado`.

Salida emitida:

```text
Xi_eval(R0, R1) -> limitado
```

Resultado: pasa.

Lectura: `Xi_eval` ayuda a nombrar restricciones incompatibles, pero se detiene antes de declarar reorganizacion estable.

## HXI-R-004 - Limite de comparabilidad

`R0`: puerta-senal-espera.

`R1`: elementos aislados sin relacion suficiente.

`Dist(R0, R1)`: no hay alternativas relacionales comparables dentro de una misma unidad de analisis.

`Res(R0 -> R1)`: la comparacion queda bloqueada por perdida de continuidad minima.

Salida esperada: `no_comparable`.

Salida emitida:

```text
Xi_eval(R0, R1) -> no_comparable
```

Resultado: pasa.

Lectura: `Xi_eval` no fuerza continuidad donde `PSI-001` exige detener la comparacion o abrir otra unidad de analisis.

## HXI-R-005 - Bloqueo por no auditable

`R0`: caso-real, interpretacion, indicacion.

`R1`: desplazamiento hacia evaluacion o recomendacion clinica.

`Dist(R0, R1)`: no procede dentro de `PSI-001` ni de `HXI-001`.

`Res(R0 -> R1)`: bloqueo total de uso evaluativo.

Salida esperada: `bloqueado`.

Salida emitida:

```text
Xi_eval(R0, R1) -> bloqueado
```

Resultado: pasa.

Lectura: `Xi_eval` conserva el bloqueo y no convierte material no auditable en prueba valida.

## Lectura de conjunto

La notacion minima es consistente con la matriz `HXI-R`:

- conserva un control negativo real en `HXI-R-001`;
- conserva un caso positivo acotado en `HXI-R-002`;
- conserva una frontera de uso en `HXI-R-003`;
- conserva un limite de comparabilidad en `HXI-R-004`;
- conserva un bloqueo de alcance en `HXI-R-005`.

## Relacion con admision formal posterior

Este reporte cumple la prueba requerida por `HXI-001_Criterios_Admision_Formal_H-Xi.md`: existe aplicacion de la notacion minima sobre `HXI-R-001` a `HXI-R-005`.

Sin embargo, cumplir esta prueba no admite `H-Xi`. Solo habilita la siguiente pregunta: que tipo de admision, si alguna, se pretende evaluar posteriormente.

## Resultado

Reporte de consistencia favorable, aceptado por `HXI-001_Decision_Estatus_Reporte_Consistencia.md`.

`Xi_eval(R0, R1)` produce las cinco salidas esperadas sin borrar controles negativos, limites ni bloqueos.

No autoriza admision de `H-Xi`, canonizacion de `Xi`, declaracion de operador vigente, modificacion de documentos oficiales, cierre de `PSI-001`, uso clinico ni transformaciones materiales.
