# MOC-AO-GEO-BRIDGE-001 - Puente AO por operator_trace

Estatus: aceptado como puente local provisional no canonico.

Fecha: 2026-07-09.

Expediente: `MOC-001`.

Decision asociada: `D-2026-07-09-001`.

## Proposito

`MOC-AO-GEO-BRIDGE-001` define como una salida geometrica local del MOC puede usarse como evidencia auxiliar para `AO-001` sin convertirse en permiso de transformacion ni cierre global.

El puente se hace exclusivamente mediante `operator_trace`.

## Esquema minimo de traza

```text
operator_trace = {
  operator_id,
  case_id,
  output,
  rule_id,
  priority,
  metric_vector,
  graph_validation,
  source_evidence,
  blockers,
  warnings
}
```

Operador:

```text
OP_MOC_GEO_GRAPH
```

## Reglas de puente AO

| `R_geo` | Rol AO local |
| --- | --- |
| `concordancia_local` | `evidencia_auxiliar_equivalencia_local` |
| `reorganizacion_local_habilitada` | `evidencia_auxiliar_con_deuda` |
| `friccion_relevante` | `evidencia_friccion_confluencia_local` |
| `friccion_desorganizante` | `bloqueo_transitabilidad_sin_uso_positivo` |
| `discordancia_local` | `deuda_local_direccion_no_cierre` |
| `disolucion_local` | `bloqueo_comparabilidad_sin_uso_positivo` |
| `fuera_de_alcance` | `bloqueo_alcance_sin_uso_positivo` |
| `indeterminado_por_falta_de_evidencia` | `bloqueo_evidencia_sin_uso_positivo` |

## Flags protegidos

Toda traza producida por este puente conserva:

```text
transformacion_permitida: false
global_closure_authorized: false
global_export_authorized: false
global_equivalence_authorized: false
global_confluence_authorized: false
report_layer_promoted: false
r4_gamma_global_export_authorized: false
modifies_doc04: false
modifies_canon: false
modifies_nivel_c: false
```

## Uso permitido

El puente puede:

- aportar evidencia auxiliar a discusiones locales `MOC/AO`;
- explicar que regla geometrica gano en cada caso;
- mostrar por que una salida se bloquea o queda como deuda;
- alimentar reportes no mutantes.

El puente no puede:

- modificar Documento 04;
- promover `REPORT_LAYER`;
- exportar R4/Gamma;
- cerrar Equivalencia global;
- cerrar Confluencia global;
- convertir una salida MOC en decision AO.

## Criterio de aceptacion

La ruta queda aceptada solo si una herramienta no mutante valida los casos 036-043 y demuestra que cada salida queda traducida a `operator_trace` sin activar permisos globales.

