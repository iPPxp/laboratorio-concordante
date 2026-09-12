# Leakage, fairness y métricas

## Congelación

Se congelan antes de entrenar: corpus, grupos familiares, partitions, outcomes,
transformaciones holdout, métrica primaria, margen de equivalencia, presupuesto y
semillas. Paráfrasis o versiones temporales de una misma familia no pueden cruzar
splits.

## Igualdad

Reportar por modelo:

```text
train_examples
concept_labels
target_labels
parameters
train_flops
inference_flops
hyperparameter_trials
wall_clock
```

La comparación confirmatoria se invalida si concepto, targets o búsqueda de
hiperparámetros no están igualados. También se reporta una comparación de
“coste total real”, donde la anotación MOC cuenta como coste.

## Métricas primarias

- exactitud/F1/AUROC según target;
- Brier y log loss;
- expected calibration error y cobertura selectiva;
- error de efecto de intervención;
- precisión/recall de posibilidades añadidas y retiradas;
- transferencia y gap OOD;
- curva de eficiencia de muestra y área bajo la curva;
- equivalencia drop-one/merge;
- complejidad, estabilidad temporal e inter-anotador.

No se suman arbitrariamente. Cada tarea tiene una primaria y restricciones duras.
Se usan intervalos paired bootstrap por familia, corrección por multiplicidad y
pruebas de equivalencia, no sólo `p>0.05`.

## Identificabilidad

Una descomposición no supervisada no puede asumirse identificable sin sesgos o
supervisión; ése es un falsador central, no un detalle. La literatura primaria
advierte que el disentanglement no supervisado requiere explicitar esos sesgos
([Locatello et al., 2019](https://proceedings.mlr.press/v97/locatello19a.html)).
Los concept bottlenecks permiten intervenciones sobre conceptos, pero cualquier
ventaja depende también de la calidad/coste de las etiquetas
([Koh et al., 2020](https://proceedings.mlr.press/v119/koh20a.html)). La causal
representation learning formula precisamente el problema de obtener variables de
alto nivel desde observaciones de bajo nivel
([Schölkopf et al., 2021](https://arxiv.org/abs/2102.11107)). Ninguna de estas
fuentes valida los cinco tipos MOC.

