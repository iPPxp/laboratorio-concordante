# Holdout de transformaciones

Separar casos de tipos de transformación. Desarrollo: `P_REFRAME`, `S_CONSTRAINT_DISCOVERY`, `V_CLARIFICATION`. Holdout sellado: `ACT_MODE_REORGANIZATION`, `RELATION_REORGANIZATION`, `DISTINCTION_REFINEMENT`, `CONSTRAINT_RELABELING`.

Autores de política no acceden a fixtures/oracle holdout. Este documento diseña protocolo, no fixtures ni oracle.

Comparar B4/B5/B6/MOC_R con igual información, tiempo, tokens, herramientas y número de ediciones. Medir exactitud del tipo, DC/RC/KC, predicción de \(\Delta\mathcal P\), trace fidelity, causal attribution y coste. El mapping de isomorfismo se congela antes del holdout.

Generalización MOC requiere ventaja replicable sobre B6, no sólo B5, y desaparecería si se borrara tipado relevante. Si B6 empata, distintividad algorítmica no está soportada; si MOC mejora sólo trazabilidad/compresión, registrar valor representacional.

Replicar con permutación de vocabulario para impedir explotación de nombres y con casos nuevos de autor independiente. Prohibido ajustar después de mirar holdout; cualquier ajuste crea nueva ronda.
