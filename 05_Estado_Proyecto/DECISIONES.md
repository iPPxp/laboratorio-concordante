# Decisiones

Este archivo registra decisiones operativas y arquitectonicas del Laboratorio Concordante.

## D-2026-07-01-001 - Instanciacion fisica del repositorio local

Estatus: decision operativa.

Fecha: 2026-07-01.

## Decision

Se registra oficialmente la instanciacion fisica del Laboratorio Concordante como estructura local de archivos auditable y operativa.

## Alcance

La decision cubre:

- existencia local de la estructura de carpetas
- separacion entre Canon, Documentos, Expedientes, Registro Historico y Estado del Proyecto
- uso de archivos Markdown como superficie primaria de trabajo
- normalizacion ASCII como criterio de interoperabilidad textual

## No cubre

La decision no cubre todavia:

- inicializacion Git
- repositorio remoto
- versionado formal por commits
- automatizacion ejecutable del Auditor
- promocion de expedientes a documentos oficiales

## Consecuencia

El Laboratorio deja de depender de una conversacion como soporte primario y pasa a operar sobre un repositorio local estructurado.

## Dependencias o referencias mencionadas no materializadas

Las siguientes referencias fueron mencionadas como contexto, pero aun no existen como archivos locales en este repositorio:

- `ROADMAP.md`
- Canon v0.1
- Decalogo
- Regla VII del Decalogo
- Nivel C - Especificaciones (materializado por `D-2026-07-01-002`)
- Regla R4
- Generalizacion Gamma

Hasta que sean importadas o formalizadas, deben tratarse como deuda conceptual y no como autoridad local vigente.

## D-2026-07-01-002 - Definicion local de Nivel C - Especificaciones

Estatus: decision arquitectonica local.

Fecha: 2026-07-01.

## Decision

Se define localmente `Nivel C - Especificaciones` mediante `NIVEL-C-001` en `05_Estado_Proyecto/NIVEL_C_ESPECIFICACIONES.md`.

Nivel C queda establecido como subnivel documental para especificaciones tecnicas oficiales, subordinado al Canon, a `M-000`, a `M-001` y a los documentos oficiales de marco general.

## Alcance

La decision cubre:

- diferencia entre especificacion candidata y especificacion tecnica oficial
- ubicacion provisional de candidatas en `03_Expedientes`
- ubicacion inicial permitida de especificaciones oficiales en `02_Documentos`
- requisitos minimos de promocion
- contenido permitido y prohibido en Nivel C
- aplicacion inicial a `SPEC-AUD-001_Candidata`

## No cubre

La decision no cubre todavia:

- promocion efectiva de `SPEC-AUD-001_Candidata`
- creacion de una especificacion oficial del Auditor en `02_Documentos`
- definicion formal completa de `R4`
- construccion formal de `Gamma`
- implementacion ejecutable completa del Auditor

## Consecuencia

`Nivel C - Especificaciones` deja de ser dependencia no materializada.

La siguiente accion valida es auditar `SPEC-AUD-001_Candidata` contra `NIVEL-C-001` antes de decidir cualquier promocion oficial.

## D-2026-07-01-003 - Promocion de SPEC-AUD-001 a C-001

Estatus: decision documental de Nivel C.

Fecha: 2026-07-01.

## Decision

Se promueve `SPEC-AUD-001_Candidata` a documento oficial de Nivel C como `02_Documentos/C-001_Especificacion_Tecnica_Auditor.md`.

## Alcance

La decision cubre:

- creacion del documento oficial `C-001`
- reconocimiento de `SPEC-AUD-001_Candidata` como fuente promovida
- cierre inicial del problema abierto `Especificacion tecnica del Auditor`
- conservacion de deudas fuera de alcance

## No cubre

La decision no cubre:

- implementacion ejecutable completa del Auditor
- definicion formal completa de `R4`
- construccion formal de `Gamma`
- transformaciones no triviales
- reversion real o cuarentena materializada
- cierre automatico de `DO-001` o `AUD-001`

## Consecuencia

`C-001` queda como referencia oficial inicial para el diseno y auditoria del Auditor.

La siguiente accion valida es decidir si `DO-001` se cierra o continua hacia implementacion y pruebas adicionales.

## D-2026-07-01-004 - Cierre de DO-001

Estatus: decision de cierre de expediente.

Fecha: 2026-07-01.

## Decision

Se cierra `DO-001` como expediente de diseno de automatizacion.

## Alcance

La decision cubre:

- cierre de `DO-001`
- reconocimiento de `C-001` como resultado oficial del expediente
- traslado del foco operativo a `AUD-001`

## No cubre

La decision no cubre:

- cierre de `AUD-001`
- implementacion ejecutable completa del Auditor
- definicion formal de `R4`
- construccion formal de `Gamma`
- validaciones adicionales de contratos del Auditor

## Consecuencia

El siguiente objetivo pasa a `AUD-001`: validar `MP_FAIL_REPORT` contra fallas adicionales de `Mp`.

## D-2026-07-01-005 - Seleccion de B-001.5 como siguiente frente activo

Estatus: decision operativa de prioridad.

Fecha: 2026-07-01.

## Decision

Se elige `B-001.5` como siguiente frente activo inmediato para clasificacion operativa.

## Alcance

La decision cubre solo la prioridad de trabajo: clasificar `B-001.5` como abierto, congelado, absorbido o cerrado.

## No cubre

La decision no clasifica todavia `B-001.5`, no reabre expedientes cerrados y no modifica Canon ni documentos oficiales.

## Consecuencia

El siguiente objetivo pasa a `B-001.5`: decidir su clasificacion operativa.

## D-2026-07-01-006 - Clasificacion de B-001.5

Estatus: decision de clasificacion de expediente.

Fecha: 2026-07-01.

## Decision

Se clasifica `B-001.5` como expediente congelado.

## Alcance

La decision retira `B-001.5` de pendientes de clasificacion y conserva su traza local sin abrir trabajo sustantivo.

## No cubre

La decision no cierra `B-001.5`, no lo absorbe en `B-001`, no reabre `B-001` y no modifica Canon ni documentos oficiales.

## Consecuencia

El siguiente objetivo vuelve a elegir un frente activo del Laboratorio desde deudas de alto nivel.

## D-2026-07-01-007 - Seleccion de P-PI como siguiente frente activo

Estatus: decision operativa de prioridad.

Fecha: 2026-07-01.

## Decision

Se elige `P-PI.0` / `P-PI.1` como siguiente frente activo inmediato para definir criterios de cierre.

## Alcance

La decision cubre solo la prioridad de trabajo: definir criterios de cierre para ambos expedientes.

## No cubre

La decision no cierra `P-PI.0` ni `P-PI.1`, no resuelve confluencia ni equivalencia de proyecciones y no modifica Canon ni documentos oficiales.

## Consecuencia

El siguiente objetivo pasa a `P-PI.0` / `P-PI.1`: definir criterios de cierre.

## D-2026-07-01-008 - Criterios de cierre P-PI

Estatus: registro operativo de criterios.

Fecha: 2026-07-01.

## Registro

