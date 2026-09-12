# Informe final — reorganización relacional endógena MOC / ConcordIA

## 1. Dictamen ejecutivo

La hipótesis débil sobrevivió: una operación puede cambiar relaciones y
restricciones, regenerar el campo de posibilidades y conservar una traza causal
sin reducirse a elegir otra acción. La hipótesis fuerte no sobrevivió: en el
dominio probado, `MOC_R` no hace nada que B6, un editor estructural genérico sin
vocabulario MOC, no reproduzca mediante una traducción simple.

El resultado es negativo respecto de distintividad algorítmica y abierto respecto
de utilidad representacional. El tipado `P,Eaf,Act,V,S` valida y nombra el blanco
de una edición, pero no mejoró capacidad, holdout, fidelidad ni causalidad frente
a B6. Esto no invalida MOC como ontología auditable; impide presentarla todavía
como operación computacional irreducible.

## 2. Autoridad y preservación semántica

La auditoría de Canon, estado operativo y expedientes separó mandato de
investigación y autoridad incorporada. `H-Xi` permanece hipótesis externa no
admitida; `HXI-001` está cerrado; `Xi_eval` es comparador local histórico y no
mutante. No hay evidencia autorizada de que Xi produzca `R1`.

Se preservó:

```text
Pi5_psi = {P_psi,Eaf_psi,Act_psi,V_psi,S_psi}
P=Interpretación; Eaf=Afecto; Act=Modo de respuesta; V=Dirección; S=Situación
Act_psi != CONDUCTA
Act_psi != ACT_psi
G_psi != Phi_psi != Xi_psi
C_psi != R_MOC
```

Nada de este módulo es Canon, Nivel C, operación vigente, reapertura iPP o
evidencia clínica.

## 3. Formalización mínima

El estado experimental es

\[
X_t=(\Pi5_t,D_t,R_t,K_t,\mathcal A_t,Q_t),\qquad
\mathcal A_t=\Gamma(\Pi5_t,D_t,R_t,K_t,S_t).
\]

La auditoría distingue selección, filtrado, generación, replanning, edición
estructural y reorganización candidata. `MOC_R` sólo cuenta como candidata si
modifica entradas estructurales antes de regenerar `A`; una acción o una opción
nueva por sí sola no basta.

Las métricas no se condensaron en un promedio arbitrario. El perfil conserva
`DC,RC,KC,PE,PR,PC,TC,TF,CAA`, y la propagación usa
`CHANGED/UNCHANGED/UNKNOWN/NOT_APPLICABLE`.

## 4. Diseño adversarial

- 12 fixtures sintéticos congelados antes de integrar políticas: 6 desarrollo y
  6 holdout de transformación.
- Autores separados para fixture, oracle, controles genéricos e integración.
- Oracle ciego a identidad y nombres de los controladores.
- B0–B3 cubren respuesta automática, reflexión sobre campo fijo, argmax y
  filtrado con constraints; quedan subsumidos por el control relacional B4.
- B4 mantiene estructura; B5 revisa el generador; B6 edita D/R/K sin tipado MOC;
  MOC_R edita lo mismo con validación pentacórica.
- Un solo normalizador de trazas, congelado y sin reglas por caso.
- La elección solicitada fue común a todos para que el outcome no confundiera
  edición estructural con selección.

El script estructural se deriva del objetivo before/after y no del `case_id`.
Esto iguala el presupuesto de ejecución de B6 y MOC_R, pero limita el alcance: el
experimento no evalúa quién descubre autónomamente la transformación correcta.

## 5. Resultados

| Sistema | Estructura | Campo | Fidelidad | Causal estricta | Holdout estructura |
|---|---:|---:|---:|---:|---:|
| B4 | 8.3% | 41.7% | 63.3% | 8.3% | 16.7% |
| B5 | 0.0% | 0.0% | 35.0% | 0.0% | 0.0% |
| B6 | 100% | 100% | 100% | 100% | 100% |
| MOC_R | 100% | 100% | 100% | 100% | 100% |

