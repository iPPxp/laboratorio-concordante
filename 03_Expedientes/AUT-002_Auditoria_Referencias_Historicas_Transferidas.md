# AUT-002 - Auditoria de referencias historicas transferidas

Estatus: auditoria favorable.

Fecha: 2026-07-03.

ID auditoria: `AUT-AUD-HIST-PSI-001`.

Expediente padre: `AUT-002`.

## Objeto auditado

- `03_Expedientes/AUT-002.md`
- `06_Automatizacion/do_check_min.py`
- `06_Automatizacion/do_check_med.py`

## Criterios

| Criterio | Resultado | Evidencia |
| --- | --- | --- |
| No restaura `PSI-001*` | pasa | el ajuste solo clasifica referencias |
| No reabre psicologia local | pasa | `AUT-002` declara alcance tecnico |
| Mantiene bloqueos activos | pasa | los usos activos sin decision puente siguen bloqueables |
| Reduce falsos bloqueos de control negativo | pasa | secciones de prueba, simulacion y "No cubre" quedan reconocidas |
| Conserva trazabilidad | pasa | las referencias transferidas quedan como advertencia controlada |

## Hallazgos

La deuda detectada por los reportes no exige restaurar la copia local de `PSI-001`.

La clasificacion nueva es mas precisa que el bloqueo anterior porque separa tres casos:

- archivo activo faltante;
- referencia historica transferida;
- uso vigente de historial como autoridad.

## Riesgos residuales

- Si una fuente oficial futura usa `PSI-001` como contenido sustantivo, debe abrir decision puente.
- Si se requiere material psicologico, debe consultarse el proyecto independiente `Psicologia Concordante`, no la copia eliminada.
- Si los detectores vuelven a producir falsos positivos, la deuda queda en automatizacion, no en restauracion documental.

## Veredicto

Favorable.

El refinamiento es no mutante respecto de Canon, documentos oficiales y expedientes sustantivos.
