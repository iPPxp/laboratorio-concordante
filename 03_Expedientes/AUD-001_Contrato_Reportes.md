# AUD-001 - Contrato provisional de reportes

Estatus: definicion provisional de expediente.

Expediente padre: `AUD-001`.

## Proposito

Normalizar la forma minima de los reportes emitidos por operadores del Auditor.

Este contrato permite que `D` lea una falla de `Mp` sin inventar una salida de `Cr` y sin habilitar `Tr`.

Este archivo no es Canon, no es RFC y no modifica `02_Documentos`.

## Fuentes locales

- `03_Expedientes/AUD-001_Casos_Prueba_Auditor.md`
- `03_Expedientes/AUD-001_Simulaciones.md`
- `03_Expedientes/AUD-001_Validaciones.md`
- `01_Canon/M-000_Reglas_Fundamentales.md`
- `01_Canon/M-001_Auditoria_Arquitectonica.md`

## Principio

Un operador no comunica intuiciones. Comunica reportes.

Si un operador falla, la falla debe producir una estructura legible por `D`. Si la falla no puede estructurarse, debe registrarse como deuda conceptual de segundo orden: falla no normalizada.

## OPERATOR_REPORT

`OPERATOR_REPORT` es la forma comun provisional para reportes de operadores.

```text
OPERATOR_REPORT = {
  report_id,
  expediente,
  caso,
  operador,
  resultado,
  tipo,
  ubicacion,
  descripcion,
  evidencia,
  estatus_afirmacion,
  alternativas_no_decididas,
  decision_permitida,
  decision_emitida,
  transformacion_permitida,
  tau_requerido,
  tau_estado,
  dependencias,
  deudas_generadas
}
```

## Campos

`report_id`: identificador unico dentro del expediente.

`expediente`: expediente que produce el reporte.

`caso`: caso o simulacion asociada.

`operador`: operador que emite el reporte.

Valores permitidos iniciales:

- `Mp`
- `Cr`
- `D`
- `Tr`
- `tau`

`resultado`: estado operativo del operador.

Valores permitidos iniciales:

- `ok`
- `falla`
- `no_autorizado`
- `bloqueado`
- `escalado`
- `terminado`
- `ejecutado`

`tipo`: clasificacion del hallazgo.

Valores permitidos iniciales:

- `deuda_conceptual`
- `contradiccion`
- `ambiguedad`
- `dependencia_no_registrada`
- `violacion_r4_aud`
- `sin_hallazgo_bloqueante`
- `cambio_acotado`
- `fallo_ejecucion`
- `reversion`

`ubicacion`: lugar del artefacto donde aparece el problema.

`descripcion`: explicacion breve del hallazgo.

`evidencia`: fragmento, referencia o estructura que sostiene el hallazgo.

`estatus_afirmacion`: estatus de la afirmacion afectada segun `M-000`.

Valores permitidos iniciales:

- `definicion`
- `hipotesis`
- `teorema`
- `algoritmo`
- `expediente`
- `decision`
- `deuda_conceptual`
- `problema_abierto`
- `no_clasificado`

`alternativas_no_decididas`: lista de reparaciones o interpretaciones posibles que el Auditor no puede ejecutar.

`decision_permitida`: decisiones que `D` puede tomar leyendo el reporte.

Valores permitidos iniciales:

- `aprobar`
- `bloquear`
- `escalar`
- `continuar_sin_transformar`
- `continuar_con_cambio_acotado`

`decision_emitida`: decision emitida por `D`.

Valores permitidos iniciales:

- `aprobar`
- `bloquear`
- `escalar`
- `continuar_sin_transformar`
- `continuar_con_cambio_acotado`
- `no_aplica`

`transformacion_permitida`: indica si `Tr` puede ejecutarse.

Valores permitidos:

- `true`
- `false`

`tau_requerido`: forma de terminacion esperada.

Valores permitidos iniciales:

- `exito`
- `bloqueo_temprano`
- `no_terminacion`
- `interrupcion_por_deuda`
- `escalamiento`

`tau_estado`: forma de terminacion emitida por `tau`.

Valores permitidos iniciales:

- `exito`
- `bloqueo_temprano`
- `no_terminacion`
- `interrupcion_por_deuda`
- `escalamiento`
- `no_aplica`

`dependencias`: fuentes o reglas usadas por el reporte.

`deudas_generadas`: deudas nuevas generadas por el reporte.

## MP_FAIL_REPORT

`MP_FAIL_REPORT` especializa `OPERATOR_REPORT` para fallas de `Mp`.

```text
MP_FAIL_REPORT = OPERATOR_REPORT where:
  operador = Mp
  resultado = falla
  decision_permitida subset_of {bloquear, escalar, continuar_sin_transformar}
  transformacion_permitida = false
  tau_requerido in {bloqueo_temprano, interrupcion_por_deuda, escalamiento}
```

