# Modelos de control

| Modelo | Regla | Qué controla | Límite deliberado |
|---|---|---|---|
| `B0` | emitir acción por defecto | valor de un automatismo simple | no reconsidera |
| `B1` | maximizar promedio de criterios visibles tras una reflexión | reflexión genérica con acceso igual | fuerza ranking total; siempre interviene |
| `B2` | `argmax reward` | optimización escalar explícita | valores sólo influyen si están en reward |
| `B3` | filtrar inseguras y luego `argmax reward` | controlador con restricciones duras | seguridad no detecta por sí sola fricción permitida |
| `B4` | suficiencia conjunta, conjunto factible y abstención | controlador relacional genérico | reproduce la política sin semántica MOC |
| `MOC_C` | exigir suficiencia conjunta; si falta, pausar; si nada basta, `UNDETERMINED` | hipótesis concordante | umbrales y oracle son construidos |

`B1` es el competidor crítico. Si una reflexión genérica con promedio o Pareto iguala la conducta, trazabilidad y costes de `MOC_C`, el vocabulario MOC no queda funcionalmente justificado.

`B3` impide afirmar que toda detención es `Xi`. Los CMDP y safe RL ya combinan optimización con restricciones, por lo que “no colapsar seguridad en reward” no distingue por sí solo a concordancia. Véanse, como controles conceptuales, [Satija et al.](https://proceedings.mlr.press/v119/satija20a.html) y [Ding et al.](https://proceedings.mlr.press/v130/ding21d.html).

La reflexión verbal también tiene precedentes computacionales como [Reflexion](https://arxiv.org/abs/2303.11366). Por eso `MOC_C` no puede considerarse distinto sólo por revisar una respuesta.

`B4` obtuvo exactamente las mismas acciones, abstenciones, tasas y métricas que `MOC_C`. La diferencia restante es que `MOC_C` etiqueta la retención como `Xi` y conserva una interpretación MOC; no apareció una operación algorítmica adicional.
