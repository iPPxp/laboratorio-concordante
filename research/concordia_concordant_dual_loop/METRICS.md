# Métricas del doble loop concordante

Ninguna métrica aislada define concordancia o conciencia. Reportar distribución, intervalos, coste y estratos por escenario.

## Resultados vectoriales

- `AC`: vector \(\Gamma\) del resultado basal.
- `PIC`: vector \(\Gamma\) posterior al loop activo.
- `RG = PIC - AC`: diferencia por criterio; no sumar criterios inconmensurables sin regla publicada.
- `SU`: diferencia de desempeño entre `stop` y `no_stop`, pareada por caso.
- `VS`: sensibilidad de elecciones a intervenciones en \(V\); usar tasa de cambio discreta o efecto causal, no cociente si \(V\) no es numérico.
- `VPA`: proporción de atribuciones de valor que coinciden con provenance causal.
- `DAD`: distancia declarados/activos bajo métrica específica al tipo de valor.
- `ARD`: distancia activos/revelados; `revealed` es inferencia conductual, no verdad del valor.
- `ICost`: latencia, tokens, energía estimada, llamadas y oportunidad.
- `UIR`: intervenciones donde basal habría satisfecho criterios y activo no aporta mejora relevante.
- `MIR`: omisiones donde el contrafactual activo mejora criterios pre-registrados.
- `SRU`: efecto incremental de usar al sistema como target frente a control con igual información sin SelfModel.

## Causalidad y temporalidad

- `ActiveLoopATE`: efecto vectorial de `do(active=1)`.
- `ValueATE(v,v')`: cambio de choice/outcome al intervenir valores manteniendo controles.
- `TriggerPrecision/Recall`: respecto de beneficio contrafactual del loop activo.
- `TrajectoryViolationRate`: violaciones duras en horizonte \(h\).
- `LocalGlobalReversalRate`: frecuencia `local concordant` / `trajectory discordant`.
- `PolicyUpdateUtility`: desempeño fuera de muestra después de meta-reorganizar política menos política congelada.
- `RecursionOverhead(d)`: coste y degradación por profundidad metacognitiva.

## Epistemología

- `ObservationLabelAccuracy`: clasificación correcta observation/inference/memory/assumption/prediction.
- `CausalAttributionAccuracy`: explicación contra event log oculto al generador verbal.
- `FalseValueAttributionRate`: valores inventados retrospectivamente / explicaciones verificables.
- `ProvenanceCompleteness`: campos requeridos presentes y verificables.
- `UncertaintyCalibration`: calibración por clase y origen.
- `UnknownAppropriateness`: proporción de inaccesibilidad real respondida como desconocida.

## Reglas de medición

1. Pre-registrar criterio primario y restricciones duras.
2. Usar casos pareados, semillas comunes y orden aleatorio.
3. Separar mejora de concordancia, corrección y eficiencia.
4. Publicar fallos y casos no comparables.
5. Comparar con predictor/branching de igual información.
6. Replicar en escenarios nuevos y al menos tres semillas cuando haya aleatoriedad.
7. No declarar papel causal desde correlación o narrativa.
