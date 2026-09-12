# Modelo de disparo y detención

## Trigger

El control provisional usa una única regla auditable:

\[
active \iff observation.signal \ge \tau.
\]

La decisión registra la señal y el umbral. Esto es un contrato de prueba, no una afirmación de que MOC use ese observable. En modo `AUTOMATIC_SINGLE`, el trigger se fuerza para conservar un control de un solo régimen.

## Xi stop

`Xi` detiene cuando:

1. `Choice=ALLOW`;
2. falta observación suficiente (`REQUEST_OBSERVATION`); o
3. se alcanza `xi_max_steps`.

Si Xi se ablaciona, el ejecutor sólo puede terminar por ausencia de feedback o por la cota externa del protocolo. La ablación no debe convertirse en recursión ilimitada.

## Orden y feedback

El orden nominal es `INFER -> PHI -> CHOICE`. La ablación `ORDER_SWAPPED` ejecuta `PHI -> INFER -> CHOICE` y registra las fases; así se puede probar si el orden aporta algo. La realimentación modifica únicamente `context.salience` mediante una ganancia declarada. No modifica observaciones, valores ni permisos.

## Dictámenes posibles

- Si dual y control automático tienen igual desempeño fuera de muestra: `DUAL_LOOP_ADVANTAGE=NOT_SUPPORTED`.
- Si eliminar Xi causa fallos de terminación bajo la misma cota: soporte local para organización, no para voluntad.
- Si intercambiar el orden no cambia ningún resultado relevante: necesidad del orden no soportada.
- Si el trigger no generaliza a observaciones nuevas: `TRIGGER_MODEL=INSUFFICIENT_EVIDENCE`.

