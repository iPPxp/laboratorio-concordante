# Laboratorio Concordante

Este repositorio contiene la forma vigente del Laboratorio Concordante. Su objetivo principal es que una persona o una IA puedan incorporarse al proyecto en pocos minutos sin depender de una conversacion larga, dispersa o privada.

La regla practica es simple: la conversacion puede producir intuiciones, pero el repositorio conserva la arquitectura. Lo que no esta registrado aqui no debe tratarse como estado vigente del Laboratorio.

## Que es el Laboratorio

El Laboratorio Concordante es un proyecto de investigacion arquitectonica: organiza definiciones, hipotesis, decisiones, problemas abiertos, procedimientos de auditoria y expedientes de trabajo para estabilizar una estructura conceptual coherente.

No es solo una coleccion de notas. Es un sistema de continuidad. Su funcion es permitir que distintos agentes, humanos o IA, trabajen sobre la misma base sin volver a reconstruir el contexto desde cero.

El Laboratorio distingue estrictamente entre:

- Definiciones: fijan vocabulario y alcance.
- Hipotesis: propuestas activas, aun no demostradas ni canonizadas.
- Teoremas: resultados demostrados dentro del marco aceptado.
- Algoritmos: procedimientos ejecutables o formalizables.
- Expedientes: unidades de investigacion abiertas o cerradas.
- Problemas abiertos: preguntas reconocidas que todavia no tienen resolucion estable.
- Decisiones: actos explicitos de cierre, aceptacion, rechazo o congelamiento.

Esa clasificacion evita que una idea prometedora sea tratada como verdad oficial antes de pasar por demostracion, auditoria o decision explicita.

## Que intenta hacer

El Laboratorio intenta convertir una investigacion extensa en un repositorio gobernable. Para lograrlo, separa la verdad vigente, el trabajo en curso y el historial completo.

Sus objetivos operativos son:

- Mantener documentos oficiales breves, auditables y actualizados.
- Registrar la investigacion en expedientes identificables.
- Distinguir lo probado, lo decidido, lo hipotetico y lo pendiente.
- Conservar el historial sin usarlo como superficie normal de trabajo.
- Permitir que una IA lea el estado actual y sepa por donde empezar.
- Evitar bucles de rediscusion sobre temas ya cerrados.

El Laboratorio tambien intenta preparar su propia automatizacion. Esto incluye flujos para auditar documentos, detectar deudas conceptuales, actualizar el estado del proyecto, revisar dependencias y proponer cierres de expedientes cuando corresponda.

## Que no intenta hacer

El Laboratorio no intenta ser una conversacion infinita ni un espacio libre de ocurrencias. Tampoco intenta maximizar produccion de ideas nuevas sin control.

En particular, no intenta:

- Reabrir decisiones cerradas sin evidencia nueva.
- Convertir hipotesis en Canon por entusiasmo, analogia o utilidad narrativa.
- Usar el historial como fuente directa de autoridad.
- Mezclar investigacion activa con documentos oficiales.
- Ocultar incertidumbre bajo lenguaje formal.
- Resolver todo en un unico documento totalizante.
- Depender de una IA especifica, una plataforma especifica o una memoria conversacional especifica.

El Laboratorio prefiere perder velocidad antes que perder trazabilidad. Una afirmacion importante debe poder ubicarse: en que documento vive, de que expediente proviene, que estatus tiene y que decision la sostiene.

## Como esta organizado

El repositorio esta organizado en seis zonas principales y algunos archivos raiz.

### Archivos raiz

- `README.md`: orientacion general del Laboratorio.
- `HANDOFF.md`: traspaso operativo historico, inactivo hasta nuevo aviso.
- `HANDOFF_PACKAGE.md`: manifiesto historico del paquete de handoff, inactivo hasta nuevo aviso.
- `INDEX.md`: mapa de lectura y rutas recomendadas.
- `CURRENT_STATE.md`: estado minimo, disenado para lectura inmediata.
- `PROMPT_MAESTRO.md`: prompt base para incorporar una IA al trabajo.
- `CHANGELOG.md`: registro de cambios del repositorio.
- `Licencia_y_Derechos.md`: reserva de derechos del MOC y Concordante Lab.

