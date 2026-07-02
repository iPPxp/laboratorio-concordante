# AUD-001 - Decision de estatus de R4-CANDIDATA

Estatus: decision provisional de expediente.

Expediente padre: `AUD-001`.

Identificador: `EST-R4-CANDIDATA-001`.

Fecha: 2026-07-01.

Objeto decidido: `03_Expedientes/AUD-001_R4-CANDIDATA.md`.

Fuente de auditoria: `03_Expedientes/AUD-001_Auditoria_R4-CANDIDATA.md`.

## Proposito

Decidir el estatus operativo de `R4-CANDIDATA` dentro de `AUD-001` despues de su auditoria contra `M-000` y `M-001`.

Esta decision no promueve `R4-CANDIDATA` a Canon, documento oficial ni Regla R4 formal.

## Fuentes locales

- `01_Canon/M-000_Reglas_Fundamentales.md`
- `01_Canon/M-001_Auditoria_Arquitectonica.md`
- `03_Expedientes/AUD-001_Invariantes_R4-AUD.md`
- `03_Expedientes/AUD-001_R4-CANDIDATA.md`
- `03_Expedientes/AUD-001_Auditoria_R4-CANDIDATA.md`
- `05_Estado_Proyecto/ESTADO_ACTUAL.md`
- `CURRENT_STATE.md`

## Decision

Se acepta `R4-CANDIDATA` como hipotesis operativa de expediente dentro de `AUD-001`.

Estatus asignado:

```text
R4-CANDIDATA = hipotesis operativa de expediente
```

## Alcance de la decision

La decision permite:

- usar `R4-CANDIDATA` como objeto de trabajo dentro de `AUD-001`
- derivar pruebas adicionales a partir de la candidata
- auditar extensiones o reformulaciones de la candidata
- compararla con objetos distintos de automatas finitos

La decision no permite:

- citar `R4-CANDIDATA` como Canon
- tratarla como Regla R4 formal
- moverla a `02_Documentos`
- usarla para modificar expedientes cerrados
- usarla como fundamento positivo fuera de `AUD-001` sin nueva decision

## Motivo

La auditoria `AUD-001_Auditoria_R4-CANDIDATA.md` fue favorable para continuar y encontro deudas no bloqueantes para decision de estatus.

Tambien registro deudas bloqueantes para cualquier promocion formal.

Por tanto, el estatus adecuado no es rechazo ni promocion, sino conservacion como hipotesis operativa de expediente.

## Deudas que permanecen

- Probar `R4-CANDIDATA` con objetos distintos de automatas finitos.
- Definir si la capa de reportes de `AUD-001` se generaliza o permanece local.
- Precisar relacion entre `R4-CANDIDATA` y la futura Regla R4 formal.
- Decidir si una version futura requiere documento oficial o nuevo expediente.
- Auditar cualquier version ampliada antes de promocion.

## Efectos sobre el repositorio

Esta decision afecta solo `AUD-001` y el estado operativo del proyecto.

No modifica Canon, documentos oficiales ni expedientes cerrados.

## Siguiente paso recomendado

Probar `R4-CANDIDATA` con un objeto no automata dentro de `AUD-001`.

Objetivo sugerido:

```text
Crear una simulacion AUD-SIM-017 con un objeto no automata para falsar o sostener R4-CANDIDATA.
```
