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

- Decision operativa reciente: `P-PI_Decision_Reactivacion_Frente_Matematico.md`.
- Decisiones de estabilizacion recientes: `D-2026-07-02-020` a `D-2026-07-02-029`.
- Ultimo expediente cerrado: `AUT-001`; ultimo expediente tecnico cerrado: `AUT-001`.
- Ultima decision arquitectonica: `C-002_RFC_Operativo_Auditor_v0.md` promovido como RFC operativo oficial del Auditor v0; complementa `C-001`.
- Ultima decision operativa: `P-PI_Decision_Reactivacion_Frente_Matematico.md` (`D-2026-07-02-032`) reactiva `P-PI.0` para Equivalencia de proyecciones y `P-PI.1` para Confluencia; `DECISION_Desactivacion_Vision_Papers.md` (`D-2026-07-02-031`) desactiva ambos vision papers.
- Propuesta provisional promovida: `DO-PROP-001` absorbida por `C-001`.
- Algoritmo provisional activo: `DO-CHECK-001`; implementaciones activas: `DO-CHECK-MIN-001` en `06_Automatizacion/do_check_min.py`, `DO-CHECK-MED-001` en `06_Automatizacion/do_check_med.py`, `DO-STATE-BOARD-001` en `06_Automatizacion/lab_status_board.py`, `DO-LAB-CONTINUITY-001` en `06_Automatizacion/lab_continuity_report.py`, `DO-LAB-RISK-001` en `06_Automatizacion/lab_risk_classifier.py`, `DO-LAB-SUMMARY-001` en `06_Automatizacion/lab_executive_summary.py` y `DO-LAB-RUN-001` en `06_Automatizacion/lab_run.py`.
- Infraestructura `AUT-001` conservada: `AUT-001_Refinamiento_DO-LAB-RISK.md`, `AUT-001_Decision_Cierre_Tecnico_Provisional.md` y `AUT-001_Decision_Cierre_Operativo_Completo.md`; mapa PSI: `PSI-001_Mapa_Continuidad_Conceptual.md`; casos PSI: `PSI-001_Casos_Transformacion_No_Clinicos.md`; matriz PSI: `PSI-001_Matriz_Patrones_Transformacion_No_Clinica.md`; auditoria matriz PSI: `PSI-001_Auditoria_Matriz_Patrones_Transformacion_No_Clinica.md`.
- Documentos oficiales de Nivel C: `C-001_Especificacion_Tecnica_Auditor.md` y `C-002_RFC_Operativo_Auditor_v0.md`.
- Especificacion candidata promovida: `SPEC-AUD-001_Candidata` en `03_Expedientes`.
- Modo operativo del Auditor: mixto, segun `MODO-AUD-001`.
- Proximo objetivo: ejecutar `PPI-CONF-001` como primer caso local de Confluencia dentro de `P-PI.1`; `PPI-EQ-001` y `PPI-EQ-002` quedan ejecutados provisionalmente. `AUT-001` queda cerrado operativamente; `HXI-001` queda abierto en pausa operativa; `P-PI.0` y `P-PI.1` quedan activos de forma acotada; `B-001.5` queda congelado; los vision papers quedan inactivos.
- No volver a discutir sin reapertura explicita: `EF-001`, `CP-001`, Procedimiento, Auditoria.

Documentos declarados como completos en el punto de partida:

- Documento 00: completo.
- Documento 01: completo.
- Documento 02: completo.
- Documento 03: completo.

Nota operativa: este repositorio contiene versiones semilla de esos documentos. La completitud anterior debe importarse desde las fuentes previas antes de tratar estos archivos como versiones sustantivas completas.

Expedientes abiertos relevantes:

- `HXI-001` (pausa operativa; reporte de consistencia aceptado sin admision)
- `PSI-001` (abierto; matriz de patrones no clinicos aceptada)
- `P-PI.0` (activo acotado; Equivalencia de proyecciones)
- `P-PI.1` (activo acotado; Confluencia)
- `AUD-001` (completo en version documental/operativa v0; produjo `C-002`; abierto solo para rutas posteriores)

Hipotesis activas iniciales:

- `H-B.6`
- `H-B.7`

Problemas abiertos relevantes:

- Confluencia.
- Equivalencia de proyecciones.
- Definicion formal completa de `R4`.
- Construccion formal de `Gamma`.

Este estado debe validarse y enriquecerse a medida que se incorporen documentos previos, expedientes completos o conversaciones historicas.
