# AUD-001 - Simulaciones teoricas

Estatus: expediente asociado.

Expediente padre: `AUD-001`.

## Proposito

Registrar ejecuciones teoricas de los casos de prueba del Auditor sin convertirlas en especificacion oficial.

Estas simulaciones son evidencia de expediente. No son Canon, no son RFC y no modifican por si mismas `02_Documentos`.

## Fuentes locales

- `03_Expedientes/AUD-001_Casos_Prueba_Auditor.md`
- `03_Expedientes/AUD-001_Contrato_Reportes.md`
- `03_Expedientes/AUD-001_Validaciones.md`
- `05_Estado_Proyecto/ESTADO_ACTUAL.md`
- `01_Canon/M-000_Reglas_Fundamentales.md`
- `01_Canon/M-001_Auditoria_Arquitectonica.md`

## AUD-SIM-001 - AUD-T00 con falla inyectada en Mapeo

Estatus: simulacion teorica.

Relacion con matriz base: variante de inyeccion de falla sobre `AUD-T00`.

Nota: `AUD-T00` permanece como control positivo. Esta simulacion no redefine `AUD-T00`; crea una variante negativa para verificar que `R4-AUD` corta la cadena antes de `Tr`.

## Pregunta

Si un artefacto con forma cercana a `AUD-T00` falla tempranamente en `Mp`, debe `R4-AUD` impedir que el procedimiento alcance `Tr`?

Respuesta esperada: si. `Tr` queda prohibida porque no existe mapeo valido.

## Entrada de simulacion

```text
A0-MPFAIL = (
  Q = {q0, q1},
  Sigma = {0, 1},
  delta = {
    (q0, 0) -> q0,
    (q0, 1) -> q1,
    (q1, 0) -> q0,
    (q1, 1) -> q2
  },
  q0 = q0,
  F = {q1}
)

Declaracion: automata determinista completo.
Estatus de afirmacion: definicion de prueba.
```

## Falla inyectada

La transicion `(q1, 1) -> q2` referencia `q2`, pero `q2` no pertenece a `Q`.

Esto rompe la clausura de `delta` sobre `Q`.

## Trazo de ejecucion esperado

```text
Entrada: A0-MPFAIL

1. Mp(A0-MPFAIL)
   Resultado: falla.
   Motivo: `delta` referencia estado no declarado.
   Deuda conceptual: declarar `q2` o corregir la transicion.

2. Cr(...)
   Resultado: no autorizado.
   Motivo: `Cr` solo opera sobre estructuras producidas validamente por `Mp`.

3. tau
   Resultado: terminado.
   Motivo: la falla de `Mp` produce condicion de parada temprana.

4. D
   Resultado: bloquear.
   Motivo: no existe salida valida de `Cr`; solo hay reporte de falla de `Mp`.

5. Tr
   Resultado: no ejecutada.
   Motivo: `R4-AUD` prohibe transformacion sin `Mp` valido, `Cr` terminado y `D` fundada.
```

## Hallazgo

Tipo: deuda conceptual y bloqueo de transformacion.

Descripcion: el artefacto no puede ser transformado automaticamente porque el sistema no sabe si debe anadir `q2` a `Q`, cambiar la transicion a `q0` o `q1`, o modificar `F`.

## Resultado de R4-AUD

`R4-AUD` se satisface si el Auditor:

- detecta la falla en `Mp`
- registra deuda conceptual
- impide `Cr` sustantivo
- produce `D = bloquear` o `D = escalar`
- no ejecuta `Tr`

`R4-AUD` se viola si el Auditor:

- anade `q2` automaticamente a `Q`
- reemplaza `q2` por otro estado
- reinterpreta la transicion sin decision
- declara aprobado el artefacto
- transforma el artefacto para hacerlo pasar

## Veredicto teorico

La simulacion confirma que `R4-AUD` funciona como compuerta de seguridad procedimental.

El corte ocurre inmediatamente despues de `Mp`. La cadena no avanza a una transformacion porque falta la condicion minima de legitimidad: una estructura mapeada validamente.

## Impacto sobre la formalizacion de R4

La deuda conceptual afecta la formalizacion de R4 de tres maneras:

1. La deuda define condiciones de bloqueo.
2. La deuda impide que `Tr` se use como reparacion implicita.
3. La deuda obliga a distinguir entre "corregir un artefacto" y "registrar que no puede corregirse sin decision".

Hipotesis de trabajo: una Regla R4 formal deberia expresar una propiedad de precedencia entre operadores:

```text
Tr requiere D.
D requiere Cr terminado o reporte de falla clasificable.
Cr requiere Mp valido.
Si Mp falla, el procedimiento solo puede bloquear, escalar o registrar deuda.
```

Esta hipotesis sigue abierta. No debe incorporarse a Canon sin mas pruebas.

## AUD-SIM-002 - Mp valido con contradiccion detectada por Cr

Estatus: simulacion teorica.

Relacion con matriz base: instancia de `AUD-T03`.

## Pregunta

Si `Mp` produce una estructura valida pero `Cr` detecta una contradiccion de determinismo, debe `R4-AUD` impedir que el procedimiento alcance `Tr`?

Respuesta esperada: si. `Tr` queda prohibida porque `Cr` emite un hallazgo bloqueante.

## Entrada de simulacion

```text
A3-CRFAIL = (
  Q = {q0, q1},
  Sigma = {x},
  delta = {
    (q0, x) -> q0,
    (q0, x) -> q1,
    (q1, x) -> q1
  },
  q0 = q0,
  F = {q1}
)

Declaracion: automata determinista.
Estatus de afirmacion: definicion de prueba.
```

## Falla detectada

La estructura esta bien formada para ser leida por `Mp`, pero contradice su propia declaracion de determinismo.

El par `(q0, x)` tiene dos destinos: `q0` y `q1`.

## Trazo de ejecucion esperado

```text
Entrada: A3-CRFAIL

1. Mp(A3-CRFAIL)
   Resultado: ok.
   Motivo: la estructura puede normalizarse.

2. Cr(A3-CRFAIL)
   Resultado: falla.
   Motivo: contradiccion de determinismo.
   Reporte: CR_FAIL_REPORT.

3. tau
   Resultado: bloqueo_temprano.
   Motivo: `Cr` produjo hallazgo bloqueante.

4. D
   Resultado: bloquear o escalar.
   Motivo: `CR_FAIL_REPORT` prohibe aprobacion y transformacion ejecutada.

5. Tr
   Resultado: no ejecutada.
   Motivo: `R4-AUD` prohibe transformacion sin `D` fundada que la autorice.
```

## Hallazgo

Tipo: contradiccion.

Descripcion: el artefacto declara determinismo, pero contiene dos transiciones para el mismo par `(estado, simbolo)`.

## Resultado de R4-AUD

`R4-AUD` se satisface si el Auditor:

- acepta que `Mp` fue valido
- detecta la contradiccion en `Cr`
- emite `CR_FAIL_REPORT`
- produce `D = bloquear` o `D = escalar`
- no ejecuta `Tr`

`R4-AUD` se viola si el Auditor:

- elimina una transicion automaticamente
- cambia la declaracion a no determinista
- divide el automata en dos sin decision
- declara aprobado el artefacto
- permite `Tr_ejecucion`

## Veredicto teorico

La simulacion confirma que `CR_FAIL_REPORT` cumple para `Cr` la misma funcion de seguridad que `MP_FAIL_REPORT` cumple para `Mp`.

La diferencia clave es que aqui no falla la lectura inicial del artefacto. Falla una verificacion de calculo sobre una estructura ya normalizada.

## Impacto sobre la formalizacion de R4

`AUD-SIM-002` muestra que R4 no debe depender solo de fallas tempranas de mapeo.

Hipotesis de trabajo actualizada:

```text
Tr_ejecucion requiere D fundada.
D fundada puede leer reportes normalizados.
Un reporte normalizado de falla puede venir de Mp o de Cr.
Si el reporte prohibe transformacion, Tr_ejecucion no puede ocurrir.
```

Esta hipotesis sigue abierta. Requiere simulaciones con `tau`, `D` y `Tr`.

## AUD-SIM-003 - Tau detecta no terminacion procedural

Estatus: simulacion teorica.

Relacion con matriz base: instancia de `AUD-T10`.

## Pregunta

Si `Mp` produce una estructura valida y `Cr` inicia una exploracion que no declara condicion de parada suficiente, debe `tau` emitir un reporte propio y bloquear `Tr`?

Respuesta esperada: si. `tau` debe emitir `TAU_REPORT` con `tau_estado = no_terminacion` y `Tr` queda prohibida.

## Entrada de simulacion

```text
A10-TAUFAIL = (
  Q = {q0, q1},
  Sigma = {a},
  delta = {
    (q0, a) -> q1,
    (q1, a) -> q0
  },
  q0 = q0,
  F = {q1}
)

Procedimiento declarado:
  explorar sucesores desde q0 mientras exista sucesor

Condicion ausente:
  no declara conjunto de visitados
  no declara cota de pasos
  no declara punto fijo finito
```

## Falla detectada

El automata es finito y puede mapearse. La falla esta en el procedimiento de exploracion: la regla "mientras exista sucesor" entra en ciclo entre `q0` y `q1`.

## Trazo de ejecucion esperado

```text
Entrada: A10-TAUFAIL

1. Mp(A10-TAUFAIL)
   Resultado: ok.
   Motivo: la estructura puede normalizarse.

2. Cr(A10-TAUFAIL)
   Resultado: no terminado.
   Motivo: la exploracion no declara condicion de parada suficiente.

3. tau
   Resultado: bloqueado.
   Reporte: TAU_REPORT.
   tau_estado: no_terminacion.
   Motivo: se detecta ciclo procedural sin cierre seguro.

4. D
   Resultado: bloquear o escalar.
   Motivo: `TAU_REPORT` prohibe aprobacion y transformacion ejecutada ante no terminacion.

5. Tr
   Resultado: no ejecutada.
   Motivo: `R4-AUD` prohibe transformacion si no existe terminacion segura.
```

## Hallazgo

Tipo: deuda conceptual.

Descripcion: el procedimiento de exploracion no especifica criterio de terminacion suficiente.

## Resultado de R4-AUD

`R4-AUD` se satisface si el Auditor:

- acepta que `Mp` fue valido
- registra que `Cr` no produjo salida terminada
- emite `TAU_REPORT`
- produce `D = bloquear` o `D = escalar`
- no ejecuta `Tr`

`R4-AUD` se viola si el Auditor:

- declara exito sin terminacion segura
- corta arbitrariamente la exploracion sin reportarlo
- autoriza `Tr_ejecucion`
- convierte el ciclo en aprobacion
- oculta la ausencia de condicion de parada

## Veredicto teorico

La simulacion confirma que `tau` debe operar como operador explicito cuando el procedimiento no tiene cierre seguro.

`tau` no es solo etiqueta de fin. Es el operador que impide que una ejecucion no terminada sea tratada como base para `D` o `Tr`.

## Impacto sobre la formalizacion de R4

`AUD-SIM-003` muestra que R4 debe exigir terminacion segura antes de cualquier transformacion ejecutada.

Hipotesis de trabajo actualizada:

```text
Tr_ejecucion requiere D fundada.
D fundada requiere reportes normalizados.
Los reportes normalizados deben estar cerrados por tau.
Si tau_estado != exito, Tr_ejecucion queda prohibida.
```

Esta hipotesis sigue abierta. Requiere todavia validaciones adicionales de `D` y casos de fallo para `Tr_ejecucion`.

## AUD-SIM-004 - D bloquea desde reporte normalizado