Se registra `03_Expedientes/P-PI_Criterios_Cierre.md` como criterios provisionales de cierre para `P-PI.0` y `P-PI.1`.

## Alcance

El registro cubre criterios para cierre, pausa, congelamiento, absorcion o continuidad abierta.

## No cubre

No cierra `P-PI.0` ni `P-PI.1`, no resuelve Confluencia ni Equivalencia de proyecciones y no modifica Canon ni documentos oficiales.

## Consecuencia

El siguiente objetivo pasa a auditar `P-PI_Criterios_Cierre.md` contra `M-000` y `M-001`.

## D-2026-07-01-009 - Auditoria de criterios de cierre P-PI

Estatus: registro operativo de auditoria.

Fecha: 2026-07-01.

## Registro

Se registra `03_Expedientes/P-PI_Auditoria_Criterios_Cierre.md` como auditoria favorable de `P-PI_Criterios_Cierre.md` contra `M-000` y `M-001`.

## Alcance

La auditoria cubre coherencia de criterios, separacion de niveles, trazabilidad, deudas y no promocion automatica.

## No cubre

No cierra `P-PI.0` ni `P-PI.1`, no resuelve Confluencia ni Equivalencia de proyecciones y no modifica Canon ni documentos oficiales.

## Consecuencia

El siguiente objetivo pasa a decidir estatus de `P-PI_Criterios_Cierre.md` como compuerta provisional de expediente.

## D-2026-07-01-010 - Estatus de criterios de cierre P-PI

Estatus: decision provisional de expediente.

Fecha: 2026-07-01.

## Decision

Se acepta `P-PI_Criterios_Cierre.md` como compuerta provisional de expediente.

## Alcance

La decision permite usar los criterios para decidir ruta operativa de `P-PI.0` y `P-PI.1`.

## No cubre

La decision no cierra, pausa, congela ni absorbe `P-PI.0` o `P-PI.1`, no resuelve Confluencia ni Equivalencia de proyecciones y no modifica Canon ni documentos oficiales.

## Consecuencia

El siguiente objetivo pasa a decidir ruta operativa de `P-PI.0` y `P-PI.1` usando la compuerta aceptada.

## D-2026-07-01-011 - Ruta operativa P-PI

Estatus: decision provisional de expediente.

Fecha: 2026-07-01.

## Decision

`P-PI.0` y `P-PI.1` quedan abiertos en pausa operativa.

## Alcance

La decision conserva ambos expedientes como trazas abiertas, retira el frente P-PI de la ejecucion inmediata y mantiene Confluencia y Equivalencia de proyecciones como problemas abiertos.

## No cubre

La decision no cierra, congela ni absorbe `P-PI.0` o `P-PI.1`, no resuelve Confluencia ni Equivalencia de proyecciones y no modifica Canon ni documentos oficiales.

## Consecuencia

El siguiente objetivo vuelve a elegir un frente activo del Laboratorio desde deudas de alto nivel.
## D-2026-07-01-012 - Cierre de RH-001

Estatus: decision provisional de expediente.

Fecha: 2026-07-01.

## Decision

Se cierra `RH-001` como expediente de procesamiento de registro historico.

## Alcance

La decision cubre:

- procesamiento local de `04_Registro_Historico/2026-07-01_chatgpt_share_001_transcripcion.md`
- clasificacion del contenido historico como incorporado, deuda condicionada, material sin soporte local, recomendacion superada o fuera de alcance
- retiro de la deuda general de materializacion y procesamiento de esa transcripcion
- conservacion de deudas condicionadas derivadas de `RH-001`

## No cubre

La decision no cubre:

- promocion de contenido historico a Canon
- modificacion de documentos oficiales
- reapertura de expedientes cerrados o en pausa
- apertura automatica de Documento 04, Concordancia, Protocolo de Admision o arquitectura multiagente
- uso de adjuntos historicos no materializados como evidencia

## Consecuencia

`RH-001` queda como ultimo expediente cerrado de procesamiento historico.

El siguiente objetivo del Laboratorio permanece: elegir siguiente frente activo desde deudas de alto nivel.

## D-2026-07-01-013 - Estatus MVP minimo de AUT-001

Estatus: decision provisional de expediente.

Fecha: 2026-07-01.

## Decision

Se acepta `DO-CHECK-MIN-001` en `06_Automatizacion/do_check_min.py` como automatizacion minima provisional del Laboratorio.

## Alcance

La decision cubre la existencia de una herramienta no mutante que lee archivos Markdown y conserva reportes en `06_Automatizacion/reportes`.

## No cubre

La decision no cierra `AUT-001`, no equivale a automatizacion media o completa, no autoriza transformaciones y no sustituye la validacion directa local de ejecucion con `python`.

## Consecuencia

El siguiente objetivo recomendado es validar ejecucion directa local de la herramienta cuando el entorno lo permita y despues elegir si avanzar a psicologia u otro frente.

## D-2026-07-01-014 - Cierre de RH-002

Estatus: decision provisional de expediente.

Fecha: 2026-07-01.

## Decision

Se cierra `RH-002` como expediente de procesamiento del lote historico de Descargas.

## Alcance

La decision cubre la materializacion local de los 23 archivos declarados por el usuario, el manifiesto verificable, las extracciones textuales seguras, el listado de zips, la preservacion de binarios sin ejecucion y la clasificacion de deudas condicionadas.

## No cubre

La decision no adopta Canon historico como Canon vigente, no reconcilia baselines, no canoniza `H-Xi`, no abre automaticamente psicologia, no modifica documentos oficiales y no cierra `AUT-001`.

## Consecuencia

El siguiente objetivo recomendado es escoger conscientemente entre reconciliacion Canon/baselines, admision de `H-Xi`, Protocolo de Admision/Concordancia, validacion directa de automatizacion minima o psicologia.

## D-2026-07-01-015 - Cierre de REC-001

Estatus: decision provisional de expediente.

Fecha: 2026-07-01.

## Decision

Se cierra `REC-001` como reconciliacion inicial de Canon y baselines historicos.

## Alcance

La decision cubre la comparacion y clasificacion de `M-000 v0.1`, baseline `v1.0.0`, paquete `v1.0.0-fase2` y paquete `v1.5` contra el workspace vigente.

## No cubre

La decision no modifica Canon, no modifica documentos oficiales, no adopta `v1.5` como estado vigente, no ejecuta codigo historico y no abre psicologia.

## Consecuencia

La deuda amplia de reconciliacion queda reemplazada por deudas refinadas: gobierno vs nucleo matematico, reglas metodologicas historicas, AAU historico, GDI/R4/Gamma y admision de hipotesis como `H-Xi`.

## D-2026-07-01-016 - Fase media de AUT-001

Estatus: decision provisional de expediente.

Fecha: 2026-07-01.

## Decision

Se acepta `DO-CHECK-MED-001` en `06_Automatizacion/do_check_med.py` como automatizacion media provisional no mutante del Laboratorio.

## Alcance

La decision cubre el mapa funcional con AAU historico, controles medios de lectura, reportes conservados y reduccion operativa inicial de `REC-DEUDA-003`.

## No cubre

