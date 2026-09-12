# Mapa de coherencia operativo del repositorio

Estatus: mapa administrativo vigente; no decisorio y no semántico.

Fecha de corte: 2026-09-12.

Base Git auditada: `origin/main@a3fb716898db6f425bcd539c2dc6415f28f53d6a`.

Este documento reconcilia las superficies del repositorio después de la
incorporación del corpus de investigación y del recovery de ChatGPT. No sustituye
el Canon, no reescribe documentos históricos y no cambia el estatus científico,
empírico, clínico, editorial u operacional de ningún contenido.

## Regla de lectura

Cuando dos archivos parezcan contradecirse, distinguir primero qué clase de
afirmación contiene cada uno:

1. `01_Canon`: reglas y objetos canónicos expresamente decididos.
2. `05_Estado_Proyecto`: corte operativo y rutas vigentes.
3. `02_Documentos`: contenido oficial, subordinado al Canon.
4. decisiones registradas: autorizaciones y cierres de alcance específico.
5. `03_Expedientes`: investigación, auditoría y trazas abiertas o cerradas.
6. `06_Automatizacion`: comprobaciones y evidencia operativa no autoritativa.
7. `04_Registro_Historico`: custodia y reconstrucción; nunca autoridad directa.

Una frase de estado incluida en un documento histórico describe su fase de
creación. No vence por sí misma a un corte Git posterior verificable.

## Inventario de superficies

| Superficie | Archivos versionados | Función coherente |
| --- | ---: | --- |
| raíz | 11 | entrada, estado breve, licencia e históricos inactivos |
| `01_Canon` | 4 | reglas y registro canónico de identidad/procedencia |
| `02_Documentos` | 9 | documentos oficiales y Nivel C |
| `03_Expedientes` | 411 | trazas temáticas, decisiones y auditorías |
| `04_Registro_Historico` | 60 | historial y cápsulas de custodia |
| `05_Estado_Proyecto` | 9 antes de este mapa | estado, decisiones y revisión de formalización |
| `06_Automatizacion` | 168 | herramientas no mutantes, fixtures y reportes |
| investigación degenerante | 39 | corpus científico con identidad canónica, no claims canónicos |

El gran volumen de `03_Expedientes` responde a la conservación de cada paso de
MOC, AO, AUD, HXI y automatización. No debe recorrerse alfabéticamente como si
los 411 archivos tuvieran igual vigencia. Se entra por los expedientes padre y
por las decisiones más recientes.

## Estado coherente por dominio

### Canon y documentos oficiales

- `M-000` y `M-001` siguen siendo las reglas rectoras.
- Documentos 00–04 permanecen consolidados; Documento 04 contiene la adopción
  oficial acotada de `operator_trace_graph` decidida por `D-2026-07-09-005`.
- `C-001` y `C-002` siguen siendo las únicas especificaciones oficiales de
  Nivel C registradas.
- No se crea `C-003`, no se promueve `REPORT_LAYER` y no se autoriza modo
  mutante.

### Expedientes abiertos

| Expediente | Estado vigente | Próxima transición permitida |
| --- | --- | --- |
| `MOC-001` | abierto en mantenimiento teórico-operativo, no clínico y sin ejecución empírica | monitoreo post-adopción sólo mediante decisión explícita |
| `AO-001` | abierto; readiness global `mantener_no_autorizado` | reconsideración separada usando evidencia externa si se autoriza |
| `TCS-001` | teoría provisional no canónica | maduración semántica y más casos no regulados |

`TCS-001.md` funciona desde este corte como índice padre de sus diez documentos;
no introduce axiomas ni decisiones nuevas.

### Expedientes cerrados, congelados y transferidos

- `RH-003` es el procesamiento histórico cerrado más reciente; organiza el
  recovery sin promoverlo.
- `HXI-001`, `AUD-001`, `AUT-001`, `AUT-002`, `R001-001`, `RH-001`, `RH-002` y
  los demás cierres registrados permanecen cerrados.
- `H-B.6`, `H-B.7` y `B-001.5` permanecen congelados.
- `PSI-001` permanece transferido al proyecto independiente Psicología
  Concordante. El borrador PSI recuperado no lo reabre.

### Corpus de investigación degenerante

La situación coherente tiene dimensiones separadas:

