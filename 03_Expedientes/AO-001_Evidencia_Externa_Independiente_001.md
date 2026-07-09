# AO-EXT-INDEP-001 - Evidencia externa independiente

Fecha: 2026-07-06.

Estatus: preparado local, no ejecutado.

Expediente: `AO-001`.

Nota posterior 2026-07-06: `AO-EXT-REAL-001` aporta primera evidencia externa independiente real admitida preliminarmente por `D-2026-07-06-035`. Esta ruta base sigue vigente como compuerta preparada; el manifiesto de control no cuenta como evidencia real y la suite real no autoriza cierre global.

## Objeto

Abrir una ruta local no mutante para preparar la admision futura de evidencia externa independiente no sintetica dentro de `AO-001`.

La ruta no busca, no descarga y no ejecuta evidencia real. Solo fija como deberia recibirse un manifiesto externo para que pueda evaluarse despues sin reabrir `P-PI.0` / `P-PI.1` ni alterar Canon, Documento 04, Nivel C o `C-002`.

## Definicion operativa

Cuenta como evidencia externa independiente, de forma preliminar, un artefacto que cumpla todas estas condiciones:

- no fue generado por fixtures del Laboratorio;
- no pertenece a dominio clinico ni regulado;
- no contiene personas reales ni datos personales;
- declara fuente identificable;
- declara unidad comparable con las proyecciones AO;
- aporta testigo, restricciones y trazabilidad;
- no usa historial como autoridad directa;
- no reclama autoridad canonica, Nivel C, cierre global ni permiso de transformacion.

## Frontera

`AO-EXT-INDEP-001` puede:

- preparar manifiestos de fuente;
- clasificar admisibilidad preliminar;
- separar deuda por falta de fuente real de rechazo por alcance, autoridad o dominio;
- alimentar `AO-GLOBAL-READINESS-001` como ruta posterior preparada.

`AO-EXT-INDEP-001` no puede:

- recolectar evidencia externa por si mismo;
- ejecutar estudios empiricos reales;
- usar personas reales, datos personales o dominios clinicos/regulados;
- promover `REPORT_LAYER`;
- exportar R4/Gamma;
- cerrar Confluencia global o Equivalencia global;
- reabrir `P-PI.0` / `P-PI.1`;
- modificar Documento 04, Canon, Nivel C o `C-002`.

## Relacion con readiness global

`AO-GLOBAL-READINESS-001` sigue vigente como matriz de no autorizacion global.

Para la compuerta base sin fuente real aportada, la salida obligatoria permanece:

```text
external_evidence_ready: false
global_closure_authorized: false
global_export_authorized: false
report_layer_promoted: false
r4_gamma_global_export_authorized: false
```

## Evidencia tecnica preparada

- Compuerta: `03_Expedientes/AO-001_Compuerta_Evidencia_Externa_001.md`.
- Herramienta: `06_Automatizacion/ao_external_evidence_gate_001.py`.
- Fixture: `06_Automatizacion/fixtures/ao_external_evidence_gate_001_manifests.json`.
- Prueba: `06_Automatizacion/test_ao_external_evidence_gate_001.py`.
- Reporte esperado: `06_Automatizacion/reportes/ao_external_evidence_gate_001_report.md`.
- Fixture real posterior: `06_Automatizacion/fixtures/ao_external_evidence_real_001_manifests.json`.
- Reporte real posterior: `06_Automatizacion/reportes/ao_external_evidence_real_001_report.md`.

## Deudas abiertas

- Decidir si `AO-EXT-REAL-001` debe alimentar una reevaluacion posterior de `AO-GLOBAL-READINESS-001`.
- Validar unidad comparable fuera de fixtures internos.
- Revisar si un manifiesto real admisible basta para reconsiderar compuertas globales.
- Mantener Confluencia global y Equivalencia global no autorizadas hasta nueva decision.
