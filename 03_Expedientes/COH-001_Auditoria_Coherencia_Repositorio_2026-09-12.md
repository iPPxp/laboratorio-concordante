# COH-001 - Auditoría de coherencia del repositorio

Estatus: auditoría cerrada con correcciones administrativas; sin promoción
semántica.

Fecha: 2026-09-12.

Base auditada: `origin/main@a3fb716898db6f425bcd539c2dc6415f28f53d6a`.

## Propósito

Reconciliar el estado actual, la navegación y los registros Git después de la
incorporación del corpus científico y del recovery de ChatGPT, sin reescribir
payload histórico ni cambiar estatus científicos o de activación.

## Fuentes

- `README.md`, `INDEX.md` y `CURRENT_STATE.md`;
- `01_Canon` y `02_Documentos`;
- `05_Estado_Proyecto/ESTADO_ACTUAL.md` y
  `05_Estado_Proyecto/REVISION_FORMALIZACION_PENDIENTE.md`;
- expedientes padre y decisiones registradas;
- `LAB-RESEARCH-PROVENANCE-001` y su manifiesto de 39 rutas;
- `RH-003` y la cápsula de recovery;
- historia y alcanzabilidad Git de `origin/main`;
- suites de pruebas del repositorio y del corpus científico.

## Hallazgos

| ID | Hallazgo | Severidad | Tratamiento |
| --- | --- | --- | --- |
| `COH-F01` | registros actuales todavía decían que el corpus de investigación no tenía commit o push | alta documental | reconciliar con `2c3264c...` y `f6ba1f7...` alcanzables desde `origin/main` |
| `COH-F02` | la revisión de formalización proponía ejecutar una ruta MOC ya ejecutada | alta documental | marcar `D-2026-07-09-005` como cierre de esa ruta y dirigir a monitoreo opcional |
| `COH-F03` | `TCS-001` carecía de expediente padre aunque tenía diez documentos | media | crear un índice padre sin semántica nueva |
| `COH-F04` | `RH-003` no aparecía en la lista de cierres históricos | media | agregarlo como procesamiento, separado de cierres sustantivos |
| `COH-F05` | la entrada raíz seguía llamando “candidata aislada” a investigación ya materializada | alta documental | actualizar navegación y conservar la fase aislada sólo como procedencia histórica |
| `COH-F06` | el repositorio no tenía un mapa único que separara custodia, incorporación, autoridad, validación y activación | alta de navegación | crear mapa Markdown y JSON |

No se encontraron enlaces Markdown rotos, JSON inválidos ni CSV ilegibles en el
corte auditado.

## Correcciones permitidas

- actualizar afirmaciones factuales de materialización Git;
- añadir notas de fase histórica a documentos de preparación;
- corregir la ruta MOC vigente;
- crear navegación y un hub para `TCS-001`;
- actualizar índices y estado sin introducir decisiones sustantivas.

## Correcciones no permitidas

- alterar los 39 archivos del corpus científico;
- alterar los 23 objetos de payload del recovery;
- declarar verdaderos o probados claims por su presencia en Git;
- activar ConcordIA, MOC, validadores, modo mutante o usos empíricos;
- reabrir PSI dentro del Laboratorio;
- cerrar AO, MOC, TCS o problemas globales.

## Verificación

```text
TRACKED_FILES_AT_AUDIT_BASE=711
MARKDOWN_LINK_ERRORS=0
JSON_PARSE_ERRORS=0
CSV_PARSE_ERRORS=0
RESEARCH_MANIFEST_HASHES=39/39
RESEARCH_MAIN_TESTS=12/12
PROJECTIVE_N2_TESTS=6/6
REPOSITORY_TESTS=110/110
```

## Criterio de cierre

La auditoría cierra cuando las seis incoherencias documentales tienen una ruta
explícita, los payloads protegidos conservan identidad y las pruebas siguen
aprobadas.

## Dictamen

`COHERENCIA_DOCUMENTAL_RESTAURADA_SIN_CAMBIO_DE_AUTORIDAD`.

Las deudas globales permanecen abiertas y se enumeran en
`05_Estado_Proyecto/MAPA_COHERENCIA_2026-09-12.md`.
