# MOC-001 - Puente formal MOC/TCS

ID: `MOC-TCS-BRIDGE-001`.

Ruta: `MOC-ROUTE-003`.

Fecha: 2026-07-05.

Estatus: formalizacion ejecutable local provisional.

Decision asociada: `D-2026-07-05-020`.

## Proposito

Convertir la lectura conceptual de `MOC-001` en operadores locales ejecutables con entradas, prioridad, manejo de conflicto y salida auditable.

Una formula expresiva como:

```text
V + D + E + contexto -> salida_observada
```

sirve para nombrar relacion, pero no basta como operador. No define como se combinan las entradas, que prioridad tienen, que ocurre ante conflicto ni que salida debe producirse.

Este puente fija una semantica operativa minima para `MOC-001` usando `TCS-001` como control de concordancia local.

## Entradas normalizadas

Cada caso se normaliza como:

```text
I_MOC = {
  R0,
  R1,
  Dist(R0,R1),
  Res(R0 -> R1),
  alcance,
  evidencia,
  restricciones,
  ejes_TCS,
  flags
}
```

Las entradas no autorizan transformacion. Solo alimentan operadores de lectura y reporte.

## Operador 1: OP_MOC_XI

Firma:

```text
OP_MOC_XI(I_MOC) -> {salida_Xi, regla, prioridad, conflictos}
```

Salidas permitidas:

- `bloqueado`;
- `no_comparable`;
- `util_acotado`;
- `limitado`;
- `redundante`.

Reglas de prioridad:

| Prioridad | Regla | Condicion | Salida |
| --- | --- | --- | --- |
| 1 | `XI-R1-ALCANCE-EVIDENCIA` | alcance no permitido, evidencia vacia o fuera de alcance | `bloqueado` |
| 2 | `XI-R2-DOMINIO-PROHIBIDO` | persona real, dominio clinico o dominio regulado | `bloqueado` |
| 3 | `XI-R3-UNIDAD-MINIMA` | unidad minima comparable perdida | `no_comparable` |
| 4 | `XI-R4-REORGANIZACION-ESTABLE` | reorganizacion relacional estable con evidencia suficiente | `util_acotado` |
| 5 | `XI-R5-CONFLICTO-SIN-ESTABILIDAD` | restriccion incompatible o conflicto sin estabilidad nueva | `limitado` |
| 6 | `XI-R6-PATRON-REDUNDANTE` | mismo patron relacional o sin aporte sustantivo | `redundante` |
| 7 | `XI-R7-DEFAULT-LIMITADO` | ninguna regla positiva decide el caso | `limitado` |

Regla de conflicto:

La prioridad menor domina. Si una regla de seguridad se activa, no se promedia con una regla positiva posterior.

## Operador 2: OP_MOC_TCS

Firma:

```text
OP_MOC_TCS(ejes_TCS) -> {estado_TCS, regla, prioridad, missing_core, missing_secondary}
```

Ejes nucleares:

- `claim_status`;
- `authority_declared`;
- `decision_present`;
- `permission_scoped`;
- `evidence_traceable`.

Ejes secundarios:

- `automation_bounded`;
- `debt_registered`.

Reglas de prioridad:

| Prioridad | Regla | Condicion | Salida |
| --- | --- | --- | --- |
| 1 | `TCS-R1-EJE-NUCLEAR-FALTANTE` | falta cualquier eje nuclear | `bloqueo_de_concordancia` |
| 2 | `TCS-R2-EJE-SECUNDARIO-FALTANTE` | ejes nucleares pasan y falta eje secundario | `deuda_secundaria` |
| 3 | `TCS-R3-EJES-COMPLETOS` | todos los ejes pasan | `tcs_completo` |

Regla de conflicto:

Un eje nuclear faltante bloquea aunque existan reorganizacion estable o evidencia parcial. Un eje secundario faltante no bloquea por si mismo, pero degrada la salida MOC.

## Operador 3: OP_MOC_STATE

Firma:

```text
OP_MOC_STATE(salida_Xi, estado_TCS, flags) -> {estado_MOC, regla, prioridad}
```

Salidas permitidas:

- `bloqueo_de_concordancia`;
- `no_comparable`;
- `discordancia_global`;
- `friccion_operativa`;
- `concordancia_parcial`;
- `concordancia_local`.

Reglas de prioridad:

| Prioridad | Regla | Condicion | Estado MOC |
| --- | --- | --- | --- |
| 1 | `STATE-R1-BLOQUEO-DOMINANTE` | `salida_Xi = bloqueado` o TCS nuclear faltante | `bloqueo_de_concordancia` |
| 2 | `STATE-R2-NO-COMPARABLE` | `salida_Xi = no_comparable` | `no_comparable` |
| 3 | `STATE-R3-CONFLICTO-GLOBAL` | conflicto global declarado | `discordancia_global` |
| 4 | `STATE-R4-FRICCION-LOCAL` | `salida_Xi = limitado` o conflicto local | `friccion_operativa` |
| 5 | `STATE-R5-CONCORDANCIA-LOCAL` | `salida_Xi` positiva, TCS completo y sin deuda no bloqueante | `concordancia_local` |
| 6 | `STATE-R6-CONCORDANCIA-PARCIAL` | `salida_Xi` positiva con deuda secundaria o deuda no bloqueante | `concordancia_parcial` |
| 7 | `STATE-R7-DEFAULT-FRICCION` | ninguna regla decide el caso | `friccion_operativa` |

Regla de conflicto:

No hay mezcla de estados. El operador emite una salida unica con regla ganadora. La traza conserva reglas anteriores para auditoria, pero no las combina como promedio.

## Operador 4: OP_MOC_AGREEMENT

Firma:

```text
OP_MOC_AGREEMENT(votos_evaluadores) -> {tipo_acuerdo, salidas_Xi, estados_MOC, familias}
```

Reglas:

- Si todos los evaluadores emiten la misma salida `Xi` y el mismo estado MOC: `coincidencia_exacta`.
- Si discrepan en estado puntual pero quedan en la misma familia: `coincidencia_parcial`.
- Si caen en familias distintas con justificacion auditable: `desacuerdo_justificado`.

Familias:

- concordante: `concordancia_local`, `concordancia_parcial`;
- friccion: `friccion_operativa`, `discordancia_global`;
- seguridad: `bloqueo_de_concordancia`, `no_comparable`.

## Casos guia

- `MOC-CASE-006`: `OP_MOC_XI` puede emitir `util_acotado`, pero `OP_MOC_STATE` aplica `STATE-R3-CONFLICTO-GLOBAL`.
- `MOC-CASE-008`: `OP_MOC_XI` aplica `XI-R5-CONFLICTO-SIN-ESTABILIDAD` y `OP_MOC_STATE` aplica `STATE-R4-FRICCION-LOCAL`.
- `MOC-CASE-009`: `OP_MOC_TCS` aplica `TCS-R2-EJE-SECUNDARIO-FALTANTE` y `OP_MOC_STATE` degrada a `concordancia_parcial`.
- `MOC-CASE-011`: `OP_MOC_STATE` aplica `STATE-R6-CONCORDANCIA-PARCIAL` por deuda no bloqueante.

## Implementacion local

`06_Automatizacion/moc_eval.py` implementa los cuatro operadores como lectura no mutante.

Cada resultado conserva:

- `operator_trace.xi`;
- `operator_trace.tcs`;
- `operator_trace.state`;
- `agreement`.

El reporte no transforma el repositorio, no autoriza cambios y no declara verdad canonica.

## No cubre

No valida empiricamente el MOC, no evalua personas reales, no abre uso clinico, no admite `H-Xi`, no canoniza `Xi`, no crea Nivel C, no modifica `Documento 04`, no cierra Confluencia global, no cierra Equivalencia global, no formaliza puente `MOC/AO` y no autoriza transformaciones materiales.

## Deudas abiertas

- puente formal `MOC/AO`;
- refinamiento posterior del protocolo de evaluadores;
- piloto empirico futuro no ejecutado;
- relacion futura con `C-001` / `C-002`;
- Confluencia global;
- Equivalencia global de proyecciones;
- maduracion posterior de `TCS-001`.
