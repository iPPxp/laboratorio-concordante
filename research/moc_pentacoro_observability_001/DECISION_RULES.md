# Árbol candidato de decisión

```text
ARTIFACT_STATUS = CANDIDATE_FOR_HUMAN_DECISION
```

Aplicar separadamente a cada componente:

1. **Alcance:** ¿están declarados sujeto y ventana relevante? Si no, `UNKNOWN`.
2. **Atribución:** ¿la evidencia pertenece al sujeto? Si no puede saberse, `UNKNOWN`; si pertenece a un tercero, excluirla.
3. **Pertinencia:** ¿la evidencia responde a la definición nominal del componente? Si no, continuar buscando; no declarar `ABSENT` por descarte.
4. **Vecino:** ¿una categoría vecina explica la evidencia igual o mejor? Si dos lecturas incompatibles siguen sostenidas, `AMBIGUOUS`.
5. **Positivo:** ¿se satisface un criterio positivo aprobado? Si sí, `PRESENT`.
6. **Ausencia afirmativa:** si no hay positivo, ¿existe evidencia aprobada de que el componente no opera en el alcance? Si sí, `ABSENT`; de lo contrario, `UNKNOWN`.
7. **Cambio:** sólo después de presence, comparar momentos/condiciones equivalentes. Sin comparación, no inferir estabilidad.
8. **Evidencia:** registrar spans literales, modo de evidencia, razón específica y confianza.

## Regla de prioridad

```text
attribution failure -> UNKNOWN
relevant incompatible readings -> AMBIGUOUS
positive sufficient evidence -> PRESENT
affirmative absence evidence -> ABSENT
mere silence -> UNKNOWN
```

## Veto de cuotas

No forzar distribución de estados ni presencia de los cinco componentes. La cobertura pertenece al diseño posterior; la anotación debe seguir la evidencia.
