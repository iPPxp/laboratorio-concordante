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

- Decision operativa vigente: `MOC-001_Decision_Paquete_Registro_Auditoria_Piloto.md` (`D-2026-07-06-005`) acepta `MOC-PILOT-REG-AUDIT-PACK-001`; `MOC-ROUTE-010` queda como siguiente ruta recomendada.
- Decisiones de estabilizacion recientes: `D-2026-07-02-020` a `D-2026-07-06-005`.
- Ultimo expediente cerrado: `DOCS-001`; ultimo expediente tecnico cerrado: `AUT-001`.
- Ultima decision arquitectonica: `C-002_RFC_Operativo_Auditor_v0.md` promovido como RFC operativo oficial del Auditor v0; complementa `C-001` y quedo alineado el 2026-07-03 con JSON, fixtures y adaptador no mutante.
- Ultima decision operativa: `MOC-001_Decision_Paquete_Registro_Auditoria_Piloto.md` (`D-2026-07-06-005`) acepta metodo de registro sin datos personales y matriz de auditoria.
- Avance MOC reciente: `MOC-ROUTE-009` prepara paquete documental de registro/auditoria; el piloto empirico real permanece bloqueado.
- Decision teorica reciente: `TCS-001_Decision_Maduracion_Provisional.md` (`D-2026-07-05-010`) acepta `TCS-METRIC-PROV-001`, `TCS-EXT-CASE-001` y `TCS-AUTH-CONF-001`; no canoniza `Concordance`, no crea Nivel C ni usa vision papers como fuente activa.
- Avance AO reciente: `AO-001_Decision_Estatus_Casos_Prueba_Algebra_Operacional.md` (`D-2026-07-03-016`), `AO-001_Decision_Criterios_Uso_R4_Gamma_Fuera_AUD.md` (`D-2026-07-03-017`) y `AO-001_Decision_Estatus_Puente_Confluencia_Equivalencia.md` (`D-2026-07-03-018`) aceptan `AO-CASE-BAT-001`, `AO-R4-GAMMA-USE-001` y `AO-PPI-BRIDGE-001` como avance local no canonico.
- Saneamiento tecnico reciente: `AUT-002_Decision_Referencias_Historicas_Transferidas.md` (`D-2026-07-03-015`) acepta `referencia_historica_transferida` para `PSI-001*` eliminado y refina falsos bloqueos de historial en controles negativos.
- Limpieza reciente: `PSI-TRASPASO-001_Decision_Eliminacion_Copia.md` (`D-2026-07-03-012`) elimina la copia local de traspaso de `PSI-001`; `HB-001_Decision_Congelamiento_Brotes_Alternos.md` (`D-2026-07-03-013`) congela `H-B.6` y `H-B.7` como brotes alternos y originales historicos.
- Decision documental reciente: `DOCS-001_Decision_Consolidacion_Documentos_00-04.md` (`D-2026-07-03-011`) consolida documentos 00-03 desde fuentes previas y actualiza el Documento 04 como version inicial de Algebra Operacional; no promueve Canon ni autoriza transformaciones materiales.
- Decision formal local reciente: `AUD-001_Decision_Estatus_R4_Gamma_Formal_Local.md` (`D-2026-07-03-010`) acepta `R4-FORMAL-AUD-001` y `GAMMA-FORMAL-AUD-001` como construcciones formales locales de `AUD-001`, y `VAL-031` como segunda prueba positiva de `Gamma_1`.
- Propuesta provisional promovida: `DO-PROP-001` absorbida por `C-001`.
- Definicion provisional activa: `GAMMA-DEF-001` en `AUD-001_Gamma_Ruta1_Definicion_Local.md`, vigente solo dentro de `AUD-001`; primer caso positivo validado por `VAL-030` contra `AUD-SIM-030`.
- Relacion provisional activa: `REL-GAMMA-R4-001` precisa que `R4-CANDIDATA` puede ser evidencia local para `Gamma_1`, sin equivaler a Regla R4 formal.
- Construcciones formales locales activas: `R4-FORMAL-AUD-001` en `AUD-001_R4_Formal_Local.md` y `GAMMA-FORMAL-AUD-001` en `AUD-001_Gamma_Formal_Local.md`.
- Expediente preparatorio activo: `AO-001` para Algebra Operacional; `AO-MARCO-001` fue incorporado al Documento 04 como version inicial consolidada, `GAMMA-EXT-AO-001` prueba `Gamma_1` fuera de `AUD-001` en grado local, `AO-CASE-BAT-001` prueba operadores minimos, `AO-R4-GAMMA-USE-001` acota el uso de R4/Gamma fuera de `AUD-001`, `AO-PPI-BRIDGE-001` avanza localmente Confluencia y Equivalencia de proyecciones, `AO-EXT-CONF-EXEC-001` ejecuta dos pruebas externas no reguladas, `AO-DOC04-FORM-001` incorpora `Pi_tb` / `Eq_tb` al Documento 04 en grado acotado y `AO-R4-GAMMA-EXPORT-GATE-001` bloquea la exportacion general de R4/Gamma.
- Algoritmo provisional activo: `DO-CHECK-001`; implementaciones activas: `DO-CHECK-MIN-001` en `06_Automatizacion/do_check_min.py`, `DO-CHECK-MED-001` en `06_Automatizacion/do_check_med.py`, `DO-STATE-BOARD-001` en `06_Automatizacion/lab_status_board.py`, `DO-LAB-CONTINUITY-001` en `06_Automatizacion/lab_continuity_report.py`, `DO-LAB-RISK-001` en `06_Automatizacion/lab_risk_classifier.py`, `DO-LAB-SUMMARY-001` en `06_Automatizacion/lab_executive_summary.py`, `DO-LAB-RUN-001` en `06_Automatizacion/lab_run.py`, `R001-TABLE-CHECK-001` en `06_Automatizacion/r001_table_checks.py`, `AO-EXT-CONF-001` en `06_Automatizacion/ao_ext_confluence.py` y `MOC-EVAL-001` en `06_Automatizacion/moc_eval.py`.
- Infraestructura `AUT-001` conservada: `AUT-001_Refinamiento_DO-LAB-RISK.md`, `AUT-001_Decision_Cierre_Tecnico_Provisional.md` y `AUT-001_Decision_Cierre_Operativo_Completo.md`; la copia local de traspaso `PSI-001*` fue eliminada del Laboratorio por `D-2026-07-03-012`.
- Documentos oficiales de Nivel C: `C-001_Especificacion_Tecnica_Auditor.md` y `C-002_RFC_Operativo_Auditor_v0.md`.
- Especificacion candidata promovida: `SPEC-AUD-001_Candidata` en `03_Expedientes`.
- Modo operativo del Auditor: mixto, segun `MODO-AUD-001`.
- Proximo objetivo: ejecutar `MOC-ROUTE-010`, decidiendo rutas posteriores despues del paquete de registro/auditoria sin reclutamiento, sin respuestas reales, sin datos personales y sin uso clinico; conservar `AO-DOC04-FORM-001` como formalizacion acotada de `Pi_tb` / `Eq_tb`, continuar Confluencia global y Equivalencia global de proyecciones desde `AO-PPI-BRIDGE-001`, mantener bloqueada la exportacion general de R4/Gamma y madurar `TCS-001` desde `TCS-MAT-PROV-001`. `P-PI.0` / `P-PI.1` quedan cerrados como frentes de trabajo; `AUT-001` queda cerrado operativamente; `HXI-001` queda abierto en mantenimiento local; `PSI-001` queda fuera del Laboratorio sin copia local de traspaso; `H-B.6` y `H-B.7` quedan congeladas; `B-001.5` queda congelado; los vision papers quedan inactivos.
- No volver a discutir sin reapertura explicita: `EF-001`, `CP-001`, Procedimiento, Auditoria.

