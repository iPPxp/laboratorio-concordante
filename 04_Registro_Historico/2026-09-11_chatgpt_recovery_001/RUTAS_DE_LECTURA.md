# Rutas de lectura del recovery 001

Estatus: guía de navegación no normativa.

Estas rutas enlazan los originales preservados. No establecen autoridad ni
modifican los estatus declarados por las fuentes.

## Verificar custodia

1. [README](README.md)
2. [Manifiesto legible](MANIFEST.md)
3. [Manifiesto estructurado](MANIFEST.json)
4. [Auditoría de almacenamiento](fuentes/CONCORDANTE_STORAGE_AUDIT_2026-09-11.md)
5. [Auditoría de almacenamiento JSON](fuentes/CONCORDANTE_STORAGE_AUDIT_2026-09-11.json)
6. [Recovery pack original](paquete/CONCORDANTE_CHATGPT_RECOVERY_PACK_2026-09-11.zip)

La auditoría del 11 de septiembre es histórica. Para el estado actual de Git se
debe verificar `main` y `origin/main` en el momento de la consulta.

## Reconstruir la evolución de Exact Trace

1. [Final repair y freeze del 23 de agosto](fuentes/FINAL_REPAIR_AND_FREEZE_2026-08-23.md)
2. [Matriz reparada del 23 de agosto](fuentes/CLAIMS_MATRIX_FINAL_REPAIRED_2026-08-23.csv)
3. [RAG extremo post-v2](fuentes/15_RAG_EXTREMO_POST_V2.md)
4. [Paquete Exact Trace v2.1](fuentes/EXACT_TRACE_THRESHOLD_EXTREMAL_PACKAGE_V2_1_2026-08-24.zip)
5. Dentro del ZIP: `14_V2_1_REFEREE_REPAIR.md`
6. [Matriz de claims v2.1](fuentes/CLAIMS_MATRIX.csv)
7. [Grafo de dependencias v2.1](fuentes/THEOREM_DEPENDENCY_GRAPH.md)
8. [Fuente TeX del preprint v0.1](fuentes/Exact_Trace_Thresholds_Preprint_v0_1.tex)
9. [PDF del preprint v0.1](fuentes/Exact_Trace_Thresholds_Preprint_v0_1.pdf)

Regla: la matriz del 23 de agosto y la matriz v2.1 no comparten una numeración
estable después de `C18`. No deben combinarse automáticamente por `claim_id`.

## Estudiar la geometría HEART

1. [HEART1](fuentes/HEART1_C_OBJECT_REPORT.md)
2. [HEART2](fuentes/HEART2_REPORT.md)
3. [HEART3](fuentes/HEART3_REPORT.md)
4. [Paper II, candidato arXiv](fuentes/Paper_II_ARXIV_CANDIDATE.pdf)

Regla: propiedades de `c`, `C6`, `C3`, fibras o coders no se traducen por sí
mismas en propiedades psicológicas universales.

## Revisar MOC y su frontera de autoridad

Antes de usar el contenido recuperado, leer las fuentes vigentes del repositorio:

1. [M-000 - Reglas fundamentales](../../01_Canon/M-000_Reglas_Fundamentales.md)
2. [Grafo de experiencia local](../../03_Expedientes/MOC-EXP-GRAPH-001_Grafo_Experiencia_Local.md)
3. [Decisión de aplicación oficial acotada](../../03_Expedientes/MOC-001_Decision_Aplicacion_Oficial_Canon_Doc04_001.md)

Después, leer el lote en este orden:

4. [Investigación de nomenclatura MOC/iPP](fuentes/MOC-IPP-NOMENCLATURE-AND-AGREEMENT-FAMILY-RESEARCH-001.md)
5. [Frontera ontológica, Fase 1](<fuentes/MOC-FRON-ONT-001_Auditoría_II_Fase_1_Rigurosa.md>)
6. [Frontera ontológica, Fase 2](fuentes/MOC-FRON-ONT-001_Auditoria_II_Fase_2_Operadores_Canonicos.md)
7. [Infografía MOC](<fuentes/Infografía MOC - Mapa de Concordancia Experiencial.png>)
8. [Presentación Pentacoron 4D](fuentes/MOC-Pentacoron-Experiencial-4D.pptx)

Regla: la Fase 2 es posterior a la Fase 1. La infografía y la presentación son
materiales explicativos candidatos, no definiciones oficiales.

## Evaluar el borrador de Psicología Concordante

1. [Borrador de arquitectura PSI-HEART](fuentes/PSI-HEART-PROJECTION-ARCHITECTURE_DRAFT.md)
2. recuperar y verificar por separado
   `PSI-CANON-001_Fundamentos_Psicologia_Concordante.md`;
3. recuperar y verificar por separado
   `PSI-CANON-002_Atlas_Corazon_Poder_Transformacion.md`;
4. comparar sus hashes, autoridad y fecha antes de revisar el borrador;
5. abrir un expediente independiente si se propone incorporar algo al
   Laboratorio.

Mientras falten las dos fuentes canónicas declaradas, la ruta queda en
`DEPENDENCIAS_FUENTE_AUSENTES`.

## Revisar Paper I para trabajo editorial

1. [Paquete editorial de Paper I](fuentes/Paper_I_EXPERIMENTAL_MATHEMATICS_SUBMISSION_PACKAGE.zip)
2. dentro del ZIP: metadatos, carta, revisión, TeX y figuras;
3. [PDF directo de consulta](fuentes/Paper_I_EXPERIMENTAL_MATHEMATICS_RESUBMISSION.pdf).

El PDF suelto y el incluido en el ZIP son idénticos; ambos se conservan por su
función editorial distinta.