La decision no cierra `AUT-001`, no confirma ejecucion directa local con `python`, no autoriza transformaciones, no modifica Canon ni documentos oficiales, no cierra o reabre expedientes y no abre psicologia automaticamente.

## Consecuencia

`AUT-001` queda abierto con MVP minimo y fase media provisional. El siguiente paso recomendado es validar ejecucion directa local de `do_check_med.py` y decidir si esta compuerta basta para abrir psicologia.

## D-2026-07-01-017 - Apertura de PSI-001

Estatus: decision provisional de expediente.

Fecha: 2026-07-01.

## Decision

Se abre `PSI-001` como frente psicologico inicial del Laboratorio Concordante.

La fase media de `AUT-001` se considera compuerta provisional suficiente para abrir un expediente conceptual no mutante, aunque la ejecucion directa local de `do_check_med.py` siga pendiente.

## Alcance

La decision cubre apertura de expediente, registro de `A-PSI-001` como axioma candidato y criterios iniciales de admision.

## No cubre

No canoniza `A-PSI-001`, no admite `H-Xi`, `P-107` ni Concordancia, no modifica Canon o documentos oficiales, no ofrece diagnostico o tratamiento y no cierra `AUT-001`.

## Consecuencia

`PSI-001` queda como expediente activo inmediato. La siguiente accion valida es auditar `A-PSI-001` contra `PSI-001_Criterios_Admision.md`.

## D-2026-07-01-018 - Estatus de A-PSI-001

Estatus: decision provisional de expediente.

Fecha: 2026-07-01.

## Decision

Se acepta `A-PSI-001` como axioma candidato operativo dentro de `PSI-001`.

## Alcance

La decision permite usarlo como punto de partida para la primera ronda conceptual del frente psicologico.

## No cubre

No canoniza el axioma, no modifica documentos oficiales, no admite `H-Xi`, `P-107` ni Concordancia, no ofrece diagnostico o tratamiento y no resuelve el problema de la conciencia.

## Consecuencia

El siguiente objetivo es definir provisionalmente `organizacion de la experiencia psicologica` dentro de `PSI-001`.

## D-2026-07-01-019 - Estatus de definicion de organizacion psicologica

Estatus: decision provisional de expediente.

Fecha: 2026-07-01.

## Decision

Se acepta `DEF-PSI-ORG-001` como definicion provisional operativa de `organizacion de la experiencia psicologica` dentro de `PSI-001`.

## Alcance

La decision permite distinguir contenido, estructura y organizacion; formular ejemplos conceptuales no clinicos; y preparar criterios de transformacion, reorganizacion, desorganizacion y disolucion.

## No cubre

No canoniza la definicion, no modifica documentos oficiales, no cierra `PSI-001`, no admite `H-Xi`, `P-107` ni Concordancia, no ofrece diagnostico o tratamiento y no autoriza transformaciones materiales.

## Consecuencia

El siguiente objetivo es definir el criterio local que diferencia transformacion, reorganizacion, desorganizacion y disolucion de la experiencia psicologica dentro de `PSI-001`.

## D-2026-07-01-020 - Estatus de criterio de transformacion psicologica

Estatus: decision provisional de expediente.

Fecha: 2026-07-01.

## Decision

Se acepta `CRIT-PSI-TR-001` como criterio provisional operativo para diferenciar `transformacion`, `reorganizacion`, `desorganizacion` y `disolucion` de la experiencia psicologica dentro de `PSI-001`.

## Alcance

La decision permite comparar estados conceptuales `E0` y `E1`, clasificar cambios dentro de `PSI-001` y crear ejemplos conceptuales no clinicos para probar `DEF-PSI-ORG-001`.

## No cubre

No canoniza el criterio, no modifica documentos oficiales, no cierra `PSI-001`, no admite `H-Xi`, `P-107` ni Concordancia, no evalua personas o casos personales reales y no ofrece diagnostico o tratamiento.

## Consecuencia

El siguiente objetivo es crear ejemplos conceptuales no clinicos para probar `DEF-PSI-ORG-001` y `CRIT-PSI-TR-001` dentro de `PSI-001`.

## D-2026-07-02-001 - Estatus de ejemplos conceptuales PSI

Estatus: decision provisional de expediente.

Fecha: 2026-07-02.

## Decision

Se acepta `EX-PSI-001` a `EX-PSI-005` como bateria conceptual provisional no clinica dentro de `PSI-001`.

## Alcance

La decision permite usar los ejemplos para probar `DEF-PSI-ORG-001`, probar `CRIT-PSI-TR-001`, distinguir cambio de contenido, reorganizacion, desorganizacion, disolucion y resultado `no auditable`.

## No cubre

No canoniza los ejemplos, no modifica documentos oficiales, no cierra `PSI-001`, no admite `H-Xi`, `P-107` ni Concordancia, no evalua personas o casos personales reales y no ofrece diagnostico o tratamiento.

## Consecuencia

El siguiente objetivo es decidir si se abre una evaluacion separada sobre la relacion entre `H-Xi` y los cambios de relaciones `R` usados por `CRIT-PSI-TR-001`.

## D-2026-07-02-002 - Apertura de evaluacion HXI-001

Estatus: decision provisional de expediente.

Fecha: 2026-07-02.

## Decision

Se abre `HXI-001` como evaluacion separada de la relacion entre `H-Xi` y los cambios de relaciones `R` usados por `CRIT-PSI-TR-001`.

## Alcance

La decision permite evaluar si distincion/restriccion aporta a la formalizacion de cambios de `R`, usar `EX-PSI-001` a `EX-PSI-005` como bateria conceptual no clinica y auditar `HXI-001_Mapa_Preliminar_PSI-R.md` contra `HXI-001_Criterios_Evaluacion.md`.

## No cubre

No admite `H-Xi`, no canoniza `Xi`, no modifica documentos oficiales, no cierra `PSI-001`, no resuelve `P-107`, no reconstruye el sistema desde `Xi`, no ofrece diagnostico o tratamiento y no autoriza transformaciones materiales.

## Consecuencia

El siguiente objetivo es auditar `HXI-001_Mapa_Preliminar_PSI-R.md` contra `HXI-001_Criterios_Evaluacion.md`.

## D-2026-07-02-003 - Estatus de mapa preliminar HXI-001

Estatus: decision provisional de expediente.

Fecha: 2026-07-02.

## Decision

Se acepta `HXI-001_Mapa_Preliminar_PSI-R.md` como mapa preliminar operativo dentro de `HXI-001`.

## Alcance

La decision permite usar el mapa como guia para pruebas `H-Xi` / `R`, construir una matriz sobre `EX-PSI-001` a `EX-PSI-005` y evaluar utilidad, redundancia, insuficiencia o prematuridad de `Xi`.

## No cubre

No admite `H-Xi`, no canoniza `Xi`, no modifica documentos oficiales, no cierra `PSI-001`, no resuelve `P-107`, no reconstruye el sistema desde `Xi`, no ofrece diagnostico o tratamiento y no autoriza transformaciones materiales.

## Consecuencia

