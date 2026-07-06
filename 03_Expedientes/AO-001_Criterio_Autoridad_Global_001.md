# AO-001 - Criterio local de autoridad AO-AUTH-GLOBAL-001

Estatus: aceptado localmente.

Fecha: 2026-07-06.

ID: `AO-AUTH-GLOBAL-001`.

Decision asociada: `D-2026-07-06-021`.

## Proposito

Definir una matriz local de comparabilidad entre niveles para evitar aumentos indebidos de autoridad cuando AO compara expedientes, documentos, Nivel C, Canon, reportes automatizados, registro historico y evidencia externa sintetica.

## Matriz local

| Fuente | Destino | Clasificacion |
| --- | --- | --- |
| `canon` | `documento` | `autoridad_superior_reconocida` |
| `nivel_c` | `expediente` | `autoridad_tecnica_acotada` |
| `documento` | `expediente` | `autoridad_documental` |
| `expediente` | `expediente` | `autoridad_local` |
| `reporte_automatizado` | `expediente` | `evidencia_tecnica_no_autoridad` |
| `registro_historico` | `expediente` | `evidencia_pasiva_no_autoridad` |
| `externo_sintetico` | `expediente` | `evidencia_externa_no_autoridad` |

## Bloqueos

- Historial usado como autoridad directa.
- Promocion por repeticion.
- Reporte convertido en decision.
- Autoridad global no declarada.
- Modo mutante no autorizado.
- Falta de testigo.

## Herramienta

- Herramienta: `06_Automatizacion/ao_authority_global_001.py`.
- Fixture: `06_Automatizacion/fixtures/ao_authority_global_001_cases.json`.
- Prueba: `06_Automatizacion/test_ao_authority_global_001.py`.
- Reportes: `06_Automatizacion/reportes/ao_authority_global_001_report.md` y `.json`.

## Resultado esperado

```text
authority_criterion_local: true
global_authority_authorized: false
global_closure_authorized: false
transformacion_permitida: false
```

## Guardas

El criterio no crea autoridad global real. Solo ordena comparabilidad local.

No modifica Canon, Nivel C, Documento 04 ni `C-002`; no promueve reportes automatizados a decision; no convierte historial en autoridad.

## Deudas abiertas

- Autoridad global real, si alguna vez se autoriza, requiere decision separada.
- Protocolo AO reproducible independiente.
- Cierre global de Confluencia y Equivalencia.
