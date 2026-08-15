# F0.2 — Manual de anotación no emitido

```text
MANUAL_STATUS = NOT_ISSUED
MANUAL_VERSION = NONE
ANNOTATION_AUTHORIZED = NO
BLOCKER = SEMANTIC_DEFINITION_INSUFFICIENT_5_OF_5
```

El esquema estructural de F0.2 puede separar `presence_status`, `change_status`, evidencia y confianza, pero las fuentes MOC vigentes no fijan todavía las condiciones observacionales necesarias para asignar esos estados a `P`, `Eaf`, `Act`, `V` y `S`.

Publicar reglas positivas en este punto transferiría autoridad semántica al validador. Eso está prohibido por:

```text
SEMANTIC_AUTHORITY = MOC
COMPUTATIONAL_AUTHORITY = VALIDATION_ONLY
```

Por tanto, este archivo es un testigo explícito de no emisión. No debe utilizarse para anotar, calibrar, generar ejemplos ni entrenar modelos.

Una futura versión `1.0.0` requerirá una fuente MOC autorizada que cierre todas las deudas listadas en `SEMANTIC_DEFINITIONS.md` y `AUTHORITY_BASELINE.md`.
