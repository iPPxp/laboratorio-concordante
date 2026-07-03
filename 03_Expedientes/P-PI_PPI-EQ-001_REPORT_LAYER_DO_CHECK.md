# P-PI - PPI-EQ-001 REPORT_LAYER / DO_CHECK_REPORT

Estatus: caso ejecutado provisional.

ID: `PPI-EQ-001`.

Fecha: 2026-07-03.

Expediente padre: `P-PI.0`.

Marco asociado: `PPI-MARCO-CORE-001`.

## Pregunta

La proyeccion de un `DO_CHECK_REPORT` hacia `REPORT_ITEM` conserva los observables suficientes para tratarla como equivalente a una lectura minima de `REPORT_LAYER`?

Respuesta: si, solo bajo contexto de lectura no mutante minima.

## Fuentes

- `03_Expedientes/P-PI_Marco_Inicial_Confluencia_Equivalencia.md`
- `03_Expedientes/AUD-001_Compatibilidad_REPORT_LAYER_DO_CHECK.md`
- `03_Expedientes/AUD-001_Ficha_Alcance_REPORT_LAYER_Pre-C.md`
- `06_Automatizacion/auditor_do_check_adapter.py`
- `06_Automatizacion/reportes/do_check_med_repo.json`
- `06_Automatizacion/test_auditor_do_check_adapter.py`

## Estado fuente

Estado fuente `S`:

```text
S = DO-CHECK-MED-LIVE-20260702-165850
```

Propiedades observadas del estado fuente:

- `algoritmo = DO-CHECK-MED-001`
- `resultado = ok`
- `recomendacion = aprobar_lectura`
- `transformacion_permitida = false`
- `findings = 0`
- `scope = claves`

## Proyecciones comparadas

### pi_do

`pi_do(S)` lee el `DO_CHECK_REPORT` como reporte documental no mutante.

Observables conservados:

- resultado de lectura;
- recomendacion;
- ausencia de permiso de transformacion;
- ausencia de hallazgos;
- identificador fuente.

### pi_rl

`pi_rl(S)` aplica `AUDITOR-DO-CHECK-ADAPTER-001` y proyecta el reporte hacia `REPORT_ITEM`.

Resultado observado:

```text
fuente_report_id = DO-CHECK-MED-LIVE-20260702-165850
operador_abstracto = calculo
clase_reporte = sin_hallazgo_bloqueante
resultado = ok
decisiones_permitidas = [aprobar_lectura, continuar_sin_transformar]
decision_emitida = no_aplica
transformacion_permitida = false
deudas_generadas = []
adapter_errors = []
conforme_c002 = true
```

## Contexto C

Se declara el contexto:

```text
C_AUD_LECTURA_MIN
```

Este contexto solo exige preservar observables de lectura no mutante:

- resultado no bloqueante;
- recomendacion conservada como recomendacion;
- decision no emitida por el adaptador;
- permiso de transformacion conservado como falso;
- ausencia de hallazgos no convertida en deuda;
- identificador fuente conservado;
- ausencia de absorcion contractual de `DO_CHECK_REPORT`.

No exige equivalencia textual, equivalencia semantica completa ni trazabilidad exhaustiva de `scope`, `targets` o `estado_aau_local`.

## Comparacion

| Observable | pi_do | pi_rl | Resultado |
| --- | --- | --- | --- |
| Identificador fuente | `DO-CHECK-MED-LIVE-20260702-165850` | `fuente_report_id` conservado | pasa |
| Resultado | `ok` | `ok` | pasa |
| Recomendacion | `aprobar_lectura` | `decisiones_permitidas` incluye `aprobar_lectura` | pasa |
| Decision emitida | no aplica en fuente | `no_aplica` | pasa |
| Transformacion | `false` | `false` | pasa |
| Hallazgos | `0` | `sin_hallazgo_bloqueante` | pasa |
| Deudas | ninguna generada por hallazgos | `[]` | pasa |
| Contrato | `DO_CHECK_REPORT` propio | `REPORT_ITEM` derivado | pasa con frontera |

## Dictamen

Bajo `C_AUD_LECTURA_MIN`:

```text
pi_do(S) ~_C pi_rl(S)
```

La equivalencia es local, contextual y no mutante.

No afirma que `DO_CHECK_REPORT` sea `REPORT_LAYER`.

No afirma que `REPORT_ITEM` sustituya `OPERATOR_REPORT`.

No habilita transformacion, decision, cierre de expediente ni promocion de `REPORT_LAYER`.

## Contexto mas fuerte

Si el contexto exigiera trazabilidad completa:

```text
C_AUD_TRAZABILIDAD_COMPLETA
```

la equivalencia no queda demostrada, porque el adaptador actual no preserva como observables principales:

- `scope`;
- `targets`;
- `estado_aau_local`;
- campos propios de `DO_CHECK_REPORT` sin traslado directo.

En ese contexto, el dictamen responsable seria bloqueo o equivalencia no demostrada.

## Deudas conservadas

- `PPI-CONF-001` queda cumplido por `P-PI_PPI-CONF-001_Rutas_Estado_Operativo.md`; los tres casos siguen siendo locales y provisionales.
- Definir si futuros contextos requieren propiedades formales de `~_C`.
- Si se busca equivalencia fuerte de trazabilidad, ampliar el adaptador o declarar un contexto mas estricto.
- Mantener `REPORT_LAYER` local pre-C hasta decision separada.

## Veredicto

`PPI-EQ-001` pasa como equivalencia de proyecciones minima.

No cierra Equivalencia de proyecciones como problema general.

Queda usado junto con `PPI-EQ-002` como insumo local de `PPI-CONF-001`.
