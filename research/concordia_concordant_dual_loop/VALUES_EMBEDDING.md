# Valores: representación y procedencia

## Representación mínima

Cada `ValueRecord` conserva obligatoriamente `value_id`, `meaning`, `source`, `source_type`, `authority`, `scope`, `priority`, `confidence`, `active`, `activation_reason` y `timestamp`. Para el experimento sintético añade criterio observable, objetivo, peso no negativo, restricciones, estado, agente, evidencia, versión sustituida e intervención. Es una estructura tipada y no un embedding aprendido.

La evaluación provisional es:

\[
\Phi(C_t)=context\_factor\sum_v w_v|target_v-observed_v|.
\]

Esta fórmula sólo permite una prueba determinista. El agregado es una implementación de juguete de **fricción**, no una definición de concordancia ni una recompensa. Si faltan valores activos o `Phi`, la salida es `UNDETERMINED`, no concordancia perfecta. Valores incompatibles sobre el mismo criterio generan una violación explícita. La fórmula no afirma validez psicológica, equivalencia semántica MOC ni optimalidad.

## Intervenciones

`intervene_value` crea una versión nueva y un evento `ValueIntervention`; no sobrescribe el registro original. `reverse_intervention` restaura el peso anterior únicamente cuando el vínculo coincide. La procedencia externa permanece externa: ConcordIA no se atribuye la autoría.

## Qué no significa embedding

Codificar valores en una colección o vector no demuestra que el sistema los tenga fenomenológicamente, los haya elegido, ni tenga autoridad para modificarlos. Un embedding futuro requeriría una función explícita, pérdidas declaradas, identificabilidad y comparación contra esta representación simple.

## Pruebas discriminantes

- Ablación V: peso cero o `enable_values=False` debe eliminar su contribución a Phi.
- Intervención aislada: cambiar un peso manteniendo observación/contexto constantes debe producir el cambio predicho.
- Reversión: debe recuperar el peso y resultado originales.
- Provenance: origen y evento deben reconstruirse sin inferirlos del contenido.
- Conflicto: objetivos activos incompatibles no deben desaparecer por promedio.

Hasta ejecutar datos externos y tareas relevantes:

```text
VALUES_REPRESENTABLE = SUPPORTED
VALUES_PROVENANCE_AUDITABLE = SUPPORTED
VALUES_EMPIRICAL_VALIDITY = INSUFFICIENT_EVIDENCE
VALUES_MOC_EQUIVALENCE = NOT_SUPPORTED
AUTONOMOUS_VALUE_FORMATION = NOT_APPLICABLE
```
