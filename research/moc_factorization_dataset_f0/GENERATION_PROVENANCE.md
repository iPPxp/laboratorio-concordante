# Procedencia de generación

## Método

Los 24 episodios base fueron redactados manualmente para este instrumento y expandidos mediante tres transformaciones controladas: original, adición explícita de que no existe más información y prefijo de equivalencia con ajuste inicial de caja. No se usaron textos personales, clínicos, propietarios ni recuperados de internet.

Cada registro sellado conserva `generator`, `source_type=SYNTHETIC`, tipo de familia, autor funcional, fecha y `supersedes=null`. La procedencia identifica el proceso de construcción; no certifica corrección semántica.

## Controles de fuga

La clave `family_id` permite agrupar paráfrasis. La asignación de split ocurrió por familia antes de expandir variantes. Ninguna familia cruza splits. La entrada visible excluye estados posteriores, intervenciones, clases de diseño e incertidumbre.

## Reproducibilidad

Los archivos JSONL usan una línea JSON por episodio y UTF-8. Los manifiestos SHA-256 fijan sus bytes. `INTEGRITY.json` registra 72 casos, 24 familias, tres variantes por familia y el conjunto exacto de campos visibles. Cualquier cambio exige nuevos digests y una revisión explícita de procedencia.

## Estatus epistemológico

```text
SYNTHETIC_CORPUS = PRODUCED
NON_CLINICAL = DECLARED_BY_DESIGN
REAL_WORLD_VALIDITY = NOT_TESTED
MOC_FACTOR_VALIDITY = NOT_ESTABLISHED
SEALED_TRAJECTORIES = DESIGN_EXPECTATIONS_ONLY
```

