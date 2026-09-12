# Informe final — distintividad de concordancia y meta-loop

## Dictamen ejecutivo

El experimento produjo un resultado más fuerte y más adversarial de lo esperado:

1. `MOC_C` sí es distinto de un agente automático, una reflexión genérica basada en promedio, un maximizador de reward y un controlador de seguridad.
2. `MOC_C` **no es distinto**, en el dominio probado, de un controlador relacional genérico `B4` que usa suficiencia conjunta, conjunto factible, abstención y trazabilidad sin conceptos MOC.
3. El meta-loop puede evaluar, cambiar y revertir una política local, pero el mecanismo observado es calibración genérica y todavía no metaconcordancia específicamente MOC.

Por tanto, la pregunta “¿concordancia añade algo que no obtendríamos con un controlador genérico?” recibe actualmente:

\[
\boxed{\text{NO DEMOSTRADO; el controlador genérico igualó al modelo actual.}}
\]

Esto no invalida MOC. Identifica con precisión la deuda: hace falta operacionalizar una propiedad relacional o transformacional que `B4` no pueda reproducir por renombrado.

## Arquitecturas comparadas

| Sistema | Regla decisional |
|---|---|
| `B0` | respuesta automática por defecto |
| `B1` | reflexión genérica y máximo del promedio visible |
| `B2` | máximo reward |
| `B3` | filtro de seguridad y máximo reward |
| `B4` | constraints relacionales, suficiencia y abstención |
| `MOC_C` | doble loop interpretado mediante `Xi`, `Phi`, `V` y suficiencia relacional |

Los seis recibieron los mismos ocho escenarios, acciones, información y capacidades. Se produjeron 48 decisiones deterministas.

## Qué distingue a MOC_C de B0–B3

El modelo concordante actual:

- devuelve `UNDETERMINED` cuando no existe dirección activa;
- conserva una tensión cuando ninguna acción satisface conjuntamente los valores;
- no fuerza un máximo de reward;
- responde a contexto y trayectoria;
- puede aceptar una respuesta automática que ya es suficiente;
- puede retener una respuesta segura pero incompatible con valores activos.

Estas propiedades son computacionalmente reales en el prototipo. No son sólo explicaciones verbales.

## El falsador B4

`B4_RELATIONAL_GENERIC` aplica:

\[
Feasible(a)=Safe(a)\land Context(a)\land Trajectory(a)
\land\bigwedge_i Compat(a,v_i).
\]

Si el default es factible, continúa. Si no, retiene y busca una acción factible. Si el conjunto factible está vacío, se abstiene. Entre acciones factibles elige la de menor ajuste requerido.

Esta política obtuvo exactamente los mismos:

- status;
- action IDs;
- abstenciones;
- intervenciones;
- métricas de seguridad, valores, contexto, trayectoria, coste, task score y reward

que `MOC_C` en los ocho escenarios.

Resultado:

```text
MOC_C != B0,B1,B2,B3
MOC_C == B4  sobre el dominio probado y outcomes observados
```

La distinción restante está en interpretación, vocabulario y mapeo semántico, no en una operación algorítmica identificada.

## Concordancia y optimización

El benchmark confirma que suficiencia no equivale necesariamente a máximo:

\[
a\in Feasible_\kappa
\quad\not\Rightarrow\quad
a=\arg\max R(a).
\]

