# AO-001 - Matriz de condiciones faltantes AO-PPI-BRIDGE-003

Estatus: matriz local no mutante.

Fecha: 2026-07-06.

ID: `AO-PPI-BRIDGE-003`.

Expediente padre: `AO-001`.

Decision asociada: `D-2026-07-06-018`.

## Proposito

Preparar una matriz de condiciones faltantes para cualquier cierre global futuro de Confluencia y Equivalencia de proyecciones.

La matriz usa `AO-PPI-BRIDGE-002` como evidencia local fuerte, pero no la convierte en cierre global.

Tambien amplia la cobertura de `REPORT_LAYER` con casos heterogeneos no mutantes, manteniendolo como capa local pre-C.

## Fuentes

- `AO-001_Puente_Confluencia_Equivalencia_002.md`.
- `AO-001_Decision_Puente_Confluencia_Equivalencia_002.md`.
- `AO-001_Pruebas_AO-DOC04-WIDE_REPORT_LAYER.md`.
- `AO-001_Relacion_REPORT_LAYER_Doc04_Amplio.md`.
- `AO-001_Justificacion_REPORT_LAYER_Nivel_C.md`.
- `AUT-003_Herramienta_REPORT_LAYER_C002.md`.
- `06_Automatizacion/ao_ppi_bridge_003.py`.
- `06_Automatizacion/fixtures/ao_ppi_bridge_003_matrix.json`.
- `06_Automatizacion/reportes/ao_ppi_bridge_003_report.md`.

## Criterio de matriz

Una condicion queda como `satisfecha_local` si:

- tiene evidencia local aceptada;
- conserva testigo o criterio operacional visible;
- no aumenta autoridad;
- no oculta deuda;
- no autoriza transformacion;
- no reabre frentes cerrados.

Una condicion queda como `faltante_global` si:

- hace falta para un cierre global;
- no esta demostrada por la evidencia local;
- exige contrato, protocolo, cobertura externa o criterio de autoridad aun no disponible.

Una condicion queda como `bloqueada_por_alcance` si:

- requeriria reabrir frentes cerrados;
- requeriria exportar operadores bloqueados;
- requeriria promocion de `REPORT_LAYER`, R4/Gamma, Nivel C o Canon.

## Matriz de condiciones

| ID | Dominio | Estado | Lectura |
| --- | --- | --- | --- |
| `AO-PPI-GC-001` | equivalencia | `satisfecha_local` | `AO-PPI-BRIDGE-002` aporta evidencia fuerte local entre `Pi_doc`, `Pi_rep` y `Pi_op`. |
| `AO-PPI-GC-002` | confluencia | `satisfecha_local` | Hay convergencia local entre ruta de estado, ruta de decision y ruta de reporte. |
| `AO-PPI-GC-003` | `REPORT_LAYER` | `satisfecha_local` | Los casos heterogeneos locales amplian cobertura sin promocion ni modo mutante. |
| `AO-PPI-GC-004` | `REPORT_LAYER` | `faltante_global` | Falta serializacion interfrente exportable con versionado y mapa de campos. |
| `AO-PPI-GC-005` | autoridad | `faltante_global` | Falta criterio general de comparabilidad entre expediente, documento, Nivel C y Canon. |
| `AO-PPI-GC-006` | dominios | `faltante_global` | Falta cobertura externa amplia e independiente del diseno interno de `AO-001`. |
| `AO-PPI-GC-007` | `TCS-001` | `faltante_global` | Falta relacion `AO/TCS` para clasificar fallos globales de concordancia. |
| `AO-PPI-GC-008` | alcance | `bloqueada_por_alcance` | `P-PI.0` y `P-PI.1` permanecen cerrados como frentes. |
| `AO-PPI-GC-009` | exportacion | `bloqueada_por_alcance` | R4/Gamma y `REPORT_LAYER` tienen exportacion o promocion bloqueada por decisiones vigentes. |
| `AO-PPI-GC-010` | reproducibilidad | `faltante_global` | Falta protocolo AO especifico para evaluadores independientes. |

## Casos heterogeneos de REPORT_LAYER

| Caso | Salida esperada | Funcion |
| --- | --- | --- |
| `RL-HET-001` | `compatible_heterogeneo_no_mutante` | Reporte documental AO con `Pi_rep` local. |
| `RL-HET-002` | `compatible_heterogeneo_no_mutante` | Reporte automatizado de riesgo con deuda documental visible. |
| `RL-HET-003` | `compatible_heterogeneo_no_mutante` | Reporte tabular `R001-TB-001` como evidencia auxiliar. |
| `RL-HET-004` | `compatible_heterogeneo_no_mutante` | Reporte `MOC/AO` con `operator_trace` como evidencia local. |
| `RL-HET-005` | `divergencia_clasificada` | Fuente externa sintetica diverge y se clasifica sin ocultarla. |
| `RL-HET-006` | `bloqueo_testigo` | Reporte sin testigo suficiente. |
| `RL-HET-007` | `bloqueo_recomendacion_como_decision` | Recomendacion convertida indebidamente en decision. |
| `RL-HET-008` | `bloqueo_autoridad` | Intento de elevar `REPORT_LAYER` a Nivel C. |
| `RL-HET-009` | `bloqueo_modo_mutante` | Intento de habilitar transformacion material. |

## Resultado automatizado

La herramienta `AO-PPI-BRIDGE-003` produce:

```text
resultado: ok
recomendacion: mantener_cierre_global_no_autorizado
global_closure_authorized: false
conditions: 10
local_satisfied: 3
missing_or_blocking: 10
report_layer_cases: 9
report_layer_passed: 9
report_layer_failed: 0
```

## Lectura operacional

La matriz no intenta demostrar Confluencia global ni Equivalencia global.

Su funcion es mas estrecha:

- convertir `AO-PPI-BRIDGE-002` en evidencia local fuerte;
- separar lo satisfecho localmente de lo que falta globalmente;
- hacer visible que todo cierre global sigue bloqueado por condiciones abiertas;
- ampliar `REPORT_LAYER` con casos heterogeneos sin promoverlo.

## Guardas

La matriz conserva estas fronteras:

- Documento 04: sin cambios.
- Canon: sin cambios.
- Nivel C: sin alta nueva.
- `P-PI.0` y `P-PI.1`: cerrados como frentes.
- Confluencia global: abierta.
- Equivalencia global: abierta.
- `REPORT_LAYER`: local pre-C.
- R4/Gamma: sin exportacion general.
- Transformaciones materiales: no autorizadas.

## Deudas abiertas

- Cierre global de Confluencia.
- Cierre global de Equivalencia de proyecciones.
- Serializacion interfrente exportable de `REPORT_LAYER`, si se decide abrirla.
- Criterio general de autoridad entre niveles.
- Cobertura externa amplia e independiente.
- Relacion `AO/TCS` para fallos globales de concordancia.
- Protocolo AO reproducible para evaluadores independientes.

## Dictamen

`AO-PPI-BRIDGE-003` queda preparado como matriz local no mutante.

La evidencia local se fortalece, pero el cierre global permanece no autorizado.