Documentos oficiales consolidados:

- Documento 00: Naturaleza, consolidado desde fuentes previas.
- Documento 01: Canon, consolidado desde fuentes previas.
- Documento 02: Fundamentos Matematicos, consolidado desde fuentes previas.
- Documento 03: Ontologia, consolidado desde fuentes previas.
- Documento 04: Algebra Operacional, actualizado como version inicial consolidada.

Nota operativa: la consolidacion esta registrada por `D-2026-07-03-011`. Cualquier promocion futura a Canon o Nivel C requiere expediente y decision separada.

Expedientes abiertos relevantes:

- `MOC-001` (expediente integrador teorico-operativo; primera ruta valida, ruta 002, puente formal `MOC/TCS`, puente formal `MOC/AO`, protocolo v0.2, protocolo documental de piloto futuro, compuerta de no autorizacion, paquete pre-ejecucion, paquete de registro/auditoria y rutas siguientes aceptadas por `D-2026-07-05-016` a `D-2026-07-06-005`; no Canon, no clinico, no regulado)
- `HXI-001` (abierto en mantenimiento local; conserva `Xi_eval`; `H-Xi` no admitida)
- `R001-001` (integracion tecnica provisional de `R001-TABLE-CHECK-001` y relacion formal local `R001-TB-001`; no canoniza `Xi`, no admite `H-Xi`, no cierra `P-200` ni resuelve `P-107`)
- `AUD-001` (completo en version documental/operativa v0; implementacion no mutante `AUDITOR-V0-001` aceptada; JSON reactivado; `REPORT_LAYER` local y compatibilidad con `DO_CHECK_REPORT` definidas; origen local de `REPORT_LAYER` fijado en `AUD-001_Origen_REPORT_LAYER.md`; suite ejecutable completa encuadrada en `AUD-001_Ficha_Alcance_Suite_Ejecutable_Completa.md`; parser real acotado en `AUD-001_Ficha_Alcance_Parser_Real.md`; R4 formal local construido en `AUD-001_R4_Formal_Local.md`; Gamma formal local construido en `AUD-001_Gamma_Formal_Local.md`; `Gamma_1` probado por `VAL-030`, `VAL-031` y `GAMMA-EXT-AO-001`)
- `AO-001` (expediente preparatorio abierto para Algebra Operacional; `AO-MARCO-001` incorporado al Documento 04; `GAMMA-EXT-AO-001`, `AO-CASE-BAT-001`, `AO-R4-GAMMA-USE-001`, `AO-PPI-BRIDGE-001`, `AO-EXT-CONF-EXEC-001`, `AO-DOC04-FORM-001` y `AO-R4-GAMMA-EXPORT-GATE-001` aceptados como avance local no canonico o documental acotado)
- `TCS-001` (expediente teorico provisional; paquete minimo y maduracion provisional `TCS-MAT-PROV-001` aceptados sin canonizacion)

