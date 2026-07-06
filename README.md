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

- Decision operativa vigente: `RH-001_Decision_Reconciliacion_PM001.md` (`D-2026-07-06-016`) conserva `PM-001` solo como deuda historica condicionada, sin expediente activo ni protocolo materializado.
- Decisiones de estabilizacion recientes: `D-2026-07-02-020` a `D-2026-07-06-016`.
- Ultimos expedientes cerrados: `HXI-001` y `AUD-001`; ultimos expedientes tecnicos cerrados: `AUT-002` y `R001-001`.
- Ultima decision arquitectonica: `C-002_RFC_Operativo_Auditor_v0.md` promovido como RFC operativo oficial del Auditor v0; complementa `C-001` y quedo alineado el 2026-07-03 con JSON, fixtures y adaptador no mutante.
- Ultimas decisiones operativas: `RH-001_Decision_Reconciliacion_PM001.md` (`D-2026-07-06-016`), `AUT-003_Decision_Herramienta_REPORT_LAYER_C002.md` (`D-2026-07-06-015`), `AO-001_Decision_REPORT_LAYER_Nivel_C.md` (`D-2026-07-06-014`) y `MOC-001_Decision_Relacion_Documental_C001_C002.md` (`D-2026-07-06-013`).
- Avance MOC reciente: `MOC-ROUTE-012` relaciona documentalmente MOC con `C-001` / `C-002`; `C-001` opera como frontera tecnica y `C-002` como secuencia operativa, sin modificar Nivel C ni promover MOC. La ruta vigente sigue siendo `MOC-ROUTE-011`, mantenimiento teorico-operativo sin ejecucion, reclutamiento, respuestas reales, datos personales ni uso clinico.
- Decision teorica reciente: `TCS-001_Decision_Maduracion_Provisional.md` (`D-2026-07-05-010`) acepta `TCS-METRIC-PROV-001`, `TCS-EXT-CASE-001` y `TCS-AUTH-CONF-001`; no canoniza `Concordance`, no crea Nivel C ni usa vision papers como fuente activa.
- Avance AO reciente: `AO-DOC04-WIDE-001` queda aceptado por `D-2026-07-06-006` como formalizacion amplia v0 del Documento 04 y probado localmente por `D-2026-07-06-007`; `REPORT_LAYER` queda precisado por `AO-REPORT-LAYER-BRIDGE-001`, mantenido local pre-C por `D-2026-07-06-014` y cubierto por la compuerta no mutante `REPORT-LAYER-C002-GATE-001` aceptada por `D-2026-07-06-015`. No cierra Confluencia global, Equivalencia global, `P-107`, `P-200` ni exportacion general R4/Gamma.
- Saneamiento tecnico reciente: `AUT-002_Decision_Cierre_Tecnico.md` (`D-2026-07-06-010`) cierra tecnicamente el tratamiento de `referencia_historica_transferida`; cualquier dependencia psicologica sustantiva requiere decision puente futura.
- Limpieza reciente: `PSI-TRASPASO-001_Decision_Eliminacion_Copia.md` (`D-2026-07-03-012`) elimina la copia local de traspaso de `PSI-001`; `HB-001_Decision_Congelamiento_Brotes_Alternos.md` (`D-2026-07-03-013`) congela `H-B.6` y `H-B.7` como brotes alternos y originales historicos.
- Decision documental reciente: `DOCS-001_Decision_Consolidacion_Documentos_00-04.md` (`D-2026-07-03-011`) consolida documentos 00-03 desde fuentes previas y actualiza el Documento 04 como version inicial de Algebra Operacional; no promueve Canon ni autoriza transformaciones materiales.
- Decision formal local reciente: `AUD-001_Decision_Cierre_Operativo_v0.md` (`D-2026-07-06-011`) cierra `AUD-001` como version documental/operativa v0; `R4-FORMAL-AUD-001`, `GAMMA-FORMAL-AUD-001`, `REPORT_LAYER` y la suite completa quedan conservados solo en perfil local, sin exportacion general.
- Propuesta provisional promovida: `DO-PROP-001` absorbida por `C-001`.
- Definicion provisional activa: `GAMMA-DEF-001` en `AUD-001_Gamma_Ruta1_Definicion_Local.md`, vigente solo dentro de `AUD-001`; primer caso positivo validado por `VAL-030` contra `AUD-SIM-030`.
- Relacion provisional activa: `REL-GAMMA-R4-001` precisa que `R4-CANDIDATA` puede ser evidencia local para `Gamma_1`, sin equivaler a Regla R4 formal.
- Construcciones formales locales activas: `R4-FORMAL-AUD-001` en `AUD-001_R4_Formal_Local.md` y `GAMMA-FORMAL-AUD-001` en `AUD-001_Gamma_Formal_Local.md`.
- Expediente preparatorio activo: `AO-001` para Algebra Operacional; `AO-MARCO-001` fue incorporado al Documento 04 como version inicial consolidada, `GAMMA-EXT-AO-001` prueba `Gamma_1` fuera de `AUD-001` en grado local, `AO-CASE-BAT-001` prueba operadores minimos, `AO-R4-GAMMA-USE-001` acota el uso de R4/Gamma fuera de `AUD-001`, `AO-PPI-BRIDGE-001` avanza localmente Confluencia y Equivalencia de proyecciones, `AO-EXT-CONF-EXEC-001` ejecuta dos pruebas externas no reguladas, `AO-DOC04-FORM-001` incorpora `Pi_tb` / `Eq_tb` al Documento 04 en grado acotado, `AO-R4-GAMMA-EXPORT-GATE-001` bloquea la exportacion general de R4/Gamma, `AO-DOC04-WIDE-001` actualiza Documento 04 a version amplia v0, `AO-DOC04-WIDE-TEST-001` prueba esa formalizacion, `AO-REPORT-LAYER-BRIDGE-001` precisa `REPORT_LAYER` y `AO-REPORT-LAYER-NIVEL-C-001` justifica su permanencia local pre-C.
- Algoritmo provisional activo: `DO-CHECK-001`; implementaciones activas: `DO-CHECK-MIN-001` en `06_Automatizacion/do_check_min.py`, `DO-CHECK-MED-001` en `06_Automatizacion/do_check_med.py`, `DO-STATE-BOARD-001` en `06_Automatizacion/lab_status_board.py`, `DO-LAB-CONTINUITY-001` en `06_Automatizacion/lab_continuity_report.py`, `DO-LAB-RISK-001` en `06_Automatizacion/lab_risk_classifier.py`, `DO-LAB-SUMMARY-001` en `06_Automatizacion/lab_executive_summary.py`, `DO-LAB-RUN-001` en `06_Automatizacion/lab_run.py`, `R001-TABLE-CHECK-001` en `06_Automatizacion/r001_table_checks.py`, `AO-EXT-CONF-001` en `06_Automatizacion/ao_ext_confluence.py`, `AO-DOC04-WIDE-TEST-001` en `06_Automatizacion/ao_doc04_wide_tests.py`, `REPORT-LAYER-C002-GATE-001` en `06_Automatizacion/report_layer_c002_gate.py` y `MOC-EVAL-001` en `06_Automatizacion/moc_eval.py`.
- Infraestructura `AUT-001` conservada: `AUT-001_Refinamiento_DO-LAB-RISK.md`, `AUT-001_Decision_Cierre_Tecnico_Provisional.md` y `AUT-001_Decision_Cierre_Operativo_Completo.md`; la copia local de traspaso `PSI-001*` fue eliminada del Laboratorio por `D-2026-07-03-012`.
- Documentos oficiales de Nivel C: `C-001_Especificacion_Tecnica_Auditor.md` y `C-002_RFC_Operativo_Auditor_v0.md`.
- Especificacion candidata promovida: `SPEC-AUD-001_Candidata` en `03_Expedientes`.
- Modo operativo del Auditor: mixto, segun `MODO-AUD-001`.
- Proximo objetivo: profundizar `AO-PPI-BRIDGE-001` hacia Confluencia y Equivalencia global o ampliar `AO-DOC04-WIDE-TEST-001` solo con casos heterogeneos/serializacion de `REPORT_LAYER` si una decision futura lo exige; `REPORT_LAYER` queda local pre-C y cualquier promocion formal o modo mutante requiere decision nueva. Mantener bloqueada la exportacion general de R4/Gamma, conservar `MOC-ROUTE-011` como mantenimiento teorico-operativo sin ejecucion y leer `MOC-ROUTE-012` solo como relacion documental local con `C-001` / `C-002`. `PM-001` queda deuda historica condicionada; `P-PI.0` / `P-PI.1` quedan cerrados como frentes de trabajo; `AUT-001`, `AUT-002`, `R001-001`, `AUD-001` y `HXI-001` quedan cerrados; `PSI-001` queda fuera del Laboratorio sin copia local de traspaso; `H-B.6` y `H-B.7` quedan congeladas; `B-001.5` queda congelado; los vision papers quedan inactivos.
- No volver a discutir sin reapertura explicita: `EF-001`, `CP-001`, Procedimiento, Auditoria.

