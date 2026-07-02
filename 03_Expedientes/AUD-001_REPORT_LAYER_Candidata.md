# AUD-001 - REPORT_LAYER Candidata

Estatus: especificacion candidata provisional de expediente.

Identificador: `REPORT-LAYER-CAND-001`.

Expediente padre: `AUD-001`.

Decision de reactivacion: `03_Expedientes/AUD-001_Decision_Reactivacion_REPORT_LAYER.md`.

Auditoria asociada: `03_Expedientes/AUD-001_Auditoria_REPORT_LAYER_Candidata.md`.

Decision de estatus asociada: `03_Expedientes/AUD-001_Decision_Estatus_REPORT_LAYER_Candidata.md`.

Mapa de origen asociado: `03_Expedientes/AUD-001_Origen_REPORT_LAYER.md`.

Decision de alcance asociada: `03_Expedientes/AUD-001_Decision_Alcance_REPORT_LAYER.md`.

Compatibilidad asociada: `03_Expedientes/AUD-001_Compatibilidad_REPORT_LAYER_DO_CHECK.md`.

## Proposito

Definir una forma abstracta minima para la capa de reportes que `R4-CANDIDATA` necesita cuando deja de hablar solo de los reportes locales de `AUD-001`.

Esta candidata no es Canon, no es documento oficial, no modifica `C-001` y no promueve `R4-CANDIDATA`.

Su funcion es separar dos cosas:

- los nombres locales ya validados en `AUD-001`;
- la estructura abstracta que una regla procedimental podria exigir en otros objetos auditables.

## Fuentes locales

- `01_Canon/M-000_Reglas_Fundamentales.md`
- `01_Canon/M-001_Auditoria_Arquitectonica.md`
- `02_Documentos/C-001_Especificacion_Tecnica_Auditor.md`
- `03_Expedientes/AUD-001_Contrato_Reportes.md`
- `03_Expedientes/AUD-001_Validaciones.md`
- `03_Expedientes/AUD-001_R4-CANDIDATA.md`
- `03_Expedientes/AUD-001_Criterios_Promocion_R4-CANDIDATA.md`
- `03_Expedientes/AUD-001_Decision_Reactivacion_REPORT_LAYER.md`
- `03_Expedientes/AUD-001_Origen_REPORT_LAYER.md`

## Origen interno de la abstraccion

`REPORT_LAYER` no se toma de una fuente externa ni del Registro Historico.

Se extrae dentro del Laboratorio por proyeccion desde:

- `M-000` y `M-001`, que fijan estatus, trazabilidad, deuda, auditoria y autoridad;
- `C-001`, que fija el alcance tecnico oficial del Auditor;
- `AUD-001_Contrato_Reportes.md`, que contiene la gramatica concreta de reportes;
- `AUD-001_Validaciones.md` y `AUD-001_Simulaciones.md`, que muestran que la cadena opera tambien fuera de automatas;
- `DO-001_DO-CHECK-001.md`, `DO-001_Regla_Permiso_Actualizacion.md` y `DO-001_Decision_Modo_Operativo_Auditor.md`, que separan reporte, recomendacion, permiso y ejecucion.

Mapa de extraccion: `AUD-001_Origen_REPORT_LAYER.md`.

## Definicion candidata

`REPORT_LAYER` es una coleccion ordenada de reportes normalizados que permite auditar la cadena:

```text
mapeo -> calculo/verificacion -> terminacion -> decision -> propuesta o ejecucion -> verificacion posterior
```

Una capa de reportes es valida para `R4-CANDIDATA` solo si permite determinar:

- que se leyo;
- que operador o funcion reporto;
- que resultado obtuvo;
- que evidencia sostiene el resultado;
- que decisiones quedan permitidas;
- que decisiones fueron emitidas;
- si existe o no permiso de transformacion;
- que dependencias y deudas quedan abiertas.

## Unidad minima

La unidad minima de `REPORT_LAYER` es `REPORT_ITEM`.

```text
REPORT_ITEM = {
  report_id,
  objeto,
  operador_abstracto,
  clase_reporte,
  resultado,
  tipo_hallazgo,
  ubicacion,
  descripcion,
  evidencia,
  estatus_afirmacion,
  decisiones_permitidas,
  decision_emitida,
  transformacion_permitida,
  terminacion_requerida,
  terminacion_observada,
  dependencias,
  deudas_generadas
}
```

## Operadores abstractos

`operador_abstracto` puede tomar estos valores iniciales:

- `mapeo`
- `calculo`
- `terminacion`
- `decision`
- `transformacion`
- `politica_post_fallo`

Estos operadores son equivalentes funcionales de `Mp`, `Cr`, `tau`, `D`, `Tr` y decision posterior al fallo, pero no obligan a exportar esos nombres fuera de `AUD-001`.

## Clases de reporte

`clase_reporte` puede tomar estos valores iniciales:

- `mapeo_falla`
- `calculo_falla`
- `terminacion`
- `decision`
- `propuesta_transformacion`
- `ejecucion_transformacion`
- `fallo_ejecucion`
- `politica_posterior_fallo`
- `sin_hallazgo_bloqueante`

## Compatibilidad con reportes locales de AUD-001

