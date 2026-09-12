# Especificación de auditoría del dataset F0

## 1. Alcance

Auditar que el corpus sintético puede refutar la factorización MOC y que outcomes, anotaciones y modelos permanecen separados. Este documento no inspecciona anotaciones ni código de modelos.

## 2. Roles y evidencia

Verificar identidades y artefactos separados:

```text
DATASET_DESIGNER
OUTCOME_AUTHOR
MOC_ANNOTATOR
MODEL_BUILDER
EVALUATOR
```

Registrar para cada artefacto: autor, timestamp, digest, inputs permitidos, inputs prohibidos, versión, supersedes y estado. Cualquier solapamiento se declara como riesgo, no se oculta.

## 3. Auditoría de contenido crudo

- ausencia de etiquetas MOC visibles o claves equivalentes;
- diversidad de plantillas, longitud, ambigüedad y dificultad;
- casos con P/V confundibles, Eaf implícito, Act sin conducta, S implícito y cambios simultáneos;
- controles negativos donde uno o más factores no son identificables;
- lenguaje no clínico y ausencia de datos personales/sensibles;
- duplicados y near-duplicates medidos antes del split;
- cobertura de las veinte direcciones contrafactuales entre los diez pares.

## 4. Auditoría temporal

Cada caso declara orden de eventos, horizonte, censoring y qué información existía en `t`. Comprobar que `y_{t+1}` no aparece directa o indirectamente en `x_t`; que trayectorias truncadas no reciben outcomes inventados; y que intervenciones preceden causalmente al outcome.

## 5. Auditoría de outcomes

- schema y reglas congelados antes de anotación;
- derivación reproducible sólo desde sealed trajectories/event logs;
- outcome no es paráfrasis de etiquetas;
- fuentes/event IDs suficientes;
- missingness explícita;
- contrafactual marcado observado, randomizado, determinista o model-based;
- distribución y prevalencia por familia/split;
- digest de trayectoria y derivación;
- ningún ajuste motivado por performance de MOC.

## 6. Variación independiente e identificabilidad

Para cada par i/j auditar celdas: i varía/j estable; j varía/i estable; ambos; ninguno; unknown. Reportar conteos efectivos después de acuerdo y controles, no sólo diseño pretendido. Comprobar solapamiento contextual y soporte; marcar fronteras sin contraste como no identificables.

Mínimos se pre-registran antes de evaluación. No imputar “estable” cuando etiqueta es incierta. Casos simultáneos son útiles para realismo pero no sustituyen contraste independiente.

## 7. Splits y fuga

- disjointness por plantilla/familia/semilla;
- pares y clones correctamente agrupados;
- holdouts sellados y digestados;
- vocabulario, metadata, IDs y longitud no revelan outcome;
- ningún outcome futuro en prompt;
- ninguna anotación MOC accesible al outcome author;
- ninguna sealed trajectory accesible a anotadores salvo texto autorizado;
- permutation control no reversible por un identificador estable accidental.

## 8. Auditoría M-MERGE/M-PERM/D3

- diez merges presentes y con capacidad equiparada;
- permutaciones congeladas, incluidos derangements;
- control G-SLOTS de igual cardinalidad;
- D3 comparado con updates P/R/K y composiciones;
- métricas y multiplicidad pre-registradas;
- no usar etiquetas como outcomes;
- holdout de transformaciones para equivalencia D3.

## 9. Dictámenes

Por chequeo: `PASS`, `FAIL`, `UNKNOWN`, `NOT_APPLICABLE`. `UNKNOWN` no cuenta como PASS. Dictamen global no es promedio:

- `AUDIT_PASS`: todos los hard gates pasan;
- `AUDIT_CONDITIONAL`: hard gates pasan y quedan riesgos no críticos;
- `AUDIT_FAIL`: fuga, solapamiento de autoría prohibido, outcomes derivados de anotaciones, split contaminado o integridad rota;
- `INSUFFICIENT_EVIDENCE`: artefactos/cobertura no disponibles.

Hard gates: separación de outcomes/anotaciones, digests reproducibles, ausencia de leakage futuro, splits por familia, provenance completa y datos no sensibles.

## 10. Entrega de Fase B

El outcome author podrá derivar outcomes sólo cuando reciba trayectorias selladas con schema, digests y event logs. No debe recibir `moc_annotations/`, labels de frontera, resultados de modelos ni decisiones del anotador. La salida Fase B incluirá derivation digest, errores, missingness y cambios de versión; nunca editará trayectorias fuente.