El siguiente objetivo es crear una matriz de pruebas `HXI-R` sobre `EX-PSI-001` a `EX-PSI-005`.

## D-2026-07-02-004 - Estatus de matriz HXI-R

Estatus: decision provisional de expediente.

Fecha: 2026-07-02.

## Decision

Se acepta `HXI-001_Matriz_Pruebas_HXI-R.md` como matriz provisional operativa dentro de `HXI-001`.

## Alcance

La decision permite usar la matriz para redactar un dictamen de utilidad local de `Xi`, mantener `HXI-001` abierto y conservar `H-Xi` como hipotesis externa no admitida.

## No cubre

No admite `H-Xi`, no canoniza `Xi`, no modifica documentos oficiales, no cierra `PSI-001`, no resuelve `P-107`, no reconstruye el sistema desde `Xi`, no ofrece diagnostico o tratamiento y no autoriza transformaciones materiales.

## Consecuencia

El siguiente objetivo es redactar un dictamen de utilidad local de `Xi` dentro de `HXI-001`, usando la matriz `HXI-R` como base.

## D-2026-07-02-005 - Estatus de dictamen de utilidad local Xi

Estatus: decision provisional de expediente.

Fecha: 2026-07-02.

## Decision

Se acepta `HXI-001_Dictamen_Utilidad_Local_Xi.md` como dictamen provisional operativo dentro de `HXI-001`.

## Alcance

La decision reconoce utilidad local acotada de `Xi` para reorganizacion relacional estable y permite usar el dictamen para decidir ruta operativa de `HXI-001`.

## No cubre

No admite `H-Xi`, no canoniza `Xi`, no declara `Xi` operador vigente, no modifica documentos oficiales, no cierra `PSI-001`, no resuelve `P-107`, no reconstruye el sistema desde `Xi`, no ofrece diagnostico o tratamiento y no autoriza transformaciones materiales.

## Consecuencia

El siguiente objetivo es decidir ruta de `HXI-001` tras el dictamen: pausa operativa, continuidad acotada con notacion minima o preparacion de admision formal posterior con criterios separados.

## D-2026-07-02-006 - Ruta operativa HXI-001

Estatus: decision provisional de expediente.

Fecha: 2026-07-02.

## Decision

Se elige la ruta 2 para `HXI-001`: continuidad acotada con notacion minima de expediente.

## Alcance

La decision permite crear y usar una notacion minima local para `Xi-R`, aplicar esa notacion a la matriz `HXI-R` y mantener `H-Xi` como hipotesis externa no admitida.

## No cubre

No admite `H-Xi`, no canoniza `Xi`, no declara `Xi` operador vigente, no modifica documentos oficiales, no cierra `PSI-001`, no resuelve `P-107`, no ofrece diagnostico o tratamiento y no autoriza transformaciones materiales.

## Consecuencia

La accion inmediata es crear, auditar y decidir estatus de `HXI-001_Notacion_Minima_Xi-R.md`.

## D-2026-07-02-007 - Estatus de notacion minima Xi-R

Estatus: decision provisional de expediente.

Fecha: 2026-07-02.

## Decision

Se acepta `HXI-001_Notacion_Minima_Xi-R.md` como notacion provisional operativa dentro de `HXI-001`.

## Alcance

La decision permite usar `Xi_eval(R0, R1)` y las salidas `redundante`, `util_acotado`, `limitado`, `no_comparable` y `bloqueado` para aplicar el dictamen local a la matriz `HXI-R`.

## No cubre

No admite `H-Xi`, no canoniza `Xi`, no declara `Xi` operador vigente, no modifica documentos oficiales, no cierra `PSI-001`, no resuelve `P-107`, no ofrece diagnostico o tratamiento y no autoriza transformaciones materiales.

## Consecuencia

El siguiente objetivo es aplicar la notacion minima `Xi-R` a `HXI-R-001` a `HXI-R-005` en un reporte de consistencia.

## D-2026-07-02-008 - Preparacion de admision formal H-Xi

Estatus: decision provisional de expediente.

Fecha: 2026-07-02.

## Decision

Se habilita la preparacion de admision formal posterior de `H-Xi` como ruta condicionada dentro de `HXI-001`.

## Alcance

La decision permite redactar criterios separados de admision formal, exigir pruebas previas y mantener separada la utilidad local de cualquier admision futura.

## No cubre

No admite `H-Xi`, no canoniza `Xi`, no declara `Xi` operador vigente, no modifica Canon ni documentos oficiales, no cierra `PSI-001`, no resuelve `P-107`, no ofrece diagnostico o tratamiento y no autoriza transformaciones materiales.

## Consecuencia

La accion inmediata es crear y auditar `HXI-001_Criterios_Admision_Formal_H-Xi.md`.

## D-2026-07-02-009 - Estatus de criterios de admision formal H-Xi

Estatus: decision provisional de expediente.

Fecha: 2026-07-02.

## Decision

Se acepta `HXI-001_Criterios_Admision_Formal_H-Xi.md` como compuerta provisional de admision formal posterior dentro de `HXI-001`.

## Alcance

La decision permite usar los criterios para una evaluacion futura de admision, exige reporte de consistencia previo y conserva `H-Xi` como hipotesis externa mientras no exista decision posterior.

## No cubre

No admite `H-Xi`, no canoniza `Xi`, no declara `Xi` operador vigente, no modifica Canon ni documentos oficiales, no cierra `PSI-001`, no resuelve `P-107`, no ofrece diagnostico o tratamiento y no autoriza transformaciones materiales.

## Consecuencia

El siguiente objetivo operativo sigue siendo aplicar la notacion minima `Xi-R` a `HXI-R-001` a `HXI-R-005` en un reporte de consistencia, requisito previo para cualquier admision formal posterior.

## D-2026-07-02-010 - Estatus de reporte de consistencia Xi-R

Estatus: decision provisional de expediente.

Fecha: 2026-07-02.

## Decision

Se acepta `HXI-001_Reporte_Consistencia_Notacion_Xi-R.md` como reporte provisional operativo dentro de `HXI-001`.

## Alcance

La decision registra que `Xi_eval(R0, R1)` produce salidas consistentes para `HXI-R-001` a `HXI-R-005` y cumple el requisito de reporte de consistencia previo a cualquier admision formal posterior.

## No cubre

No admite `H-Xi`, no canoniza `Xi`, no declara `Xi` operador vigente, no modifica Canon ni documentos oficiales, no cierra `PSI-001`, no resuelve `P-107`, no ofrece diagnostico o tratamiento y no autoriza transformaciones materiales.

## Consecuencia

El siguiente objetivo es decidir el tipo de evaluacion posterior: mantener solo `Xi_eval`, evaluar admision solo de expediente, pausar admision o abrir evaluacion formal separada.

## D-2026-07-02-011 - Pausa operativa HXI-001

Estatus: decision provisional de expediente.

Fecha: 2026-07-02.

## Decision

`HXI-001` queda en pausa operativa, abierto sin admision de `H-Xi`.

## Alcance

La decision conserva el reporte de consistencia, la notacion minima `Xi-R`, los criterios de admision formal posterior y la hipotesis externa `H-Xi`, pero detiene la evaluacion inmediata.

