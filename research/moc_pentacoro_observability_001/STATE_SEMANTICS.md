# Semántica candidata de estados

```text
ARTIFACT_STATUS = CANDIDATE_FOR_HUMAN_DECISION
```

## Capa observada

Los estados describen qué autoriza a concluir el fragmento respecto de un componente y un sujeto objetivo. No describen directamente el estado latente completo de la persona.

| Estado | Regla candidata |
|---|---|
| `PRESENT` | Existe evidencia pertinente, atribuible al sujeto y suficiente según al menos un criterio positivo aprobado; no queda una lectura vecina igualmente plausible sin resolver. |
| `ABSENT` | Existe evidencia pertinente y afirmativa de que el componente no opera dentro del alcance y ventana declarados. El mero silencio nunca basta. |
| `AMBIGUOUS` | Existe evidencia pertinente que sostiene dos o más lecturas incompatibles, incluida una frontera entre componentes, sin criterio textual para decidir. |
| `UNKNOWN` | Falta evidencia pertinente o no puede establecerse atribución, alcance, referente o ventana. No expresa ausencia. |

## Presencia y cambio

```text
presence_status != change_status
```

| Estado de cambio | Regla candidata |
|---|---|
| `STABLE` | El componente está `PRESENT` en al menos dos momentos o condiciones comparables y la evidencia sostiene continuidad sin transición atribuible. |
| `INCREASED` | Existe comparación explícita y atribuible que muestra mayor intensidad, peso o influencia según una escala aprobada para el componente. |
| `DECREASED` | Existe comparación explícita y atribuible que muestra menor intensidad, peso o influencia según una escala aprobada. |
| `CHANGED_OTHER` | Existe una transición cualitativa, emergencia, desaparición o reorganización que no es legítimo ordenar como aumento/disminución. |
| `AMBIGUOUS` | Hay evidencia de transición, pero dos cambios incompatibles siguen siendo plausibles. |
| `UNKNOWN` | No puede determinarse si hubo transición o faltan puntos comparables. |
| `NOT_APPLICABLE` | No se estableció presencia en una forma que permita preguntar por estabilidad o cambio. |

## Reglas de compatibilidad propuestas

1. `presence=ABSENT` exige normalmente `change=NOT_APPLICABLE`, salvo que el fragmento describa explícitamente una transición hacia ausencia; entonces se propone `CHANGED_OTHER`.
2. `presence=PRESENT` es compatible con `change=STABLE`.
3. Un solo momento sin comparación produce normalmente `change=UNKNOWN`, no `STABLE`.
4. Diferencias de vocabulario entre momentos no demuestran cambio del componente.
5. Cambio de conducta no demuestra cambio de `Act` sin evidencia atribuible del modo interno.
6. Cambio ambiental no demuestra cambio de `S` si no cambia su función experiencial.

Todas estas reglas requieren aprobación humana antes de integrarse a un manual.
