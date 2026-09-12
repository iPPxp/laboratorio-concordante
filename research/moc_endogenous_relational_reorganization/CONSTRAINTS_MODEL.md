# Modelo de restricciones

Cada \(k\in K\) registra `id, predicate, HARD|SOFT, ASSUMED|INFERRED|EXTERNAL|SELF_IMPOSED|UNKNOWN, scope, source, authority, evidence, confidence, active, time`.

Operaciones: `ADD`, `REMOVE`, `RETYPE`, `REFINE_SCOPE`, `CHANGE_STATUS`. Retirar una restricción asumida falsa puede expandir; añadir un límite real debe contraer. Ambas pueden ser reorganización si la edición es causal, justificada y estructural.

No se permite que una preferencia blanda se reetiquete como límite externo sin evidencia. Constraints duros no se promedian con ganancias. Conflictos generan `INFEASIBLE` o `UNDETERMINED` hasta regla autorizada.

Pruebas mínimas: falsa restricción \(K=\{k_{real},k_{assumed}\}\); límite real omitido; relabel correcto/incorrecto; constraint sin efecto por redundancia. KC es diff tipado con justificación, no número único.
