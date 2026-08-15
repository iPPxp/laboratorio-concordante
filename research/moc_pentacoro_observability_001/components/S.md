# S — Ficha operacional candidata

```text
COMPONENT = S
DECISION_STATUS = PENDING_HUMAN_REVIEW
```

| Campo | Propuesta para revisión humana |
|---|---|
| `NOMINAL_DEFINITION` | Situación encarnada o representación experiencial del entorno tal como opera en la experiencia. |
| `OBSERVABLE_POSITIVE_CRITERIA` | Evidencia atribuible de que cuerpo, tiempo, espacio, recurso, límite, soporte, entorno o posibilidad percibida modifica o estructura funcionalmente lo disponible en la experiencia. |
| `OBSERVABLE_NEGATIVE_CRITERIA` | No bastan menciones de lugar, hora, personas, objetos o cuerpo como escenografía; tampoco un afecto corporal Eaf sin función situacional demostrada. |
| `ABSENT_CRITERIA` | Evidencia explícita de que los detalles contextuales declarados no operan como condición, recurso, límite o posibilidad dentro del alcance. La falta de contexto produce `UNKNOWN`, no `ABSENT`. |
| `AMBIGUOUS_CRITERIA` | No puede decidirse si un detalle es incidental o funcional, o si una señal corporal pertenece a S, Eaf o ambos. |
| `UNKNOWN_CRITERIA` | No se informa la función experiencial del contexto, o falta atribución de cómo opera para el sujeto. |
| `SUBJECT_ATTRIBUTION_RULES` | La función situacional debe expresarse respecto de las posibilidades o experiencia del sujeto objetivo, no sólo como hecho externo. |
| `THIRD_PARTY_EXCLUSION_RULES` | Excluir recursos, límites o contextos de terceros cuando no estructuran la experiencia del sujeto; excluir decorado narrativo sin función. |
| `PRESENCE_RULES` | `PRESENT` requiere función experiencial; la mera existencia objetiva del entorno no basta. |
| `STABILITY_RULES` | Requiere continuidad funcional de la condición situacional en momentos comparables; el mismo lugar puede cambiar de función. |
| `CHANGE_RULES` | Requiere transición en recurso, límite, soporte, condición encarnada o posibilidad percibida; cambio escenográfico sin función no cuenta. |
| `BOUNDARY_CASES` | Contexto incidental/funcional; sensación corporal S/Eaf; posibilidad percibida P/S; apoyo externo funcional/decorativo. |
| `NEGATIVE_NEIGHBORS` | Escenografía, metadatos temporales, lugar incidental, objetos mencionados, afecto corporal sin función situacional. |
| `COUNTEREXAMPLES` | Nombrar una habitación no prueba S. Una fecha no prueba función temporal. Una condición corporal puede apoyar S sólo si estructura posibilidades o límites. |

## Campo especializado propuesto

```text
context_role =
  INCIDENTAL_CONTEXT |
  FUNCTIONAL_SITUATION |
  BOTH |
  NONE |
  AMBIGUOUS |
  UNKNOWN
```

Este campo describe la función de la evidencia contextual; no sustituye `presence_status` de S.
