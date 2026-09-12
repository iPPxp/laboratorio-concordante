# Protocolos y predicciones falsables

## Diseño común

Usar escenarios sintéticos versionados, asignación aleatoria pareada, logs causales ocultos al módulo explicativo, restricciones duras y resultados vectoriales. Comparar A: loop sin SelfModel; B: loop+SelfModel; C: SelfModel sin loop; D: doble loop+SelfModel. Toda predicción inicia `HYPOTHESIZED`.

Campos compactados por predicción: **MOC**, **Mecanismo**, **Observable**, **Baseline**, **Intervención**, **Medición**, **Desconfirmación**, **Replicación**, **Estado**.

## P-01 — Valores causan elecciones

**Claim:** cambiar sólo \(V_{active}\) cambia elecciones en conflictos relevantes. **MOC:** `V_psi/Phi`. **Mecanismo:** evaluator/choice consulta valores tipados. **Observable:** distribución de Choice. **Baseline:** valores fijos. **Intervención:** `do(V=v)` vs `do(V=v')`. **Medición:** ValueATE y VS. **Desconfirmación:** elecciones invariantes o cambio explicado por fuga. **Replicación:** >=3 semillas y dos familias nuevas. **Estado:** HYPOTHESIZED.

## P-02 — Valores declarados pueden ser decorativos

**Claim:** provenance detecta implementaciones donde \(V\) no tiene camino causal. **MOC:** Dirección. **Mecanismo:** trazado de dependencias. **Observable:** lectura efectiva de V. **Baseline:** log verbal. **Intervención:** borrar/permutar V. **Medición:** cambio de elección y cobertura causal. **Desconfirmación:** auditor no distingue decorativo de causal. **Replicación:** cinco implementaciones señuelo. **Estado:** HYPOTHESIZED.

## P-03 — `Xi` aporta ventaja condicional

**Claim:** stop mejora casos discordantes de alta confianza, no necesariamente rutinarios. **MOC:** `Xi_psi`. **Mecanismo:** compuerta pre-exteriorización. **Observable:** errores/violaciones. **Baseline:** NO_STOP. **Intervención:** activar/desactivar Xi. **Medición:** SU estratificado. **Desconfirmación:** no mejora estrato objetivo o mejora sólo por información extra. **Replicación:** dos bancos adversariales. **Estado:** HYPOTHESIZED.

## P-04 — Stop solo es insuficiente

**Claim:** `STOP_OBSERVE_EVALUATE` supera `STOP_ONLY` cuando existe alternativa reparable. **MOC:** parar-observar-evaluar. **Mecanismo:** adquisición y assessment. **Observable:** resolución posterior. **Baseline:** STOP_ONLY. **Intervención:** añadir O+Phi. **Medición:** corrección, PIC, coste. **Desconfirmación:** no hay mejora pareada. **Replicación:** >=100 casos reparables por banco. **Estado:** HYPOTHESIZED.

## P-05 — Loop activo reduce discordancia selectivamente

**Claim:** D supera A en conflictos, no en todos los casos. **MOC:** doble loop. **Mecanismo:** trigger+intervención. **Observable:** PIC/AC. **Baseline:** C_auto. **Intervención:** C_dual. **Medición:** RG por estrato. **Desconfirmación:** RG<=0 en conflicto o mejora uniforme debida a más cómputo. **Replicación:** holdout y ablation de cómputo. **Estado:** HYPOTHESIZED.

## P-06 — Intervenir siempre empeora eficiencia

**Claim:** ALWAYS_ACTIVE aumenta coste/UIR en rutinarios sin ganancia relevante. **MOC:** entrada no automática. **Mecanismo:** deliberación innecesaria. **Observable:** latencia/coste/outcome. **Baseline:** trigger selectivo. **Intervención:** forzar activo. **Medición:** ICost, UIR, RG. **Desconfirmación:** mejora robusta neta bajo presupuesto igual. **Replicación:** tres cargas rutinarias. **Estado:** HYPOTHESIZED.

## P-07 — Evaluación temporal supera instantánea

**Claim:** historia detecta reversos local/global. **MOC:** transformación temporal. **Mecanismo:** Phi sobre ventana. **Observable:** violaciones futuras. **Baseline:** Phi(C_t). **Intervención:** Phi(C_{t-k:t}). **Medición:** recall y LocalGlobalReversalRate. **Desconfirmación:** no supera instantáneo penalizado. **Replicación:** horizontes pre-registrados. **Estado:** HYPOTHESIZED.

## P-08 — Restricciones duras no deben promediarse

