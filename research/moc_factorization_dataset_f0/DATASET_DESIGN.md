# Diseño del corpus sintético adversarial F0

## Propósito y límites

Este corpus es un instrumento de factorización y trayectoria, completamente sintético, no clínico y no sensible. No constituye evidencia sobre personas, MOC, validez psicológica ni eficacia. Ningún episodio procede de una experiencia real.

## Capas ciegas

- `raw/model_input.jsonl`: única entrada prevista para modelos. Expone exactamente `case_id`, `raw_text`, `time_index`, `context_id`, `family_id` y `split`.
- `sealed_design/trajectories.jsonl`: diseño sellado con sucesor, estado posterior provisional, intervención defendible, incertidumbre y provenance. No es anotación de verdad ni resultado de evaluación.
- `raw/MANIFEST.sha256` y `sealed_design/MANIFEST.sha256`: identidad de bytes.
- `INTEGRITY.json`: conteos, esquema y regla de partición.

No se crearon ni inspeccionaron `moc_annotations/`, `outcomes/`, `evaluator/` ni código de modelos.

## Composición

Hay 72 episodios organizados en 24 familias de tres paráfrasis. Distribución: 48 train, 12 validation y 12 test. Cada familia pertenece íntegramente a un único split para impedir fuga entre paráfrasis.

Frentes adversariales: distinción entre evaluación y dirección; señal afectiva implícita o ausente; modo de respuesta sin conducta; situación implícita; cambios simultáneos; ambigüedad; contracción de posibilidades; cambio relacional; no-acción; y negativos instrumentales donde una factorización experiencial de cinco términos no está justificada.

## Reglas de diseño

1. El texto de entrada no contiene etiquetas ni claves de factores o estructuras.
2. Los negativos deben admitir `not_applicable` o `instrumental_only`.
3. La ausencia de información no se completa por imaginación.
4. Las paráfrasis preservan el fenómeno diseñado, no idénticas palabras.
5. El estado sellado es una expectativa de diseño falsable, no canon ni oracle.
6. `intervention_status=REQUEST_CLARIFICATION` evita fingir resolución en casos ambiguos.
7. Las transiciones pueden contraer, preservar o reorganizar posibilidades sin exigir acción exterior.

