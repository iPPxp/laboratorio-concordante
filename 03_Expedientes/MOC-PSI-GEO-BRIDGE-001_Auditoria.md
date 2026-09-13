# MOC-PSI-GEO-BRIDGE-001 — Auditoría del puente 4D

Estatus: revisión Git final favorable y primer commit de gobernanza
materializado localmente; publicación pendiente.

Fecha: 2026-09-12.

Expediente: `MOC-001`.

Decisión asociada: `D-2026-09-12-001`.

## Objetos auditados

- los dos commits fuente y los dos cherry-picks preparados del Lab;
- las 37 rutas de `LAB-RESEARCH-PROVENANCE-002`;
- cuatro blobs autoritativos del commit PSI `f068faf9...`;
- la correspondencia documental del 4-simplex;
- la hipótesis de investigación del 24-cell;
- las suites `unittest` del Lab y el verificador entero PSI `D4`.

## Evidencia Git

| Control | Resultado |
| --- | --- |
| `origin/main` del Lab actualizado mediante fetch dirigido | `71a84f655ff4ec71a89640cca1f1b781fc523d79` |
| Cadena mínima cerrada | `679e898` seguida por `d65aab8` |
| Commits previos ajenos arrastrados | 0 |
| Conflictos de cherry-pick | 0 |
| Payload preparado | `4b59c3b` seguido por `8b7ad0e` |
| Árbol preparado tras payload | `89efdef2a066c0e9432dd5ebcf15efa8f1f4fc29` |
| `8b7ad0e...` es ancestro de `HEAD` preparado | sí |
| Diff del directorio de payload preparado contra fuente `d65aab8` | vacío |
| Rutas de la extensión | 37/37 presentes |
| Huellas SHA-256 | 37/37 coincidentes |
| SHA-256 de `PATHS.txt`, serialización UTF-8/LF | `734fc7060f2798bd8b21fd8b96c7847faa5b9c480a89038bec9d686bbd987335` |
| SHA-256 de `SHA256SUMS.txt`, serialización UTF-8/LF | `465ad0d0fa8c19b426c949f0f0f73da2343756ce9fd719abfff59e278aaeaeb0` |
| Snapshot histórico P001 | 39/39 mediante `git cat-file --filters` |
| Overlay vivo P001 + P002 | 56/56; superposición exacta de 20 |

El worktree usado es `C:\w\lab4d-0912`. El checkout principal no fue usado
para editar ni para cherry-pick.

## Evidencia matemática y computacional

La suite se ejecutó con `unittest`, no con `pytest`:

```powershell
$env:PYTHONPATH = (Join-Path $PWD 'src')
python -B -m unittest discover -s tests -v
```

```text
Ran 45 tests
OK
```

Entre las 45 pruebas constan:

- contrato Gram y contactos `K5` del 4-simplex regular;
- raíces, contactos, pares antipodales e invariancia de escala del 24-cell;
- rechazo explícito de pérdida silenciosa de coordenadas 4D en visualizadores
  3D;
- intersticios regulares y desiguales;
- seis matchings entre dos ternas;
- distinción tipada prisma/octaedro y cruces visuales;
- `test_tiny_positive_center_between_two_has_twice_its_radius_as_gap`.

La última prueba confirma expresamente la burbuja positiva diminuta entre dos y
su límite cuando el radio tiende a cero.

La suite general del repositorio, ampliada con controles de tamper, ruta
faltante, duplicado y cardinalidad de overlay, produjo `115/115 PASS`.

El verificador PSI del commit autoritativo produjo:

```text
status=PASS
checks=20/20
enumeration_sha256=510EDB65C7F1A94453C3A884B68D2E0A00F6D762310002C366648587B9418ACD
```

## Evidencia de autoridad PSI

| Objeto | Blob verificado en `f068faf9...` |
| --- | --- |
| `PSI-CANON-003` | `cf223249204c3aae24904d242dbe8862946e898f` |
| `PSI-CANON-004` | `6ece278c588ed188ddfb8e89a3d6805fab26bf92` |
| `PSI-D4-LOCAL-CARRIER-001` | `053e41ae7d041b8b33ef3148fb1aa748afec62b8` |
| verificador `D4` | `e571f7331b9f8b76e49acaf256bc2669cc85e81a` |

El commit y su árbol coinciden con los identificadores declarados y el commit
es alcanzable desde `origin/main` de Psicología Concordante.

## Controles semánticos

| Condición | Resultado |
| --- | --- |
| 4-simplex remite a `PSI-CANON-004` | cumplida |
| 24-cell se conserva como investigación | cumplida |
| `K6` completo y ciclo `C6` permanecen distintos | cumplida |
| `A4` y `D4` no reciben biyección canónica | cumplida |
| `RAT`, `RLF`, Higher Mind y Personalidad siguen abiertos | cumplida |
| autoridad PSI no se copia ni se suplanta desde el Lab | cumplida |
| identidad/procedencia no se confunden con verdad de claims | cumplida |

## Dictamen

`MOC-PSI-GEO-BRIDGE-001` es documentalmente consistente y reproducible. El
diff completo quedó revisado y su primer registro de gobernanza se materializó
en `90762c11cd75b8f41c61b17ff82a9174d220935b`. La publicación remota permanece
pendiente en este corte.