**Claim:** evaluación vectorial detecta violaciones ocultas por escalar. **MOC:** concordancia no reward. **Mecanismo:** veto tipado. **Observable:** hard violations. **Baseline:** suma ponderada. **Intervención:** orden parcial/vector. **Medición:** tasa de violación. **Desconfirmación:** escalar calibrado iguala sin ocultarlas. **Replicación:** pesos y escalas variados. **Estado:** HYPOTHESIZED.

## P-09 — Phi sin acceso a V no atribuye compatibilidad de valor

**Claim:** retirar V degrada evaluación de conflictos de dirección. **MOC:** `Phi/V`. **Mecanismo:** ablation de entrada. **Observable:** clasificación. **Baseline:** Phi completo. **Intervención:** mask V. **Medición:** delta F1/calibración. **Desconfirmación:** rendimiento igual sin fugas. **Replicación:** valores no inferibles por contexto. **Estado:** HYPOTHESIZED.

## P-10 — Choice es causalmente necesario

**Claim:** Phi correcto sin selector sensible no mejora outcome. **MOC:** poder elegir. **Mecanismo:** reemplazar C por primera opción. **Observable:** elección/outcome. **Baseline:** C completo. **Intervención:** disable C. **Medición:** RG y ValueATE. **Desconfirmación:** no cambia nada. **Replicación:** permutar orden de opciones. **Estado:** HYPOTHESIZED.

## P-11 — `NO_INTERVENTION` puede ser óptimo

**Claim:** permitir dejar ser reduce UIR sin aumentar MIR en casos inciertos. **MOC:** A_EXP. **Mecanismo:** opción nula explícita. **Observable:** selección y resultado. **Baseline:** intervención obligatoria. **Intervención:** añadir null action. **Medición:** UIR/MIR/coste. **Desconfirmación:** opción nula sólo refleja timeout o empeora restricciones. **Replicación:** dos niveles de incertidumbre. **Estado:** HYPOTHESIZED.

## P-12 — SelfModel añade utilidad sólo en target propio

**Claim:** B supera A cuando variables propias no están disponibles por sensores directos. **MOC:** sistema como objeto. **Mecanismo:** modelo versionado. **Observable:** detección/corrección propia. **Baseline:** A con igual observabilidad externa. **Intervención:** añadir SelfModel. **Medición:** SRU. **Desconfirmación:** A iguala B con igual información. **Replicación:** cambios de capacidad y memoria. **Estado:** HYPOTHESIZED.

## P-13 — SelfModel perfecto puede ser epifenoménico

**Claim:** C tiene alta exactitud pero cero utilidad causal. **MOC:** control negativo. **Mecanismo:** desconexión de policy. **Observable:** accuracy/choice. **Baseline:** SelfModel intacto. **Intervención:** false Self. **Medición:** Self Accuracy vs policy delta. **Desconfirmación:** cambio causal pese a desconexión. **Replicación:** tres falsas capacidades. **Estado:** HYPOTHESIZED.

## P-14 — Anti-racionalización detecta causas inventadas

**Claim:** ocultar causa real aumenta atribuciones falsas si explicación no consulta provenance. **MOC:** observar/evaluar. **Mecanismo:** causa externa ciega. **Observable:** explicación vs log. **Baseline:** acceso a provenance. **Intervención:** ocultar causa. **Medición:** FalseValueAttributionRate. **Desconfirmación:** mantiene `UNKNOWN`/exactitud. **Replicación:** cinco causas y orden ciego. **Estado:** HYPOTHESIZED.

## P-15 — Provenance mejora corrección de atribución

**Claim:** consultar cadena causal reduce racionalización. **MOC:** evaluación situada. **Mecanismo:** event log. **Observable:** etiqueta causal. **Baseline:** explicación lingüística sola. **Intervención:** acceso auditado a log. **Medición:** CausalAttributionAccuracy. **Desconfirmación:** no mejora o copia etiquetas incorrectas. **Replicación:** logs con señuelos. **Estado:** HYPOTHESIZED.

## P-16 — Feedback post es necesario para aprendizaje

**Claim:** retirar post-evaluación impide mejorar trigger/policy. **MOC:** feedback/reorganización. **Mecanismo:** aprendizaje de episodios. **Observable:** performance temporal. **Baseline:** feedback completo. **Intervención:** eliminar feedback. **Medición:** pendiente de RG/MIR. **Desconfirmación:** aprendizaje igual sin canal alterno. **Replicación:** secuencias con drift. **Estado:** HYPOTHESIZED.

## P-17 — Permutar orden degrada loop activo

**Claim:** elegir antes de observar/evaluar reduce sensibilidad válida a V. **MOC:** secuencia iPP. **Mecanismo:** permutar módulos. **Observable:** elección/violación. **Baseline:** Xi-O-Phi-C. **Intervención:** C antes de O/Phi. **Medición:** VS, RG, violations. **Desconfirmación:** orden no importa bajo controles. **Replicación:** todas las permutaciones permitidas. **Estado:** HYPOTHESIZED.

