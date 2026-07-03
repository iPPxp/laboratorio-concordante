# AUD-001 - Ficha de alcance REPORT_LAYER pre-C

Estatus: ficha de alcance local.

Fecha: 2026-07-03.

ID: `ALC-REPORT-LAYER-002`.

Expediente padre: `AUD-001`.

Objeto: `REPORT-LAYER-CAND-001`.

## Proposito

Precisar el alcance vivo de `REPORT_LAYER` despues de:

- `ALC-REPORT-LAYER-001`;
- `COMPAT-RL-DO-CHECK-001`;
- `AUDITOR-DO-CHECK-ADAPTER-001`;
- actualizacion de `C-002` con JSON, fixtures y adaptador.

## Decision de alcance

`REPORT_LAYER` queda como capa local pre-C de `AUD-001`.

No se promueve a Nivel C propio en esta ronda.

No se abre expediente propio.

No se convierte en contrato obligatorio para otros frentes.

## Alcance permitido

`REPORT_LAYER` puede usarse para:

- nombrar la estructura abstracta de reportes dentro de `AUD-001`;
- explicar por que `C-002` puede hablar de reportes compatibles sin promover una especificacion separada;
- proyectar `DO_CHECK_REPORT` a `REPORT_ITEM` mediante adaptador no mutante;
- conservar la frontera entre reporte, recomendacion, decision, permiso y ejecucion;
- evaluar si una futura suite ejecutable necesita serializacion formal.

## Alcance no permitido

`REPORT_LAYER` no puede usarse para:

- modificar `C-001` o `C-002`;
- sustituir `OPERATOR_REPORT`;
- absorber `DO_CHECK_REPORT`;
- exigir adopcion fuera de `AUD-001`;
- habilitar `Tr_ejecucion`;
- promover `R4-CANDIDATA`;
- resolver R4 formal o `Gamma`;
- declararse Nivel C sin candidata, auditoria y decision de promocion.

## Estado frente a Nivel C

La ruta a Nivel C queda diferida.

Para reabrirla se requiere:

- demostrar uso estable fuera de `AUD-001`;
- declarar alcance exportable independiente;
- definir serializacion o contrato de datos si va a gobernar herramientas;
- auditar contra `M-000`, `M-001` y `NIVEL-C-001`;
- registrar decision de promocion con destino documental.

Mientras esas condiciones no existan, `REPORT_LAYER` permanece como vocabulario tecnico local incorporado por referencia en `C-002`.

## Deuda viva posterior

La deuda ya no es "definir si existe `REPORT_LAYER`".

La deuda viva queda acotada a:

- serializacion formal si se construye suite ejecutable completa;
- promocion a Nivel C solo si aparece uso interfrente;
- expediente propio solo si genera deudas no contenibles en `AUD-001`.

## Veredicto

`REPORT_LAYER` queda cerrado para el alcance operativo v0 del Auditor.

Permanece abierto solo como posible ruta futura de Nivel C, no como bloqueo actual.
