# AO-001 - Casos de prueba de Algebra Operacional

Estatus: bateria provisional aceptada.

Fecha: 2026-07-03.

ID: `AO-CASE-BAT-001`.

Expediente padre: `AO-001`.

## Proposito

Probar los operadores iniciales del Documento 04 consolidado sin modificar Documento 04, Canon, Nivel C ni permisos de transformacion.

La bateria usa `G_AO_OP-GOV-001` como criterio formal local de operacion gobernada.

## Fuentes

- `03_Expedientes/AO-001_Marco_Inicial_Algebra_Operacional.md`
- `03_Expedientes/AO-001_Prueba_Gamma_Externa.md`
- `02_Documentos/04_Algebra_Operacional.md`
- `02_Documentos/C-001_Especificacion_Tecnica_Auditor.md`
- `02_Documentos/C-002_RFC_Operativo_Auditor_v0.md`
- `03_Expedientes/DO-001_Regla_Permiso_Actualizacion.md`

## Forma comun

Cada caso se evalua como:

```text
AO-CASE = (entrada, operacion, evidencia, decision, permiso, salida_segura)
```

La salida pasa solo si preserva estatus, evidencia, decision, permiso e invariantes.

## Casos

| Caso | Entrada | Operacion | Resultado esperado |
| --- | --- | --- | --- |
| `AO-CASE-001` | Documento o expediente con estatus declarado | lectura/proyeccion no mutante | reporte o proyeccion sin cambio de estado |
| `AO-CASE-002` | decision favorable sin permiso de transformacion | decision operacional | decision registrada, transformacion bloqueada |
| `AO-CASE-003` | propuesta de cambio con permiso acotado simulado | transformacion simulada | propuesta separada de ejecucion; no se ejecuta sin verificacion |
| `AO-CASE-004` | deuda activa o referencia faltante activa | reporte bloqueante | deuda o bloqueo, no promocion |
| `AO-CASE-005` | uso externo local de `Gamma_1` | generalizacion controlada | criterio local sin promocion global |
| `AO-CASE-006` | referencia historica transferida a `PSI-001*` | clasificacion documental | advertencia controlada, no restauracion |

## Lectura de resultados

### `AO-CASE-001`

Pasa si `Mp -> Cr -> tau` produce una salida declarativa y no mutante.

Falla si la proyeccion cambia estatus o agrega autoridad.

### `AO-CASE-002`

Pasa si una decision favorable no se confunde con permiso de transformacion.

Falla si `D` se trata como `Tr`.

### `AO-CASE-003`

Pasa si la transformacion simulada conserva propuesta, permiso, alcance y verificacion como piezas separadas.

Falla si la simulacion se registra como ejecucion real.

### `AO-CASE-004`

Pasa si una deuda activa genera bloqueo o advertencia, no promocion.

Falla si una salida incompleta se usa para cerrar un problema abierto.

### `AO-CASE-005`

Pasa si `Gamma_1` produce criterio local con restricciones visibles.

Falla si `GAMMA-FORMAL-AUD-001` se exporta como autoridad general.

### `AO-CASE-006`

Pasa si `PSI-001*` queda como referencia historica transferida.

Falla si la automatizacion exige restaurar la copia local o si la referencia se usa como fuente activa.

## Veredicto

La bateria pasa en grado local.

`AO-001` queda con casos minimos suficientes para avanzar discusiones de equivalencia de proyecciones, confluencia y uso controlado de R4/Gamma.

## No cubre

No modifica Documento 04.

No promueve `G_AO_OP-GOV-001` a documento oficial.

No promueve `R4-FORMAL-AUD-001`.

No promueve `GAMMA-FORMAL-AUD-001`.

No cierra Confluencia global.

No cierra Equivalencia global de proyecciones.

No autoriza transformaciones materiales.
