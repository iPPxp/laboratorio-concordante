# Concordante — auditoría diferencial de custodia

**Fecha:** 2026-09-11  
**Superficies:** ChatGPT Library ↔ Google Drive ↔ Dropbox ↔ GitHub accesible.  
**Modo:** sólo lectura sobre destinos externos; no se modificó Drive, Dropbox ni GitHub.

## Dictamen

Sí existe un riesgo real de **artefactos huérfanos en ChatGPT Library**.

El hallazgo más importante es HEART1/2/3: los archivos originales completos siguen en ChatGPT Library. Las copias externas `*_RECUPERADO.md` son cápsulas reconstruidas; al menos HEART1 declara explícitamente que no sustituye al original.

La carpeta `Psicologia Concordante/2026-09-11` está razonablemente espejada entre Drive y Dropbox por nombre y tamaño para 12 archivos observados. Esto todavía no equivale a verificación criptográfica.

El programa matemático —Exact Trace, matrices de claims, freezes/RAG y varios candidatos de papers— aparece mucho más expuesto: los artefactos clave localizados en Library no aparecieron en las búsquedas externas representativas realizadas.

## Estado por grupo

| Grupo | Library | Drive | Dropbox | GitHub accesible | Clasificación |
|---|---|---|---|---|---|
| HEART1/2/3 originales | completos | sólo RECUPERADO | sólo RECUPERADO | repo esperado no accesible | **P0 CRÍTICO** |
| PSI-CANON-001/002 | disponible | sí | sí | no verificable | **SAFE-ish** |
| PSI-CANON-003 / decisión / C3 sufficiency | mixto | sí | sí | no verificable | **SAFE-ish** |
| PSI-HEART-PROJECTION draft | sí + duplicado | no encontrado exacto | no encontrado | no verificable | **P1 CHATGPT-ONLY** |
| MOC Pentacoron 4D | sí | no encontrado exacto | no encontrado | no verificable | **P1** |
| MOC auditorías/nomenclatura | sí | búsquedas clave sin resultado | búsquedas clave sin resultado | no verificable | **P1** |
| Exact Trace / claims / RAG | sí | búsquedas clave sin resultado | no visibles fuera de PSI | no verificable | **P1 ALTO** |
| Papers I/II del paquete recuperado | sí | no verificados externamente | no visibles | no verificable | **P1** |

## Espejo Drive ↔ Dropbox observado

- `PSI-CANON-001_Fundamentos_Psicologia_Concordante.md` — 8,326 bytes en ambos listados observados.
- `PSI-CANON-002_Atlas_Corazon_Poder_Transformacion.md` — 10,854 bytes en ambos listados observados.
- `HEART1_C_OBJECT_REPORT_RECUPERADO.md` — 1,530 bytes en ambos listados observados.
- `HEART2_REPORT_RECUPERADO.md` — 1,769 bytes en ambos listados observados.
- `HEART3_REPORT_RECUPERADO.md` — 1,734 bytes en ambos listados observados.
- `PSI-CANON-003_Arquitectura_Corazon_Mente_Proyeccion.md` — 12,851 bytes en ambos listados observados.
- `PSI-001_Decision_Arquitectura_Corazon_Mente_2026-09-11.md` — 1,493 bytes en ambos listados observados.
- `PSI-HEART-C3-AXES-SUFFICIENCY-001.md` — 18,329 bytes en ambos listados observados.
- `verify_c3_sufficiency.py` — 1,744 bytes en ambos listados observados.
- `Psicologia_Concordante_2026-09-11.zip` — 64,118 bytes en ambos listados observados.
- `Psicologia_Concordante_HEART_2026-09-11.zip` — 72,312 bytes en ambos listados observados.
- `Psicologia_Concordante_HEART_C3_2026-09-11.zip` — 82,628 bytes en ambos listados observados.

## Paquete de rescate creado

Se materializaron **20 archivos prioritarios** desde ChatGPT Library y se calculó SHA-256 para cada uno.

