# TCS-001 - Tipologia provisional de fallos de concordancia

Estatus: tipologia provisional de expediente.

Fecha: 2026-07-03.

ID: `TCS-FAIL-TYP-001`.

Expediente padre: `TCS-001`.

## Proposito

Separar clases iniciales de perdida de concordancia para que `TCS-001` pueda producir casos negativos auditables.

## Fallos

| ID | Fallo | Descripcion |
| --- | --- | --- |
| `TCS-F1` | afirmacion sin estatus | el sistema usa una afirmacion relevante sin clasificarla |
| `TCS-F2` | estatus sin autoridad | una afirmacion recibe estatus operativo sin mecanismo reconocido |
| `TCS-F3` | autoridad por repeticion | una afirmacion gana autoridad por repetirse o circular |
| `TCS-F4` | recomendacion como decision | una salida automatizada o analitica se ejecuta como decision |
| `TCS-F5` | decision sin permiso suficiente | la decision existe pero excede su alcance |
| `TCS-F6` | ejecucion sin verificacion | se registra una transformacion sin comprobar efecto posterior |
| `TCS-F7` | historial como autoridad | se usa historial para cambiar estado vigente sin decision intermedia |
| `TCS-F8` | revision sin meta-gobernanza | el sistema cambia reglas de cambio sin procedimiento |
| `TCS-F9` | conflicto de autoridades no resuelto | dos autoridades validas producen decisiones incompatibles |
| `TCS-F10` | concordancia local con discordancia global | un subsistema conserva coherencia interna pero rompe coherencia mayor |

## Lectura

La tipologia no presupone que todo fallo destruya el sistema completo.

Algunos fallos producen bloqueo; otros producen deuda, advertencia o necesidad de decision.

## Relacion con el Laboratorio

`TCS-F4`, `TCS-F5`, `TCS-F6` y `TCS-F7` ya aparecen como controles operativos en `C-001`, `C-002`, `DO-CHECK-MED-001` y `AO-CASE-BAT-001`.

## No cubre

No define metricas.

No establece severidades universales.

No decide casos clinicos, juridicos o institucionales externos.

No convierte la tipologia en Canon.
