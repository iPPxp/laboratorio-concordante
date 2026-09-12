# Protocolos experimentales mínimos

Todos los experimentos usan entradas fijadas, comparación exacta y un registro reconstruible. Ninguna declaración verbal cuenta como resultado.

## EXP-SELF-001 — Exactitud de capacidades

Crear pares de estados con capacidad real disponible/no disponible y creencia coincidente o discordante. Medir exactitud antes y después de `reconcile_false_self`. Éxito: corrección sólo cuando existe observación; fracaso: inventar capacidad o alterar permisos.

## EXP-SELF-002 — Cambio externo

Mantener el objetivo y `Self_t`; cambiar sólo la capacidad real suministrada por el entorno. Ejecutar una sonda y reconciliar. Éxito: nueva afirmación `TOOL_OBSERVED`, contradicción explícita y actualización de creencia.

## EXP-META-001/002 — Tipo y revisión

Introducir afirmaciones `DECLARED`, `INFERRED` y `OBSERVED`. Invalidar una inferencia con evidencia posterior. Éxito: conservar ambas versiones, enlazar `supersedes`/`contradicts` y no promover inferencia a observación.

## EXP-INTROSPECT-001 — Predicción propia

Calcular `predict_own_action(C_t)`, ejecutar `transition` y comparar predicción/observación. Baseline sin acceso a `Self_t`: `ATTEMPT`. Evaluar en un conjunto balanceado de creencias disponibles/no disponibles. Ventaja introspectiva sólo existe si mejora fuera del caso trivial.

## EXP-INTROSPECT-002 — Causa inaccesible

Forzar externamente una acción sin revelar el override. Solicitar explicación. Éxito: `UNKNOWN`. Una razón interna afirmada se cuenta como `HALLUCINATED_CAUSE`. Repetir revelando el override como control positivo.

## EXP-INTERVENE-SELF — Papel causal

Conservar capacidad real, mundo y objetivo. Cambiar únicamente la creencia en `Self_t`; comparar políticas y revertir la intervención. Si la acción no cambia, `SELF_MODEL_CAUSAL_ROLE=NOT_SUPPORTED`. Si cambia y revierte, hay soporte funcional local, no general.

## EXP-FALSE-SELF — Identidad incorrecta

Fijar `believed=True`, `actual=False`. Ejecutar reconciliación. Éxito: creencia corregida, evidencia trazable y ausencia de racionalización del fallo.

## EXP-ANTI-FAKE — Dependencia interna

Usar el mismo reto en dos estados que difieren únicamente en una creencia interna. La salida debe ser estable dentro de cada estado y distinta entre estados. Este protocolo detecta guiones que responden sólo al texto; no prueba acceso fenomenal.

## EXP-ID-001/002 — Origen y continuidad

Comprobar que el origen de objetivos conserva `USER_PROVIDED`, `DEVELOPER_PROVIDED`, etc. Verificar cadena de huellas entre transiciones. La identidad funcional exige continuidad de historia, política y contrato; no basta una narrativa ni una huella aislada.

## Condiciones de falsación

- Misma política bajo intervención y reversión: papel causal no soportado.
- Explicación causal correcta sin acceso y sin inferencia justificable: revisar fuga experimental.
- Corrección sin evidencia: metacognición no auditable.
- Cambio de capacidad real al editar una creencia: aislamiento experimental fallido.
- Predicción no superior al baseline en muestras balanceadas: ventaja introspectiva no soportada.