## No cubre

No admite `H-Xi`, no canoniza `Xi`, no declara operador vigente, no cierra `HXI-001`, no modifica `PSI-001`, Canon ni documentos oficiales, y no autoriza transformaciones materiales.

## Consecuencia

El frente activo inmediato pasa a `AUT-001`.

## D-2026-07-02-012 - Reactivacion de AUT-001

Estatus: decision provisional de expediente.

Fecha: 2026-07-02.

## Decision

Se reactiva `AUT-001` como frente activo inmediato del Laboratorio.

## Alcance

La decision permite crear una herramienta de tablero operativo, conservar reportes y continuar automatizacion no mutante.

## No cubre

No cierra `AUT-001`, no confirma ejecucion directa local con `python`, no autoriza transformaciones, no modifica Canon ni documentos oficiales, y no cierra o reabre expedientes.

## Consecuencia

La accion inmediata es crear y validar `DO-STATE-BOARD-001`.

## D-2026-07-02-013 - Estatus de tablero de estado AUT-001

Estatus: decision provisional de expediente.

Fecha: 2026-07-02.

## Decision

Se acepta `06_Automatizacion/lab_status_board.py` como `DO-STATE-BOARD-001`, tablero no mutante de estado del Laboratorio.

## Alcance

La decision cubre existencia de la herramienta, reportes conservados y visibilidad del estado operativo.

## No cubre

No cierra `AUT-001`, no confirma ejecucion directa local con `python`, no automatiza completamente el Auditor, no autoriza cambios reales, no modifica Canon ni documentos oficiales y no cierra o reabre expedientes.

## Consecuencia

El siguiente objetivo es definir integracion entre `DO-STATE-BOARD-001` y `DO-CHECK-MED-001` para un reporte combinado de continuidad y riesgos.

## D-2026-07-02-014 - Continuidad integrada AUT-001

Estatus: decision provisional de expediente.

Fecha: 2026-07-02.

## Decision

Se acepta `06_Automatizacion/lab_continuity_report.py` como `DO-LAB-CONTINUITY-001`, integracion no mutante entre `DO-STATE-BOARD-001` y `DO-CHECK-MED-001`. Decision espejo: `03_Expedientes/AUT-001_Decision_Continuidad_Laboratorio.md`.

## Alcance

La decision cubre el reporte combinado de continuidad, conservacion de advertencias heredadas y recomendacion operacional sin transformacion.

## No cubre

No cierra `AUT-001`, no confirma ejecucion directa local con `python`, no autoriza cambios reales, no modifica Canon ni documentos oficiales y no cierra o reabre expedientes.

## Consecuencia

El siguiente objetivo es Crear comando unico de corrida local para `AUT-001`.

## D-2026-07-02-015 - Comando unico AUT-001

Estatus: decision provisional de expediente.

Fecha: 2026-07-02.

## Decision

Se acepta `06_Automatizacion/lab_run.py` como `DO-LAB-RUN-001`, comando unico provisional de corrida local para `AUT-001`. Decision espejo: `03_Expedientes/AUT-001_Decision_Comando_Unico_LAB.md`.

## Alcance

La decision cubre orquestacion no mutante de chequeo minimo, chequeo medio, tablero y continuidad integrada, con reportes Markdown y JSON.

## No cubre

No cierra `AUT-001`, no confirma ejecucion directa local con `python`, no autoriza cambios reales, no modifica Canon ni documentos oficiales y no cierra o reabre expedientes.

## Consecuencia

El siguiente objetivo es separar advertencias heredadas de riesgos nuevos dentro de `AUT-001`.

## D-2026-07-02-016 - Clasificacion de advertencias y riesgos AUT-001

Estatus: decision provisional de expediente.

Fecha: 2026-07-02.

## Decision

Se acepta `06_Automatizacion/lab_risk_classifier.py` como `DO-LAB-RISK-001`, clasificador provisional no mutante de advertencias y riesgos. Decision espejo: `03_Expedientes/AUT-001_Decision_Riesgos_Advertencias.md`.

## Alcance

La decision cubre separacion de advertencias heredadas, deuda documental y riesgos activos a partir de reportes de `AUT-001`.

## No cubre

No resuelve hallazgos, no cierra `AUT-001`, no confirma ejecucion directa local con `python`, no autoriza cambios reales, no modifica Canon ni documentos oficiales y no cierra o reabre expedientes.

## Consecuencia

El siguiente objetivo es crear resumen ejecutivo automatico del laboratorio usando `DO-LAB-RUN-001` y `DO-LAB-RISK-001`.

## D-2026-07-02-017 - Resumen ejecutivo automatico AUT-001

Estatus: decision provisional de expediente.

Fecha: 2026-07-02.

## Decision

Se acepta `06_Automatizacion/lab_executive_summary.py` como `DO-LAB-SUMMARY-001`, resumen ejecutivo automatico provisional del Laboratorio. Decision espejo: `03_Expedientes/AUT-001_Decision_Resumen_Ejecutivo.md`.

## Alcance

La decision cubre sintesis ejecutiva no mutante de corrida, riesgos, estado operativo y siguientes acciones.

## No cubre

No resuelve hallazgos, no cierra `AUT-001`, no confirma ejecucion directa local con `python`, no autoriza cambios reales, no modifica Canon ni documentos oficiales y no cierra o reabre expedientes.

## Consecuencia

El siguiente objetivo es definir criterio de cierre de `AUT-001` y tratamiento inicial de riesgos activos altos.

## D-2026-07-02-018 - Criterios de cierre y riesgos altos AUT-001

Estatus: decision provisional de expediente.

Fecha: 2026-07-02.

## Decision

Se aceptan `AUT-CLOSE-CRIT-001` y `AUT-RISK-TREAT-001` como criterios de cierre de fase media y tratamiento inicial de riesgos altos para `AUT-001`. Decision espejo: `03_Expedientes/AUT-001_Decision_Cierre_Riesgos.md`.

## Alcance

La decision cubre compuerta de cierre tecnico provisional, cierre operativo completo y tratamiento no mutante de 2 riesgos altos.

## No cubre

No cierra `AUT-001`, no autoriza cierre operativo completo, no confirma ejecucion directa local con `python`, no autoriza cambios reales, no modifica Canon ni documentos oficiales y no cierra o reabre expedientes.

## Consecuencia

El siguiente objetivo es decidir si `AUT-001` pasa a cierre tecnico provisional o continua con refinamiento antes de cambiar de frente.

## D-2026-07-02-019 - Revision de riesgos activos AUT-001

Estatus: decision provisional de expediente.

Fecha: 2026-07-02.

## Decision

Se acepta `AUT-001_Matriz_Revision_Riesgos_Activos.md` como revision provisional no mutante de los 17 riesgos activos emitidos por `DO-LAB-RISK-001`. Decision espejo: `03_Expedientes/AUT-001_Decision_Revision_Riesgos_Activos.md`.

## Alcance

La decision cubre lectura, clasificacion y tratamiento no mutante de riesgos activos como guardrails, decision registrada, historial o refinamiento pendiente del detector.

## No cubre

