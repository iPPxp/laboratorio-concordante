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

La fuente activa posterior queda fuera del Laboratorio, en un repositorio independiente y privado. La copia local de traspaso existio solo de forma transitoria y fue eliminada posteriormente por `D-2026-07-03-012`.

## Alcance

La decision transfiere el paquete documental `PSI-001*`: expediente principal, axioma candidato, definicion, criterio, ejemplos, casos, matrices, compuerta, auditorias y decisiones internas.

## No cubre

No canoniza contenido, no modifica documentos oficiales, no habilita uso clinico, no abre subfrente patologico o psicopatologico, no admite `H-Xi`, `P-107` ni Concordancia y no reabre `HXI-001`.

## Consecuencia

Dentro del Laboratorio, `PSI-001` queda como frente transferido / independizado. Las continuidades sustantivas de psicologia solo deben trabajarse en el proyecto independiente.

El proximo objetivo interno del Laboratorio vuelve a `AUD-001`, `Gamma`, definicion formal de `R4`, Confluencia y Equivalencia de proyecciones.

Actualizacion posterior: la deuda sobre conservar, archivar o eliminar la copia queda resuelta por `D-2026-07-03-012`, que elimina `PSI-001*` del Laboratorio. Permanece abierto mantener visible que la fuente activa ya no esta en el Laboratorio y no usar Canon, documentos oficiales ni automatizaciones del Laboratorio como autoridad directa para el proyecto independiente sin decision puente posterior.

## D-2026-07-03-007 - Gamma ruta 1 como definicion local provisional

Estatus: decision provisional de expediente.

Fecha: 2026-07-03.

## Decision

Se acepta `GAMMA-DEF-001` como definicion local provisional de `Gamma` en ruta 1 dentro de `AUD-001`.

Documento base: `03_Expedientes/AUD-001_Gamma_Ruta1_Definicion_Local.md`.

Auditoria: `03_Expedientes/AUD-001_Auditoria_Gamma_Ruta1_Definicion_Local.md`.

Decision espejo: `03_Expedientes/AUD-001_Decision_Estatus_Gamma_Ruta1_Definicion_Local.md`.

## Alcance

La decision permite usar `Gamma_1(E, C) = G` solo como mecanismo local de expediente para producir salidas provisionales: hipotesis operativas, definiciones o criterios provisionales, deudas refinadas o problemas abiertos delimitados.

La definicion exige evidencia local `E`, contexto declarado `C`, invariantes, restricciones, estatus provisional y salida segura.

## No cubre

No construye `Gamma` formal, no convierte `Gamma` en teorema, no modifica Canon, no modifica `C-001` ni `C-002`, no crea Nivel C, no resuelve R4 formal, no promueve `REPORT_LAYER`, no autoriza transformaciones materiales y no invalida `AUD-SIM-025` / `VAL-025` para usos de estatus excesivo.

## Consecuencia

La deuda "definir localmente `Gamma`" queda atendida solo en grado minimo provisional de expediente. En ese momento permanecia abierta la construccion formal completa de `Gamma`; quedo atendida localmente despues por `D-2026-07-03-010`.

Actualizacion operativa posterior: `AUD-SIM-030` y `VAL-030` validan `Gamma_1` contra un primer caso positivo acotado; `AUD-SIM-025` / `VAL-025` quedan revisados como control negativo de estatus excesivo; `REL-GAMMA-R4-001` precisa que `R4-CANDIDATA` puede ser evidencia local para `Gamma_1`, pero no equivale a Regla R4 formal.

## D-2026-07-03-008 - Apertura de AO-001 para Algebra Operacional

Estatus: decision provisional de expediente.

Fecha: 2026-07-03.

## Decision

Se abre `AO-001` como expediente preparatorio de la futura Algebra Operacional del Laboratorio Concordante.

Documento base: `03_Expedientes/AO-001_Decision_Apertura.md`.

Marco inicial: `03_Expedientes/AO-001_Marco_Inicial_Algebra_Operacional.md`.

Documento destino eventual: `02_Documentos/04_Algebra_Operacional.md`.

## Alcance

La decision permite preparar notacion operacional para artefactos, estatus, evidencia, reportes, decisiones, permisos, invariantes, transformaciones y salidas de seguridad.

Tambien permite usar `C-001`, `C-002`, `R4-CANDIDATA` y `GAMMA-DEF-001` como fuentes locales de vocabulario operacional, sin promoverlos de estatus.

## No cubre

No llena el Documento 04 como contenido oficial, no modifica Canon, no promueve `R4-CANDIDATA`, no construye `R4` formal, no construye `Gamma` formal, no promueve `GAMMA-DEF-001`, no autoriza transformaciones materiales y no cierra Confluencia ni Equivalencia de proyecciones.

## Consecuencia

`AO-001` queda abierto como expediente preparatorio.

`04_Algebra_Operacional.md` permanece reservado, con nota de estado hacia `AO-001`.

El siguiente paso recomendado es auditar el marco inicial contra `M-000`, `M-001`, `C-001` y `C-002` antes de cualquier incorporacion al Documento 04.

## D-2026-07-03-009 - Estatus del marco inicial de AO-001

Estatus: decision provisional de expediente.

Fecha: 2026-07-03.

## Decision

Se acepta `AO-MARCO-001` como marco inicial provisional de Algebra Operacional dentro de `AO-001`.

Documento base: `03_Expedientes/AO-001_Marco_Inicial_Algebra_Operacional.md`.

Auditoria: `03_Expedientes/AO-001_Auditoria_Marco_Inicial_Algebra_Operacional.md`.

Decision espejo: `03_Expedientes/AO-001_Decision_Estatus_Marco_Inicial_Algebra_Operacional.md`.

## Alcance

La decision acepta objetos candidatos, operadores candidatos, invariantes operacionales iniciales, formas de salida, antipatrones, preguntas abiertas y criterio de avance.

## No cubre

No incorpora contenido sustantivo al Documento 04, no modifica Canon, no modifica `C-001` ni `C-002`, no construye R4 formal, no construye `Gamma` formal, no promueve `GAMMA-DEF-001`, no autoriza transformaciones materiales y no cierra Confluencia ni Equivalencia de proyecciones.

## Consecuencia

`AO-001` queda abierto con primer marco provisional aceptado.

El Documento 04 permanece reservado.

El siguiente paso recomendado es crear una bateria minima de casos `AO-CASE` para probar los operadores candidatos.

## D-2026-07-03-010 - R4 formal local y Gamma formal local

Estatus: decision provisional de expediente.

Fecha: 2026-07-03.

## Decision

Se acepta `R4-FORMAL-AUD-001` como construccion formal local de `R4` dentro de `AUD-001`.

Se acepta `GAMMA-FORMAL-AUD-001` como construccion formal local de `Gamma` dentro de `AUD-001`.

Se acepta `VAL-031` como segunda prueba positiva de `Gamma_1`, fuera de `R4-CANDIDATA`.

Documento base: `03_Expedientes/AUD-001_R4_Formal_Local.md`, `03_Expedientes/AUD-001_Gamma_Formal_Local.md`, `03_Expedientes/AUD-001_Simulaciones.md` y `03_Expedientes/AUD-001_Validaciones.md`.

Auditoria: `03_Expedientes/AUD-001_Auditoria_R4_Gamma_Formal_Local.md`.

Decision espejo: `03_Expedientes/AUD-001_Decision_Estatus_R4_Gamma_Formal_Local.md`.

## Alcance

La decision permite usar `R4-FORMAL-AUD-001`, `GAMMA-FORMAL-AUD-001` y `VAL-031` como artefactos formales locales de `AUD-001`.

`R4-FORMAL-AUD-001` define trazas, decision fundada, ejecucion valida y teorema local de seguridad.

`GAMMA-FORMAL-AUD-001` define `Gamma` como operador parcial local de generalizacion controlada.

`VAL-031` prueba `Gamma_1` con `REPORT_LAYER` / `DO_CHECK_REPORT`.

## No cubre

No modifica Canon, no modifica `C-001` ni `C-002`, no promueve R4 a regla canonica ni documento oficial, no promueve `Gamma` a teoria global ni Nivel C, no promueve `REPORT_LAYER`, no autoriza transformaciones materiales, no cierra Confluencia ni Equivalencia de proyecciones y no exporta autoridad fuera de `AUD-001`.

## Consecuencia

Las deudas de construir formalmente R4 y `Gamma` dentro de `AUD-001` quedan atendidas localmente.

