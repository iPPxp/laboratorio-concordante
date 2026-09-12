# Informe del autor de outcomes F0.1

**Rol:** `F0_1_OUTCOME_AUTHOR_INDEPENDENT`  
**Fecha:** 2026-08-15  
**Estatus:** capa sintética genérica, no clínica, no canónica y sin entrenamiento.

## Declaración de acceso

Este rol leyó exclusivamente:

- `world/world_states.jsonl`
- `OUTCOME_SCHEMA.md`
- `PREREGISTRATION.md`
- `ROLE_MATRIX.md`

No leyó narrativas, datos crudos, anotaciones, adjudicaciones ni código de
modelos. El primer intento buscó el esquema dentro de `world/`, donde no
existía; se corrigió la ruta al `OUTCOME_SCHEMA.md` de la raíz sin abrir ningún
archivo adicional.

## Identidad de los insumos

| Insumo | SHA-256 |
|---|---|
| `world/world_states.jsonl` | `44b79f67f237a998b560aabcdb2ffc31d2abb12360cd3c70ffcba202f43a70a7` |
| `OUTCOME_SCHEMA.md` | `3f0b807ca4b5bcf738843bbdbf29f3f4b0bef34292d5622382c1738ce9ad924c` |
| `PREREGISTRATION.md` | `282034e97618d109a72ce2d59e94d3d2ae809c26174fb66640982c2a5facdbb1` |
| `ROLE_MATRIX.md` | `5229e3f63f018e3a813f8761218e929941e8ae5631e88bf5deb9bb505578a14c` |

Cada outcome conserva el digest del mundo sellado en `source_world_digest`.

## Derivación genérica

La unidad es una familia y existe un único caso por familia. Como el mundo
sellado no proporciona otro identificador de caso, `case_id` se iguala a
`family_id`. No se introducen identificadores provenientes de una capa
narrativa.

Las reglas conocidas se aplicaron de forma determinista sobre la firma
numérica sellada:

- conservación: mantiene la firma observada;
- amortiguación: lleva la firma a cero;
- cruce: aplica una rotación cíclica de una posición;
- amplificación: multiplica la firma por dos;
- futuro opaco: no imputa firma, conteo ni cambio de posibilidades.

`change_signature_hash` es SHA-256 de la representación UTF-8 compacta de la
firma resultante, por ejemplo `[0,0,0,0,0]`. Sólo se publica el digest: no se
publican posiciones, nombres ni significados. En futuros opacos el campo queda
en `null`.

`next_state_class` distingue cero, uno, varios o un número desconocido de
cambios. `changed_slot_count` contiene el conteo únicamente cuando el futuro es
conocido. `stability_change` se deriva del mismo conteo.

Las listas de posibilidades usan identificadores opacos específicos de cada
caso. Cada identificador es un prefijo `q-` seguido de 16 caracteres del
SHA-256 de dirección, familia y firma. No constituyen un diccionario reutilizable
de posiciones. Una firma con entradas positivas agrega una posibilidad opaca;
una con entradas negativas retira una; si contiene ambas direcciones, el cambio
es mixto. Cero produce `UNCHANGED`; un futuro opaco conserva `UNKNOWN` con
listas vacías.

Las clases de intervención disponibles se remapearon a `CLASS_A`, `CLASS_B` y
`CLASS_C`; la no disponibilidad se representa con `NONE`. El efecto operacional
se codificó así:

- conservación: `NULL`;
- amortiguación: `NEGATIVE`;
- amplificación: `POSITIVE`;
- cruce: `UNKNOWN`, porque no tiene dirección escalar;
- futuro opaco: `UNKNOWN`;
- intervención no disponible: `NOT_AVAILABLE`, con precedencia sobre la regla.

Estas etiquetas describen exclusivamente transformaciones del mundo sintético.
No afirman eficacia, causalidad ni beneficio humano.

## Resultado

```text
OUTCOMES = 60
UNIQUE_CASE_IDS = 60
UNIQUE_FAMILY_IDS = 60
TRAIN = 35
VALIDATION = 10
TEST = 15
NOT_AVAILABLE = 12
NOT_AVAILABLE_BY_SPLIT = 6 / 3 / 3
UNKNOWN_FUTURES = 3
UNKNOWN_FUTURES_BY_SPLIT = 1 / 1 / 1
```

Distribución de estados futuros:

| Clase | Casos |
|---|---:|
| `STABLE` | 26 |
| `SINGLE_CHANGE` | 20 |
| `MULTIPLE_CHANGE` | 11 |
| `UNKNOWN` | 3 |

Distribución del cambio de posibilidades:

| Clase | Casos |
|---|---:|
| `UNCHANGED` | 26 |
| `EXPANDED` | 25 |
| `CONTRACTED` | 3 |
| `MIXED` | 3 |
| `UNKNOWN` | 3 |

## Límites de divulgación

`outcomes.jsonl` contiene sólo las claves exigidas por el esquema. No incluye
labels MOC, bloques contrafactuales, celdas experimentales, nombres internos de
posiciones, significados de posiciones ni el codebook del generador. Los hashes
sirven para identidad y comparación; no demuestran independencia por sí solos.

## Digest de la capa

```text
outcomes/outcomes.jsonl =
5a429037a3ec83e6bebae4e33d3c574ed72e4b50090814676ca1f8274a56931c
```