No modifica el clasificador, no regenera reportes, no cierra `AUT-001`, no confirma ejecucion directa local con `python`, no autoriza cambios reales, no modifica Canon ni documentos oficiales y no cierra o reabre expedientes.

## Consecuencia

El siguiente objetivo recomendado es refinar `DO-LAB-RISK-001` para distinguir prohibiciones, decisiones historicas y definiciones de checks antes de decidir cierre tecnico provisional de `AUT-001`.

## D-2026-07-02-020 - Refinamiento DO-LAB-RISK AUT-001

Estatus: decision provisional de expediente.

Fecha: 2026-07-02.

## Decision

Se acepta `AUT-RISK-REFINE-001` como refinamiento provisional de `DO-LAB-RISK-001`. Documento base: `03_Expedientes/AUT-001_Refinamiento_DO-LAB-RISK.md`. Decision espejo: `03_Expedientes/AUT-001_Decision_Refinamiento_DO-LAB-RISK.md`.

## Alcance

Cubre reclasificacion contextual de 17 riesgos activos como `advertencia_controlada`, conservando evidencia y `transformacion_permitida: false`.

## No cubre

No confirma ejecucion directa local con `python`, no cierra operativamente `AUT-001`, no autoriza cambios reales y no modifica Canon ni documentos oficiales.

## Consecuencia

Se habilita decidir cierre tecnico provisional de `AUT-001`.

## D-2026-07-02-021 - Cierre tecnico provisional AUT-001

Estatus: decision provisional de expediente.

Fecha: 2026-07-02.

## Decision

Se acepta cierre tecnico provisional de `AUT-001`. Decision espejo: `03_Expedientes/AUT-001_Decision_Cierre_Tecnico_Provisional.md`.

## Alcance

La automatizacion media queda estable como paquete no mutante provisional; las advertencias controladas permanecen visibles.

## No cubre

No cierra operativamente `AUT-001`, no confirma ejecucion directa local con `python`, no modifica Canon ni documentos oficiales y no cierra o reabre expedientes.

## Consecuencia

El siguiente frente beneficioso recomendado es `PSI-001`.

## D-2026-07-02-022 - Mapa de continuidad conceptual PSI-001

Estatus: decision provisional de expediente.

Fecha: 2026-07-02.

## Decision

Se acepta `PSI-MAP-CONT-001` como mapa provisional de continuidad conceptual no clinica dentro de `PSI-001`. Documento base: `03_Expedientes/PSI-001_Mapa_Continuidad_Conceptual.md`. Decision espejo: `03_Expedientes/PSI-001_Decision_Estatus_Mapa_Continuidad_Conceptual.md`.

## Alcance

Orienta la continuidad de `PSI-001` como frente conceptual estable.

## No cubre

No canoniza contenido psicologico, no habilita diagnostico clinico, no admite `H-Xi` y no modifica Canon ni documentos oficiales.

## Consecuencia

El siguiente trabajo recomendado es una serie breve de casos conceptuales no clinicos de transformacion psicologica.

## D-2026-07-02-023 - Casos de transformacion no clinicos PSI-001

Estatus: decision provisional de expediente.

Fecha: 2026-07-02.

## Decision

Se acepta `CAS-PSI-001` a `CAS-PSI-006` como serie conceptual provisional no clinica dentro de `PSI-001`. Documento base: `03_Expedientes/PSI-001_Casos_Transformacion_No_Clinicos.md`. Auditoria: `03_Expedientes/PSI-001_Auditoria_Casos_Transformacion_No_Clinicos.md`. Decision espejo: `03_Expedientes/PSI-001_Decision_Estatus_Casos_Transformacion_No_Clinicos.md`.

## Alcance

Permite usar los casos para ampliar la prueba de `DEF-PSI-ORG-001` y `CRIT-PSI-TR-001` y preparar una matriz interna de patrones no clinicos.

## No cubre

No canoniza contenido psicologico, no habilita diagnostico clinico, no admite `H-Xi`, no reabre `HXI-001` y no modifica Canon ni documentos oficiales.

## Consecuencia

El siguiente trabajo recomendado es sintetizar los casos en una matriz de patrones no clinicos de transformacion.

## D-2026-07-02-024 - Matriz de patrones no clinicos PSI-001

Estatus: decision provisional de expediente.

Fecha: 2026-07-02.

## Decision

Se acepta `PSI-MAT-PAT-001` como matriz provisional de patrones no clinicos de transformacion dentro de `PSI-001`. Documento base: `03_Expedientes/PSI-001_Matriz_Patrones_Transformacion_No_Clinica.md`. Auditoria: `03_Expedientes/PSI-001_Auditoria_Matriz_Patrones_Transformacion_No_Clinica.md`. Decision espejo: `03_Expedientes/PSI-001_Decision_Estatus_Matriz_Patrones_Transformacion_No_Clinica.md`.

## Alcance

Permite sintetizar `CAS-PSI-001` a `CAS-PSI-006` en patrones comparables de cambio, continuidad, relaciones `R` y bloqueo no clinico.

## No cubre

No canoniza contenido psicologico, no habilita diagnostico clinico, no abre psicopatologia, no admite `H-Xi`, no reabre `HXI-001` y no modifica Canon ni documentos oficiales.

## Consecuencia

La compuerta de frontera para psicopatologia conceptual no clinica quedo cumplida por `D-2026-07-03-003`, la primera serie de casos abstractos quedo cumplida por `D-2026-07-03-004` y la matriz provisional de frontera quedo cumplida por `D-2026-07-03-005`. El siguiente trabajo recomendado dentro de `PSI-001` es solo refinamiento interno no clinico, sin expansion patologica, clinica ni canonica.

## D-2026-07-02-025 - Reactivacion de AUD-001 para REPORT_LAYER

Estatus: decision provisional de expediente.

Fecha: 2026-07-02.

## Decision

Se reactiva `AUD-001` de forma acotada para separar `REPORT_LAYER` como candidata provisional de expediente.

Documento base: `03_Expedientes/AUD-001_Decision_Reactivacion_REPORT_LAYER.md`.

## Alcance

La decision permite redactar y auditar `AUD-001_REPORT_LAYER_Candidata.md`, mapear reportes locales de `AUD-001` a una capa abstracta y continuar el frente del Auditor solo en esa ruta.

## No cubre

No promueve `REPORT_LAYER`, no modifica `C-001`, no promueve `R4-CANDIDATA`, no resuelve R4 formal ni `Gamma`, y no autoriza transformaciones materiales.

## Consecuencia

La accion inmediata es redactar, auditar y decidir estatus de `REPORT-LAYER-CAND-001`.

## D-2026-07-02-026 - Estatus de REPORT_LAYER Candidata

Estatus: decision provisional de expediente.

Fecha: 2026-07-02.

## Decision

Se acepta `REPORT-LAYER-CAND-001` como candidata provisional de expediente dentro de `AUD-001`.

Documento base: `03_Expedientes/AUD-001_REPORT_LAYER_Candidata.md`. Auditoria: `03_Expedientes/AUD-001_Auditoria_REPORT_LAYER_Candidata.md`. Decision espejo: `03_Expedientes/AUD-001_Decision_Estatus_REPORT_LAYER_Candidata.md`.

