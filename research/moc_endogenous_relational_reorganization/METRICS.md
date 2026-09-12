# Métricas estructurales

- `DC`: diff tipado de distinciones (add/remove/refine/merge/relabel/unknown).
- `RC`: diff tipado de relaciones (incidencia/tipo/dirección/condición).
- `KC`: diff tipado de constraints y estatus epistemológico.
- `PE`, `PR`, `PC`: conjuntos de expansión, restricción y diferencia simétrica.
- `TC`: cambios de transitabilidad por posibilidad común.
- `SRP`: tupla no promediada `(DC,RC,KC,PE,PR,PC,TC,TF,CAA)`.
- `TF`: proporción ponderada de pasos before/after justificables por la traza; pesos pre-registrados por criticidad.
- `CAA`: causa atribuida coincide con intervención aleatorizada/provenance.
- `HTG`: rendimiento en tipos de transformación no vistos.
- `GIR`: trazas reducibles a B6 mediante mapping simple congelado.
- `InterventionSparsity`: ediciones no necesarias / ediciones totales.
- `PossibilityPrediction`: precisión/calibración al predecir qué aparece, desaparece o cambia transitabilidad.

## Propagación four-valued

Por celda reportar `CHANGED/UNCHANGED/UNKNOWN/NA`. Tasas usan denominadores explícitos: `KnownChangeRate=CHANGED/(CHANGED+UNCHANGED)` y `UnknownRate=UNKNOWN/(total-NA)`. Nunca convertir UNKNOWN en UNCHANGED ni NA en cero.

## Regla de éxito

No hay promedio arbitrario. Cada experimento define restricciones duras y vector de criterios. Resultado positivo fuerte exige: efecto estructural preespecificado, CAA correcta, TF suficiente, mejora holdout y GIR baja frente a B6. Reportar Pareto/casos incomparables y coste.
