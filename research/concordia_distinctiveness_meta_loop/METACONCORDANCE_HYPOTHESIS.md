# Metaconcordancia — hipótesis de investigación

`Metaconcordancia` no es un término canónico. Denota provisionalmente que el propio patrón de intervención sea objeto de evaluación concordante:

\[
Loop_t\rightarrow Log_t\rightarrow\Phi_{meta}(Loop_t)
\rightarrow CandidatePolicy_{t+1}\rightarrow Validate\rightarrow Policy_{t+1}.
\]

## Implementación mínima

El meta-loop observa episodios tipados y calcula:

- falsos positivos de intervención;
- intervenciones omitidas;
- fallos de provenance;
- desempeño del resultado.

Propone una nueva política únicamente sobre un parámetro permitido. La candidata se acepta si mejora entrenamiento y no empeora holdout. Conserva versión, fuente, autoridad, `supersedes` y reversibilidad.

## Resultado local

El umbral cambió de `0.20` a `0.50`:

```text
training_error: 2 -> 0
holdout_error:  0 -> 0
accepted: true
reversal: PASS
permission_change: false
authority_change: false
code_rewrite: false
```

Esto respalda un meta-loop calibrador local. No demuestra metaconcordancia específicamente MOC: cualquier sistema de selección de hiperparámetros con holdout y rollback puede reproducirlo. La prueba distintiva futura debe evaluar un perfil relacional del propio proceso, no sólo un umbral.

