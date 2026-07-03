# AUD-001 - Ficha de alcance Gamma

Estatus: ficha de alcance futura.

Fecha: 2026-07-03.

ID: `ALC-GAMMA-001`.

Expediente padre: `AUD-001`.

Objeto: construccion formal de `Gamma`.

## Proposito

Precisar el alcance de una eventual construccion formal de `Gamma` dentro de `AUD-001`, sin confundirla con una afirmacion ya valida, con una simplificacion narrativa o con una extension automatica de `R4-CANDIDATA`.

## Decision de alcance

`Gamma` no forma parte del cierre documental/operativo v0.

No modifica `C-001` ni `C-002`.

No convierte `Gamma` en teorema por declaracion.

No absorbe `REPORT_LAYER`, `DO_CHECK_REPORT` ni `R4-CANDIDATA`.

No sustituye el trabajo de `R4` formal; lo presupone como deuda previa o paralela si la ruta asi lo exige.

## Alcance permitido

La ruta de `Gamma` puede incluir:

- definicion local de la construccion;
- sintaxis minima y condiciones de aplicacion;
- relacion con `R4` formal y con la candidata `R4-CANDIDATA`;
- criterio para distinguir construccion formal, hipotesis, deuda y uso indebido;
- pruebas o ejemplos internos donde `Gamma` no sea meramente nominal;
- delimitacion de casos en que `Gamma` debe degradarse a deuda o problema abierto.

## Alcance no permitido

La ruta de `Gamma` no puede:

- usar el Registro Historico como autoridad directa;
- convertir una invocacion textual en construccion valida;
- promover `Gamma` por analogia;
- resolver transformaciones no cubiertas por simple declaracion;
- convertir `R4-CANDIDATA` en Regla R4 formal;
- imponer `Gamma` como contrato obligatorio para otros frentes;
- saltar la necesidad de pruebas o definicion local.

## Dependencias probables

Si este frente se abre de forma real, probablemente requiera:

- una definicion local de `Gamma`;
- relacion clara con `R4` formal;
- una forma de verificar que no se trata de nombre vacio;
- casos de uso o de no uso dentro del Auditor;
- decision explicita sobre su estatus documental;
- posible revision de `AUD-001_Validaciones.md` y `AUD-001_Simulaciones.md`.

## Estado frente a v0

Mientras esas condiciones no existan, `Gamma` sigue siendo deuda futura, no requisito de completitud v0.

`AUD-001` sigue completo en version documental/operativa v0 sin `Gamma`.

## Veredicto

La ruta de `Gamma` queda abierta y acotada como siguiente deuda estructural, lista para trabajo posterior si se decide abrirla.