Permanecen abiertas promocion, exportacion, implementacion ejecutable, pruebas fuera de `AUD-001` y uso eventual en Confluencia o Equivalencia de proyecciones.

## D-2026-07-03-011 - Consolidacion documentos 00-04

Estatus: decision documental.

Fecha: 2026-07-03.

## Decision

Se incorporan versiones completas desde fuentes previas a:

- `02_Documentos/00_Naturaleza.md`
- `02_Documentos/01_Canon.md`
- `02_Documentos/02_Fundamentos_Matematicos.md`
- `02_Documentos/03_Ontologia.md`

Se actualiza `02_Documentos/04_Algebra_Operacional.md` como version inicial consolidada.

Documento base: `03_Expedientes/DOCS-001.md`.

Auditoria: `03_Expedientes/DOCS-001_Auditoria_Consolidacion_Documentos_00-04.md`.

Decision espejo: `03_Expedientes/DOCS-001_Decision_Consolidacion_Documentos_00-04.md`.

## Alcance

La decision permite tratar documentos 00-03 como versiones consolidadas oficiales y Documento 04 como version inicial consolidada de Algebra Operacional.

## No cubre

No modifica archivos de `01_Canon`.

No canoniza reglas historicas por nombre.

No promueve `R4-FORMAL-AUD-001` ni `GAMMA-FORMAL-AUD-001` fuera de `AUD-001`.

No admite `H-Xi`.

No canoniza `Xi`, `Omega`, `Phi`, `Psi`, `P-108`, `P-200` ni Concordancia.

No autoriza transformaciones materiales.

No cierra Confluencia ni Equivalencia de proyecciones.

## Consecuencia

La deuda de consolidar contenido real de documentos 00, 01, 02 y 03 desde fuentes previas queda atendida.

La deuda de preparacion auditable del Documento 04 queda atendida en grado de version inicial consolidada.

El siguiente trabajo recomendado es crear `AO-CASE` para probar los operadores del Documento 04.

## D-2026-07-03-012 - Eliminacion de copia local PSI-001

Estatus: decision operativa de limpieza.

Fecha: 2026-07-03.

## Decision

Se elimina del Laboratorio la copia local de traspaso de `PSI-001`.

Documento de decision: `03_Expedientes/PSI-TRASPASO-001_Decision_Eliminacion_Copia.md`.

## Alcance

La decision cubre la eliminacion de los archivos locales `03_Expedientes/PSI-001*` que habian quedado como copia de traspaso despues de la independizacion.

El proyecto activo de psicologia permanece fuera del Laboratorio, en `Psicologia Concordante`.

## No cubre

No elimina ni modifica el proyecto independiente, no reabre psicologia dentro del Laboratorio, no abre subfrente patologico, clinico ni canonico, no habilita uso clinico y no borra la trazabilidad historica agregada.

## Consecuencia

`PSI-001` deja de existir como copia local de trabajo o traspaso dentro de `03_Expedientes`.

El Laboratorio puede mencionar `PSI-001` solo como antecedente historico transferido o dependencia externa, mediante decision puente si se requiere contenido sustantivo.

Resultado posterior inicial: `DO-LAB-RUN-001` fue regenerado y quedo bloqueado por referencias historicas no materializadas a `PSI-001*`. Esa deuda queda atendida despues por `D-2026-07-03-015`; la salida regenerada queda en `advertencia`, no en bloqueo, sin restaurar la copia local.

## D-2026-07-03-013 - Congelamiento de H-B.6 y H-B.7

Estatus: decision provisional de expediente.

Fecha: 2026-07-03.

## Decision

`H-B.6` y `H-B.7` quedan congeladas como brotes alternos y originales historicos.

Documento de decision: `03_Expedientes/HB-001_Decision_Congelamiento_Brotes_Alternos.md`.

## Alcance

La decision usa las fichas de alcance minimo y la deuda viva `HB-001` como evidencia de que no hay contenido sustantivo local materializado.

`H-B.6` y `H-B.7` dejan de figurar como hipotesis activas.

## No cubre

No demuestra, refuta ni desarrolla las hipotesis; no diferencia semanticamente ambas; no reabre `B-001`; no descongela `B-001.5`; no modifica Canon ni documentos oficiales; no habilita uso como premisa para `REPORT_LAYER`, R4 formal, `Gamma`, Confluencia o Equivalencia de proyecciones.

## Consecuencia

Las fichas `ALC-HB6-001` y `ALC-HB7-001` quedan como registros historicos congelados.

La deuda restante es condicional: solo vuelve si aparece fuente verificable y decision explicita de reactivacion.

## D-2026-07-03-014 - Prueba externa local de Gamma_1

Estatus: decision provisional de expediente.

Fecha: 2026-07-03.

## Decision

Se acepta `GAMMA-EXT-AO-001` como prueba positiva externa local de `Gamma_1` dentro de `AO-001`.

Documento base: `03_Expedientes/AO-001_Prueba_Gamma_Externa.md`.

Auditoria: `03_Expedientes/AO-001_Auditoria_Prueba_Gamma_Externa.md`.

Decision espejo: `03_Expedientes/AO-001_Decision_Estatus_Prueba_Gamma_Externa.md`.

## Alcance

La decision acepta que `Gamma_1` puede operar fuera de `AUD-001` cuando la evidencia, el contexto, el testigo, las restricciones, las deudas y las salidas de seguridad estan declarados.

La salida aceptada es `G_AO_OP-GOV-001`, con estatus de criterio formal local de expediente dentro de `AO-001`.

## No cubre

No promueve `Gamma` a Canon, Nivel C, teoria global o documento oficial; no exporta `GAMMA-FORMAL-AUD-001` como autoridad general; no modifica Documento 04; no sustituye `AO-CASE`; no cierra Confluencia ni Equivalencia de proyecciones; no autoriza transformaciones materiales.

## Consecuencia

La deuda de prueba externa de `Gamma_1` queda atendida en grado minimo local.

Actualizacion posterior: la bateria `AO-CASE` queda atendida en grado minimo local por `D-2026-07-03-016`; el uso de R4/Gamma como puente queda acotado por `D-2026-07-03-017` y `D-2026-07-03-018`.

Permanecen abiertas promocion/exportacion general de `Gamma`, formalizacion completa de operadores del Documento 04 y cierre global de Confluencia o Equivalencia de proyecciones.

## D-2026-07-03-015 - Referencias historicas transferidas

Estatus: decision tecnica aceptada.

Fecha: 2026-07-03.

## Decision

Se acepta `AUT-002` como expediente tecnico minimo para tratar referencias historicas transferidas sin reabrir `AUT-001`.

Se acepta la clasificacion `referencia_historica_transferida` para referencias a `PSI-001*` eliminadas por `D-2026-07-03-012`.

Documento base: `03_Expedientes/AUT-002.md`.

Auditoria: `03_Expedientes/AUT-002_Auditoria_Referencias_Historicas_Transferidas.md`.

Decision espejo: `03_Expedientes/AUT-002_Decision_Referencias_Historicas_Transferidas.md`.

## Alcance

La decision permite regenerar reportes sin exigir restaurar la copia local de `PSI-001`.

Tambien permite refinar falsos bloqueos de historial en controles negativos, simulaciones, validaciones, restricciones o secciones "No cubre".

## No cubre

No reabre `AUT-001`, no restaura `PSI-001*`, no reabre psicologia dentro del Laboratorio, no abre frente clinico o patologico, no convierte Registro Historico en fuente normativa y no autoriza transformaciones materiales.

## Consecuencia

La deuda de detector/historial creada por la eliminacion local de `PSI-001*` queda atendida en grado operativo minimo.

Permanece abierta la necesidad de decision puente si alguna ruta futura requiere contenido sustantivo de psicologia.

## D-2026-07-03-016 - Casos de prueba de Algebra Operacional

Estatus: decision provisional de expediente.

Fecha: 2026-07-03.

## Decision

Se acepta `AO-CASE-BAT-001` como bateria minima provisional de casos de prueba para Algebra Operacional.

Documento base: `03_Expedientes/AO-001_Casos_Prueba_Algebra_Operacional.md`.

Auditoria: `03_Expedientes/AO-001_Auditoria_Casos_Prueba_Algebra_Operacional.md`.

Decision espejo: `03_Expedientes/AO-001_Decision_Estatus_Casos_Prueba_Algebra_Operacional.md`.

## Alcance

La decision acepta `AO-CASE-001` a `AO-CASE-006` para probar lectura no mutante, separacion decision/transformacion, deuda activa, uso local de `Gamma_1` y referencia historica transferida.