| Reporte local | Clase abstracta | Operador abstracto |
| --- | --- | --- |
| `MP_FAIL_REPORT` | `mapeo_falla` | `mapeo` |
| `CR_FAIL_REPORT` | `calculo_falla` | `calculo` |
| `TAU_REPORT` | `terminacion` | `terminacion` |
| `D_REPORT` | `decision` | `decision` |
| `TR_PROPOSAL_REPORT` | `propuesta_transformacion` | `transformacion` |
| `TR_EXECUTION_REPORT` | `ejecucion_transformacion` | `transformacion` |
| `TR_EXECUTION_FAIL_REPORT` | `fallo_ejecucion` | `transformacion` |
| `REVERSAL_REPORT` | `politica_posterior_fallo` | `politica_post_fallo` |
| `OPERATOR_REPORT` | superestructura compatible | segun operador |

Esta tabla no convierte los reportes locales en Canon. Solo declara una equivalencia funcional provisional dentro de `AUD-001`.

## Reglas minimas

### 1. Monotonia de permisos

Una decision no puede emitir una salida mas permisiva que los reportes leidos.

Si los reportes previos bloquean transformacion, `REPORT_LAYER` debe conservar `transformacion_permitida = false`.

### 2. Terminacion segura

Si `terminacion_observada` no es `exito`, la capa solo puede habilitar:

- bloquear;
- escalar;
- continuar sin transformar;
- registrar propuesta no ejecutada.

No puede habilitar ejecucion material.

### 3. Decision explicita antes de ejecucion

`ejecucion_transformacion` solo puede aparecer si antes existe un `REPORT_ITEM` de clase `decision` con:

```text
decision_emitida = continuar_con_cambio_acotado
transformacion_permitida = true
```

Ademas, el cambio autorizado debe estar identificado de forma acotada.

### 4. Evidencia antes y despues

Toda `ejecucion_transformacion` debe incluir en `evidencia`:

- estado previo;
- cambio autorizado;
- cambio aplicado;
- estado posterior;
- verificacion posterior.

Si falta una de estas piezas, el resultado no puede registrarse como ejecucion valida.

### 5. Fallo no autoriza recuperacion automatica

Un `fallo_ejecucion` no permite reintento ni reversion por si mismo.

La recuperacion posterior requiere `politica_posterior_fallo`, nueva decision o permiso operativo adicional.

### 6. Deuda no opera como fundamento positivo

Una dependencia ausente o una deuda conceptual puede bloquear, escalar o motivar una propuesta.

No puede usarse como fundamento positivo para ejecutar transformaciones.

### 7. Historial no opera como autoridad directa

Si la evidencia proviene de Registro Historico, la capa debe clasificarla como traza o pista.

No puede usarla como autoridad vigente sin decision, documento o expediente actual que la incorpore.

## Relacion con R4-CANDIDATA

`R4-CANDIDATA` puede referirse a `REPORT_LAYER` cuando necesita hablar de reportes equivalentes fuera de los nombres locales de `AUD-001`.

La relacion minima es:

```text
transformar requiere decision fundada;
decision fundada requiere REPORT_LAYER;
REPORT_LAYER requiere evidencia, estatus, permisos y terminacion;
ejecucion requiere evidencia previa, posterior y verificacion.
```

Esta relacion no convierte `R4-CANDIDATA` en Regla R4 formal.

## Condiciones de validez

Una instancia de `REPORT_LAYER` es valida si:

- contiene al menos un `REPORT_ITEM`;
- cada `REPORT_ITEM` declara estatus de afirmacion;
- las decisiones permitidas estan trazadas a reportes previos;
- ninguna decision aumenta permisos sin fundamento;
- toda transformacion ejecutada tiene decision previa y evidencia posterior;
- toda deuda generada queda registrada antes de ser usada;
- la capa permite bloquear o escalar sin ejecutar cambios.

Una instancia es invalida si:

- omite evidencia relevante;
- oculta falla como exito;
- trata propuesta como ejecucion;
- trata decision como transformacion material;
- usa historial como autoridad directa;
- borra deudas para habilitar cambio.

## Fuera de alcance

Esta candidata no cubre:

- formato JSON, YAML o serializacion ejecutable definitiva;
- esquema oficial de Nivel C;
- implementacion completa del Auditor;
- reversion materializada;
- cuarentena materializada;
- definicion formal de R4;
- construccion formal de `Gamma`.

## Deudas antes de estatus superior

Antes de cualquier promocion fuera de `AUD-001`, falta:

- auditar esta candidata contra `M-000` y `M-001`;
- decidir si `REPORT_LAYER` permanece local o se prepara como Nivel C;
- probar al menos una instancia no reducida a nombres locales de `AUD-001`, o declarar explicitamente que sigue siendo capa local. Cumplido provisionalmente como origen interno por `AUD-SIM-022` y `VAL-022`; queda pendiente decidir alcance;
- definir serializacion si se busca herramienta ejecutable;
- decidir relacion con `C-001` antes de modificar documentos oficiales.

## Veredicto de redaccion

`REPORT_LAYER-CAND-001` queda redactada como candidata provisional de expediente.

No queda aprobada como especificacion oficial.

## Siguiente paso recomendado

Objetivo cumplido posteriormente por `AUD-001_Auditoria_REPORT_LAYER_Candidata.md` y `AUD-001_Decision_Estatus_REPORT_LAYER_Candidata.md`.

Siguiente paso vigente: decidir si se requiere una validacion teorica del puente `REPORT_LAYER` / `DO_CHECK_REPORT` o si basta conservarlo como frontera conceptual.
