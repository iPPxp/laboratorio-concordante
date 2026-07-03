# AUD-001 - Implementacion no mutante C-002

Estatus: implementacion inicial de expediente.

Fecha: 2026-07-02.

Actualizacion: 2026-07-03.

Expediente padre: `AUD-001`.

Identificador operativo: `AUDITOR-V0-001`.

Archivo ejecutable: `06_Automatizacion/auditor_v0.py`.

## Proposito

Materializar una primera implementacion no mutante del Auditor v0 conforme a `C-002`.

La implementacion ejecuta lectura acotada, clasificacion de casos y emision de reportes. No ejecuta transformaciones, no modifica artefactos de entrada y no convierte recomendaciones en decisiones de autoridad.

## Fuentes locales

- `02_Documentos/C-002_RFC_Operativo_Auditor_v0.md`
- `02_Documentos/C-001_Especificacion_Tecnica_Auditor.md`
- `03_Expedientes/AUD-001_Casos_Prueba_Auditor.md`
- `03_Expedientes/AUD-001_Contrato_Reportes.md`
- `03_Expedientes/DO-001_Regla_Permiso_Actualizacion.md`

## Superficie implementada

`auditor_v0.py` implementa:

- matriz minima `AUD-T00` a `AUD-T09`;
- reportes `AUDITOR_V0_REPORT` en Markdown y JSON;
- reportes por operador compatibles con `OPERATOR_REPORT`;
- modo no mutante con `transformacion_permitida = false`;
- matriz interna como fuente vigente de casos;
- carga opcional de casos JSON por `--case-file`;
- fixture externo `06_Automatizacion/fixtures/auditor_v0_cases.json`;
- fixture documental parcial `06_Automatizacion/fixtures/auditor_v0_documental_cases.json`;
- esquema operativo `06_Automatizacion/fixtures/auditor_v0_case_schema.json`;
- salida por consola o por `--output`;
- validacion de ruta de salida dentro del repositorio.
- validacion de campos requeridos por `kind` para casos documentales.

## Comandos

```powershell
python 06_Automatizacion/auditor_v0.py --format md
python 06_Automatizacion/auditor_v0.py --format md --output 06_Automatizacion/reportes/auditor_v0_report.md
python 06_Automatizacion/auditor_v0.py --format json --output 06_Automatizacion/reportes/auditor_v0_report.json
python 06_Automatizacion/auditor_v0.py --format json --case-file 06_Automatizacion/fixtures/auditor_v0_cases.json
python 06_Automatizacion/auditor_v0.py --format json --case-file 06_Automatizacion/fixtures/auditor_v0_documental_cases.json
python -m unittest 06_Automatizacion/test_auditor_v0.py
```

`--format json` y `--case-file` quedan reactivados por `AUD-001_Decision_Reactivacion_JSON_Auditor_v0.md`.

El fixture documental es parcial y debe devolver codigo distinto de cero si se ejecuta por CLI, porque omite los casos obligatorios `AUD-T00` a `AUD-T09`. Esa no conformidad es esperada y no implica permiso de transformacion.

## No cubre

Esta implementacion no cubre:

- ejecucion de `Tr`;
- modificacion de Canon;
- modificacion de documentos oficiales;
- cierre automatico de expedientes;
- promocion de `REPORT_LAYER` a contrato independiente de Nivel C;
- inferencia de dependencias no materializadas;
- reversion material.

## Deuda viva

- ampliar validaciones semanticas por tipo de caso;
- ampliar fixtures documentales externos mas alla del primer lote parcial;
- conectar la salida con tableros sin convertir reportes en autoridad;
- mantener `REPORT_LAYER` como lectura local mientras no exista promocion propia.
