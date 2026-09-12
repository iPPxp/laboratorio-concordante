# Gobierno del dataset de factorización MOC F0

**Estatus:** contrato de investigación aislado. No es Canon MOC, validación humana, instrumento clínico ni autorización de despliegue.

## Separación obligatoria de funciones

```text
DATASET_DESIGNER != MOC_ANNOTATOR != OUTCOME_AUTHOR != MODEL_BUILDER != EVALUATOR
```

| Rol | Puede | No puede |
|---|---|---|
| `DATASET_DESIGNER` | crear casos de entrada, IDs, particiones y metadatos neutrales | asignar etiquetas MOC finales, outcomes o ajustar casos al modelo |
| `MOC_ANNOTATOR` | anotar únicamente entradas autorizadas según protocolo | consultar outcomes, diseño sellado, predicciones o código de modelos |
| `OUTCOME_AUTHOR` | fijar outcomes sellados después de congelar entradas/anotaciones | alterar entradas o revelar outcomes a anotadores/model builders |
| `MODEL_BUILDER` | desarrollar sobre la partición permitida | leer holdout/outcomes sellados o cambiar etiquetas para favorecer el modelo |
| `EVALUATOR` | ejecutar evaluación congelada y reportar métricas | reentrenar, reinterpretar etiquetas post hoc u ocultar resultados negativos |

Una misma persona o agente no debe acumular roles incompatibles en la misma corrida. Si ocurre por limitación material, el resultado se marca `ROLE_SEPARATION_BREACH` y no cuenta como evaluación ciega.

## Autoridad y guardas

MOC conserva autoridad semántica. Este dataset sólo operacionaliza una tarea sintética o documental. Etiquetas, relaciones, digests, tests o métricas no canonizan semántica ni prueban experiencias reales.

```text
Act_psi != conducta
Act_psi != ACT_psi
V_psi != reward
ANNOTATION != OBSERVATION_OF_A_PERSON
MODEL_SUCCESS != HUMAN_VALIDATION
```

## Estados

Artefactos: `DRAFT`, `FROZEN`, `SEALED`, `ANNOTATED`, `EVALUATION_READY`, `EVALUATED`, `SUPERSEDED`, `REJECTED`, `QUARANTINED`.

Claims: `OBSERVED_IN_PROVIDED_TEXT`, `DECLARED_BY_CASE`, `ANNOTATOR_INFERENCE`, `DERIVED`, `HYPOTHESIZED`, `ABSENT`, `AMBIGUOUS`, `UNKNOWN`, `CONFLICTED`, `REJECTED`.

`ABSENT`, `AMBIGUOUS` y `UNKNOWN` no son equivalentes: ausencia exige evidencia suficiente de no presencia dentro del campo revisado; ambigüedad indica varias lecturas compatibles; desconocido indica información insuficiente.

## Flujo

1. Designer materializa entradas y manifiesto.
2. Se congela el hash de entradas.
3. Annotator recibe sólo la superficie autorizada.
4. Se congelan anotación, provenance y desacuerdos.
5. Outcome Author fija outcomes en superficie sellada.
6. Model Builder trabaja sólo con development autorizado.
7. Evaluator abre holdout/outcomes una vez bajo protocolo.
8. Todo cambio posterior crea versión nueva; nunca reescribe silenciosamente una evaluación.

## Incidentes bloqueantes

- acceso del anotador a `sealed_design/`, `outcomes/`, predicciones o código de modelos;
- filtración del holdout al desarrollo;
- modificación de inputs después de anotar sin nueva versión;
- sustitución de `UNKNOWN` por inferencia obligatoria;
- colapso `Act_psi`/conducta/`ACT_psi` o `V_psi`/reward;
- claims humanos, clínicos, diagnósticos, terapéuticos o causales;
- datos personales o casos reales no autorizados;
- omisión de conflictos, desacuerdos o provenance.

Ante incidente: `QUARANTINED`, con alcance, artefactos afectados y posibilidad o imposibilidad de repetición limpia.
