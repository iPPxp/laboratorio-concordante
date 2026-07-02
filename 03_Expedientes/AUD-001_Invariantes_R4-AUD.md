# AUD-001 - Invariantes de R4-AUD

Estatus: sintesis provisional de expediente.

Expediente padre: `AUD-001`.

## Proposito

Extraer invariantes comunes de `AUD-SIM-001` a `AUD-SIM-016` para decidir si `R4-AUD` puede evolucionar hacia una candidata `R4-CANDIDATA`.

Este archivo no es Canon, no es documento oficial y no define la Regla R4 formal. Es una pieza de trabajo para preparar una candidata auditable.

## Fuentes locales

- `03_Expedientes/AUD-001_Casos_Prueba_Auditor.md`
- `03_Expedientes/AUD-001_Contrato_Reportes.md`
- `03_Expedientes/AUD-001_Simulaciones.md`
- `03_Expedientes/AUD-001_Validaciones.md`
- `02_Documentos/C-001_Especificacion_Tecnica_Auditor.md`
- `01_Canon/M-000_Reglas_Fundamentales.md`
- `01_Canon/M-001_Auditoria_Arquitectonica.md`

## Base de extraccion

La base de extraccion son dieciseis simulaciones y dieciseis validaciones provisionales:

- `AUD-SIM-001` a `AUD-SIM-016`.
- `VAL-001` a `VAL-016`.

La cadena cubre fallas y salidas de `Mp`, `Cr`, `tau`, `D`, `Tr_propuesta`, `Tr_ejecucion`, `TR_EXECUTION_FAIL_REPORT` y `REVERSAL_REPORT`.

## Invariantes confirmados

### INV-R4-AUD-001 - Precedencia operacional

`Tr_ejecucion` solo puede ocurrir despues de una cadena fundada:

```text
Mp valido
-> Cr sin hallazgo bloqueante o reporte bloqueante normalizado
-> tau con cierre seguro
-> D_REPORT compatible
-> autorizacion explicita de cambio acotado
-> Tr_ejecucion reportada
```

Si falla `Mp`, `Cr` o `tau`, la cadena no puede llegar a `Tr_ejecucion`.

### INV-R4-AUD-002 - Reporte antes que decision

Toda falla relevante debe convertirse en reporte normalizado antes de que `D` pueda decidir.

`D` no decide desde intuicion, estado implicito o historial conversacional. Decide leyendo reportes.

### INV-R4-AUD-003 - Decision no aumenta permisos

`D` no puede emitir una decision mas permisiva que los reportes leidos.

Si lee varios reportes, debe respetar la interseccion util de `decision_permitida`. Si la interseccion esta vacia o es inconsistente, la salida segura es bloquear o escalar sin transformar.

### INV-R4-AUD-004 - Aprobacion no transforma

`D = aprobar` cierra sin hallazgos bloqueantes, pero no ejecuta `Tr`.

Aprobacion y transformacion son actos distintos.

### INV-R4-AUD-005 - Propuesta no ejecuta

`Tr_propuesta` puede registrar alternativas no decididas despues de decisiones no transformativas.

Una propuesta no elige reparacion, no modifica el artefacto y no resuelve autoridad faltante.

### INV-R4-AUD-006 - Ejecucion requiere permiso acotado

`Tr_ejecucion` requiere `D_REPORT` previo con:

- `decision_emitida = continuar_con_cambio_acotado`
- `transformacion_permitida = true`
- cambio autorizado identificado
- evidencia previa y posterior exigible

Sin esos campos, no hay ejecucion valida.

### INV-R4-AUD-007 - Ejecucion no trivial requiere invariante declarado

Cuando una transformacion cambia estructura matematica o representacion no meramente textual, debe declarar antes el invariante que preserva.

La verificacion posterior debe comprobar ese invariante. Si falla, no hay `TR_EXECUTION_REPORT` exitoso.

### INV-R4-AUD-008 - Fallo de ejecucion corta la cadena

Un fallo de `Tr_ejecucion` produce `TR_EXECUTION_FAIL_REPORT`, conserva evidencia y devuelve `transformacion_permitida = false`.

El fallo no autoriza reintento, reparacion ni reversion por si mismo.

### INV-R4-AUD-009 - Reversion es politica, no reflejo automatico

