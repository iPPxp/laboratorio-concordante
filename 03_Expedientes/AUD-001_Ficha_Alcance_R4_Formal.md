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

Precision posterior: `AUD-001_Relacion_Gamma_Ruta1_R4_Formal.md` fija que `Gamma_1` puede usar `R4-CANDIDATA` como evidencia local para producir una candidata provisional, pero esa salida no constituye Regla R4 formal.

## Alcance permitido

La ruta de R4 formal puede incluir:

- definicion local de la forma general de la regla;
- especificacion de premisas, restricciones y efecto esperado;
- relacion precisa entre `R4-CANDIDATA` y la forma general;
- revision de `REL-GAMMA-R4-001` si se usa `Gamma_1` para preparar una candidata generalizada;
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

`AUD-001` seguia completo en version documental/operativa v0 sin R4 formal. La construccion local posterior de `R4-FORMAL-AUD-001` no modifica ese cierre v0 ni promueve documentos oficiales.

## Ruta formal local construida

La ruta formal local quedo materializada posteriormente en `AUD-001_R4_Formal_Local.md`.

Resultado: `R4-FORMAL-AUD-001` define una Regla R4 formal local sobre trazas, decision fundada, ejecucion valida, evidencia previa/posterior e invariantes verificados.

Esta construccion fue auditada en `AUD-001_Auditoria_R4_Gamma_Formal_Local.md` y aceptada localmente por `AUD-001_Decision_Estatus_R4_Gamma_Formal_Local.md` (`D-2026-07-03-010`).

La construccion no modifica Canon, no modifica `C-001` ni `C-002`, no promueve `R4` a documento oficial y no autoriza transformaciones materiales.

## Veredicto

La ruta de `R4` formal local dentro de `AUD-001` queda construida. Permanece abierta cualquier promocion, exportacion, canonizacion, implementacion ejecutable o prueba fuera de `AUD-001`.
