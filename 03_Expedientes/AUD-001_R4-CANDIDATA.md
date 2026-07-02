# AUD-001 - R4-CANDIDATA

Estatus: hipotesis operativa de expediente por `EST-R4-CANDIDATA-001`.

Expediente padre: `AUD-001`.

Decision de estatus: `03_Expedientes/AUD-001_Decision_Estatus_R4-CANDIDATA.md`.

Fuente principal: `03_Expedientes/AUD-001_Invariantes_R4-AUD.md`.

## Proposito

Redactar una candidata local de la Regla R4 a partir de los invariantes validados provisionalmente en `AUD-001`.

Esta candidata no es Canon, no es documento oficial y no modifica `M-000`, `M-001` ni `C-001`. No modifica Canon, documentos oficiales ni decisiones registradas.

Su funcion es dar una forma auditable a `R4-AUD` para decidir si puede evolucionar hacia una regla general del Laboratorio.

## Estatus de afirmacion

`R4-CANDIDATA` tiene estatus de hipotesis operativa de expediente.

No debe citarse como teorema, Canon, decision arquitectonica ni regla vigente fuera de `AUD-001` hasta que exista auditoria y decision explicita.

## Fuentes locales

- `01_Canon/M-000_Reglas_Fundamentales.md`
- `01_Canon/M-001_Auditoria_Arquitectonica.md`
- `02_Documentos/C-001_Especificacion_Tecnica_Auditor.md`
- `03_Expedientes/AUD-001_Casos_Prueba_Auditor.md`
- `03_Expedientes/AUD-001_Contrato_Reportes.md`
- `03_Expedientes/AUD-001_Simulaciones.md`
- `03_Expedientes/AUD-001_Validaciones.md`
- `03_Expedientes/AUD-001_Invariantes_R4-AUD.md`

## Vocabulario provisional

Esta candidata usa el vocabulario operacional de `AUD-001`:

```text
Procedimiento = (Mp, Cr, tau, D, Tr)
```

Donde:

- `Mp` mapea o normaliza el artefacto.
- `Cr` calcula, verifica o detecta hallazgos sobre lo mapeado.
- `tau` cierra la terminacion del procedimiento.
- `D` emite decision explicita fundada en reportes.
- `Tr` propone o ejecuta transformaciones segun permiso.

Este vocabulario sigue siendo provisional y no debe confundirse con una ontologia canonica.

## Definicion candidata

Sea `P` un procedimiento del Laboratorio aplicado a un artefacto `A`.

`R4-CANDIDATA(P, A)` se satisface si ninguna transformacion ejecutada sobre `A` ocurre sin que antes exista una cadena fundada, trazable y terminada.

Forma:

```text
Tr_ejecucion(A) es valida solo si existen antes:

1. Mp(A) = ok, o un reporte normalizado de falla de Mp que bloquee Tr_ejecucion.
2. Cr opera solo sobre salida valida de Mp, o emite reporte normalizado de falla.
3. tau produce cierre seguro del procedimiento.
4. D emite decision explicita fundada en reportes normalizados.
5. D autoriza cambio acotado con transformacion_permitida = true.
6. Tr_ejecucion aplica solo el cambio autorizado.
7. Tr_ejecucion registra evidencia previa y posterior.
8. La verificacion posterior confirma el invariante declarado.
```

Si cualquiera de esas condiciones falla, `Tr_ejecucion` queda prohibida o deja de ser valida.

## Salidas seguras ante falla

Cuando la cadena no alcanza condiciones para ejecucion valida, las salidas permitidas son:

- bloquear
- escalar
- continuar sin transformar
- registrar propuesta no ejecutada
- emitir reporte de fallo
- activar politica posterior al fallo sin recuperacion material automatica

Ninguna de estas salidas autoriza por si misma una transformacion ejecutada.

## Condiciones positivas

Una ejecucion puede considerarse valida bajo esta candidata si satisface todas estas condiciones:

- existe `D_REPORT` previo con `decision_emitida = continuar_con_cambio_acotado`
- `transformacion_permitida = true` fue emitido antes de ejecutar
- el cambio autorizado esta identificado de forma acotada
- el cambio intentado coincide con el cambio autorizado
- existe estado previo registrado
- existe estado posterior registrado
- existe verificacion posterior
- si la transformacion es no trivial, existe invariante declarado antes de ejecutar
- la verificacion posterior confirma el invariante declarado
- el resultado no promueve por si mismo afirmaciones a Canon, documento oficial o decision arquitectonica

## Condiciones de violacion

`R4-CANDIDATA` se viola si ocurre cualquiera de estos patrones:

- `Tr_ejecucion` ocurre sin `D_REPORT` previo suficiente
- `Tr_ejecucion` ocurre despues de una falla de `Mp`, `Cr` o `tau` sin reporte y decision compatible
- `D` aprueba desde reporte bloqueante
- `D` emite una decision mas permisiva que los reportes leidos
- `tau_estado = exito` se usa como aprobacion automatica
- `D = aprobar` se usa como permiso de transformacion
- `Tr_propuesta` modifica el artefacto o elige una reparacion
- `Tr_ejecucion` modifica mas que el alcance autorizado
- una verificacion posterior fallida se registra como exito
- un fallo de ejecucion autoriza reintento o reversion automatica
- una deuda conceptual se cierra por ejecucion no decidida
- el Registro Historico se usa como autoridad directa para transformar

## Decision sobre capa de reportes

Por `CAPA-REPORTES-R4-001`, los nombres concretos de reportes de `AUD-001` permanecen locales.

