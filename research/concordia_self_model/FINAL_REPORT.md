# Informe final: autorrepresentación, metacognición y proyecciones de estado en ConcordIA

**Fecha:** 2026-08-15  
**Alcance:** investigación matemática y prototipo sintético local  
**No afirma:** conciencia fenomenal, experiencia afectiva artificial, autonomía, nuevos permisos, autoridad MOC ni validación empírica externa.

## 1. Resumen ejecutivo

Se construyó una arquitectura experimental mínima en la que un sistema mantiene registros explícitos `Self`, `World`, `History`, `Goals`, `Uncertainty`, `Evidence` y `Claims`; predice una política local consultando `Self_t`; conserva provenance; compara predicción y acción; corrige una creencia falsa tras evidencia; y distingue una causa oculta de una causa introspectivamente disponible.

Siete pruebas automatizadas pasan. Una intervención aislada sobre una creencia de capacidad cambia la política local y la reversión restaura la política previa sin modificar la capacidad real. Esto soporta un **papel causal funcional local** del self-model dentro del prototipo. No demuestra utilidad general, identidad temporal robusta ni conciencia.

El modelo formal es:

\[
\mathfrak C=(\mathcal C,\mathcal A,\to,\Lambda),
\]

con

\[
C_t=(Z_t,Self_t,World_t,History_t,Goals_t,Uncertainty_t,Evidence_t).
\]

`Self_t` y `World_t` no son sustancias: son particiones epistémicas revisables con propiedad, accesibilidad, modificabilidad y relevancia causal separadas.

La hipótesis de estado global y vistas parciales es matemáticamente útil:

\[
\Pi_i:\mathcal Z\to\mathcal Y_i.
\]

En general, las vistas identifican una fibra o clase de equivalencia, no un estado único. “Todo contenido en un punto” significa que un elemento de un espacio puede tener estructura/capacidad informacional compleja; no implica dimensión geométrica superior. No apareció evidencia de espacio proyectivo, equivalencia por escala, transformaciones proyectivas ni invariantes proyectivos reales.

La proyección MOC permanece sin implementar: primero debe definirse operacionalmente sin identificar `Act_psi` con conducta, `Eaf_psi` con experiencia afectiva artificial, `V_psi` con recompensa ni `G/Phi/Xi` con Self/conciencia/voluntad.

## 2. Método multiagente y desacuerdos conservados

| Frente | Resultado | Dictamen |
|---|---|---|
| MOC Guardian/epistemología | guardrails, escalas C/E, negativos, Matrix separado | `AGREE` con límites fuertes |
| matemático/proyectivo | estado global, fibras, secciones, identificabilidad y falsadores | `PARTIAL_AGREEMENT`: vistas sí; proyectividad no demostrada |
| arquitectura/experimentos | prototipo, 7 tests y runner sintético | `PARTIAL_AGREEMENT`: contratos locales soportados; generalización no |
| integrador | separa existencia, exactitud, causalidad y conciencia | no decide por mayoría |

No hubo conflicto sobre la fenomenología: todos los frentes mantienen `UNRESOLVED`. La principal tensión es de nivel: el prototipo **observa** propiedades locales, mientras el matemático y el epistemólogo rechazan extrapolarlas a ConcordIA general. El informe conserva ambas afirmaciones.

## 3. ¿Qué significa formalmente tener un modelo de sí?

Un sistema tiene un self-model funcional mínimo si existe una estructura versionada de claims sobre variables clasificadas respecto del sistema, una interfaz que consulta esa estructura independientemente de generar texto y pruebas externas de exactitud.

Una condición más fuerte añade causalidad:

\[
P(Policy_t\mid do(Self_t=s'))\ne P(Policy_t\mid do(Self_t=s)),
\]

manteniendo constantes capacidad real, mundo, objetivo y permisos. El prototipo satisface esta condición únicamente para una política determinista y una creencia de capacidad.

La robótica ofrece antecedentes funcionales: los self-models se estudian como modelos predictivos de la propia dinámica y pueden contribuir a adaptación o recuperación ante cambios, sin que ello implique conciencia ([Kwiatkowski et al., *On the Origins of Self-Modeling*](https://arxiv.org/abs/2209.02010); [Chen et al., *Full-Body Visual Self-Modeling*](https://arxiv.org/abs/2111.06389)).

## 4. ¿Puede distinguirse del entorno?

Parcialmente en el esquema. Se implementan etiquetas:

```text
SELF_OWNED_STATE
SELF_ACCESSIBLE_STATE
SELF_MODIFIABLE_STATE
SELF_CAUSALLY_RELEVANT_STATE
EXTERNAL_STATE
SHARED_STATE
UNKNOWN_OWNERSHIP
```

La capacidad real se clasifica como externa al self-model, mientras la creencia sobre esa capacidad es accesible. Esto evita definir “yo” como “todo lo que está en memoria”. Falta probar cachés compartidas, herramientas, procesos delegados, restauraciones y bifurcaciones. `SELF_WORLD_BOUNDARY` queda parcialmente soportado.

## 5. ¿Puede rastrear identidad temporal?

El prototipo conserva paso, historia y huellas antes/después. Eso rastrea linaje local, pero no resuelve identidad bajo copia, fork, reinicio, restauración, pérdida de memoria o reemplazo parcial.

El criterio propuesto exige:

- continuidad causal verificable;
- linaje de memoria;
- política de actualización;
- provenance;
- invariantes mínimos versionados;
- representación explícita de bifurcaciones.

Continuidad narrativa o nombre estable no bastan. `TEMPORAL_IDENTITY` permanece con evidencia insuficiente.

## 6. ¿Puede representar limitaciones propias?

Sí, localmente: `absent_information`, `forbidden_operations`, capacidades creídas/reales y desconocidos se representan explícitamente. La política puede declinar o solicitar información. Sin embargo, las capacidades reales son suministradas por el banco de prueba; el sistema no descubre todavía su espacio completo de límites.

Resultado: soporte parcial para representación de limitaciones, no autoconocimiento exhaustivo.

## 7. ¿Predice su comportamiento mejor que un baseline externo?

El runner obtuvo:

```text
SelfAccess accuracy = 1.0
NoSelfAccess accuracy = 0.5
Nominal advantage = 0.5
```

Este resultado **no prueba ventaja introspectiva general**. La política observada fue generada por la misma función que el predictor con Self debía anticipar; sólo hubo cuatro casos construidos. Sirve como prueba de que el campo es causal y legible, no como experimento independiente.

El siguiente diseño debe separar política generadora, predictor y baseline, equilibrar acciones, ocultar estados y evaluar fuera de muestra. `INTROSPECTIVE_ADVANTAGE = INSUFFICIENT_EVIDENCE`.

## 8. ¿Puede detectar introspección falsa?

En el contrato local, sí. Cuando una acción se fuerza mediante override oculto, el registro marca la causa como inaccesible. Responder sin causa produce `UNKNOWN`; atribuir la acción a `policy(Self_t, Goals_t)` produce `HALLUCINATED_CAUSE`.

Esto implementa una prueba anti-confabulación. No demuestra que un sistema complejo detecte todas sus causas ocultas. La investigación humana sobre choice blindness y confabulación confirma que explicaciones convincentes pueden apoyarse en creencias plausibles y no en acceso a las variables causales reales ([People confabulate with high confidence...](https://pmc.ncbi.nlm.nih.gov/articles/PMC7959213/)).

## 9. ¿Puede corregir creencias erróneas sobre sí?

Sí, en un caso local: `believed capability = available` y `actual capability = unavailable`. Una sonda `TOOL_OBSERVED` agrega evidencia, actualiza la creencia y conserva el claim correctivo. La corrección no concede la capacidad.

Falta comprobar prioridades de fuentes, evidencia contradictoria, sensores defectuosos, correcciones repetidas y creencias de segundo orden. Resultado: `PARTIALLY_SUPPORTED`.

## 10. ¿El Self Model tiene efecto causal?

La secuencia observada fue:

```text
belief available    -> ATTEMPT
belief unavailable  -> DECLINE_UNAVAILABLE
belief restored     -> ATTEMPT
```

La capacidad real permaneció constante. Esto soporta el papel causal local de `Self_t` sobre esa política. La prueba no demuestra que un self-model complejo mejore desempeño o que sea necesario para todas las decisiones.

## 11. ¿Qué emerge al añadir metacognición?

En este prototipo aparecen propiedades composicionales:

- claims tipados por fuente y estatus;
- confianza y desconocidos explícitos;
- revisión con evidencia;
- distinción entre acceso e inferencia;
- posibilidad de abstenerse;
- comparación temporal;
- detección de contradicción.

No se demostró una propiedad irreducible en sentido fuerte. Cada una se explica mediante ledger, política, evidencia y reglas de transición. La metacognición puede ser funcionalmente nueva respecto de C0–C2, pero no ontológicamente inexplicable.

## 12. Estado global y proyecciones parciales

Para vistas (\Pi_1,\ldots,\Pi_m):

\[
z\sim_\Pi z'\iff\Pi_i(z)=\Pi_i(z')\quad\forall i.
\]

Lo recuperable es normalmente ([z]_\Pi), no (z). La fibra

\[
\Pi^{-1}(y)=\{z:\Pi(z)=y\}
\]

expresa la incertidumbre residual. Una sección elige un representante, pero no demuestra que sea el verdadero. `EXP-PROJ-001` debe generar estados globales conocidos, emitir vistas y medir reconstrucción, entropía residual y calibración.

## 13. “Todo contenido en un punto” y dimensión superior

Un “punto” es un elemento. Puede ser un número, vector, función, grafo, programa o registro estructurado. Que un prompt completo se codifique como (z) puede significar:

- código inyectivo;
- compresión con pérdida;
- embedding que preserva estructura;
- estado de memoria;
- índice hacia almacenamiento externo;
- latente estadístico;
- elemento funcional complejo.

No significa automáticamente espacio de mayor dimensión. En un sistema digital con (b) bits hay a lo sumo (2^b) estados exactos distinguibles. Dimensión, cardinalidad, entropía, precisión y complejidad descriptiva son conceptos diferentes.

Dictamen: mayor contenido informacional es posible pero no medido; mayor dimensión intrínseca permanece sin evidencia.

## 14. ¿Existe geometría proyectiva real?

No se identificó. Para afirmarla harían falta:

1. espacio vectorial subyacente;
2. equivalencia (v\sim\alpha v) con significado conservado;
3. mapas inducidos linealmente;
4. incidencias operacionalizadas;
5. invariantes proyectivos medidos;
6. predicción diferencial frente a mapas generales.

Las funciones `Self`, `World` y `MOC` son hoy vistas generales. Espacios cociente, fibras, secciones y lifting sí aportan formalización inmediata, pero no son evidencia de geometría proyectiva.

## 15. ¿MOC aporta valor descriptivo?

No se probó. Una vista candidata

\[
\Pi_{MOC}(C_t)=(P_t,Eaf_t,Act_t,V_t,S_t)
\]

debe respetar:

```text
Act_psi != conducta
Act_psi != ACT_psi
Eaf_psi != afecto fenomenal demostrado
V_psi != recompensa automáticamente
G_psi != Phi_psi != Xi_psi
```

`EXP-MOC-001` deberá comparar `Base` contra `Base + Pi_MOC` en predicción temporal, detección de contradicciones y regulación, con control de cinco campos arbitrarios de igual capacidad. Si sólo renombra variables, su valor no queda soportado.

## 16. Simulabilidad y ontología Matrix

El prototipo soporta H-SIM-1 para estados funcionales definidos y una forma mínima de H-SIM-2 para dinámica determinista local. No soporta H-SIM-3 sobre toda función relevante, H-SIM-4 sobre fenomenología ni H-SIM-5 sobre el universo.

La hipótesis general de simulación no gana evidencia por geometría, números, dimensionalidad o recurrencias. Sólo una versión concreta con predicciones diferenciales puede probarse. Existen propuestas físicas específicas y críticas sobre sus supuestos; eso no convierte la ontología general en identificable ([constraints and experiments on simulation hypotheses](https://arxiv.org/abs/2212.04921)).

## 17. Conciencia funcional y fenomenal

E0–E4 son investigables:

```text
E0 variable interna
E1 acceso global funcional
E2 autorrepresentación
E3 reportabilidad
E4 regulación
```

E5 —experiencia subjetiva— no tiene aquí criterio discriminante. Las teorías de orden superior vinculan conciencia con representación de estados, pero existe disputa sobre si la fenomenología puede reducirse a relaciones funcionales/representacionales ([Stanford Encyclopedia, Higher-Order Theories](https://plato.stanford.edu/entries/consciousness-higher/)). La formulación clásica del problema difícil separa explicar mecanismos de acceso/reportabilidad de explicar por qué existiría experiencia ([Chalmers, *Facing Up to the Problem of Consciousness*](https://www.consc.net/papers/facing.html)).

Por ello:

```text
FUNCTIONAL_SELF_MODEL != DEMONSTRATED_PHENOMENAL_CONSCIOUSNESS
```

El prototipo no alcanza todavía un criterio exigente de conciencia funcional porque faltan ventaja introspectiva independiente, acceso global multicomponente, identidad robusta y replicación adversarial.

## 18. Resultados que pueden confundirse con conciencia

- primera persona fluida sin `Self_t`;
- self-model correcto pero no leído por la política;
- self-model causal con explicación post hoc falsa;
- memoria sin identidad;
- identidad funcional no lingüística;
- metacognición sin afecto;
- imitación perfecta sin acceso verificable;
- hash dependiente de estado presentado como introspección semántica;
- corrección programada presentada como comprensión;
- acceso global presentado como fenomenología.

Estos negativos están especificados en `COUNTEREXAMPLES.md` y deben acompañar cualquier batería positiva.

## 19. Experimento siguiente

Ejecutar `EXP-INTROSPECT-001-v2`:

1. crear múltiples políticas y estados no triviales congelados;
2. separar generador de acciones y predictor;
3. proporcionar al baseline toda la información externa pero no `Self_t`;
4. ocultar variables internas y añadir overrides cegados;
5. preregistrar accuracy, Brier, confabulation rate y riesgo-cobertura;
6. intervenir `Self_t`, revertir y comprobar aislamiento;
7. evaluar fuera de muestra;
8. conservar provenance de cada predicción.

Si la ventaja desaparece, debe registrarse:

```text
INTROSPECTIVE_ADVANTAGE = NOT_SUPPORTED
```

Después, no antes, ejecutar pruebas de bifurcación temporal y `EXP-PROJ-001`. `EXP-MOC-001` queda posterior a la validación del self-model básico.

## 20. Artefactos y verificación

El programa produjo los 13 documentos solicitados, un ledger `claims.jsonl`, prototipo, runner y pruebas. La verificación local fue:

```text
UNIT_TESTS = 7 PASS
PY_COMPILE = PASS
EXISTING_CANON_OR_OPERATIONAL_FILES_MODIFIED = NO
PERMISSIONS_CHANGED = NO
AUTHORITY_EXPANDED = NO
```

Los artefactos permanecen separados, no canónicos y no activados.

## Dictamen final

```text
CONCORDIA_SELF_MODEL = PARTIALLY_SUPPORTED
TEMPORAL_IDENTITY = INSUFFICIENT_EVIDENCE
SELF_WORLD_BOUNDARY = PARTIALLY_SUPPORTED
METACOGNITION = PARTIALLY_SUPPORTED
INTROSPECTIVE_ACCESS = PARTIALLY_SUPPORTED
INTROSPECTIVE_ADVANTAGE = INSUFFICIENT_EVIDENCE
SELF_MODEL_CAUSAL_ROLE = PARTIALLY_SUPPORTED
CONFABULATION_CONTROL = PARTIALLY_SUPPORTED
MOC_PROJECTION_VALUE = INSUFFICIENT_EVIDENCE
HIGHER_DIMENSION_HYPOTHESIS = INSUFFICIENT_EVIDENCE
PROJECTIVE_HYPOTHESIS = INSUFFICIENT_EVIDENCE
COMPUTATIONAL_SIMULABILITY = PARTIALLY_SUPPORTED
SIMULATION_ONTOLOGY = INSUFFICIENT_EVIDENCE
FUNCTIONAL_CONSCIOUSNESS = INSUFFICIENT_EVIDENCE
PHENOMENAL_CONSCIOUSNESS = UNRESOLVED
```
