# Protocolo independiente de anotación MOC F0

## Cegamiento

El `MOC_ANNOTATOR` recibe sólo el archivo de entrada autorizado y este protocolo. No accede a `sealed_design/`, `outcomes/`, código de modelos, predicciones, métricas previas ni anotaciones ajenas antes de entregar su primera pasada.

Cada caso se anota independientemente. No se deduce una etiqueta por IDs, orden, partición o casos vecinos. La evidencia primaria es el contenido explícito del caso; toda etiqueta cita un campo/fragmento o se declara inferencia.

## Registro obligatorio

```text
case_id
annotation_id
field
value
status
evidence_span_or_field
reason
confidence
annotator_id
source_file
source_record_digest
timestamp
supersedes
contradicts
```

## Ausencia e incertidumbre

- `ABSENT`: el campo/relación está explícitamente negado o el alcance completo permite concluir que no aparece.
- `AMBIGUOUS`: dos o más valores son compatibles sin criterio textual para elegir.
- `UNKNOWN`: faltan datos para afirmar presencia, ausencia o una ambigüedad delimitada.

No usar `ABSENT` por defecto ni forzar una categoría cuando corresponde `UNKNOWN`.

## Componentes

### `P_psi`

Anotar interpretación sólo si hay una lectura, significado atribuido o modelo del evento. No reducir a tokens, percepción bruta o contenido literal sin interpretación.

### `Eaf_psi`

Anotar afecto únicamente según lo declarado. No inferirlo desde conducta, score, urgencia o estereotipos lingüísticos.

### `Act_psi`

```text
Act_psi != conducta
Act_psi != ACT_psi
```

Anotar el modo de respuesta experiencial declarado, que puede incluir acción, no acción o pauta interna. Una salida observable se registra separadamente como `conducta` y no prueba por sí sola `Act_psi`.

### `V_psi`

```text
V_psi != reward
```

Anotar dirección, criterio u orientación declarada. Score, utilidad o recompensa son señales separadas, no equivalencia semántica.

### `S_psi`

Separar:

- `S_REAL`: condición situacional externa declarada.
- `S_RELECTURA`: cambio interpretativo sin cambio externo demostrado.
- `S_INFORMATION`: información nueva o corregida sobre la situación.

No convertir relectura en cambio del mundo. Si no se distingue, usar `AMBIGUOUS`; si faltan datos, `UNKNOWN`.

## Relaciones

Cada relación registra:

```text
source_component
target_component
relation_type
direction
polarity_or_sign_if_declared
status
evidence
confidence
```

Reglas:

1. Coaparición no implica relación.
2. Relación no implica causalidad.
3. No asumir dirección, simetría, peso o signo.
4. No completar automáticamente todas las parejas.
5. No reducir una relación superior a pares sin evidencia.
6. Anotar por separado cambios marginales y relacionales.
7. Una relación inferida usa `ANNOTATOR_INFERENCE`, no `OBSERVED_IN_PROVIDED_TEXT`.

## Secuencia

1. Verificar ID, digest y alcance F0.
2. Leer el caso completo una vez sin etiquetar.
3. Extraer evidencia explícita por componente.
4. Anotar `P`, `Eaf`, `Act`, `V` y las tres capas de `S`.
5. Registrar conducta separada si aparece.
6. Anotar relaciones y estatus.
7. Revisar transformaciones sin inferir causalidad.
8. Aplicar `ABSENT`, `AMBIGUOUS` o `UNKNOWN`.
9. Registrar provenance y confianza.
10. Ejecutar vetos antes de congelar.

## Confianza

- `HIGH`: declaración explícita no contradictoria.
- `MEDIUM`: inferencia estrecha con evidencia identificable.
- `LOW`: lectura posible pero incompleta; revisar `AMBIGUOUS/UNKNOWN`.

La confianza mide claridad de evidencia, no probabilidad de que MOC sea verdadero.

## Desacuerdo

No negociar antes de la primera pasada independiente. Después se calcula acuerdo por campo. La adjudicación conserva ambas anotaciones, registra adjudicador y crea un claim nuevo con `supersedes`; nunca borra el desacuerdo.

## Vetos finales

```text
NO_ACCESS_TO_SEALED_DESIGN = REQUIRED
NO_ACCESS_TO_OUTCOMES = REQUIRED
NO_MODEL_CODE_OR_PREDICTIONS = REQUIRED
Act_EQUALS_CONDUCT = FORBIDDEN
Act_EQUALS_ACT_UPPERCASE = FORBIDDEN
V_EQUALS_REWARD = FORBIDDEN
S_REINTERPRETATION_EQUALS_WORLD_CHANGE = FORBIDDEN
UNSUPPORTED_RELATION_COMPLETION = FORBIDDEN
HUMAN_OR_CLINICAL_CLAIM = FORBIDDEN
```
