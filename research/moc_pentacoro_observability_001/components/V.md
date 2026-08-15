# V — Ficha operacional candidata

```text
COMPONENT = V
DECISION_STATUS = PENDING_HUMAN_REVIEW
```

| Campo | Propuesta para revisión humana |
|---|---|
| `NOMINAL_DEFINITION` | Valores, dirección o criterio orientador: lo que importa sostener en la experiencia. |
| `OBSERVABLE_POSITIVE_CRITERIA` | Evidencia atribuible de un criterio de importancia o dirección que orienta una evaluación, continuidad, renuncia, conflicto o prioridad. Puede ser explícito o inferible sólo si el criterio organiza el fragmento. |
| `OBSERVABLE_NEGATIVE_CRITERIA` | No bastan gusto, preferencia puntual, deseo, comodidad, reward, objetivo instrumental, mandato externo o una evaluación P sin función de importancia. |
| `ABSENT_CRITERIA` | Evidencia explícita de que ninguna consideración de importancia orienta la configuración dentro del alcance, o que la selección se declara puramente instrumental sin criterio ulterior, sujeto a aprobación humana. El silencio produce `UNKNOWN`. |
| `AMBIGUOUS_CRITERIA` | No puede decidirse entre preferencia y criterio de importancia, entre evaluación P y orientación V, o hay criterios de importancia incompatibles sin prioridad. |
| `UNKNOWN_CRITERIA` | Existe elección, objetivo o preferencia, pero no se informa qué importa ni si funciona como dirección. |
| `SUBJECT_ATTRIBUTION_RULES` | El criterio debe ser sostenido o adoptado por el sujeto. Un valor impuesto o citado no se atribuye sin adopción. |
| `THIRD_PARTY_EXCLUSION_RULES` | Excluir prioridades de terceros, normas mencionadas pero rechazadas, recompensas externas y objetivos asignados sin apropiación. |
| `PRESENCE_RULES` | `PRESENT` exige función orientadora, no sólo contenido valorativo. Dos valores en conflicto pueden estar presentes simultáneamente. |
| `STABILITY_RULES` | Requiere continuidad del criterio orientador en momentos comparables, aunque cambien preferencias o medios. |
| `CHANGE_RULES` | Requiere cambio en importancia, prioridad, dirección o relación entre criterios; cambiar de medio instrumental no basta. |
| `BOUNDARY_CASES` | Preferencia profunda/puntual; objetivo/valor; regla P/criterio V; emoción intensa/importancia; norma externa/adopción. |
| `NEGATIVE_NEIGHBORS` | Preferencia, deseo, gusto, objetivo instrumental, reward, interpretación evaluativa, norma externa. |
| `COUNTEREXAMPLES` | Elegir lo agradable no prueba V. Perseguir un medio no revela el criterio final. Sentir intensamente no demuestra importancia orientadora. |

## Prueba humana de dureza

La autoridad debe poder decidir por separado:

- preferencia sin dirección valorativa;
- dirección valorativa contra preferencia inmediata;
- objetivo instrumental sin valor explícito;
- valor implícito sin objetivo;
- criterios en conflicto;
- ausencia real de dirección discernible.
