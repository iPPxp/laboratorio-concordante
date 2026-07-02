# SRC-008 - extraccion textual

Fuente: `Laboratorio_M-000_Estado_Consolidacion_Borrador.docx`

Estatus: material historico extraido automaticamente; no autoridad directa.

## Texto

## word/document.xml

Laboratorio M-000 — Estado de Consolidación (Borrador Canónico)
Estado general
Este documento resume el estado alcanzado del núcleo formal del Laboratorio durante la conversación. No sustituye el futuro canon numerado, pero sirve como referencia de trabajo.
Arquitectura general
Separación explícita entre Axiomas, Definiciones, Decisiones de diseño, Teoremas, Fallas estructurales, Algoritmos y Problemas abiertos.
Principio de Dependencia Explícita adoptado como criterio metodológico.
Separación entre Firmas, Instancias del GDI y Anotaciones del modelo.
Firmas estructurales
Subsunción definida semánticamente y caracterizada sintácticamente mediante embeddings tipados e inyectivos.
Equivalencia derivada por antisimetrización.
RFE organizado mediante relación de cobertura (diagrama de Hasse).
Gramática positiva, tipada, sin variables libres, con tamaño acotado (N_max).
Comparación de firmas
C-S1 compara por embeddings.
C-S2 refina únicamente el caso de incomparabilidad.
Separación entre existencia de compatibilidad y construcción de Γ.
Problema abierto: cardinalidad de Γ (P-S1c).
Axiomas del núcleo
Ax-1: Finitud sintáctica.
Ax-2: Alfabeto finito.
Ax-3: Universo finito de Firmas del GDI-core.
Ax-4: Clausura finita de la abstracción instancia → Firma.
Decisiones de diseño principales
D-S1: RFE almacena cobertura.
D-S2: Predicados positivos.
D-S3: Cota N_max.
D-S4: Matching inyectivo.
D-S5: Semántica existencial abierta.
D-S6: Predicados atómicos sin inferencia interna.
D-S7: Compatibilidad mediante alineación estructural.
Auditoría y R4
Separación entre terminación del Auditor y convergencia del modelo.
T-R4.1: El Auditor termina bajo precondiciones explícitas.
Cycle{} pertenece a la capa de anotaciones del modelo.
Un certificado total por SCC en el núcleo.
FE-CYC-0: ausencia de certificado.
FE-CYC-1: certificado inválido.
D-R4.5: Codominios pertenecen a un repertorio finito y decidible.
Pendientes
Formalizar operativamente R4 (clausura de ruptura).
Definir extracción de Firmas desde regiones de ruptura.
Construcción eficiente de Γ (C-S2b).
Algoritmo completo del Auditor.
Formato del Informe de Ruptura.
Casos de prueba y validación.
