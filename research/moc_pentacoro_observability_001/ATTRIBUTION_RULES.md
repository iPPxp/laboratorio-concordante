# Reglas candidatas de atribución

```text
ARTIFACT_STATUS = CANDIDATE_FOR_HUMAN_DECISION
TARGET = SUBJECT_ATTRIBUTION_AND_THIRD_PARTY_EXCLUSION
```

## Regla base

Una evidencia sólo puede clasificar un componente si el fragmento permite atribuirla al sujeto objetivo dentro de la ventana declarada.

## Evidencia admisible propuesta

1. expresión en primera persona del sujeto;
2. discurso indirecto inequívocamente atribuido al sujeto;
3. narración sintética en tercera persona que afirma explícitamente el estado del sujeto, si el protocolo declara esa voz como informativa;
4. cita previa adoptada explícitamente por el sujeto como posición o estado propio actual;
5. contraste temporal cuyo referente se mantiene estable.

## Exclusiones propuestas

No atribuir automáticamente al sujeto:

- palabras o estados de otra persona;
- citas que el sujeto sólo repite, cuestiona o rechaza;
- descripciones del narrador sin referente claro;
- detalles ambientales incidentales;
- conducta observada sin vínculo explícito con el modo experiencial;
- metáforas cuyo sentido pertinente no esté establecido;
- términos afectivos, valorativos o de acción usados como nombres, etiquetas o ejemplos.

## Ambigüedad frente a desconocimiento

- Si dos referentes concretos son plausibles y producen clasificaciones distintas: `AMBIGUOUS`.
- Si no existe información suficiente para resolver a quién pertenece la evidencia: `UNKNOWN`.
- Si la evidencia pertenece claramente a un tercero: excluirla para el sujeto; evaluar `ABSENT` sólo si existe además evidencia afirmativa de ausencia en el sujeto.

## Spans compartidos

El mismo span puede apoyar dos componentes únicamente cuando cada registro declara una razón diferente y la frontera correspondiente permanece resuelta. Copiar la misma justificación entre componentes invalida la atribución instrumental.
