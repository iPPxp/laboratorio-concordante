# Metodo interdisciplinario y trazabilidad

## Roles aplicados a la primera version

| Rol | Pregunta controlada | Artefacto | Limite aplicado |
|---|---|---|---|
| Geometria discreta | Cuerdas, angulos, holguras, contacto | `geometry.py`, informe | No deducir optimalidad global de un caso finito |
| Matematicas de redes | Base, vectores, capa de vecinos | `lattices.py` | HCP se conserva como periodica con base, no Bravais simple |
| Ingenieria computacional | Ejecucion determinista, exportacion, pruebas | `run_initial_study.py`, `run_interstitial_multilevel.py`, `audit_r3_cycles.py`, `tests/` | Sin red, IA, dinamica fisica ni optimizador oculto |
| Ontologia | Tipos, relaciones, restricciones | `ONTOLOGIA.*` | No importar semantica humana ni clinica |
| DSL | Entrada declarativa y validacion de estructura | `dsl.py`, `ESPECIFICACION_DSL.md` | Una instancia no acredita un teorema |
| Auditoria bibliografica | Etiqueta, fuente, alcance y vacio | `BIBLIOGRAFIA.md` | Fuente clasica no se extrapola a transiciones locales |

## Protocolo de reproduccion

1. Usar una version de Python compatible y las dependencias fijadas en `requirements.txt`.
2. Ejecutar `scripts/run_initial_study.py` desde la raiz del proyecto.
3. Ejecutar `python -B -m unittest discover -s tests -v` con `PYTHONPATH=src`.
4. Validar que `data/results_initial.json` sea JSON valido y que sus campos correspondan con la version de codigo ejecutada.
5. Inspeccionar los SVG y el visor HTML solo como observacion visual; las conclusiones numericas vienen del JSON/CSV y las simbolicas del informe.

## Criterio de aceptacion de un futuro resultado

Un cambio debera declarar: hipotesis, dominio, parametros, precision/tolerancia, entrada exacta, version de algoritmo, salida, etiqueta epistemica, fuente y prueba o certificado cuando se use la palabra “demostrado”. Una falla, contraejemplo o resultado inconcluso debe conservarse como dato; no se normaliza como confirmacion.

## Controles actuales

- La suite unitaria cubre normalizacion, invariancia de escala, umbrales cerrados
  de tetraedro y octaedro, cardinalidades, distincion HCP, geometria R3 y
  resultados negativos/positivos de inclusion literal.
- El modelo no acepta `epsilon <= 0` para materializar centros, aunque puede informar el infimo analitico cero.
- Las salidas distinguen contactos de solapamientos por el signo de la holgura.
- Las transiciones incluyen un campo de alcance que impide presentarlas como teoremas universales.
