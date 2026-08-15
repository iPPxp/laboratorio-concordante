# Eaf — Ficha operacional candidata

```text
COMPONENT = EAF
DECISION_STATUS = PENDING_HUMAN_REVIEW
```

| Campo | Propuesta para revisión humana |
|---|---|
| `NOMINAL_DEFINITION` | Emoción-afecto situado: respuesta afectiva atribuible al sujeto dentro de una situación experiencial. |
| `OBSERVABLE_POSITIVE_CRITERIA` | Evidencia explícita de sentir afectivo atribuible al sujeto, o evidencia implícita de una cualidad afectiva situada cuya función no se reduce a condición corporal S, criterio V o modo Act. |
| `OBSERVABLE_NEGATIVE_CRITERIA` | No bastan términos emocionales en citas o metáforas, afectos de terceros, activación corporal sin cualidad afectiva, evaluación de importancia ni intensidad conductual. |
| `ABSENT_CRITERIA` | Evidencia explícita y situada de ausencia de respuesta afectiva dentro de la ventana, sin señal positiva incompatible. No mencionar emoción produce `UNKNOWN`. |
| `AMBIGUOUS_CRITERIA` | Una señal corporal puede ser afecto Eaf o condición S; una expresión de valencia puede ser sentir Eaf o criterio V; dos afectos incompatibles permanecen plausibles. |
| `UNKNOWN_CRITERIA` | Sólo existe vocabulario afectivo sin atribución/función, o falta evidencia de cualidad afectiva. |
| `SUBJECT_ATTRIBUTION_RULES` | El afecto debe atribuirse al sujeto objetivo; la percepción del afecto ajeno no se transfiere al sujeto. |
| `THIRD_PARTY_EXCLUSION_RULES` | Excluir emociones de otras personas, etiquetas del narrador no ancladas, citas no adoptadas y léxico emocional usado como descripción ambiental. |
| `PRESENCE_RULES` | `PRESENT` exige respuesta afectiva, no mera palabra emocional. La evidencia implícita debe satisfacer una regla humana específica aún por aprobar. |
| `STABILITY_RULES` | Requiere continuidad de la respuesta afectiva en momentos comparables; una disposición general no se presume estable en el fragmento. |
| `CHANGE_RULES` | Requiere transición atribuible en cualidad, intensidad o organización afectiva; cambio de situación no implica por sí solo cambio Eaf. |
| `BOUNDARY_CASES` | Sensación corporal; valencia evaluativa; disposición para actuar; palabra emocional sin sentir; afecto de terceros. |
| `NEGATIVE_NEIGHBORS` | S corporal/ambiental, V de importancia, Act como activación operativa, señuelo léxico afectivo. |
| `COUNTEREXAMPLES` | Una limitación corporal sin cualidad afectiva no prueba Eaf. Decir que algo importa no prueba afecto. Nombrar una emoción ajena no prueba Eaf del sujeto. |

## Cuadrante obligatorio para revisión posterior

| | Vocabulario afectivo presente | Vocabulario afectivo ausente |
|---|---|---|
| Eaf presente | positivo explícito candidato | positivo implícito candidato |
| Eaf ausente | señuelo léxico candidato | ausencia afirmativa candidata |

No generar casos hasta que la autoridad humana apruebe qué evidencia satisface cada celda.
