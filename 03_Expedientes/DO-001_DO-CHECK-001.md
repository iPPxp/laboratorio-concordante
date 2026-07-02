# DO-001 - DO-CHECK-001

Estatus: algoritmo provisional de expediente.

Expediente padre: `DO-001`.

Fecha: 2026-07-01.

## Proposito

Definir `DO-CHECK-001` como primera superficie automatizable no mutante del Laboratorio Concordante.

`DO-CHECK-001` no modifica archivos, no cierra expedientes, no promueve estatus y no ejecuta transformaciones. Solo lee artefactos locales y emite un reporte de trazabilidad, estatus y bloqueo.

## Fuentes locales

- `CURRENT_STATE.md`
- `05_Estado_Proyecto/ESTADO_ACTUAL.md`
- `01_Canon/M-000_Reglas_Fundamentales.md`
- `01_Canon/M-001_Auditoria_Arquitectonica.md`
- `03_Expedientes/DO-001.md`
- `03_Expedientes/DO-001_Auditoria_DO-PROP-001.md`
- `03_Expedientes/AUD-001_Contrato_Reportes.md`

## Definicion provisional

`DO-CHECK-001` es un procedimiento de lectura que recibe un archivo local o un conjunto acotado de archivos locales y produce un `DO_CHECK_REPORT`.

Forma:

```text
DO-CHECK-001(entrada_local)
-> leer fuentes minimas
-> inspeccionar estatus, dependencias y permisos
-> emitir DO_CHECK_REPORT
-> no modificar archivos
```

## Estatus de salida

`DO_CHECK_REPORT` es un reporte provisional de expediente.

No es Canon.

No es RFC.

No es todavia `OPERATOR_REPORT`, porque `AUD-001_Contrato_Reportes.md` no define un operador `DO-CHECK`.

`DO_CHECK_REPORT` debe conservar compatibilidad conceptual con `OPERATOR_REPORT` para que pueda integrarse despues si existe una decision explicita.

## Entradas permitidas

`DO-CHECK-001` puede recibir:

- un archivo Markdown local del repositorio
- un expediente abierto
- un conjunto acotado de archivos locales
- una propuesta de cambio expresada como texto
- un reporte provisional ya registrado

## Entradas no permitidas como autoridad

`DO-CHECK-001` no puede tratar como autoridad:

- registro historico sin decision registrada
- referencias mencionadas pero no materializadas
- hipotesis sin demostracion, auditoria o decision
- salidas de herramienta sin estatus declarado
- deudas conceptuales usadas como fundamento positivo

## Fuentes minimas por ejecucion

Toda ejecucion de `DO-CHECK-001` debe leer o citar:

- `CURRENT_STATE.md`
- `05_Estado_Proyecto/ESTADO_ACTUAL.md`
- `01_Canon/M-000_Reglas_Fundamentales.md`
- `01_Canon/M-001_Auditoria_Arquitectonica.md`
- el archivo o conjunto de archivos objetivo

Si alguna fuente minima no esta disponible, el resultado debe ser `bloqueado` o `escalado`.

## DO_CHECK_REPORT

Estatus: definicion provisional de expediente.

```text
DO_CHECK_REPORT = {
  report_id,
  expediente,
  objetivo,
  modo,
  resultado,
  tipo,
  ubicacion,
  descripcion,
  evidencia,
  estatus_afirmacion,
  fuentes_leidas,
  dependencias,
  referencias_no_materializadas,
  expedientes_cerrados_afectados,
  problemas_abiertos_afectados,
  deudas_generadas,
  recomendacion,
  cambios_propuestos,
  transformacion_permitida
}
```

## Campos

`report_id`: identificador unico dentro de `DO-001`.

`expediente`: expediente que emite el reporte. Valor esperado: `DO-001`.

`objetivo`: archivo, expediente o propuesta revisada.

`modo`: tipo de ejecucion.

Valores permitidos iniciales:

- `lectura`
- `pre_cambio`
- `post_cambio`
- `validacion`

`resultado`: resultado operativo del check.

Valores permitidos iniciales:

- `ok`
- `advertencia`
- `bloqueado`
- `escalado`

`tipo`: clasificacion del hallazgo principal.

Valores permitidos iniciales:

