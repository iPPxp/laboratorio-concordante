# MOC-001 - Protocolo de evaluacion v0.2

ID: `MOC-EVAL-PROTO-002`.

Ruta: `MOC-ROUTE-005`.

Fecha: 2026-07-05.

Estatus: refinamiento provisional no canonico.

Decision asociada: `D-2026-07-05-024`.

## Proposito

Refinar `MOC-EVAL-PROTO-001` para que el protocolo de evaluadores use `operator_trace`, `Pi_moc_trace` y `ao_bridge` como evidencia local de desempate, desacuerdo justificado y trazabilidad de regla ganadora.

El refinamiento no sustituye a los evaluadores ni borra desacuerdos. Solo agrega una capa comun para explicar por que la salida local reportable queda asociada a una regla ganadora y a un rol AO acotado.

## Entrada adicional

Ademas de la plantilla v0.1, cada evaluador o auditor recibe:

```text
operator_trace:
  xi.rule_id
  tcs.rule_id
  state.rule_id
Pi_moc_trace:
  case_id
  xi_rule
  tcs_rule
  state_rule
  state_family
ao_bridge:
  witness_id
  ao_role
  can_support_equivalence_local
  can_support_confluence_local
```

## Salida adicional

El protocolo v0.2 agrega por caso:

- `status`: estado protocolar de la revision.
- `disagreement_axes`: ejes que explican la diferencia entre evaluadores.
- `tie_breaker_rule`: regla de estado usada como desempate local.
- `trace_witness`: testigo local de la traza.
- `ao_role`: rol local dentro de AO.
- `treatment`: tratamiento protocolar.
- `review_required`: si el caso requiere micro-revision si el patron se repite.

## Ejes de desacuerdo

Los ejes permitidos son:

- `sin_desacuerdo`: los evaluadores coinciden plenamente.
- `regla_xi`: discrepan en salida `Xi`.
- `estado_moc`: discrepan en estado MOC puntual.
- `familia_moc`: discrepan entre familias de estado.
- `regla_tcs`: hay deuda TCS visible que afecta la lectura.
- `rol_ao`: el rol AO local ayuda a clasificar el desacuerdo.

## Tratamientos

El protocolo permite cuatro tratamientos:

| Estado protocolar | Tratamiento | Alcance |
| --- | --- | --- |
| `resuelto` | `aceptar_salida_local` | coincidencia exacta sin bloqueo |
| `resuelto_con_deuda` | `aceptar_operator_trace_con_deuda_visible` | coincidencia parcial con deuda registrada |
| `resuelto_por_bloqueo` | `aceptar_bloqueo_sin_uso_positivo` | bloqueo o no comparabilidad sin evidencia positiva |
| `revision_si_repite` | `mantener_desacuerdo_justificado_y_abrir_micro_revision_si_repite` | desacuerdo entre familias o reglas |

## Regla de desempate local

La regla de desempate local es:

```text
tie_breaker_rule = operator_trace.state.rule_id
```

Esta regla no anula votos de evaluadores. Solo fija la salida local reportable de `MOC-EVAL-001` y obliga a conservar el desacuerdo como deuda si los evaluadores no convergen.

## Regla de desacuerdo repetido

Si `review_required: true` aparece repetidamente con el mismo eje, la accion valida es abrir una micro-revision de regla dentro de `MOC-001`.

La micro-revision no modifica Canon, no modifica `Documento 04`, no cierra Confluencia global, no cierra Equivalencia global y no habilita estudio empirico real.

## Implementacion local

`06_Automatizacion/moc_eval.py` agrega `protocol_v02` a cada resultado y `protocol_v02_summary` al reporte.

Resumen de la corrida local:

- casos: 11;
- aprobados: 11;
- fallos: 0;
- coincidencia exacta: 6;
- coincidencia parcial: 3;
- desacuerdo justificado: 2;
- `review_required`: 2;
- `blocked_positive_use`: 2.

## Restricciones

- No es estudio empirico real.
- No evalua personas reales.
- No abre uso clinico, patologico, juridico, financiero o institucional regulado.
- No canoniza `Xi`.
- No admite `H-Xi`.
- No convierte `operator_trace` en autoridad canonica.
- No modifica `Documento 04`.
- No cierra Confluencia global.
- No cierra Equivalencia global.

## Deudas abiertas

- micro-revision futura si se repiten ejes de desacuerdo;
- preparacion documental de piloto empirico no ejecutado;
- relacion futura con `C-001` / `C-002`;
- Confluencia global;
- Equivalencia global de proyecciones;
- maduracion posterior de `TCS-001`.
