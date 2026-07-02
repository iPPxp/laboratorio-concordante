# AUD-001 - Decision de estatus de REPORT_LAYER Candidata

Estatus: decision provisional de expediente.

ID local: `D-2026-07-02-026`.

Expediente padre: `AUD-001`.

Objeto decidido: estatus de `AUD-001_REPORT_LAYER_Candidata.md`.

Auditoria asociada: `03_Expedientes/AUD-001_Auditoria_REPORT_LAYER_Candidata.md`.

## Decision

Se acepta `REPORT-LAYER-CAND-001` como candidata provisional de expediente dentro de `AUD-001`.

Estatus asignado:

```text
REPORT_LAYER = candidata provisional de expediente
AUD-001 = frente activo acotado
```

## Motivo

La auditoria fue favorable y no detecto hallazgos bloqueantes para estatus provisional.

La candidata separa una capa abstracta necesaria para `R4-CANDIDATA` sin promoverla a Canon, documento oficial, Nivel C ni Regla R4 formal.

## Alcance permitido

La decision permite:

- citar `REPORT_LAYER-CAND-001` dentro de `AUD-001`;
- usar la candidata para leer `R4-CANDIDATA` con una capa abstracta de reportes;
- mapear reportes locales de `AUD-001` a clases abstractas;
- preparar validaciones adicionales de `REPORT_LAYER`;
- conservar deudas de Nivel C, serializacion e implementacion como abiertas.

## Alcance no permitido

La decision no permite:

- modificar `C-001`;
- convertir `REPORT_LAYER` en especificacion oficial;
- promover `R4-CANDIDATA`;
- resolver Regla R4 formal;
- resolver `Gamma`;
- ejecutar transformaciones materiales;
- cerrar `AUD-001`.

## Deudas que permanecen

- Validar `REPORT_LAYER-CAND-001` contra una instancia no automata no reducida a nombres locales de `AUD-001`, o decidir que permanece local.
- Decidir si una ruta futura busca Nivel C o se mantiene como expediente.
- Definir serializacion solo si se busca herramienta ejecutable.
- Mantener `R4` formal y `Gamma` como problemas abiertos.

## Consecuencia operativa

Lectura posterior: el alcance local de `REPORT_LAYER-CAND-001` quedo decidido por `ALC-REPORT-LAYER-001`, el puente conceptual con `DO_CHECK_REPORT` quedo definido por `COMPAT-RL-DO-CHECK-001` y validado por `VAL-028`, y la ruta tipo RFC culmino en `C-002`.

## Veredicto

`REPORT_LAYER-CAND-001`: aceptada como candidata provisional de expediente.

Promocion formal: no procede por esta decision.
