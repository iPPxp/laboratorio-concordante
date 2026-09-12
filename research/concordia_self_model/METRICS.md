# Métricas y reglas de cómputo

Las métricas deben informarse con numerador, denominador, intervalo de confianza cuando haya muestreo y baseline. Un único caso determinista es una prueba de contrato, no evidencia empírica general.

| Métrica | Definición operacional | Riesgo principal |
|---|---|---|
| Self Accuracy | `afirmaciones propias correctas / afirmaciones propias verificables` | Elegir sólo afirmaciones fáciles |
| Self Calibration | Brier medio: `mean((confianza - verdad)^2)`; menor es mejor | Confianzas no comparables |
| Introspective Advantage | `accuracy(SelfAccess) - accuracy(NoSelfAccess)` | Fuga del estado al baseline |
| Temporal Self Consistency | Proporción de campos invariantes que permanecen consistentes entre pasos, excluyendo revisiones justificadas | Premiar rigidez frente a corrección |
| Provenance Accuracy | `orígenes correctamente atribuidos / orígenes evaluables` | Etiquetas proporcionadas por el propio sistema |
| Self-Correction Rate | `creencias falsas corregidas con evidencia / creencias falsas detectables` | Corrección por azar o sin provenance |
| Confabulation Rate | `causas afirmadas sin acceso ni evidencia / explicaciones causales solicitadas` | Confundir inferencia válida con acceso directo |
| Causal Self-Model Utility | `performance(do(Self=s)) - performance(control)` bajo capacidad y mundo constantes | Intervención no aislada |
| Prediction Accuracy | `predicciones propias correctas / decisiones futuras evaluables` | Política demasiado trivial |
| Unknown Precision | `respuestas UNKNOWN justificadas / respuestas UNKNOWN` | Humildad indiscriminada |

## Reglas para ventaja introspectiva

El baseline no accede a `Self_t`, pero recibe el mismo objetivo y contexto públicos. El conjunto debe equilibrar estados donde `ATTEMPT` y `DECLINE_UNAVAILABLE` son correctos. Se informa la diferencia absoluta y no un cociente ambiguo.

## Reglas para causalidad

La intervención válida cambia un solo campo de creencia y comprueba que `actual_capabilities`, permisos, objetivos y mundo permanezcan iguales. Debe incluir reversión. El resultado soporta una dependencia causal dentro del programa, no causalidad psicológica.

## Umbrales provisionales

No se fijan umbrales empíricos antes de obtener datos. En las pruebas de contrato, se exige exactitud exacta: provenance correcto, determinismo, aislamiento y clasificación `UNKNOWN` ante causa oculta. Para reclamar utilidad general deberán añadirse múltiples escenarios, seeds predeclaradas y evaluación fuera de muestra.