## No cubre

No modifica Documento 04, no modifica Canon, no promueve `G_AO_OP-GOV-001`, no exporta R4/Gamma, no cierra Confluencia ni Equivalencia de proyecciones y no autoriza transformaciones materiales.

## Consecuencia

La deuda "crear `AO-CASE`" queda atendida en grado minimo local.

Permanece abierta la formalizacion posterior del Documento 04.

## D-2026-07-03-017 - Criterios de uso R4/Gamma fuera de AUD-001

Estatus: decision provisional de expediente.

Fecha: 2026-07-03.

## Decision

Se acepta `AO-R4-GAMMA-USE-001` como criterio provisional para usar R4/Gamma fuera de `AUD-001` solo en grado local controlado.

Documento base: `03_Expedientes/AO-001_Criterios_Uso_R4_Gamma_Fuera_AUD.md`.

Auditoria: `03_Expedientes/AO-001_Auditoria_Criterios_Uso_R4_Gamma_Fuera_AUD.md`.

Decision espejo: `03_Expedientes/AO-001_Decision_Criterios_Uso_R4_Gamma_Fuera_AUD.md`.

## Alcance

La decision permite tres usos: referencia formal local, prueba local controlada y puente de problema.

## No cubre

No promueve `R4-FORMAL-AUD-001`, no promueve `GAMMA-FORMAL-AUD-001`, no crea Nivel C, no modifica Canon, no autoriza transformaciones materiales y no cierra Confluencia ni Equivalencia de proyecciones.

## Consecuencia

`AO-001` puede usar R4/Gamma como herramientas locales para el puente de Confluencia y Equivalencia de proyecciones.

La promocion/exportacion general permanece abierta.

## D-2026-07-03-018 - Puente local de Confluencia y Equivalencia

Estatus: decision provisional de expediente.

Fecha: 2026-07-03.

## Decision

Se acepta `AO-PPI-BRIDGE-001` como avance sustantivo local sobre Confluencia y Equivalencia de proyecciones.

Se aceptan `AO-PPI-EQ-001` y `AO-PPI-CONF-001` como pruebas locales provisionales.

Documento base: `03_Expedientes/AO-001_Puente_Confluencia_Equivalencia.md`.

Auditoria: `03_Expedientes/AO-001_Auditoria_Puente_Confluencia_Equivalencia.md`.

Decision espejo: `03_Expedientes/AO-001_Decision_Estatus_Puente_Confluencia_Equivalencia.md`.

## Alcance

La decision permite tratar el puente como evidencia local dentro de `AO-001` y orientar formalizacion posterior de Documento 04 o de una futura capa de reportes.

## No cubre

No reabre `P-PI.0`, no reabre `P-PI.1`, no cierra Confluencia global, no cierra Equivalencia global de proyecciones, no promueve R4/Gamma, no modifica Documento 04 y no autoriza transformaciones materiales.

## Consecuencia

Confluencia y Equivalencia de proyecciones dejan de estar solo como deudas abstractas y pasan a tener pruebas locales conectadas con `AO-001`.

Las deudas globales permanecen abiertas.

## D-2026-07-03-019 - Paquete minimo TCS-001

Estatus: decision teorica provisional.

Fecha: 2026-07-03.

## Decision

Se acepta el paquete minimo de `TCS-001` como avance teorico provisional no canonico.

Se aceptan `TCS-DEF-MIN-001`, `TCS-FAIL-TYP-001` y `TCS-CASE-BAT-001`.

Documento base: `03_Expedientes/TCS-001_Definiciones_Minimas.md`, `03_Expedientes/TCS-001_Tipologia_Fallos_Concordancia.md` y `03_Expedientes/TCS-001_Casos_Prueba.md`.

Auditoria: `03_Expedientes/TCS-001_Auditoria_Paquete_Minimo.md`.

Decision espejo: `03_Expedientes/TCS-001_Decision_Estatus_Paquete_Minimo.md`.

## Alcance

La decision permite trabajar `TCS-001` como marco teorico provisional con definiciones, fallos y casos iniciales.

## No cubre

No canoniza `Concordance`, no modifica Canon, no crea Nivel C, no convierte `TCS-001` en teoria completa, no usa vision papers como fuente activa y no abre frente clinico, patologico ni institucional externo.

## Consecuencia

La deuda inmediata de `TCS-001` queda atendida en grado minimo provisional.

Permanecen abiertas la formalizacion, los casos externos, la metrica de concordancia y la relacion con dominios regulados.

## D-2026-07-03-020 - Refinamiento de contexto de guardrails AUT-001

Estatus: decision tecnica aceptada.

Fecha: 2026-07-03.

## Decision

Se acepta `AUT-RISK-REFINE-002` como refinamiento de contexto de guardrails para `DO-LAB-RISK-001`.

Se acepta `AUT-VAL-012` como validacion favorable.

Documento base: `03_Expedientes/AUT-001_Refinamiento_Contexto_Guardrails.md`.

Validacion: `03_Expedientes/AUT-001_Validacion_Refinamiento_Contexto_Guardrails.md`.

Decision espejo: `03_Expedientes/AUT-001_Decision_Refinamiento_Contexto_Guardrails.md`.

## Alcance

La decision permite clasificar como advertencia controlada las menciones sensibles que aparecen en matrices de prueba, criterios de rechazo, prohibiciones explicitas, validaciones que niegan transformacion o reglas de autoridad.

## No cubre

No borra hallazgos, no modifica Canon, no modifica documentos oficiales, no reabre `AUT-001`, no autoriza transformaciones materiales y no cierra deudas documentales o conceptuales.

## Consecuencia

`DO-LAB-RISK-001` queda refinado para mantener `riesgo_activo: 0` cuando los hallazgos pertenecen a guardrails ya documentados.

`AUT-001` conserva cierre operativo con deuda documental visible.

## D-2026-07-05-001 - Reapertura operativa HXI-001

Estatus: decision provisional de expediente.

Fecha: 2026-07-05.

## Decision

Se acepta `HXI-REOPEN-001` como reapertura operativa controlada de `HXI-001`.

Documento base: `03_Expedientes/HXI-001_Reapertura_Operativa.md`.

Auditoria: `03_Expedientes/HXI-001_Auditoria_Reapertura_Operativa.md`.

Decision espejo: `03_Expedientes/HXI-001_Decision_Reapertura_Operativa.md`.

## Alcance

La decision reactiva `HXI-001` como frente activo inmediato para aplicar la compuerta provisional de admision formal posterior de `H-Xi`.

Permite usar `Xi_eval` solo como herramienta local de expediente y decidir posteriormente entre `no_admitir`, `pausar_admision`, `admitir_solo_expediente`, `mantener_Xi_eval` o `abrir_promocion_separada`.

## No cubre

No admite `H-Xi`, no canoniza `Xi`, no declara operador vigente, no modifica Canon, documentos oficiales ni Nivel C, no reabre `PSI-001`, no restaura copias locales `PSI-001*`, no habilita uso clinico, no resuelve `P-107`, no abre promocion formal y no autoriza transformaciones materiales.

## Consecuencia

`HXI-001` deja de estar en pausa operativa como frente inmediato.

El siguiente objetivo del Laboratorio es aplicar `HXI-001_Criterios_Admision_Formal_H-Xi.md` contra la evidencia ya aceptada y emitir una decision de resultado sin admision automatica.

## D-2026-07-05-002 - Resultado de compuerta de admision formal HXI-001

Estatus: decision provisional de expediente.

Fecha: 2026-07-05.

## Decision

Se acepta `HXI-GATE-001` como aplicacion de la compuerta de admision formal posterior de `H-Xi`.

Resultado de compuerta: `mantener_Xi_eval`.

Documento base: `03_Expedientes/HXI-001_Evaluacion_Compuerta_Admision_Formal.md`.

Auditoria: `03_Expedientes/HXI-001_Auditoria_Compuerta_Admision_Formal.md`.

Decision espejo: `03_Expedientes/HXI-001_Decision_Resultado_Compuerta_Admision_Formal.md`.

## Alcance

La decision conserva `Xi_eval` como herramienta local de `HXI-001` y mantiene `H-Xi` como hipotesis externa no admitida.

Permite usar dentro de `HXI-001` las salidas `redundante`, `util_acotado`, `limitado`, `no_comparable` y `bloqueado`.

## No cubre

