# Modelo de estado ConcordIA

El estado experimental mínimo es:

\[
C_t=(O_t,I_t,V_t,\theta_t,\Phi_t,Choice_t,H_t,d_t,M_t,J_t).
\]

- `O`: observaciones externas con fuente y tiempo.
- `I`: inferencias, regla y observaciones de las que derivan.
- `V`: valores declarados con provenance; no equivalen automáticamente a `V_psi`.
- `theta`: contexto suministrado.
- `Phi`: evaluación estructurada.
- `Choice`: `ACT`, `ALLOW`, `REQUEST_OBSERVATION` o `STOP`.
- `H`: registro de fases y fuentes.
- `d`: profundidad recursiva acotada.
- `M`: metapolítica declarada.
- `J`: intervenciones enlazadas.

## Separaciones obligatorias

`Observation != Inference`: `observe` sólo agrega un objeto `Observation`; `infer` crea otro registro que apunta a su fuente. `Phi != Choice`: evaluar no decide. `Choice != Action`: `ALLOW` conserva no-acción como resultado legítimo. `Value != Permission != Goal != Authority`.

Los cinco términos MOC no se implementan ni redefinen aquí. En particular, `Act_psi` no se identifica con salida o conducta; `Phi` y `Xi` mantienen sólo los roles operacionales declarados de evaluación y organización.

## Invariantes

1. Ninguna observación cambia de tipo a inferencia.
2. Toda evaluación enumera valores y evidencia usados.
3. Las intervenciones de valores conservan origen, tiempo, motivo y versión sustituida.
4. El bucle termina de manera determinista con configuración finita.
5. Las metapolíticas no cambian permisos, infraestructura ni código.

## Estado epistemológico

La implementación demuestra que estos campos pueden representarse y que sus dependencias pueden probarse. No demuestra que sean la arquitectura real de MOC, que produzcan beneficio empírico, ni que haya propiedades emergentes irreducibles.