Documentos oficiales consolidados:

- Documento 00: Naturaleza, consolidado desde fuentes previas.
- Documento 01: Canon, consolidado desde fuentes previas.
- Documento 02: Fundamentos Matematicos, consolidado desde fuentes previas.
- Documento 03: Ontologia, consolidado desde fuentes previas.
- Documento 04: Algebra Operacional, actualizado como version amplia v0.

Nota operativa: la consolidacion esta registrada por `D-2026-07-03-011`. Cualquier promocion futura a Canon o Nivel C requiere expediente y decision separada.

Expedientes abiertos relevantes:

- `MOC-001` (expediente integrador teorico-operativo abierto en mantenimiento sin ejecucion; rutas posteriores decididas por `D-2026-07-06-008` y relacion documental local con `C-001` / `C-002` aceptada por `D-2026-07-06-013`; no Canon, no clinico, no regulado)
- `AO-001` (expediente preparatorio abierto para Algebra Operacional; `AO-MARCO-001` incorporado al Documento 04; `GAMMA-EXT-AO-001`, `AO-CASE-BAT-001`, `AO-R4-GAMMA-USE-001`, `AO-PPI-BRIDGE-001`, `AO-EXT-CONF-EXEC-001`, `AO-DOC04-FORM-001`, `AO-R4-GAMMA-EXPORT-GATE-001`, `AO-DOC04-WIDE-001`, `AO-DOC04-WIDE-TEST-001`, `AO-REPORT-LAYER-BRIDGE-001` y `AO-REPORT-LAYER-NIVEL-C-001` aceptados como avance local no canonico o documental)
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
- Pruebas heterogeneas adicionales de la formalizacion amplia v0 del Documento 04 si una decision futura exige mas cobertura; `AO-DOC04-WIDE-001`, `AO-DOC04-WIDE-TEST-001`, `AO-REPORT-LAYER-BRIDGE-001`, la permanencia local pre-C de `REPORT_LAYER` y la compuerta no mutante `C-002` ya fueron aceptados sin cerrar problemas globales.
- Maduracion de `TCS-001` mas alla de `TCS-MAT-PROV-001`.
- Relacion global posterior entre `R001-TB-001`, Equivalencia global y Confluencia global.
- Pruebas externas adicionales no reguladas si una decision futura exige mas evidencia para Confluencia o Equivalencia global.

Este estado debe validarse y enriquecerse a medida que se incorporen documentos previos, expedientes completos o conversaciones historicas.