## Regla provisional de lectura por D

Estatus: regla provisional de expediente.

`D` puede fundarse en un `MP_FAIL_REPORT` solo para bloquear, escalar o continuar sin transformar.

`D` no puede aprobar, ni autorizar `Tr`, ni declarar completitud cuando el reporte de `Mp` tiene `resultado = falla`.

Forma:

```text
Si Mp emite MP_FAIL_REPORT:
  Cr sustantivo queda no_autorizado.
  tau debe producir cierre seguro.
  D puede bloquear, escalar o continuar_sin_transformar.
  Tr_ejecucion queda prohibida.
```

## Separacion entre propuesta y ejecucion de Tr

`Tr_propuesta` y `Tr_ejecucion` no son equivalentes.

`Tr_propuesta` puede aparecer como lista de `alternativas_no_decididas`.

`Tr_ejecucion` solo puede ocurrir si `transformacion_permitida = true`, si `D` la autoriza explicitamente y si produce `TR_EXECUTION_REPORT`.

En un `MP_FAIL_REPORT`, `Tr_ejecucion` siempre queda prohibida.

## CR_FAIL_REPORT

`CR_FAIL_REPORT` especializa `OPERATOR_REPORT` para hallazgos bloqueantes emitidos por `Cr`.

Nota: en este contrato, `resultado = falla` significa que el artefacto falla una verificacion de calculo. No significa que el operador `Cr` haya funcionado mal.

```text
CR_FAIL_REPORT = OPERATOR_REPORT where:
  operador = Cr
  resultado = falla
  decision_permitida subset_of {bloquear, escalar, continuar_sin_transformar}
  transformacion_permitida = false
  tau_requerido in {bloqueo_temprano, interrupcion_por_deuda, escalamiento}
```

## Regla provisional de lectura de CR_FAIL_REPORT por D

Estatus: regla provisional de expediente.

`D` puede fundarse en un `CR_FAIL_REPORT` solo para bloquear, escalar o continuar sin transformar.

`D` no puede aprobar ni autorizar `Tr_ejecucion` cuando `Cr` emite un hallazgo bloqueante.

Forma:

```text
Si Cr emite CR_FAIL_REPORT:
  Mp ya produjo estructura valida.
  Cr produjo hallazgo bloqueante.
  tau debe producir cierre seguro.
  D puede bloquear, escalar o continuar_sin_transformar.
  Tr_ejecucion queda prohibida.
```

## Ejemplo derivado de AUD-SIM-002

Este ejemplo materializa el reporte esperado por `AUD-SIM-002`.

```text
CR_FAIL_REPORT = {
  report_id: AUD-SIM-002-CR-FAIL-001,
  expediente: AUD-001,
  caso: AUD-SIM-002,
  operador: Cr,
  resultado: falla,
  tipo: contradiccion,
  ubicacion: delta[(q0, x)],
  descripcion: automata declara determinismo pero contiene dos destinos para el mismo par,
  evidencia: "(q0, x) -> q0; (q0, x) -> q1",
  estatus_afirmacion: definicion,
  alternativas_no_decididas: [
    tratar artefacto como no determinista,
    eliminar una transicion,
    cambiar declaracion de determinismo,
    dividir el caso en dos automatas
  ],
  decision_permitida: [bloquear, escalar],
  decision_emitida: no_aplica,
  transformacion_permitida: false,
  tau_requerido: bloqueo_temprano,
  tau_estado: no_aplica,
  dependencias: [R4-AUD, M-000, M-001],
  deudas_generadas: [
    validar TAU_REPORT contra bloqueo temprano despues de Cr
  ]
}
```

## Reglas de validez para CR_FAIL_REPORT

Un `CR_FAIL_REPORT` es valido si:

- presupone un `Mp` valido
- identifica la verificacion de `Cr` que falla
- clasifica el tipo de hallazgo
- aporta evidencia calculable
- enumera alternativas no decididas
- prohibe `Tr_ejecucion`
- habilita solo decisiones no transformativas
- exige una forma segura de `tau`

Un `CR_FAIL_REPORT` es invalido si:

- intenta reparar el artefacto
- convierte una contradiccion en aprobacion
- autoriza `Tr_ejecucion` sin decision externa
- omite la evidencia de calculo
- trata el hallazgo como teorema general

## Frontera de CR_FAIL_REPORT con TAU_REPORT

Si `Cr` no produce una salida terminada, `CR_FAIL_REPORT` no debe fingir un hallazgo completo.

En ese caso el cierre corresponde a `TAU_REPORT` con `tau_estado = no_terminacion`, `interrupcion_por_deuda` o `escalamiento`.

