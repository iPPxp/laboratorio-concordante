# Decision - Relacion documental MOC con C-001 y C-002

ID: `D-2026-07-06-013`.

Fecha: 2026-07-06.

Estatus: decision provisional de expediente.

## Decision

Se acepta `MOC-C001-C002-REL-001` como relacion documental controlada entre `MOC-001`, `C-001` y `C-002`.

Documento base: `03_Expedientes/MOC-001_Relacion_Documental_C001_C002.md`.

Auditoria: `03_Expedientes/MOC-001_Auditoria_Relacion_Documental_C001_C002.md`.

## Resultado

`MOC-ROUTE-012` queda ejecutada como puente documental local.

El MOC puede ser leido por el Auditor como artefacto de expediente, salida no mutante, propuesta o conjunto acotado de fuentes locales, siempre que conserve evidencia, estatus, deuda, separacion entre resultado/decision/permiso y `transformacion_permitida = false`.

## Alcance aceptado

- `C-001` aporta la frontera tecnica: entradas, salidas, prohibiciones, permiso y no autoridad autonoma.
- `C-002` aporta la secuencia operativa: leer, mapear, verificar, reportar y no transformar sin autorizacion.
- `MOC-EVAL-001` puede producir evidencia documental local, pero no sustituye el Auditor.
- `operator_trace` puede usarse como evidencia local de regla ganadora, pero no como decision.

## No cubre

No modifica `C-001`, no modifica `C-002`, no crea `C-003`, no crea Nivel C, no modifica Canon, no modifica Documento 04, no autoriza piloto real, no recluta evaluadores, no recopila datos personales, no evalua personas reales, no abre uso clinico, no admite `H-Xi`, no canoniza `Xi`, no cierra Confluencia global, no cierra Equivalencia global y no exporta R4/Gamma.

## Deuda resultante

La deuda previa de relacion con `C-001` / `C-002` queda atendida en grado documental local.

Permanecen abiertas:

- eventual especificacion tecnica futura si el MOC requiere herramienta auditora propia;
- compuerta nueva para cualquier ejecucion empirica real;
- Confluencia global;
- Equivalencia global;
- maduracion posterior de `TCS-001`;
- exportacion general de R4/Gamma.