- `sin_hallazgo_bloqueante`
- `deuda_conceptual`
- `dependencia_no_registrada`
- `estatus_ausente`
- `violacion_m000`
- `violacion_m001`
- `historial_como_autoridad`
- `expediente_cerrado_afectado`
- `reporte_incompleto`
- `cambio_no_autorizado`

`ubicacion`: lugar del archivo o propuesta donde aparece el hallazgo.

`descripcion`: explicacion breve del resultado.

`evidencia`: cita breve, referencia local o estructura minima que justifica el resultado.

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

`fuentes_leidas`: fuentes locales leidas para emitir el reporte.

`dependencias`: fuentes, reglas o expedientes usados por el check.

`referencias_no_materializadas`: referencias necesarias que no existen como archivo local o decision registrada.

`expedientes_cerrados_afectados`: expedientes cerrados que la propuesta tocaria o reabriria.

`problemas_abiertos_afectados`: problemas abiertos afectados por la lectura o propuesta.

`deudas_generadas`: deudas conceptuales nuevas o confirmadas.

`recomendacion`: salida operativa.

Valores permitidos iniciales:

- `aprobar_lectura`
- `bloquear`
- `escalar`
- `continuar_sin_transformar`

`cambios_propuestos`: cambios documentales sugeridos, si existen. Debe estar vacio si el reporte no propone cambios.

`transformacion_permitida`: indica si `DO-CHECK-001` permite transformacion ejecutada.

Valor fijo en v0:

- `false`

## Reglas de validez

Un `DO_CHECK_REPORT` es valido si:

- identifica objetivo y modo
- lista fuentes leidas
- clasifica el hallazgo principal
- declara el estatus de la afirmacion afectada
- registra dependencias usadas
- registra referencias no materializadas
- registra expedientes cerrados afectados, si existen
- registra problemas abiertos afectados, si existen
- emite una recomendacion permitida
- conserva `transformacion_permitida = false`

Un `DO_CHECK_REPORT` es invalido si:

- modifica un archivo por si mismo
- promueve una hipotesis a Canon
- usa registro historico como autoridad vigente
- omite fuentes minimas
- omite deudas conceptuales necesarias
- recomienda `continuar_con_cambio_acotado`
- permite `Tr_ejecucion`
- cierra un expediente

## Checks minimos

Estatus: algoritmo provisional de expediente.

```text
1. CHECK-FUENTES
   Verificar que la ejecucion cite fuentes minimas.

2. CHECK-ESTATUS
   Detectar afirmaciones relevantes sin estatus declarado.

3. CHECK-DEPENDENCIAS
   Detectar referencias necesarias no materializadas.

4. CHECK-HISTORIAL
   Detectar uso del Registro Historico como autoridad directa.

5. CHECK-NIVELES
   Detectar intentos de modificar Canon o documentos oficiales desde expedientes sin decision explicita.

6. CHECK-CERRADOS
   Detectar efectos sobre expedientes cerrados.

7. CHECK-REPORTES
   Detectar reportes normalizados incompletos.

8. CHECK-ESTADO
   Distinguir propuesta de actualizacion de estado frente a actualizacion ejecutada.

9. CHECK-ASCII
   Detectar caracteres no ASCII cuando el archivo objetivo mantiene politica ASCII.
```

## Regla de decision

`DO-CHECK-001` debe emitir `bloquear` si detecta:

- uso de Registro Historico como autoridad vigente
- promocion de hipotesis a Canon
- modificacion de Canon sin decision explicita
- intento de cierre automatico de expediente
- `Tr_ejecucion` sin autorizacion previa
- dependencia necesaria no materializada usada como fundamento positivo

`DO-CHECK-001` debe emitir `escalar` si detecta:

- conflicto entre fuentes locales de distinto nivel
- expediente cerrado afectado
- problema abierto afectado sin tratamiento
- regla de permiso insuficiente para ejecutar un cambio

`DO-CHECK-001` puede emitir `continuar_sin_transformar` si detecta:

- deuda conceptual registrable
- estatus ausente que puede anotarse antes de continuar
- reporte incompleto que puede corregirse sin modificar niveles superiores

`DO-CHECK-001` puede emitir `aprobar_lectura` solo si:

- no hay hallazgos bloqueantes
- no hay transformacion ejecutada
- las deudas relevantes estan registradas
- las fuentes minimas fueron leidas