## Alcance

La decision permite usar `REPORT_LAYER-CAND-001` dentro de `AUD-001`, mapear reportes locales a clases abstractas y preparar validaciones adicionales.

## No cubre

No convierte `REPORT_LAYER` en especificacion oficial, no modifica documentos oficiales, no promueve `R4-CANDIDATA`, no cierra `AUD-001`, no resuelve R4 formal ni `Gamma`, y no autoriza transformaciones materiales.

## Consecuencia

El siguiente trabajo recomendado es validar `REPORT-LAYER-CAND-001` contra una instancia no automata no reducida a nombres locales de `AUD-001`, o decidir explicitamente que permanece local.

## D-2026-07-02-027 - Completitud documental/operativa del Auditor v0

Estatus: decision de expediente.

Fecha: 2026-07-02.

## Decision

Se acepta que el Auditor queda completo en version documental/operativa v0 dentro de `AUD-001`.

Documento base: `03_Expedientes/AUD-001_Decision_Estatus_Auditor_v0.md`.

## Alcance

La decision cubre la matriz minima `AUD-T00` a `AUD-T09`, contratos de reporte, validaciones hasta `VAL-029`, `REPORT_LAYER` local, puente conceptual con `DO_CHECK_REPORT` y limites de autoridad del Auditor.

## No cubre

No cubre herramienta ejecutable completa, parser real, Regla R4 formal, `Gamma` formal, reversion material, cuarentena materializada, promocion de `REPORT_LAYER` a Nivel C ni cierre de `H-B.6` o `H-B.7`.

## Consecuencia

`AUD-001` queda habilitado para proyectar la completitud v0 a una especificacion tipo RFC, sin cerrar sus deudas formales.

## D-2026-07-02-028 - Promocion de SPEC-RFC-AUDITOR-V0 a C-002

Estatus: decision documental de Nivel C.

Fecha: 2026-07-02.

## Decision

Se promueve `SPEC-RFC-AUDITOR-V0` a documento oficial de Nivel C como `02_Documentos/C-002_RFC_Operativo_Auditor_v0.md`.

Documento base: `03_Expedientes/AUD-001_Decision_Promocion_SPEC-RFC-AUDITOR-V0.md`.

## Alcance

La decision cubre el documento tipo RFC operativo del Auditor v0, su lenguaje normativo local, modelo operacional, permisos, reportes, conformidad y matriz minima de pruebas.

## No cubre

No reemplaza `C-001`, no modifica Canon, no resuelve R4 formal ni `Gamma`, no autoriza implementacion ejecutable completa y no promueve `REPORT_LAYER` a Nivel C.

## Consecuencia

`C-002` queda como referencia oficial para revisar conformidad de lecturas, herramientas o propuestas de implementacion del Auditor v0.

## D-2026-07-02-029 - Cierre operativo completo de AUT-001

Estatus: decision de cierre de expediente.

Fecha: 2026-07-02.

## Decision

Se cierra operativamente `AUT-001`.

Documento base: `03_Expedientes/AUT-001_Decision_Cierre_Operativo_Completo.md`.

Validacion: `03_Expedientes/AUT-001_Validacion_Cierre_Operativo_Completo.md`.

## Alcance

La decision cubre la automatizacion no mutante inicial del Laboratorio: chequeo minimo, chequeo medio, tablero, continuidad, corrida unica, clasificacion de riesgos y resumen ejecutivo, con evidencia de ejecucion directa local sobre archivos clave.

## No cubre

No afirma consistencia global perfecta del repositorio, no autoriza transformaciones materiales, no modifica Canon ni documentos oficiales, no cierra expedientes ajenos y no resuelve R4 formal ni `Gamma`.

## Consecuencia

`AUT-001` pasa a expedientes cerrados. Las herramientas quedan conservadas como infraestructura no mutante y cualquier mejora futura requiere nuevo expediente, subexpediente o decision de reapertura.

## D-2026-07-02-030 - Fichas de alcance H-B.6 y H-B.7

Estatus: decision provisional de expediente.

Fecha: 2026-07-02.

## Decision

Se aceptan las fichas de alcance local minimo para `H-B.6` y `H-B.7`.

Documento base: `03_Expedientes/HB-001_Decision_Fichas_Alcance_H-B.md`.

Fichas:

- `03_Expedientes/HB-001_Ficha_Alcance_H-B.6.md`
- `03_Expedientes/HB-001_Ficha_Alcance_H-B.7.md`

## Alcance

La decision precisa que ambas hipotesis siguen activas solo como etiquetas de deuda viva de Nivel B con contenido sustantivo no materializado.

## No cubre

No demuestra, refuta, desarrolla ni diferencia semanticamente `H-B.6` o `H-B.7`; no reabre `B-001`, no descongela `B-001.5`, no modifica Canon ni documentos oficiales y no habilita uso como premisa para R4, `Gamma` o `REPORT_LAYER`.

## Consecuencia

La deuda pendiente deja de ser precisar alcance minimo y pasa a ser buscar fuente local sustantiva o decidir congelamiento, absorcion, cierre o apertura de expediente propio.

## D-2026-07-02-031 - Desactivacion de vision papers

Estatus: decision operativa de prioridad.

Fecha: 2026-07-02.

## Decision

Se desactivan `VISION_PAPER_PROPUESTA.md` y `VISION_PAPER_FINAL_REFERENCIAS.md` hasta nuevo aviso.

Documento base: `05_Estado_Proyecto/DECISION_Desactivacion_Vision_Papers.md`.

## Alcance

La decision conserva ambos archivos como borradores editoriales locales, pero los retira de autoridad, agenda y ruta operativa vigente.

## No cubre

No elimina los archivos, no los publica, no los promueve a documento oficial, no los usa como fuente para `TCS-001`, `P-PI`, `R4`, `Gamma` o `REPORT_LAYER`, y no modifica Canon ni documentos oficiales.

## Consecuencia

El avance inmediato se traslada a frentes sustantivos, especialmente `P-PI.0` / `P-PI.1`.

## D-2026-07-02-032 - Reactivacion matematica acotada de P-PI

Estatus: decision provisional de expediente.

Fecha: 2026-07-02.

## Decision

Se reactiva `P-PI.0` / `P-PI.1` como frente matematico acotado.

Documento base: `03_Expedientes/P-PI_Decision_Reactivacion_Frente_Matematico.md`.

Marco aceptado: `03_Expedientes/P-PI_Marco_Inicial_Confluencia_Equivalencia.md`.

Auditoria: `03_Expedientes/P-PI_Auditoria_Marco_Inicial_Confluencia_Equivalencia.md`.

## Alcance

`P-PI.0` queda activo acotado para Equivalencia de proyecciones.

`P-PI.1` queda activo acotado para Confluencia.

`PPI-MARCO-CORE-001` queda aceptado como marco provisional de expediente.

## No cubre

No cierra Confluencia, no cierra Equivalencia de proyecciones, no modifica Canon ni documentos oficiales, no reactiva vision papers, no usa historial como autoridad directa y no promueve el marco al Documento 02.

