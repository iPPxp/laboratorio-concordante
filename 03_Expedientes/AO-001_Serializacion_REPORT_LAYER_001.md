# AO-001 - Serializacion interfrente de REPORT_LAYER

Estatus: serializacion local no mutante.

Fecha: 2026-07-06.

ID: `AO-REPORT-SERIAL-001`.

Expediente padre: `AO-001`.

Decision asociada: `D-2026-07-06-019`.

## Proposito

Preparar una serializacion local de `REPORT_LAYER` que permita comparar reportes de frentes distintos sin convertir la capa en Nivel C, sin darle autoridad global y sin autorizar transformaciones.

La ruta atiende localmente la condicion `AO-PPI-GC-004` detectada por `AO-PPI-BRIDGE-003`.

## Fuentes

- `AO-001_Matriz_Condiciones_Cierre_Global_003.md`.
- `AO-001_Relacion_REPORT_LAYER_Doc04_Amplio.md`.
- `AO-001_Justificacion_REPORT_LAYER_Nivel_C.md`.
- `AUT-003_Herramienta_REPORT_LAYER_C002.md`.
- `02_Documentos/C-002_RFC_Operativo_Auditor_v0.md`.
- `06_Automatizacion/report_layer_serialization.py`.
- `06_Automatizacion/fixtures/report_layer_serialization_cases.json`.
- `06_Automatizacion/reportes/report_layer_serialization_report.md`.

## Contrato local v0

Un sobre serializado `REPORT-LAYER-SERIAL-v0` debe conservar:

- `serial_id`;
- `schema_id`;
- `schema_version`;
- `origin_front`;
- `source_artifact`;
- `source_family`;
- `projection_target`;
- `witness`;
- `authority_claim`;
- `export_scope`;
- `field_map`;
- `roundtrip_loss`;
- `global_authority_claim`;
- `report_layer`.

El campo `report_layer` conserva el contrato minimo de `C-002`:

- `report_id`;
- `artefacto_revisado`;
- `operador_fase`;
- `resultado`;
- `tipo_hallazgo`;
- `ubicacion`;
- `evidencia`;
- `estatus_afirmacion`;
- `decisiones_permitidas`;
- `decision_emitida`;
- `transformacion_permitida`;
- `dependencias`;
- `deudas_generadas`;
- `recomendacion`.

## Campos protegidos

La serializacion bloquea si una ronda pierde cualquiera de estos campos:

- `report_id`;
- `artefacto_revisado`;
- `resultado`;
- `evidencia`;
- `estatus_afirmacion`;
- `decision_emitida`;
- `transformacion_permitida`;
- `deudas_generadas`;
- `witness`;
- `source_family`;
- `projection_target`;
- `authority_claim`.

## Casos de prueba

| Caso | Salida esperada | Lectura |
| --- | --- | --- |
| `RL-SERIAL-001` | `serializable_interfrente_no_mutante` | Reporte documental AO. |
| `RL-SERIAL-002` | `serializable_interfrente_no_mutante` | Reporte automatizado de riesgo. |
| `RL-SERIAL-003` | `serializable_interfrente_no_mutante` | Reporte tabular `R001-TB-001`. |
| `RL-SERIAL-004` | `serializable_interfrente_no_mutante` | Reporte `MOC/AO` con `operator_trace`. |
| `RL-SERIAL-005` | `serializable_con_divergencia_clasificada` | Reporte externo sintetico divergente. |
| `RL-SERIAL-006` | `bloqueo_testigo` | Ausencia de testigo. |
| `RL-SERIAL-007` | `bloqueo_perdida_campo_protegido` | Perdida de `decision_emitida`. |
| `RL-SERIAL-008` | `bloqueo_autoridad` | Intento de reclamar Nivel C o autoridad global. |
| `RL-SERIAL-009` | `bloqueo_modo_mutante` | Intento de habilitar transformacion material. |
| `RL-SERIAL-010` | `bloqueo_version` | Version futura no aceptada por el contrato local v0. |

## Resultado automatizado

La herramienta `AO-REPORT-SERIAL-001` debe producir:

```text
resultado: ok
recomendacion: mantener_serializacion_local_pre_c
serializacion_interfrente_local: true
global_export_authorized: false
transformacion_permitida: false
```

## Efecto sobre AO-PPI-GC-004

La condicion `AO-PPI-GC-004` deja de ser deuda local total.

Queda leida como:

```text
atendida_localmente_no_global
```

Esto significa:

- existe versionado local;
- existe mapa de campos;
- existe prueba interfrente sintetica;
- existe bloqueo de perdida de campos protegidos;
- existe bloqueo de autoridad y modo mutante;
- no existe contrato global independiente;
- no existe promocion de `REPORT_LAYER`;
- no se autoriza cierre global.

## Guardas

Esta ruta no modifica Documento 04, Canon, `C-001`, `C-002` ni Nivel C.

Tampoco:

- promueve `REPORT_LAYER`;
- exporta `REPORT_LAYER` como autoridad global;
- reabre `P-PI.0` o `P-PI.1`;
- exporta R4/Gamma;
- autoriza transformaciones materiales;
- cierra Confluencia global;
- cierra Equivalencia global.

## Deudas abiertas

- Criterio global de autoridad entre niveles.
- Cobertura externa amplia e independiente.
- Relacion `AO/TCS` para fallos globales de concordancia.
- Protocolo AO reproducible para evaluadores independientes.
- Cierre global de Confluencia.
- Cierre global de Equivalencia de proyecciones.
- Eventual promocion formal de `REPORT_LAYER`, solo si una decision futura abre candidata independiente.

## Dictamen

`AO-REPORT-SERIAL-001` queda preparado como serializacion interfrente local de `REPORT_LAYER`.

La deuda inmediata de serializacion local avanza, pero el cierre global permanece no autorizado.
