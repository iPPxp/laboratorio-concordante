# AUT-001 - Refinamiento DO-LAB-RISK

Estatus: refinamiento provisional implementado.

ID: AUT-RISK-REFINE-001.

Fecha: 2026-07-02.

## Objeto

Refinar `DO-LAB-RISK-001` para distinguir riesgos activos reales de advertencias controladas por guardrails, decisiones registradas, bitacora historica o definiciones internas de checks.

## Cambios aceptados

- Se agrega la categoria `advertencia_controlada`.
- Se conservan los campos previos de cada hallazgo.
- Se agregan `context_class`, `treatment_status`, `risk_blocks_closure` y `source_context`.
- Se mantiene `transformacion_permitida: false`.
- Se mantiene visible toda advertencia; no se borra evidencia.

## Resultado del refinamiento

- Hallazgos considerados: 82.
- `riesgo_activo`: 0.
- `advertencia_controlada`: 17.
- `deuda_documental`: 18.
- `advertencia_heredada`: 47.
- `risk_blocks_closure`: false.

## Lectura

Los 17 riesgos activos previamente revisados pasan a advertencias controladas. La razon no es que desaparezcan, sino que su contexto muestra prohibicion, decision registrada, bitacora, definicion de check o regla de auditoria.

## No cubre

No cierra operativamente `AUT-001`, no confirma ejecucion directa local con `python`, no modifica Canon, no modifica documentos oficiales y no cierra ni reabre expedientes.
