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

## Ruta 1 activada

La primera ruta acotada quedo materializada posteriormente en `AUD-001_Gamma_Ruta1_Definicion_Local.md`.

Resultado: `GAMMA-DEF-001` define localmente `Gamma` como `Gamma_1(E, C) = G`, una operacion de generalizacion controlada con evidencia, contexto, invariantes, restricciones, deudas y salida segura.

Esta activacion no construye `Gamma` formal, no modifica `C-001` ni `C-002`, no promueve `Gamma` a Nivel C y no cierra la deuda de construccion formal.

La ruta posterior quedo atendida provisionalmente por `AUD-SIM-030` y `VAL-030`, que validan `Gamma_1` contra un caso positivo acotado y distinguen esa aplicacion del bloqueo conservado por `AUD-SIM-025` y `VAL-025`.

La relacion con R4 formal quedo precisada en `AUD-001_Relacion_Gamma_Ruta1_R4_Formal.md`: `R4-CANDIDATA` puede ser evidencia local para `Gamma_1`, pero la salida no equivale a Regla R4 formal.

## Ruta formal local construida

La construccion formal local quedo materializada posteriormente en `AUD-001_Gamma_Formal_Local.md`.

Resultado: `GAMMA-FORMAL-AUD-001` define `Gamma` como operador parcial local de generalizacion controlada, con paquetes de evidencia, contexto, testigo, bien formacion, salidas seguras y teoremas locales de conservacion de permiso y trazabilidad.

La segunda prueba positiva de `Gamma_1` quedo registrada en `AUD-SIM-031` y `VAL-031`, usando `REPORT_LAYER` / `DO_CHECK_REPORT` como evidencia fuera de `R4-CANDIDATA`.

Esta construccion fue auditada en `AUD-001_Auditoria_R4_Gamma_Formal_Local.md` y aceptada localmente por `AUD-001_Decision_Estatus_R4_Gamma_Formal_Local.md` (`D-2026-07-03-010`).

## Veredicto

La ruta de `Gamma` formal local dentro de `AUD-001` queda construida. Permanece abierta cualquier promocion, exportacion, canonizacion, implementacion ejecutable o prueba fuera de `AUD-001`.
