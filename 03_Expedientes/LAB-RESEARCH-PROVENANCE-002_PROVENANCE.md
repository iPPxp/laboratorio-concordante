# LAB-RESEARCH-PROVENANCE-002 — Procedencia de la extensión 4D

DOCUMENT_STATUS=LOCAL_GIT_MATERIALIZATION_RECORDED
DATE=2026-09-12
DECISION_ID=D-2026-09-12-001

## Cadena de origen

```text
SOURCE_REPOSITORY=https://github.com/iPPxp/laboratorio-concordante.git
SOURCE_BRANCH=ipp/psi-heart-multinivel-20260912
SOURCE_COMMIT_1=679e898b66b28e4f72d1f7bd38bc5469e940ad7a
SOURCE_COMMIT_2=d65aab858df6bd0cc11609ec24a09b40eb8fec12
SOURCE_PATH=investigacion_empaquetamientos_esfericos_degenerantes/
SOURCE_CHAIN_ORDER=SOURCE_COMMIT_1_THEN_SOURCE_COMMIT_2
```

Los ocho commits exclusivos anteriores de la rama fuente no modifican
`SOURCE_PATH`. Por ello, la cadena cerrada mínima de esta extensión contiene
exactamente los dos commits indicados.

## Transferencia preparada

```text
TRANSFER_MODE=ORDERED_CHERRY_PICK_OF_TWO_CLOSED_COMMITS
TARGET_BASE=71a84f655ff4ec71a89640cca1f1b781fc523d79
TARGET_BRANCH=ipp/lab-4d-semantic-integration-20260912
TARGET_WORKTREE=C:\w\lab4d-0912
TARGET_COMMIT_1=4b59c3bd13d6bd8ae3d09a3c5f847fe1b3ef1b8e
TARGET_COMMIT_2=8b7ad0e02ca231a0f35ddd2ccff7c4d2d18ef2db
TARGET_TREE_AFTER_PAYLOAD=89efdef2a066c0e9432dd5ebcf15efa8f1f4fc29
CHERRY_PICK_CONFLICT_COUNT=0
PAYLOAD_DIRECTORY_DIFF=EMPTY
```

La transferencia afecta 37 rutas: 17 altas y 20 revisiones. El conjunto
cerrado está en `LAB-RESEARCH-PROVENANCE-002_PATHS.txt`; las huellas de los
bytes presentes después de ambos commits están en
`LAB-RESEARCH-PROVENANCE-002_SHA256SUMS.txt`.

```text
PATH_COUNT=37
HASH_COUNT=37
BYTE_MATCH_COUNT=37
BYTE_MISMATCH_COUNT=0
MANIFEST_TEXT_SERIALIZATION=UTF8_LF
MANIFEST_HASH_NORMALIZATION=UTF8_LF
PATHS_SHA256=734fc7060f2798bd8b21fd8b96c7847faa5b9c480a89038bec9d686bbd987335
MANIFEST_SHA256=465ad0d0fa8c19b426c949f0f0f73da2343756ce9fd719abfff59e278aaeaeb0
```

## Verificación computacional

Comando reproducible desde el directorio del estudio:

```powershell
$env:PYTHONPATH = (Join-Path $PWD 'src')
python -B -m unittest discover -s tests -v
```

Resultado observado:

```text
UNITTEST_RESULT=PASS
UNITTEST_COUNT=45/45
REPOSITORY_UNITTEST_RESULT=PASS
REPOSITORY_UNITTEST_COUNT=115/115
CHERRY_PICK_CONFLICTS=0
```

La suite incluye
`test_tiny_positive_center_between_two_has_twice_its_radius_as_gap`: la
posibilidad límite de una burbuja positiva diminuta entre dos anfitrionas está
incorporada expresamente en la matemática y el código.

## Fuente semántica PSI enlazada

```text
PSI_REPOSITORY=https://github.com/iPPxp/psicologia-concordante.git
PSI_COMMIT=f068faf9dca98408b1a3b93b43f97401f8768795
PSI_TREE=e47e28e752ab6ad00f2fa97b6e92a81754547d0b
PSI_CANON_003_BLOB=cf223249204c3aae24904d242dbe8862946e898f
PSI_CANON_004_BLOB=6ece278c588ed188ddfb8e89a3d6805fab26bf92
PSI_D4_CANDIDATE_BLOB=053e41ae7d041b8b33ef3148fb1aa748afec62b8
PSI_D4_VERIFIER_BLOB=e571f7331b9f8b76e49acaf256bc2669cc85e81a
```

Los cuatro blobs y el árbol fueron comprobados contra ese commit, alcanzable
desde `origin/main` y desde la rama PSI de investigación en el momento de la
auditoría.

## Autoridad y límites

```text
IDENTITY_AND_PROVENANCE_CANONIZED=YES
CUSTODY_AND_RESEARCH_STATUS_CANONIZED=YES
SCIENTIFIC_CLAIMS_CANONIZED_AS_TRUE=NO
PSI_SEMANTIC_CONTENT_COPIED_INTO_LAB=NO
PSI_CANON_004_REMAINS_EXTERNAL_SEMANTIC_AUTHORITY=YES
TWENTY_FOUR_CELL_PSYCHOLOGICAL_STATUS=RESEARCH
ACTIVATION=NO
FINAL_GIT_COMMIT=90762c11cd75b8f41c61b17ff82a9174d220935b
PUSH_EXECUTED=NO
```

El hash anterior identifica el primer commit que materializa este registro y
el puente de gobernanza. La publicación remota queda pendiente en este corte.
