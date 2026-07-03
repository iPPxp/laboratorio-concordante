# AUD-001 - Ficha de alcance parser real

Estatus: ficha de alcance futura.

Fecha: 2026-07-03.

ID: `ALC-PARSER-REAL-001`.

Expediente padre: `AUD-001`.

Objeto: parser real del Auditor.

## Proposito

Precisar que deberia cubrir una ruta de parser real dentro de `AUD-001`, entendida como lectura efectiva de archivos locales y extraccion de datos estructurados sin mutar el repositorio.

## Decision de alcance

El parser real no forma parte del cierre documental/operativo v0.

No modifica `C-001` ni `C-002`.

No promueve `REPORT_LAYER` a Nivel C.

No resuelve `R4` formal ni `Gamma`.

No convierte al Auditor en una herramienta mutante.

## Alcance permitido

La ruta de parser real puede incluir:

- lectura de archivos locales reales;
- interpretacion de estructuras textuales o JSON ya presentes en el repositorio;
- conversion de entradas a una forma estructurada util para el Auditor;
- validacion de errores de formato y ausencia de campos;
- integracion con `AUDITOR-V0-001` sin cambiar su semantica no mutante;
- pruebas reproducibles sobre casos concretos del repositorio.

## Alcance no permitido

La ruta de parser real no puede:

- modificar Canon o documentos oficiales;
- absorber `DO_CHECK_REPORT`;
- transformar recomendaciones en ejecucion;
- resolver `R4` formal o `Gamma`;
- promover `REPORT_LAYER` a Nivel C;
- convertir fixtures o ejemplos en autoridad por si mismos;
- saltar a una suite ejecutable completa sin decision explicita.

## Dependencias probables

Si este frente se abre de forma real, probablemente requiera:

- contrato de entrada estable;
- mapeo de formatos reales del repositorio;
- manejo de errores y vacios;
- pruebas de lectura y normalizacion;
- criterio no mutante para salida;
- decision explicita sobre si el parser vive dentro de `AUDITOR-V0-001` o como capa auxiliar.

## Estado frente a v0

Mientras esas condiciones no existan, el parser real sigue siendo deuda futura, no requisito de completitud v0.

`AUD-001` sigue completo en version documental/operativa v0 sin parser real.

## Veredicto

La ruta de parser real queda abierta y acotada, lista para trabajo posterior si se decide abrirla.
