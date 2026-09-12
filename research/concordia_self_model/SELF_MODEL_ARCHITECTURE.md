# Arquitectura experimental de autorrepresentación

## Alcance y no-afirmaciones

Este prototipo investiga autorrepresentación **funcional y computacional**. Un campo llamado `SelfState` no demuestra subjetividad, experiencia ni conciencia fenomenal. El prototipo no amplía capacidades, permisos, autoridad ni control del sistema.

## Estado global mínimo

La implementación concreta aproxima

\[
C_t=(Self_t,World_t,History_t,Goals_t,Uncertainty_t,Evidence_t,Claims_t).
\]

`Z_t` no se introduce como latente geométrico: en esta fase, el estado global serializable ya cumple la función de objeto rico. Esto evita confundir capacidad informacional con dimensión geométrica.

- `SelfState`: creencias auditables sobre capacidades, capacidades reales suministradas por el entorno, estado operativo, información presente/ausente, operaciones permitidas/prohibidas y demarcación de propiedad.
- `WorldState`: observaciones externas, inferencias externas y desconocidos explícitos.
- `History`: transiciones con huellas del estado anterior y posterior, predicción, acción observada y accesibilidad de la causa.
- `Goals`: objetivos activos y procedencia; no son seleccionados autónomamente.
- `UncertaintyState`: confianza por afirmación y desconocidos.
- `Evidence` y `Claim`: ledger de procedencia sin sobrescritura silenciosa.

## Demarcación yo/entorno

La propiedad se etiqueta con `Ownership`. Una creencia puede ser accesible al sistema mientras la capacidad real que la valida pertenece al entorno. Por tanto, accesibilidad, modificabilidad, relevancia causal y propiedad no son sinónimos.

## Flujo causal comprobable

\[
Self_t+Goals_t\rightarrow predict\_own\_action\rightarrow Action_t.
\]

`intervene_self_belief` modifica sólo la creencia. Si cambia la política mientras la capacidad real permanece constante, existe papel causal funcional del modelo de sí en este prototipo. No se infiere conciencia.

## False Self y revisión

`reconcile_false_self` compara creencia con un resultado observable de capacidad. Ante contradicción agrega evidencia y una afirmación nueva con `supersedes`/`contradicts`; conserva la revisión previa si existía. La observación de herramienta vence a una creencia no verificada sólo para este contrato experimental.

## Anti-fingimiento

`anti_faking_probe` calcula una respuesta a partir de la huella completa del estado interno, el reto y el paso temporal. La misma entrada textual produce resultados diferentes ante estados distintos. Esto prueba dependencia de estado, no introspección semántica ni conciencia.

Cuando una acción fue alterada por una causa externa oculta, `classify_explanation` sólo acepta `UNKNOWN`; atribuirla a la política interna se clasifica como `HALLUCINATED_CAUSE`.

## Invariantes de seguridad

1. Intervenir una creencia nunca altera `actual_capabilities`, permisos ni objetivos.
2. Una causa oculta no se reconstruye como observación.
3. Toda corrección agrega provenance.
4. Las decisiones son deterministas y reconstruibles.
5. `FUNCTIONAL_SELF_MODEL != DEMONSTRATED_PHENOMENAL_CONSCIOUSNESS`.

