# 01 - Canon

Estatus: documento oficial consolidado.

Decision de consolidacion: `D-2026-07-03-011`.

Fuentes principales: `01_Canon/M-000_Reglas_Fundamentales.md`, `01_Canon/M-001_Auditoria_Arquitectonica.md`, `SRC-007`, `SRC-008`, `SRC-010`, `SRC-012`, `SRC-013`, `SRC-023`, `REC-001`.

## Definicion

El Canon contiene las reglas fundamentales que limitan como cambia el Laboratorio Concordante.

No contiene todo el conocimiento del proyecto. Su funcion es impedir promociones automaticas, mezcla de niveles, cierres dogmaticos, dependencias invisibles y cambios sin trazabilidad.

## Canon vigente de gobierno

El Canon local vigente vive en `01_Canon`:

- `M-000`: reglas fundamentales del repositorio.
- `M-001`: auditoria arquitectonica.

Este documento incorpora el canon metodologico historico como contenido documental oficial y como mapa de criterios. Esa incorporacion no renombra automaticamente los archivos canonicos vigentes ni sustituye decisiones ya registradas.

## Reglas vigentes de gobierno local

### M-000 - Reglas fundamentales

`M-000` establece:

- separacion de niveles;
- estatus obligatorio de afirmaciones;
- no promocion automatica;
- trazabilidad minima;
- historial no operativo;
- registro de deuda conceptual;
- cierre y reapertura solo con decision explicita.

### M-001 - Auditoria arquitectonica

`M-001` establece que una intervencion debe ser auditada por coherencia, estatus, dependencias, deudas y efectos sobre el repositorio vigente.

La auditoria minima lee estado, Canon y fuentes afectadas; clasifica afirmaciones; detecta dependencias no registradas; y declara impacto sobre documentos, expedientes, estado o Canon.

## Canon metodologico historico incorporado

Las fuentes historicas `SRC-010`, `SRC-012`, `SRC-013` y `SRC-023` contienen un canon metodologico previo. Queda incorporado aqui como contenido oficial del Documento 01, con esta frontera:

- puede orientar auditorias y expedientes;
- puede fundar deudas refinadas;
- puede servir como fuente para futuras promociones;
- no cambia por si mismo el contenido de `01_Canon`;
- no reabre expedientes cerrados sin decision explicita.

### C-000 historico - Principio de alcance

El Laboratorio estudia las condiciones bajo las cuales una explicacion puede ser auditada, comparada, modificada y rechazada mediante procedimientos explicitos.

No estudia directamente la realidad fisica. No determina que teoria es verdadera. No produce teorias cientificas. Produce protocolos para evaluar estructuras de justificacion.

Garantiza, bajo condiciones definidas:

- terminacion procedimental;
- reproducibilidad;
- trazabilidad;
- coherencia interna;
- auditabilidad.

No garantiza:

- verdad;
- correspondencia con la realidad;
- exito predictivo;
- superioridad filosofica.

Principio de neutralidad: dos modelos incompatibles pueden recibir el mismo dictamen si poseen la misma estructura de auditabilidad.

### M-000 historico - Auditoria interna

El Laboratorio debe poder someter sus propias conclusiones, reglas y protocolos al mismo procedimiento de evaluacion que aplica a cualquier hipotesis externa.

Toda afirmacion del Laboratorio debe poder ser auditada, incluida la afirmacion sobre que cuenta como auditoria.

Esta regla detecta:

- lenguaje inflado;
- afirmaciones no demostradas;
- conceptos introducidos sin necesidad;
- cierre dogmatico del Canon;
- expansion no justificada del alcance.

### M-001 historico - Presuncion de reducibilidad

Todo candidato a concepto fundamental se presume reducible hasta que demuestre formalmente su irreductibilidad.

La carga de la prueba recae sobre el candidato, no sobre el Laboratorio.

Un concepto solo puede adquirir estatus canonico si demuestra:

- irreductibilidad;
- necesidad;
- rendimiento formal;
- compatibilidad con el Canon vigente;
- apertura a auditoria futura.

### C-001 historico - Reduccion conceptual

