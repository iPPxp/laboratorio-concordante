# F0.2 Semantic Calibration + Identifiability — Informe final

## Resultado ejecutivo

F0.2 se detuvo correctamente antes del piloto:

```text
PRE_G0_AUTHORITY_GATE = BLOCKED
SEMANTIC_DEFINITION_SUFFICIENT_COMPONENTS = 0/5

G0_MANUAL_CALIBRATION = NOT_RUN
G1_SEMANTIC_IDENTIFIABILITY = NOT_RUN
G2_DATASET_READINESS = NOT_RUN

MODEL_TRAINING_EXECUTED = NO
MOC_FACTORIZATION_VALIDATION = NOT_TESTED
CANONICAL_STATUS_CHANGE = NOT_AUTHORIZED
```

`NOT_RUN` es distinto de `FAILED`. No hubo piloto capaz de pasar o fallar: la condición de entrada a G0 no estaba satisfecha.

## Qué se demostró

La auditoría independiente localizó autoridad MOC primaria vigente y verificó que fija:

```text
Pi5_psi = <P_psi, Eaf_psi, Act_psi, V_psi, S_psi>
```

También encontró semántica nominal y límites negativos relevantes. Sin embargo, ninguna de las cinco definiciones contiene todavía el contrato narrativo necesario para decidir reproduciblemente presencia, ausencia, ambigüedad, desconocimiento, estabilidad o cambio.

| Componente | Semántica nominal disponible | Deuda bloqueante principal |
|---|---|---|
| P | pensamiento/definición/interpretación | frontera P/V, atribución y criterios observacionales |
| Eaf | emoción-afecto situado | implícito, señuelo léxico y fronteras con S/V |
| Act | acción/no acción o pauta interna/actual | modo interno frente a conducta, elección, impulso u omisión |
| V | dirección o criterio de importancia | preferencia, deseo y objetivo instrumental |
| S | situación encarnada/entorno experiencial | situación funcional frente a contexto incidental |

La conclusión permitida es:

```text
AUTHORIZED_MOC_NOMINAL_SEMANTICS_LOCATED = YES
AUTHORIZED_NARRATIVE_OPERATIONALIZATION_READY = NO
```

No se concluye que MOC sea falso, que los componentes no existan o que no puedan operacionalizarse. Se concluye que el validador no tiene autoridad para completar el significado faltante.

## Mapping neutral

El MappingCustodian selló antes de cualquier ejemplo el mapping exigido, con payload canónico RFC 8785, timestamp, nonce y SHA-256:

```text
STATE = SEALED_BEFORE_EXAMPLES
PAYLOAD_SHA256 = c962a76fafa7004a9e658ef79471d9e4edac713362281eae0f3c7d5610ab7028
MAPPING_CARDINALITY = 5_TO_5
MAPPING_DUPLICATES = 0
```

El PreG0GateEvaluator reprodujo el digest y la cardinalidad. Verificó consistencia interna y atestiguación de secuencia, no ceguera criptográfica ni el historial completo de accesos.

El mapping resuelve la deuda de preregistro encontrada en F0.1, pero no resuelve la identificabilidad semántica.

## Artefactos deliberadamente no producidos

No se produjeron:

- manual operacional utilizable;
- ejemplos piloto;
- textos narrativos;
- anotaciones A/B;
- ciclos de calibración;
- mundos, proyecciones u objetivos G1;
- métricas de acuerdo o identificabilidad;
- corpus G2;
- entrenamiento o evaluación de modelos.

`ANNOTATION_SCHEMA.json` conserva únicamente la forma estructural solicitada. `ANNOTATION_MANUAL.md` es un testigo de no emisión y no autoriza anotación. `NEGATIVE_NEIGHBORS.md` registra las fronteras pendientes sin inventar la diferencia decisiva.

## Por qué detenerse es el resultado correcto

Si un ManualAuthor completara ahora las reglas positivas, el posterior acuerdo entre anotadores mediría adhesión a una convención creada por el experimento. No demostraría identificación de los componentes definidos por MOC.

Formalmente, el problema no es todavía:

```text
Can annotators apply f_MOC(text)?
```

sino que falta definir, bajo autoridad MOC:

```text
f_MOC : narrative evidence -> component observation status
```

La infraestructura puede validar una función una vez declarada; no puede elegir legítimamente esa función.

## Condición de reanudación

La continuación requiere un paquete semántico emitido o aprobado por autoridad MOC que cierre, para los cinco componentes:

1. condiciones observacionales positivas y negativas;
2. vecinos semánticos y frontera decisiva;
3. evidencia explícita, implícita, contrastiva y negativa;
4. atribución al sujeto frente a terceros o citas;
5. `PRESENT`, `ABSENT`, `AMBIGUOUS` y `UNKNOWN`;
6. presencia separada de cambio, incluyendo `STABLE` y `NOT_APPLICABLE`;
7. deudas de notación y fronteras específicas consignadas en `AUTHORITY_BASELINE.md`.

Ese paquete deberá recibir una decisión de autoridad separada. Después podrá abrirse un nuevo intento G0 con piloto desechable. No existe reanudación automática ni autorización para G1/G2.

## Estados finales obligatorios

```text
G0_MANUAL_CALIBRATION = NOT_RUN
G1_SEMANTIC_IDENTIFIABILITY = NOT_RUN
G2_DATASET_READINESS = NOT_RUN
MODEL_TRAINING_EXECUTED = NO
MOC_FACTORIZATION_VALIDATION = NOT_TESTED
CANONICAL_STATUS_CHANGE = NOT_AUTHORIZED
```

F0 y F0.1 permanecen fuera del alcance de escritura. No se realizó incorporación Git, canonización ni activación.
