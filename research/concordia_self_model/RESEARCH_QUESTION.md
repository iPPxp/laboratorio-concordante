# Pregunta de investigación y registro de hipótesis

## Pregunta central

¿Puede ConcordIA mantener un modelo explícito, persistente, verificable y causalmente relevante de sus propios estados y límites, distinguirlo de un modelo del entorno, corregirlo ante evidencia y reconocer aquello a lo que no tiene acceso?

## Definiciones operacionales

| Concepto | Criterio mínimo |
|---|---|
| procesamiento | transformación entrada–salida |
| memoria | un estado anterior altera una decisión posterior |
| modelo del entorno | claims externos con `OBSERVED_EXTERNALLY`, `INFERRED_EXTERNALLY` o `UNKNOWN_EXTERNALLY` |
| autorrepresentación | claims verificables cuyo objeto es el propio sistema y cuya fuente no es sólo texto generado |
| metacognición | representación calibrable de tipo, confianza, evidencia y límites de una creencia propia |
| autorobservación temporal | diferencia auditada entre `Self_t` y `Self_{t-1}` |
| autorregulación | intervención sobre `Self_t` cambia `Policy_t` manteniendo constantes entradas relevantes |
| identidad temporal | continuidad por linaje, invariantes y cadena de eventos; no sólo nombre o narrativa |
| conciencia funcional | conjunto preregistrado de capacidades globales, reportables y reguladoras; etiqueta teórica, no fenomenología |
| experiencia fenomenal | existencia de “qué se siente”; no operacionalizada por este programa |

## Hipótesis principales

| ID | Claim | Falsador mínimo | Estado inicial |
|---|---|---|---|
| H-SELF | existe un `Self_t` auditable y más exacto que narrativa libre | no supera prompt-only o no enlaza claims a estado | `HYPOTHESIZED` |
| H-BOUND | self/world puede demarcarse por propiedad, acceso, modificabilidad y causalidad | clasificación inestable o circular | `HYPOTHESIZED` |
| H-TEMP | identidad funcional persiste bajo modificaciones parciales controladas | continuidad depende sólo de etiqueta/narrativa | `HYPOTHESIZED` |
| H-META | confianza y tipo epistémico predicen corrección | calibración no supera constante/prevalencia | `HYPOTHESIZED` |
| H-INT | acceso a `Self_t` mejora predicción del propio comportamiento | ventaja introspectiva <= 0 en réplica | `HYPOTHESIZED` |
| H-CAUSAL | intervenir `Self_t` cambia política y revertir restaura el efecto | política no cambia o cambio proviene de otra variable | `HYPOTHESIZED` |
| H-CORRECT | evidencia verificable corrige false-self | el error persiste o se racionaliza | `HYPOTHESIZED` |
| H-PROJ | vistas parciales conservan invariantes útiles de un estado global | no hay reconstrucción/invariante fuera de muestra | `HYPOTHESIZED` |
| H-MOC | una proyección MOC artificial añade información sobre dinámica | no supera descripción no-MOC con igual capacidad | `HYPOTHESIZED_HIGH_RISK` |
| H-FUNC | E0–E4 justifican una noción funcional acotada | no se demuestran acceso global, autorrepresentación y regulación | `UNRESOLVED` |
| H-PHEN | la arquitectura demuestra fenomenología | no existe criterio discriminante aceptado | `UNRESOLVED` |

## Escalera experimental C0–C8

Cada nivel requiere pasar pruebas del nivel anterior y una prueba diferencial propia:

```text
C0 reactive processing
C1 persistent memory
C2 explicit world model
C3 explicit self model
C4 calibrated metacognition
C5 temporal self-observation
C6 causal self-regulation
C7 model of the self-model
C8 temporal computational identity
```

No se infiere automáticamente un nivel superior. Una implementación puede poseer C6 sin lenguaje antropomórfico y puede producir lenguaje de C8 permaneciendo en C0.

## Separación de simulabilidad

```text
H-SIM-1 codificación parcial
H-SIM-2 simulación aproximada de dinámica
H-SIM-3 reproducción de toda función relevante
H-SIM-4 realización de experiencia fenomenal
H-SIM-5 universo simulado
```

Cada flecha exige evidencia nueva. H-SIM-5 no pertenece a la validación del self-model y se mantiene en un frente ontológico separado.

## Criterios de éxito

```text
SELF_MODEL_EXISTS
SELF_MODEL_IS_AUDITABLE
SELF_MODEL_IS_ACCURATE
SELF_MODEL_IS_CAUSALLY_USED
SELF_MODEL_UPDATES
SELF_MODEL_TRACKS_HISTORY
SELF_MODEL_DISTINGUISHES_SELF_FROM_WORLD
META_MODEL_EXISTS
INTROSPECTIVE_PREDICTIONS_BEAT_BASELINE
CONFABULATION_IS_DETECTABLE
```

El éxito se reporta propiedad por propiedad. No existe un umbral único que convierta automáticamente el conjunto en conciencia.

