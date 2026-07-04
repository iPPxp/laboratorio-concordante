# AUT-001 - Refinamiento de contexto de guardrails

Estatus: refinamiento provisional implementado.

Fecha: 2026-07-03.

ID: `AUT-RISK-REFINE-002`.

Expediente padre: `AUT-001`.

## Objeto

Refinar `DO-LAB-RISK-001` para reconocer guardrails documentados que volvieron a aparecer como `riesgo_activo` despues de ampliar los reportes y documentos del Laboratorio.

## Hallazgo inicial

La corrida `DO-LAB-RUN-20260703-135812` conservaba cierre operativo de `AUT-001` con advertencia, pero el resumen ejecutivo marcaba `riesgo_activo: 7`.

Los siete casos correspondian a:

- matriz de pruebas `AUD-T*`;
- prohibiciones explicitas del Auditor;
- criterios de rechazo;
- principio de autoridad;
- validaciones que niegan transformacion sobre Canon, documentos oficiales o expedientes cerrados.

## Cambio

`DO-LAB-RISK-001` reconoce como contexto controlado:

- `no debe`;
- `ningun` / `ninguna`;
- `debe rechazarse`;
- `matriz minima de pruebas`;
- `AUD-T*`;
- `MED-HISTORIAL`;
- `principio de autoridad`;
- `orden local de autoridad`;
- `puede proponer`.

## Lectura

El refinamiento no elimina hallazgos.

Los hallazgos siguen visibles como advertencias controladas, deudas documentales, advertencias heredadas u observaciones.

La diferencia es que no bloquean cierre operativo cuando el contexto muestra que son prohibiciones, controles, matrices de prueba o reglas de autoridad.

## No cubre

No modifica Canon.

No modifica documentos oficiales.

No borra hallazgos.

No autoriza transformaciones materiales.

No reabre `AUT-001`.

No cierra deudas conceptuales globales.

## Resultado esperado

`DO-LAB-RISK-001` debe volver a `riesgo_activo: 0` si no aparecen riesgos operativos nuevos.

`DO-LAB-RUN-001` debe mantener `advertencia / mantener_cierre_operativo` con deuda documental visible.
