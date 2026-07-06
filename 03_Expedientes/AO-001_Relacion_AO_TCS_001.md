# AO-001 - Relacion local AO/TCS AO-TCS-REL-001

Estatus: aceptada localmente.

Fecha: 2026-07-06.

ID: `AO-TCS-REL-001`.

Decision asociada: `D-2026-07-06-020`.

## Proposito

Relacionar fallos de `AO-001` con la tipologia provisional de `TCS-001`, sin canonizar `TCS-001` y sin convertir la clasificacion local en cierre global.

## Alcance

La relacion acepta solo clasificacion no mutante de fallos:

| Senal AO | Tipo TCS | Estado MOC/TCS local |
| --- | --- | --- |
| `falta_testigo` | `TCS-F1` | `bloqueo_de_concordancia` |
| `aumento_autoridad` | `TCS-F2` | `bloqueo_de_concordancia` |
| `autoridad_por_repeticion` | `TCS-F3` | `bloqueo_de_concordancia` |
| `recomendacion_como_decision` | `TCS-F4` | `bloqueo_de_concordancia` |
| `perdida_permiso` | `TCS-F5` | `bloqueo_de_concordancia` |
| `historial_autoridad` | `TCS-F7` | `bloqueo_de_concordancia` |
| `conflicto_autoridades` | `TCS-F9` | `bloqueo_de_concordancia` |
| `divergencia_clasificada` | `TCS-F10` | `discordancia_global_controlada` |
| `no_comparable` | `TCS-F10` | `no_comparable` |
| `bloqueo_concordancia` | `TCS-F10` | `bloqueo_de_concordancia` |

## Herramienta

- Herramienta: `06_Automatizacion/ao_tcs_rel_001.py`.
- Fixture: `06_Automatizacion/fixtures/ao_tcs_rel_001_cases.json`.
- Prueba: `06_Automatizacion/test_ao_tcs_rel_001.py`.
- Reportes: `06_Automatizacion/reportes/ao_tcs_rel_001_report.md` y `.json`.

## Resultado esperado

```text
tcs_relation_local: true
tcs_canonical: false
global_closure_authorized: false
transformacion_permitida: false
```

La herramienta ejecuta diez casos sinteticos: siete mapeos locales, un caso no comparable y dos bloqueos defensivos por alcance.

## Guardas

Esta relacion no modifica Documento 04, Canon, Nivel C ni `C-002`.

No canoniza `TCS-001`, no promueve `REPORT_LAYER`, no exporta R4/Gamma, no reabre `P-PI.0` / `P-PI.1` y no cierra Confluencia ni Equivalencia global.

## Deudas abiertas

- Semantica formal posterior de `TCS-001`.
- Protocolo AO reproducible independiente.
- Cierre global de Confluencia.
- Cierre global de Equivalencia de proyecciones.
