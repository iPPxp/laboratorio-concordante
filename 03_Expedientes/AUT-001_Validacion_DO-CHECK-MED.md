# AUT-001 - Validacion provisional DO-CHECK-MED

Estatus: validacion provisional de expediente.

Fecha: 2026-07-01.

Identificador: `AUT-VAL-002`.

## Objeto

Validar provisionalmente `06_Automatizacion/do_check_med.py` como automatizacion media no mutante del Laboratorio.

## Fuentes

- `03_Expedientes/AUT-001.md`
- `03_Expedientes/AUT-001_Mapa_Fase_Media_AAU.md`
- `06_Automatizacion/do_check_med.py`
- `06_Automatizacion/reportes/do_check_med_claves.md`
- `06_Automatizacion/reportes/do_check_med_repo.md`
- `06_Automatizacion/reportes/do_check_med_repo.json`
- `02_Documentos/C-001_Especificacion_Tecnica_Auditor.md`
- `03_Expedientes/DO-001_DO-CHECK-001.md`
- `03_Expedientes/DO-001_Regla_Permiso_Actualizacion.md`
- `03_Expedientes/REC-001_Mapa_Reconciliacion_Canon_Baselines.md`

## Ejecucion

La ejecucion directa con `python` fue intentada en esta sesion y quedo bloqueada por la politica del entorno.

Para conservar avance verificable, los reportes se generaron mediante una ejecucion equivalente interna de las mismas reglas de lectura.

Esta validacion no debe tratarse como confirmacion de ejecucion directa local con `python`.

## Cobertura validada

- Revision de archivos clave: `CURRENT_STATE.md`, `03_Expedientes/AUT-001.md` y `02_Documentos/C-001_Especificacion_Tecnica_Auditor.md`.
- Barrido Markdown del repositorio excluyendo reportes generados.
- Resolucion mejorada de referencias locales por ruta exacta, directorio existente o nombre de archivo materializado.
- Deteccion de estatus ausente.
- Deteccion de referencias no materializadas.
- Deteccion de lenguaje sensible sobre Canon, documentos oficiales, expedientes cerrados o hipotesis.
- Deteccion de usos historicos como posible autoridad vigente.
- Puente funcional con AAU historico: `Presv`, `Activas(G)`, `Inv(G)`, `Break(Fk)` y estados locales.

## Resultado

La herramienta produce reportes conservados y no mutantes.

El resultado esperado para el repositorio vigente es `advertencia` / `SUSPENDIDO`: hay deudas y zonas sensibles, pero no se permite transformacion.

`transformacion_permitida` permanece siempre en `false`.

## Dictamen

`DO-CHECK-MED-001` queda validado provisionalmente como automatizacion media de lectura, reporte y priorizacion de riesgos.

`AUT-001` no debe cerrarse todavia: queda pendiente validar ejecucion directa local de `do_check_med.py` y decidir si esta fase media basta como compuerta antes de abrir psicologia.
