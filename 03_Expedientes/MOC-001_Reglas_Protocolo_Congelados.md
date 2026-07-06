# MOC-001 - Version congelada de reglas y protocolo

ID: `MOC-PILOT-RULE-FREEZE-001`.

Ruta: `MOC-ROUTE-008`.

Fecha: 2026-07-06.

Estatus: version documental congelada, no ejecutada.

Decision asociada: `D-2026-07-06-004`.

## Proposito

Congelar la version de reglas y protocolo que acompana el paquete documental pre-ejecucion del piloto futuro.

El congelamiento no ejecuta piloto, no valida empiricamente el MOC y no autoriza reclutamiento.

## Documentos congelados

| Documento | Rol | SHA256 |
| --- | --- | --- |
| `MOC-001_Formalizacion_Xi_eval.md` | reglas `Xi_eval` | `454F6C35E4D620F38ECCCEF50AF46B8A218A7AA5BBFCF647FD35EDAF43735C6B` |
| `MOC-001_Metricas_Estados.md` | estados y familias MOC | `A1231D5343DB16907DD67D9E11A8CA6BBB525852BDA89C72016B40E16C863CD5` |
| `MOC-001_Puente_Formal_MOC_TCS.md` | operadores `OP_MOC_XI`, `OP_MOC_TCS`, `OP_MOC_STATE`, `OP_MOC_AGREEMENT` | `87E22AFCDFF05255122681A5D0A0E3C4A057189DAAEA7C938ECF70D7EB852563` |
| `MOC-001_Puente_Formal_MOC_AO.md` | `operator_trace`, `Pi_moc_trace`, `ao_bridge` | `FE46FC3387B4C210276684FF5E3F14B5F555FEDB0E283FFB9CCE9FB45E402376` |
| `MOC-001_Protocolo_Evaluacion_v0_2.md` | protocolo de respuesta y desacuerdo | `156CA7006304285519C46E841A0482A8B20FB2DECC404B58EBE6A2605CEF2A08` |

## Reglas congeladas

| Grupo | Regla congelada |
| --- | --- |
| Dominio | solo `sintetico_no_clinico` |
| Seguridad | personas reales, datos personales, uso clinico o dominio regulado producen bloqueo |
| Comparabilidad | perdida de unidad minima produce `no_comparable` |
| Xi | `bloqueado`, `no_comparable`, `util_acotado`, `limitado`, `redundante` |
| TCS | eje nuclear faltante bloquea; eje secundario faltante degrada |
| Estado MOC | seguridad domina; luego comparabilidad; luego conflicto global; luego friccion; luego concordancia |
| Agreement | exacto, parcial o desacuerdo justificado |
| Trace | siempre conservar regla ganadora, testigo y deuda |
| AO bridge | solo apoyo local; no cierre global |
| Protocolo v0.2 | desempate por `operator_trace.state.rule_id`, sin borrar desacuerdos |

## Flujo congelado

```text
caso -> OP_MOC_SCOPE
     -> OP_MOC_XI
     -> OP_MOC_TCS
     -> OP_MOC_STATE
     -> OP_MOC_AGREEMENT
     -> OP_MOC_TRACE
     -> OP_MOC_AO_BRIDGE
     -> OP_MOC_PROTOCOL_V02
     -> OP_MOC_RESPONSE
```

## Criterio de version

La version queda congelada solo mientras:

- los hashes de documentos no cambien;
- el fixture congelado conserve hash registrado en `MOC-PILOT-CASE-FREEZE-001`;
- no se modifique `moc_eval.py` para alterar reglas de salida;
- no se autorice ejecucion real por decision posterior.

## Restricciones

Esta version congelada:

- no autoriza piloto;
- no recluta evaluadores;
- no recoge respuestas reales;
- no recopila datos personales;
- no usa casos reales;
- no canoniza MOC ni `Xi`;
- no modifica `Documento 04`;
- no cierra Confluencia global ni Equivalencia global.
