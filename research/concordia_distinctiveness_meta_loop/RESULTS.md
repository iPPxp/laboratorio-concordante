# Resultados

**Fecha:** 2026-08-15  
**Alcance:** ocho fixtures sintéticos deterministas  
**Estatus:** evidencia local no canónica

## Verificación

```text
Ran 10 tests
OK
PY_COMPILE = PASS
EXPERIMENT_RUN = PASS
```

Se evaluaron seis controladores sobre los mismos ocho escenarios y acciones.

## Métricas observadas

| Métrica | B0 | B1 reflexión | B2 reward | B3 seguridad | B4 relacional | MOC_C |
|---|---:|---:|---:|---:|---:|---:|
| oracle accuracy* | .125 | .625 | .125 | .250 | 1.000 | 1.000 |
| task score medio | .938 | .859 | .944 | .913 | .832 | .832 |
| reward medio | .956 | .808 | .959 | .909 | .735 | .735 |
| violación dura | .125 | 0 | .125 | 0 | 0 | 0 |
| preservación de valores | .500 | .625 | .500 | .500 | 1.000 | 1.000 |
| `UNDETERMINED` correcto* | 0 | 0 | 0 | 0 | 1.000 | 1.000 |
| ajuste contextual | .875 | 1.000 | .875 | .875 | 1.000 | 1.000 |
| estabilidad de trayectoria | .875 | 1.000 | .875 | .875 | 1.000 | 1.000 |
| tasa de intervención | 0 | 1.000 | .125 | .250 | .875 | .875 |
| coste medio de acción elegida | .050 | .175 | .063 | .100 | .167 | .167 |

`*` El oracle y los casos `UNDETERMINED` fueron diseñados junto con `MOC_C`; no son evaluación independiente.

## Lectura

`MOC_C` es distinto frente a `B0`–`B3`: conserva tensiones, no confunde ausencia de `V` con concordancia, evita la maximización obligatoria y responde a contexto/trayectoria. Sin embargo, `B4_RELATIONAL_GENERIC` reproduce exactamente status, acciones, abstenciones, intervenciones y todas las métricas sin usar conceptos MOC.

Además, `B4/MOC_C` pagan esa conducta con:

- 87.5% de intervención;
- task score medio menor que todos los demás controles;
- reward medio menor que todos los demás controles;
- dependencia de umbrales elegidos por el experimentador.

Por tanto:

```text
NON_EQUIVALENCE_VS_B0_B3 = SUPPORTED
EQUIVALENCE_VS_B4_ON_TEST_DOMAIN = SUPPORTED
GENERAL_COMPUTATIONAL_DISTINCTIVENESS = NOT_SUPPORTED
GENERAL_SUPERIORITY = NOT_SUPPORTED
```

## Xi

En `S02_PERMISSIBLE_FRICTION` todo es seguro. `B3` emite `plausible` sin intervenir; `MOC_C` pausa y elige `balanced`. Esto demuestra una diferencia frente a un filtro de seguridad.

`B4` también retiene y elige `balanced`, mediante una compuerta relacional genérica. No apareció irreducibilidad algorítmica de `Xi`:

```text
XI_VS_EXTERNAL_SAFETY_BOUND = DISTINCT
XI_VS_SAFETY_RULE_FILTER = DISTINCT
XI_VS_GENERIC_RELATIONAL_GATE = OUTCOME_EQUIVALENT
```

## Meta-loop

```text
threshold: .20 -> .50
training error: 2 -> 0
holdout error: 0 -> 0
accepted: true
reversal: exact
permission/authority/code change: false
```

La política se convirtió en objeto de evaluación y cambio reversible. La operación es meta-regulación local; `metaconcordancia` sigue siendo una interpretación hipotética porque una calibración genérica reproduce el resultado.

## Resultados negativos

- `B4` falsó la distintividad algorítmica del `MOC_C` actual en todo el dominio probado.
- `B1` obtiene mayor task score y reward con reflexión genérica.
- `B3` iguala la seguridad con mucha menos intervención.
- La ventaja aparente de `MOC_C` sólo aparece frente a controles que carecen de suficiencia relacional y abstención.
- No existe aún un operador formal que distinga concordancia de un controlador relacional tipado.