`R4-CANDIDATA` puede usar una capa abstracta equivalente: `REPORT_LAYER`, entendida como reportes normalizados suficientes para fundar decision, permiso, ejecucion y recuperacion.

## Relacion con reportes de AUD-001

La candidata depende de los reportes normalizados validados en `AUD-001`:

- `MP_FAIL_REPORT`
- `CR_FAIL_REPORT`
- `TAU_REPORT`
- `D_REPORT`
- `TR_PROPOSAL_REPORT`
- `TR_EXECUTION_REPORT`
- `TR_EXECUTION_FAIL_REPORT`
- `REVERSAL_REPORT`

Esta dependencia no significa que esos nombres deban volverse Canon. Significa que la candidata necesita una capa de reportes equivalentes si se generaliza fuera de `AUD-001`.

## Generalizacion pretendida

La parte generalizable de `R4-CANDIDATA` no es el automata finito, sino la restriccion procedimental:

```text
transformar requiere decision fundada;
decision fundada requiere reportes;
reportes requieren calculo o falla normalizada;
calculo requiere mapeo valido;
toda cadena requiere terminacion segura;
todo cambio ejecutado requiere evidencia y verificacion posterior.
```

## Elementos no generalizados

Quedan fuera de la definicion candidata general:

- `Q`, `Sigma`, `delta`, `q0`, `F` como estructura de automatas
- determinismo como propiedad especifica de automatas
- alcanzabilidad de finales como calculo particular
- minimizacion de automatas como transformacion particular
- equivalencia de automatas como dependencia matematica especifica

Estos elementos siguen siendo ejemplos de prueba, no contenido de la regla candidata.

## Relacion con M-000

La candidata respeta provisionalmente `M-000` porque:

- declara su estatus como hipotesis operativa de expediente
- no se promueve automaticamente a Canon
- registra fuentes y trazabilidad
- marca dependencias pendientes como deudas conceptuales
- no usa historial como autoridad directa

Esta relacion debe ser auditada formalmente antes de cualquier promocion.

## Relacion con M-001

La candidata queda lista para auditoria porque identifica:

- alcance
- fuentes leidas
- afirmaciones relevantes
- dependencias
- posibles hallazgos
- deudas conceptuales
- recomendacion de siguiente fase

La auditoria debe verificar si el texto introduce ambiguedades, promociones indebidas o dependencias no registradas.

## Pruebas no automata iniciales

`R4-CANDIDATA` fue probada provisionalmente contra:

- un objeto documental no automata en `AUD-SIM-017` y `VAL-017`
- una tabla de decisiones conflictiva con `REPORT_LAYER` en `AUD-SIM-018` y `VAL-018`
- un expediente que usa Registro Historico como autoridad directa en `AUD-SIM-019` y `VAL-019`
- un algoritmo textual sin condicion de parada en `AUD-SIM-020` y `VAL-020`
- un documento oficial incompleto en `AUD-SIM-021` y `VAL-021`

Estas pruebas sostienen la candidata como hipotesis operativa de expediente y completan una primera ronda no automata, pero no agotan la generalizacion fuera de automatas.

Sintesis asociada: `03_Expedientes/AUD-001_Sintesis_Cobertura_No_Automata_R4-CANDIDATA.md`.

Decision asociada: `03_Expedientes/AUD-001_Decision_Auditoria_Post-No-Automata_R4-CANDIDATA.md`.

Auditoria posterior asociada: `03_Expedientes/AUD-001_Auditoria_Post-No-Automata_R4-CANDIDATA.md`.

Decision de cierre asociada: `03_Expedientes/AUD-001_Decision_Cierre_Ronda_No_Automata_R4-CANDIDATA.md`.

Decision de siguiente fase asociada: `03_Expedientes/AUD-001_Decision_Siguiente_Fase_R4-CANDIDATA.md`.

Criterios de promocion asociados: `03_Expedientes/AUD-001_Criterios_Promocion_R4-CANDIDATA.md`.

Auditoria de criterios asociada: `03_Expedientes/AUD-001_Auditoria_Criterios_Promocion_R4-CANDIDATA.md`.

Decision de estatus de criterios asociada: `03_Expedientes/AUD-001_Decision_Estatus_Criterios_Promocion_R4-CANDIDATA.md`.

Decision de ruta asociada: `03_Expedientes/AUD-001_Decision_Ruta_Siguiente_R4-CANDIDATA.md`.

Decision de pausa asociada: `03_Expedientes/AUD-001_Decision_Pausa_Operativa_R4-CANDIDATA.md`.

## Deudas antes de promocion

Antes de cualquier promocion fuera de `AUD-001`, falta:

- reactivar `AUD-001` mediante decision explicita si se busca una ruta futura
- decidir si una ruta futura reabre definicion provisional, Nivel C, `REPORT_LAYER`, R4 formal o congelamiento
- decidir si requiere documento de Nivel C o expediente adicional
- definir si la capa de reportes de `AUD-001` se generaliza o permanece como implementacion local del Auditor
- ampliar pruebas no automatas o justificar cierre provisional de la primera ronda
- precisar relacion con la futura Regla R4 formal

## Veredicto de redaccion

`R4-CANDIDATA` queda redactada como candidata de expediente y lista para auditoria.

No queda aprobada como regla formal.

## Siguiente paso recomendado

Objetivo cumplido posteriormente por `AUD-001_Decision_Pausa_Operativa_R4-CANDIDATA.md`.