## Consecuencia

El siguiente objetivo es ejecutar `PPI-EQ-001` como primer caso de Equivalencia de proyecciones y preparar `PPI-CONF-001` solo despues de declarar una relacion `~_C`.

## D-2026-07-03-003 - Compuerta de frontera psicopatologica conceptual no clinica PSI-001

Estatus: decision provisional de expediente.

Fecha: 2026-07-03.

## Decision

Se acepta `PSI-FRON-PSICOPAT-001` como compuerta provisional de frontera para psicopatologia conceptual no clinica dentro de `PSI-001`.

Documento base: `03_Expedientes/PSI-001_Compuerta_Frontera_Psicopatologia_Conceptual_No_Clinica.md`.

Auditoria: `03_Expedientes/PSI-001_Auditoria_Compuerta_Frontera_Psicopatologia_Conceptual_No_Clinica.md`.

Decision espejo: `03_Expedientes/PSI-001_Decision_Estatus_Compuerta_Frontera_Psicopatologia_Conceptual_No_Clinica.md`.

## Alcance

La decision permite usar la compuerta para evaluar propuestas abstractas de frontera conceptual no clinica, estabilizar `no auditable` como salida de seguridad y preparar casos abstractos posteriores dentro de `PSI-001`.

## No cubre

No abre un subfrente psicopatologico, no habilita uso clinico, diagnostico, tratamiento, consejo profesional, evaluacion de personas reales, clasificacion de trastornos, canonizacion, modificacion de documentos oficiales, admision de `H-Xi`, `P-107` o Concordancia, reapertura de `HXI-001` ni cierre de `PSI-001`.

## Consecuencia

`PSI-001` quedaba abierto con compuerta de frontera aceptada en esta decision. La primera serie de casos abstractos de frontera quedo creada posteriormente por `D-2026-07-03-004`; el frente fue independizado despues por `D-2026-07-03-006`.

## D-2026-07-03-004 - Casos de frontera conceptual no clinica PSI-001

Estatus: decision provisional de expediente.

Fecha: 2026-07-03.

## Decision

Se acepta `PSI-FRON-CAS-001` a `PSI-FRON-CAS-006` como primera serie provisional de casos abstractos de frontera conceptual no clinica dentro de `PSI-001`.

Documento base: `03_Expedientes/PSI-001_Casos_Frontera_Conceptual_No_Clinica.md`.

Auditoria: `03_Expedientes/PSI-001_Auditoria_Casos_Frontera_Conceptual_No_Clinica.md`.

Decision espejo: `03_Expedientes/PSI-001_Decision_Estatus_Casos_Frontera_Conceptual_No_Clinica.md`.

Compuerta aplicada: `PSI-FRON-PSICOPAT-001`.

## Alcance

La decision permite usar la serie para probar la compuerta de frontera aceptada por `D-2026-07-03-003`, conservar tres casos admisibles, devolver un caso ordinario a `PSI-001`, exigir reformulacion de un caso insuficientemente formal y bloquear un caso por uso clinico o personal.

## No cubre

No abre subfrente psicopatologico, no habilita uso clinico, diagnostico, tratamiento, consejo profesional, evaluacion de personas reales, clasificacion de trastornos, canonizacion, modificacion de documentos oficiales, admision de `H-Xi`, `P-107` o Concordancia, reapertura de `HXI-001` ni cierre de `PSI-001`.

## Consecuencia

`PSI-001` quedaba abierto con primera serie de casos de frontera aceptada en esta decision. La matriz provisional de frontera quedo creada posteriormente por `D-2026-07-03-005`; el frente fue independizado despues por `D-2026-07-03-006`.

## D-2026-07-03-005 - Matriz de frontera conceptual no clinica PSI-001

Estatus: decision provisional de expediente.

Fecha: 2026-07-03.

## Decision

Se acepta `PSI-FRON-MAT-001` como matriz provisional no clinica de frontera conceptual dentro de `PSI-001`.

Documento base: `03_Expedientes/PSI-001_Matriz_Frontera_Conceptual_No_Clinica.md`.

Auditoria: `03_Expedientes/PSI-001_Auditoria_Matriz_Frontera_Conceptual_No_Clinica.md`.

Decision espejo: `03_Expedientes/PSI-001_Decision_Estatus_Matriz_Frontera_Conceptual_No_Clinica.md`.

## Alcance

La decision permite usar `PSI-FRON-MAT-001` para sintetizar cuatro patrones abstractos: rigidez relacional, fragmentacion de unidad, bloqueo de transicion y tension relacional.

Tambien deja `PSI-FRON-CAS-005` reformulado como tension relacional formalizada, mantiene `PSI-FRON-CAS-006` bloqueado como control negativo y conserva `PSI-FRON-CAS-004` devuelto a `PSI-001`.

## No cubre

No abre subfrente patologico o psicopatologico, no habilita uso clinico, diagnostico, tratamiento, consejo profesional, recomendacion de conducta, evaluacion de personas reales, clasificacion de trastornos, canonizacion, modificacion de documentos oficiales, admision de `H-Xi`, `P-107` o Concordancia, reapertura de `HXI-001` ni cierre de `PSI-001`.

## Consecuencia

`PSI-001` quedaba abierto con matriz provisional de frontera conceptual no clinica aceptada en esta decision. La expansion patologica, clinica y canonica quedaba detenida; posteriormente el frente fue independizado por `D-2026-07-03-006`.

## D-2026-07-03-006 - Independizacion de PSI-001

Estatus: decision provisional de transferencia.

Fecha: 2026-07-03.

## Decision

Se independiza `PSI-001` como proyecto propio bajo el nombre operativo `Psicologia Concordante`.

Documento de decision: `03_Expedientes/PSI-001_Decision_Independizacion_Proyecto.md`.

La fuente activa posterior queda fuera del Laboratorio, en un repositorio independiente y privado. El Laboratorio conserva una copia local de traspaso para trazabilidad historica, pero no debe usarla como superficie normal de trabajo.

## Alcance

La decision transfiere el paquete documental `PSI-001*`: expediente principal, axioma candidato, definicion, criterio, ejemplos, casos, matrices, compuerta, auditorias y decisiones internas.

## No cubre

No canoniza contenido, no modifica documentos oficiales, no habilita uso clinico, no abre subfrente patologico o psicopatologico, no admite `H-Xi`, `P-107` ni Concordancia y no reabre `HXI-001`.

## Consecuencia

Dentro del Laboratorio, `PSI-001` queda como frente transferido / independizado. Las continuidades sustantivas de psicologia solo deben trabajarse en el proyecto independiente.

El proximo objetivo interno del Laboratorio vuelve a `AUD-001`, `Gamma`, definicion formal de `R4`, Confluencia y Equivalencia de proyecciones.

Deudas abiertas: decidir si la copia de traspaso se conserva, archiva o elimina; mantener visible que la fuente activa ya no esta en el Laboratorio; no usar Canon, documentos oficiales ni automatizaciones del Laboratorio como autoridad directa para el proyecto independiente sin decision puente posterior.
