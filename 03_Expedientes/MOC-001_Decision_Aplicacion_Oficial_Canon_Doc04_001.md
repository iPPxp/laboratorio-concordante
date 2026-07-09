# MOC-001 - Decision de aplicacion oficial Canon/Documento 04

Decision: `D-2026-07-09-005`.

Fecha: 2026-07-09.

Estado: aceptada y ejecutada.

Expediente: `MOC-001`.

Ruta: `MOC-CANON-DOC04-APPLY-001`.

## Decision

Se acepta y ejecuta la aplicacion oficial acotada de la matriz MOC sobre `M-001` y Documento 04.

La aplicacion material se limita a:

- agregar en `01_Canon/M-001_Auditoria_Arquitectonica.md` la seccion `Matriz de superficies para intervenciones de nivel sensible`;
- agregar en `02_Documentos/04_Algebra_Operacional.md` la subseccion `Entrada auxiliar por traza local de grafo`;
- conservar `01_Canon/M-000_Reglas_Fundamentales.md` sin cambio textual.

## Resultado por superficie

```text
m000_text_changed: false
m001_official_section_added: true
doc04_official_section_added: true
official_application_executed: true
official_application_scope: m001_and_doc04_only
mutating_mode_authorized: false
external_use_authorized: false
global_closure_authorized: false
report_layer_promoted: false
r4_gamma_global_export_authorized: false
nivel_c_modified: false
h_xi_admitted: false
psi_canonized: false
regulated_domain_authorized: false
```

## Dictamen

`M-000` no se modifica porque ya contiene la barrera suficiente de separacion de niveles, estatus, no promocion automatica, trazabilidad y deuda conceptual.

`M-001` incorpora una exigencia procedimental: cuando una auditoria toque superficies sensibles, debe distinguir Canon, documento oficial, expediente, prohibiciones y deuda conceptual.

Documento 04 incorpora una entrada auxiliar restringida: una traza local de grafo puede alimentar `Pi_op` como evidencia local de regla ganadora, bajo contexto, testigo, evidencia, estatus y salida segura.

## Repercusiones totales registradas

- Canon cambia solo en `M-001`, no en `M-000`.
- Documento 04 gana una entrada auxiliar compatible con `operator_trace`.
- `MOC-001` deja cerrada la deuda de aplicacion material de la matriz candidata.
- `MOC-001` no queda canonizado como modelo general.
- El vocabulario local del grafo permanece solo en expediente.
- Los casos 036-043 siguen como evidencia documental estructural, no como muestra empirica real.
- Nivel C permanece sin cambios.
- `C-001` y `C-002` permanecen sin cambios.
- `REPORT_LAYER` permanece local pre-C y no promovido.
- R4/Gamma permanecen sin exportacion general.
- Confluencia global y Equivalencia global permanecen abiertas.
- El piloto empirico real del MOC sigue no autorizado.

## Prohibiciones conservadas

Sigue prohibido:

- admitir `H-Xi`;
- canonizar `Xi`, `Phi`, `TrueSelf` o vocabulario local del grafo;
- evaluar personas reales;
- abrir uso clinico, patologico, juridico, financiero o regulado;
- publicar o redistribuir el grafo sin revision legal externa;
- cerrar Confluencia global o Equivalencia global;
- promover `REPORT_LAYER`;
- exportar R4/Gamma;
- modificar Nivel C;
- activar modo mutante.

## Verificacion requerida

La aplicacion debe quedar cubierta por:

- auditoria documental posterior;
- herramienta no mutante de verificacion `MOC-CANON-DOC04-APPLY-CHECK-001`;
- corrida general del laboratorio;
- confirmacion de `riesgo_activo: 0`;
- revision de formato.

## Siguiente ruta posible

La siguiente ruta no debe ser otra adopcion oficial inmediata. La ruta defensible posterior es:

```text
MOC-CANON-DOC04-POST-ADOPT-MONITOR-001
```

Esa ruta solo monitorea si la nueva entrada auxiliar produce ambiguedades o deudas nuevas al interactuar con AO, sin modificar Canon ni Documento 04.