Expedientes transferidos:

- `PSI-001` (independizado como proyecto `Psicologia Concordante`; copia local de traspaso eliminada por `D-2026-07-03-012`, sin continuidad activa dentro del Laboratorio)

Hipotesis congeladas:

- `H-B.6` (brote alterno y original historico)
- `H-B.7` (brote alterno y original historico)

Problemas abiertos relevantes:

- Maduracion de `MOC-001` por `MOC-ROUTE-010`, rutas posteriores despues del paquete de registro/auditoria, con ejecucion real no autorizada, sin canonizacion y sin dominios clinicos o regulados.
- Confluencia.
- Equivalencia de proyecciones.
- Promocion o exportacion general fuera de `AUD-001` de `R4-FORMAL-AUD-001`.
- Promocion o exportacion general fuera de pruebas locales controladas de `GAMMA-FORMAL-AUD-001`.
- Formalizacion posterior amplia del Documento 04 - Algebra Operacional; `Pi_tb` / `Eq_tb` ya fue incorporado solo en grado acotado.
- Maduracion de `TCS-001` mas alla de `TCS-MAT-PROV-001`.
- Relacion global posterior entre `R001-TB-001`, Equivalencia global y Confluencia global.
- Pruebas externas adicionales no reguladas si una decision futura exige mas evidencia para Confluencia o Equivalencia global.

Este estado debe validarse y enriquecerse a medida que se incorporen documentos previos, expedientes completos o conversaciones historicas.