`CR_FAIL_REPORT` solo cubre fallas de verificacion identificables o dependencias necesarias no registradas.

## TAU_REPORT

`TAU_REPORT` especializa `OPERATOR_REPORT` para reportes emitidos por `tau`.

`tau` no decide si el artefacto es valido. `tau` decide si el procedimiento puede cerrarse de forma segura.

```text
TAU_REPORT = OPERATOR_REPORT where:
  operador = tau
  resultado in {terminado, bloqueado, escalado}
  tau_estado in {exito, bloqueo_temprano, no_terminacion, interrupcion_por_deuda, escalamiento}
  decision_permitida subset_of {aprobar, bloquear, escalar, continuar_sin_transformar}
  transformacion_permitida = false when tau_estado != exito
```

## Regla provisional de lectura de TAU_REPORT por D

Estatus: regla provisional de expediente.

`D` puede fundarse en un `TAU_REPORT` para cerrar el procedimiento de forma segura.

`D` no puede autorizar `Tr_ejecucion` si `tau_estado` es distinto de `exito`.

Forma:

```text
Si tau emite TAU_REPORT con tau_estado != exito:
  D puede bloquear, escalar o continuar_sin_transformar.
  Tr_ejecucion queda prohibida.

Si tau emite TAU_REPORT con tau_estado = exito:
  D puede continuar segun los reportes previos de Mp y Cr.
  tau_estado = exito no equivale a D = aprobar.
  Tr_ejecucion sigue requiriendo decision explicita de D y permiso compatible.
```

## Ejemplo derivado de AUD-SIM-003

Este ejemplo materializa el reporte esperado por `AUD-SIM-003`.

```text
TAU_REPORT = {
  report_id: AUD-SIM-003-TAU-REPORT-001,
  expediente: AUD-001,
  caso: AUD-SIM-003,
  operador: tau,
  resultado: bloqueado,
  tipo: deuda_conceptual,
  ubicacion: procedimiento.reachability_loop,
  descripcion: procedimiento de exploracion no declara condicion de parada suficiente,
  evidencia: "q0 -> q1 -> q0 repeats without visited set or step bound",
  estatus_afirmacion: algoritmo,
  alternativas_no_decididas: [
    declarar conjunto de visitados,
    declarar cota de pasos,
    reformular exploracion como punto fijo finito,
    escalar el procedimiento como no terminado
  ],
  decision_permitida: [bloquear, escalar],
  decision_emitida: no_aplica,
  transformacion_permitida: false,
  tau_requerido: no_terminacion,
  tau_estado: no_terminacion,
  dependencias: [R4-AUD, M-000, M-001],
  deudas_generadas: [
    validar TAU_REPORT,
    definir criterio formal de terminacion
  ]
}
```

## Reglas de validez para TAU_REPORT

Un `TAU_REPORT` es valido si:

- identifica que `tau` emite el reporte
- distingue terminacion exitosa de bloqueo, escalamiento o no terminacion
- indica el punto del procedimiento donde ocurre el corte
- aporta evidencia de la condicion de terminacion
- prohibe `Tr_ejecucion` cuando `tau_estado != exito`
- habilita solo decisiones compatibles con el estado de terminacion

Un `TAU_REPORT` es invalido si:

- marca `exito` sin evidencia de cierre
- permite `Tr_ejecucion` ante `no_terminacion`
- oculta una no terminacion como aprobacion
- omite el punto procedural donde ocurre el corte
- usa `tau` para reparar el artefacto

## D_REPORT

`D_REPORT` especializa `OPERATOR_REPORT` para decisiones emitidas por `D`.

`D` no calcula, no repara y no transforma. `D` lee reportes normalizados y emite una decision explicita.

```text
D_REPORT = OPERATOR_REPORT where:
  operador = D
  resultado in {terminado, bloqueado, escalado}
  decision_emitida in {aprobar, bloquear, escalar, continuar_sin_transformar, continuar_con_cambio_acotado}
  decision_emitida in intersection(decision_permitida de reportes leidos) when intersection is nonempty
  decision_emitida in {bloquear, escalar} when intersection is empty or inconsistent
  transformacion_permitida = false when decision_emitida in {bloquear, escalar, continuar_sin_transformar}
```

## Regla provisional de lectura de D_REPORT

Estatus: regla provisional de expediente.

`D` solo puede emitir una decision permitida por los reportes que lee, salvo cuando la interseccion es vacia o inconsistente; en ese caso solo puede bloquear o escalar sin transformar.

Si algun reporte leido prohibe `Tr_ejecucion`, `D_REPORT` no puede habilitar `Tr_ejecucion`.

Forma:

```text
Si D lee reportes normalizados:
  decision_emitida debe pertenecer a las decisiones permitidas por esos reportes si hay interseccion util.
  D no puede inventar aprobacion.
  D no puede ejecutar Tr.
  D solo puede autorizar o negar condiciones para una futura Tr.
```

`D` solo puede emitir `transformacion_permitida = true` cuando:

- `decision_emitida = continuar_con_cambio_acotado`
- todos los reportes leidos permiten transformacion
- la transformacion autorizada esta identificada de forma acotada
- la salida esperada puede auditarse con evidencia previa y posterior

## Regla provisional de interseccion de D

Cuando `D` lee varios reportes, calcula la interseccion de `decision_permitida`.

`decision_emitida` debe pertenecer a esa interseccion cuando la interseccion es util. Si la interseccion esta vacia o no permite una salida responsable, `D` debe emitir bloqueo o escalamiento sin transformar y registrar deuda decisional.

`D = aprobar` nunca autoriza `Tr_ejecucion`. `D = continuar_con_cambio_acotado` autoriza condiciones para una ejecucion posterior, pero no ejecuta el cambio.

## Ejemplo derivado de AUD-SIM-004

Este ejemplo materializa el reporte esperado por `AUD-SIM-004`.

```text
D_REPORT = {
  report_id: AUD-SIM-004-D-REPORT-001,
  expediente: AUD-001,
  caso: AUD-SIM-004,
  operador: D,
  resultado: bloqueado,
  tipo: deuda_conceptual,
  ubicacion: decision.input_reports,
  descripcion: decision bloquea porque TAU_REPORT indica no terminacion,
  evidencia: "TAU_REPORT.tau_estado = no_terminacion; TAU_REPORT.transformacion_permitida = false",
  estatus_afirmacion: decision,
  alternativas_no_decididas: [
    escalar procedimiento,
    declarar criterio de terminacion,
    reejecutar despues de completar tau
  ],
  decision_permitida: [bloquear, escalar],
  decision_emitida: bloquear,
  transformacion_permitida: false,
  tau_requerido: no_terminacion,
  tau_estado: no_terminacion,
  dependencias: [TAU_REPORT, R4-AUD, M-000, M-001],
  deudas_generadas: [
  ]
}
```

## Reglas de validez para D_REPORT

Un `D_REPORT` es valido si:

- identifica que `D` emite el reporte
- enumera o cita reportes previos normalizados
- emite una decision explicita
- no emite una decision fuera de lo permitido por los reportes leidos
- no ejecuta `Tr`
- preserva `transformacion_permitida = false` cuando algun reporte previo la prohibe
- clasifica la decision como `decision` segun `M-000`

Un `D_REPORT` es invalido si:

- aprueba ante reporte bloqueante
- autoriza `Tr_ejecucion` contra una prohibicion previa
- usa una deuda conceptual como fundamento positivo
- omite evidencia de los reportes leidos
- ejecuta una reparacion

## TR_PROPOSAL_REPORT

`TR_PROPOSAL_REPORT` especializa `OPERATOR_REPORT` para propuestas no ejecutadas de `Tr`.

`Tr_propuesta` no transforma el artefacto. Solo registra alternativas posibles para una decision futura.

```text
TR_PROPOSAL_REPORT = OPERATOR_REPORT where:
  operador = Tr
  resultado = terminado
  decision_emitida = no_aplica
  transformacion_permitida = false
  alternativas_no_decididas is not empty
  dependencias include D_REPORT
```

## Regla provisional de lectura de TR_PROPOSAL_REPORT

Estatus: regla provisional de expediente.

`TR_PROPOSAL_REPORT` solo puede aparecer despues de un reporte normalizado y una decision no transformativa de `D`.

Puede listar reparaciones posibles, pero debe conservarlas como alternativas no decididas.

Forma:

```text
Si D emite bloquear, escalar o continuar_sin_transformar:
  Tr_propuesta puede registrar alternativas no decididas.
  Tr_propuesta no puede modificar el artefacto.
  Tr_propuesta no puede declarar una alternativa como elegida.
  Tr_ejecucion queda prohibida.
```

## Ejemplo derivado de AUD-SIM-005

Este ejemplo materializa una propuesta no ejecutada despues de la falla de `Mp` registrada en `AUD-SIM-001`.