```text
CORPUS_PRESERVED=YES
INCORPORATION_COMMIT=2c3264c473c865835571a1df4b28e1a022790695
INCORPORATION_REACHABLE_FROM_ORIGIN_MAIN=YES
GOVERNANCE_COMMIT=f6ba1f7e35ae5f8b771ba6c0a73cb18d65c19317
GOVERNANCE_REACHABLE_FROM_ORIGIN_MAIN=YES
CORPUS_IDENTITY_CANONICAL=YES
PROVENANCE_CHAIN_CANONICAL=YES
SCIENTIFIC_CLAIMS_CANONIZED_AS_TRUE=NO
MATHEMATICAL_CLAIMS_CANONIZED_AS_PROVEN=NO
EMPIRICAL_VALIDATION=NO
ACTIVATION=NO
```

El commit fuente `96843d913fb21e673707f01da8e2929cda8c33be` conserva identidad
archivística, pero no fue incorporado íntegramente como ancestro de `main`. La
transferencia autorizada de 39 rutas vive en `2c3264c...`, que sí es alcanzable
desde `origin/main`. Esta diferencia es deliberada y no es una pérdida de
procedencia.

Los 39 hashes del manifiesto continúan coincidiendo. Las pruebas del estudio
principal pasan 12/12 y las de la unidad proyectiva N2 pasan 6/6. Estos controles
demuestran reproducibilidad local acotada, no verdad universal ni validación
empírica.

### Recovery de ChatGPT

```text
CUSTODY_PRESERVED=YES
GIT_INCORPORATION=YES
CONTENT_CLASSIFIED=YES
CANON=NO
SEMANTIC_AUTHORITY=NO
SCIENTIFIC_OR_EMPIRICAL_VALIDATION=NO
ACTIVATION=NO
```

El lote se incorporó por custodia en `c3a4855b71ada97c940adba7d7820418c67c8a9c`
y se organizó en `a3fb716898db6f425bcd539c2dc6415f28f53d6a`. Su entrada correcta
es `04_Registro_Historico/2026-09-11_chatgpt_recovery_001/CATALOGO_CONTENIDO.md`.

### Automatización

- Las herramientas continúan siendo no mutantes respecto de Canon, decisiones y
  transformaciones materiales.
- Una prueba aprobada confirma únicamente su contrato comprobado.
- Los reportes guardados son cortes reproducibles, no autoridad superior ni
  garantía de actualidad indefinida.
- La suite de repositorio del corte de coherencia pasa 110/110 pruebas.

### Archivos raíz inactivos

`HANDOFF.md`, `HANDOFF_PACKAGE.md`, `VISION_PAPER_PROPUESTA.md` y
`VISION_PAPER_FINAL_REFERENCIAS.md` permanecen históricos o inactivos. No son
entrada recomendada ni autoridad vigente.

## Contradicciones reconciliadas

1. La investigación degenerante ya no se describe como “sin commit ni push”:
   esa frase pertenece a su fase de preparación aislada.
2. El registro canónico de procedencia ya está materializado en Git; esta
   corrección factual no amplía su objeto canónico.
3. `MOC-CANON-DOC04-APPLY-001` ya fue ejecutado por `D-2026-07-09-005`; no es
   una ruta futura pendiente.
4. `RH-003` queda distinguido como cierre de procesamiento histórico, sin
   desplazar el significado de los últimos cierres sustantivos.
5. `TCS-001` recibe una entrada padre para evitar navegar diez piezas aisladas.
6. El recovery y el corpus científico quedan separados: compartir vecindad en
   el repositorio no implica relación matemática o semántica.

## Deudas vivas, sin autorización automática

- Confluencia global y Equivalencia global.
- Promoción formal de `REPORT_LAYER`.
- Exportación general de R4/Gamma.
- Decisión sobre una reconsideración de readiness de `AO-001`.
- Maduración posterior de `TCS-001`.
- Monitoreo post-adopción de MOC, sólo si se abre explícitamente.
- Revisión independiente de resultados científicos y manuscritos recuperados.
- Recuperación de las fuentes `PSI-CANON-001/002` dentro de su proyecto externo,
  no dentro del Laboratorio por defecto.

## Entrada recomendada

1. `CURRENT_STATE.md`
2. este mapa
3. `INDEX.md`
4. `01_Canon/M-000_Reglas_Fundamentales.md`
5. `05_Estado_Proyecto/ESTADO_ACTUAL.md`
6. el expediente padre del frente que se vaya a trabajar

## Dictamen

`REPOSITORIO_COHERENTE_CON_DEUDAS_EXPLICITAS`.

La coherencia alcanzada es documental y de gobernanza. No equivale a cierre de
los frentes científicos, formalización global, canonización adicional,
publicación, activación ni validación empírica.
