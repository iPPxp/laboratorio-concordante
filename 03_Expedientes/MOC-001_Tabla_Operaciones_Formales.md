# MOC-001 - Tabla de operaciones formales

ID: `MOC-OPS-FORMAL-001`.

Ruta: `MOC-ROUTE-008`.

Fecha: 2026-07-06.

Estatus: tabla operativa provisional, no canonica.

Decision asociada: `D-2026-07-06-004`.

## Proposito

Consolidar las operaciones formales locales del MOC en una tabla unica para lectura, auditoria y preparacion documental de piloto no ejecutado.

## Tabla principal

| Operacion | Firma local | Entrada minima | Salida | Regla ganadora | Efecto permitido |
| --- | --- | --- | --- | --- | --- |
| `OP_MOC_NORMALIZE` | `raw_case -> C` | caso sintetico, alcance, evidencia | caso normalizado | `NORM-R*` | preparar lectura |
| `OP_MOC_SCOPE` | `C -> scope_status` | alcance, restricciones | `permitido` / `bloqueado` | `SCOPE-R*` | bloquear dominios prohibidos |
| `OP_MOC_XI` | `C -> X` | `R0`, `R1`, `Dist`, `Res`, evidencia | `redundante`, `util_acotado`, `limitado`, `no_comparable`, `bloqueado` | `XI-R*` | lectura relacional local |
| `OP_MOC_TCS` | `C -> T` | ejes TCS | `tcs_completo`, `deuda_secundaria`, `bloqueo_de_concordancia` | `TCS-R*` | control de concordancia minima |
| `OP_MOC_STATE` | `(X,T,flags) -> S` | salida Xi, TCS, banderas | estado MOC | `STATE-R*` | clasificacion ordinal local |
| `OP_MOC_AGREEMENT` | `votos -> A` | respuestas de evaluadores | coincidencia o desacuerdo | `AGR-R*` | medir similitud sin forzar unanimidad |
| `OP_MOC_TRACE` | `(X,T,S,A) -> Q` | reglas ganadoras y deuda | `operator_trace` | `TRACE-R*` | conservar testigo |
| `OP_MOC_AO_BRIDGE` | `Q -> B_AO` | `operator_trace` | rol AO local | `AO-BRIDGE-R*` | apoyo local a AO sin cierre global |
| `OP_MOC_PROTOCOL_V02` | `(C,Q,votos) -> P` | caso, traza, votos | tratamiento protocolar | `PROTO-R*` | explicar desempate y deuda |
| `OP_MOC_RESPONSE` | `(C,S,Q,P) -> Y` | caso, estado, traza, protocolo | respuesta de evaluador | `RESP-R*` | registro documental |
| `OP_MOC_FREEZE` | `paquete -> F` | casos, reglas, protocolo | version congelada | `FREEZE-R*` | fijar version documental |
| `OP_MOC_GATE` | `F -> gate_status` | version congelada, deudas, restricciones | autorizar / no autorizar | `GATE-R*` | decidir compuerta, no ejecutar por si mismo |

## Reglas de combinacion

| Regla | Prioridad | Descripcion |
| --- | --- | --- |
| `COMB-R1-SEGURIDAD` | 1 | bloqueo por alcance, evidencia, persona real, datos personales o dominio prohibido domina cualquier salida positiva |
| `COMB-R2-COMPARABILIDAD` | 2 | perdida de unidad minima produce `no_comparable` salvo que exista bloqueo de seguridad |
| `COMB-R3-CONFLICTO-GLOBAL` | 3 | rutas validas incompatibles escalan a `discordancia_global` |
| `COMB-R4-FRICCION` | 4 | conflicto local sin estabilidad nueva produce `friccion_operativa` |
| `COMB-R5-CONCORDANCIA-PARCIAL` | 5 | salida positiva con deuda secundaria produce `concordancia_parcial` |
| `COMB-R6-CONCORDANCIA-LOCAL` | 6 | salida positiva sin deuda bloqueante produce `concordancia_local` |

## Estados y familias

| Estado MOC | Familia | Uso permitido |
| --- | --- | --- |
| `concordancia_local` | concordante | evidencia local fuerte, sin cierre global |
| `concordancia_parcial` | concordante | evidencia local con deuda visible |
| `friccion_operativa` | friccion | caso para ajuste de regla o decision local |
| `discordancia_global` | friccion | evidencia de problema global abierto |
| `bloqueo_de_concordancia` | seguridad | no uso positivo |
| `no_comparable` | seguridad | comparacion detenida |

## Salidas prohibidas

Ninguna operacion formal puede producir:

- autorizacion de piloto real;
- reclutamiento de evaluadores;
- recoleccion de datos personales;
- evaluacion de personas reales;
- uso clinico;
- modificacion de Canon, Nivel C, `Documento 04` o repositorio;
- cierre de Confluencia global o Equivalencia global.

## Estado de implementacion local

`MOC-EVAL-001` implementa ya las operaciones centrales de lectura:

- `OP_MOC_XI`;
- `OP_MOC_TCS`;
- `OP_MOC_STATE`;
- `OP_MOC_AGREEMENT`;
- `OP_MOC_TRACE`;
- `OP_MOC_AO_BRIDGE`;
- `OP_MOC_PROTOCOL_V02`.

`OP_MOC_FREEZE`, `OP_MOC_RESPONSE` y `OP_MOC_GATE` quedan documentadas para el paquete pre-ejecucion, no como ejecucion real.