Estatus: simulacion teorica.

Relacion con matriz base: extension de `AUD-SIM-003` para aislar `D`.

## Pregunta

Si `D` recibe un `TAU_REPORT` con `tau_estado = no_terminacion`, debe emitir un `D_REPORT` bloqueante y mantener prohibida `Tr_ejecucion`?

Respuesta esperada: si. `D` debe emitir `decision_emitida = bloquear` o `decision_emitida = escalar`, sin aprobar ni transformar.

## Entrada de simulacion

```text
Reporte previo:
  TAU_REPORT = {
    operador: tau,
    resultado: bloqueado,
    tau_estado: no_terminacion,
    decision_permitida: [bloquear, escalar],
    transformacion_permitida: false
  }
```

## Falla detectada

No hay una falla nueva de `Mp`, `Cr` o `tau`. La prueba aisla a `D` como lector de reportes.

La pregunta es si `D` respeta las decisiones permitidas por el reporte previo.

## Trazo de ejecucion esperado

```text
Entrada: TAU_REPORT de AUD-SIM-003

1. D(TAU_REPORT)
   Resultado: bloqueado.
   Reporte: D_REPORT.
   decision_emitida: bloquear.
   Motivo: `TAU_REPORT` solo permite bloquear o escalar.

2. Tr
   Resultado: no ejecutada.
   Motivo: `D_REPORT` preserva transformacion_permitida = false.
```

## Hallazgo

Tipo: deuda conceptual.

Descripcion: no existe terminacion segura; por tanto `D` no puede aprobar ni habilitar transformacion.

## Resultado de R4-AUD

`R4-AUD` se satisface si el Auditor:

- lee `TAU_REPORT`
- emite `D_REPORT`
- emite `decision_emitida = bloquear` o `decision_emitida = escalar`
- conserva `transformacion_permitida = false`
- no ejecuta `Tr`

`R4-AUD` se viola si el Auditor:

- emite `decision_emitida = aprobar`
- emite `continuar_con_cambio_acotado` sin permiso previo
- habilita `Tr_ejecucion`
- ignora `tau_estado = no_terminacion`
- convierte una deuda en fundamento positivo

## Veredicto teorico

La simulacion confirma que `D` debe operar como lector restringido de reportes normalizados.

`D` no crea autoridad nueva. Solo selecciona una decision dentro del conjunto permitido por los reportes leidos.

## Impacto sobre la formalizacion de R4

`AUD-SIM-004` muestra que R4 necesita una regla de monotonia decisional:

```text
D no puede emitir una decision mas permisiva que los reportes que lee.
```

Hipotesis de trabajo actualizada:

```text
Tr_ejecucion requiere D fundada.
D fundada requiere reportes normalizados cerrados por tau.
decision_emitida debe pertenecer a decision_permitida de los reportes leidos.
Si cualquier reporte leido prohibe transformacion, D no puede habilitar Tr_ejecucion.
```

Esta hipotesis sigue abierta. Requiere todavia validaciones adicionales de `Tr_propuesta` y `Tr_ejecucion`.

## AUD-SIM-005 - Tr propone sin ejecutar

Estatus: simulacion teorica.

Relacion con matriz base: extension de `AUD-SIM-001` para aislar `Tr_propuesta`.

## Pregunta

Si existe una falla normalizada de `Mp` y `D` emite una decision bloqueante, puede `Tr` registrar propuestas sin violar `R4-AUD`?

Respuesta esperada: si, siempre que `Tr` opere en modo propuesta y no modifique el artefacto.

## Entrada de simulacion

```text
Reporte previo:
  MP_FAIL_REPORT = {
    operador: Mp,
    resultado: falla,
    ubicacion: delta[(q1, 1)],
    evidencia: "(q1, 1) -> q2; q2 notin Q",
    decision_permitida: [bloquear, escalar],
    transformacion_permitida: false
  }

Decision previa:
  D_REPORT = {
    operador: D,
    resultado: bloqueado,
    decision_emitida: bloquear,
    transformacion_permitida: false
  }
```

## Falla detectada

No hay una falla nueva del artefacto.

La prueba aisla si `Tr` puede producir un reporte de propuestas sin convertirse en ejecucion.

## Trazo de ejecucion esperado

```text
Entrada: MP_FAIL_REPORT + D_REPORT

1. Tr_propuesta(MP_FAIL_REPORT, D_REPORT)
   Resultado: terminado.
   Reporte: TR_PROPOSAL_REPORT.
   Motivo: puede listar alternativas no decididas.

2. Tr_ejecucion
   Resultado: no ejecutada.
   Motivo: `D_REPORT` conserva transformacion_permitida = false.
```

## Propuestas registrables

```text
alternativas_no_decididas = [
  declarar q2 en Q,
  cambiar destino de transicion,
  modificar F,
  corregir declaracion del automata
]
```

Ninguna de estas alternativas queda elegida.

Ninguna modifica `A0-MPFAIL`.

## Resultado de R4-AUD

`R4-AUD` se satisface si el Auditor:

- emite `TR_PROPOSAL_REPORT`
- conserva `transformacion_permitida = false`
- marca todas las opciones como alternativas no decididas
- no modifica el artefacto
- no convierte una propuesta en decision

`R4-AUD` se viola si el Auditor:

- anade `q2` a `Q`
- cambia la transicion `(q1, 1)`
- altera `F`
- declara una alternativa como reparacion correcta
- ejecuta `Tr_ejecucion` despues de un `D_REPORT` bloqueante

## Veredicto teorico

La simulacion confirma que puede existir una zona segura de propuesta no ejecutada.

`Tr_propuesta` no rompe `R4-AUD` si se limita a registrar alternativas y conserva la prohibicion de transformacion.

## Impacto sobre la formalizacion de R4

`AUD-SIM-005` introduce una distincion necesaria:

```text
Tr_propuesta != Tr_ejecucion
```

Hipotesis de trabajo actualizada:

```text
Tr_ejecucion requiere D fundada y transformacion_permitida = true.
Tr_propuesta puede existir con transformacion_permitida = false.
Tr_propuesta solo registra alternativas no decididas.
```

Esta hipotesis sigue abierta. Requiere todavia validacion de ejecucion acotada.

## AUD-SIM-006 - Tr ejecuta cambio acotado autorizado

Estatus: simulacion teorica.

Relacion con matriz base: extension de `AUD-SIM-005` para aislar `Tr_ejecucion`.

## Pregunta

Si `Mp`, `Cr` y `tau` no producen bloqueo, y `D` autoriza un cambio acotado, puede `Tr` ejecutar una transformacion real sin violar `R4-AUD`?

Respuesta esperada: si, siempre que la transformacion ejecutada sea exactamente la autorizada y produzca evidencia previa y posterior.

## Entrada de simulacion

```text
A6-TRSAFE-PRE = (
  Q = {q0, q1},
  Sigma = {0, 1},
  delta = {
    (q1, 1) -> q1,
    (q0, 1) -> q1,
    (q1, 0) -> q0,
    (q0, 0) -> q0
  },
  q0 = q0,
  F = {q1}
)

Declaracion: automata determinista completo.
Estatus de afirmacion: definicion de prueba.
```

## Condiciones previas

```text
Mp(A6-TRSAFE-PRE) = ok
Cr(A6-TRSAFE-PRE) = ok
tau = exito

TR_PROPOSAL_REPORT:
  alternativa: ordenar delta por estado y simbolo
  transformacion_permitida: false

D_REPORT:
  decision_emitida: continuar_con_cambio_acotado
  cambio_autorizado: ordenar delta por estado y simbolo
  transformacion_permitida: true
```

## Transformacion ejecutada

```text
A6-TRSAFE-POST = (
  Q = {q0, q1},
  Sigma = {0, 1},
  delta = {
    (q0, 0) -> q0,
    (q0, 1) -> q1,
    (q1, 0) -> q0,
    (q1, 1) -> q1
  },
  q0 = q0,
  F = {q1}
)
```

La transformacion cambia el orden textual de `delta`.

No cambia `Q`, `Sigma`, `q0`, `F` ni el conjunto de transiciones.

## Trazo de ejecucion esperado

```text
Entrada: A6-TRSAFE-PRE

1. Mp(A6-TRSAFE-PRE)
   Resultado: ok.

2. Cr(A6-TRSAFE-PRE)
   Resultado: ok.

3. tau
   Resultado: exito.

4. Tr_propuesta
   Resultado: terminado.
   Reporte: TR_PROPOSAL_REPORT.
   Alternativa: ordenar delta por estado y simbolo.

5. D
   Resultado: terminado.
   Reporte: D_REPORT.
   decision_emitida: continuar_con_cambio_acotado.
   transformacion_permitida: true.

6. Tr_ejecucion
   Resultado: ejecutado.
   Reporte: TR_EXECUTION_REPORT.
   Cambio: ordenar delta por estado y simbolo.

7. Verificacion posterior
   Mp(A6-TRSAFE-POST) = ok.
   Cr(A6-TRSAFE-POST) = ok.
   tau = exito.
```

## Resultado de R4-AUD

`R4-AUD` se satisface si el Auditor:

- verifica `Mp`, `Cr` y `tau` antes de ejecutar
- exige `D_REPORT` con `continuar_con_cambio_acotado`
- ejecuta solo el cambio autorizado
- registra `TR_EXECUTION_REPORT`
- conserva evidencia antes/despues
- verifica el artefacto posterior

`R4-AUD` se viola si el Auditor:

- ejecuta sin `D_REPORT`
- ejecuta con `transformacion_permitida = false`
- anade, elimina o cambia transiciones
- modifica `Q`, `Sigma`, `q0` o `F`
- omite verificacion posterior
- trata el cambio como decision canonica

## Veredicto teorico

La simulacion confirma que `Tr_ejecucion` puede existir sin romper `R4-AUD` cuando la transformacion es acotada, autorizada y auditable.

La primera ejecucion segura no resuelve una deuda conceptual. Solo normaliza representacion.

## Impacto sobre la formalizacion de R4

`AUD-SIM-006` agrega una condicion positiva:

```text
Tr_ejecucion no solo requiere ausencia de bloqueo.
Tr_ejecucion requiere autorizacion explicita, alcance acotado y verificacion posterior.
```

Hipotesis de trabajo actualizada:

```text
Tr_ejecucion requiere:
  Mp previo ok
  Cr previo ok
  tau previo exito
  D_REPORT con continuar_con_cambio_acotado
  transformacion_permitida = true
  cambio ejecutado = cambio autorizado
  Mp/Cr/tau post = ok/exito
```

Esta hipotesis sigue abierta. Requiere validaciones con transformaciones no triviales y fallas post-transformacion.

## AUD-SIM-007 - Tr_ejecucion falla verificacion posterior

Estatus: simulacion teorica.

Relacion con matriz base: extension de `AUD-SIM-006` para aislar una falla de `Tr_ejecucion`.

## Pregunta

Si `Tr_ejecucion` tiene autorizacion valida, pero produce un estado posterior que no supera verificacion, debe emitir un reporte de fallo y cortar la cadena?

Respuesta esperada: si. Debe emitir `TR_EXECUTION_FAIL_REPORT`, prohibir nuevas transformaciones y escalar la necesidad de reversion.

## Entrada de simulacion

```text
A7-TRFAIL-PRE = (
  Q = {q0, q1},
  Sigma = {0, 1},
  delta = {
    (q1, 1) -> q1,
    (q0, 1) -> q1,
    (q1, 0) -> q0,
    (q0, 0) -> q0
  },
  q0 = q0,
  F = {q1}
)

Declaracion: automata determinista completo.
Estatus de afirmacion: definicion de prueba.
```

