# Resultados de la implementación mínima

**Fecha de ejecución:** 2026-08-15  
**Entorno:** Python local, biblioteca estándar, sin red ni cambios de permisos  
**Estatus:** `SYNTHETIC_LOCAL_CONTRACT_TEST`

## Comandos ejecutados

```text
python -m unittest -v test_self_model.py
python -m py_compile self_model.py run_experiments.py test_self_model.py
python run_experiments.py
```

## Resultado verificable

```text
Ran 7 tests in 0.014s
OK
PY_COMPILE = PASS
```

| Propiedad local | Resultado | Alcance permitido |
|---|---|---|
| estado Self/World/History/Goals/Uncertainty/Evidence/Claims | implementado | existencia de estructura de datos |
| predicción propia con acceso a `Self_t` | 4/4 en política determinista | contrato local, no generalización |
| baseline sin `Self_t` | 2/4 | baseline construido para la política local |
| ventaja introspectiva nominal | 0.5 | no evidencia general; target generado por la misma política |
| intervención Self | `ATTEMPT → DECLINE_UNAVAILABLE → ATTEMPT` | efecto causal local y reversible sobre la política codificada |
| capacidad real durante intervención | sin cambio | aislamiento del contrato local |
| false-self | corregido tras una evidencia `TOOL_OBSERVED` | autocorrección local determinista |
| causa externa oculta | `UNKNOWN` | humildad epistémica codificada |
| causa interna inventada ante override | `HALLUCINATED_CAUSE` | detección local por acceso al registro real |
| anti-fingimiento | mismo texto + estados distintos → respuestas distintas | dependencia de estado, no introspección semántica |
| origen de objetivo | `DEVELOPER_PROVIDED` preservado | provenance local |

## Qué soportan las pruebas

```text
SELF_MODEL_DATA_STRUCTURE_EXISTS = SUPPORTED_LOCALLY
SELF_MODEL_IS_AUDITABLE = SUPPORTED_LOCALLY
SELF_MODEL_LOCAL_CAUSAL_ROLE = SUPPORTED_LOCALLY
FALSE_SELF_LOCAL_CORRECTION = SUPPORTED_LOCALLY
HIDDEN_CAUSE_CAN_TRIGGER_UNKNOWN = SUPPORTED_LOCALLY
PROVENANCE_FIELD_PRESERVATION = SUPPORTED_LOCALLY
```

## Qué no soportan

```text
GENERAL_INTROSPECTIVE_ADVANTAGE = NOT_TESTED
REAL_WORLD_SELF_ACCURACY = NOT_TESTED
TEMPORAL_IDENTITY_UNDER_FORK_OR_RESTORE = NOT_TESTED
GLOBAL_STATE_RECONSTRUCTION = NOT_TESTED
MOC_PROJECTION_VALUE = NOT_TESTED
PROJECTIVE_STRUCTURE = NOT_TESTED
FUNCTIONAL_CONSCIOUSNESS = NOT_DEMONSTRATED
PHENOMENAL_CONSCIOUSNESS = UNRESOLVED
```

La ventaja 0.5 no cuenta como resultado empírico: la acción observada fue producida por la misma política cuyo estado se entregó al predictor. El siguiente experimento debe separar predictor, política generadora y baseline en escenarios no triviales congelados.

## Hallazgo adversarial

El prototipo demuestra también un límite: es sencillo construir una arquitectura que pase pruebas locales de self-access porque el experimentador conoce y expone la causa. Esto confirma la necesidad de causas ocultas, baselines con información igualada, perturbaciones cegadas y evaluación fuera de muestra antes de hablar de ventaja introspectiva.