No admite `H-Xi`, no canoniza `Xi`, no declara operador vigente, no modifica Canon, documentos oficiales ni Nivel C, no reabre `PSI-001`, no restaura copias locales `PSI-001*`, no habilita uso clinico, no resuelve `P-107`, no abre promocion formal, no prueba dominios independientes y no autoriza transformaciones materiales.

## Consecuencia

La compuerta de admision formal posterior queda aplicada.

El siguiente objetivo limpio es decidir el estatus posterior de `HXI-001`: mantenerlo abierto en mantenimiento local, pausarlo o cerrarlo tras el resultado `mantener_Xi_eval`.

## D-2026-07-05-003 - Mantenimiento local HXI-001

Estatus: decision provisional de expediente.

Fecha: 2026-07-05.

## Decision

Se acepta `HXI-MAINT-001` como regimen de mantenimiento local de `HXI-001`.

Documento base: `03_Expedientes/HXI-001_Mantenimiento_Local.md`.

Auditoria: `03_Expedientes/HXI-001_Auditoria_Mantenimiento_Local.md`.

Decision espejo: `03_Expedientes/HXI-001_Decision_Mantenimiento_Local.md`.

## Alcance

La decision mantiene `HXI-001` abierto en mantenimiento local.

Conserva `H-Xi` como hipotesis externa no admitida y `Xi_eval` como herramienta local de expediente.

`HXI-001` deja de ser frente activo inmediato.

## No cubre

No admite `H-Xi`, no canoniza `Xi`, no declara operador vigente, no reabre admision sin evidencia nueva, no modifica Canon, documentos oficiales ni Nivel C, no reabre `PSI-001`, no restaura copias locales `PSI-001*`, no habilita uso clinico, no resuelve `P-107`, no abre promocion formal y no autoriza transformaciones materiales.

## Consecuencia

El trabajo activo puede volver a `AO-001`, Confluencia, Equivalencia de proyecciones o formalizacion posterior del Documento 04.

`HXI-001` solo debe salir de mantenimiento mediante decision posterior con evidencia nueva, decision puente, cierre o promocion separada.

## D-2026-07-05-004 - Integracion R001 table checks

Estatus: decision provisional de expediente.

Fecha: 2026-07-05.

## Decision

Se acepta `R001-TABLE-CHECK-001` como herramienta local no mutante del Laboratorio.

Documento base: `03_Expedientes/R001-001_Integracion_Table_Checks.md`.

Auditoria: `03_Expedientes/R001-001_Auditoria_Integracion_Table_Checks.md`.

Decision espejo: `03_Expedientes/R001-001_Decision_Integracion_Table_Checks.md`.

## Alcance

La decision permite conservar una bateria de 20 chequeos tabulares `R-001` / `Xi`, generar reportes Markdown y JSON, ejecutarla dentro de `DO-LAB-RUN-001` y usarla como evidencia tecnica auxiliar local en `AO-001`.

## No cubre

No canoniza `Xi`, no admite `H-Xi`, no declara `Xi` operador vigente, no reabre admision de `H-Xi`, no cierra `P-200`, no resuelve `P-107`, no demuestra Equivalencia global de proyecciones, no demuestra Confluencia global, no produce cambios al Canon, a documentos oficiales ni a Nivel C, no reabre `PSI-001`, no habilita uso clinico y no autoriza transformaciones materiales.

## Consecuencia

`R001-TABLE-CHECK-001` queda integrado a `06_Automatizacion`, con prueba unitaria y reportes conservados.

`AO-001` sigue como frente operativo principal para Confluencia, Equivalencia de proyecciones y formalizacion posterior del Documento 04.

`HXI-001` permanece abierto en mantenimiento local por `D-2026-07-05-003`.

## D-2026-07-05-005 - Relacion formal R001 con AO

Estatus: decision provisional de expediente.

Fecha: 2026-07-05.

## Decision

Se acepta `R001-TB-001` como relacion formal local entre `R001-TABLE-CHECK-001` y `AO-PPI-BRIDGE-001`.

Documento base: `03_Expedientes/R001-001_Relacion_Formal_AO.md`.

Auditoria: `03_Expedientes/R001-001_Auditoria_Relacion_Formal_AO.md`.

Decision espejo: `03_Expedientes/R001-001_Decision_Relacion_Formal_AO.md`.

## Alcance

La decision permite usar `Pi_tb(C, O_adm)` como instancia local de proyeccion operacional `Pi_op`, usar `Eq_tb(C1, C2, O_adm)` como equivalencia local bajo testigo y tratar los reportes `R001` como evidencia auxiliar para `AO-PPI-EQ-001` y `AO-PPI-CONF-001`.

## No cubre

No canoniza `Xi`, no admite `H-Xi`, no declara `Xi` operador vigente, no cierra `P-200`, no resuelve `P-107`, no cierra Equivalencia global de proyecciones, no cierra Confluencia global, no produce cambios al Canon, a documentos oficiales ni a Nivel C, no incorpora contenido al Documento 04 y no autoriza transformaciones materiales.

## Consecuencia

La deuda local de relacion formal entre `R001-TABLE-CHECK-001` y `AO-001` queda atendida por `R001-TB-001`.

`AO-001` sigue abierto como frente operativo principal para profundizar Confluencia, Equivalencia de proyecciones y formalizacion posterior del Documento 04.

Las deudas globales permanecen abiertas.

## D-2026-07-05-006 - Ruta de formalizacion Doc04 y Confluencia externa

Estatus: decision provisional de expediente.

Fecha: 2026-07-05.

## Decision

Se aceptan `AO-DOC04-FORM-CHK-001` y `AO-CONF-EXT-OPTIONS-001` como evaluacion de ruta para formalizacion futura en Documento 04 y pruebas externas de Confluencia.

Documento base 1: `03_Expedientes/AO-001_Evaluacion_Formalizacion_Doc04_R001_TB.md`.

Documento base 2: `03_Expedientes/AO-001_Opciones_Prueba_Confluencia_Externa.md`.

Auditoria: `03_Expedientes/AO-001_Auditoria_Formalizacion_Doc04_Confluencia_Externa.md`.

Decision espejo: `03_Expedientes/AO-001_Decision_Ruta_Formalizacion_Doc04_Confluencia_Externa.md`.

## Alcance

La decision permite conservar una seccion candidata de `Pi_tb` y `Eq_tb` para Documento 04, sin cambiar todavia el documento oficial.

Tambien permite priorizar `EXT-CONF-001` como primera prueba externa sintetica de Confluencia y usar resultados futuros para decidir si procede una incorporacion documental acotada.

## No cubre

No modifica Documento 04, Canon ni Nivel C.

No canoniza `Xi`, no admite `H-Xi`, no cierra `P-200`, no resuelve `P-107`, no cierra Equivalencia global, no cierra Confluencia global, no abre dominios clinicos, juridicos, financieros o institucionales y no autoriza transformaciones materiales.

## Consecuencia

`R001-TB-001` queda listo como candidata formal para Documento 04, pero su incorporacion oficial queda bloqueada hasta que existan pruebas externas de Confluencia.

Nota posterior: la accion recomendada queda ejecutada por `D-2026-07-05-007` mediante `AO-EXT-CONF-EXEC-001`.

Nota posterior: la incorporacion documental acotada queda ejecutada por `D-2026-07-05-008` mediante `AO-DOC04-FORM-001`.

Las deudas globales permanecen abiertas.

## D-2026-07-05-007 - Estatus de pruebas externas de Confluencia AO-001

Estatus: decision provisional de expediente.

Fecha: 2026-07-05.

## Decision

Se acepta `AO-EXT-CONF-EXEC-001` como validacion provisional ejecutada de pruebas externas no reguladas de Confluencia.

Documento base: `03_Expedientes/AO-001_Pruebas_Externas_Confluencia.md`.

Auditoria: `03_Expedientes/AO-001_Auditoria_Pruebas_Externas_Confluencia.md`.

Decision espejo: `03_Expedientes/AO-001_Decision_Estatus_Pruebas_Externas_Confluencia.md`.

Evidencia ejecutable: `06_Automatizacion/ao_ext_confluence.py`.

Fixture: `06_Automatizacion/fixtures/ao_ext_confluence_cases.json`.

Reportes: `06_Automatizacion/reportes/ao_ext_confluence_report.md` y `06_Automatizacion/reportes/ao_ext_confluence_report.json`.

## Alcance

La decision acepta `EXT-CONF-001` ejecutado sobre tabla de datos sintetica y `EXT-CONF-002` agregado y ejecutado sobre paquete de software de juguete.

