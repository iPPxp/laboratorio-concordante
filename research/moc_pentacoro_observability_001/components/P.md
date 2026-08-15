# P — Ficha operacional candidata

```text
COMPONENT = P
DECISION_STATUS = PENDING_HUMAN_REVIEW
```

| Campo | Propuesta para revisión humana |
|---|---|
| `NOMINAL_DEFINITION` | Pensamiento, definición o interpretación: forma atribuible en que el sujeto organiza significado, expectativa, creencia, regla o lectura de la experiencia. |
| `OBSERVABLE_POSITIVE_CRITERIA` | Una proposición atribuible al sujeto establece o adopta un significado, creencia, expectativa, definición o regla de lectura que organiza el fragmento. La evidencia implícita requiere contenido semántico recuperable, no sólo una palabra cognitiva. |
| `OBSERVABLE_NEGATIVE_CRITERIA` | No bastan una cita no adoptada, una descripción factual sin función interpretativa demostrada, vocabulario como “pensar” referido a terceros, ni una afirmación exclusiva de importancia V. |
| `ABSENT_CRITERIA` | Evidencia explícita y atribuible de que el sujeto suspende, rechaza o no formula una interpretación dentro del alcance declarado, sin evidencia positiva contradictoria. El silencio produce `UNKNOWN`. |
| `AMBIGUOUS_CRITERIA` | La misma evidencia puede funcionar plausiblemente como interpretación P o criterio de importancia V, o existen dos interpretaciones incompatibles atribuibles al sujeto. |
| `UNKNOWN_CRITERIA` | Falta contenido interpretativo recuperable, referente, atribución o alcance; sólo se observa conducta o contexto. |
| `SUBJECT_ATTRIBUTION_RULES` | La interpretación debe pertenecer al sujeto objetivo y a la ventana actual; una creencia pasada cuenta para cambio sólo con comparación explícita. |
| `THIRD_PARTY_EXCLUSION_RULES` | Excluir opiniones de terceros, citas rechazadas, reglas culturales mencionadas sin adopción y explicaciones del narrador no atribuidas al sujeto. |
| `PRESENCE_RULES` | Marcar `PRESENT` sólo si la evidencia muestra una lectura o estructura de significado operante, no por asumir que toda experiencia implica pensamiento. |
| `STABILITY_RULES` | Requiere la misma interpretación o regla en dos momentos comparables. Repetición léxica sola no basta. |
| `CHANGE_RULES` | Requiere sustitución, revisión, abandono o reorganización explícita de la interpretación atribuible al mismo sujeto y objeto. |
| `BOUNDARY_CASES` | Evaluación descriptiva frente a importancia; expectativa frente a intención; cita frente a adopción; hecho narrado frente a significado activo. |
| `NEGATIVE_NEIGHBORS` | V por importancia; Act por intención/plan; discurso de terceros; mera descripción factual. |
| `COUNTEREXAMPLES` | Una prioridad sin interpretación no prueba P. Una conducta compatible con una creencia no prueba esa creencia. Una palabra cognitiva en una cita no prueba P del sujeto. |

## Preguntas de decisión humana

1. ¿“Suspender interpretación” puede sostener `ABSENT`, o debe permanecer siempre `UNKNOWN`?
2. ¿Qué contenido mínimo vuelve recuperable una interpretación implícita?
3. ¿Puede una misma proposición marcar P y V cuando se justifican funciones diferentes?
