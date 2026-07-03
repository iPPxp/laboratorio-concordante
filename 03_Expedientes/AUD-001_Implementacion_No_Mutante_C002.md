# AUD-001 - Implementacion no mutante C-002

Estatus: implementacion inicial de expediente.

Fecha: 2026-07-02.

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
- reportes `AUDITOR_V0_REPORT` en Markdown;
- salida JSON pausada temporalmente hasta reactivacion explicita;
- reportes por operador compatibles con `OPERATOR_REPORT`;
- modo no mutante con `transformacion_permitida = false`;
- matriz interna como fuente vigente de casos;
- carga opcional de casos por `--case-file` pausada temporalmente junto con JSON;
- salida por consola o por `--output`;
- validacion de ruta de salida dentro del repositorio.

## Comandos

```powershell
python 06_Automatizacion/auditor_v0.py --format md
python 06_Automatizacion/auditor_v0.py --format md --output 06_Automatizacion/reportes/auditor_v0_report.md
python -m unittest 06_Automatizacion/test_auditor_v0.py
```

Mientras JSON este pausado, `--format json` y `--case-file` deben fallar temprano.

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

- reactivar JSON solo con decision explicita;
- estabilizar un esquema formal para archivos externos de casos cuando JSON se reactive;
- ampliar pruebas de casos externos cuando JSON se reactive;
- definir fixtures documentales fuera de automatas;
- conectar la salida con tableros sin convertir reportes en autoridad;
- mantener `REPORT_LAYER` como lectura local mientras no exista promocion propia.
