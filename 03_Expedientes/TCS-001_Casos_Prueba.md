# TCS-001 - Casos de prueba abstractos

Estatus: casos provisionales de expediente.

Fecha: 2026-07-03.

ID: `TCS-CASE-BAT-001`.

Expediente padre: `TCS-001`.

## Proposito

Crear casos abstractos para probar `TCS-DEF-MIN-001` y `TCS-FAIL-TYP-001` sin abrir teoria canonica.

## Casos positivos

| Caso | Descripcion | Resultado esperado |
| --- | --- | --- |
| `TCS-CASE-001` | sistema registra afirmacion, estatus, autoridad, decision y permiso antes de actuar | concordancia local |
| `TCS-CASE-002` | sistema conserva desacuerdo con estatus declarado y decision de alcance acotado | concordancia local con desacuerdo |
| `TCS-CASE-003` | automatizacion recomienda, pero autoridad humana o documental decide | concordancia asistida |

## Casos negativos

| Caso | Fallo principal | Resultado esperado |
| --- | --- | --- |
| `TCS-CASE-004` | `TCS-F1` | bloqueo por afirmacion sin estatus |
| `TCS-CASE-005` | `TCS-F4` | recomendacion no puede ejecutarse como decision |
| `TCS-CASE-006` | `TCS-F7` | historial queda como evidencia pasiva, no autoridad |
| `TCS-CASE-007` | `TCS-F9` | se exige mecanismo de resolucion de autoridades |
| `TCS-CASE-008` | `TCS-F10` | se registra discordancia global aunque haya coherencia local |

## Criterio de pase

Un caso pasa si la clasificacion resultante conserva:

- estatus;
- autoridad;
- permiso;
- evidencia;
- decision;
- deuda o bloqueo cuando corresponda.

## Veredicto

La bateria permite empezar a probar `TCS-001` como marco teorico minimo.

No basta para teoria general ni promocion.

## No cubre

No prueba dominios externos.

No define metrica cuantitativa.

No modifica Canon ni documentos oficiales.

No abre frente clinico, juridico o institucional externo.