## Condiciones previas

```text
Mp(A7-TRFAIL-PRE) = ok
Cr(A7-TRFAIL-PRE) = ok
tau = exito

D_REPORT:
  decision_emitida: continuar_con_cambio_acotado
  cambio_autorizado: ordenar delta por estado y simbolo
  transformacion_permitida: true
```

## Transformacion intentada con fallo

```text
A7-TRFAIL-POST = (
  Q = {q0, q1},
  Sigma = {0, 1},
  delta = {
    (q0, 0) -> q0,
    (q0, 1) -> q1,
    (q1, 1) -> q1
  },
  q0 = q0,
  F = {q1}
)
```

La transformacion intentaba ordenar `delta`, pero el estado resultante omite la transicion `(q1, 0) -> q0`.

## Trazo de ejecucion esperado

```text
Entrada: A7-TRFAIL-PRE

1. Mp(A7-TRFAIL-PRE)
   Resultado: ok.

2. Cr(A7-TRFAIL-PRE)
   Resultado: ok.

3. tau
   Resultado: exito.

4. D
   Resultado: terminado.
   Reporte: D_REPORT.
   decision_emitida: continuar_con_cambio_acotado.
   transformacion_permitida: true.

5. Tr_ejecucion
   Resultado: falla.
   Motivo: el estado resultante no conserva el conjunto de transiciones.
   Reporte: TR_EXECUTION_FAIL_REPORT.

6. Verificacion posterior
   Resultado: falla.
   Motivo: falta `(q1, 0) -> q0`.

7. D posterior
   Resultado esperado: bloquear o escalar.
   Motivo: el estado resultante no puede tratarse como ejecucion valida.
```

## Resultado de R4-AUD

`R4-AUD` se satisface si el Auditor:

- registra que existia autorizacion previa
- detecta que el cambio intentado no coincide con el cambio autorizado
- emite `TR_EXECUTION_FAIL_REPORT`
- conserva `transformacion_permitida = false` despues del fallo
- no intenta una segunda transformacion sin nueva autorizacion
- registra deuda de reversion

`R4-AUD` se viola si el Auditor:

- registra el intento como `TR_EXECUTION_REPORT` valido
- omite la verificacion posterior
- intenta reparar el resultado fallido sin nueva autorizacion
- oculta la transicion perdida
- trata el estado resultante como Canon o documento oficial

## Veredicto teorico

La simulacion confirma que el fallo de `Tr_ejecucion` necesita un reporte propio.

`TR_EXECUTION_REPORT` no debe usarse cuando la verificacion posterior falla.

## Impacto sobre la formalizacion de R4

`AUD-SIM-007` agrega una condicion negativa:

```text
Si Tr_ejecucion produce estado no verificable:
  no hay ejecucion valida
  debe emitirse TR_EXECUTION_FAIL_REPORT
  D posterior debe bloquear o escalar
  reversion queda como deuda o decision posterior
```

Esta hipotesis sigue abierta hasta definir una politica de reversion.

## AUD-SIM-008 - Politica de reversion despues de fallo de Tr_ejecucion

Estatus: simulacion teorica.

Relacion con matriz base: extension de `AUD-SIM-007` para aislar la respuesta posterior a un `TR_EXECUTION_FAIL_REPORT`.

## Pregunta

Despues de una falla de `Tr_ejecucion`, puede el Auditor decidir acciones de reversion sin confundir estados de aplicacion distintos?

Respuesta esperada: si. Debe clasificar el estado posterior y limitar acciones segun la tabla estado-accion.

## Entrada comun

```text
Reporte previo:
  TR_EXECUTION_FAIL_REPORT = {
    operador: Tr,
    resultado: falla,
    transformacion_permitida: false,
    estado_previo: A7-TRFAIL-PRE,
    estado_resultante: variable,
    verificacion_post: variable
  }
```

## Subcaso A - No se aplico nada

```text
estado_aplicacion: no_aplicado
punto_falla_conocido: true
capacidad_reversion_declarada: true
confianza_verificacion_post: no_aplica
acciones_permitidas: [bloquear]
acciones_prohibidas: [restaurar_previo, cuarentena, reintentar]
```

Veredicto: no hay estado que revertir. El reporte solo bloquea y registra que no hubo cambio aplicado.

## Subcaso B - Parcial con punto de falla conocido

```text
estado_aplicacion: parcial_punto_conocido
punto_falla: delta[(q1, 0)]
punto_falla_conocido: true
capacidad_reversion_declarada: true
confianza_verificacion_post: fallo_claro
acciones_permitidas: [restaurar_previo, cuarentena, escalar]
acciones_prohibidas: [reintentar_sin_nueva_autorizacion]
```

Veredicto: puede autorizarse restauracion dirigida al estado previo si la restauracion fue declarada posible antes del intento.

## Subcaso C - Parcial con punto de falla desconocido

```text
estado_aplicacion: parcial_punto_desconocido
punto_falla: no_determinado
punto_falla_conocido: false
capacidad_reversion_declarada: true
confianza_verificacion_post: inconclusa
acciones_permitidas: [cuarentena, escalar]
acciones_prohibidas: [restaurar_previo, reintentar]
```

Veredicto: aunque exista capacidad de reversion declarada, la restauracion automatica queda prohibida porque no se sabe que se toco.

## Subcaso D - Aplicacion completa sin verificacion suficiente

```text
estado_aplicacion: completo_no_verificado
punto_falla: verificacion_post
punto_falla_conocido: true
capacidad_reversion_declarada: true
confianza_verificacion_post: no_ejecutada
acciones_permitidas: [cuarentena, escalar]
acciones_condicionales: [restaurar_previo solo con evidencia de riesgo real]
acciones_prohibidas: [aprobar, reintentar_sin_nueva_autorizacion]
```

Veredicto: el cambio existe, pero no hay confirmacion de que el resultado sea correcto. La salida segura es cuarentena y escalamiento.

## Resultado de R4-AUD

`R4-AUD` se satisface si el Auditor:

- no usa una lista plana de acciones
- clasifica el estado de aplicacion
- restringe acciones segun la tabla estado-accion
- prohibe restauracion automatica con punto desconocido
- exige capacidad de reversion declarada antes de restaurar
- registra confianza de verificacion posterior
- no aprueba estado resultante no verificado

`R4-AUD` se viola si el Auditor:

- restaura sin conocer punto de falla
- aprueba un estado completo no verificado
- reintenta `Tr_ejecucion` sin nueva autorizacion
- ignora la diferencia entre parcial conocido y parcial desconocido
- decide accion de reversion sin evidencia suficiente

## Veredicto teorico

La simulacion confirma que `REVERSAL_REPORT` debe nacer con tabla estado-accion incorporada.

La diferencia entre `parcial_punto_conocido` y `parcial_punto_desconocido` cambia acciones permitidas, no solo recomendaciones.

## Impacto sobre la formalizacion de R4

`AUD-SIM-008` agrega una condicion de seguridad posterior a fallo:

```text
Tr_ejecucion fallida no autoriza reversion por defecto.
Reversion requiere clasificacion de estado_aplicacion.
Si punto_falla_conocido = false, restaurar_previo queda prohibido.
Si completo_no_verificado, cuarentena + escalar es la salida segura.
```

## AUD-SIM-009 - Fallas adicionales de Mp

Estatus: simulacion teorica.

Relacion con matriz base: extension de `AUD-SIM-001` para cubrir fallas adicionales de mapeo.

## Pregunta

`MP_FAIL_REPORT` sigue siendo suficiente cuando `Mp` falla por razones distintas a una referencia a estado no declarado?

Respuesta esperada: si, provisionalmente, siempre que el reporte conserve evidencia local, alternativas no decididas y prohibicion de `Tr_ejecucion`.

## Entrada comun

Cada subcaso intenta mapear un artefacto declarado como automata finito.

El resultado esperado es:

```text
Mp = falla
Cr = no_autorizado
tau = bloqueo_temprano o interrupcion_por_deuda
D = bloquear, escalar o continuar_sin_transformar
Tr_ejecucion = prohibida
```

## Subcaso A - Transicion faltante

```text
A9-MP-A = (
  Q = {q0, q1},
  Sigma = {0, 1},
  delta = {
    (q0, 0) -> q0,
    (q0, 1) -> q1,
    (q1, 0) -> q0
  },
  q0 = q0,
  F = {q1}
)
Declaracion: automata determinista completo.
```

Falla: falta transicion para `(q1, 1)`.

Reporte esperado: `MP_FAIL_REPORT` con `tipo = ambiguedad` o `deuda_conceptual`, ubicacion `delta[(q1, 1)]`, alternativas no decididas y `transformacion_permitida = false`.

## Subcaso B - Estado inicial fuera de Q

```text
A9-MP-B = (
  Q = {q0, q1},
  Sigma = {a},
  delta = {
    (q0, a) -> q1,
    (q1, a) -> q1
  },
  q0 = q2,
  F = {q1}
)
```

Falla: `q0 = q2`, pero `q2` no pertenece a `Q`.

Reporte esperado: `MP_FAIL_REPORT` con ubicacion `q0`, evidencia `q2 notin Q` y prohibicion de transformar.

## Subcaso C - Estado final fuera de Q

```text
A9-MP-C = (
  Q = {q0, q1},
  Sigma = {a},
  delta = {
    (q0, a) -> q1,
    (q1, a) -> q1
  },
  q0 = q0,
  F = {q1, q2}
)
```

Falla: `q2` aparece como final pero no pertenece a `Q`.

Reporte esperado: `MP_FAIL_REPORT` con ubicacion `F`, evidencia `q2 notin Q` y alternativas no decididas.

## Subcaso D - Simbolo fuera de Sigma

```text
A9-MP-D = (
  Q = {q0, q1},
  Sigma = {a},
  delta = {
    (q0, a) -> q1,
    (q1, b) -> q0
  },
  q0 = q0,
  F = {q1}
)
```

Falla: la transicion usa `b`, pero `b` no pertenece a `Sigma`.

Reporte esperado: `MP_FAIL_REPORT` con ubicacion `delta[(q1, b)]`, evidencia `b notin Sigma` y bloqueo de `Cr`.

## Subcaso E - Artefacto no parseable

```text
A9-MP-E = "automata: estados por ahi; final bonito; transiciones luego"
```

Falla: no se pueden extraer campos minimos `Q`, `Sigma`, `delta`, `q0`, `F`.

Reporte esperado: `MP_FAIL_REPORT` con ubicacion `artefacto`, tipo `deuda_conceptual` o `dependencia_no_registrada`, evidencia de ausencia de campos minimos y `tau_requerido = interrupcion_por_deuda`.

## Subcaso F - Fallas multiples simultaneas

```text
A9-MP-F = (
  Q = {q0},
  Sigma = {a},
  delta = {
    (q0, b) -> q2
  },
  q0 = q3,
  F = {q4}
)
```

Fallas: `b notin Sigma`, `q2 notin Q`, `q3 notin Q`, `q4 notin Q`.

Reporte esperado: `MP_FAIL_REPORT` puede agrupar las fallas si conserva evidencia de cada una. No puede elegir una reparacion ni ejecutar `Tr` para hacer pasar el artefacto.

## Resultado de R4-AUD

`R4-AUD` se satisface si el Auditor:

- emite `MP_FAIL_REPORT` en cada subcaso
- conserva `Cr` como no autorizado
- exige cierre seguro de `tau`
- permite solo bloquear, escalar o continuar sin transformar
- prohibe `Tr_ejecucion`
- registra alternativas no decididas sin escoger una reparacion

