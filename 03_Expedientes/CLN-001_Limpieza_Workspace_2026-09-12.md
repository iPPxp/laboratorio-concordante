# CLN-001 — Limpieza conservadora del workspace

Estatus: procesamiento local cerrado con custodia recuperable.

Fecha: 2026-09-12.

## Resultado

El workspace autoritativo se limpió después de preservar su estado completo.
La operación no incorporó payload científico a `origin/main`, no modificó
Canon y no activó software.

```text
PREFLIGHT_STATUS_ENTRIES=478
PREFLIGHT_TRACKED_MODIFIED=11
PREFLIGHT_UNTRACKED=467
SNAPSHOT_FILES=1308
SNAPSHOT_HASH_MATCHES=1308/1308
SCIENTIFIC_OBJECTS_MANIFESTED=248/248
SCIENTIFIC_LOCAL_TESTS=97/97
AUTOMATION_LOCAL_TESTS=107/107
WORKSPACE_STATUS_AFTER_CLEANUP=0
```

## Custodia

La cápsula `WORKSPACE-CLEANUP-2026-09-12-001` conserva:

- snapshot completo sin directorios `.git`;
- manifiesto por ruta, tamaño y SHA-256;
- diff binario y estado previo;
- bundle Git completo anterior y posterior a la preservación;
- instrucciones de recuperación.

La cápsula está en almacenamiento local del mismo disco: es una salvaguarda de
reorganización, no un respaldo independiente.

## Acciones

- cuatro artefactos científicos fueron reubicados dentro de sus familias con
  SHA-256 idéntico;
- cinco familias quedaron en commits locales separados;
- `exports/`, `output/`, `outputs/` y `tmp/` se retiraron de la raíz;
- nueve directorios `__pycache__` regenerables se enviaron a la Papelera;
- `Concordantes/`, los metadatos Git, worktrees, ramas, Canon y payloads
  históricos quedaron fuera de alcance.

Todo lo retirado permanece recuperable desde la cápsula y, para los elementos
enviados a la Papelera, también desde la Papelera mientras no se vacíe.
