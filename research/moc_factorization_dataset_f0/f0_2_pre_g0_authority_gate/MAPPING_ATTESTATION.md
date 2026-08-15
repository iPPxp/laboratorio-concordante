# Atestiguación pública del mapping sellado

```text
PAYLOAD_INCLUDED = NO
EXACT_MAPPING_DISCLOSED = NO
MAPPING_CARDINALITY = 5_TO_5
UNIQUE_TARGETS = 5
SEALED_STATE = SEALED_BEFORE_EXAMPLES
SECRECY_GUARANTEE = PROCEDURAL_NOT_CRYPTOGRAPHIC
```

## Compromisos criptográficos

```text
CANONICALIZATION = RFC_8785_JSON_CANONICALIZATION_SCHEME_JCS
CANONICAL_PAYLOAD_BYTES = 604
PAYLOAD_SHA256 = c962a76fafa7004a9e658ef79471d9e4edac713362281eae0f3c7d5610ab7028
SEALED_FILE_SHA256 = 96e348200d2fbcfefbe7366d90f6b905b0f5e2cec60b1f738c4a675629361d11
PAYLOAD_DIGEST_MATCH = YES
MAPPING_DUPLICATES = 0
```

El evaluador independiente reprodujo bytes, digest y cardinalidad. Verificó consistencia interna y la presencia de una atestiguación de secuencia. No verificó independientemente todo el historial de acceso o generación.

El digest permite comprobar posteriormente la identidad del payload bajo custodia sin publicarlo ahora. El digest no revela por sí solo autoridad semántica, aprobación del manual ni autorización de G0.