```text
TR_PROPOSAL_REPORT = {
  report_id: AUD-SIM-005-TR-PROPOSAL-001,
  expediente: AUD-001,
  caso: AUD-SIM-005,
  operador: Tr,
  resultado: terminado,
  tipo: deuda_conceptual,
  ubicacion: delta[(q1, 1)],
  descripcion: propuestas no ejecutadas para resolver referencia a estado no declarado,
  evidencia: "D_REPORT.decision_emitida = bloquear; MP_FAIL_REPORT.transformacion_permitida = false",
  estatus_afirmacion: expediente,
  alternativas_no_decididas: [
    declarar q2 en Q,
    cambiar destino de transicion,
    modificar F,
    corregir declaracion del automata
  ],
  decision_permitida: [bloquear, escalar, continuar_sin_transformar],
  decision_emitida: no_aplica,
  transformacion_permitida: false,
  tau_requerido: bloqueo_temprano,
  tau_estado: bloqueo_temprano,
  dependencias: [MP_FAIL_REPORT, D_REPORT, R4-AUD, M-000, M-001],
  deudas_generadas: [
    validar TR_EXECUTION_REPORT contra cambio acotado autorizado
  ]
}
```

## Reglas de validez para TR_PROPOSAL_REPORT

Un `TR_PROPOSAL_REPORT` es valido si:

- identifica que `Tr` opera en modo propuesta
- cita un reporte previo normalizado
- cita una decision previa de `D`
- conserva `decision_emitida = no_aplica`
- conserva `transformacion_permitida = false`
- enumera alternativas no decididas
- no modifica el artefacto
- no promueve una alternativa a decision

Un `TR_PROPOSAL_REPORT` es invalido si:

- modifica el artefacto
- declara una reparacion como elegida
- habilita `Tr_ejecucion`
- omite el `D_REPORT` previo
- convierte una deuda conceptual en decision
- se presenta como demostracion o Canon

## TR_EXECUTION_REPORT

`TR_EXECUTION_REPORT` especializa `OPERATOR_REPORT` para transformaciones ejecutadas por `Tr`.

`Tr_ejecucion` modifica un artefacto. Por eso exige autorizacion previa explicita, alcance acotado y evidencia antes/despues.

```text
TR_EXECUTION_REPORT = OPERATOR_REPORT where:
  operador = Tr
  resultado = ejecutado
  tipo = cambio_acotado
  decision_emitida = no_aplica
  transformacion_permitida = true
  tau_estado = exito
  dependencias include D_REPORT
  evidencia contains estado_previo, cambio_aplicado, estado_posterior, verificacion_post
```

## Regla provisional de lectura de TR_EXECUTION_REPORT

Estatus: regla provisional de expediente.

`TR_EXECUTION_REPORT` solo es valido si la ejecucion fue autorizada antes de ocurrir.

La autorizacion debe venir de un `D_REPORT` con `decision_emitida = continuar_con_cambio_acotado` y `transformacion_permitida = true`.

Forma:

```text
Si D emite continuar_con_cambio_acotado:
  D debe identificar el cambio permitido.
  Tr_ejecucion solo puede aplicar ese cambio.
  Tr_ejecucion debe registrar estado previo y posterior.
  Mp, Cr y tau deben poder auditar el resultado posterior.
```

`TR_EXECUTION_REPORT` no puede usarse para resolver deuda conceptual abierta. Si la ejecucion descubre una dependencia nueva, debe bloquearse o registrarse como deuda antes de continuar.

Para transformaciones no triviales, el reporte debe declarar el invariante autorizado antes de ejecutar y verificarlo despues. Si el invariante falla, el resultado no es `TR_EXECUTION_REPORT` exitoso sino `TR_EXECUTION_FAIL_REPORT`.

## Ejemplo derivado de AUD-SIM-006

Este ejemplo materializa una transformacion de representacion autorizada: ordenar `delta` sin cambiar el conjunto de transiciones.

```text
TR_EXECUTION_REPORT = {
  report_id: AUD-SIM-006-TR-EXECUTION-001,
  expediente: AUD-001,
  caso: AUD-SIM-006,
  operador: Tr,
  resultado: ejecutado,
  tipo: cambio_acotado,
  ubicacion: delta,
  descripcion: ordenamiento lexicografico de transiciones sin cambio semantico,
  evidencia: {
    autorizacion: "D_REPORT.decision_emitida = continuar_con_cambio_acotado",
    estado_previo: "delta order = [(q1,1), (q0,1), (q1,0), (q0,0)]",
    cambio_aplicado: "ordenar delta por estado y simbolo",
    estado_posterior: "delta order = [(q0,0), (q0,1), (q1,0), (q1,1)]",
    verificacion_post: "mismo Q, Sigma, q0, F y mismo conjunto de transiciones"
  },
  estatus_afirmacion: expediente,
  alternativas_no_decididas: [],
  decision_permitida: [aprobar, escalar],
  decision_emitida: no_aplica,
  transformacion_permitida: true,
  tau_requerido: exito,
  tau_estado: exito,
  dependencias: [TR_PROPOSAL_REPORT, D_REPORT, R4-AUD, M-000, M-001],
  deudas_generadas: [
    definir reporte de fallo para Tr_ejecucion
  ]
}
```