### 01_Canon

Contiene solo reglas fundamentales. Debe ser pequeno, estable y dificil de modificar.

El Canon no es el lugar para investigacion, ejemplos largos, motivacion historica ni discusiones. Si una regla no es fundamental, vive en documentos o expedientes.

### 02_Documentos

Contiene documentos oficiales por tema. Estos textos representan la verdad vigente del Laboratorio, siempre subordinada al Canon y al estado del proyecto.

Documentos iniciales:

- `00_Naturaleza.md`
- `01_Canon.md`
- `02_Fundamentos_Matematicos.md`
- `02-0_Perimetro_Epistemologico.md`
- `03_Ontologia.md`
- `04_Algebra_Operacional.md`

### 03_Expedientes

Contiene investigacion viva. Un expediente puede durar dias o meses. Puede estar abierto, congelado, cerrado, rechazado o absorbido por un documento oficial.

Los expedientes no son verdad vigente por si mismos. Son trazas organizadas del trabajo que puede llegar a modificar documentos o Canon.

### 04_Registro_Historico

Contiene conversaciones completas, transcripciones y materiales historicos. No se usa para trabajar salvo auditoria, reconstruccion o trazabilidad.

La regla es importante: el historial explica como se llego a una decision, pero no sustituye a la decision.

### 05_Estado_Proyecto

Contiene el estado operativo del Laboratorio: documentos vigentes, expedientes abiertos, hipotesis activas, problemas abiertos, ultimas decisiones y proximos objetivos.

Para una IA nueva, este es el punto de entrada despues de `CURRENT_STATE.md`.

### 06_Automatizacion

Contiene herramientas ejecutables no mutantes y sus reportes conservados. Su funcion inicial es revisar y reportar, no transformar ni autorizar cambios.

## Estado actual

Estado operativo resumido:

- Decision operativa vigente: `MOC-001_Decision_Aplicacion_Oficial_Canon_Doc04_001.md` (`D-2026-07-09-005`) acepta y ejecuta `MOC-CANON-DOC04-APPLY-001` en alcance acotado; `M-001` adopta matriz de superficies y Documento 04 adopta entrada auxiliar por traza local de grafo. `M-000` queda sin cambio textual.
- Decisiones de estabilizacion recientes: `D-2026-07-02-020` a `D-2026-07-09-005`.
- Ultimos expedientes cerrados: `HXI-001` y `AUD-001`; ultimos expedientes tecnicos cerrados: `AUT-002` y `R001-001`.
- Ultima decision arquitectonica: `C-002_RFC_Operativo_Auditor_v0.md` promovido como RFC operativo oficial del Auditor v0; complementa `C-001` y quedo alineado el 2026-07-03 con JSON, fixtures y adaptador no mutante.
- Ultimas decisiones operativas: `MOC-001_Decision_Aplicacion_Oficial_Canon_Doc04_001.md` (`D-2026-07-09-005`), `MOC-001_Decision_Compuerta_Incorporacion_Canon_Doc04_001.md` (`D-2026-07-09-004`), `MOC-001_Decision_Matriz_Impacto_Canon_Doc04_001.md` (`D-2026-07-09-003`), `MOC-001_Decision_Autorizacion_Grafo_Canon_Doc04.md` (`D-2026-07-09-002`), `MOC-001_Decision_Grafo_Experiencia_Local.md` (`D-2026-07-09-001`) y `AO-001_Decision_Evidencia_Externa_Real_001.md` (`D-2026-07-06-035`).
- Avance MOC reciente: `MOC-ROUTE-012` relaciona documentalmente MOC con `C-001` / `C-002`; `D-2026-07-09-001` a `D-2026-07-09-005` aceptan grafo local, autorizacion preparatoria, matriz candidata, compuerta de incorporacion y aplicacion oficial acotada sobre `M-001` y Documento 04. Nivel C, `C-001`, `C-002`, cierre global, uso clinico/regulado, modo mutante, `REPORT_LAYER` y exportacion R4/Gamma permanecen sin promocion.
- Decision teorica reciente: `TCS-001_Decision_Maduracion_Provisional.md` (`D-2026-07-05-010`) acepta `TCS-METRIC-PROV-001`, `TCS-EXT-CASE-001` y `TCS-AUTH-CONF-001`; no canoniza `Concordance`, no crea Nivel C ni usa vision papers como fuente activa.
- Avance AO reciente: `AO-DOC04-WIDE-001` queda aceptado por `D-2026-07-06-006` como formalizacion amplia v0 del Documento 04 y probado localmente por `D-2026-07-06-007`; `REPORT_LAYER` queda precisado por `AO-REPORT-LAYER-BRIDGE-001`, mantenido local pre-C por `D-2026-07-06-014` y cubierto por la compuerta no mutante `REPORT-LAYER-C002-GATE-001` aceptada por `D-2026-07-06-015`. `AO-PPI-BRIDGE-002`, `AO-PPI-BRIDGE-003`, `AO-REPORT-SERIAL-001`, `AO-TCS-REL-001`, `AO-AUTH-GLOBAL-001`, `AO-EXT-COV-001`, `AO-PPI-BRIDGE-004` y `AO-PPI-LOCAL-CLOSE-001` quedan aceptados por `D-2026-07-06-017` a `D-2026-07-06-024`; `AO-PROTO-INDEP-001`, `AO-EQ-GLOBAL-GATE-001`, `AO-CONF-GLOBAL-GATE-001`, `AO-REPORT-PROMO-GATE-001`, `AO-R4-GAMMA-EXPORT-GATE-002` y `AO-GLOBAL-READINESS-001` quedan aceptados por `D-2026-07-06-025` a `D-2026-07-06-030`; `AO-EXT-INDEP-001` y `AO-EXT-EVID-GATE-001` quedan preparados por `D-2026-07-06-031` a `D-2026-07-06-034`; `AO-EXT-REAL-001` queda aceptado por `D-2026-07-06-035` como evidencia externa real admisible preliminarmente. La salida vigente sigue siendo `mantener_no_autorizado`: no cierra Confluencia global, Equivalencia global, `P-107`, `P-200`, promocion de `REPORT_LAYER` ni exportacion general R4/Gamma.
- Saneamiento tecnico reciente: `AUT-002_Decision_Cierre_Tecnico.md` (`D-2026-07-06-010`) cierra tecnicamente el tratamiento de `referencia_historica_transferida`; cualquier dependencia psicologica sustantiva requiere decision puente futura.
- Limpieza reciente: `PSI-TRASPASO-001_Decision_Eliminacion_Copia.md` (`D-2026-07-03-012`) elimina la copia local de traspaso de `PSI-001`; `HB-001_Decision_Congelamiento_Brotes_Alternos.md` (`D-2026-07-03-013`) congela `H-B.6` y `H-B.7` como brotes alternos y originales historicos.
- Decision documental reciente: `DOCS-001_Decision_Consolidacion_Documentos_00-04.md` (`D-2026-07-03-011`) consolida documentos 00-03 desde fuentes previas y actualiza el Documento 04 como version inicial de Algebra Operacional; no promueve Canon ni autoriza transformaciones materiales.
- Decision formal local reciente: `AUD-001_Decision_Cierre_Operativo_v0.md` (`D-2026-07-06-011`) cierra `AUD-001` como version documental/operativa v0; `R4-FORMAL-AUD-001`, `GAMMA-FORMAL-AUD-001`, `REPORT_LAYER` y la suite completa quedan conservados solo en perfil local, sin exportacion general.
- Propuesta provisional promovida: `DO-PROP-001` absorbida por `C-001`.
- Definicion provisional activa: `GAMMA-DEF-001` en `AUD-001_Gamma_Ruta1_Definicion_Local.md`, vigente solo dentro de `AUD-001`; primer caso positivo validado por `VAL-030` contra `AUD-SIM-030`.
- Relacion provisional activa: `REL-GAMMA-R4-001` precisa que `R4-CANDIDATA` puede ser evidencia local para `Gamma_1`, sin equivaler a Regla R4 formal.
- Construcciones formales locales activas: `R4-FORMAL-AUD-001` en `AUD-001_R4_Formal_Local.md` y `GAMMA-FORMAL-AUD-001` en `AUD-001_Gamma_Formal_Local.md`.
- Expediente preparatorio activo: `AO-001` para Algebra Operacional; conserva `AO-PPI-BRIDGE-004` como estado actual local de deudas, `AO-GLOBAL-READINESS-001` como matriz vigente de no autorizacion global, `AO-EXT-EVID-GATE-001` como compuerta preparada y `AO-EXT-REAL-001` como evidencia externa real admitida preliminarmente. El protocolo local, las compuertas de Equivalencia/Confluencia, la promocion de `REPORT_LAYER`, la exportacion R4/Gamma y la admisibilidad externa ya fueron evaluadas o preparadas localmente; cualquier cierre global, promocion o exportacion general requiere decision separada.
- Algoritmo provisional activo: `DO-CHECK-001`; implementaciones activas: `DO-CHECK-MIN-001` en `06_Automatizacion/do_check_min.py`, `DO-CHECK-MED-001` en `06_Automatizacion/do_check_med.py`, `DO-STATE-BOARD-001` en `06_Automatizacion/lab_status_board.py`, `DO-LAB-CONTINUITY-001` en `06_Automatizacion/lab_continuity_report.py`, `DO-LAB-RISK-001` en `06_Automatizacion/lab_risk_classifier.py`, `DO-LAB-SUMMARY-001` en `06_Automatizacion/lab_executive_summary.py`, `DO-LAB-RUN-001` en `06_Automatizacion/lab_run.py`, `R001-TABLE-CHECK-001` en `06_Automatizacion/r001_table_checks.py`, `AO-EXT-CONF-001` en `06_Automatizacion/ao_ext_confluence.py`, `AO-DOC04-WIDE-TEST-001` en `06_Automatizacion/ao_doc04_wide_tests.py`, `AO-PPI-BRIDGE-002` en `06_Automatizacion/ao_ppi_bridge_002.py`, `AO-PPI-BRIDGE-003` en `06_Automatizacion/ao_ppi_bridge_003.py`, `AO-REPORT-SERIAL-001` en `06_Automatizacion/report_layer_serialization.py`, `AO-TCS-REL-001` en `06_Automatizacion/ao_tcs_rel_001.py`, `AO-AUTH-GLOBAL-001` en `06_Automatizacion/ao_authority_global_001.py`, `AO-EXT-COV-001` en `06_Automatizacion/ao_ext_cov_001.py`, `AO-PPI-BRIDGE-004` en `06_Automatizacion/ao_ppi_bridge_004.py`, `AO-GLOBAL-READINESS-001` en `06_Automatizacion/ao_global_readiness_001.py`, `AO-EXT-EVID-GATE-001` en `06_Automatizacion/ao_external_evidence_gate_001.py`, `AO-EXT-REAL-001` como suite real en `06_Automatizacion/fixtures/ao_external_evidence_real_001_manifests.json`, `REPORT-LAYER-C002-GATE-001` en `06_Automatizacion/report_layer_c002_gate.py`, `MOC-EVAL-001` en `06_Automatizacion/moc_eval.py`, `MOC-EXP-GRAPH-CHECK-001` en `06_Automatizacion/moc_experience_graph_001.py`, `MOC-GRAPH-CANON-DOC04-GATE-001` en `06_Automatizacion/moc_exp_graph_authorization_gate_001.py`, `MOC-CANON-DOC04-IMPACT-001` en `06_Automatizacion/moc_canon_doc04_impact_001.py`, `MOC-CANON-DOC04-ADOPT-GATE-001` en `06_Automatizacion/moc_canon_doc04_adopt_gate_001.py` y `MOC-CANON-DOC04-APPLY-001` en `06_Automatizacion/moc_canon_doc04_apply_001.py`.
- Infraestructura `AUT-001` conservada: `AUT-001_Refinamiento_DO-LAB-RISK.md`, `AUT-001_Decision_Cierre_Tecnico_Provisional.md` y `AUT-001_Decision_Cierre_Operativo_Completo.md`; la copia local de traspaso `PSI-001*` fue eliminada del Laboratorio por `D-2026-07-03-012`.
- Documentos oficiales de Nivel C: `C-001_Especificacion_Tecnica_Auditor.md` y `C-002_RFC_Operativo_Auditor_v0.md`.
- Especificacion candidata promovida: `SPEC-AUD-001_Candidata` en `03_Expedientes`.
- Modo operativo del Auditor: mixto, segun `MODO-AUD-001`.
- Proximo objetivo: conservar `AO-GLOBAL-READINESS-001` como matriz vigente de no autorizacion global, `AO-PPI-BRIDGE-004` como estado actual local de deudas, `AO-EXT-EVID-GATE-001` como compuerta preparada de admisibilidad externa y `AO-EXT-REAL-001` como evidencia real admitida preliminarmente. Avanzar solo con decision explicita posterior para reconsiderar readiness global, cierre global, promocion formal de `REPORT_LAYER` o exportacion general R4/Gamma. Mantener `REPORT_LAYER` local pre-C, mantener `global_closure_authorized: false`, `global_export_authorized: false`, `report_layer_promoted: false` y `r4_gamma_global_export_authorized: false`; conservar `MOC-ROUTE-011` como mantenimiento teorico-operativo sin ejecucion y leer `MOC-ROUTE-012` solo como relacion documental local con `C-001` / `C-002`. `PM-001` queda deuda historica condicionada; `P-PI.0` / `P-PI.1` quedan cerrados como frentes de trabajo; `AUT-001`, `AUT-002`, `R001-001`, `AUD-001` y `HXI-001` quedan cerrados; `PSI-001` queda fuera del Laboratorio sin copia local de traspaso; `H-B.6` y `H-B.7` quedan congeladas; `B-001.5` queda congelado; los vision papers quedan inactivos.
- No volver a discutir sin reapertura explicita: `EF-001`, `CP-001`, Procedimiento, Auditoria.

