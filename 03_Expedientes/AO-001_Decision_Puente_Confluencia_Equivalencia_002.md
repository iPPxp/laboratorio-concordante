# Decision - AO-PPI-BRIDGE-002

Estatus: decision provisional aceptada.

Fecha: 2026-07-06.

ID de decision: `D-2026-07-06-017`.

Expediente: `AO-001`.

Objeto: `AO-PPI-BRIDGE-002`.

## Decision

Se acepta `AO-PPI-BRIDGE-002` como bateria fuerte local no mutante para Confluencia y Equivalencia de proyecciones.

## Se acepta

- El documento `AO-001_Puente_Confluencia_Equivalencia_002.md`.
- La herramienta `06_Automatizacion/ao_ppi_bridge_002.py`.
- El fixture `06_Automatizacion/fixtures/ao_ppi_bridge_002_cases.json`.
- Los reportes `06_Automatizacion/reportes/ao_ppi_bridge_002_report.md` y `.json`.
- La integracion a `DO-LAB-RUN-001` como paso no mutante.

## Resultado

La bateria ejecuta 8 casos fuertes:

- 2 equivalencias fuertes locales positivas;
- 1 confluencia fuerte local positiva;
- 2 divergencias clasificadas;
- 1 bloqueo por testigo;
- 1 bloqueo por `REPORT_LAYER` incompleto;
- 1 bloqueo por aumento de autoridad.

Todos los casos pasan contra la salida esperada.

## Guardas

Esta decision conserva las siguientes fronteras:

- Documento 04: sin cambios.
- Canon: sin cambios.
- Nivel C: sin alta nueva.
- `P-PI.0` y `P-PI.1`: cerrados como frentes de trabajo.
- Confluencia global: abierta.
- Equivalencia global: abierta.
- `REPORT_LAYER`: local pre-C, sin promocion.
- R4/Gamma: sin exportacion general.
- Transformaciones materiales: no autorizadas.

## Deudas abiertas

- Confluencia global.
- Equivalencia global de proyecciones.
- Serializacion interfrente de `REPORT_LAYER`, solo si una decision futura la exige.
- Relacion posterior con `TCS-001`.
- Exportacion general R4/Gamma, bloqueada por compuerta vigente.

## Ruta posterior recomendada

La siguiente ruta defensible es una de estas:

- `AO-PPI-BRIDGE-003`: matriz de condiciones faltantes para cierre global;
- `AO-REPORT-SERIAL-001`: serializacion interfrente de `REPORT_LAYER`, solo si se decide abrirla;
- `AO-TCS-REL-001`: lectura de fallos de concordancia desde `TCS-001`, sin canonizar TCS.
