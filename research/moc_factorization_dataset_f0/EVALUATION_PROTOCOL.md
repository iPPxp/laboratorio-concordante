# Protocolo de evaluación F0

## 1. Pregunta

¿La partición semántica MOC aporta predicción, transferencia, calibración o sensibilidad a intervenciones frente a controles con igual información y presupuesto?

Comparaciones mínimas:

```text
RAW_BASELINE
G-SLOTS          cinco slots genéricos
M-CBM            cinco tipos MOC sin relaciones
M-REL            tipos más relaciones
M-MERGE(i,j)     fusión de cada uno de los diez pares
M-PERM(sigma)    permutación de identidades semánticas
```

No se entrena ningún modelo en esta fase documental.

## 2. Splits

Separar por familia generadora y plantilla, no por fila aleatoria. Usar `development`, `case-holdout`, `boundary-holdout`, `intervention-holdout` y `trajectory-holdout`. Sellar splits antes de acceder a anotaciones. Casos gemelos permanecen en el mismo split salvo test contrafactual expresamente pareado.

## 3. Métricas de outcome

Según tipo: balanced accuracy/macro-F1, log loss y Brier para categorías; MAE y pinball para ordinal/count/duration; Jaccard/precision-recall para conjuntos; edit distance y event-F1 para secuencias. Reportar calibración, intervalos bootstrap por familia y coste. Primarias pre-registradas por outcome; no seleccionar retrospectivamente.

## 4. Variación independiente

Para cada frontera \(i/j\):

- `BoundaryCoverage`: pares donde anotadores sostienen cambio en i con j aproximadamente estable y viceversa;
- `ResidualAssociation`: asociación entre i/j después de controles; alta colinealidad limita identificación;
- `MatchedOutcomeContrast`: diferencia de outcome en pares matched;
- `ConditionalMutualInformation`: \(I(Y;i\mid j,C)\) y viceversa, con estimador/control de sesgo declarado;
- `InterventionResponseDivergence`: distancia entre distribuciones futuras de dos manipulaciones selladas;
- `CrossComponentLeakage`: predictibilidad de una etiqueta desde la otra; no se interpreta automáticamente como identidad.

Separación computacional requiere efectos bidireccionales o al menos asimetría estable fuera de muestra; ausencia puede significar dataset insuficiente, no equivalencia ontológica.

## 5. M-MERGE

Para los diez pares comparar M-CBM contra la representación fusionada manteniendo parámetros, información y tuning comparables. Medir:

\[
\Delta_{merge}=Perf(M\text{-}CBM)-Perf(M\text{-}MERGE(i,j)).
\]

Exigir pérdida replicable en outcome, calibración, transferencia o intervención, con corrección por multiplicidad y tamaño mínimo pre-registrado. Si no hay pérdida reproducible:

```text
COMPUTATIONAL_SEPARATION_i_j = NOT_DEMONSTRATED
```

No se redefine la semántica MOC.

## 6. M-PERM

Permutar identidades/roles preservando número de slots, capacidad y distribución marginal. Usar varias permutaciones, incluidas derangements, congeladas antes de entrenamiento. Comparar M-CBM con M-PERM en holdouts. Si permutar no perjudica, la ventaja puede provenir de cinco slots o del pipeline:

```text
MOC_TYPE_IDENTITY_VALUE = NOT_DEMONSTRATED
```

Una permutación meramente nominal que el modelo pueda deshacer no es control suficiente; debe permutar la asignación semántica entre casos/splits según protocolo sin introducir fuga.

## 7. Relaciones

M-REL sólo aporta valor si supera M-CBM con igual presupuesto y las relaciones no codifican outcomes futuros. Ablation de aristas, relación aleatoria y grafo con mismo grado controlan capacidad. Reportar ganancia por outcome y boundary.

## 8. Criterio confirmatorio fuerte

Con intervalos y replicación:

\[
M\text{-}CBM>G\text{-}SLOTS,\quad
M\text{-}REL>M\text{-}CBM,
\]

\[
M\text{-}MERGE<M\text{-}CBM,\quad
M\text{-}PERM<M\text{-}CBM.
\]

Resultados parciales deben desagregarse. No promediar outcomes incompatibles ni convertir un win aislado en validación global.

## 9. Falsadores

- G-SLOTS iguala M-CBM;
- M-REL no supera controles relacionales aleatorios;
- merges no degradan;
- permutations no degradan;
- ventaja desaparece en familias/transformaciones nuevas;
- outcomes se predicen desde artefactos de plantilla o leakage;
- variación independiente efectiva es insuficiente;
- calibración empeora aunque accuracy suba.

## 10. Replicación

Dos generaciones sintéticas independientes, autores separados, al menos tres semillas de modelo futuro y análisis congelado. F0 sólo autoriza `INSTRUMENT_SUPPORTED/PARTIALLY_SUPPORTED/NOT_SUPPORTED/INSUFFICIENT_EVIDENCE`.
