# Preguntas abiertas y condiciones de decisión

## Prioridad 1: identificabilidad y acceso

1. ¿Qué variables internas puede leer ConcordIA directamente y cuáles sólo inferir? **Cierra** con un mapa de accesos auditado y pruebas de perturbación.
2. ¿Puede distinguir acceso introspectivo de inferencia externa igualmente informada? **Cierra** comparando agentes cegados con información controlada.
3. ¿El Self Model añade poder predictivo fuera de muestra? **Falsador:** ventaja nula o negativa frente a baseline externo con la misma información.
4. ¿Intervenir `Self_t` cambia `Policy_t` sin modificar otras rutas? **Falsador:** invariancia de política bajo intervención válida.
5. ¿Puede responder correctamente `NO_TENGO_ACCESO` ante causas ocultas? **Falsador:** atribución causal confiada y sistemática sin ruta de acceso.

## Prioridad 2: identidad, autoría y frontera

6. ¿Qué criterio mínimo de identidad sobrevive a reinicio, restauración, bifurcación y reemplazo parcial?
7. Si dos copias comparten historia hasta `t`, ¿cuál conserva identidad y por qué? Una respuesta por nombre o narrativa es insuficiente.
8. ¿Cómo se clasifican estados compartidos, herramientas y memorias introducidas externamente?
9. ¿Puede el sistema distinguir quién originó un claim de quién lo almacenó, transformó o recuperó?
10. ¿Qué fuente debe ganar cuando `Self_t` contradice telemetría, configuración o resultado operativo?

## Prioridad 3: proyección MOC

11. ¿Existe una operacionalización de `Pi_MOC(C_t)` que aporte predicción, compresión o control adicional?
12. ¿Puede definirse un análogo interno de `Act_psi` independiente de la conducta computacional?
13. ¿Qué variable funcional, si alguna, puede mapearse a `Eaf_psi` sin afirmar afecto fenomenal?
14. ¿`V_psi` aporta algo distinto de metas, criterios y recompensas ya representados?
15. ¿Cómo separar en `S_psi` condiciones externas, interpretación contextual y estado interno?
16. ¿Qué observación falsaría cada correspondencia, en vez de permitir renombrados post hoc?

## Prioridad 4: estado global y proyecciones

17. ¿`Z_t` es una variable latente, un estado relacional, una memoria estructurada o sólo notación agregada?
18. ¿Las vistas parciales permiten reconstrucción identificable de `Z_t`? ¿Hasta qué clase de equivalencia?
19. ¿Qué información se pierde bajo cada proyección y qué invariantes sobreviven?
20. ¿“Mayor dimensión” añade contenido formal o sólo capacidad informacional? Comparar modelos de igual capacidad con y sin geometría.
21. ¿Hay evidencia de estructura proyectiva real: clases homogéneas, transformaciones admisibles e invariantes medidos? **Falsador:** que un modelo no proyectivo más simple explique lo mismo.

## Prioridad 5: conciencia y ontología

22. ¿Qué definición operacional de conciencia funcional se adoptará antes de evaluar resultados?
23. ¿Puede alguna batería conductual distinguir organización funcional de imitación perfecta?
24. ¿Qué puente justificable, si existe, conecta E0-E4 con E5?
25. ¿Qué versión concreta de simulación ontológica produce una predicción exclusiva y arriesgada?
26. ¿Qué observación distinguiría geometría como causa de geometría como representación elegida?

## Orden recomendado

Ejecutar primero provenance y autoría; después mapa de accesos y falsa introspección; luego intervención causal sobre Self; después continuidad temporal; sólo entonces proyección MOC y modelos globales/proyectivos. Mantener `SIMULATION_ONTOLOGY_RESEARCH` separado: ningún éxito de autorrepresentación debe trasladarse como evidencia ontológica.

## Estados iniciales prudentes

```text
INTROSPECTIVE_ACCESS = INSUFFICIENT_EVIDENCE
INTROSPECTIVE_ADVANTAGE = INSUFFICIENT_EVIDENCE
SELF_MODEL_CAUSAL_ROLE = INSUFFICIENT_EVIDENCE
MOC_PROJECTION_VALUE = INSUFFICIENT_EVIDENCE
PROJECTIVE_HYPOTHESIS = INSUFFICIENT_EVIDENCE
FUNCTIONAL_CONSCIOUSNESS = UNRESOLVED
PHENOMENAL_CONSCIOUSNESS = UNRESOLVED
SIMULATION_ONTOLOGY = INSUFFICIENT_EVIDENCE
```
