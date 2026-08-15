# F0.2 — Informe de calibración no ejecutada

## Estado

```text
REPORT_SCOPE = PRE_G0_AUTHORIZATION_CHECK
G0_PILOT_CREATED = NO
G0_MANUAL_CREATED = NO
G0_EXAMPLES_CREATED = NO
G0_ANNOTATIONS_CREATED = NO
G0_CALIBRATION_CYCLES_EXECUTED = 0
G0_MANUAL_FROZEN = NO
G0_MANUAL_CALIBRATION = NOT_RUN
```

Este informe no reporta el fallo de un piloto. Documenta que la calibración no
se inició porque su prerrequisito semántico no está satisfecho.

## Condición de entrada a G0

El mandato prohíbe inventar definiciones y ordena detener la fase cuando la
autoridad MOC no permite distinguir operacionalmente algún componente. La
baseline autorizada registra insuficiencia para los cinco:

```text
P = SEMANTIC_DEFINITION_INSUFFICIENT
Eaf = SEMANTIC_DEFINITION_INSUFFICIENT
Act = SEMANTIC_DEFINITION_INSUFFICIENT
V = SEMANTIC_DEFINITION_INSUFFICIENT
S = SEMANTIC_DEFINITION_INSUFFICIENT
```

Las ausencias transversales incluyen criterios observacionales positivos,
fronteras con vecinos semánticos, tratamiento de evidencia explícita e
implícita, atribución al sujeto objetivo, reglas de `PRESENT`, `ABSENT`,
`AMBIGUOUS` y `UNKNOWN`, y separación entre presencia y cambio.

## Consecuencia metodológica

Sin esas decisiones de autoridad, un `ManualAuthor` tendría que introducir
significado nuevo. Hacerlo excedería `COMPUTATIONAL_AUTHORITY=VALIDATION_ONLY` y
contaminaría cualquier acuerdo posterior: dos anotadores podrían concordar con
una convención inventada sin haber identificado instrumentalmente los
componentes MOC autorizados.

Por esa razón no se produjeron ni evaluaron:

- definiciones operacionales nuevas;
- reglas positivas o negativas;
- negativos vecinos;
- ejemplos explícitos, implícitos, ambiguos, desconocidos o `DECOY`;
- anotaciones A/B;
- revisiones del manual;
- métricas de acuerdo o calibración.

## Estado de los gates

```text
G0_MANUAL_CALIBRATION_AUTHORIZED = NO
G0_MANUAL_CALIBRATION = NOT_RUN

G1_SEMANTIC_IDENTIFIABILITY_AUTHORIZED = NO
G1_SEMANTIC_IDENTIFIABILITY = NOT_RUN

G2_DATASET_READINESS_AUTHORIZED = NO
G2_DATASET_READINESS = NOT_RUN

MODEL_TRAINING_EXECUTED = NO
MOC_FACTORIZATION_VALIDATION = NOT_TESTED
CANONICAL_STATUS_CHANGE = NOT_AUTHORIZED
GIT_EXECUTED = NO
```

No se aplicará `FAILED` a G0 porque el piloto no fue ejecutado. G1 y G2 tampoco
pueden abrirse: el mandato exige gates sucesivos y G0 ni siquiera está
autorizado.

## Condición para reconsiderar G0

G0 sólo podrá reconsiderarse después de que autoridad semántica MOC explícita
cierre, para cada componente, los criterios y fronteras enumerados por la
baseline. Una validación computacional posterior podrá comprobar consistencia y
aplicabilidad; no puede redactar por sí misma el significado faltante.

El mapping sellado puede preservar independencia entre capas, pero no corrige
esta insuficiencia semántica y no autoriza por sí solo la calibración.

