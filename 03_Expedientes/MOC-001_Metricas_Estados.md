# MOC-001 - Metricas de estados

ID: `MOC-METRIC-STATE-001`.

Estatus: metrica cualitativa ordinal provisional.

Decision asociada: `D-2026-07-05-013`.

## Proposito

Definir estados del Modelo Operativo de Concordancia combinando la salida local de `Xi_eval_MOC` con los ejes provisionales de `TCS-001`.

La metrica es cualitativa y ordinal. No es numerica universal, no mide personas y no produce diagnostico.

## Ejes minimos de lectura

- `claim_status`: el reclamo esta formulado de forma verificable.
- `authority_declared`: la autoridad o fuente esta declarada.
- `decision_present`: existe decision o estado operativo asociado.
- `permission_scoped`: los permisos y limites estan acotados.
- `evidence_traceable`: la evidencia es rastreable.
- `automation_bounded`: cualquier software asociado es no mutante o acotado.
- `debt_registered`: las deudas quedan visibles.

## Orden ordinal local

```text
bloqueo_de_concordancia / no_comparable
< discordancia_global
< friccion_operativa
< concordancia_parcial
< concordancia_local
```

Este orden solo expresa madurez local de evaluacion. No equivale a valor ontologico, verdad canonica ni calidad humana.

## Estados

### concordancia_local

Criterios de entrada:

- `Xi_eval_MOC` emite `util_acotado` o `redundante`.
- Los siete ejes minimos estan satisfechos.
- No hay deuda bloqueante ni conflicto global declarado.

Salida esperada:

- El caso puede tratarse como lectura local concordante.

Deuda asociada:

- Ninguna bloqueante; conservar trazabilidad.

Regla de desempate:

- Si hay deuda no bloqueante, degradar a `concordancia_parcial`.

### concordancia_parcial

Criterios de entrada:

- `Xi_eval_MOC` emite `util_acotado` o `redundante`.
- La autoridad, evidencia y alcance existen.
- Queda deuda no bloqueante o algun eje secundario incompleto.

Salida esperada:

- El caso puede usarse como evidencia local, con deuda explicita.

Deuda asociada:

- Completar ejes faltantes antes de usar el resultado como apoyo fuerte.

Regla de desempate:

- Si la deuda afecta evidencia, autoridad o permiso, degradar a `friccion_operativa` o `bloqueo_de_concordancia`.

### friccion_operativa

Criterios de entrada:

- `Xi_eval_MOC` emite `limitado`.
- Hay conflicto, ambiguedad de regla o restricciones incompatibles.
- La unidad minima comparable todavia existe.

Salida esperada:

- El caso no se descarta, pero requiere decision, ajuste de evidencia o refinamiento de regla.

Deuda asociada:

- Precisar conflicto, autoridad, regla de desempate o testigo.

Regla de desempate:

- Si el conflicto es global entre rutas validas, degradar a `discordancia_global`.

### discordancia_global

Criterios de entrada:

- Hay rutas locales validas que producen estados incompatibles.
- El problema excede una sola decision, un solo reporte o un solo testigo.
- Confluencia global o Equivalencia global queda invocada sin cierre.

Salida esperada:

- El caso se conserva como evidencia de problema global abierto.

Deuda asociada:

- Conservar Confluencia global y Equivalencia global como deudas abiertas.

Regla de desempate:

- Si falta evidencia o permiso, degradar a `bloqueo_de_concordancia`.

### bloqueo_de_concordancia

Criterios de entrada:

- `Xi_eval_MOC` emite `bloqueado`.
- Falta evidencia, falta alcance, falta autoridad o aparece uso prohibido.

Salida esperada:

- El caso no puede usarse como evidencia positiva.

Deuda asociada:

- Completar evidencia o abrir decision separada si el dominio esta fuera de alcance.

Regla de desempate:

- El bloqueo domina sobre cualquier estado positivo.

### no_comparable

Criterios de entrada:

- `Xi_eval_MOC` emite `no_comparable`.
- Se pierde la unidad minima comun entre `R0` y `R1`.

Salida esperada:

- La comparacion se detiene y debe abrirse nueva unidad o nuevo caso.

Deuda asociada:

- Redefinir unidad minima comparable.

Regla de desempate:

- Si ademas hay falta de evidencia o uso prohibido, clasificar como `bloqueo_de_concordancia`.

## Familias de salida

- Familia concordante: `concordancia_local`, `concordancia_parcial`.
- Familia de friccion: `friccion_operativa`, `discordancia_global`.
- Familia de seguridad: `bloqueo_de_concordancia`, `no_comparable`.

Estas familias permiten medir coincidencia parcial entre evaluadores sin forzar unanimidad.