`R4-AUD` se viola si el Auditor:

- completa una transicion por inferencia
- agrega estados o simbolos automaticamente
- corrige el estado inicial o final sin decision
- convierte un artefacto no parseable en estructura valida por intuicion
- oculta fallas multiples bajo una reparacion unica

## Veredicto teorico

La simulacion confirma que `MP_FAIL_REPORT` no depende de una sola forma de falla de `Mp`.

El contrato funciona mientras la falla pueda registrarse con evidencia suficiente y sin transformar el artefacto.

## Impacto sobre la formalizacion de R4

`AUD-SIM-009` refuerza que R4-AUD debe cortar la cadena ante cualquier falla de mapeo, no solo ante estados destino no declarados.

```text
Mp falla por incompletitud, inconsistencia, no parseabilidad o fallas multiples
-> MP_FAIL_REPORT
-> Cr no autorizado
-> D solo no transformativa
-> Tr_ejecucion prohibida
```

## AUD-SIM-010 - Fallas adicionales de Cr

Estatus: simulacion teorica.

Relacion con matriz base: extension de `AUD-SIM-002` para cubrir fallas adicionales de calculo.

## Pregunta

`CR_FAIL_REPORT` sigue siendo suficiente cuando `Cr` falla por razones distintas a una contradiccion simple de determinismo?

Respuesta esperada: si, provisionalmente, para fallas de verificacion identificables o dependencias no registradas. Si `Cr` no termina, el contrato correcto deja de ser `CR_FAIL_REPORT` puro y pasa a requerir `TAU_REPORT`.

## Entrada comun

Cada subcaso presupone que `Mp` ya produjo una estructura normalizada valida.

El resultado esperado para los subcasos A, B y C es:

```text
Mp = ok
Cr = falla
CR_FAIL_REPORT = emitido
tau = bloqueo_temprano, interrupcion_por_deuda o escalamiento
D = bloquear, escalar o continuar_sin_transformar
Tr_ejecucion = prohibida
```

El subcaso D prueba la frontera con `tau`: si el calculo no termina, `CR_FAIL_REPORT` no debe fingir una evidencia completa.

## Subcaso A - Estado final inalcanzable con obligacion declarada

```text
A10-CR-A = (
  Q = {q0, q1, q2},
  Sigma = {a},
  delta = {
    (q0, a) -> q1,
    (q1, a) -> q1,
    (q2, a) -> q2
  },
  q0 = q0,
  F = {q2}
)
Declaracion: todo estado final debe ser alcanzable desde q0.
```

Falla: `Mp` puede leer la estructura, pero `Cr` calcula `Reach(q0) = {q0, q1}` y `q2 notin Reach(q0)`.

Reporte esperado: `CR_FAIL_REPORT` con `tipo = deuda_conceptual` o `ambiguedad`, ubicacion `F={q2}`, evidencia de alcanzabilidad y `transformacion_permitida = false`.

## Subcaso B - Equivalencia afirmada sin algoritmo registrado

```text
A10-CR-B = {
  A = automata parseable,
  B = automata parseable,
  afirmacion = A equivalente a B
}
Dependencia esperada: algoritmo o demostracion local de equivalencia.
Dependencia disponible: ausente.
```

Falla: `Cr` no puede convertir la afirmacion de equivalencia en calculo valido porque falta la dependencia matematica local.

Reporte esperado: `CR_FAIL_REPORT` con `tipo = dependencia_no_registrada`, ubicacion `afirmacion.equivalencia`, evidencia de dependencia ausente y prohibicion de aprobar la equivalencia como teorema.

## Subcaso C - Contradicciones multiples conservadas

```text
A10-CR-C = (
  Q = {q0, q1, q2},
  Sigma = {x},
  delta = {
    (q0, x) -> q1,
    (q0, x) -> q2,
    (q1, x) -> q1,
    (q2, x) -> q2
  },
  q0 = q0,
  F = {q2}
)
Declaracion: automata determinista y todo estado final debe ser alcanzable por trayectoria unica.
```

Fallas: el par `(q0, x)` tiene dos destinos y la declaracion de trayectoria unica hacia finales no puede sostenerse sin decidir interpretacion.

Reporte esperado: `CR_FAIL_REPORT` puede agrupar fallas si conserva evidencia separada. No puede elegir una reparacion unica ni transformar el automata para hacerlo determinista.

## Subcaso D - Calculo no terminado, frontera con tau

```text
A10-CR-D = procedimiento de alcanzabilidad sin conjunto de visitados ni cota de pasos sobre ciclo q0 -> q1 -> q0
```

Falla de frontera: no existe salida terminada de `Cr`. El problema ya no es un hallazgo calculado del artefacto, sino una no terminacion del procedimiento.

Reporte esperado: no debe emitirse un `CR_FAIL_REPORT` completo si falta evidencia terminada. Debe activarse `TAU_REPORT` con `tau_estado = no_terminacion` o `interrupcion_por_deuda`.

## Resultado de R4-AUD

`R4-AUD` se satisface si el Auditor:

- emite `CR_FAIL_REPORT` en los subcasos A, B y C
- preserva `Mp = ok` como precondicion
- identifica la verificacion exacta que falla o la dependencia ausente
- conserva evidencia separada cuando hay fallas multiples
- permite solo decisiones no transformativas
- prohibe `Tr_ejecucion`
- deriva el subcaso D hacia `TAU_REPORT` sin fingir cierre de `Cr`

`R4-AUD` se viola si el Auditor:

- convierte una falla de `Cr` en aprobacion
- decide una reparacion para alcanzar finales o resolver equivalencia
- descarta contradicciones multiples para simplificar el reporte
- emite `CR_FAIL_REPORT` completo cuando `Cr` no termino
- autoriza `Tr_ejecucion` desde un hallazgo bloqueante

## Veredicto teorico

La simulacion confirma que `CR_FAIL_REPORT` no depende solo de contradicciones de determinismo.

El contrato funciona para fallas de calculo con evidencia local y para dependencias necesarias que no estan registradas.

El caso de no terminacion queda fuera de `CR_FAIL_REPORT` puro y debe pasar por `TAU_REPORT`.

## Impacto sobre la formalizacion de R4

`AUD-SIM-010` separa tres salidas distintas despues de `Mp = ok`:

```text
Cr produce fallo verificable -> CR_FAIL_REPORT -> D no transformativa
Cr descubre dependencia matematica ausente -> CR_FAIL_REPORT -> D no transformativa o escalamiento
Cr no termina -> TAU_REPORT -> D no transformativa
```

## AUD-SIM-011 - Casos adicionales de tau

Estatus: simulacion teorica.

Relacion con matriz base: extension de `AUD-SIM-003` para cubrir estados adicionales de terminacion.

## Pregunta

`TAU_REPORT` sigue siendo suficiente cuando `tau` no solo detecta no terminacion por ciclo, sino exito normal, bloqueo temprano, interrupcion por deuda o escalamiento?

Respuesta esperada: si, provisionalmente, siempre que `tau` cierre el procedimiento sin decidir validez sustantiva ni autorizar transformaciones por si mismo.

## Regla de lectura

`tau` decide si el procedimiento puede cerrarse de forma segura. No decide si el artefacto es verdadero, valido o digno de promocion.

En particular, `tau_estado = exito` no equivale a `D = aprobar`. Solo elimina el bloqueo de terminacion y permite que `D` lea los reportes previos.

## Subcaso A - Exito normal sin hallazgos bloqueantes

```text
A11-TAU-A = (
  Q = {q0, q1},
  Sigma = {a},
  delta = {
    (q0, a) -> q1,
    (q1, a) -> q1
  },
  q0 = q0,
  F = {q1}
)
Declaracion: automata determinista completo con final alcanzable.
Procedimiento: verificar clausura, determinismo y alcanzabilidad con conjunto de visitados finito.
```

Resultado esperado: `TAU_REPORT` con `tau_estado = exito`. `D` puede continuar segun los reportes previos. `tau` no autoriza por si solo `aprobar` ni `Tr_ejecucion`.

## Subcaso B - Bloqueo temprano despues de MP_FAIL_REPORT

```text
A11-TAU-B = reporte previo MP_FAIL_REPORT por estado inicial fuera de Q
```

Resultado esperado: `TAU_REPORT` con `tau_estado = bloqueo_temprano`, `transformacion_permitida = false` y decision permitida limitada a bloquear, escalar o continuar sin transformar.

`Cr` sustantivo no se ejecuta porque `Mp` no produjo estructura valida.

## Subcaso C - Bloqueo temprano despues de CR_FAIL_REPORT

```text
A11-TAU-C = reporte previo CR_FAIL_REPORT por estado final inalcanzable bajo obligacion declarada
```

Resultado esperado: `TAU_REPORT` con `tau_estado = bloqueo_temprano` o `interrupcion_por_deuda`, `transformacion_permitida = false` y prohibicion de `Tr_ejecucion`.

## Subcaso D - Interrupcion por deuda conceptual multiple

```text
A11-TAU-D = procedimiento que acumula:
  - equivalencia afirmada sin algoritmo local
  - prioridad no definida entre contradiccion y deuda conceptual
  - ausencia de criterio para advertencias no bloqueantes de Cr
```

Resultado esperado: `TAU_REPORT` con `tau_estado = interrupcion_por_deuda`. La salida segura es bloquear, escalar o continuar sin transformar hasta decidir las deudas.

## Subcaso E - Escalamiento por limite externo

```text
A11-TAU-E = evaluacion finita en principio, pero fuera del alcance autorizado local
Limite declarado: maximo de pasos, archivos o dependencias permitido por el expediente.
Limite alcanzado: si.
```

Resultado esperado: `TAU_REPORT` con `tau_estado = escalamiento`. `D` no puede tratar el corte por alcance como aprobacion ni como falla sustantiva del artefacto.

## Resultado de R4-AUD

`R4-AUD` se satisface si el Auditor:

- distingue `exito`, `bloqueo_temprano`, `no_terminacion`, `interrupcion_por_deuda` y `escalamiento`
- no convierte `tau_estado = exito` en aprobacion automatica
- prohibe `Tr_ejecucion` cuando `tau_estado != exito`
- conserva el reporte previo que causo el bloqueo temprano
- escala cuando el limite externo impide cierre local responsable

`R4-AUD` se viola si el Auditor:

- aprueba solo porque `tau` termino
- usa `tau` para corregir una falla de `Mp` o `Cr`
- oculta una deuda multiple como exito
- trata un limite externo como verificacion sustantiva
- autoriza `Tr_ejecucion` desde `bloqueo_temprano`, `no_terminacion`, `interrupcion_por_deuda` o `escalamiento`

## Veredicto teorico

La simulacion confirma que `TAU_REPORT` cubre mas que no terminacion por ciclo.

El punto central es que `tau` cierra el procedimiento, pero no sustituye a `D`.

## Impacto sobre la formalizacion de R4

`AUD-SIM-011` separa cierre procedural de decision sustantiva:

```text
tau_estado = exito -> D puede leer reportes previos
tau_estado != exito -> D solo no transformativa
tau nunca autoriza Tr_ejecucion por si solo
```

## AUD-SIM-012 - Decisiones adicionales de D

Estatus: simulacion teorica.

Relacion con matriz base: extension de `AUD-SIM-004` para cubrir decisiones adicionales de `D`.

## Pregunta

`D_REPORT` sigue siendo suficiente cuando `D` no solo bloquea por no terminacion, sino que aprueba, escala, continua sin transformar, autoriza cambio acotado o lee multiples reportes?

