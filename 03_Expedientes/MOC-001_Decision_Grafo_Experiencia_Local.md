# MOC-001 - Decision de grafo de experiencia local

Decision: `D-2026-07-09-001`.

Fecha: 2026-07-09.

Estado: aceptada.

Expediente: `MOC-001`.

## Decision

Se acepta `MOC-EXP-GRAPH-001` como grafo local de experiencia para `MOC-001`.

La decision acepta tambien:

- `MOC-GEO-METR-LAB-001` como metrica geometrica local;
- `MOC-AO-GEO-BRIDGE-001` como puente local con `AO-001` por `operator_trace`;
- `MOC-EXP-GRAPH-CHECK-001` como herramienta no mutante de validacion de vectores/casos;
- el fixture `moc_experience_graph_cases.json` con casos 036-043 importados como evidencia documental estructural.

## Alcance

La decision permite usar el grafo para:

- validar estructura local de experiencia;
- evaluar vectores geometricos ordinales;
- producir `R_geo`;
- emitir `operator_trace`;
- crear evidencia auxiliar para `MOC/AO`.

## Limites

La decision no autoriza:

- admitir `H-Xi`;
- canonizar `Xi`, `Phi`, `TrueSelf` o la notacion `psi`;
- evaluar personas reales;
- uso clinico, patologico o regulado;
- consejo practico para casos reales;
- mantener sin cambios Canon, Documento 04, Nivel C y `C-002`;
- cerrar Confluencia global o Equivalencia global;
- promover `REPORT_LAYER`;
- exportar R4/Gamma;
- modo mutante.

## Resultado esperado

```text
resultado: ok
transformacion_permitida: false
global_closure_authorized: false
global_export_authorized: false
global_equivalence_authorized: false
global_confluence_authorized: false
report_layer_promoted: false
r4_gamma_global_export_authorized: false
```

## Deudas abiertas

- decidir si el grafo se conserva como herramienta separada o se integra posteriormente a `MOC-EVAL-001`;
- mantener la evidencia externa como auxiliar, no como autoridad;
- ampliar pruebas si se aportan nuevos casos no clinicos;
- conservar abiertas Confluencia global y Equivalencia global.
