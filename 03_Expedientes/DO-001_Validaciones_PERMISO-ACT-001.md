# DO-001 - Validaciones de PERMISO-ACT-001

Estatus: expediente asociado.

Expediente padre: `DO-001`.

Fecha: 2026-07-01.

Objeto validado: `PERMISO-ACT-001` en `DO-001_Regla_Permiso_Actualizacion.md`.

## Proposito

Validar si la regla local de permiso distingue correctamente entre recomendacion, autorizacion y cambio ejecutado.

Estas validaciones no autorizan cambios nuevos por si mismas. Solo prueban la regla contra casos locales.

## Fuentes locales

- `CURRENT_STATE.md`
- `05_Estado_Proyecto/ESTADO_ACTUAL.md`
- `01_Canon/M-000_Reglas_Fundamentales.md`
- `01_Canon/M-001_Auditoria_Arquitectonica.md`
- `03_Expedientes/DO-001.md`
- `03_Expedientes/DO-001_DO-CHECK-001.md`
- `03_Expedientes/DO-001_Regla_Permiso_Actualizacion.md`
- `03_Expedientes/DO-001_Validaciones_DO-CHECK-001.md`

## PERM-VAL-001 - Actualizacion de estado autorizada

Estatus: validado provisionalmente.

Caso: una instruccion humana explicita solicita registrar en `CURRENT_STATE.md`, `ESTADO_ACTUAL.md` y `CHANGELOG.md` una pieza ya materializada en expedientes.

Archivo materializado: `03_Expedientes/DO-001_Regla_Permiso_Actualizacion.md`.

Pregunta: `PERMISO-ACT-001` permite convertir esa instruccion en cambio ejecutado de estado operativo?

Respuesta: si, provisionalmente.

```text
PERMISSION_CHECK = {
  validation_id: PERM-VAL-001,
  regla: PERMISO-ACT-001,
  caso: actualizacion_estado_operativo,
  autorizacion: instruccion_humana_explicita,
  objetivo: [CURRENT_STATE.md, 05_Estado_Proyecto/ESTADO_ACTUAL.md, CHANGELOG.md],
  alcance: registrar pieza ya materializada y actualizar proximo objetivo,
  superficie: estado_operativo,
  resultado: permitido,
  condicion: cambio acotado, trazable y sin modificacion de Canon, documentos oficiales o expedientes cerrados,
  verificacion_posterior: revisar referencias cruzadas y ASCII,
  transformacion_permitida: true
}
```

Resultado: la regla permite actualizaciones acotadas de estado operativo cuando registran hechos ya materializados y existe instruccion humana explicita.

Limite: el permiso no se extiende a Canon, documentos oficiales ni expedientes cerrados.

## PERM-VAL-002 - Recomendacion sin autorizacion

Estatus: validado provisionalmente.

Caso: un `DO_CHECK_REPORT` propone actualizar un archivo, pero no existe decision registrada, `D_REPORT` valido ni instruccion humana explicita.

Pregunta: `PERMISO-ACT-001` permite ejecutar el cambio?

Respuesta: no.

```text
PERMISSION_CHECK = {
  validation_id: PERM-VAL-002,
  regla: PERMISO-ACT-001,
  caso: recomendacion_sin_autorizacion,
  autorizacion: ausente,
  objetivo: archivo_no_especificado,
  alcance: recomendacion de cambio,
  superficie: no_determinada,
  resultado: bloqueado,
  condicion: una recomendacion no ejecuta y `DO_CHECK_REPORT` conserva `transformacion_permitida = false`,
  verificacion_posterior: no_aplica,
  transformacion_permitida: false
}
```

Resultado: la regla bloquea correctamente la cadena recomendacion -> ejecucion cuando falta autorizacion previa.

Limite: un reporte puede motivar una decision posterior, pero no reemplazarla.

## PERM-VAL-003 - Cambio de nivel superior con permiso insuficiente

Estatus: validado provisionalmente.

Caso: una instruccion simple intenta modificar Canon, un documento oficial o un expediente cerrado sin decision registrada.

Pregunta: `PERMISO-ACT-001` permite ejecutar el cambio?

Respuesta: no; debe bloquearse o escalarse segun la superficie afectada.

```text
PERMISSION_CHECK = {
  validation_id: PERM-VAL-003,
  regla: PERMISO-ACT-001,
  caso: nivel_superior_o_expediente_cerrado,
  autorizacion: instruccion_humana_simple,
  objetivo: [01_Canon, 02_Documentos, expediente_cerrado],
  alcance: cambio sustantivo o reapertura/cierre,
  superficie: nivel_superior_o_cerrado,
  resultado: escalado,
  condicion: requiere decision registrada, trazabilidad completa o condicion de reapertura segun M-000.7,
  verificacion_posterior: no_aplica hasta que exista autorizacion valida,
  transformacion_permitida: false
}
```

Resultado: la regla conserva separacion de niveles. Una instruccion simple no basta para modificar Canon, documentos oficiales o expedientes cerrados.

Limite: si existe decision registrada posterior, el caso debe revalidarse con la decision como fuente de autorizacion.

## Checklist comun

| Criterio | PERM-VAL-001 | PERM-VAL-002 | PERM-VAL-003 |
| --- | --- | --- | --- |
| Distingue recomendacion de autorizacion | pasa | pasa | pasa |
| Identifica fuente de autorizacion | pasa | pasa | pasa |
| Declara superficie afectada | pasa | pasa | pasa |
| Conserva separacion de niveles | pasa | pasa | pasa |
| Prohibe ejecucion sin autorizacion | pasa | pasa | pasa |
| Exige decision para nivel superior o cerrado | no aplica | no aplica | pasa |
| Exige verificacion posterior cuando hay ejecucion | pasa | no aplica | no aplica |

## Resultado general

`PERMISO-ACT-001` queda validado provisionalmente contra tres casos locales.

La regla distingue correctamente:

- actualizacion acotada de estado operativo autorizada por instruccion humana explicita
- recomendacion sin autorizacion
- cambio de nivel superior o expediente cerrado con permiso insuficiente

## Deudas derivadas

- Definir reporte de fallo para `Tr_ejecucion`.
- Definir politica de reversion si falla la verificacion posterior.
- Validar `PERMISO-ACT-001` contra un `D_REPORT` con `continuar_con_cambio_acotado` cuando exista un caso local adecuado.

## Criterio de suficiencia

La regla es suficiente para continuar la fase documental de `DO-001` sin convertir recomendaciones en cambios reales por accidente.

El siguiente objetivo operativo recomendado es definir el reporte de fallo para `Tr_ejecucion`.
