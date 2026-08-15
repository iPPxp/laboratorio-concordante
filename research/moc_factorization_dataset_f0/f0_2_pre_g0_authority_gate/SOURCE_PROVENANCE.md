# Procedencia y transformación de publicación

## Fuente

```text
SOURCE_WORKING_SET = research/moc_factorization_dataset_f0_2/
SOURCE_RESULT = PRE_G0_BLOCKED
SOURCE_MANIFEST_ENTRIES = 15
SOURCE_MANIFEST_HASH_ERRORS = 0
SOURCE_MANIFEST_SET_ERRORS = 0
```

## Regla de incorporación

Los quince registros lógicos del conjunto fuente se preservan de esta forma:

- doce documentos no sellados se incorporan como documentos del expediente;
- `INTEGRITY.json` se recalcula sobre el conjunto público;
- el payload sellado se sustituye públicamente por `MAPPING_ATTESTATION.md`;
- su manifest de custodia se sustituye públicamente por `MAPPING_CUSTODY_RECORD.md`.

Se añaden `README.md`, `STATUS.md`, este registro y un manifest público como envoltura de incorporación. La transformación evita revelar el mapping exacto y no altera el resultado científico.

## Sanitización

`CLAIMS.jsonl` elimina la correspondencia exacta entre identificadores neutrales y componentes, conservando únicamente cardinalidad, biectividad, secuencia y digest. Ninguna otra copia del payload sellado se incorpora en este directorio.

```text
SCIENTIFIC_RESULT_CHANGED = NO
SEALED_PAYLOAD_DISCLOSED = NO
AUTHORITY_INCREASED = NO
ACTIVATION_CHANGED = NO
```
