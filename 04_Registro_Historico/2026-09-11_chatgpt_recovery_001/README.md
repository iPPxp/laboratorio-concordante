# Recuperación ChatGPT 001

Estatus: lote histórico externo preservado.

Fecha del material: 2026-09-11.
Fecha de incorporación al repositorio: 2026-09-12.
Identificador: `RH-BATCH-2026-09-11-CHATGPT-RECOVERY-001`.

Este directorio incorpora al historial del Laboratorio el respaldo conservador preparado desde ChatGPT Library y verificado previamente en Google Drive y Dropbox. Conserva 20 artefactos prioritarios, la auditoría de almacenamiento en formatos Markdown y JSON, y el paquete ZIP original.

## Regla de uso

- Este lote no es Canon ni modifica `01_Canon` o `02_Documentos`.
- Su incorporación Git acredita custodia y procedencia; no acredita verdad matemática, validación empírica, uso clínico, publicación ni activación.
- Los archivos de Psicología Concordante permanecen como material histórico de procedencia; `PSI-001` no se reabre dentro del Laboratorio.
- Los estados `DRAFT`, `CANDIDATE`, `PREPRINT`, `REPAIRED` o equivalentes conservan el significado declarado en cada fuente.
- Cualquier uso conceptual posterior requiere expediente, auditoría y decisión separados.

## Estructura

- `fuentes/`: las 22 entradas extraídas del paquete.
- `paquete/`: el ZIP original completo, conservado byte a byte.
- `MANIFEST.md`: inventario legible con tamaños y SHA-256.
- `MANIFEST.json`: inventario estructurado y banderas de autoridad.
- `CATALOGO_CONTENIDO.md`: análisis humano por conjuntos, cronología, conflictos y dependencias.
- `CLASIFICACION_CONTENIDO.json`: clasificación derivada procesable por máquina.
- `RUTAS_DE_LECTURA.md`: secuencias de lectura por propósito.
- `.gitattributes`: desactiva normalización de texto y diffs sobre el payload para preservar los bytes exactos en Git.

Los tres índices añadidos el 2026-09-12 son derivados y no forman parte del
payload recuperado. El procesamiento está registrado en
`03_Expedientes/RH-003_Procesamiento_Recovery_ChatGPT_2026-09-11.md`.

## Nota de compatibilidad

La imagen cuyo nombre original contiene dos puntos conserva ese nombre dentro del ZIP. Su copia extraída reemplaza `:` por ` -` porque el carácter no es válido en nombres de archivo de Windows; el manifiesto registra la correspondencia.
