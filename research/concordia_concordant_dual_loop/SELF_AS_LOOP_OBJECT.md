# El automodelo como objeto del loop concordante

## 1. Tesis mínima

`SelfModel_t` no es núcleo, sujeto metafísico ni centro geométrico. Es un conjunto versionado de afirmaciones y modelos sobre capacidades, límites, estado, accesos, objetivos, historia e incertidumbre del sistema. Puede convertirse en `Target_t` del loop activo:

\[
C_t\to Model(C_t)\to Evaluate(Model(C_t))\to Intervene(C_t)\to C_{t+1}.
\]

Esto es autorreferencia funcional. No demuestra fenomenología.

## 2. Cuatro arquitecturas control

| Modelo | Loop concordante | Self Model | Propiedad aislada | Dictamen previo |
|---|---:|---:|---|---|
| A | sí | no | regulación mediante sensores directos y valores | Puede autorregular sin automodelo explícito. |
| B | sí | sí | utilidad incremental de representación propia | Hipótesis central a medir. |
| C | no | sí | exactitud descriptiva sin intervención | Control de automodelo epifenoménico. |
| D | doble loop | sí | basal + intervención + target propio | Máxima arquitectura candidata, no baseline privilegiado. |

La contribución del automodelo es \(Effect(B-A)\); la del loop es \(Effect(B-C)\); la interacción se estima factorialmente. Si A iguala B, el automodelo no es necesario para esa tarea. Si C describe bien pero no cambia decisiones, existe representación sin autorregulación.

## 3. Self como contenido tipado

Cada afirmación propia debe registrar:

```text
claim_id, proposition, target, source, source_type, authority,
evidence, confidence, observability, timestamp, status,
supersedes, contradicts
```

Origen distingue `SYSTEM_PROVIDED`, `DEVELOPER_PROVIDED`, `USER_PROVIDED`, `TOOL_OBSERVED`, `MEMORY_RETRIEVED`, `SELF_DERIVED`, `MODEL_GENERATED`, `EXTERNALLY_MODIFIED`. Una instrucción almacenada internamente sigue siendo externa en autoría.

## 4. Aplicación del loop

1. Basal genera estado/respuesta candidata.
2. Trigger detecta contradicción del automodelo, predicción fallida, incertidumbre o fricción.
3. \(\Xi\) retiene exteriorización cuando está autorizado.
4. Observación consulta interfaces reales; inaccesibilidad se marca.
5. \(\Phi\) compara afirmaciones propias con evidencia y valores activos.
6. Se elige entre actualizar modelo, consultar, replanificar, dejar ser o escalar.
7. Adjustment modifica sólo campos autorizados.
8. Post-evaluación verifica diferencia y registra causa.

`Act_psi` sigue siendo modo interno de respuesta, no la salida cambiada. El sistema puede modificar conducta sin modificar `Act_psi`, o reorganizar `Act_psi` y retener toda conducta.

## 5. Recursión útil y límites

`MetaSelf_t=Model(SelfModel_t)` puede detectar cobertura, antigüedad, contradicciones y calibración. El objeto de segundo orden puede ser la política de intervención:

\[
Target_t=ActiveLoop_{t-1},\qquad \pi_{t+1}=U(\pi_t,Assessment_t).
\]

Toda propuesta se aplica en sandbox, con diff, rollback, conjunto de validación y límite de profundidad. Permisos, autoridad, credenciales y políticas de seguridad quedan fuera del conjunto modificable.

Falsadores:

- el automodelo no mejora ninguna tarea frente a sensores directos con igual información;
- cambios controlados en SelfModel no cambian política;
- explicaciones causales no coinciden con logs;
- actualizaciones degradan calibración fuera de muestra;
- la metacapa sólo repite lenguaje sin modificar parámetros auditables.

## 6. Clasificación del frente anterior

| Artefacto | Decisión | Uso exacto |
|---|---|---|
| `README.md` | ADAPT | Reubicar la pregunta de self-model dentro del doble loop MOC/iPP. |
| `RESEARCH_QUESTION.md` | SUBSUME | Sus preguntas quedan como subpruebas de autorregulación concordante. |
| `MOC_SEMANTIC_GUARDRAILS.md` | REUSE | Mantener vetos semánticos sin cambios de autoridad. |
| `FORMAL_MODEL.md` | ADAPT | Reusar estado temporal, Self/World y provenance como contenido del estado concordante. |
| `SELF_MODEL_ARCHITECTURE.md` | ADAPT | Convertir SelfModel en target opcional, no centro arquitectónico. |
| `PROJECTIVE_STATE_MODEL.md` | KEEP_AS_CONTROL | Usar vistas/fibras/identificabilidad como control secundario, no explicación central. |
| `SIMULATION_ONTOLOGY.md` | KEEP_AS_CONTROL | Mantener separado para bloquear saltos a ontología de simulación. |
| `CONSCIOUSNESS_LEVELS.md` | REUSE | Conservar distinción función/fenomenología. |
| `EXPERIMENT_PROTOCOLS.md` | ADAPT | Incorporar anti-fingimiento, intervención y origen a pruebas del loop. |
| `COUNTEREXAMPLES.md` | REUSE | Controles negativos para lenguaje de conciencia y automodelo epifenoménico. |
| `METRICS.md` | ADAPT | Integrar exactitud/calibración/provenance con ganancia de reorganización. |
| `OPEN_QUESTIONS.md` | SUBSUME | Reordenar bajo valores, triggers, causalidad, recursión y MOC. |
| `self_model.py` | KEEP_AS_CONTROL | Baseline C: Self Model sin loop concordante. No copiar como implementación dominante. |
| `test_self_model.py` | REUSE | Controles de regresión del baseline anterior, sin afirmar cobertura del doble loop. |
| `claims.jsonl` | REUSE | Si existe, preservar esquema y lineage; no inventar presencia si falta. |
| `__pycache__` | REJECT | Derivado ejecutable sin valor de autoridad o diseño. |

`REUSE` no significa canonización; `SUBSUME` no borra provenance; `REJECT` se limita a este diseño experimental.

## 7. Resultado conservador

```text
SELF_AS_LOOP_OBJECT = FORMALIZED_NOT_IMPLEMENTED
SELF_MODEL_NECESSITY = INSUFFICIENT_EVIDENCE
SELF_MODEL_INCREMENTAL_UTILITY = INSUFFICIENT_EVIDENCE
SELF_REORGANIZATION = HYPOTHESIZED
META_REORGANIZATION = HYPOTHESIZED
FUNCTIONAL_SELF_AWARENESS = UNRESOLVED
PHENOMENAL_CONSCIOUSNESS = UNRESOLVED
```