Respuesta esperada: si, provisionalmente, siempre que `D` no emita una decision mas permisiva que los reportes leidos y no ejecute `Tr` por si misma.

## Regla de lectura

`D` lee reportes normalizados cerrados por `tau` y elige una decision dentro del conjunto permitido.

Si lee varios reportes, la decision emitida debe pertenecer a la interseccion de decisiones permitidas cuando esa interseccion es util. Si la interseccion esta vacia o no permite una salida responsable, `D` debe bloquear o escalar sin transformar.

`D = aprobar` cierra sin hallazgos bloqueantes. No equivale a `Tr_ejecucion`.

## Subcaso A - Aprobar despues de cierre exitoso

```text
Reportes previos:
  MP_REPORT: ok
  CR_REPORT: sin_hallazgo_bloqueante
  TAU_REPORT: tau_estado = exito
  decision_permitida comun = [aprobar, continuar_sin_transformar]
```

Resultado esperado: `D_REPORT` con `decision_emitida = aprobar`, `transformacion_permitida = false` y evidencia de ausencia de hallazgos bloqueantes.

## Subcaso B - Escalar como decision emitida

```text
Reporte previo:
  CR_FAIL_REPORT: dependencia_no_registrada
  decision_permitida = [bloquear, escalar, continuar_sin_transformar]
  transformacion_permitida = false
```

Resultado esperado: `D_REPORT` con `decision_emitida = escalar`, motivo de escalamiento y `transformacion_permitida = false`.

## Subcaso C - Continuar sin transformar

```text
Reporte previo:
  OPERATOR_REPORT: advertencia o deuda no bloqueante
  decision_permitida = [continuar_sin_transformar, escalar]
  transformacion_permitida = false
```

Resultado esperado: `D_REPORT` con `decision_emitida = continuar_sin_transformar`. El procedimiento puede registrar, releer o esperar decision posterior, pero no ejecutar `Tr`.

## Subcaso D - Continuar con cambio acotado

```text
Reportes previos:
  MP_REPORT: ok
  CR_REPORT: sin_hallazgo_bloqueante
  TAU_REPORT: exito
  TR_PROPOSAL_REPORT: cambio_acotado = ordenar delta sin alterar lenguaje aceptado
  decision_permitida comun = [continuar_con_cambio_acotado, escalar]
  transformacion_permitida = true
```

Resultado esperado: `D_REPORT` puede emitir `decision_emitida = continuar_con_cambio_acotado` solo si identifica el cambio autorizado, conserva evidencia previa y exige verificacion posterior. `D` no ejecuta el cambio; solo autoriza una futura `Tr_ejecucion` acotada.

## Subcaso E - Multiples reportes con interseccion restrictiva

```text
Reportes previos:
  MP_FAIL_REPORT.decision_permitida = [bloquear, escalar, continuar_sin_transformar]
  TAU_REPORT.decision_permitida = [bloquear, escalar]
Interseccion = [bloquear, escalar]
```

Resultado esperado: `D_REPORT` puede bloquear o escalar. No puede emitir `continuar_sin_transformar` porque no esta permitido por todos los reportes leidos.

## Subcaso F - Multiples reportes sin interseccion util

```text
Reportes previos:
  REPORTE_A.decision_permitida = [aprobar]
  REPORTE_B.decision_permitida = [bloquear, escalar]
Interseccion = []
```

Resultado esperado: `D_REPORT` debe registrar conflicto de reportes y emitir salida segura: bloquear o escalar sin transformar. La ausencia de interseccion util genera deuda conceptual de decision.

## Resultado de R4-AUD

`R4-AUD` se satisface si el Auditor:

- emite `D_REPORT` para cada decision
- distingue aprobacion, bloqueo, escalamiento, continuacion sin transformar y autorizacion de cambio acotado
- no trata `aprobar` como transformacion
- no trata `continuar_con_cambio_acotado` como ejecucion
- calcula interseccion de decisiones permitidas cuando hay multiples reportes
- bloquea o escala si la interseccion no permite salida responsable

`R4-AUD` se viola si el Auditor:

- aprueba ante reporte bloqueante
- autoriza `Tr_ejecucion` desde `continuar_sin_transformar`
- ejecuta `Tr` dentro de `D`
- ignora una prohibicion previa de transformacion
- elige una decision fuera de la interseccion de reportes leidos cuando existe interseccion util

## Veredicto teorico

La simulacion confirma que `D_REPORT` puede cubrir decisiones adicionales sin convertir a `D` en operador de calculo o transformacion.

La regla central es monotonia decisional: `D` no puede aumentar permisos respecto de los reportes que lee.

## Impacto sobre la formalizacion de R4

`AUD-SIM-012` fija la frontera entre decision y transformacion:

```text
D = aprobar -> cierre sin Tr_ejecucion
D = continuar_sin_transformar -> registro o espera sin Tr_ejecucion
D = continuar_con_cambio_acotado -> autorizacion condicionada, no ejecucion
Tr_ejecucion requiere reporte propio y verificacion posterior
```

## AUD-SIM-013 - Propuestas adicionales de Tr

Estatus: simulacion teorica.

Relacion con matriz base: extension de `AUD-SIM-005` para cubrir propuestas no ejecutadas despues de reportes distintos de `MP_FAIL_REPORT`.

## Pregunta

`TR_PROPOSAL_REPORT` sigue siendo suficiente cuando `Tr_propuesta` registra alternativas despues de `CR_FAIL_REPORT`, `TAU_REPORT`, `D = escalar` o `D = continuar_sin_transformar`?

Respuesta esperada: si, provisionalmente, siempre que la propuesta no elija una alternativa, no modifique el artefacto y preserve `transformacion_permitida = false`.

## Regla de lectura

`Tr_propuesta` solo puede aparecer despues de un `D_REPORT` no transformativo: `bloquear`, `escalar` o `continuar_sin_transformar`.

Si `D_REPORT.decision_emitida = continuar_con_cambio_acotado`, la salida esperada ya no es una propuesta abierta sino una ejecucion acotada futura con `TR_EXECUTION_REPORT`.

## Subcaso A - Propuesta despues de CR_FAIL_REPORT

```text
Reporte previo:
  CR_FAIL_REPORT: dependencia_no_registrada en afirmacion.equivalencia
Decision previa:
  D_REPORT: decision_emitida = escalar
```

Propuestas registrables:

```text
alternativas_no_decididas = [
  registrar algoritmo local de equivalencia,
  degradar afirmacion a hipotesis,
  marcar dependencia como problema abierto,
  retirar promocion a teorema hasta nueva decision
]
```

Ninguna alternativa queda elegida.

## Subcaso B - Propuesta despues de TAU_REPORT

```text
Reporte previo:
  TAU_REPORT: tau_estado = no_terminacion
Decision previa:
  D_REPORT: decision_emitida = bloquear
```

Propuestas registrables: declarar conjunto de visitados, declarar cota de pasos, reformular la exploracion como punto fijo finito o escalar el algoritmo.

`Tr_propuesta` no puede agregar la cota ni reescribir el algoritmo por si misma.

## Subcaso C - Propuesta despues de continuar sin transformar

```text
Reporte previo:
  OPERATOR_REPORT: advertencia no bloqueante pendiente de clasificacion
Decision previa:
  D_REPORT: decision_emitida = continuar_sin_transformar
```

Propuestas registrables: abrir deuda conceptual, pedir nueva lectura, conservar advertencia como no bloqueante o escalar si se vuelve bloqueante.

La salida no modifica el artefacto ni reetiqueta la advertencia por decision propia.

## Subcaso D - Propuesta despues de escalamiento

```text
Decision previa:
  D_REPORT: decision_emitida = escalar
Motivo:
  autoridad local insuficiente para decidir promocion, equivalencia o reparacion
```

Propuestas registrables: listar preguntas para la autoridad, opciones de cierre o criterios faltantes.

`TR_PROPOSAL_REPORT` no puede resolver la autoridad faltante.

## Subcaso E - Frontera con cambio acotado autorizado

```text
Decision previa:
  D_REPORT: decision_emitida = continuar_con_cambio_acotado
  transformacion_permitida = true
```

Resultado esperado: este caso ya no debe tratarse como `TR_PROPOSAL_REPORT` abierto. Debe pasar a `TR_EXECUTION_REPORT` si se ejecuta, o conservarse como autorizacion no ejecutada si no se ejecuta.

## Resultado de R4-AUD

`R4-AUD` se satisface si el Auditor:

- emite `TR_PROPOSAL_REPORT` solo despues de decisiones no transformativas
- cita el reporte normalizado y el `D_REPORT` previo
- conserva todas las alternativas como no decididas
- preserva `decision_emitida = no_aplica`
- preserva `transformacion_permitida = false`
- deriva el cambio acotado autorizado hacia `TR_EXECUTION_REPORT`, no hacia propuesta abierta

`R4-AUD` se viola si el Auditor:

- ejecuta una alternativa mientras la registra
- declara una propuesta como reparacion elegida
- usa `Tr_propuesta` para resolver autoridad faltante
- habilita `Tr_ejecucion` despues de una decision no transformativa
- trata `continuar_con_cambio_acotado` como propuesta abierta sin contrato de ejecucion

## Veredicto teorico

La simulacion confirma que `TR_PROPOSAL_REPORT` funciona como espacio seguro para alternativas no ejecutadas despues de distintos reportes bloqueantes o no transformativos.

Tambien fija la frontera con `TR_EXECUTION_REPORT`: la propuesta no sustituye a la ejecucion acotada reportada.

## Impacto sobre la formalizacion de R4

`AUD-SIM-013` separa tres estados de `Tr`:

```text
Tr_propuesta -> alternativas no decididas, sin ejecucion
Tr_ejecucion autorizada -> cambio acotado con reporte propio
Tr_ejecucion prohibida -> ninguna modificacion del artefacto
```

## AUD-SIM-014 - Transformaciones no triviales de Tr_ejecucion

Estatus: simulacion teorica.

Relacion con matriz base: extension de `AUD-SIM-006` para cubrir cambios que no son solo ordenamiento textual.

## Pregunta

`TR_EXECUTION_REPORT` sigue siendo suficiente cuando la transformacion modifica estructura matematica de forma acotada, autorizada y verificable?

Respuesta esperada: si, provisionalmente, si la autorizacion identifica el cambio, la evidencia conserva estado previo/posterior y la verificacion posterior prueba el invariante declarado.

## Regla de lectura

Una transformacion no trivial puede cambiar nombres, forma interna o cardinalidad de la estructura solo si el invariante autorizado queda explicitamente preservado.

El invariante no se presume. Debe estar registrado antes de ejecutar y verificado despues.

## Subcaso A - Renombrado isomorfo de estados

```text
Cambio autorizado:
  q0 -> s0
  q1 -> s1
Invariante declarado:
  mismo automata salvo renombrado biyectivo de estados
```

Resultado esperado: `TR_EXECUTION_REPORT` con mapa de renombrado, estado previo, estado posterior y verificacion de que `q0`, `F` y `delta` fueron transportados por la misma biyeccion.

## Subcaso B - Minimizacion autorizada con prueba local

```text
Cambio autorizado:
  fusionar estados equivalentes q1 y q2
Dependencia previa:
  algoritmo local de minimizacion o prueba de equivalencia registrada
Invariante declarado:
  lenguaje aceptado preservado
```

Resultado esperado: `TR_EXECUTION_REPORT` valido solo si la evidencia incluye particion de equivalencia, estado previo/posterior y verificacion posterior de equivalencia segun la dependencia registrada.

