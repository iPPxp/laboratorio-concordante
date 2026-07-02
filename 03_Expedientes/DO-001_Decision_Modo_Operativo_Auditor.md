# DO-001 - Decision de modo operativo del Auditor

Estatus: decision provisional de expediente.

Expediente padre: `DO-001`.

Fecha: 2026-07-01.

Identificador: `MODO-AUD-001`.

Objeto: decidir si el Auditor opera como algoritmo ejecutable, protocolo asistido o combinacion de ambos.

## Decision

El Auditor opera en modo mixto.

La parte ejecutable queda permitida solo como capa verificable, trazable y restringida. La parte asistida queda obligatoria para toda decision que produzca autoridad, cambie estatus, elija entre alternativas no decididas o habilite modificaciones reales.

Forma:

```text
lectura/verificacion/reporte -> algoritmo ejecutable
recomendacion/decision/permiso -> protocolo asistido o decision registrada
ejecucion real -> algoritmo acotado solo con autorizacion valida
```

## Capas operativas

| Capa | Modo | Puede modificar archivos | Puede crear autoridad |
| --- | --- | --- | --- |
| Lectura local | algoritmo ejecutable | no | no |
| Verificacion de trazabilidad | algoritmo ejecutable | no | no |
| Emision de reportes | algoritmo ejecutable | no | no |
| Recomendacion | algoritmo ejecutable o asistido | no | no |
| Decision de permiso | protocolo asistido o decision registrada | no | si, dentro del alcance declarado |
| Ejecucion acotada | algoritmo ejecutable subordinado | si, solo con autorizacion valida | no |
| Promocion de estatus | protocolo asistido y decision registrada | si, si corresponde | si |

## Regla central

La automatizacion puede ser ejecutable en el calculo, pero no autonoma en la autoridad.

Un algoritmo puede detectar, comparar, normalizar, reportar y aplicar un cambio ya autorizado. No puede decidir por si mismo que una recomendacion se vuelve cambio real, que una hipotesis se vuelve Canon, que un expediente se cierra o que una deuda queda resuelta.

## Relacion con DO-CHECK-001

`DO-CHECK-001` pertenece a la capa ejecutable no mutante.

Puede leer archivos locales y emitir `DO_CHECK_REPORT`.

No puede modificar archivos, cerrar expedientes, promover estatus ni emitir `AUTORIZACION_DE_EJECUCION`.

## Relacion con PERMISO-ACT-001

`PERMISO-ACT-001` gobierna el paso de recomendacion a cambio real.

`MODO-AUD-001` no reemplaza esa regla. La ubica dentro del modo mixto:

- el algoritmo puede producir la recomendacion
- la autorizacion debe venir de fuente valida
- la ejecucion solo aplica el alcance autorizado
- la verificacion posterior registra si el cambio quedo dentro del permiso

## Relacion con AUD-001

Los contratos de `AUD-001` son compatibles con este modo mixto.

`Mp`, `Cr`, `tau`, `D` y `Tr` pueden describirse como operadores formales, pero su ejecucion local debe respetar la frontera entre reporte, decision y transformacion.

En particular:

- `OPERATOR_REPORT` y reportes derivados pueden ser producidos por algoritmo.
- `D_REPORT` puede expresar decision dentro del modelo, pero no convierte al agente ejecutor en autoridad general.
- `TR_EXECUTION_REPORT` solo es valido si existia autorizacion previa.
- `REVERSAL_REPORT` decide acciones permitidas despues de fallo, pero no borra la necesidad de evidencia y permiso.

## Acciones permitidas por modo

### Ejecutable no mutante

Permitido:

- leer fuentes locales autorizadas
- verificar estatus, dependencias y referencias
- detectar deudas conceptuales
- emitir reportes normalizados
- proponer cambios como borrador
- comparar decision emitida contra decision permitida

Prohibido:

- escribir cambios
- cerrar expedientes
- modificar Canon
- modificar documentos oficiales
- aprobar transformaciones
- resolver deudas por redaccion

### Ejecutable acotado subordinado

Permitido solo con `AUTORIZACION_DE_EJECUCION` valida:

- aplicar el cambio exacto autorizado
- registrar evidencia antes y despues
- ejecutar verificacion posterior
- actualizar estado operativo si el permiso lo cubre

Prohibido:

- ampliar el alcance autorizado
- elegir una alternativa no decidida
- usar el cambio para cerrar deuda conceptual
- reintentar despues de fallo sin nueva autorizacion

### Protocolo asistido

Obligatorio para:

- decisiones que cambian estatus
- promocion hacia documentos oficiales o Canon
- cierre, reapertura o reclasificacion de expedientes
- autorizacion de cambios reales
- decisiones sobre deudas conceptuales abiertas
- reversion o cuarentena cuando el estado posterior es ambiguo

## Resultado

`DO-001` no define un Auditor completamente autonomo.

Define un Auditor hibrido: ejecutable para revisar y reportar; asistido para autorizar, promover, cerrar o transformar con efecto real.

## Limite

Esta decision no crea todavia una Especificacion Tecnica oficial del Auditor.

Tampoco implementa una herramienta ejecutable completa. Solo fija el modo operativo que debera respetar cualquier especificacion o implementacion futura.

## Criterio de cierre

Esta decision queda registrada si:

- existe este archivo asociado a `DO-001`
- `DO-001` referencia `MODO-AUD-001`
- existe validacion local del modo mixto
- el estado del proyecto retira la deuda "decidir modo operativo"
- el siguiente objetivo pasa a definir `Nivel C - Especificaciones` antes de promocion oficial

Estado actual: cumplido por `ALC-SPEC-AUD-001`.