Tambien acepta `AO-EXT-CONF-001` como herramienta no mutante integrada a `06_Automatizacion` y sus resultados locales como evidencia de apoyo para `AO-PPI-BRIDGE-001`.

## No cubre

No cierra Confluencia global, no cierra Equivalencia global de proyecciones, no modifica Documento 04, no incorpora `Pi_tb` / `Eq_tb` a Documento 04, no modifica Canon, no crea Nivel C, no promueve ni exporta `R4-FORMAL-AUD-001`, no promueve ni exporta `GAMMA-FORMAL-AUD-001`, no canoniza ni cierra `TCS-001`, no abre dominios clinicos, juridicos, financieros o institucionales y no autoriza transformaciones materiales.

## Consecuencia

`EXT-CONF-001` queda ejecutado.

`EXT-CONF-002` queda agregado como segunda prueba externa no regulada.

La condicion minima de dos pruebas externas queda atendida en grado local, pero no basta por si sola para modificar Documento 04.

Nota posterior: `D-2026-07-05-008` usa esta evidencia para incorporar `Pi_tb` / `Eq_tb` al Documento 04 solo en grado acotado bajo testigo.

Permanecen abiertas Confluencia global, Equivalencia global, formalizacion posterior de Documento 04, exportacion general de R4/Gamma y maduracion de `TCS-001`.

## D-2026-07-05-008 - Formalizacion acotada en Documento 04

Estatus: decision documental acotada.

Fecha: 2026-07-05.

## Decision

Se acepta `AO-DOC04-FORM-001` como incorporacion acotada al Documento 04.

Documento base: `03_Expedientes/AO-001_Formalizacion_Acotada_Doc04_R001_TB.md`.

Auditoria: `03_Expedientes/AO-001_Auditoria_Formalizacion_Acotada_Doc04.md`.

Decision espejo: `03_Expedientes/AO-001_Decision_Formalizacion_Acotada_Doc04.md`.

Documento modificado: `02_Documentos/04_Algebra_Operacional.md`.

## Alcance

La decision incorpora `Pi_tb` y `Eq_tb` como proyeccion tabular local bajo testigo.

La incorporacion queda apoyada por `R001-TB-001`, `AO-DOC04-FORM-CHK-001` y `AO-EXT-CONF-EXEC-001`.

## No cubre

No cierra `P-200`, no resuelve `P-107`, no cierra Equivalencia global de proyecciones, no cierra Confluencia global, no admite `H-Xi`, no canoniza `Xi`, no promueve R4/Gamma, no crea Nivel C y no autoriza transformaciones materiales.

## Consecuencia

La deuda "formalizacion posterior de Documento 04" queda atendida solo en grado acotado para `Pi_tb` / `Eq_tb`.

Permanecen abiertas las formalizaciones posteriores de Confluencia, Equivalencia global, R4/Gamma, `TCS-001` y cualquier especificacion futura de proyecciones/reportes.

## D-2026-07-05-009 - Compuerta de exportacion R4/Gamma

Estatus: decision provisional de expediente.

Fecha: 2026-07-05.

## Decision

Se acepta `AO-R4-GAMMA-EXPORT-GATE-001` como compuerta provisional de exportacion de R4/Gamma.

Documento base: `03_Expedientes/AO-001_Compuerta_Exportacion_R4_Gamma.md`.

Auditoria: `03_Expedientes/AO-001_Auditoria_Compuerta_Exportacion_R4_Gamma.md`.

Decision espejo: `03_Expedientes/AO-001_Decision_Compuerta_Exportacion_R4_Gamma.md`.

## Resultado

La exportacion general de `R4-FORMAL-AUD-001` y `GAMMA-FORMAL-AUD-001` queda bloqueada.

Se acepta solo el `perfil_restringido_interoperable` como avance local controlado.

## No cubre

No promueve R4/Gamma a Canon, no promueve R4/Gamma a Nivel C, no modifica Documento 04, no crea una teoria global de R4 o Gamma, no cierra Confluencia global, no cierra Equivalencia global y no autoriza transformaciones materiales.

## Consecuencia

La deuda de exportacion general de R4/Gamma no queda cerrada.

Queda refinada: antes de reintentar exportacion general debe existir dominio externo, semantica independiente del expediente, pruebas externas suficientes y relacion con Confluencia/Equivalencia global.

## D-2026-07-05-010 - Maduracion provisional TCS-001

Estatus: decision teorica provisional.

Fecha: 2026-07-05.

## Decision

Se acepta `TCS-MAT-PROV-001` como avance de maduracion provisional de `TCS-001`.

Documento base: `03_Expedientes/TCS-001_Maduracion_Provisional.md`.

Auditoria: `03_Expedientes/TCS-001_Auditoria_Maduracion_Provisional.md`.

Decision espejo: `03_Expedientes/TCS-001_Decision_Maduracion_Provisional.md`.

## Componentes aceptados

- `TCS-METRIC-PROV-001`: metrica cualitativa provisional.
- `TCS-EXT-CASE-001`: casos externos no regulados.
- `TCS-AUTH-CONF-001`: patron de conflicto de autoridades validas.

## No cubre

No canoniza `Concordance`, no crea Nivel C, no modifica documentos oficiales, no abre dominios clinicos, juridicos, financieros o institucionales, no convierte `TCS-001` en teoria completa y no cierra la deuda de maduracion de TCS.

## Consecuencia

La deuda de maduracion de `TCS-001` queda reducida, pero permanece abierta.

Los siguientes avances deben enfocarse en semantica formal, mas casos externos no regulados y relacion controlada con `AO-001` / `C-001`.

## D-2026-07-05-011 - Apertura de MOC-001

Estatus: decision provisional de expediente.

Fecha: 2026-07-05.

## Decision

Se abre `MOC-001` como expediente integrador teorico-operativo, no canonico, no clinico y no regulado.

Documento base: `03_Expedientes/MOC-001.md`.

Auditoria: `03_Expedientes/MOC-001_Auditoria_Apertura.md`.

Decision espejo: `03_Expedientes/MOC-001_Decision_Apertura.md`.

## Alcance

La decision permite construir una primera version del Modelo Operativo de Concordancia con operadores locales, metricas, protocolo, simulaciones no mutantes y diseno empirico futuro.

## No cubre

No admite `H-Xi`, no canoniza `Xi`, no declara operador general vigente, no modifica Canon, documentos oficiales ni Nivel C, no modifica `Documento 04`, no reabre `PSI-001`, no abre trabajo clinico y no autoriza transformaciones materiales.

## Consecuencia

`MOC-001` queda abierto como frente integrador provisional conectado con `HXI-001`, `TCS-001` y `AO-001`.

## D-2026-07-05-012 - Formalizacion local de Xi_eval para MOC-001

Estatus: decision provisional de expediente.

Fecha: 2026-07-05.

## Decision

Se acepta `MOC-XI-EVAL-FORMAL-001` como formalizacion local de `Xi_eval` dentro de `MOC-001`.

Documento base: `03_Expedientes/MOC-001_Formalizacion_Xi_eval.md`.

Auditoria: `03_Expedientes/MOC-001_Auditoria_Formalizacion_Xi_eval.md`.

Decision espejo: `03_Expedientes/MOC-001_Decision_Formalizacion_Xi_eval.md`.

## Alcance

La decision permite usar `Xi_eval_MOC` para evaluar casos sinteticos no clinicos con entradas, salidas, reglas e invariantes definidos.

## No cubre

No admite `H-Xi`, no canoniza `Xi`, no declara operador general vigente, no habilita uso clinico, no evalua personas reales, no modifica documentos oficiales y no cierra `P-107`.

## Consecuencia

`Xi_eval` queda disponible para `MOC-001` solo como operador local de evaluacion.

## D-2026-07-05-013 - Metricas y protocolo MOC-001

Estatus: decision provisional de expediente.

Fecha: 2026-07-05.

## Decision

Se aceptan `MOC-METRIC-STATE-001` y `MOC-EVAL-PROTO-001` como metricas y protocolo provisional de evaluacion para `MOC-001`.

Documentos base:

- `03_Expedientes/MOC-001_Metricas_Estados.md`.
- `03_Expedientes/MOC-001_Protocolo_Evaluacion.md`.

Auditoria: `03_Expedientes/MOC-001_Auditoria_Metricas_Protocolo.md`.

Decision espejo: `03_Expedientes/MOC-001_Decision_Metricas_Protocolo.md`.

## Alcance

La decision permite clasificar casos sinteticos no clinicos en estados MOC y comparar salidas entre evaluadores simulados.

## No cubre