Documentos oficiales consolidados:

- Documento 00: Naturaleza, consolidado desde fuentes previas.
- Documento 01: Canon, consolidado desde fuentes previas.
- Documento 02: Fundamentos Matematicos, consolidado desde fuentes previas.
- Documento 03: Ontologia, consolidado desde fuentes previas.
- Documento 04: Algebra Operacional, actualizado como version amplia v0.

Nota operativa: la consolidacion esta registrada por `D-2026-07-03-011`. Cualquier promocion futura a Canon o Nivel C requiere expediente y decision separada.

Expedientes abiertos relevantes:

- `MOC-001` (expediente integrador teorico-operativo abierto en mantenimiento sin ejecucion; rutas posteriores decididas por `D-2026-07-06-008`, relacion documental local con `C-001` / `C-002` aceptada por `D-2026-07-06-013`, grafo local aceptado por `D-2026-07-09-001`, autorizacion interna preparatoria aceptada por `D-2026-07-09-002`, matriz/propuesta candidata aceptada por `D-2026-07-09-003`, compuerta de incorporacion aceptada por `D-2026-07-09-004` y aplicacion oficial acotada sobre `M-001` y Documento 04 aceptada por `D-2026-07-09-005`; sin ejecucion empirica, no clinico, no regulado)
- `AO-001` (expediente preparatorio abierto para Algebra Operacional; `AO-MARCO-001` incorporado al Documento 04; `GAMMA-EXT-AO-001`, `AO-CASE-BAT-001`, `AO-R4-GAMMA-USE-001`, `AO-PPI-BRIDGE-001`, `AO-PPI-BRIDGE-002`, `AO-PPI-BRIDGE-003`, `AO-REPORT-SERIAL-001`, `AO-TCS-REL-001`, `AO-AUTH-GLOBAL-001`, `AO-EXT-COV-001`, `AO-PPI-BRIDGE-004`, `AO-PPI-LOCAL-CLOSE-001`, `AO-PROTO-INDEP-001`, `AO-EQ-GLOBAL-GATE-001`, `AO-CONF-GLOBAL-GATE-001`, `AO-REPORT-PROMO-GATE-001`, `AO-R4-GAMMA-EXPORT-GATE-002`, `AO-GLOBAL-READINESS-001`, `AO-EXT-INDEP-001`, `AO-EXT-EVID-GATE-001`, `AO-EXT-REAL-001`, `AO-EXT-CONF-EXEC-001`, `AO-DOC04-FORM-001`, `AO-R4-GAMMA-EXPORT-GATE-001`, `AO-DOC04-WIDE-001`, `AO-DOC04-WIDE-TEST-001`, `AO-REPORT-LAYER-BRIDGE-001` y `AO-REPORT-LAYER-NIVEL-C-001` aceptados como avance local no canonico, documental o preparado)
- `TCS-001` (expediente teorico provisional; paquete minimo y maduracion provisional `TCS-MAT-PROV-001` aceptados sin canonizacion)

