# MOC-EXTRACTOR-001-H3 — Contrato candidato

## Estado

`CANDIDATE_NOT_INCORPORATED`.

## Frontera externa

`FrictionCandidateInput` es el único DTO de fricción aceptado dentro de una extracción. Su configuración es cerrada (`extra=forbid`) y sólo admite:

- `type`;
- `claim_refs`;
- `annotation_rule`;
- `description`;
- `verification_status=FRICTION_CANDIDATE`.

Se rechazan `verified`, estados mecánicos, `proof`, `predicate_result`, `structured_fact`, hashes de claims o colecciones aceptadas aportadas externamente.

`FactSourceReference` contiene sólo identidad de procedencia. No transporta dimensión, booleano ni resultado del predicado. El parámetro histórico `structured_facts` se conserva únicamente para reproducibilidad H2: sus valores semánticos se descartan y sólo se proyecta su referencia de procedencia.

## Recomputation

Una candidata sólo se promueve cuando:

1. la extracción y los claims son estructuralmente válidos;
2. la regla existe en el catálogo cerrado y coincide en tipo, cardinalidad, campos, procedencias y slots;
3. cada referencia de procedencia coincide con una identidad cerrada conocida;
4. H3 vuelve a derivar internamente los hechos desde `surface_value` mediante `FACT-BOOLEAN-STATE-ES-001`;
5. H3 evalúa internamente el predicado cerrado;
6. el resultado verdadero produce un proof interno nuevo.

El proof registra:

- `verification_rule_id`;
- `rule_version`;
- `catalog_sha256` y versión;
- `claim_refs` canónicas;
- `canonical_claims_sha256`;
- `structured_predicate` / `predicate_id`;
- `predicate_result=true`.

`FrictionMechanicalProof` y `MechanicallyVerifiedFriction` no forman parte del JSON Schema de entrada. Sus constructores y deserialización pública rechazan uso externo. `model_construct` no es una frontera de seguridad: cualquier objeto así creado sigue sin poder entrar en el DTO de extracción ni sustituir la recomputación pública.

## Migración C

Antes de copiar, contar o iterar `cases`, H3 exige:

```python
if type(cases) is not list:
    raise MigrationError("MIGRATION_CASES_INVALID")
```

Después exige `1 <= len(cases) <= 12`. Tuplas, generadores, iterables personalizados y subclases de `list` se rechazan. El mismo objeto built-in contado es el único objeto migrado. La entrada proyectada aplica la misma frontera.

## Delta deliberado de compatibilidad

La suite fresca H2 se conserva byte a byte. Cuatro expected dejan de representar el contrato H3:

1. una subclase honesta de `list` ya no es válida;
2. dos pruebas intentan construir directamente un proof y fallan antes de su aserción posterior;
3. cambiar valores semánticos de `structured_facts` ya no altera el resultado porque H3 los descarta y recalcula desde claims.

No se modifican esas pruebas. H3 registra el delta y aporta controles propios equivalentes.