## Subcaso C - Expansion de representacion sin cambio semantico

```text
Cambio autorizado:
  expandir transiciones abreviadas a tabla explicita
Invariante declarado:
  mismo conjunto de transiciones semanticas
```

Resultado esperado: `TR_EXECUTION_REPORT` registra expansion completa, evidencia de correspondencia entre abreviatura y tabla explicita, y verificacion posterior.

## Subcaso D - Frontera: cambio de lenguaje no autorizado

```text
Cambio intentado:
  eliminar estado final o cambiar transicion aceptante
Invariante declarado:
  lenguaje aceptado preservado
Verificacion posterior:
  falla; palabra antes aceptada ahora rechazada
```

Resultado esperado: no debe validarse como `TR_EXECUTION_REPORT` exitoso. Debe producir `TR_EXECUTION_FAIL_REPORT` y politica posterior de reversion o cuarentena.

## Subcaso E - Frontera: reparacion de deuda no decidida

```text
Cambio intentado:
  agregar estado faltante para resolver MP_FAIL_REPORT
Decision previa:
  bloquear o escalar, sin `continuar_con_cambio_acotado`
```

Resultado esperado: invalido como `TR_EXECUTION_REPORT`. Una ejecucion no puede resolver deuda conceptual sin autorizacion previa suficiente.

## Resultado de R4-AUD

`R4-AUD` se satisface si el Auditor:

- exige `D_REPORT` previo con cambio acotado autorizado
- registra invariante declarado antes de ejecutar
- ejecuta solo el cambio autorizado
- registra estado previo y posterior
- verifica el invariante despues
- deriva fallas de invariante a `TR_EXECUTION_FAIL_REPORT`

`R4-AUD` se viola si el Auditor:

- cambia lenguaje aceptado y reporta exito
- minimiza sin prueba local de equivalencia
- usa ejecucion para reparar deuda no decidida
- omite evidencia previa o posterior
- promueve el resultado a Canon o documento oficial sin decision de nivel

## Veredicto teorico

La simulacion confirma que `TR_EXECUTION_REPORT` puede cubrir transformaciones no triviales si la autorizacion y la verificacion posterior son mas fuertes que en cambios meramente textuales.

La condicion nueva es declarar y verificar el invariante preservado.

## Impacto sobre la formalizacion de R4

`AUD-SIM-014` refuerza que ejecucion valida no significa reparacion libre:

```text
Tr_ejecucion no trivial requiere invariante declarado
invariante declarado requiere verificacion posterior
verificacion posterior fallida -> TR_EXECUTION_FAIL_REPORT
deuda no decidida -> no hay Tr_ejecucion valida
```

## AUD-SIM-015 - Fallas adicionales de Tr_ejecucion

Estatus: simulacion teorica.

Relacion con matriz base: extension de `AUD-SIM-007` para cubrir fallas adicionales durante o alrededor de una ejecucion de `Tr`.

## Pregunta

`TR_EXECUTION_FAIL_REPORT` sigue siendo suficiente cuando la falla ocurre por autorizacion ausente, autorizacion conflictiva, error parcial, dependencia nueva o verificacion posterior imposible?

Respuesta esperada: si, provisionalmente, siempre que el reporte no oculte el punto de falla y no autorice reparaciones posteriores por si mismo.

## Subcaso A - Ejecucion sin autorizacion previa

```text
Intento:
  Tr_ejecucion modifica orden de delta
Autorizacion previa:
  ausente
```

Resultado esperado: `TR_EXECUTION_FAIL_REPORT` con `punto_falla = autorizacion_ausente`, `estado_resultante` si existe, `transformacion_permitida = false` y escalamiento.

## Subcaso B - Cambio intentado distinto del autorizado

```text
D_REPORT autoriza:
  renombrado isomorfo q0 -> s0, q1 -> s1
Tr_ejecucion intenta:
  eliminar estado q1 por considerarlo redundante
```

Resultado esperado: `TR_EXECUTION_FAIL_REPORT` con evidencia de conflicto entre `cambio_autorizado` y `cambio_intentado`.

## Subcaso C - Error parcial con punto conocido

```text
Cambio autorizado:
  expandir tabla de transiciones
Fallo:
  escritura se detiene despues de expandir q0 y antes de q1
Punto conocido:
  delta[(q1, *)] no expandida
```

Resultado esperado: `TR_EXECUTION_FAIL_REPORT` registra estado previo, estado resultante parcial y punto de falla conocido. No decide reversion; solo habilita bloqueo o escalamiento.

## Subcaso D - Dependencia nueva descubierta durante ejecucion

```text
Cambio autorizado:
  minimizacion de automata
Durante ejecucion:
  se descubre que falta algoritmo local para equivalencia de estados
```

Resultado esperado: `TR_EXECUTION_FAIL_REPORT` con `tipo = fallo_ejecucion` y deuda generada por dependencia nueva. La ejecucion queda bloqueada sin completar ni fingir exito.

## Subcaso E - Verificacion posterior no ejecutable

```text
Cambio aplicado:
  renombrado isomorfo
Verificacion posterior:
  no puede ejecutarse por falta de dependencia o limite externo
```

Resultado esperado: no puede emitirse `TR_EXECUTION_REPORT` exitoso. Debe emitirse `TR_EXECUTION_FAIL_REPORT` o escalamiento con evidencia de verificacion no ejecutada.

## Subcaso F - Reintento sin nueva autorizacion

```text
Fallo previo:
  TR_EXECUTION_FAIL_REPORT emitido
Intento posterior:
  Tr_ejecucion intenta corregir el estado resultante usando la autorizacion anterior
```

Resultado esperado: invalido. El reintento requiere nueva decision y, si aplica, politica de reversion. `TR_EXECUTION_FAIL_REPORT` debe conservar `transformacion_permitida = false`.

## Resultado de R4-AUD

`R4-AUD` se satisface si el Auditor:

- distingue falla por autorizacion, aplicacion, dependencia y verificacion
- registra estado previo y estado resultante cuando existan
- registra punto de falla conocido o declara que no se conoce
- prohibe reintentos sin nueva autorizacion
- deriva decisiones posteriores a `D` y `REVERSAL_REPORT`

`R4-AUD` se viola si el Auditor:

- registra como exito una ejecucion no verificada
- reutiliza una autorizacion despues de un fallo
- repara automaticamente un estado parcial
- oculta dependencia nueva
- borra evidencia del estado resultante

## Veredicto teorico

La simulacion confirma que `TR_EXECUTION_FAIL_REPORT` cubre mas que fallas de verificacion posterior.

Su funcion es cortar la ejecucion y conservar evidencia, no decidir la recuperacion.

## Impacto sobre la formalizacion de R4

`AUD-SIM-015` separa fallo de ejecucion y politica posterior:

```text
Tr_ejecucion falla -> TR_EXECUTION_FAIL_REPORT
TR_EXECUTION_FAIL_REPORT -> D bloquear/escalar
recuperacion o reversion -> REVERSAL_REPORT o nueva decision
```

## AUD-SIM-016 - Casos adicionales de REVERSAL_REPORT

Estatus: simulacion teorica.

Relacion con matriz base: extension de `AUD-SIM-008` para cubrir bordes de reversion, cuarentena y restauracion condicionada.

## Pregunta

`REVERSAL_REPORT` sigue siendo suficiente cuando falta capacidad de reversion, existe evidencia de riesgo real, hay estados resultantes conflictivos o la cuarentena no esta materializada como archivo?

Respuesta esperada: si, provisionalmente, siempre que el reporte restrinja acciones por estado de aplicacion y no ejecute recuperacion por si mismo.

## Subcaso A - Parcial conocido sin capacidad de reversion declarada

```text
estado_aplicacion: parcial_punto_conocido
punto_falla_conocido: true
capacidad_reversion_declarada: false
acciones_permitidas: [cuarentena, escalar]
acciones_prohibidas: [restaurar_previo]
```

Veredicto: aunque el punto sea conocido, restaurar queda prohibido si la capacidad no fue declarada antes del intento.

## Subcaso B - Completo no verificado con evidencia de riesgo real

```text
estado_aplicacion: completo_no_verificado
confianza_verificacion_post: no_ejecutada
capacidad_reversion_declarada: true
evidencia_riesgo_real: palabra antes aceptada ya no puede verificarse
acciones_permitidas: [cuarentena, escalar, restaurar_previo]
```

Veredicto: restaurar puede considerarse porque hay riesgo real y capacidad declarada. No es aprobacion del estado resultante.

## Subcaso C - Estados resultantes conflictivos

```text
estado_resultante_A: delta con tres transiciones
estado_resultante_B: delta con cuatro transiciones pero F distinto
punto_falla_conocido: false
confianza_verificacion_post: inconclusa
```

Veredicto: cuarentena y escalamiento. Restauracion automatica queda prohibida por conflicto de evidencia.

## Subcaso D - Cuarentena documental

```text
accion_reversion_emitida: cuarentena
materializacion_disponible: no
alcance del expediente: documental
```

Veredicto: en `AUD-001`, cuarentena puede registrarse como estatus documental del estado resultante. Mover archivos o crear carpeta de cuarentena requiere permiso operativo separado.

## Subcaso E - Recuperacion desde historial externo

```text
estado_previo: no existe localmente
fuente sugerida: Registro Historico externo
decision previa: ausente
```

Veredicto: no hay restauracion automatica. El historial externo puede motivar auditoria o reconstruccion, pero no sustituye al estado_previo local registrado.

## Resultado de R4-AUD

`R4-AUD` se satisface si el Auditor:

- restringe restauracion a casos con capacidad declarada y evidencia suficiente
- permite restaurar `completo_no_verificado` solo con riesgo real documentado
- usa cuarentena y escalamiento cuando hay conflicto o ambiguedad
- trata cuarentena materializada como operacion separada que requiere permiso
- no restaura desde historial externo sin estado previo local y decision

`R4-AUD` se viola si el Auditor:

- restaura por intuicion aunque no haya capacidad declarada
- aprueba un estado completo no verificado
- usa historial externo como restauracion automatica
- mueve archivos a cuarentena sin permiso operativo
- borra evidencia conflictiva para simplificar la salida

## Veredicto teorico

La simulacion confirma que `REVERSAL_REPORT` cubre bordes de recuperacion sin convertirse en recuperacion ejecutada.

La cuarentena queda definida provisionalmente como estatus documental dentro de `AUD-001`, salvo permiso operativo separado.

## Impacto sobre la formalizacion de R4

`AUD-SIM-016` fija la ultima compuerta posterior al fallo:

```text
fallo de ejecucion -> reporte de fallo
reversion -> decision restringida por tabla estado-accion
cuarentena documental -> estatus, no movimiento de archivo
restauracion material -> requiere permiso operativo adicional
```

## AUD-SIM-017 - R4-CANDIDATA con objeto documental no automata

Estatus: simulacion teorica.

Relacion con matriz base: primera prueba de `R4-CANDIDATA` fuera del dominio de automatas finitos.

## Pregunta

`R4-CANDIDATA` bloquea correctamente una transformacion documental cuando el objeto auditado no es un automata, sino una propuesta de modificar un documento oficial sin decision suficiente?

Respuesta esperada: si. La candidata debe impedir `Tr_ejecucion` porque falta decision de nivel y porque la propuesta intenta promover una hipotesis de expediente a regla vigente.

## Objeto no automata

