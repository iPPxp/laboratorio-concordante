# AUT-002 - Cierre tecnico

ID: `AUT-002-CLOSE-TECH-001`.

Fecha: 2026-07-06.

Estatus: propuesta de cierre tecnico.

Expediente: `AUT-002`.

## Base aceptada

`AUT-002` fue aceptado por `D-2026-07-03-015` para tratar referencias historicas transferidas a `PSI-001*` sin restaurar la copia local ni reabrir `AUT-001`.

La regla aceptada distingue:

- referencia historica transferida;
- deuda/advertencia controlada;
- uso activo de historial como autoridad, que sigue bloqueando.

## Criterio de cierre

El expediente puede cerrarse porque:

- la clasificacion `referencia_historica_transferida` ya existe;
- `DO-CHECK-MIN-001` y `DO-CHECK-MED-001` la reconocen;
- el estado vigente conserva `PSI-001` fuera del Laboratorio;
- la corrida local mantiene `riesgo_activo: 0`;
- no hay evidencia de dependencia activa nueva hacia `PSI-001`.

## Deudas trasladadas

La unica deuda restante es condicional:

- si una ruta futura necesita contenido sustantivo de psicologia, debe abrir decision puente hacia `Psicologia Concordante`.

Esa deuda no requiere mantener abierto `AUT-002`.

## No cubre

No reabre `AUT-001`, no restaura `03_Expedientes/PSI-001*`, no reabre `PSI-001`, no abre frente clinico, no convierte Registro Historico en autoridad normativa, no modifica Canon, no modifica documentos oficiales y no autoriza transformaciones materiales.

## Resultado

Procede cierre tecnico de `AUT-002`.