No produce medicion universal, no valida empiricamente el modelo, no evalua personas reales, no abre uso clinico y no canoniza `TCS-001`.

## Consecuencia

`MOC-001` puede pasar a bateria de casos y simulacion no mutante.

## D-2026-07-05-014 - Simulacion no mutante MOC-001

Estatus: decision tecnica provisional.

Fecha: 2026-07-05.

## Decision

Se acepta `MOC-EVAL-001` como simulador no mutante de `MOC-001`.

Documento base: `03_Expedientes/MOC-001_Casos_No_Clinicos.md`.

Auditoria: `03_Expedientes/MOC-001_Auditoria_Simulacion_Software.md`.

Decision espejo: `03_Expedientes/MOC-001_Decision_Simulacion_Software.md`.

Evidencia ejecutable:

- `06_Automatizacion/moc_eval.py`.
- `06_Automatizacion/fixtures/moc_cases.json`.
- `06_Automatizacion/test_moc_eval.py`.

Reportes:

- `06_Automatizacion/reportes/moc_eval_report.md`.
- `06_Automatizacion/reportes/moc_eval_report.json`.

## Alcance

La decision permite ejecutar casos sinteticos no clinicos, generar reportes y sumar `MOC-EVAL-001` a `DO-LAB-RUN-001` como paso de lectura.

## No cubre

No valida empiricamente el MOC, no evalua personas reales, no autoriza transformaciones, no modifica Canon ni documentos oficiales, no admite `H-Xi`, no canoniza `Xi` y no cierra deudas globales.

## Consecuencia

`MOC-001` cuenta con una superficie ejecutable provisional y no mutante.

## D-2026-07-05-015 - Diseno empirico futuro MOC-001

Estatus: decision teorica provisional.

Fecha: 2026-07-05.

## Decision

Se acepta `MOC-EMP-STUDY-001` como diseno documental de estudio empirico futuro para `MOC-001`.

Documento base: `03_Expedientes/MOC-001_Disenio_Estudio_Empirico.md`.

Auditoria: `03_Expedientes/MOC-001_Auditoria_Disenio_Estudio_Empirico.md`.

Decision espejo: `03_Expedientes/MOC-001_Decision_Disenio_Estudio_Empirico.md`.

## Alcance

La decision permite conservar una ruta futura de comparacion con baselines no clinicos mediante casos sinteticos, consistencia entre evaluadores y clasificacion de desacuerdos.

## No cubre

No ejecuta estudio empirico real, no recluta personas, no evalua casos reales, no abre dominios clinicos ni regulados, no declara validez estadistica y no canoniza el MOC.

## Consecuencia

`MOC-001` queda avanzado como frente integrador provisional con formalizacion, metricas, protocolo, simulacion y diseno empirico futuro.

## D-2026-07-05-016 - Ejecucion de primera ruta valida MOC-001

Estatus: decision provisional de expediente.

Fecha: 2026-07-05.

## Decision

Se acepta `MOC-ROUTE-EXEC-001` como ejecucion favorable de la primera ruta valida de `MOC-001`.

Documento base: `03_Expedientes/MOC-001_Ejecucion_Ruta_Valida_001.md`.

Auditoria: `03_Expedientes/MOC-001_Auditoria_Ejecucion_Ruta_Valida_001.md`.

Decision espejo: `03_Expedientes/MOC-001_Decision_Ejecucion_Ruta_Valida_001.md`.

## Alcance

La decision acepta que `Xi_eval_MOC`, estados metricos, protocolo de evaluacion y software no mutante fueron probados localmente con casos sinteticos no clinicos.

## Resultado

`MOC-EVAL-001` ejecuta 7 casos, aprueba 7 y no registra hallazgos.

El protocolo registra 4 coincidencias exactas, 3 coincidencias parciales y 0 desacuerdos justificados.

`DO-LAB-RUN-001` conserva `MOC-EVAL-001` como paso `ok` y `DO-LAB-RISK-001` mantiene `risk_blocks_closure: false`.

## No cubre

No valida empiricamente el MOC, no evalua personas reales, no abre uso clinico, no admite `H-Xi`, no canoniza `Xi`, no crea Nivel C, no modifica `Documento 04`, no cierra Confluencia global, no cierra Equivalencia global y no autoriza transformaciones materiales.

## Consecuencia

La primera ruta valida queda ejecutada. La siguiente accion valida es elegir una ruta posterior dentro de `MOC-001` sin salir del alcance no canonico, no clinico y no regulado.

## D-2026-07-05-017 - Siguientes rutas validas MOC-001

Estatus: decision provisional de expediente.

Fecha: 2026-07-05.

## Decision

Se acepta `MOC-NEXT-ROUTES-001` como matriz provisional de rutas posteriores para `MOC-001`.

Documento base: `03_Expedientes/MOC-001_Siguientes_Rutas_Validas.md`.

Auditoria: `03_Expedientes/MOC-001_Auditoria_Siguientes_Rutas_Validas.md`.

Decision espejo: `03_Expedientes/MOC-001_Decision_Siguientes_Rutas_Validas.md`.

## Ruta recomendada

La siguiente ruta recomendada es `MOC-ROUTE-002`: ampliar la bateria sintetica no clinica con desacuerdos justificados y casos limite.

## No cubre

No ejecuta todavia `MOC-ROUTE-002`, no modifica software, no abre estudio empirico real, no admite `H-Xi`, no canoniza `Xi`, no abre uso clinico, no modifica `Documento 04`, no crea Nivel C y no cierra problemas globales.

## Consecuencia

`MOC-001` queda listo para avanzar ordenadamente hacia ampliacion de casos sinteticos no clinicos antes de formalizar puentes `MOC/TCS` o `MOC/AO`.

## D-2026-07-05-018 - Ejecucion de ruta 002 MOC-001

Estatus: decision provisional de expediente.

Fecha: 2026-07-05.

## Decision

Se acepta `MOC-ROUTE-002` como ejecucion favorable de la ampliacion de bateria sintetica no clinica de `MOC-001`.

Documento base: `03_Expedientes/MOC-001_Ejecucion_Ruta_002.md`.

Auditoria: `03_Expedientes/MOC-001_Auditoria_Ejecucion_Ruta_002.md`.

Decision espejo: `03_Expedientes/MOC-001_Decision_Ejecucion_Ruta_002.md`.

## Alcance

La decision acepta la incorporacion de `MOC-CASE-008` a `MOC-CASE-011` y la actualizacion de `MOC-EVAL-001` para reportar desacuerdos justificados y casos limite.

## Resultado

`MOC-EVAL-001` ejecuta 11 casos, aprueba 11 y no registra fallos.

El protocolo registra 6 coincidencias exactas, 3 coincidencias parciales y 2 desacuerdos justificados.

`DO-LAB-RUN-001` conserva `MOC-EVAL-001` como paso `ok` y `DO-LAB-RISK-001` mantiene `risk_blocks_closure: false`.

## No cubre

No valida empiricamente el MOC, no evalua personas reales, no abre uso clinico, no admite `H-Xi`, no canoniza `Xi`, no crea Nivel C, no modifica `Documento 04`, no cierra Confluencia global, no cierra Equivalencia global y no autoriza transformaciones materiales.

## Consecuencia

`MOC-ROUTE-002` queda cerrada como ruta ejecutada favorablemente.

La siguiente decision valida debe elegir entre rutas posteriores; la recomendacion tecnica pasa a `MOC-ROUTE-003`, formalizar puente `MOC/TCS`.

## D-2026-07-05-019 - Rutas posteriores a ruta 002 MOC-001

Estatus: decision provisional de expediente.

Fecha: 2026-07-05.

## Decision

Se acepta `MOC-NEXT-ROUTES-002` como matriz provisional de rutas posteriores despues de `MOC-ROUTE-002`.

Documento base: `03_Expedientes/MOC-001_Rutas_Posteriores_Ruta_002.md`.

Auditoria: `03_Expedientes/MOC-001_Auditoria_Rutas_Posteriores_Ruta_002.md`.

Decision espejo: `03_Expedientes/MOC-001_Decision_Rutas_Posteriores_Ruta_002.md`.

## Ruta recomendada

La siguiente ruta recomendada es `MOC-ROUTE-003`: formalizar puente `MOC/TCS` a partir de la bateria ampliada y los casos limite de `MOC-ROUTE-002`.

## No cubre