Expedientes transferidos:

- `PSI-001` (independizado como proyecto `Psicologia Concordante`; copia local de traspaso eliminada por `D-2026-07-03-012`, sin continuidad activa dentro del Laboratorio)

Hipotesis congeladas:

- `H-B.6` (brote alterno y original historico)
- `H-B.7` (brote alterno y original historico)

Problemas abiertos relevantes:

- Maduracion de `MOC-001` en `MOC-ROUTE-011`, mantenimiento teorico-operativo sin ejecucion, con piloto real no autorizado, sin canonizacion y sin dominios clinicos o regulados; `MOC-ROUTE-012` queda como relacion documental local con `C-001` / `C-002`, no como Nivel C ni permiso operativo.
- Confluencia.
- Equivalencia de proyecciones.
- Promocion o exportacion general fuera de `AUD-001` de `R4-FORMAL-AUD-001`.
- Promocion o exportacion general fuera de pruebas locales controladas de `GAMMA-FORMAL-AUD-001`.
- Serializacion interfrente exportable de `REPORT_LAYER` si una decision futura la abre; los casos heterogeneos locales ya quedan ampliados por `D-2026-07-06-018`, sin cerrar problemas globales.
- Maduracion de `TCS-001` mas alla de `TCS-MAT-PROV-001`.
- Relacion global posterior entre `R001-TB-001`, `AO-PPI-BRIDGE-002`, `AO-PPI-BRIDGE-003`, `AO-PPI-BRIDGE-004`, `AO-PPI-LOCAL-CLOSE-001`, Equivalencia global y Confluencia global.
- Evidencia externa independiente real si una decision futura exige mas evidencia para Confluencia o Equivalencia global.

Este estado debe validarse y enriquecerse a medida que se incorporen documentos previos, expedientes completos o conversaciones historicas.

## Candidata aislada de investigación

Se preparó una candidata de investigación y procedencia para
investigacion_empaquetamientos_esfericos_degenerantes/. Su estado es
INCORPORATION_CANDIDATE: no tiene rama, staging, commit, merge o push y no
concede autoridad semántica, canonización ni activación.

La unidad proyectiva N2 queda conservada aquí como procedencia. Su autoridad de
trabajo corresponde a una candidata separada de ConcordIA y no concede al
Laboratorio autoridad semántica MOC.
