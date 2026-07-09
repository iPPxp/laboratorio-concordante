# MOC-001 - Decision de compuerta de incorporacion Canon/Documento 04

Decision: `D-2026-07-09-004`.

Fecha: 2026-07-09.

Estado: aceptada.

Expediente: `MOC-001`.

Ruta: `MOC-CANON-DOC04-ADOPT-GATE-001`.

## Decision

Se acepta la compuerta `MOC-CANON-DOC04-ADOPT-GATE-001`.

La salida aceptada es:

```text
lista_para_aplicacion_posterior
```

Esta decision no ejecuta edicion oficial de Canon ni Documento 04. No autoriza edicion automatica ni modo mutante.

## Resultado por superficie

```text
m000_adoption_recommended: false
m001_adoption_recommended: true
doc04_adoption_recommended: true
official_file_edit_executed: false
official_edit_requires_explicit_apply_step: true
mutating_mode_authorized: false
external_use_authorized: false
global_closure_authorized: false
```

## Dictamen

`M-000` no debe recibir cambio textual en esta fase.

`M-001` queda listo para aplicacion posterior de una seccion de matriz de superficies para intervenciones de nivel sensible.

Documento 04 queda listo para aplicacion posterior de una subseccion de entrada auxiliar por traza local de grafo.

El grafo completo, la notacion `psi`, las metricas y los casos 036-043 permanecen solo en expediente.

## Prohibiciones conservadas

Sigue prohibido:

- admitir `H-Xi`;
- canonizar `Xi`, `Phi`, `TrueSelf` o `psi`;
- evaluar personas reales;
- abrir uso clinico o regulado;
- cerrar Confluencia global o Equivalencia global;
- promover `REPORT_LAYER`;
- exportar R4/Gamma;
- modificar Nivel C;
- activar modo mutante;
- publicar o redistribuir sin revision legal externa.

## Siguiente ruta posible

Si se decide aplicar la incorporacion oficial, la siguiente ruta es:

```text
MOC-CANON-DOC04-APPLY-001
```

Esa ruta debe editar archivos oficiales de forma acotada, registrar verificacion posterior y confirmar `riesgo_activo: 0`.