- `15_RAG_EXTREMO_POST_V2.md` — 10,121 bytes — `f864c41d271f538ffe6c3fb64aa0b4ed69020e1023d2fc01fd28d6829a319c5e`
- `CLAIMS_MATRIX.csv` — 7,860 bytes — `bf02a16f3ae9108f4e38b68ae3dd539a8d6513078d6e8c458b47612798c45652`
- `CLAIMS_MATRIX_FINAL_REPAIRED_2026-08-23.csv` — 5,447 bytes — `ca806ab617581f66134c2015330b4c2174b4b6e47a00aaab12d1670230a38fbe`
- `EXACT_TRACE_THRESHOLD_EXTREMAL_PACKAGE_V2_1_2026-08-24.zip` — 110,615 bytes — `5b5d78f108076f4e355c452fa66a707fa7249ec5a263dd033600b00170955d63`
- `Exact_Trace_Thresholds_Preprint_v0_1.pdf` — 523,020 bytes — `582302204f3ecf072cf0bbada23afde8508f2dbf16950fbbe9ff7667b09b9a03`
- `Exact_Trace_Thresholds_Preprint_v0_1.tex` — 56,196 bytes — `b65bb29ad12822e6f6c435fbbc349696f5a596847aa23914c9eb57551f9adae5`
- `FINAL_REPAIR_AND_FREEZE_2026-08-23.md` — 4,842 bytes — `371223d8f10142ec0351461b2c4bda1fd21970038d63437d7e0efebc0b5f90d2`
- `HEART1_C_OBJECT_REPORT.md` — 5,570 bytes — `2d570cefc774885301263e83079f28c027a8761445eb7f3a19a6f4ba1fae5ee3`
- `HEART2_REPORT.md` — 10,344 bytes — `6998eadd612b91134f8eb835e2e4f32a3c626f89b4667ffb1e7d8b42d81684cc`
- `HEART3_REPORT.md` — 8,094 bytes — `d974007d754646006d62f265f68b841f6d8749fa42d8f83e921ec1817a01d008`
- `Infografía MOC: Mapa de Concordancia Experiencial.png` — 1,882,979 bytes — `5211bd2edfa72efdf258b6f4a9cbde724e705e4cae66a82a85278657ceac1da5`
- `MOC-FRON-ONT-001_Auditoria_II_Fase_2_Operadores_Canonicos.md` — 15,621 bytes — `f997dcf0366ffbbaea3e1c039f3e8f5cd5559a6c5a0af40ce9b7865f3ab0441d`
- `MOC-FRON-ONT-001_Auditoría_II_Fase_1_Rigurosa.md` — 18,355 bytes — `b5fc3b3652fd39b4021a5ec0d5ad73834fe948a73fba3d544e839a933edcb944`
- `MOC-IPP-NOMENCLATURE-AND-AGREEMENT-FAMILY-RESEARCH-001.md` — 17,548 bytes — `10f4c5f01480de4a9f132cf5a5eef0de3575b697b565bb8106fcf8575f33aad3`
- `MOC-Pentacoron-Experiencial-4D.pptx` — 3,704,871 bytes — `10d44b4b4013a1cc5d6e2d79d570397083d2d67d7907ec6b8013f9abbe569fd9`
- `PSI-HEART-PROJECTION-ARCHITECTURE_DRAFT.md` — 36,600 bytes — `0c6e58e4b47b7b0d325b194a07c0ba32188716c3a2ef54f67b1178e4b7934b9b`
- `Paper_II_ARXIV_CANDIDATE.pdf` — 328,891 bytes — `b8f1dd26cb3f503d7442caad204e79f783f08c50f891e40af987324a9f092129`
- `Paper_I_EXPERIMENTAL_MATHEMATICS_RESUBMISSION.pdf` — 446,611 bytes — `a8ee2d81925a69b7932f2d8a67119e9c03003de0b2b810b1d8b02e6e83f706dc`
- `Paper_I_EXPERIMENTAL_MATHEMATICS_SUBMISSION_PACKAGE.zip` — 626,599 bytes — `b169669f99899283201197b205919ab086dd3dbdea34a3c2aef6d43d7ed6b7de`
- `THEOREM_DEPENDENCY_GRAPH.md` — 1,498 bytes — `bb07353017d81f809726364a62fbc478b30e329538e01202cb371538d113b120`

## GitHub

La conexión GitHub de esta sesión corresponde a `iximco-boop` y sólo expone `iximco-boop/Concordante`. La raíz visible contiene principalmente metadatos Git y README. El repositorio esperado `iPPxp/psicologia-concordante` no está accesible desde esta conexión, así que GitHub no cuenta todavía como copia verificada.

## Limitaciones

- Google Drive no ofrece aquí un recorrido recursivo completo de toda la cuenta; se combinaron listados de carpeta y búsquedas exactas.
- Drive y Dropbox no se compararon hash-a-hash.
- El paquete prioriza artefactos científicos y psicológicos de alto valor; no incluye cada archivo histórico de toda la Library.
- Se excluyeron documentos personales/administrativos ajenos a Concordante.

## Acción recomendada

1. Copiar los tres HEART originales con sus nombres exactos a dos destinos externos.
2. Copiar el paquete de rescate completo a una carpeta autoritativa de recuperación.
3. Conectar la cuenta/repositorio GitHub correcto.
4. Ejecutar después una segunda auditoría ruta+SHA256 antes de deduplicar cualquier cosa de Library.