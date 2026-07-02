# AUT-001 - Clasificacion de Advertencias y Riesgos

Estatus: especificacion provisional aceptada para clasificacion no mutante.

Fecha: 2026-07-02.

## Objeto

`DO-LAB-RISK-001` clasifica hallazgos de `DO-CHECK-MIN-001` y `DO-CHECK-MED-001` para separar advertencias heredadas, deuda documental y riesgos activos.

## Categorias

- `riesgo_activo`: hallazgo situado en superficie vigente, Canon, documento oficial, estado o automatizacion activa.
- `deuda_documental`: referencia faltante, estatus ausente o reporte incompleto.
- `advertencia_heredada`: hallazgo localizado en expediente cerrado, pausado o historico.
- `observacion`: hallazgo conservado sin clasificacion fuerte.

## Alcance

- leer reportes JSON existentes;
- deduplicar hallazgos;
- asignar categoria y severidad operativa;
- emitir reporte Markdown y JSON;
- mantener `transformacion_permitida: false`.

## Fuera de alcance

- corregir hallazgos por si mismo;
- modificar Canon o documentos oficiales;
- cerrar expedientes;
- convertir riesgos en decisiones.

## Artefacto ejecutable

- `06_Automatizacion/lab_risk_classifier.py`

## Reportes esperados

- `06_Automatizacion/reportes/lab_risk_report.md`
- `06_Automatizacion/reportes/lab_risk_report.json`