## Reglas de validez para TR_EXECUTION_REPORT

Un `TR_EXECUTION_REPORT` es valido si:

- identifica que `Tr` opera en modo ejecucion
- cita un `D_REPORT` previo que autoriza el cambio
- ejecuta solo el cambio autorizado
- registra estado previo
- registra estado posterior
- registra verificacion posterior
- mantiene trazabilidad con la propuesta o decision que origino el cambio
- no introduce dependencias nuevas sin registrarlas como deuda

Un `TR_EXECUTION_REPORT` es invalido si:

- ejecuta sin `D_REPORT` previo
- ejecuta con `transformacion_permitida = false`
- ejecuta una alternativa no autorizada
- cambia el artefacto mas alla del alcance declarado
- omite evidencia before/after
- usa la ejecucion para cerrar una deuda conceptual no decidida
- promueve el resultado a Canon

## TR_EXECUTION_FAIL_REPORT

`TR_EXECUTION_FAIL_REPORT` especializa `OPERATOR_REPORT` para fallas de `Tr_ejecucion`.

Un fallo de `Tr_ejecucion` no es una propuesta fallida. Es una ejecucion intentada que no puede registrarse como `TR_EXECUTION_REPORT` valido.

Puede ocurrir por:

- cambio intentado fuera del alcance autorizado
- error durante la aplicacion del cambio
- estado posterior no verificable
- dependencia nueva detectada durante la ejecucion
- conflicto entre autorizacion y resultado producido

```text
TR_EXECUTION_FAIL_REPORT = OPERATOR_REPORT where:
  operador = Tr
  resultado in {falla, bloqueado, escalado}
  tipo = fallo_ejecucion
  decision_emitida = no_aplica
  transformacion_permitida = false
  tau_estado in {bloqueo_temprano, interrupcion_por_deuda, escalamiento}
  dependencias include D_REPORT
  evidencia contains autorizacion, cambio_autorizado, cambio_intentado, punto_falla, estado_previo, estado_resultante, verificacion_post
```

## Regla provisional de lectura de TR_EXECUTION_FAIL_REPORT

Estatus: regla provisional de expediente.

`TR_EXECUTION_FAIL_REPORT` corta la cadena de ejecucion.

Despues de un `TR_EXECUTION_FAIL_REPORT`, `D` solo puede bloquear o escalar hasta que exista politica de reversion o decision posterior.

El reporte debe distinguir si la falla ocurrio por autorizacion ausente, conflicto entre autorizacion e intento, aplicacion parcial, dependencia nueva, verificacion posterior fallida o verificacion posterior no ejecutable.

Forma:

```text
Si Tr_ejecucion falla:
  Tr debe emitir TR_EXECUTION_FAIL_REPORT.
  Tr no puede intentar una segunda reparacion.
  D debe bloquear o escalar.
  transformacion_permitida vuelve a false.
  una politica de reversion posterior debe decidir como tratar el estado resultante.
```

## Ejemplo derivado de AUD-SIM-007

Este ejemplo materializa una falla posterior a una autorizacion valida: `Tr_ejecucion` intenta ordenar `delta`, pero el estado resultante pierde una transicion.

```text
TR_EXECUTION_FAIL_REPORT = {
  report_id: AUD-SIM-007-TR-EXECUTION-FAIL-001,
  expediente: AUD-001,
  caso: AUD-SIM-007,
  operador: Tr,
  resultado: falla,
  tipo: fallo_ejecucion,
  ubicacion: delta,
  descripcion: transformacion autorizada produjo estado posterior no verificable,
  evidencia: {
    autorizacion: "D_REPORT.decision_emitida = continuar_con_cambio_acotado",
    cambio_autorizado: "ordenar delta por estado y simbolo",
    estado_previo: "delta contiene cuatro transiciones",
    cambio_intentado: "ordenar delta",
    estado_resultante: "delta contiene tres transiciones",
    punto_falla: "verificacion_post",
    verificacion_post: "falta (q1, 0) -> q0"
  },
  estatus_afirmacion: expediente,
  alternativas_no_decididas: [
    bloquear estado resultante,
    escalar a decision humana,
    definir politica de reversion,
    reintentar solo con nueva autorizacion
  ],
  decision_permitida: [bloquear, escalar],
  decision_emitida: no_aplica,
  transformacion_permitida: false,
  tau_requerido: escalamiento,
  tau_estado: escalamiento,
  dependencias: [D_REPORT, TR_EXECUTION_REPORT, R4-AUD, M-000, M-001],
  deudas_generadas: [
    definir politica de reversion si falla la verificacion posterior,
  ]
}
```

