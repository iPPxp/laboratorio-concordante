# MOC-001 - Decision de matriz de impacto Canon/Documento 04

Decision: `D-2026-07-09-003`.

Fecha: 2026-07-09.

Estado: aceptada.

Expediente: `MOC-001`.

Ruta: `MOC-CANON-DOC04-IMPACT-001`.

## Decision

Se acepta `MOC-CANON-DOC04-IMPACT-001` como matriz no mutante de impacto y propuesta candidata.

La decision no autoriza edicion oficial de Canon ni Documento 04.

## Salida aceptada

```text
impact_matrix_accepted: true
candidate_proposal_prepared: true
m000_text_change_recommended: false
m001_candidate_amendment_recommended: true
doc04_candidate_amendment_recommended: true
official_canon_edit_authorized: false
official_doc04_edit_authorized: false
mutating_mode_authorized: false
external_use_authorized: false
```

## Dictamen por superficie

### `M-000`

No se recomienda cambio textual. `M-000` funciona como limite rector:

- separacion de niveles;
- estatus obligatorio;
- no promocion automatica;
- trazabilidad minima;
- deuda conceptual.

### `M-001`

Queda preparada una propuesta candidata para agregar una matriz de superficies en auditorias de nivel sensible.

La propuesta no queda incorporada oficialmente.

### Documento 04

Queda preparada una propuesta candidata para entrada auxiliar por `operator_trace` de grafo local.

La propuesta no queda incorporada oficialmente.

### Expediente

Permanecen solo en `MOC-001`:

- notacion `psi`;
- grafo completo;
- metricas geometricas locales;
- casos 036-043;
- puente `MOC/AO` detallado;
- fuente externa como evidencia documental estructural.

### Prohibido

Sigue prohibido:

- admitir `H-Xi`;
- canonizar `Xi`, `Phi`, `TrueSelf` o `psi`;
- evaluar personas reales;
- abrir uso clinico o regulado;
- cerrar Confluencia global o Equivalencia global;
- promover `REPORT_LAYER`;
- exportar R4/Gamma;
- modificar Nivel C;
- activar modo mutante.

## Siguiente ruta defensible

La siguiente ruta, si se decide avanzar, es una compuerta de incorporacion posterior:

```text
MOC-CANON-DOC04-ADOPT-GATE-001
```

Esa compuerta deberia decidir separadamente si se incorpora texto a `M-001`, a Documento 04, a ambos o a ninguno.