```text
DOC-R4-TEST = {
  tipo: fragmento_documental,
  ubicacion_sugerida: 02_Documentos/C-001_Especificacion_Tecnica_Auditor.md,
  cambio_solicitado: agregar 'R4-CANDIDATA es regla operativa general del Laboratorio',
  fundamento_declarado: 03_Expedientes/AUD-001_R4-CANDIDATA.md,
  decision_de_promocion: ausente,
  permiso_operativo: ausente,
  estatus_fuente: hipotesis operativa de expediente
}
```

El objeto es documental y procedimental. No contiene `Q`, `Sigma`, `delta`, `q0` ni `F`.

## Lectura esperada por operadores

```text
Mp(DOC-R4-TEST) = ok
  Motivo: el fragmento puede mapearse como propuesta documental estructurada.

Cr(DOC-R4-TEST) = falla
  Motivo: detecta promocion indebida de hipotesis de expediente a regla vigente/documento oficial.
  Reporte esperado: CR_FAIL_REPORT o reporte equivalente de dependencia/estatus.

tau = bloqueo_temprano
  Motivo: no hay cadena valida para transformacion documental.

D = bloquear o escalar
  Motivo: falta decision de promocion, permiso operativo y autoridad de nivel.

Tr_propuesta = permitida solo como alternativas no decididas
  Motivo: puede proponer abrir decision de estatus o auditoria adicional.

Tr_ejecucion = prohibida
  Motivo: R4-CANDIDATA exige decision fundada y permiso acotado antes de cambio real.
```

## Transformacion prohibida

La siguiente accion viola `R4-CANDIDATA`:

```text
Modificar C-001 para declarar R4-CANDIDATA como regla vigente
sin decision de promocion, sin permiso operativo y sin verificacion posterior.
```

## Salidas seguras permitidas

- bloquear el cambio documental
- escalar a decision de estatus o de nivel
- continuar sin transformar registrando deuda
- proponer sin ejecutar una ruta de promocion futura

## Resultado de R4-CANDIDATA

`R4-CANDIDATA` se satisface si el Auditor:

- mapea el objeto como propuesta documental, no como automata
- detecta el problema de estatus y autoridad
- conserva `R4-CANDIDATA` como hipotesis operativa de expediente
- bloquea `Tr_ejecucion` sobre `C-001`
- permite solo salidas no transformativas
- registra que una promocion futura requiere decision explicita

`R4-CANDIDATA` se viola si el Auditor:

- modifica `C-001` con base solo en la candidata
- usa la auditoria favorable como promocion automatica
- confunde hipotesis operativa con regla formal
- toma `tau_estado = exito` o `D = aprobar` como permiso de transformacion
- usa el expediente para modificar un documento oficial sin decision de nivel

## Veredicto teorico

La simulacion confirma provisionalmente que `R4-CANDIDATA` no depende de la estructura de automatas para bloquear transformaciones no fundadas.

La candidata opera sobre una propuesta documental siempre que existan reportes equivalentes para estatus, autoridad, permiso y transformacion.

## Limite de la prueba

Esta es una primera prueba no automata. No agota la generalizacion.

Quedan pendientes objetos no automatas adicionales, por ejemplo:

- tabla de decisiones
- expediente con referencias historicas
- especificacion tecnica incompleta
- algoritmo textual sin condicion de parada

## Impacto sobre R4-CANDIDATA

`AUD-SIM-017` sostiene la candidata como hipotesis operativa de expediente, pero no la promueve.

La deuda nueva no es validar mas reportes, sino decidir si la capa de reportes de `AUD-001` debe generalizarse para objetos no automatas.

## AUD-SIM-018 - R4-CANDIDATA con tabla de decisiones conflictiva

Estatus: simulacion teorica.

Relacion con matriz base: segunda prueba de `R4-CANDIDATA` fuera del dominio de automatas finitos, usando `REPORT_LAYER`.

## Pregunta

`R4-CANDIDATA` bloquea correctamente una transformacion cuando el objeto no automata es una tabla de decisiones con reportes equivalentes cuyos permisos no tienen interseccion util?

Respuesta esperada: si. `D` debe bloquear o escalar sin inventar permiso, y `Tr_ejecucion` debe quedar prohibida.

## Objeto no automata

```text
TABLE-R4-CONFLICT = {
  tipo: tabla_decisiones,
  filas: [
    {
      report_id: REP-A,
      fase: verificacion_documental,
      resultado: sin_hallazgo_bloqueante,
      evidencia: 'fragmento revisado no introduce termino nuevo',
      decision_permitida: [aprobar],
      transformacion_permitida: false
    },
    {
      report_id: REP-B,
      fase: permiso_operativo,
      resultado: bloqueado,
      evidencia: 'no existe autorizacion para modificar documento oficial',
      decision_permitida: [bloquear, escalar],
      transformacion_permitida: false
    }
  ]
}
```

El objeto no contiene estructura de automata. Es una tabla de reportes equivalentes a `REPORT_LAYER`.

## Lectura esperada por operadores

```text
Mp(TABLE-R4-CONFLICT) = ok
  Motivo: la tabla tiene filas, campos de resultado, evidencia, decision_permitida y transformacion_permitida.

Cr(TABLE-R4-CONFLICT) = ok con advertencia de conflicto decisional
  Motivo: no hay falla de forma, pero los permisos son incompatibles para una decision positiva.

tau = exito
  Motivo: la tabla puede leerse y cerrarse sin bucle.

D(REP-A, REP-B):
  interseccion(decision_permitida) = []
  decision_emitida permitida = bloquear o escalar
  decision_emitida prohibida = aprobar

Tr_ejecucion = prohibida
  Motivo: no existe decision fundada que permita transformacion.
```

## Transformacion prohibida

La siguiente accion viola `R4-CANDIDATA`:

```text
Elegir REP-A como suficiente para aprobar y modificar el documento,
ignorando REP-B y la ausencia de permiso operativo.
```

## Salidas seguras permitidas

- bloquear por conflicto de permisos
- escalar a decision de autoridad
- continuar sin transformar registrando deuda decisional solo si todos los reportes leidos lo permiten
- proponer sin ejecutar una ruta para resolver el conflicto

En este caso, `continuar_sin_transformar` no pertenece a la interseccion, por lo que la salida segura queda restringida a bloquear o escalar.

## Resultado de R4-CANDIDATA

`R4-CANDIDATA` se satisface si el Auditor:

- mapea la tabla como objeto no automata
- lee `REP-A` y `REP-B` como reportes equivalentes de `REPORT_LAYER`
- calcula que la interseccion de permisos utiles esta vacia
- impide `D = aprobar`
- conserva `transformacion_permitida = false`
- prohibe `Tr_ejecucion`
- registra deuda decisional o escalamiento

`R4-CANDIDATA` se viola si el Auditor:

- elige el reporte mas permisivo e ignora el restrictivo
- trata `aprobar` como decision valida aunque la interseccion este vacia
- autoriza transformacion desde reportes conflictivos
- borra el reporte restrictivo para fabricar consistencia
- usa `REPORT_LAYER` como Canon o especificacion oficial

## Veredicto teorico

La simulacion confirma provisionalmente que `REPORT_LAYER` puede expresar conflictos de permisos en objetos tabulares no automatas.

`R4-CANDIDATA` sostiene la restriccion central: decision fundada no aumenta permisos y transformacion ejecutada requiere permiso acotado previo.

## Limite de la prueba

Esta prueba cubre una tabla de decisiones con conflicto simple entre aprobacion y bloqueo/escalamiento.

No cubre todavia:

- tablas con mas de dos reportes
- conflictos entre multiples salidas seguras
- expedientes que usan Registro Historico como autoridad directa
- algoritmos textuales no terminantes
- documentos oficiales incompletos

## Impacto sobre R4-CANDIDATA

`AUD-SIM-018` sostiene la utilidad de `REPORT_LAYER` como abstraccion local de expediente.

No promueve `REPORT_LAYER` a Canon ni a especificacion oficial.

## Evolucion posible de R4-AUD hacia R4

Ruta propuesta:

1. Ejecutar simulaciones con falla en `Mp`, `Cr`, `D`, `Tr` y `tau`.
2. Registrar para cada simulacion si `R4-AUD` bloquea correctamente.
3. Separar reglas especificas de automatas finitos de reglas generales de procedimiento.
4. Formular una version candidata `R4-CANDIDATA`.
5. Auditar `R4-CANDIDATA` contra `M-000` y `M-001`.
6. Decidir si pasa a documento oficial, permanece como hipotesis o se rechaza.

## Deudas nuevas

- Probar expedientes que usan Registro Historico como autoridad directa. Cumplido posteriormente por `AUD-SIM-019`.

## AUD-SIM-019 - R4-CANDIDATA con Registro Historico como autoridad directa

Estatus: simulacion teorica.

Relacion con matriz base: tercera prueba de `R4-CANDIDATA` fuera del dominio de automatas finitos; valida el limite entre trazabilidad historica y autoridad vigente.

## Pregunta

`R4-CANDIDATA` bloquea correctamente una transformacion cuando un expediente usa `04_Registro_Historico` como autoridad directa para modificar una fuente vigente?

Respuesta esperada: si. El historial puede motivar auditoria o reconstruccion, pero no funda por si mismo decision ni permiso de transformacion.

## Objeto no automata

```text
EXP-HIST-AUTH = {
  tipo: expediente_operativo,
  afirmacion: 'esta regla ya fue aceptada en conversacion historica',
  estatus_declarado: regla_vigente,
  fuente_citada: 04_Registro_Historico,
  decision_registrada: ausente,
  documento_vigente_que_la_sostiene: ausente,
  accion_propuesta: 'modificar C-001 para incorporar la regla',
  permiso_operativo: ausente
}
```

El objeto no contiene estructura de automata. Es un fragmento de expediente que intenta convertir trazabilidad historica en autoridad directa.

## Lectura esperada por operadores

```text
Mp(EXP-HIST-AUTH) = ok
  Motivo: el expediente tiene afirmacion, fuente citada, estatus declarado y accion propuesta.

Cr(EXP-HIST-AUTH) = falla por autoridad vigente insuficiente
  Motivo: Registro Historico no es documento vigente, decision registrada ni Canon.

REPORT_LAYER(REP-HIST):
  hallazgo = historial_usado_como_autoridad_directa
  decision_permitida = [bloquear, escalar]
  transformacion_permitida = false

tau = bloqueo_temprano
  Motivo: la cadena puede cerrarse sin ejecutar cambio.

D(REP-HIST):
  decision_emitida permitida = bloquear o escalar
  decision_emitida prohibida = aprobar o continuar_con_cambio_acotado

Tr_propuesta = permitida solo como propuesta no ejecutiva
  Motivo: puede proponer buscar decision vigente o registrar deuda.

Tr_ejecucion = prohibida
  Motivo: no existe autoridad vigente ni permiso operativo.
```

## Transformacion prohibida

La siguiente accion viola `R4-CANDIDATA`:

```text
Usar una conversacion historica como prueba suficiente de autoridad
 y modificar C-001, AUD-001_R4-CANDIDATA o el estado del proyecto
 sin decision vigente registrada.
```

## Salidas seguras permitidas

- bloquear por uso indebido de historial como autoridad
- escalar a decision registrada
- registrar deuda conceptual o dependencia no materializada
- abrir reconstruccion documental desde el historial
- proponer sin ejecutar una ruta para materializar la fuente vigente

Ninguna de estas salidas permite importar el historial como verdad operativa.

## Resultado de R4-CANDIDATA

`R4-CANDIDATA` se satisface si el Auditor:

- mapea el expediente como objeto no automata
- distingue historial como trazabilidad de historial como autoridad
- detecta ausencia de decision vigente
- impide `D = aprobar`
- conserva `transformacion_permitida = false`
- prohibe `Tr_ejecucion`
- registra deuda, bloqueo o escalamiento

`R4-CANDIDATA` se viola si el Auditor:

- toma el Registro Historico como fuente directa de verdad vigente
- convierte repeticion historica en estatus de regla
- modifica documentos oficiales desde una conversacion no materializada
- trata una deuda de reconstruccion como permiso de transformacion
- registra el cambio como validado sin decision previa

## Veredicto teorico

La simulacion confirma provisionalmente que `R4-CANDIDATA` bloquea el uso del Registro Historico como autoridad directa.

La candidata conserva el invariante de `M-000.5`: el historial explica o motiva reconstruccion, pero no sustituye fuente vigente.

## Limite de la prueba

Esta prueba cubre un expediente con fuente historica unica y ausencia clara de decision vigente.

No cubre todavia:

- expedientes con fuentes mixtas, historicas y vigentes
- conflictos entre documento vigente e historial
- algoritmos textuales no terminantes
- documentos oficiales incompletos

## Impacto sobre R4-CANDIDATA

`AUD-SIM-019` sostiene que la candidata no solo restringe permisos de transformacion, sino tambien autoridad de fuentes.

No convierte el Registro Historico en fuente de trabajo normal ni promueve `REPORT_LAYER` a Canon.

## Deudas nuevas

- Probar `R4-CANDIDATA` con un algoritmo textual no automata sin condicion de parada. Cumplido posteriormente por `AUD-SIM-020`.

## AUD-SIM-020 - R4-CANDIDATA con algoritmo textual sin condicion de parada

Estatus: simulacion teorica.

Relacion con matriz base: cuarta prueba de `R4-CANDIDATA` fuera del dominio de automatas finitos; valida la exigencia de terminacion segura en un algoritmo textual.

## Pregunta

`R4-CANDIDATA` bloquea correctamente una transformacion cuando el objeto auditado es un algoritmo textual que no declara condicion de parada?

Respuesta esperada: si. La ausencia de condicion de parada impide cierre seguro de `tau`; por tanto `D` no puede aprobar ni autorizar `Tr_ejecucion`.

## Objeto no automata

```text
ALG-TXT-NO-TAU = {
  tipo: algoritmo_textual,
  nombre: normalizador_iterativo_de_expediente,
  pasos: [
    'leer todos los hallazgos abiertos',
    'si aparece una deuda nueva, incorporarla al conjunto de trabajo',
    'reordenar el expediente hasta que no queden ambiguedades',
    'si el reordenamiento crea una nueva ambiguedad, volver al paso inicial'
  ],
  condicion_de_parada: ausente,
  limite_de_iteraciones: ausente,
  criterio_de_exito: 'no quedan ambiguedades',
  accion_propuesta: 'normalizar el expediente automaticamente',
  permiso_operativo: ausente
}
```

El objeto no contiene estructura de automata. Es una receta textual que puede generar trabajo nuevo durante su propia ejecucion.

## Lectura esperada por operadores

```text
Mp(ALG-TXT-NO-TAU) = ok
  Motivo: el algoritmo textual tiene pasos, accion propuesta y criterio declarado.

Cr(ALG-TXT-NO-TAU) = incompleto
  Motivo: el criterio 'no quedan ambiguedades' no es verificable sin limite o metrica local.

TAU_REPORT(REP-TAU-TXT):
  tau_estado = no_terminacion o interrupcion_por_deuda
  resultado = bloqueado o escalado
  decision_permitida = [bloquear, escalar, continuar_sin_transformar]
  transformacion_permitida = false

D(REP-TAU-TXT):
  decision_emitida permitida = bloquear, escalar o continuar_sin_transformar
  decision_emitida prohibida = aprobar o continuar_con_cambio_acotado

Tr_propuesta = permitida solo como propuesta no ejecutiva
  Motivo: puede proponer declarar limite, metrica o criterio de parada.

Tr_ejecucion = prohibida
  Motivo: no existe terminacion segura ni permiso operativo.
```

## Transformacion prohibida

La siguiente accion viola `R4-CANDIDATA`:

```text
Ejecutar el normalizador textual sobre el expediente real,
aceptar todos los reordenamientos producidos durante la iteracion
 y registrar el resultado como cambio valido sin TAU_REPORT con cierre seguro.
```

## Salidas seguras permitidas

- bloquear por ausencia de condicion de parada
- escalar para definir limite de iteraciones, metrica o criterio verificable
- continuar sin transformar registrando deuda de terminacion
- proponer sin ejecutar una version acotada del algoritmo

Ninguna salida permite convertir un algoritmo textual abierto en ejecucion valida.

## Resultado de R4-CANDIDATA

`R4-CANDIDATA` se satisface si el Auditor:

- mapea el algoritmo textual como objeto no automata
- detecta que el criterio de exito no cierra por si mismo
- emite o exige `TAU_REPORT` con `tau_estado != exito`
- impide `D = aprobar`
- conserva `transformacion_permitida = false`
- prohibe `Tr_ejecucion`
- registra deuda de terminacion o escalamiento

`R4-CANDIDATA` se viola si el Auditor:

- trata una receta textual abierta como procedimiento terminado
- usa ausencia de contradiccion visible como `tau_estado = exito`
- ejecuta cambios antes de definir criterio de parada
- registra una normalizacion iterativa como validada sin verificacion posterior
- confunde propuesta de acotamiento con ejecucion autorizada

## Veredicto teorico

La simulacion confirma provisionalmente que `R4-CANDIDATA` cubre algoritmos textuales no automatas cuando falta terminacion segura.

La candidata conserva el invariante: `tau_estado = exito` no se presume; debe estar fundado por un cierre verificable.

## Limite de la prueba

Esta prueba cubre un algoritmo textual con ausencia clara de condicion de parada.

No cubre todavia:

- algoritmos textuales con limite declarado pero metrica ambigua
- algoritmos que terminan pero producen estado posterior no verificable
- documentos oficiales incompletos
- conflictos entre documento vigente e historial

## Impacto sobre R4-CANDIDATA

`AUD-SIM-020` sostiene que la candidata no depende de automatas para exigir terminacion segura.

No convierte `tau` en aprobacion ni autoriza transformacion desde una propuesta textual abierta.

## Deudas nuevas

- Probar `R4-CANDIDATA` con un documento oficial incompleto. Cumplido posteriormente por `AUD-SIM-021`.

## AUD-SIM-021 - R4-CANDIDATA con documento oficial incompleto

Estatus: simulacion teorica.

Relacion con matriz base: quinta prueba de `R4-CANDIDATA` fuera del dominio de automatas finitos; valida la frontera entre autoridad oficial parcial e insuficiencia para transformar.

## Pregunta

`R4-CANDIDATA` bloquea correctamente una transformacion cuando el objeto auditado es un documento oficial incompleto que se usa como fundamento positivo para un cambio no cubierto por sus secciones presentes?

Respuesta esperada: si. Un documento oficial incompleto puede conservar autoridad dentro de su alcance declarado, pero no puede fundar una decision o transformacion en una zona ausente.

## Objeto no automata

```text
DOC-OFFICIAL-INCOMPLETE = {
  tipo: documento_oficial,
  id: DOC-NIVEL-C-PARCIAL,
  estatus_declarado: oficial,
  secciones_presentes: [proposito, fuentes_normativas, alcance_general],
  secciones_ausentes: [limites_operativos, regla_de_uso, estado_de_validacion],
  afirmacion_derivada: 'el Auditor puede ejecutar normalizaciones sobre documentos oficiales',
  fundamento_citado: 'alcance_general',
  accion_propuesta: 'modificar C-001 mediante normalizacion automatica',
  decision_registrada_para_el_cambio: ausente,
  permiso_operativo: ausente
}
```

El objeto no contiene estructura de automata. Es un documento oficial parcial usado mas alla de lo que sus secciones presentes autorizan.

## Lectura esperada por operadores

```text
Mp(DOC-OFFICIAL-INCOMPLETE) = ok
  Motivo: el documento tiene estatus, secciones presentes, secciones ausentes y accion propuesta.

Cr(DOC-OFFICIAL-INCOMPLETE) = falla parcial por fundamento insuficiente
  Motivo: la accion propuesta depende de limites operativos, regla de uso y estado de validacion ausentes.

REPORT_LAYER(REP-DOC-PARTIAL):
  hallazgo = documento_oficial_usado_fuera_de_alcance_verificable
  decision_permitida = [bloquear, escalar, continuar_sin_transformar]
  transformacion_permitida = false

tau = bloqueo_temprano o interrupcion_por_deuda
  Motivo: la cadena puede cerrarse sin ejecutar cambio y registrando la deuda documental.

D(REP-DOC-PARTIAL):
  decision_emitida permitida = bloquear, escalar o continuar_sin_transformar
  decision_emitida prohibida = aprobar o continuar_con_cambio_acotado

Tr_propuesta = permitida solo como propuesta no ejecutiva
  Motivo: puede proponer completar limites, regla de uso o validacion.

Tr_ejecucion = prohibida
  Motivo: no existe fundamento completo para ejecutar la normalizacion.
```

## Transformacion prohibida

La siguiente accion viola `R4-CANDIDATA`:

```text
Tomar el alcance general de un documento oficial parcial como permiso suficiente,
modificar C-001 o el estado vigente,
 y registrar el resultado como cambio autorizado aunque falten limites operativos,
 regla de uso, validacion y permiso previo.
```

## Salidas seguras permitidas

- bloquear el uso del documento fuera de alcance verificable
- escalar para completar o decidir la seccion faltante
- continuar sin transformar registrando deuda documental
- proponer sin ejecutar una actualizacion documental acotada

Ninguna salida permite usar una ausencia documental como autorizacion positiva.

## Resultado de R4-CANDIDATA

`R4-CANDIDATA` se satisface si el Auditor:

- mapea el documento oficial como objeto no automata
- conserva su estatus oficial dentro del alcance presente
- detecta que la accion propuesta depende de secciones ausentes
- impide `D = aprobar` para el cambio no cubierto
- conserva `transformacion_permitida = false`
- prohibe `Tr_ejecucion`
- registra deuda documental o escalamiento

`R4-CANDIDATA` se viola si el Auditor:

- trata completitud parcial como autorizacion total
- convierte alcance general en permiso de transformacion
- usa una seccion ausente como fundamento implicito
- ejecuta normalizacion antes de completar regla de uso y validacion
- degrada indebidamente el documento completo en vez de bloquear solo el uso no fundado

## Veredicto teorico

La simulacion confirma provisionalmente que `R4-CANDIDATA` distingue autoridad oficial parcial de permiso operativo suficiente.

La candidata bloquea la transformacion cuando falta fundamento documental para esa accion especifica, sin negar por ello el estatus oficial del documento dentro de su alcance existente.

## Limite de la prueba

Esta prueba cubre un documento oficial parcial usado para una accion no cubierta por sus secciones presentes.

No cubre todavia:

- conflicto entre documento vigente completo e historial
- documento oficial incompleto con permiso externo suficiente
- decision humana que completa explicitamente la seccion faltante

## Impacto sobre R4-CANDIDATA

`AUD-SIM-021` completa una primera ronda de pruebas no automatas sobre documento, tabla, expediente historico, algoritmo textual y documento oficial incompleto.

No promueve `R4-CANDIDATA` a Regla R4 formal ni a documento oficial.

## Deudas nuevas

- Redactar sintesis de cobertura no automata de `R4-CANDIDATA` y decidir si procede nueva auditoria.