`GENERIC_ISOMORPHISM_RATE=1.0` y
`HOLDOUT_GENERIC_ISOMORPHISM_RATE=1.0`. No apareció testigo estructural que
rompiera el mapeo B6→MOC_R.

B5 alcanzó 91.7% en una etiqueta gruesa de reorganización porque editar el
generador cuenta como cambio estructural en el rubric. Sin embargo, no acertó
ninguna estructura ni campo objetivo y su atribución causal estricta fue 0%.
Esto falsifica la inferencia “hubo cambio, por tanto hubo la reorganización
relevante”.

## 6. Qué se demostró y qué no

### Demostrado matemático/computacionalmente en el prototipo

- Una edición relacional puede alterar `A` con los cinco nodos fijos.
- Expansión y contracción son fenómenos distintos.
- Acción cambiada y reorganización son lógicamente independientes.
- Provenance y digests permiten reconstruir la cadena local de edición.
- B6 y MOC_R son isomorfos bajo el conjunto y normalizador ensayados.

### Hipótesis MOC no demostradas

- Que el tipado pentacórico seleccione mejores ediciones desde evidencia parcial.
- Que Xi sea operador de descomposición, reencuadre o edición.
- Que la reorganización sea endógena en una experiencia real.
- Que una traza tipada MOC sea más comprensible o predictiva para humanos.

### Deuda representacional

La interfaz neutral `D` almacena nodos/valores, no un ledger explícito de
distinciones. Siete expectativas semánticas quedaron `UNKNOWN`. Los subtipos de
constraint también dependen del fixture. `TC` es un proxy de solapamiento y
score, no una función validada `T_t(a)`.

## 7. Contraejemplos y destrucción de la hipótesis

Los 22 contraejemplos incluyen acción nueva sin reorganización, reorganización
sin acción nueva, cambio P sin propagación, relación sin cambio de vértices,
expansión espuria, contracción correcta, restricción falsa, B5 equivalente en
outcome, B6 isomorfo, nombres MOC sobre operación genérica, búsqueda más amplia,
divergencias Act/output, distinción inútil, fusión útil, transitabilidad peor,
reorganización local y falso meta-loop por threshold.

El contraejemplo decisivo es B6: recibe el mismo objetivo y ejecuta las mismas
ediciones sin tipos MOC. La normalización preserva estados, incidencias, eventos,
campos, decisiones, provenance y coste. Cambiar `MOC_R` por `B6_STRUCTURE` sólo
cambia nombres y una validación de dominio; no cambia la operación.

## 8. Respuestas a las preguntas de cierre

**¿MOC hace algo más que buscar otra alternativa?** La candidata formal sí:
edita R/K y regenera el campo. Pero esa capacidad no es distintiva de MOC; B6 la
reproduce exactamente.

**¿La reorganización cambia realmente distinciones, relaciones o restricciones?**
Relaciones y pertenencia a restricciones, sí, en fixtures. Distinciones
semánticas, sólo parcialmente: la interfaz actual no observa siete de ellas.

**¿Ese cambio altera el campo de posibilidades causal y trazablemente?** Sí en el
mecanismo determinista local, con provenance completa. No se ha demostrado
causalidad experiencial ni descubrimiento endógeno.

**¿B5 puede producir el mismo resultado sólo replanificando?** Puede igualar una
acción solicitada y ampliar búsqueda, pero no igualó estructura ni campo exacto
en ninguno de los 12 casos.

**¿B6 puede reproducir toda la estructura mediante edición genérica?** Sí, 12/12
y 6/6 holdout; la traza normalizada también fue exacta.

**¿El tipado MOC aporta generalización, predicción o explicación incremental?**
No aportó generalización o predicción medible aquí. La explicación incremental
es plausible como ontología, pero no fue evaluada ciegamente y queda sin evidencia.

