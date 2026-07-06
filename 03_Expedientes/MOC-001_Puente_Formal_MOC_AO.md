# MOC-001 - Puente formal MOC/AO

ID: `MOC-AO-BRIDGE-001`.

Ruta: `MOC-ROUTE-004`.

Fecha: 2026-07-05.

Estatus: formalizacion local provisional.

Decision asociada: `D-2026-07-05-022`.

## Proposito

Relacionar `MOC-001` con `AO-001` usando `operator_trace` como evidencia local de regla ganadora.

El puente no convierte MOC en autoridad operacional ni modifica `Documento 04`. Solo define cuando una traza MOC puede servir como testigo auxiliar para equivalencia local, confluencia local, friccion local o deuda global abierta.

## Antecedentes

- `MOC-TCS-BRIDGE-001`: formaliza `OP_MOC_XI`, `OP_MOC_TCS`, `OP_MOC_STATE` y `OP_MOC_AGREEMENT`.
- `AO-PPI-BRIDGE-001`: define `AO-PPI-EQ-001` y `AO-PPI-CONF-001` como avances locales de Equivalencia y Confluencia.
- `R001-TB-001`: instancia tabular local de proyeccion operacional.
- `AO-DOC04-FORM-001`: incorporacion acotada de `Pi_tb` / `Eq_tb` al Documento 04 bajo testigo.

## Entrada del puente

La entrada minima es:

```text
operator_trace = {
  xi.rule_id,
  tcs.rule_id,
  state.rule_id,
  actual_xi,
  actual_moc,
  agreement,
  debt
}
```

`operator_trace` es evidencia local porque conserva:

- regla ganadora de `OP_MOC_XI`;
- regla ganadora de `OP_MOC_TCS`;
- regla ganadora de `OP_MOC_STATE`;
- familia de salida;
- deuda asociada.

## Proyeccion Pi_moc_trace

Forma:

```text
Pi_moc_trace(C) = {
  case_id,
  xi_rule,
  tcs_rule,
  state_rule,
  state_family
}
```

La proyeccion es local y no canonica. Su funcion es permitir que `AO-001` compare trazas MOC sin releer semanticamente cada caso.

## Relacion con AO-PPI-EQ-001

`Pi_moc_trace` puede operar como evidencia auxiliar para equivalencia local si:

- conserva `case_id`;
- conserva regla ganadora `Xi`;
- conserva regla ganadora `TCS`;
- conserva regla ganadora de estado MOC;
- conserva familia de salida;
- declara deuda y no la oculta.

Salida permitida:

```text
evidencia_auxiliar_equivalencia_local
```

Solo aplica para `concordancia_local` y `concordancia_parcial`.

No demuestra Equivalencia global de proyecciones.

## Relacion con AO-PPI-CONF-001

`Pi_moc_trace` puede operar como evidencia auxiliar para confluencia local si:

- la traza no aumenta autoridad;
- la salida conserva familia MOC;
- la deuda permanece visible;
- el puente no convierte salida MOC en permiso de transformacion.

Salidas permitidas:

- `evidencia_auxiliar_con_deuda`;
- `evidencia_friccion_confluencia_local`;
- `deuda_global_no_cierre`;
- `bloqueo_seguridad_sin_uso_positivo`;
- `bloqueo_comparabilidad_sin_uso_positivo`.

No demuestra Confluencia global.

## Tabla de roles AO

| Estado MOC | Rol AO local | Uso permitido |
| --- | --- | --- |
| `concordancia_local` | `evidencia_auxiliar_equivalencia_local` | apoyo local para equivalencia y confluencia |
| `concordancia_parcial` | `evidencia_auxiliar_con_deuda` | apoyo local con deuda visible |
| `friccion_operativa` | `evidencia_friccion_confluencia_local` | caso de friccion local para criterio de confluencia |
| `discordancia_global` | `deuda_global_no_cierre` | evidencia de problema global abierto |
| `bloqueo_de_concordancia` | `bloqueo_seguridad_sin_uso_positivo` | bloqueo; no evidencia positiva |
| `no_comparable` | `bloqueo_comparabilidad_sin_uso_positivo` | comparacion detenida; no evidencia positiva |

## Invariantes

- `MOC-AO-BRIDGE-001` no modifica `Documento 04`.
- No crea nuevos operadores oficiales de Algebra Operacional.
- No promueve MOC a Canon, Nivel C ni documento oficial.
- No convierte `operator_trace` en permiso de transformacion.
- No cierra Confluencia global.
- No cierra Equivalencia global.
- No exporta R4/Gamma.
- No admite `H-Xi` ni canoniza `Xi`.

## Implementacion local

`06_Automatizacion/moc_eval.py` agrega `ao_bridge` a cada resultado.

Campos principales:

- `bridge_id`: `MOC-AO-BRIDGE-001`;
- `witness_id`: combinacion de `case_id` y `state_rule`;
- `pi_moc_trace`: proyeccion local desde `operator_trace`;
- `ao_role`: rol AO local;
- `can_support_equivalence_local`;
- `can_support_confluence_local`;
- `closes_equivalence_global: false`;
- `closes_confluence_global: false`;
- `modifies_doc04: false`;
- `transformacion_permitida: false`.

## Casos guia

- `MOC-CASE-002`: `concordancia_local` produce `evidencia_auxiliar_equivalencia_local`.
- `MOC-CASE-003`: `friccion_operativa` produce `evidencia_friccion_confluencia_local`.
- `MOC-CASE-005`: `bloqueo_de_concordancia` produce `bloqueo_seguridad_sin_uso_positivo`.
- `MOC-CASE-006`: `discordancia_global` produce `deuda_global_no_cierre`.
- `MOC-CASE-009`: conserva `TCS-R2-EJE-SECUNDARIO-FALTANTE` como deuda secundaria visible.

## No cubre

No valida empiricamente el MOC, no evalua personas reales, no abre uso clinico, no admite `H-Xi`, no canoniza `Xi`, no crea Nivel C, no modifica `Documento 04`, no cierra Confluencia global, no cierra Equivalencia global, no formaliza una semantica general de proyecciones y no autoriza transformaciones materiales.

## Deudas abiertas

- semantica general de proyecciones fuera de casos locales;
- refinamiento posterior del protocolo de evaluadores;
- piloto empirico futuro no ejecutado;
- relacion futura con `C-001` / `C-002`;
- Confluencia global;
- Equivalencia global de proyecciones;
- maduracion posterior de `TCS-001`.
