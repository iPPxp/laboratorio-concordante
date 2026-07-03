# AUD-001 - Ficha de alcance suite ejecutable completa

Estatus: ficha de alcance futura.

Fecha: 2026-07-02.

ID: `ALC-SUITE-EJEC-001`.

Expediente padre: `AUD-001`.

Objeto: suite ejecutable completa del Auditor.

## Proposito

Precisar que deberia incluir una suite ejecutable completa de `AUD-001` si algun frente posterior decide construirla, sin confundirla con el cierre v0, el RFC operativo ni la reactivacion JSON.

## Decision de alcance

La suite ejecutable completa no forma parte del cierre documental/operativo v0.

No modifica `C-001` ni `C-002`.

No promueve `REPORT_LAYER` a Nivel C.

No resuelve `R4` formal ni `Gamma`.

No obliga a otros frentes a adoptar un formato comun.

## Alcance permitido

La suite ejecutable completa puede incluir:

- ejecucion extremo a extremo del Auditor sobre archivos locales y casos JSON;
- carga de casos externos reproducibles;
- comparacion entre salida esperada y salida obtenida;
- verificacion de que los reportes no mutan el repositorio;
- ejecucion de validaciones y pruebas integradas;
- adaptacion del contrato de entrada y salida sin cambiar la semantica v0;
- serializacion formal si se decide una interfaz estable.

## Alcance no permitido

La suite ejecutable completa no puede:

- escribir en Canon, `C-001` o `C-002`;
- absorber `DO_CHECK_REPORT`;
- convertir `REPORT_LAYER` en contrato oficial de Nivel C;
- convertir `R4-CANDIDATA` en Regla R4 formal;
- resolver `Gamma`;
- introducir transformacion material o reversion real sin decision explicita;
- convertir la deuda de v0 en bloqueo retroactivo.

## Dependencias futuras probables

Si este frente se abre de forma real, probablemente requiera:

- parser real de archivos locales;
- contrato de datos estable;
- fixtures externos versionados;
- orquestacion de pruebas reproducibles;
- criterio de salida no mutante;
- decision explicita sobre serializacion formal.

## Estado frente a v0

Mientras esas condiciones no existan, la suite ejecutable completa sigue siendo deuda futura, no requisito de completitud v0.

`AUD-001` sigue completo en version documental/operativa v0 sin ella.

## Veredicto

La suite ejecutable completa queda como ruta futura abierta y documentable, no como bloqueo actual.