No ejecuta todavia `MOC-ROUTE-003`, no crea puente `MOC/TCS`, no modifica software, no abre estudio empirico real, no admite `H-Xi`, no canoniza `Xi`, no abre uso clinico, no modifica `Documento 04`, no crea Nivel C y no cierra problemas globales.

## Consecuencia

`MOC-001` queda listo para avanzar ordenadamente hacia puente formal `MOC/TCS`, manteniendo la bateria ampliada como evidencia local no canonica.

## D-2026-07-05-020 - Puente formal MOC/TCS

Estatus: decision provisional de expediente.

Fecha: 2026-07-05.

## Decision

Se acepta `MOC-TCS-BRIDGE-001` como formalizacion ejecutable local de `MOC-ROUTE-003`.

Documento base: `03_Expedientes/MOC-001_Puente_Formal_MOC_TCS.md`.

Auditoria: `03_Expedientes/MOC-001_Auditoria_Puente_Formal_MOC_TCS.md`.

Decision espejo: `03_Expedientes/MOC-001_Decision_Puente_Formal_MOC_TCS.md`.

## Alcance

La decision acepta cuatro operadores locales:

- `OP_MOC_XI`;
- `OP_MOC_TCS`;
- `OP_MOC_STATE`;
- `OP_MOC_AGREEMENT`.

Tambien acepta que `MOC-EVAL-001` emita `operator_trace` para conservar regla ganadora, prioridad aplicada y deudas TCS.

## Resultado

La formalizacion deja de depender de una formula conceptual sin criterio de combinacion.

Cada caso sintetico no clinico puede evaluarse mediante operadores con entradas normalizadas, prioridad explicita, regla de conflicto, salida unica y traza auditable.

## No cubre

No valida empiricamente el MOC, no evalua personas reales, no abre uso clinico, no admite `H-Xi`, no canoniza `Xi`, no crea Nivel C, no modifica `Documento 04`, no cierra Confluencia global, no cierra Equivalencia global, no formaliza puente `MOC/AO` y no autoriza transformaciones materiales.

## Consecuencia

`MOC-ROUTE-003` queda aceptada como avance formal local.

La siguiente ruta recomendada pasa a `MOC-ROUTE-004`: formalizar puente `MOC/AO`.

## D-2026-07-05-021 - Rutas posteriores a ruta 003 MOC-001

Estatus: decision provisional de expediente.

Fecha: 2026-07-05.

## Decision

Se acepta `MOC-NEXT-ROUTES-003` como matriz provisional de rutas posteriores despues de `MOC-ROUTE-003`.

Documento base: `03_Expedientes/MOC-001_Rutas_Posteriores_Ruta_003.md`.

Auditoria: `03_Expedientes/MOC-001_Auditoria_Rutas_Posteriores_Ruta_003.md`.

Decision espejo: `03_Expedientes/MOC-001_Decision_Rutas_Posteriores_Ruta_003.md`.

## Ruta recomendada

La siguiente ruta recomendada es `MOC-ROUTE-004`: formalizar puente `MOC/AO` usando `operator_trace` como evidencia local de regla ganadora.

## No cubre

No ejecuta todavia `MOC-ROUTE-004`, no crea puente `MOC/AO`, no modifica software, no abre estudio empirico real, no admite `H-Xi`, no canoniza `Xi`, no abre uso clinico, no modifica `Documento 04`, no crea Nivel C y no cierra problemas globales.

## Consecuencia

`MOC-001` queda listo para avanzar ordenadamente hacia puente formal `MOC/AO`, manteniendo `MOC/TCS` como formalizacion ejecutable local.

## D-2026-07-05-022 - Puente formal MOC/AO

Estatus: decision provisional de expediente.

Fecha: 2026-07-05.

## Decision

Se acepta `MOC-AO-BRIDGE-001` como formalizacion local de `MOC-ROUTE-004`.

Documento base: `03_Expedientes/MOC-001_Puente_Formal_MOC_AO.md`.

Auditoria: `03_Expedientes/MOC-001_Auditoria_Puente_Formal_MOC_AO.md`.

Decision espejo: `03_Expedientes/MOC-001_Decision_Puente_Formal_MOC_AO.md`.

## Alcance

La decision acepta que `operator_trace` funcione como evidencia local de regla ganadora mediante `Pi_moc_trace`.

Tambien acepta que `MOC-EVAL-001` emita `ao_bridge` para proyectar cada caso hacia roles operacionales de `AO-001`:

- `evidencia_auxiliar_equivalencia_local`;
- `evidencia_auxiliar_con_deuda`;
- `evidencia_friccion_confluencia_local`;
- `deuda_global_no_cierre`;
- `bloqueo_seguridad_sin_uso_positivo`;
- `bloqueo_comparabilidad_sin_uso_positivo`.

## Resultado

El puente permite usar la regla ganadora del MOC como testigo local para discutir equivalencia local, friccion de confluencia o deuda global en `AO-001`.

Cada proyeccion conserva `case_id`, regla `Xi`, regla `TCS`, regla de estado, familia de estado, rol AO y banderas negativas de cierre global.

## No cubre

No valida empiricamente el MOC, no evalua personas reales, no abre uso clinico, no admite `H-Xi`, no canoniza `Xi`, no crea Nivel C, no modifica `Documento 04`, no cierra Confluencia global, no cierra Equivalencia global, no promueve R4/Gamma, no autoriza transformaciones materiales y no convierte `operator_trace` en autoridad canonica.

## Consecuencia

`MOC-ROUTE-004` queda aceptada como avance formal local.

`MOC-EVAL-001` conserva `operator_trace` y agrega `ao_bridge` en reportes Markdown/JSON.

La siguiente ruta recomendada pasa a `MOC-ROUTE-005`: refinar el protocolo de evaluadores usando `operator_trace` y `ao_bridge` como evidencia local controlada.

## D-2026-07-05-023 - Rutas posteriores a ruta 004 MOC-001

Estatus: decision provisional de expediente.

Fecha: 2026-07-05.

## Decision

Se acepta `MOC-NEXT-ROUTES-004` como matriz provisional de rutas posteriores despues de `MOC-ROUTE-004`.

Documento base: `03_Expedientes/MOC-001_Rutas_Posteriores_Ruta_004.md`.

Auditoria: `03_Expedientes/MOC-001_Auditoria_Rutas_Posteriores_Ruta_004.md`.

Decision espejo: `03_Expedientes/MOC-001_Decision_Rutas_Posteriores_Ruta_004.md`.

## Ruta recomendada

La siguiente ruta recomendada es `MOC-ROUTE-005`: refinar el protocolo de evaluadores para que use `operator_trace`, `Pi_moc_trace` y `ao_bridge` como evidencia local de desempate, desacuerdo justificado y trazabilidad de regla ganadora.

## No cubre

No ejecuta todavia `MOC-ROUTE-005`, no crea estudio empirico real, no admite `H-Xi`, no canoniza `Xi`, no abre uso clinico, no modifica `Documento 04`, no crea Nivel C, no exporta R4/Gamma y no cierra problemas globales.

## Consecuencia

`MOC-001` queda listo para avanzar ordenadamente hacia refinamiento de protocolo evaluador sin salir del alcance no canonico, no clinico, no regulado y no mutante.

## D-2026-07-05-024 - Ejecucion de ruta 005 MOC-001

Estatus: decision provisional de expediente.

Fecha: 2026-07-05.

## Decision

Se acepta `MOC-ROUTE-005` como ejecucion favorable del refinamiento del protocolo de evaluadores.

Documento base: `03_Expedientes/MOC-001_Protocolo_Evaluacion_v0_2.md`.

Ejecucion: `03_Expedientes/MOC-001_Ejecucion_Ruta_005.md`.

Auditoria: `03_Expedientes/MOC-001_Auditoria_Ejecucion_Ruta_005.md`.

Decision espejo: `03_Expedientes/MOC-001_Decision_Ejecucion_Ruta_005.md`.

## Alcance

La decision acepta `MOC-EVAL-PROTO-002` como protocolo v0.2 local, no canonico y no empirico.

Tambien acepta que `MOC-EVAL-001` emita `protocol_v02` por caso y `protocol_v02_summary` por reporte.

## Resultado

La ejecucion local conserva 11 casos aprobados, 0 fallos, 6 coincidencias exactas, 3 coincidencias parciales y 2 desacuerdos justificados.

El protocolo v0.2 registra 2 casos con `review_required` y 2 casos con `blocked_positive_use`.

## No cubre

No valida empiricamente el MOC, no evalua personas reales, no abre uso clinico, no admite `H-Xi`, no canoniza `Xi`, no crea Nivel C, no modifica `Documento 04`, no cierra Confluencia global, no cierra Equivalencia global, no exporta R4/Gamma y no autoriza transformaciones materiales.