## Reglas de validez para TR_EXECUTION_FAIL_REPORT

Un `TR_EXECUTION_FAIL_REPORT` es valido si:

- identifica que `Tr` opera en modo ejecucion
- cita la autorizacion previa o registra su ausencia
- declara el cambio autorizado y el cambio intentado
- registra el punto de falla
- registra estado previo y estado resultante si existen
- registra la verificacion posterior fallida si el fallo ocurre despues de aplicar el cambio
- conserva `transformacion_permitida = false` despues del fallo
- habilita solo bloqueo o escalamiento
- genera deuda de reversion cuando el estado resultante queda incierto

Un `TR_EXECUTION_FAIL_REPORT` es invalido si:

- oculta el fallo como ejecucion exitosa
- emite `TR_EXECUTION_REPORT` aunque la verificacion posterior falle
- intenta una segunda transformacion sin nueva autorizacion
- omite el estado previo o el estado resultante disponible
- mantiene `transformacion_permitida = true` despues del fallo
- usa el fallo para cerrar una deuda conceptual
- promueve el estado resultante a Canon o documento oficial

## REVERSAL_REPORT

`REVERSAL_REPORT` especializa `OPERATOR_REPORT` para decidir que hacer despues de un `TR_EXECUTION_FAIL_REPORT`.

No es una reversion ejecutada por si misma. Es el reporte que clasifica el estado posterior al fallo y declara que acciones quedan permitidas.

```text
REVERSAL_REPORT = OPERATOR_REPORT where:
  operador = D
  resultado in {bloqueado, escalado, terminado}
  tipo = reversion
  dependencias include TR_EXECUTION_FAIL_REPORT
  evidencia contains estado_aplicacion, punto_falla, capacidad_reversion_declarada, confianza_verificacion_post, accion_reversion_permitida, estado_previo, estado_resultante, verificacion_post
```

## Estados de aplicacion post-fallo

`REVERSAL_REPORT` debe clasificar el estado posterior en uno de estos valores:

- `no_aplicado`
- `parcial_punto_conocido`
- `parcial_punto_desconocido`
- `completo_no_verificado`

## Tabla estado-accion

| Estado de aplicacion | Acciones permitidas | Acciones prohibidas | Condicion |
| --- | --- | --- | --- |
| `no_aplicado` | `bloquear` | `restaurar_previo`, `cuarentena`, `reintentar` | no hay cambio que revertir |
| `parcial_punto_conocido` | `restaurar_previo`, `cuarentena`, `escalar` | `reintentar` sin nueva autorizacion | restaurar solo si hay capacidad de reversion declarada y punto exacto de falla |
| `parcial_punto_desconocido` | `cuarentena`, `escalar` | `restaurar_previo` automatico, `reintentar` | no se sabe con precision que se toco |
| `completo_no_verificado` | `cuarentena`, `escalar`; `restaurar_previo` solo con evidencia de riesgo real | `aprobar`, `reintentar` sin nueva autorizacion | el cambio existe, pero no hay confirmacion suficiente de resultado correcto |

## Campos obligatorios adicionales

Ademas de los campos de `OPERATOR_REPORT`, `REVERSAL_REPORT` debe declarar en `evidencia`:

- `estado_aplicacion`
- `punto_falla`
- `punto_falla_conocido`
- `capacidad_reversion_declarada`
- `confianza_verificacion_post`
- `accion_reversion_permitida`
- `accion_reversion_emitida`
- `estado_previo`
- `estado_resultante`
- `verificacion_post`

Valores iniciales para `capacidad_reversion_declarada`:

- `true`
- `false`
- `no_declarada`

Valores iniciales para `confianza_verificacion_post`:

- `fallo_claro`
- `no_ejecutada`
- `inconclusa`
- `no_aplica`

## Regla provisional de lectura de REVERSAL_REPORT

Estatus: regla provisional de expediente.

`REVERSAL_REPORT` no puede aprobar el estado resultante de una ejecucion fallida.

`REVERSAL_REPORT` solo puede habilitar restauracion dirigida cuando:

- `estado_aplicacion = parcial_punto_conocido`
- `punto_falla_conocido = true`
- `capacidad_reversion_declarada = true`
- la accion autorizada es volver exactamente al `estado_previo` registrado

Si `estado_aplicacion = parcial_punto_desconocido`, la restauracion automatica queda prohibida.

Si `estado_aplicacion = completo_no_verificado`, la accion minima es cuarentena y escalamiento. Restaurar solo puede considerarse si existe evidencia de riesgo real en el estado resultante y capacidad de reversion declarada.

En `AUD-001`, `cuarentena` significa estatus documental del estado resultante. Mover, copiar o aislar archivos materialmente requiere permiso operativo adicional.

## Ejemplo derivado de AUD-SIM-008