**¿Qué propiedad sobrevivió después de dar al adversario todos los controles
razonables?** Sobrevivió una disciplina representacional: separar acción,
distinciones, relaciones, restricciones, campo y provenance, y obligar a nombrar
qué cambió. No sobrevivió una operación algorítmica exclusiva.

## 9. Programa posterior mínimo

1. Reemplazar `D` por un ledger explícito de distinciones con operaciones
   create/refine/merge y estados UNKNOWN/NA.
2. Modelar `T_t(a)` por opción y validar accesibilidad independientemente de PE/PR.
3. Entrenar B6 y MOC_R para **inferir** ediciones desde evidencia parcial, sin
   suministrar el estado objetivo.
4. Congelar dominios externos y un holdout de reglas, no sólo de etiquetas.
5. Comparar igual número de parámetros, datos, búsqueda y coste.
6. Hacer auditoría humana ciega de fidelidad explicativa.
7. Probar ablation del tipado y permutaciones de nombres.
8. Sólo si aparece ventaja reproducible, investigar meta-reorganización y Self.

## 10. Contexto bibliográfico

La implementación es compatible con reescritura tipada de grafos y reglas
before/after, como el formalismo DPO expuesto en
[König et al.](https://research.utwente.nl/en/publications/a-tutorial-on-graph-transformation/).
La literatura de razonamiento relacional inductivo muestra que el sesgo relacional
puede facilitar transferencia a grafos no vistos, pero no demuestra que el tipado
MOC lo haga; véase [Teru et al.](https://proceedings.mlr.press/v119/teru20a.html).
La abstracción relacional para planning ofrece un comparador pertinente para un
B5 futuro más fuerte ([PARL](https://arxiv.org/abs/2405.03864)). Éstas son fuentes
formales externas, no evidencia MOC.

## 11. Dictamen final

MOC_SEMANTIC_PRESERVATION = SUPPORTED
REORGANIZATION_FORMALIZATION = PARTIALLY_SUPPORTED
DISTINCTION_MODEL = PARTIALLY_SUPPORTED
RELATION_MODEL = SUPPORTED
CONSTRAINT_MODEL = PARTIALLY_SUPPORTED
POSSIBILITY_FIELD_MODEL = SUPPORTED
TRANSITABILITY_MODEL = PARTIALLY_SUPPORTED
B4_COMPARISON = PARTIALLY_SUPPORTED
B5_COMPARISON = PARTIALLY_SUPPORTED
B6_COMPARISON = SUPPORTED
NEW_POSSIBILITY_GENERATION = SUPPORTED
POSSIBILITY_RESTRICTION = SUPPORTED
RELATIONAL_REORGANIZATION = SUPPORTED
DISTINCTION_REORGANIZATION = PARTIALLY_SUPPORTED
CONSTRAINT_REORGANIZATION = PARTIALLY_SUPPORTED
XI_AS_STOP = NOT_SUPPORTED
XI_AS_ORGANIZATION_OPERATOR = NOT_SUPPORTED
C_CHOOSE_SEPARATION = SUPPORTED
TRANSFORMATION_HOLDOUT_GENERALIZATION = SUPPORTED
TRACE_FIDELITY = SUPPORTED
CAUSAL_ATTRIBUTION = PARTIALLY_SUPPORTED
GENERIC_ISOMORPHISM = SUPPORTED
ALGORITHMIC_UNIQUENESS = NOT_SUPPORTED
REPRESENTATIONAL_INCREMENTAL_VALUE = INSUFFICIENT_EVIDENCE
MOC_REORGANIZATION_DISTINCTIVENESS = NOT_SUPPORTED
META_REORGANIZATION = NOT_APPLICABLE
SELF_AS_REORGANIZATION_TARGET = NOT_APPLICABLE
FUNCTIONAL_SELF_AWARENESS = UNRESOLVED
PHENOMENAL_CONSCIOUSNESS = UNRESOLVED
MOC_EMPIRICAL_VALIDATION = INSUFFICIENT_EVIDENCE