## Consecuencia

`MOC-ROUTE-005` queda aceptada como avance local de reproducibilidad.

La siguiente ruta recomendada pasa a `MOC-ROUTE-006`: preparar protocolo documental de piloto empirico futuro, sin ejecucion real.

## D-2026-07-05-025 - Rutas posteriores a ruta 005 MOC-001

Estatus: decision provisional de expediente.

Fecha: 2026-07-05.

## Decision

Se acepta `MOC-NEXT-ROUTES-005` como matriz provisional de rutas posteriores despues de `MOC-ROUTE-005`.

Documento base: `03_Expedientes/MOC-001_Rutas_Posteriores_Ruta_005.md`.

Auditoria: `03_Expedientes/MOC-001_Auditoria_Rutas_Posteriores_Ruta_005.md`.

Decision espejo: `03_Expedientes/MOC-001_Decision_Rutas_Posteriores_Ruta_005.md`.

## Ruta recomendada

La siguiente ruta recomendada es `MOC-ROUTE-006`: preparar protocolo documental de piloto empirico futuro, sin ejecucion real.

## No cubre

No ejecuta estudio empirico real, no recluta personas, no evalua personas reales, no abre uso clinico, no admite `H-Xi`, no canoniza `Xi`, no modifica `Documento 04`, no crea Nivel C, no exporta R4/Gamma y no cierra problemas globales.

## Consecuencia

`MOC-001` queda listo para avanzar hacia preparacion documental de piloto futuro manteniendo el alcance provisional y no regulado.

## D-2026-07-06-001 - Protocolo documental de piloto empirico futuro MOC-001

Estatus: decision provisional de expediente.

Fecha: 2026-07-06.

## Decision

Se acepta `MOC-EMP-PILOT-PROTO-001` como protocolo documental preparado para un piloto empirico futuro, sin ejecucion real.

Documento base: `03_Expedientes/MOC-001_Protocolo_Piloto_Empirico_Futuro.md`.

Auditoria: `03_Expedientes/MOC-001_Auditoria_Protocolo_Piloto_Empirico_Futuro.md`.

Decision espejo: `03_Expedientes/MOC-001_Decision_Protocolo_Piloto_Empirico_Futuro.md`.

## Alcance

La decision permite conservar un protocolo futuro para comparar MOC contra baselines simples en tareas sinteticas no clinicas.

Tambien fija una compuerta: cualquier ejecucion futura requiere decision separada que confirme dominio sintetico no clinico, ausencia de casos reales, ausencia de datos personales, ausencia de uso clinico y ausencia de modificacion documental automatica.

## No cubre

No ejecuta estudio empirico real, no recluta evaluadores, no evalua personas reales, no recopila datos personales, no abre uso clinico, no admite `H-Xi`, no canoniza `Xi`, no promueve MOC a Canon o Nivel C, no modifica `Documento 04`, no cierra Confluencia global, no cierra Equivalencia global, no exporta R4/Gamma y no autoriza transformaciones materiales.

## Consecuencia

`MOC-ROUTE-006` queda preparada como protocolo documental.

La ejecucion real del piloto queda bloqueada hasta decision posterior explicita.

## D-2026-07-06-002 - Rutas posteriores a ruta 006 MOC-001

Estatus: decision provisional de expediente.

Fecha: 2026-07-06.

## Decision

Se acepta `MOC-NEXT-ROUTES-006` como matriz provisional de rutas posteriores despues de preparar el protocolo documental de piloto empirico futuro.

Documento base: `03_Expedientes/MOC-001_Rutas_Posteriores_Ruta_006.md`.

Auditoria: `03_Expedientes/MOC-001_Auditoria_Rutas_Posteriores_Ruta_006.md`.

Decision espejo: `03_Expedientes/MOC-001_Decision_Rutas_Posteriores_Ruta_006.md`.

## Ruta recomendada

La siguiente ruta recomendada es `MOC-ROUTE-007`: decidir compuerta de autorizacion o no autorizacion del piloto futuro, sin ejecutarlo.

## No cubre

No ejecuta piloto empirico, no recluta evaluadores, no evalua personas reales, no recopila datos personales, no abre uso clinico, no admite `H-Xi`, no canoniza `Xi`, no modifica `Documento 04`, no crea Nivel C y no cierra problemas globales.

## Consecuencia

`MOC-001` queda listo para decidir, en una ruta posterior, si el piloto permanece bloqueado, requiere mas preparacion documental o puede ser autorizado bajo condiciones estrictas.

## D-2026-07-06-003 - Compuerta de autorizacion de ejecucion de piloto MOC-001

Estatus: decision provisional de expediente.

Fecha: 2026-07-06.

## Decision

Se acepta `MOC-GATE-PILOT-EXEC-001` como compuerta aplicada a la ejecucion del piloto empirico futuro.

Resultado: no se autoriza ejecucion real.

Documento base: `03_Expedientes/MOC-001_Compuerta_Autorizacion_Ejecucion_Piloto.md`.

Auditoria: `03_Expedientes/MOC-001_Auditoria_Compuerta_Autorizacion_Ejecucion_Piloto.md`.

Decision espejo: `03_Expedientes/MOC-001_Decision_Compuerta_Autorizacion_Ejecucion_Piloto.md`.

## Declaracion de compuerta

```text
piloto_autorizado = false
resultado_compuerta = no_autorizar_ejecucion
ejecucion_permitida = false
transformacion_permitida = false
```

## Razon

La evidencia local permite preparar el piloto, pero no autoriza ejecutarlo.

Siguen pendientes paquete congelado de casos, plantilla de respuesta, version congelada de reglas/protocolo, metodo de registro sin datos personales, responsable de auditoria y criterio operativo completo para participantes/evaluadores.

## No cubre

No ejecuta piloto empirico, no recluta evaluadores, no recopila respuestas reales, no evalua personas reales, no recopila datos personales, no abre uso clinico, no admite `H-Xi`, no canoniza `Xi`, no modifica `Documento 04`, no crea Nivel C, no cierra Confluencia global, no cierra Equivalencia global y no presenta validacion empirica del MOC.

## Consecuencia

`MOC-ROUTE-007` queda ejecutada como compuerta de no autorizacion.

La siguiente ruta recomendada es `MOC-ROUTE-008`: preparar paquete documental pre-ejecucion de piloto, sin reclutamiento ni ejecucion.

## D-2026-07-06-004 - Paquete documental pre-ejecucion de piloto MOC-001

Estatus: decision provisional de expediente.

Fecha: 2026-07-06.

## Decision

Se acepta `MOC-PREEXEC-PACK-001` como paquete documental pre-ejecucion de piloto.

Documento base: `03_Expedientes/MOC-001_Paquete_PreEjecucion_Piloto.md`.

Auditoria: `03_Expedientes/MOC-001_Auditoria_Paquete_PreEjecucion_Piloto.md`.

Decision espejo: `03_Expedientes/MOC-001_Decision_Paquete_PreEjecucion_Piloto.md`.

## Componentes aceptados

- `MOC-SEM-PROV-001`: semantica provisional local del MOC.
- `MOC-OPS-FORMAL-001`: tabla de operaciones formales.
- `MOC-PILOT-CASE-FREEZE-001`: paquete congelado de 11 casos sinteticos.
- `MOC-PILOT-RESPONSE-TPL-001`: plantilla de respuesta de evaluadores.
- `MOC-PILOT-RULE-FREEZE-001`: version congelada de reglas/protocolo.

## Resultado

`MOC-ROUTE-008` queda ejecutada como preparacion documental pre-ejecucion.

El piloto empirico real permanece no autorizado.

```text
piloto_autorizado = false
ejecucion_permitida = false
reclutamiento_permitido = false
respuestas_reales_permitidas = false
datos_personales_permitidos = false
uso_clinico = false
```

## No cubre

No ejecuta piloto empirico, no recluta evaluadores, no recopila respuestas reales, no evalua personas reales, no recopila datos personales, no abre uso clinico, no admite `H-Xi`, no canoniza `Xi`, no modifica `Documento 04`, no crea Nivel C, no cierra Confluencia global, no cierra Equivalencia global y no presenta validacion empirica del MOC.

## Consecuencia

La siguiente ruta recomendada es `MOC-ROUTE-009`: preparar metodo de registro sin datos personales y matriz de auditoria de piloto, sin reclutamiento ni ejecucion.