```text
REVERSAL_REPORT = {
  report_id: AUD-SIM-008-REVERSAL-001,
  expediente: AUD-001,
  caso: AUD-SIM-008-B,
  operador: D,
  resultado: terminado,
  tipo: reversion,
  ubicacion: tr_ejecucion.post_failure_state,
  descripcion: fallo parcial con punto de falla conocido permite restauracion dirigida si la capacidad fue declarada antes del intento,
  evidencia: {
    estado_aplicacion: parcial_punto_conocido,
    punto_falla: delta[(q1, 0)],
    punto_falla_conocido: true,
    capacidad_reversion_declarada: true,
    confianza_verificacion_post: fallo_claro,
    accion_reversion_permitida: [restaurar_previo, cuarentena, escalar],
    accion_reversion_emitida: restaurar_previo,
    estado_previo: "A7-TRFAIL-PRE",
    estado_resultante: "A7-TRFAIL-POST",
    verificacion_post: "falta (q1, 0) -> q0"
  },
  estatus_afirmacion: decision,
  alternativas_no_decididas: [cuarentena, escalar],
  decision_permitida: [continuar_con_cambio_acotado, escalar],
  decision_emitida: continuar_con_cambio_acotado,
  transformacion_permitida: true,
  tau_requerido: escalamiento,
  tau_estado: escalamiento,
  dependencias: [TR_EXECUTION_FAIL_REPORT, D_REPORT, R4-AUD, M-000, M-001],
  deudas_generadas: [
  ]
}
```

## Reglas de validez para REVERSAL_REPORT

Un `REVERSAL_REPORT` es valido si:

- cita un `TR_EXECUTION_FAIL_REPORT` previo
- clasifica `estado_aplicacion` segun la tabla estado-accion
- declara capacidad de reversion antes de emitir accion
- declara confianza de verificacion posterior
- no permite acciones fuera de la fila correspondiente
- prohibe restauracion automatica cuando el punto de falla es desconocido
- conserva cuarentena y escalamiento como salida segura ante ambiguedad
- no trata el estado resultante como ejecucion valida

Un `REVERSAL_REPORT` es invalido si:

- restaura automaticamente con punto de falla desconocido
- aprueba un estado completo no verificado
- omite capacidad de reversion declarada
- omite confianza de verificacion posterior
- reintenta `Tr_ejecucion` sin nueva autorizacion
- borra evidencia del estado fallido
- promueve el estado resultante a Canon o documento oficial

## Ejemplo derivado de AUD-SIM-001

```text
MP_FAIL_REPORT = {
  report_id: AUD-SIM-001-MP-FAIL-001,
  expediente: AUD-001,
  caso: AUD-SIM-001,
  operador: Mp,
  resultado: falla,
  tipo: deuda_conceptual,
  ubicacion: delta[(q1, 1)],
  descripcion: transicion referencia estado no declarado,
  evidencia: "(q1, 1) -> q2; q2 notin Q",
  estatus_afirmacion: definicion,
  alternativas_no_decididas: [
    declarar q2 en Q,
    cambiar destino de transicion,
    modificar F,
    corregir declaracion del automata
  ],
  decision_permitida: [bloquear, escalar],
  decision_emitida: no_aplica,
  transformacion_permitida: false,
  tau_requerido: bloqueo_temprano,
  tau_estado: no_aplica,
  dependencias: [R4-AUD, M-000, M-001],
  deudas_generadas: [
    decidir reparacion correcta,
    validar contrato MP_FAIL_REPORT
  ]
}
```

## Reglas de validez

Un `MP_FAIL_REPORT` es valido si:

- identifica el operador que falla
- clasifica el tipo de hallazgo
- indica ubicacion y evidencia
- enumera alternativas no decididas
- prohibe `Tr_ejecucion`
- habilita solo decisiones no transformativas
- exige una forma segura de `tau`

Un `MP_FAIL_REPORT` es invalido si:

- incluye una reparacion ya ejecutada
- permite `aprobar`
- permite `Tr_ejecucion`
- omite la evidencia
- usa una deuda conceptual como fundamento positivo
- promueve una hipotesis a decision

## Relacion con R4-AUD

`MP_FAIL_REPORT` convierte la falla de `Mp` en entrada legible para `D`.

Esto sostiene `R4-AUD` porque impide la cadena:

```text
Mp falla -> Cr simulado -> D inventada -> Tr ejecutada
```

Y reemplaza esa cadena por:

```text
Mp falla -> MP_FAIL_REPORT -> tau bloqueo_temprano -> D bloquear/escalar -> Tr no ejecutada
```

## Deudas abiertas

- Precisar si `continuar_sin_transformar` permite nuevas lecturas o solo registro.
