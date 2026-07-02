# AUD-001 - Decision de auditoria posterior a cobertura no automata de R4-CANDIDATA

Estatus: decision provisional de expediente.

ID: `AUD-POST-NO-AUT-R4-001`.

Expediente padre: `AUD-001`.

Fuente principal: `AUD-001_Sintesis_Cobertura_No_Automata_R4-CANDIDATA.md`.

## Decision

Procede una nueva auditoria limitada de `R4-CANDIDATA` posterior a la primera ronda no automata.

La auditoria procede porque `VAL-017` a `VAL-021` agregan evidencia nueva que no existia al momento de la auditoria inicial.

## Alcance autorizado

La auditoria posterior puede revisar:

- consistencia de `R4-CANDIDATA` con `M-000` y `M-001` despues de la ronda no automata
- suficiencia provisional de la cobertura `VAL-017` a `VAL-021`
- deudas bloqueantes antes de cualquier promocion formal
- si la primera ronda no automata puede considerarse cerrada provisionalmente
- si `REPORT_LAYER` debe seguir como abstraccion local o requerir especificacion separada

## Alcance no autorizado

Esta decision no autoriza:

- promover `R4-CANDIDATA` a Canon
- convertir `R4-CANDIDATA` en Regla R4 formal
- promover `R4-CANDIDATA` a documento oficial o Nivel C
- convertir `REPORT_LAYER` en especificacion oficial
- cerrar `AUD-001`
- ejecutar transformaciones materiales

## Motivo

La evidencia no automata es consistente y favorable, pero sigue siendo evidencia de expediente.

La ronda muestra robustez transversal, no demostracion general completa.

## Condiciones de la auditoria posterior

La auditoria debe:

- leer `AUD-001_R4-CANDIDATA.md`
- leer la sintesis de cobertura no automata
- leer `AUD-SIM-017` a `AUD-SIM-021`
- leer `VAL-017` a `VAL-021`
- conservar la separacion entre hipotesis, decision, documento oficial y Canon
- registrar hallazgos bloqueantes y no bloqueantes por separado

## Resultado operativo

El siguiente objetivo queda definido como:

```text
Objetivo cumplido posteriormente por AUD-001_Auditoria_Post-No-Automata_R4-CANDIDATA.md.
```

## Veredicto

Nueva auditoria: procede.

Promocion formal: no procede todavia.
