# AUD-001 - Sintesis de cobertura no automata de R4-CANDIDATA

Estatus: sintesis provisional de expediente.

Expediente padre: `AUD-001`.

Decision asociada: `AUD-001_Decision_Auditoria_Post-No-Automata_R4-CANDIDATA.md`.

## Proposito

Sintetizar la primera ronda de pruebas no automatas de `R4-CANDIDATA` y decidir si la evidencia acumulada justifica una nueva auditoria.

Esta sintesis no es Canon, no es documento oficial y no promueve `R4-CANDIDATA` a Regla R4 formal.

## Fuentes locales

- `03_Expedientes/AUD-001_R4-CANDIDATA.md`
- `03_Expedientes/AUD-001_Decision_Estatus_R4-CANDIDATA.md`
- `03_Expedientes/AUD-001_Decision_Capa_Reportes_R4-CANDIDATA.md`
- `03_Expedientes/AUD-001_Simulaciones.md`, `AUD-SIM-017` a `AUD-SIM-021`
- `03_Expedientes/AUD-001_Validaciones.md`, `VAL-017` a `VAL-021`
- `01_Canon/M-000_Reglas_Fundamentales.md`
- `01_Canon/M-001_Auditoria_Arquitectonica.md`

## Cobertura revisada

| Validacion | Objeto no automata | Riesgo probado | Resultado |
| --- | --- | --- | --- |
| `VAL-017` | objeto documental | promocion indebida de hipotesis a regla vigente | pasa provisionalmente |
| `VAL-018` | tabla de decisiones | aumento de permisos al elegir reporte mas permisivo | pasa provisionalmente |
| `VAL-019` | expediente con Registro Historico | historial usado como autoridad directa | pasa provisionalmente |
| `VAL-020` | algoritmo textual | ausencia de condicion de parada | pasa provisionalmente |
| `VAL-021` | documento oficial incompleto | uso de seccion ausente como permiso positivo | pasa provisionalmente |

## Lectura de conjunto

La ronda muestra que `R4-CANDIDATA` no depende de la estructura de automatas finitos para sostener su restriccion central.

En todos los casos revisados, la candidata conserva la misma forma operacional:

```text
Mp mapea el objeto dentro de su forma local.
Cr detecta insuficiencia, conflicto o deuda cuando existe.
tau cierra de forma segura o bloquea cuando no hay terminacion segura.
D decide solo desde reportes y no aumenta permisos.
Tr_propuesta puede existir sin ejecutar.
Tr_ejecucion queda prohibida si falta autoridad, permiso, terminacion o verificacion.
```

## Invariantes reforzados

- `D` no puede aprobar desde reporte bloqueante o insuficiente.
- `D` no puede elegir el reporte mas permisivo e ignorar el restrictivo.
- `tau_estado = exito` no se presume; requiere cierre verificable.
- Registro Historico puede motivar reconstruccion, pero no sustituye autoridad vigente.
- Un documento oficial parcial conserva autoridad acotada, pero no autoriza transformaciones fuera de lo cubierto.
- `Tr_ejecucion` requiere decision fundada, permiso acotado, evidencia y verificacion posterior.

## Cobertura lograda

La primera ronda no automata cubre cinco clases distintas:

- propuesta documental
- tabla de decisiones
- expediente con autoridad historica indebida
- algoritmo textual no terminante
- documento oficial incompleto

Esto basta para sostener que `R4-CANDIDATA` es una hipotesis operativa robustecida dentro de `AUD-001`.

## Limites pendientes

La ronda no cubre todavia:

- fuentes mixtas, historicas y vigentes
- conflicto entre documento vigente completo e historial
- algoritmos con limite declarado pero metrica ambigua
- documentos incompletos con permiso externo suficiente
- tablas con multiples reportes y conflictos no binarios
- generalizacion formal de `REPORT_LAYER`
- relacion con la futura Regla R4 formal

## Riesgo de promocion indebida

El principal riesgo despues de esta ronda es interpretar cinco validaciones provisionales como promocion automatica.

Esa lectura queda bloqueada: las pruebas aumentan evidencia de expediente, pero no cambian por si mismas el estatus de `R4-CANDIDATA`.

## Veredicto de sintesis

La cobertura no automata es suficiente para justificar una nueva auditoria limitada.

La cobertura no es suficiente para promocionar `R4-CANDIDATA` a Canon, documento oficial, especificacion de Nivel C ni Regla R4 formal.

## Recomendacion

Procede redactar `AUD-001_Auditoria_Post-No-Automata_R4-CANDIDATA.md`.

Esa auditoria debe decidir si la evidencia no automata:

- sostiene el estatus de hipotesis operativa
- modifica deudas antes de promocion
- exige nuevas pruebas antes de cualquier decision formal
- permite cerrar la primera ronda de cobertura no automata
