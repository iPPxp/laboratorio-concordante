# DO-001 - Regla de permiso de actualizacion

Estatus: regla provisional de expediente.

Expediente padre: `DO-001`.

Fecha: 2026-07-01.

Identificador: `PERMISO-ACT-001`.

Objeto: paso de recomendacion o propuesta a cambio real dentro del repositorio.

## Regla central

Ninguna recomendacion, reporte, validacion o propuesta se convierte en cambio ejecutado por si misma.

Un cambio real requiere siempre una `AUTORIZACION_DE_EJECUCION` previa, trazable y acotada.

La automatizacion puede ejecutar un cambio solo cuando actua sobre una autorizacion valida. No puede producir por si misma la autoridad que la habilita.

## Separacion de funciones

| Funcion | Puede recomendar | Puede autorizar | Puede ejecutar |
| --- | --- | --- | --- |
| `DO_CHECK_REPORT` | si | no | no |
| `OPERATOR_REPORT` | si | no | no |
| `D_REPORT` | no | si, dentro de reportes permitidos | no |
| Decision registrada | no aplica | si | no |
| Instruccion humana explicita | no aplica | si, solo en alcance permitido | no ejecuta por si misma |
| Automatizacion o agente | si, como borrador | no | si, solo con autorizacion previa |

## AUTORIZACION_DE_EJECUCION

Una autorizacion de ejecucion es valida si declara:

- fuente de autorizacion
- archivo o conjunto de archivos objetivo
- alcance exacto del cambio
- razon del cambio
- fuente que lo justifica
- expedientes o problemas abiertos afectados
- tipo de superficie afectada
- verificacion posterior requerida
- si `transformacion_permitida = true` para ese cambio acotado

## Fuentes de autorizacion permitidas

En v0, solo pueden autorizar ejecucion:

- una decision registrada en el repositorio
- un `D_REPORT` valido con `decision_emitida = continuar_con_cambio_acotado` y `transformacion_permitida = true`
- una instruccion humana explicita dentro de la intervencion activa, solo para cambios permitidos por esta regla

Una recomendacion de `DO_CHECK_REPORT` nunca basta como autorizacion.

## Superficies y permisos

### Estado operativo

Archivos incluidos:

- `CURRENT_STATE.md`
- `05_Estado_Proyecto/ESTADO_ACTUAL.md`
- `CHANGELOG.md`

Permiso v0: una instruccion humana explicita puede autorizar actualizaciones acotadas si el cambio solo registra hechos ya materializados en archivos locales y no modifica Canon, documentos oficiales ni expedientes cerrados.

### Expedientes abiertos

Permiso v0: una instruccion humana explicita puede autorizar cambios acotados en expedientes abiertos cuando el cambio mantiene estatus provisional, registra fuentes y no cierra ni reabre expedientes.

Cerrar, reabrir o reclasificar un expediente requiere decision registrada.

### Documentos oficiales

Permiso v0: requieren decision registrada. Una instruccion humana simple no basta si el cambio altera contenido sustantivo de `02_Documentos`.

### Canon

Permiso v0: requiere decision explicita de nivel canonico o arquitectonico y trazabilidad completa. Ningun reporte, recomendacion o instruccion operativa simple modifica Canon.

### Expedientes cerrados

Permiso v0: no pueden modificarse ni reabrirse por conveniencia. Requieren decision explicita, contradiccion demostrable o evidencia nueva registrada, conforme a `M-000.7`.

### Registro Historico

Permiso v0: no puede usarse como autoridad vigente. Puede motivar busqueda o reconstruccion, pero no autoriza cambios por si mismo.

## Cambio ejecutado valido

Un cambio ejecutado es valido si:

- tiene autorizacion previa valida
- respeta el alcance exacto autorizado
- no usa deuda conceptual como fundamento positivo
- conserva separacion de niveles
- registra evidencia antes y despues cuando el cambio no es trivial
- actualiza estado o changelog si cambia el objetivo operativo o registra una pieza nueva
- pasa una verificacion posterior compatible con `M-000`, `M-001` y `DO-CHECK-001`

## Cambio ejecutado invalido

Un cambio ejecutado es invalido si:

- nace solo de una recomendacion
- no identifica autorizacion previa
- excede el alcance autorizado
- modifica Canon sin decision explicita
- modifica documentos oficiales sin decision registrada
- cierra o reabre expedientes sin decision registrada
- convierte hipotesis, deuda o historial en autoridad vigente
- omite verificacion posterior

## Regla para agentes y automatizaciones

Un agente puede preparar borradores, reportes y propuestas.

Un agente solo puede ejecutar cambios cuando la instruccion humana o decision registrada identifica el alcance permitido. La ejecucion debe quedar trazada en los archivos de estado o en el changelog cuando afecte el estado del proyecto.

Forma:

```text
recomendacion
-> autorizacion valida
-> ejecucion acotada
-> verificacion posterior
-> registro de estado si corresponde
```

## Relacion con DO-CHECK-001

`DO-CHECK-001` puede detectar permiso insuficiente y recomendar bloquear, escalar o continuar sin transformar.

`DO-CHECK-001` no puede emitir `AUTORIZACION_DE_EJECUCION` y conserva `transformacion_permitida = false`.

## Relacion con D_REPORT

`D_REPORT` puede autorizar una transformacion futura solo si cumple el contrato de `AUD-001`:

- `decision_emitida = continuar_con_cambio_acotado`
- `transformacion_permitida = true`
- reportes previos permiten esa decision
- el cambio autorizado esta identificado de forma acotada
- la salida esperada puede auditarse antes y despues

`D_REPORT` autoriza condiciones. No ejecuta `Tr`.

## Resultado operativo

La respuesta a quien tiene permiso es:

- la recomendacion no tiene permiso
- el reporte no tiene permiso
- la automatizacion no tiene permiso propio
- la autorizacion nace de una decision registrada, un `D_REPORT` valido o una instruccion humana explicita dentro del alcance permitido
- la ejecucion solo puede aplicar exactamente lo autorizado

## Validacion inicial

`PERMISO-ACT-001` fue validado provisionalmente en `03_Expedientes/DO-001_Validaciones_PERMISO-ACT-001.md`.

Casos cubiertos:

- actualizacion de estado operativo autorizada por instruccion humana explicita
- recomendacion sin autorizacion
- cambio de nivel superior o expediente cerrado con permiso insuficiente

## Limite

Esta regla no estabiliza por si misma la reversion ejecutada real ni la cuarentena materializada. Esos casos dependen de `REVERSAL_REPORT` y de decisiones posteriores.

## Criterio de cierre

Esta regla queda registrada si:

- existe este archivo asociado a `DO-001`
- `DO-001` referencia la regla
- el estado del proyecto registra la regla como activa provisionalmente
- existe validacion inicial contra casos locales

Estado actual: cumplido.
