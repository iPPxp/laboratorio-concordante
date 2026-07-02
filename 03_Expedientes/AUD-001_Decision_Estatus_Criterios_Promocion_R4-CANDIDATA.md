# AUD-001 - Decision de estatus de criterios de promocion de R4-CANDIDATA

Estatus: decision provisional de expediente.

ID: `EST-CRIT-PROM-R4-CANDIDATA-001`.

Expediente padre: `AUD-001`.

Objeto decidido: `AUD-001_Criterios_Promocion_R4-CANDIDATA.md`.

Fuente de auditoria: `AUD-001_Auditoria_Criterios_Promocion_R4-CANDIDATA.md`.

Decision posterior asociada: `AUD-001_Decision_Ruta_Siguiente_R4-CANDIDATA.md`.

## Decision

Se acepta `AUD-001_Criterios_Promocion_R4-CANDIDATA.md` como compuerta provisional de expediente.

Estatus asignado:

```text
criterios de promocion = compuerta provisional de expediente
```

## Alcance permitido

La decision permite:

- usar los criterios para evaluar rutas futuras de `R4-CANDIDATA` dentro de `AUD-001`
- exigir que cualquier ruta futura declare nivel, alcance, auditoria y decision necesaria
- bloquear discusiones de promocion que no pasen por la compuerta
- mantener `R4-CANDIDATA` como hipotesis operativa robustecida mientras no exista nueva decision

## Alcance no permitido

La decision no permite:

- promover `R4-CANDIDATA` a Canon
- convertir `R4-CANDIDATA` en Regla R4 formal
- mover `R4-CANDIDATA` a `02_Documentos`
- convertir `REPORT_LAYER` en especificacion oficial
- elegir por si misma una ruta futura
- cerrar `AUD-001`
- ejecutar transformaciones materiales

## Motivo

La auditoria de criterios fue favorable y no detecto promocion indebida.

Los criterios organizan rutas futuras y bloqueos, pero no sustituyen una decision sobre que ruta tomar.

## Consecuencia para R4-CANDIDATA

`R4-CANDIDATA` conserva el estatus de hipotesis operativa robustecida de expediente.

Cualquier cambio de estatus debe pasar por la compuerta aceptada y por una decision explicita posterior.

## Deudas que permanecen

- Decidir ruta siguiente de `R4-CANDIDATA` usando la compuerta de criterios. Cumplido posteriormente por `AUD-001_Decision_Ruta_Siguiente_R4-CANDIDATA.md`.
- Decidir si `REPORT_LAYER` requiere especificacion separada.
- Mantener abiertos `R4` formal y `Gamma` hasta definicion local.
- Auditar cualquier ruta futura contra el nivel que pretenda ocupar.

## Resultado operativo

El siguiente objetivo queda definido como:

```text
Objetivo cumplido posteriormente por AUD-001_Decision_Ruta_Siguiente_R4-CANDIDATA.md.
```

## Veredicto

Criterios de promocion: aceptados como compuerta provisional de expediente.

`R4-CANDIDATA`: permanece como hipotesis operativa robustecida.

Promocion formal: no procede por esta decision.