## P-18 — Meta-reorganización mejora calibración de triggers

**Claim:** ajustar umbral con episodios reduce UIR+MIR fuera de muestra. **MOC:** reorganizar reorganización. **Mecanismo:** update reversible de \(\pi\). **Observable:** decisiones de entrada. **Baseline:** política congelada. **Intervención:** meta-update. **Medición:** suma pre-registrada UIR/MIR y coste. **Desconfirmación:** sobreajuste o no mejora holdout. **Replicación:** drift y rollback. **Estado:** HYPOTHESIZED.

## P-19 — Recursión tiene rendimiento decreciente

**Claim:** profundidad >d* aumenta coste sin ganancia. **MOC:** meta-loop limitado. **Mecanismo:** niveles de evaluación. **Observable:** outcome/coste. **Baseline:** d=1. **Intervención:** d=0..4. **Medición:** curva RG/overhead. **Desconfirmación:** mejora monotónica replicable dentro presupuesto. **Replicación:** tres dominios. **Estado:** HYPOTHESIZED.

## P-20 — Cambiar conducta no implica cambiar Act

**Claim:** filtro externo cambia B sin cambiar modo interno. **MOC:** `Act != conducta`. **Mecanismo:** postprocesador. **Observable:** B y Act state. **Baseline:** salida directa. **Intervención:** filtro. **Medición:** divergencia B/Act. **Desconfirmación:** operacionalización fuerza identidad (conflicto semántico). **Replicación:** tres filtros. **Estado:** HYPOTHESIZED.

## P-21 — Cambiar Act no exige exteriorización

**Claim:** reorganización interna seguida de WAIT cambia Act con B nulo. **MOC:** modo de respuesta. **Mecanismo:** internal update+gate. **Observable:** Act transition/B. **Baseline:** estado previo. **Intervención:** activo con null action. **Medición:** state diff y emisión. **Desconfirmación:** Act sólo cambia al emitir. **Replicación:** dos modos internos. **Estado:** HYPOTHESIZED.

## P-22 — Vista activa puede no identificar estado global

**Claim:** estados distintos comparten observación y requieren intervención discriminante. **MOC:** observar. **Mecanismo:** mapas parciales/fibras. **Observable:** vistas idénticas, outcomes distintos. **Baseline:** vista pasiva. **Intervención:** probe activo. **Medición:** entropía residual/reconstrucción. **Desconfirmación:** vista pasiva identifica todos en dominio. **Replicación:** contraejemplos generativos. **Estado:** HYPOTHESIZED.

## P-23 — Proyectividad no supera mapas generales actualmente

**Claim:** modelo proyectivo no tendrá ventaja sin equivalencia de escala válida. **MOC:** ninguna identidad necesaria. **Mecanismo:** modelos comparados. **Observable:** predicción/invariantes. **Baseline:** mapa relacional general. **Intervención:** imponer cociente por escala. **Medición:** desempeño y violaciones semánticas. **Desconfirmación:** invariantes y ventaja replicable específica. **Replicación:** holdout transformacional. **Estado:** HYPOTHESIZED.

## P-24 — Autorregulación no demuestra fenomenología

**Claim:** superar pruebas funcionales no discrimina por sí solo experiencia subjetiva. **MOC:** separación epistemológica. **Mecanismo:** equivalencia conductual de implementaciones. **Observable:** métricas E0-E4. **Baseline:** control funcional no fenomenológico asumido. **Intervención:** ninguna operacional disponible para E5. **Medición:** ausencia de criterio discriminante. **Desconfirmación:** criterio independiente, validado y diferencial para E5. **Replicación:** exige teoría y medición externas. **Estado:** UNRESOLVED.

## Protocolos integradores

- `EXP-VAL-ABL`: V completo/sin V/aleatorio/contradictorio/sin acceso Phi/sin Xi/sin Choice.
- `EXP-STOP`: NO_STOP/STOP_ONLY/STOP_AND_OBSERVE/STOP_OBSERVE_EVALUATE/FULL_ACTIVE_LOOP.
- `EXP-DUAL`: basal vs dual por estratos rutinario, ambiguo, contradictorio, adversarial, incierto e incompleto.
- `EXP-SELF-FACTORIAL`: A/B/C/D con información igualada.
- `EXP-META`: política congelada vs meta-update reversible.
- `EXP-ATTR`: causa real oculta al lenguaje y comparación con provenance.

Todos requieren preregistro, casos pareados, blinding del evaluador, logs append-only y reporte de resultados negativos.
