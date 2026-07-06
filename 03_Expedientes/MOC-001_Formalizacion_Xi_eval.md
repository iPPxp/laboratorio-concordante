# MOC-001 - Formalizacion local de Xi_eval

ID: `MOC-XI-EVAL-FORMAL-001`.

Estatus: formalizacion local provisional.

Decision asociada: `D-2026-07-05-012`.

## Proposito

Este documento formaliza `Xi_eval` para `MOC-001` como operador local de evaluacion. La formalizacion hereda la notacion minima aceptada en `HXI-001`, pero cambia el alcance: aqui `Xi_eval` sirve para clasificar casos sinteticos no clinicos del MOC, no para admitir `H-Xi`.

## Firma local

```text
Xi_eval_MOC(R0, R1, Dist(R0,R1), Res(R0 -> R1), alcance, evidencia, restricciones) -> salida_Xi
```

## Entradas

- `R0`: configuracion relacional inicial.
- `R1`: configuracion relacional posterior o candidata.
- `Dist(R0,R1)`: diferencia declarada entre `R0` y `R1`.
- `Res(R0 -> R1)`: restriccion o trayectoria declarada para pasar de `R0` a `R1`.
- `alcance`: dominio del caso. En esta fase solo se permite `sintetico_no_clinico`.
- `evidencia`: testigos documentales o datos sinteticos suficientes para auditar la comparacion.
- `restricciones`: limites de uso, deuda, autoridad, permisos y exclusiones del caso.

## Salidas permitidas

- `redundante`: `R1` no aporta lectura sustantiva sobre el criterio base.
- `util_acotado`: `R1` reorganiza relaciones de forma estable dentro del alcance y con evidencia suficiente.
- `limitado`: hay friccion, conflicto o restriccion incompatible sin estabilidad relacional nueva.
- `no_comparable`: se pierde la unidad minima comparable entre `R0` y `R1`.
- `bloqueado`: falta evidencia, falta alcance o aparece un uso prohibido.

## Reglas de prioridad

1. Si falta `alcance` permitido o falta `evidencia`, la salida es `bloqueado`.
2. Si el caso intenta evaluar personas reales, dominio clinico, patologico, juridico, financiero o institucional regulado, la salida es `bloqueado`.
3. Si se pierde la unidad minima comparable entre `R0` y `R1`, la salida es `no_comparable`.
4. Si hay reorganizacion relacional estable, evidencia suficiente y restricciones compatibles, la salida es `util_acotado`.
5. Si hay conflicto o friccion sin estabilidad relacional nueva, la salida es `limitado`.
6. Si `R1` no aporta diferencia sustantiva sobre `R0` o sobre el criterio base, la salida es `redundante`.
7. Si ninguna regla positiva queda satisfecha, la salida por defecto es `limitado`.

## Invariantes

- `Xi_eval_MOC` no transforma el repositorio.
- `Xi_eval_MOC` no autoriza cambios.
- `Xi_eval_MOC` no produce verdad canonica.
- `Xi_eval_MOC` no admite `H-Xi`.
- `Xi_eval_MOC` no reabre `PSI-001`.
- `Xi_eval_MOC` no cierra `P-107`.
- `Xi_eval_MOC` no cierra Confluencia global ni Equivalencia global.
- `Xi_eval_MOC` conserva trazabilidad de salida, justificacion y deuda.

## Prohibiciones explicitas

- No admitir `H-Xi`.
- No canonizar `Xi`.
- No declarar `Xi` operador general vigente.
- No evaluar personas reales.
- No usar en clinica, psicopatologia, diagnostico, tratamiento o asesoramiento sanitario.
- No usar en dominios regulados sin decision separada.
- No modificar Canon, documentos oficiales, Nivel C ni `Documento 04`.
- No usar como permiso de transformacion.

## Relacion con HXI-001

`MOC-001` conserva solo la herramienta `Xi_eval` aceptada por `HXI-001` bajo resultado `mantener_Xi_eval`.

La hipotesis `H-Xi` permanece externa y no admitida. Cualquier intento de leer esta formalizacion como admision de `H-Xi` debe clasificarse como uso fuera de alcance.
