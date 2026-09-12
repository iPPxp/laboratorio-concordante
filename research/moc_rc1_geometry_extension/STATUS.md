# Estado de la extensión

```text
OBJECT = MOC-RC1-GEOMETRY-EXTENSION-001
STATUS = CANDIDATE
BASELINE = MOC-Base-1.0-RC1-SECRETS2.tar.gz
RC1_ORIGINAL_MUTATED = NO
INTEGRATION_MODE = OPTIONAL_NON_MUTATING_SIDECAR

MATHEMATICAL_COMBINATORICS = ESTABLISHED
SOFTWARE_CONTRACT = LOCALLY_TESTED
WINDOWS_MODEL_ADAPTER_CHECK = IMPORT_ONLY_WITH_FCNTL_SHIM
LINUX_RC1_RUNTIME_CHECK = NOT_RUN_DOCKER_ENGINE_UNAVAILABLE
SCIENTIFIC_VALIDATION = NOT_TESTED

MOC_SEMANTIC_APPROVAL = NOT_GRANTED
ROW_MAPPING_APPROVAL = NOT_GRANTED
PAIRWISE_RELATIONS_APPROVAL = NOT_GRANTED
CANONIZATION = NO
ACTIVATION = NO
MODEL_TRAINING_AUTHORIZED = NO
```

La extensión materializa una interfaz que puede probarse, pero no decide la
semántica MOC. El mapeo entre las filas históricas `I/E/A/V/S` de RC1 y
`P/Eaf/Act/V/S` debe ser suministrado y documentado por una autoridad humana.

La comprobación Windows del adaptador puede importar las clases de datos reales
de RC1 mediante un sustituto inerte de `fcntl`. Esto sirve únicamente para
comprobar la frontera de tipos y la ausencia de mutación; no prueba el vault ni
el funcionamiento integral de RC1, que está diseñado para POSIX/Linux.