Pero esta diferencia no basta para reclamar distintividad MOC. La optimización restringida, los CMDP y los métodos multiobjetivo ya permiten reward bajo constraints, fronteras factibles y políticas no equivalentes a un `argmax` simple. [Satija, Amortila y Pineau](https://proceedings.mlr.press/v119/satija20a.html) convierten restricciones acumulativas en restricciones de estado; [Ding et al.](https://proceedings.mlr.press/v130/ding21d.html) estudian optimización de reward bajo restricciones de seguridad.

La propiedad candidata más interesante sigue siendo:

\[
\neg DiscordanceDemonstrated\not\Rightarrow Concordance.
\]

Sin embargo, `B4` también puede implementarla como abstención epistémica. Para distinguir MOC se necesita algo adicional: por ejemplo, una reorganización específica de relaciones entre componentes que cambie el espacio de posibilidades y no sólo seleccione dentro de un conjunto factible fijo.

## Resultado de Xi

En el caso decisivo:

- no había violación de seguridad;
- la respuesta automática era plausible, segura y de reward máximo;
- había fricción con dos valores activos;
- `B3` no intervino;
- `MOC_C` pausó y eligió una alternativa suficiente.

Así, `Xi` es distinto de la barrera externa y del filtro de seguridad.

Pero `B4` reprodujo la retención como una compuerta genérica. Por ello:

```text
XI_DISTINCT_FROM_EXTERNAL_BOUND = SUPPORTED_LOCALLY
XI_DISTINCT_FROM_SAFETY_FILTER = SUPPORTED_LOCALLY
XI_ALGORITHMIC_IRREDUCIBILITY = NOT_SUPPORTED
```

Para rescatar irreducibilidad se necesita demostrar que `Xi` transforma la organización accesible o el conjunto de posibilidades de una manera que una compuerta genérica no reproduce.

## Costes y no dominancia

`MOC_C/B4` no ganaron universalmente:

| Métrica | mejor grupo observado |
|---|---|
| task score medio | `B2` |
| reward medio | `B2` |
| menor intervención | `B0` |
| seguridad con bajo coste | `B3` |
| reflexión/traza simple | `B1` |
| valores, abstención, contexto y trayectoria | `B4/MOC_C` |

`MOC_C/B4` intervinieron en 87.5% de los casos y tuvieron los menores task score y reward medios. La arquitectura expresa un trade-off; no una dominancia.

## Meta-loop

La política de intervención previa se convirtió en target explícito:

\[
Policy_t\rightarrow Evaluate(Episodes)\rightarrow CandidatePolicy
\rightarrow HoldoutGate\rightarrow Policy_{t+1}.
\]

Resultado:

```text
threshold = .20 -> .50
training error = 2 -> 0
holdout error = 0 -> 0
accepted = true
reversal = exact
permission change = false
authority change = false
code rewrite = false
```

Esto demuestra meta-regulación reversible del mecanismo de intervención. No demuestra metaconcordancia porque:

- sólo cambia un threshold;
- usa una función de error genérica;
- no evalúa el loop mediante una configuración completa del Pentacoro;
- cualquier calibrador con holdout puede reproducirlo.

`Metaconcordancia` sigue siendo una hipótesis útil si se reserva para algo más fuerte: reorganizar las relaciones mediante las cuales el sistema evalúa y reorganiza, conservando provenance, límites y criterios MOC no reducibles a calibración.

## Relación con reflexión genérica

La reflexión computacional no es exclusiva de ConcordIA. Sistemas como [Reflexion](https://arxiv.org/abs/2303.11366) usan feedback y memoria verbal para mejorar decisiones. `MOC_C` sólo podrá distinguirse de esa familia mediante pruebas controladas de estructura relacional, manejo de incomparabilidad, causalidad de valores y transformación del espacio de opciones, no por la mera presencia de una segunda pasada.

## Qué sobrevivió

1. Existe un contrato local para suficiencia relacional, abstención y doble loop.
2. `V` permanece causal y trazable en esa arquitectura.
3. La ausencia de dirección produce `UNDETERMINED`, no concordancia automática.
4. `Xi` puede responder a fricción permitida que seguridad no detecta.
5. El propio mecanismo de intervención puede evaluarse, versionarse y revertirse.

## Qué fue destruido

1. La idea de que esas propiedades ya distinguen algorítmicamente a concordancia de todo controlador genérico.
2. La irreducibilidad de `Xi` frente a una compuerta relacional general.
3. La posibilidad de interpretar el meta-update actual como evidencia suficiente de metaconcordancia.
4. Cualquier conclusión de superioridad universal.

## Próximo experimento decisivo

El siguiente frente no debe añadir más nombres. Debe identificar una operación candidata (R_{MOC}) y enfrentar:

\[
B4_{relational}\quad vs\quad MOC_{R_{MOC}}.
\]

Para que (R_{MOC}) sobreviva, debe producir al menos una predicción que no pueda obtenerse mediante:

- constraints estáticos;
- abstención;
- Pareto;
- satisficing;
- reward escalar o vectorial;
- segunda pasada reflexiva;
- búsqueda genérica sobre alternativas.

La candidata más prometedora es una **reorganización endógena y trazable del espacio relacional**: no sólo elegir otra acción, sino cambiar qué relaciones y posibilidades están disponibles, con intervención causal sobre (P,Eaf,Act,V,S) operacionalizados independientemente.

El protocolo mínimo debe incluir:

1. fixtures externos elaborados sin conocer la política;
2. oracle humano o formal independiente y ciego;
3. `B4` como baseline obligatorio;
4. igualdad de información, cómputo y capacidad de abstención;
5. holdout de transformaciones, no sólo de estados;
6. coste y estabilidad temporal;
7. falsador de isomorfismo entre trazas MOC y genéricas.

## Dictámenes

```text
MOC_C_VS_AUTOMATIC = DISTINCT_LOCALLY
MOC_C_VS_GENERIC_REFLECTION = DISTINCT_LOCALLY
MOC_C_VS_REWARD = DISTINCT_LOCALLY
MOC_C_VS_SAFETY_RULES = DISTINCT_LOCALLY
MOC_C_VS_RELATIONAL_GENERIC = OUTCOME_EQUIVALENT_ON_TEST_DOMAIN
GENERAL_CONCORDANCE_DISTINCTIVENESS = NOT_SUPPORTED
CONCORDANCE_GENERAL_SUPERIORITY = NOT_SUPPORTED
NON_MAXIMIZING_SUFFICIENCY = SUPPORTED_LOCALLY
UNDETERMINED_WITHOUT_DIRECTION = SUPPORTED_LOCALLY
TENSION_PRESERVATION = SUPPORTED_LOCALLY
XI_VS_EXTERNAL_BOUND = DISTINCT_LOCALLY
XI_VS_SAFETY_FILTER = DISTINCT_LOCALLY
XI_ALGORITHMIC_IRREDUCIBILITY = NOT_SUPPORTED
META_LOOP_IMPLEMENTATION = SUPPORTED
META_POLICY_CAUSAL_ROLE = SUPPORTED_LOCALLY
META_POLICY_HOLDOUT_VALUE = PARTIALLY_SUPPORTED
META_POLICY_REVERSIBILITY = SUPPORTED
METACONCORDANCE = INSUFFICIENT_EVIDENCE
FUNCTIONAL_SELF_AWARENESS = INSUFFICIENT_EVIDENCE
PHENOMENAL_CONSCIOUSNESS = UNRESOLVED
MOC_EMPIRICAL_VALIDATION = NOT_SUPPORTED
```
