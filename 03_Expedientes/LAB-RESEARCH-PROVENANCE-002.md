# LAB-RESEARCH-PROVENANCE-002 — Registro de la extensión 4D

Estatus: extensión de investigación con identidad, procedencia, custodia y
clasificación canónicas; integración Git preparada y pendiente de revisión
final.

Fecha: 2026-09-12.

Decisión asociada: `D-2026-09-12-001`.

## Propósito

Registrar el conjunto cerrado de 37 rutas que amplía el corpus de
empaquetamientos esféricos degenerantes con:

- intersticios entre dos o más anfitrionas;
- refinamiento y carriers multinivel tipados;
- auditoría geométrica `R3`;
- geometría dimension-agnostic y coordenadas en `R^4`;
- 4-simplex regular y su grafo de contactos;
- raíces `D4`, 24-cell y shell de kissing número 24;
- pruebas y resultados reproducibles correspondientes.

## Ubicación

- Payload: `investigacion_empaquetamientos_esfericos_degenerantes/`.
- Procedencia: `LAB-RESEARCH-PROVENANCE-002_PROVENANCE.md`.
- Rutas: `LAB-RESEARCH-PROVENANCE-002_PATHS.txt`.
- Huellas: `LAB-RESEARCH-PROVENANCE-002_SHA256SUMS.txt`.
- Registro canónico: `01_Canon/LAB-RESEARCH-PROVENANCE-002_Extension_4D_Corpus_Canonico.md`.
- Puente PSI: `MOC-PSI-GEO-BRIDGE-001_Puente_4Simplex_24Cell.md`.

## Clasificación

```text
LAB_ROLE=CUSTODY_AND_RESEARCH_PROVENANCE
RESEARCH_STATUS=ACTIVE_RESEARCH_MATERIAL
DELTA_IDENTITY_CANONICAL=YES
PROVENANCE_CHAIN_CANONICAL=YES
SCIENTIFIC_CLAIMS_CANONIZED_AS_TRUE=NO
PSYCHOLOGICAL_SEMANTIC_AUTHORITY=EXTERNAL_PSI_CANON_EXACT_COMMIT
ACTIVATION=NO
```

## Estado Git preparado

```text
TARGET_BASE=origin/main@71a84f655ff4ec71a89640cca1f1b781fc523d79
PAYLOAD_COMMITS=4b59c3bd13d6bd8ae3d09a3c5f847fe1b3ef1b8e,8b7ad0e02ca231a0f35ddd2ccff7c4d2d18ef2db
PREPARED_TREE=89efdef2a066c0e9432dd5ebcf15efa8f1f4fc29
PAYLOAD_MATCHES_SOURCE_BRANCH=YES
CHERRY_PICK_CONFLICTS=0
FINAL_GOVERNANCE_COMMIT=PENDING_AFTER_REVIEW
PUSH_EXECUTED=NO
```

## Criterio de cierre

El registro queda materialmente completo cuando:

1. las 37 rutas y 37 huellas vuelvan a verificarse;
2. las 45 pruebas `unittest` permanezcan aprobadas;
3. las 115 pruebas generales, incluidos los controles de manifiestos
   versionados, permanezcan aprobadas;
4. el diff completo de gobernanza sea revisado;
5. el commit final y su alcance se registren sin alterar los identificadores de
   fuente;
6. la rama autorizada se publique o incorpore a `origin/main` mediante decisión
   Git posterior.