Todo concepto candidato debe descomponerse en componentes mas simples antes de aceptarse.

Un concepto solo permanece si eliminarlo produce perdida explicativa demostrable.

La reduccion no busca simplificar por estetica. Busca distinguir lo necesario de lo decorativo.

### C-002 historico - Criterio de parada adaptativo

La reduccion conceptual debe detenerse cuando continuar reduciendo destruye la capacidad del sistema para auditar, distinguir o reconstruir la justificacion del modelo.

Tambien debe detenerse cuando seguir reduciendo deja de aumentar el poder explicativo o empieza a deteriorar el rendimiento del modelo.

### EF-001 historico - Economia formal

Todo concepto o modulo nuevo debe justificar su costo estructural.

Un incremento de complejidad solo se acepta si produce ganancia demostrable en auditabilidad, trazabilidad, terminacion, discriminacion, reproducibilidad o rendimiento explicativo.

Nota de gobierno: `EF-001` local esta cerrado/no reabrir sin decision explicita. La incorporacion documental de esta regla historica no reabre ese frente.

### Doble auditoria

Todo candidato debe poder someterse a dos auditorias distinguibles:

- auditoria interna: minimalidad estructural, coherencia y economia formal;
- auditoria externa: conservacion de poder explicativo, rendimiento o adecuacion al dominio declarado.

En el repositorio vigente, la auditoria externa no equivale automaticamente a validacion empirica. Debe declararse el tipo de evidencia externa disponible.

### Clausula de incompletitud

Ningun componente del Laboratorio queda exento de revision.

El Laboratorio dispone de un marco formal provisional para estudiar la evolucion interna de modelos, pero su completitud permanece como hipotesis abierta.

Una regla que impide revisar otra regla deja de ser metodologica y se convierte en dogma.

## Decalogo incorporado

El Decalogo historico de `SRC-023` queda incorporado como orientacion oficial del Documento 01:

1. El Laboratorio estudia explicaciones, no ideas.
2. Ninguna hipotesis entra al Canon sin superar el protocolo de admision.
3. Todo concepto debe justificar su existencia.
4. Toda reduccion termina cuando deja de aumentar el poder explicativo.
5. Ningun concepto es definitivo.
6. Las anomalias tienen prioridad sobre las intuiciones.
7. El conocimiento aceptado y las hipotesis abiertas nunca se mezclan.
8. Toda modificacion debe ser trazable.
9. El costo de una explicacion tambien es evidencia.
10. El Laboratorio protege el proceso antes que los resultados.

Regla VII tiene fuerza documental especial: las hipotesis viven en expedientes; el conocimiento aceptado vive en Canon, documentos oficiales o decisiones vigentes segun corresponda.

## Compatibilidad y cambio

Las fuentes historicas distinguian:

- patch: correcciones, aclaraciones o demostraciones sin alterar Canon;
- minor: protocolos o modulos nuevos compatibles con Canon;
- major: cambios en axiomas, definiciones fundamentales o comportamiento del auditor.

En el repositorio vigente, toda modificacion del Canon requiere:

- motivo explicito;
- impacto sobre documentos y expedientes;
- auditoria;
- decision registrada;
- actualizacion de estado;
- actualizacion de `CHANGELOG.md` cuando corresponda.

## Frontera nominal

Hay nombres historicos que coinciden con nombres vigentes pero no significan exactamente lo mismo:

- `M-000` historico no sustituye a `01_Canon/M-000_Reglas_Fundamentales.md`;
- `M-001` historico no sustituye a `01_Canon/M-001_Auditoria_Arquitectonica.md`;
- `C-001` historico no sustituye a `02_Documentos/C-001_Especificacion_Tecnica_Auditor.md`;
- `C-002` historico no sustituye a `02_Documentos/C-002_RFC_Operativo_Auditor_v0.md`.

Cuando un expediente use estos nombres, debe declarar si habla del elemento historico o del elemento vigente.

## Estado

Documento 01 queda consolidado como descripcion oficial del Canon local y del canon metodologico historico incorporado.

Cualquier promocion de reglas historicas a archivos canonicos nuevos requiere expediente y decision separada.
