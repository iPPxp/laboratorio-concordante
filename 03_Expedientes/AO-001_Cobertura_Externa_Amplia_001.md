# AO-001 - Cobertura externa amplia AO-EXT-COV-001

Estatus: aceptada localmente.

Fecha: 2026-07-06.

ID: `AO-EXT-COV-001`.

Decision asociada: `D-2026-07-06-022`.

## Proposito

Ampliar la evidencia local de AO con casos sinteticos no regulados fuera del diseno interno de `AO-001`.

## Casos cubiertos

| Caso | Dominio | Salida esperada |
| --- | --- | --- |
| `EXT-COV-001` | repositorio documental | `cobertura_externa_local` |
| `EXT-COV-002` | release tecnico | `cobertura_externa_local` |
| `EXT-COV-003` | migracion de datos ficticia | `cobertura_externa_local` |
| `EXT-COV-004` | registro de politicas | `cobertura_externa_local` |
| `EXT-COV-005` | conflicto de revisores | `conflicto_autoridades_clasificado` |
| `EXT-COV-006` | reporte externo divergente | `divergencia_clasificada` |
| `EXT-COV-007` | caso sin testigo | `bloqueo_testigo` |
| `EXT-COV-008` | autoridad excedida | `bloqueo_autoridad` |

## Herramienta

- Herramienta: `06_Automatizacion/ao_ext_cov_001.py`.
- Fixture: `06_Automatizacion/fixtures/ao_ext_cov_001_cases.json`.
- Prueba: `06_Automatizacion/test_ao_ext_cov_001.py`.
- Reportes: `06_Automatizacion/reportes/ao_ext_cov_001_report.md` y `.json`.

## Resultado esperado

```text
external_coverage_local: true
external_coverage_global: false
global_closure_authorized: false
transformacion_permitida: false
```

## Guardas

Los casos son sinteticos, no regulados y no clinicos.

La cobertura no autoriza cierre global, no modifica Documento 04, Canon, Nivel C ni `C-002`, y no usa evidencia externa como autoridad global.

## Deudas abiertas

- Cobertura independiente real.
- Evaluacion por terceros.
- Protocolo AO reproducible independiente.
- Cierre global de Confluencia y Equivalencia.
