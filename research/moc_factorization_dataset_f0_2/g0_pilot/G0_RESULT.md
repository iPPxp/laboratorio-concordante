# F0.2 — Resultado del gate previo a G0

```text
EVALUATOR_ROLE = PreG0GateEvaluator
SEMANTIC_AUTHORITY = MOC
COMPUTATIONAL_AUTHORITY = VALIDATION_ONLY

SEMANTIC_DEFINITION_SUFFICIENT_COMPONENTS = 0/5
SEMANTIC_DEFINITION_INSUFFICIENT_COMPONENTS = 5/5

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

## Dictamen

G0 no está autorizado. La baseline de autoridad concluye que ninguna de las
cinco definiciones MOC contiene todavía criterios observacionales suficientes
para producir un manual narrativo reproducible sin añadir decisiones semánticas
nuevas.

Por tanto, el piloto de calibración no se ejecutó. `NOT_RUN` no significa
`FAILED`: no hubo manual, ejemplos, anotaciones, ciclos de revisión ni resultado
empírico que pudiera pasar o fallar G0.

## Suficiencia semántica por componente

| Componente | Dictamen previo a G0 | Insuficiencia bloqueante resumida |
|---|---|---|
| `P` | `SEMANTIC_DEFINITION_INSUFFICIENT` | No hay criterios narrativos autorizados ni frontera operacional cerrada frente a `V`; tampoco reglas separadas de presencia y cambio. |
| `Eaf` | `SEMANTIC_DEFINITION_INSUFFICIENT` | No se resuelven observabilidad implícita, señuelos léxicos, atribución ni fronteras con disposición, `S` y `V`. |
| `Act` | `SEMANTIC_DEFINITION_INSUFFICIENT` | No se fijan criterios para ensayo, disponibilidad, impulso, inhibición u omisión, ni se cierra `Act` frente a conducta y elección. |
| `V` | `SEMANTIC_DEFINITION_INSUFFICIENT` | No existe umbral autorizado entre dirección o importancia y preferencia, deseo, gusto u objetivo instrumental. |
| `S` | `SEMANTIC_DEFINITION_INSUFFICIENT` | No hay umbral observacional para separar situación funcional de contexto meramente narrado o incidental. |

El recuento es, en consecuencia:

```text
SUFFICIENT = 0
INSUFFICIENT = 5
TOTAL = 5
```

## Verificación del mapping sellado

El manifest declara un mapping neutral uno-a-uno entre cinco identificadores
`U_i` y los cinco componentes, con estado `SEALED_BEFORE_EXAMPLES` y mutabilidad
`IMMUTABLE_FOR_F0.2`.

La verificación del payload canónico pasó:

```text
CANONICALIZATION_SCHEME = RFC_8785_JSON_CANONICALIZATION_SCHEME_JCS
DECLARED_CANONICAL_PAYLOAD_BYTES = 604
COMPUTED_CANONICAL_PAYLOAD_BYTES = 604
CANONICAL_PAYLOAD_STRING_MATCH = YES
DECLARED_PAYLOAD_SHA256 = c962a76fafa7004a9e658ef79471d9e4edac713362281eae0f3c7d5610ab7028
COMPUTED_PAYLOAD_SHA256 = c962a76fafa7004a9e658ef79471d9e4edac713362281eae0f3c7d5610ab7028
PAYLOAD_DIGEST_MATCH = YES
MAPPING_CARDINALITY = 5_TO_5
MAPPING_DUPLICATES = 0
```

El timestamp sellado es `2026-08-15T21:42:41.925Z`. El manifest declara:

```text
MAPPING_STATE = SEALED_BEFORE_EXAMPLES
EXAMPLES_GENERATED_BY_CUSTODIAN = FALSE
MAPPING_RECONSTRUCTED_RETROSPECTIVELY = FALSE
```

Con los inputs permitidos, esto verifica la consistencia interna del sello y la
presencia de una atestación de secuencia. No demuestra de forma independiente
que ningún otro rol hubiera generado ejemplos antes del sello, porque no se
consultaron ejemplos, bitácoras de generación ni artefactos de freeze. Por ello:

```text
MAPPING_BEFORE_EXAMPLES_ATTESTATION = PRESENT_AND_INTERNALLY_CONSISTENT
MAPPING_BEFORE_EXAMPLES_INDEPENDENT_VERIFICATION = NOT_AVAILABLE_WITHIN_ALLOWED_INPUTS
SECRECY_GUARANTEE = PROCEDURAL_NOT_CRYPTOGRAPHIC
```

Esta limitación no cambia el gate: incluso un mapping íntegro y oportunamente
sellado no puede suplir las cinco definiciones semánticas insuficientes.

## Inputs y digests

| Input autorizado | Bytes | SHA-256 |
|---|---:|---|
| Mandato F0.2 `pasted-text.txt` | 13834 | `f51ac2ed373144597f585a1d5a04bf6e09cec445f6daaa13532ff92fee6a6093` |
| `AUTHORITY_BASELINE.md` | 16693 | `1cfefd9905481070a32165e682c47a3f80c066eb4e8b3566076a2e990129e1c8` |
| `SEALED_MAPPING_MANIFEST.json` | 3515 | `96e348200d2fbcfefbe7366d90f6b905b0f5e2cec60b1f738c4a675629361d11` |

No se generaron manuales ni ejemplos, no se evaluó ningún piloto, no se
abrieron G1 o G2, no se entrenaron modelos y no se ejecutó Git.

