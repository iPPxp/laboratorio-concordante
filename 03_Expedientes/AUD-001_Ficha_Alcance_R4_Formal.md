# AUD-001 - Ficha de alcance R4 formal

Estatus: ficha de alcance futura.

Fecha: 2026-07-03.

ID: `ALC-R4-FORMAL-001`.

Expediente padre: `AUD-001`.

Objeto: Regla R4 formal.

## Proposito

Precisar el alcance de una eventual formalizacion de `R4` dentro de `AUD-001`, sin confundirla con `R4-CANDIDATA`, con una simple auditoria de cobertura o con una promesa de promocion.

## Decision de alcance

La Regla R4 formal no forma parte del cierre documental/operativo v0.

No modifica `C-001` ni `C-002`.

No depende de `REPORT_LAYER` como contrato oficial.

No convierte `R4-CANDIDATA` en Canon.

No resuelve `Gamma` por si misma.

## Alcance permitido

La ruta de R4 formal puede incluir:

- definicion local de la forma general de la regla;
- especificacion de premisas, restricciones y efecto esperado;
- relacion precisa entre `R4-CANDIDATA` y la forma general;
- criterios para distinguir hipotesis operativa, compuerta provisional y regla formal;
- pruebas o demostraciones internas sobre ejemplos ya registrados;
- delimitacion de casos no cubiertos por la candidata.

## Alcance no permitido

La ruta de R4 formal no puede:

- promover `R4-CANDIDATA` por analogia;
- usar el Registro Historico como autoridad directa;
- cambiar Canon sin proceso formal;
- absorber `REPORT_LAYER` o `DO_CHECK_REPORT`;
- resolver `Gamma` por declaracion;
- convertir una sintesis de cobertura en demostracion total;
- saltar a una formalizacion completa sin evidencia local suficiente.

## Dependencias probables

Si este frente se abre de forma real, probablemente requiera:

- revisitar `AUD-001_Invariantes_R4-AUD.md`;
- revisar `AUD-001_R4-CANDIDATA.md`;
- revisar criterios, sintesis y auditorias de `R4-CANDIDATA`;
- fijar una sintaxis local para la regla;
- decidir el nivel de generalidad aceptable;
- definir como se prueba la regla sin convertirla en mera interpretacion.

## Estado frente a v0

Mientras esas condiciones no existan, `R4` formal sigue siendo deuda futura, no requisito de completitud v0.

`AUD-001` sigue completo en version documental/operativa v0 sin R4 formal.

## Veredicto

La ruta de `R4` formal queda abierta como siguiente deuda estructural, lista para trabajo posterior si se decide abrirla.