## Relacion con OPERATOR_REPORT

Estatus: regla provisional de expediente actualizada por decision.

Fuente de decision: `03_Expedientes/DO-001_Decision_DO-CHECK-REPORT.md`.

`DO_CHECK_REPORT` no reemplaza `OPERATOR_REPORT`.

`DO_CHECK_REPORT` permanece como reporte propio de `DO-001` porque `AUD-001_Contrato_Reportes.md` no define un operador `DO-CHECK`.

La compatibilidad con `OPERATOR_REPORT` es parcial y conceptual. Permite lectura futura, pero no integracion automatica.

Campos compatibles directamente:

- `report_id`
- `expediente`
- `ubicacion`
- `descripcion`
- `evidencia`
- `estatus_afirmacion`
- `dependencias`
- `deudas_generadas`
- `transformacion_permitida`

Campos compatibles solo parcialmente:

- `objetivo` con `caso`
- `resultado` con `resultado`
- `tipo` con `tipo`
- `fuentes_leidas` con `dependencias`
- `referencias_no_materializadas` con `deudas_generadas`
- `recomendacion` con `decision_permitida`
- `cambios_propuestos` con `alternativas_no_decididas`

Campos sin equivalente directo:

- `modo`
- `expedientes_cerrados_afectados`
- `problemas_abiertos_afectados`

Consecuencia: una integracion futura requiere decision explicita y ampliacion del contrato de `AUD-001`.

## Relacion con D_REPORT

`DO-CHECK-001` puede recomendar `bloquear`, `escalar`, `continuar_sin_transformar` o `aprobar_lectura`.

Esa recomendacion no es una decision arquitectonica.

Un `D_REPORT` posterior podria leer `DO_CHECK_REPORT`, pero `DO_CHECK_REPORT` por si mismo no decide ni autoriza transformacion.

## Prohibiciones

`DO-CHECK-001` aplica `PERMISO-ACT-001` como regla local de permiso. Si una propuesta no identifica autorizacion valida, el resultado debe ser `bloqueado` o `escalado` segun el alcance.

`DO-CHECK-001` no puede:

- escribir en Canon
- modificar documentos oficiales
- modificar expedientes cerrados
- cerrar expedientes
- ejecutar `Tr_ejecucion`
- resolver `R4`
- resolver `Gamma`
- importar historial como autoridad
- actualizar estado sin instruccion humana explicita o decision registrada

## Validacion requerida

Antes de tratar `DO-CHECK-001` como herramienta estable, debe validarse contra al menos tres archivos locales:

- `03_Expedientes/DO-001.md`
- `03_Expedientes/AUD-001_Casos_Prueba_Auditor.md`
- `CURRENT_STATE.md`

Cada validacion debe producir un `DO_CHECK_REPORT` de ejemplo y registrar si el reporte fue suficiente.

Resultado actual: cumplido provisionalmente en `03_Expedientes/DO-001_Validaciones_DO-CHECK-001.md`.

## Criterio de cierre

Esta definicion queda suficientemente estable para la siguiente fase cuando:

- `DO-CHECK-001` este registrado en `DO-001`
- el estado del proyecto registre que `DO-CHECK-001` esta definido provisionalmente
- exista una validacion inicial contra tres archivos locales
- quede decidido si la salida futura se integra a `OPERATOR_REPORT` o permanece como reporte propio de `DO-001`

## Estado actual

`DO-CHECK-001` queda definido provisionalmente, validado inicialmente contra tres archivos locales y asociado a una decision provisional sobre `DO_CHECK_REPORT`.

Decision: `DO_CHECK_REPORT` permanece como reporte propio de `DO-001`, con compatibilidad parcial futura con `OPERATOR_REPORT`.

Regla de permiso: `PERMISO-ACT-001` registrada en `03_Expedientes/DO-001_Regla_Permiso_Actualizacion.md`.

Validacion de permiso: registrada en `03_Expedientes/DO-001_Validaciones_PERMISO-ACT-001.md`.

Decision de modo operativo: `MODO-AUD-001` confirma que `DO-CHECK-001` pertenece a la capa ejecutable no mutante.

Pendiente: definir si alguna parte de `DO-001` pasa a Especificacion Tecnica del Auditor.