Despues de un `TR_EXECUTION_FAIL_REPORT`, la recuperacion requiere `REVERSAL_REPORT` o nueva decision.

Restaurar solo es admisible bajo condiciones declaradas: estado de aplicacion clasificado, punto de falla conocido cuando corresponda, capacidad de reversion declarada y evidencia suficiente.

### INV-R4-AUD-010 - Terminacion no aprueba

`tau_estado = exito` solo elimina el bloqueo de terminacion. No equivale a `D = aprobar`.

Si `tau_estado != exito`, `Tr_ejecucion` queda prohibida.

### INV-R4-AUD-011 - Historial no sustituye autoridad

Registro Historico, conversaciones o memoria externa pueden motivar auditoria o reconstruccion, pero no sustituyen reportes, decisiones ni documentos vigentes.

### INV-R4-AUD-012 - Cuarentena documental no es movimiento material

En `AUD-001`, cuarentena significa estatus documental del estado resultante.

Mover, copiar o aislar archivos materialmente requiere permiso operativo adicional.

## Fronteras negativas

`R4-AUD` prohibe, en las simulaciones validadas:

- ejecutar `Tr` despues de una falla de `Mp`, `Cr` o `tau`
- aprobar desde un reporte bloqueante
- usar `tau_estado = exito` como aprobacion automatica
- usar `D = aprobar` como autorizacion de transformacion
- convertir una propuesta en reparacion elegida
- ejecutar sin `D_REPORT` previo suficiente
- usar ejecucion para resolver deuda conceptual no decidida
- registrar exito cuando la verificacion posterior falla o no se ejecuta
- restaurar automaticamente con punto de falla desconocido
- usar Registro Historico como autoridad directa

## Especifico de automatas finitos

Los siguientes elementos pertenecen al objeto de prueba y no deben pasar tal cual a `R4-CANDIDATA`:

- estados `Q`, alfabeto `Sigma`, transicion `delta`, estado inicial `q0` y finales `F`
- determinismo como propiedad especifica de automatas
- alcanzabilidad de estados finales como calculo concreto
- equivalencia de automatas como dependencia matematica local
- minimizacion de automatas como ejemplo de transformacion no trivial

Estos elementos sirven para falsar o ilustrar, no para definir la regla general.

## Generalizable a procedimiento

Los siguientes elementos si parecen candidatos a regla general:

- precedencia entre mapeo, calculo, terminacion, decision y transformacion
- normalizacion de reportes antes de decidir
- monotonia de permisos en `D`
- separacion entre propuesta y ejecucion
- autorizacion previa y alcance acotado para cambios reales
- evidencia antes/despues para toda ejecucion
- verificacion posterior obligatoria
- tratamiento seguro de fallos de ejecucion
- politica posterior a fallo separada de la ejecucion
- respeto de niveles de autoridad y estatus de afirmaciones

## Forma candidata minima

Una forma candidata de `R4` podria expresarse asi, todavia como expediente:

```text
R4-CANDIDATA(P, A):
  Ninguna transformacion ejecutada sobre A es valida si no existe antes:
    1. mapeo valido o reporte normalizado de falla,
    2. calculo terminado o reporte normalizado de falla,
    3. cierre de terminacion seguro,
    4. decision explicita fundada en reportes,
    5. permiso de transformacion acotado,
    6. evidencia previa y posterior,
    7. verificacion posterior satisfactoria.

  Si cualquiera de esas condiciones falla,
  la salida permitida es bloquear, escalar, continuar sin transformar,
  proponer sin ejecutar, o activar politica posterior al fallo segun reporte normalizado.
```

Esta forma no debe copiarse a Canon sin auditoria.

## Veredicto provisional

Si alcanza para redactar `R4-CANDIDATA` como expediente.

No alcanza para declarar la Regla R4 formal ni para modificar Canon.

La candidata debe nacer con estatus de hipotesis o definicion provisional de expediente, y debe auditarse contra `M-000` y `M-001` antes de cualquier promocion.

## Siguiente paso recomendado

Redactar `03_Expedientes/AUD-001_R4-CANDIDATA.md` usando estos invariantes como fuente principal.

Esa candidata debe separar claramente:

- regla general de procedimiento
- ejemplos derivados de automatas finitos
- condiciones de validez
- condiciones de violacion
- deudas restantes antes de cualquier promocion
