# AUT-001 - Validacion provisional DO-CHECK-MIN

Estatus: validacion provisional de expediente.

Fecha: 2026-07-01.

## Objeto

Validar provisionalmente `06_Automatizacion/do_check_min.py` como automatizacion minima no mutante del Laboratorio.

## Alcance de la prueba

La validacion cubre:

- lectura de archivos Markdown locales;
- emision de reportes en Markdown y JSON;
- conservacion de `transformacion_permitida = false`;
- revision de archivos clave;
- revision completa del repositorio como barrido informativo.

## Reportes conservados

- `06_Automatizacion/reportes/do_check_min_claves.md`: resultado `ok`, 2 archivos revisados, 0 hallazgos.
- `06_Automatizacion/reportes/do_check_min_repo.md`: resultado `advertencia`, 81 archivos revisados, 23 hallazgos.
- `06_Automatizacion/reportes/do_check_min_repo.json`: version estructurada del barrido completo.

## Salvedad de entorno

La ejecucion directa con `python` fue bloqueada por la politica local de esta sesion de trabajo.

Por eso los reportes fueron regenerados mediante una ejecucion equivalente en el entorno interno. Esta salvedad no autoriza tratar la prueba como validacion ejecutable completa.

## Resultado

La prueba de archivos clave queda favorable como lectura minima.

El barrido completo queda en advertencia, no en bloqueo: detecta frases sensibles sobre Registro Historico y autoridad, pero conserva `transformacion_permitida = false` y recomienda continuar sin transformar.

## Conclusion

`DO-CHECK-MIN-001` queda validado provisionalmente como automatizacion minima de lectura y reporte.

`AUT-001` no debe cerrarse todavia: queda pendiente validar la ejecucion directa de `do_check_min.py` en una terminal local que permita lanzar `python`.
