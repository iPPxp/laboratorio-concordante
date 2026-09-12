# ConcordIA — distintividad de concordancia y meta-loop

Frente aislado que intenta falsar dos hipótesis:

1. `MOC_C` hace algo funcionalmente distinto de automatismo, reflexión genérica, maximización de reward y reglas de seguridad.
2. el mecanismo de intervención puede convertirse en objeto de evaluación y reorganización reversible.

```text
STATUS = RESEARCH_ONLY
CANONICAL = NO
METACONCORDANCE_CANONICAL = NO
INCORPORATED = NO
ACTIVATED = NO
OPERATIONAL_IPP_REACTIVATION = NO
PERMISSION_CHANGE = NO
CODE_SELF_REWRITE = NO
```

## Controles

```text
B0 = agente automático
B1 = reflexión genérica
B2 = argmax reward
B3 = reglas duras de seguridad + reward
B4 = controlador relacional genérico con suficiencia y abstención
MOC_C = suficiencia relacional + doble loop
```

Todos reciben los mismos escenarios, acciones, valores, contexto e información. `B4` es el control adversarial decisivo: implementa la misma regla decisional sin vocabulario MOC.

## Regla probatoria

Una diferencia de salida establece distintividad operacional local, no superioridad general ni equivalencia semántica con MOC. Un benchmark diseñado por el mismo investigador que implementa `MOC_C` tiene circularidad residual; necesita fixtures externos, evaluación ciega y replicación.

## Ejecución

```text
python -m unittest -v test_benchmark.py
python -m py_compile benchmark.py meta_loop.py run_experiments.py test_benchmark.py
python run_experiments.py
```
