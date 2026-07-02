# AUD-001 - Decision de ruta siguiente de R4-CANDIDATA

Estatus: decision provisional de expediente.

ID: `RUTA-SIG-R4-CANDIDATA-001`.

Expediente padre: `AUD-001`.

Objeto decidido: ruta siguiente de `R4-CANDIDATA` despues de aceptar la compuerta de criterios.

Fuente principal: `AUD-001_Decision_Estatus_Criterios_Promocion_R4-CANDIDATA.md`.

Decision posterior asociada: `AUD-001_Decision_Pausa_Operativa_R4-CANDIDATA.md`.

## Decision

Se elige la Ruta A definida en `AUD-001_Criterios_Promocion_R4-CANDIDATA.md`:

```text
mantener R4-CANDIDATA como hipotesis operativa robustecida dentro de AUD-001
```

Esta decision no abre ruta de promocion formal.

## Rutas no elegidas

No se procede a:

- convertir `R4-CANDIDATA` en definicion provisional mas fuerte
- promover `R4-CANDIDATA` a documento oficial o Nivel C
- separar `REPORT_LAYER` como especificacion propia
- derivar una propuesta hacia Regla R4 formal
- congelar o rechazar `R4-CANDIDATA`

## Motivo

La compuerta de criterios ya fue aceptada como provisional y permite distinguir rutas sin promover la candidata.

La evidencia acumulada basta para sostener `R4-CANDIDATA` como hipotesis operativa robustecida dentro de `AUD-001`.

Las rutas de mayor nivel siguen bloqueadas o diferidas porque requieren decisiones y artefactos adicionales: alcance oficial, auditoria de Nivel C, especificacion separada de `REPORT_LAYER`, definicion formal de R4 y tratamiento de `Gamma`.

Mantener la Ruta A conserva la evidencia acumulada sin convertir una recomendacion en cambio de estatus superior.

## Alcance permitido

La decision permite:

- citar `R4-CANDIDATA` dentro de `AUD-001` como hipotesis operativa robustecida
- usar la compuerta de criterios para evaluar cualquier ruta futura
- conservar la cadena de evidencia de `R4-CANDIDATA` en el handoff
- tratar la primera ronda no automata como estable para continuidad operativa

## Alcance no permitido

La decision no permite:

- promover `R4-CANDIDATA` a Canon
- convertir `R4-CANDIDATA` en Regla R4 formal
- mover `R4-CANDIDATA` a `02_Documentos`
- convertir `REPORT_LAYER` en especificacion oficial
- cerrar `AUD-001`
- ejecutar transformaciones materiales
- tratar la ruta elegida como cierre de `R4` formal o de `Gamma`

## Evaluacion por ruta

| Ruta | Estado posterior |
| --- | --- |
| Mantener hipotesis robustecida | elegida |
| Definicion provisional de expediente | diferida |
| Documento oficial o Nivel C | bloqueada |
| Especificacion separada de `REPORT_LAYER` | diferida |
| Propuesta hacia Regla R4 formal | bloqueada |
| Congelar o rechazar | no elegida |

## Consecuencia operativa

No queda activa ninguna ruta inmediata de promocion formal.

`R4-CANDIDATA` queda estable como hipotesis operativa robustecida para el handoff de `AUD-001`.

Cualquier intento futuro de moverla de estatus debe abrir una nueva decision y pasar de nuevo por la compuerta aceptada.

## Deudas que permanecen

- Decidir si `AUD-001` queda en pausa operativa tras la ruta elegida de `R4-CANDIDATA`. Cumplido posteriormente por `AUD-001_Decision_Pausa_Operativa_R4-CANDIDATA.md`.
- Si se busca promocion formal, redactar una especificacion separada de `REPORT_LAYER`.
- Si se busca promocion formal, justificar si la primera ronda no automata basta o ampliar pruebas especificas.
- Mantener abiertos `R4` formal y `Gamma` hasta definicion local.

## Resultado operativo

Objetivo cumplido posteriormente por `AUD-001_Decision_Pausa_Operativa_R4-CANDIDATA.md`.

## Veredicto

Ruta siguiente de `R4-CANDIDATA`: decidida.

Estatus resultante: hipotesis operativa robustecida dentro de `AUD-001`.

Promocion formal: no procede por esta decision.
