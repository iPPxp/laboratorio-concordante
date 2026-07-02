# AUD-001 - Decision de siguiente fase de R4-CANDIDATA

Estatus: decision provisional de expediente.

ID: `SIG-FASE-R4-CANDIDATA-001`.

Expediente padre: `AUD-001`.

Fuente principal: `AUD-001_Decision_Cierre_Ronda_No_Automata_R4-CANDIDATA.md`.

## Decision

La siguiente fase de `R4-CANDIDATA` dentro de `AUD-001` sera una fase de criterios de promocion futura y frontera formal.

Nombre operativo de la fase:

```text
Fase de criterios de promocion y frontera formal de R4-CANDIDATA
```

## Estatus resultante

`R4-CANDIDATA` conserva el estatus de hipotesis operativa robustecida de expediente.

No cambia a definicion provisional, documento oficial, Canon ni Regla R4 formal.

## Motivo

La primera ronda no automata quedo cerrada provisionalmente y la auditoria posterior fue favorable para sostener la candidata dentro de `AUD-001`.

Sin embargo, la evidencia acumulada todavia no define criterios de promocion, no especifica `REPORT_LAYER` fuera de `AUD-001`, no resuelve la Regla R4 formal y no resuelve `Gamma`.

Por eso la siguiente fase no debe ser promocion, sino preparacion de criterios verificables para cualquier decision futura.

## Alcance autorizado

Esta decision autoriza:

- redactar criterios de promocion futura de `R4-CANDIDATA`
- distinguir requisitos para hipotesis robustecida, definicion provisional, documento oficial y Regla R4 formal
- identificar dependencias bloqueantes para cada estatus posible
- precisar que papel tendria `REPORT_LAYER` en una promocion futura
- preparar una decision posterior sobre si conviene promover, mantener, dividir o congelar la candidata

## Alcance no autorizado

Esta decision no autoriza:

- promover `R4-CANDIDATA` a Canon
- convertir `R4-CANDIDATA` en Regla R4 formal
- mover `R4-CANDIDATA` a `02_Documentos`
- convertir `REPORT_LAYER` en especificacion oficial
- cerrar `AUD-001`
- modificar documentos oficiales o Canon
- ejecutar transformaciones materiales

## Producto esperado

La fase comienza con el siguiente artefacto:

```text
AUD-001_Criterios_Promocion_R4-CANDIDATA.md
```

Ese artefacto debe funcionar como compuerta: antes de discutir promocion, debe quedar claro que criterios se exigen y que deudas bloquean cada ruta.

## Rutas futuras que debera distinguir

- mantener `R4-CANDIDATA` como hipotesis operativa robustecida
- convertirla en definicion provisional de expediente
- preparar una especificacion de Nivel C
- separar una especificacion futura de `REPORT_LAYER`
- derivar una propuesta hacia Regla R4 formal
- congelar la candidata si aparecen dependencias no resolubles localmente

## Deudas que permanecen

- Definir criterios de promocion futura. Cumplido posteriormente por `AUD-001_Criterios_Promocion_R4-CANDIDATA.md`.
- Decidir si `REPORT_LAYER` requiere especificacion separada.
- Precisar relacion entre `R4-CANDIDATA` y Regla R4 formal.
- Mantener abiertos `R4` formal y `Gamma` hasta definicion local.
- Decidir si una futura version requiere documento oficial, expediente separado o ambos.

## Resultado operativo

El siguiente objetivo queda definido como:

```text
Objetivo cumplido posteriormente por AUD-001_Criterios_Promocion_R4-CANDIDATA.md.
```

## Veredicto

Siguiente fase decidida: criterios de promocion y frontera formal.

`R4-CANDIDATA` permanece como hipotesis operativa robustecida de expediente.

Promocion formal: no procede por esta decision.
