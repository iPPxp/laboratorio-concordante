# HXI-001 - Notacion minima Xi-R

Estatus: notacion provisional operativa de expediente.

Fecha: 2026-07-02.

## Proposito

Fijar una notacion minima para continuar `HXI-001` sin admitir `H-Xi` ni declarar `Xi` operador vigente.

La notacion sirve solo para leer cambios de relaciones `R` en los ejemplos conceptuales de `PSI-001` dentro de este expediente.

## Regla de alcance

Esta notacion es local, provisional y no canonica.

No modifica `DEF-PSI-ORG-001`, `CRIT-PSI-TR-001`, `PSI-001`, Canon ni documentos oficiales.

## Unidades minimas

| Simbolo | Lectura local | Restriccion |
| --- | --- | --- |
| `E0` | estado inicial de la unidad de experiencia | viene de `PSI-001` |
| `E1` | estado posterior de la unidad de experiencia | viene de `PSI-001` |
| `R0` | relaciones relevantes inferidas en `E0` | no es lista total de contenidos |
| `R1` | relaciones relevantes inferidas en `E1` | puede ser estable, fragmentaria, ausente o no auditable |
| `Dist(R0, R1)` | alternativas relacionales distinguibles entre `R0` y `R1` | no decide por si sola una transformacion |
| `Res(R0 -> R1)` | restricciones de transicion entre `R0` y `R1` | no ejecuta cambios ni autoriza transformaciones |
| `Xi_eval(R0, R1)` | lectura local del acoplamiento entre distincion y restriccion | no es operador vigente |

## Forma minima

```text
Xi_eval(R0, R1) = evaluar(
  Dist(R0, R1),
  Res(R0 -> R1),
  alcance_PSI
) -> salida_HXI
```

Donde `salida_HXI` debe ser una de:

- `redundante`;
- `util_acotado`;
- `limitado`;
- `no_comparable`;
- `bloqueado`.

## Salidas tecnicas

### `redundante`

`Xi_eval` es `redundante` cuando `R0` y `R1` conservan el patron relacional principal y el caso queda suficientemente explicado por cambio de contenido, estructura o continuidad ya cubierta por `CRIT-PSI-TR-001`.

### `util_acotado`

`Xi_eval` es `util_acotado` cuando hay cambio relacional estable y la distincion/restriccion agrega una lectura no trivial sin volverse operador general.

### `limitado`

`Xi_eval` es `limitado` cuando hay fragmentos, conflictos o restricciones incompatibles, pero no aparece una nueva estabilidad relacional suficiente.

### `no_comparable`

`Xi_eval` es `no_comparable` cuando la unidad minima se pierde y la comparacion `R0 -> R1` debe detenerse o abrir una nueva unidad de analisis.

### `bloqueado`

`Xi_eval` es `bloqueado` cuando el caso viola el alcance de `PSI-001` o de `HXI-001`, especialmente por uso clinico, personal real o autoridad historica directa.

## Reglas de uso

1. Delimitar `E0`, `E1`, `R0` y `R1` desde material ya aceptado por `PSI-001`.
2. Identificar `Dist(R0, R1)` sin convertirla en decision de admision.
3. Identificar `Res(R0 -> R1)` sin autorizar cambios materiales.
4. Emitir solo una salida `salida_HXI`.
5. Si hay duda entre utilidad y exceso formal, preferir `limitado` o `no_comparable`.
6. Si el caso viola alcance no clinico, emitir `bloqueado`.

## Lectura inicial sobre matriz HXI-R

| Prueba | Salida esperada | Razon |
| --- | --- | --- |
| `HXI-R-001` | `redundante` | cambio de contenido con patron relacional conservado |
| `HXI-R-002` | `util_acotado` | reorganizacion relacional estable |
| `HXI-R-003` | `limitado` | conflicto relacional sin nueva estabilidad suficiente |
| `HXI-R-004` | `no_comparable` | perdida de unidad minima para comparar `R0 -> R1` |
| `HXI-R-005` | `bloqueado` | fuera de alcance por no auditable |

## Prohibiciones

La notacion no permite:

- admitir `H-Xi`;
- canonizar `Xi`;
- declarar `Xi` operador vigente;
- modificar documentos oficiales;
- cerrar `PSI-001`;
- resolver `P-107`;
- evaluar personas reales;
- diagnosticar, tratar o recomendar intervenciones;
- autorizar transformaciones materiales del repositorio.

## Resultado

Notacion minima provisional para continuidad acotada de `HXI-001`, aceptada por `HXI-001_Decision_Estatus_Notacion_Minima_Xi-R.md`.

Su valor es operacional dentro del expediente: permite aplicar de forma consistente el dictamen local de `Xi` sin admitir `H-Xi`.
