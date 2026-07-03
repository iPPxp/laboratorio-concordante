# AUD-001 - Decision de estatus de implementacion no mutante C-002

Estatus: decision operativa de expediente.

Fecha: 2026-07-02.

Actualizacion: 2026-07-03.

Expediente padre: `AUD-001`.

## Decision

Se acepta `06_Automatizacion/auditor_v0.py` como implementacion inicial no mutante de `AUDITOR-V0-001`.

La aceptacion queda limitada a lectura, evaluacion de la matriz minima `AUD-T00` a `AUD-T09`, emision de reportes y validacion local contra `C-002`.

## Fundamento

- `C-002` exige que una herramienta no mutante implemente lectura acotada, produzca reportes y no transforme artefactos.
- `AUD-001_Casos_Prueba_Auditor.md` define la matriz minima `AUD-T00` a `AUD-T09`.
- `AUD-001_Contrato_Reportes.md` define la forma provisional de reportes por operador.
- `auditor_v0.py` emite `AUDITOR_V0_REPORT` con `transformacion_permitida = false`.
- `test_auditor_v0.py` confirma cobertura minima y estabilidad de resultados esperados.

## Alcance

La decision cubre:

- ejecucion local del auditor en modo no mutante;
- generacion de reportes Markdown;
- generacion de reportes JSON;
- carga opcional de casos JSON por `--case-file`;
- conservacion de evidencia en `06_Automatizacion/reportes/`;
- uso de la implementacion como base de pruebas para siguientes iteraciones.

## No autoriza

Esta decision no autoriza:

- ejecutar transformaciones sobre artefactos;
- modificar Canon;
- modificar documentos oficiales;
- cerrar `AUD-001` completo;
- promover `REPORT_LAYER` como contrato independiente;
- tratar los reportes como autoridad directa fuera de `C-002`.

## Consecuencia

El siguiente frente tecnico queda en pruebas externas y endurecimiento de contrato:

- fixtures externos documentales;
- pruebas de entradas mal formadas;
- validacion de esquema de reportes;
- integracion posterior con herramientas de estado sin introducir mutacion.
