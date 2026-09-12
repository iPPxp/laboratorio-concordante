# Dataset card F0

## Motivación

Probar si el instrumento puede mantener separadas entrada cruda, anotación MOC y
outcomes antes de construir un corpus naturalista. El corpus fue diseñado para
contener ambigüedad y negativos, no para maximizar reconocimiento MOC.

## Composición

| Campo | Valor |
|---|---:|
| textos/episodios | 72 |
| familias independientes | 24 |
| paráfrasis por familia | 3 |
| train | 48 textos / 16 familias |
| validation | 12 textos / 4 familias |
| test | 12 textos / 4 familias |
| datos personales | 0 |
| datos clínicos | 0 |
| humanos observados | 0 |

Cobertura del diseño sellado:

| Familia adversarial | Casos |
|---|---:|
| P/V confundibles | 9 |
| modo sin conducta | 9 |
| negativos no pentacóricos | 9 |
| contracción | 9 |
| afecto implícito | 6 |
| situación implícita | 6 |
| ambigüedad | 6 |
| cambio simultáneo | 6 |
| cambio relacional | 6 |
| afecto ausente | 3 |
| Allow/no acción | 3 |

## Entrada visible

```text
case_id, raw_text, time_index, context_id, family_id, split
```

No contiene campos estructurales ni outcomes. `family_id` debe usarse para
agrupar; tratar 72 paráfrasis como 72 muestras independientes sería
pseudorreplicación.

## Anotaciones

Un anotador instrumental independiente produjo estados
`PRESENT/ABSENT/AMBIGUOUS/UNKNOWN` y relaciones prudentes. No existe acuerdo
interevaluador. Conteos PRESENT:

```text
P=39  EAF=0  ACT=18  V=24  S=54
```

`EAF=0` impide probar la necesidad de los cinco factores. No se corregirá
post-hoc dentro de esta versión porque hacerlo después de ver el resultado
contaminaría el instrumento; una F0.1 deberá diseñarse y congelarse por separado.

## Outcomes

Los 72 outcomes fueron derivados ciegamente de trayectorias sintéticas selladas.
No usan campos MOC. Sin embargo, las trayectorias fueron creadas por el mismo
diseñador que los textos: la codificación es independiente, la fuente causal no.
Treinta casos mantienen `possibility_change=UNKNOWN` y los 72 declaran una
intervención disponible.

## Usos adecuados

- probar schemas, manifests, separación de capas y auditorías;
- desarrollar loaders sin abrir capas selladas;
- ensayar métricas y pipelines con resultados explícitamente instrumentales;
- descubrir huecos antes de F1/F2.

## Usos prohibidos

- validar MOC o los cinco factores;
- estimar eficacia psicológica o causalidad humana;
- entrenar y publicar un modelo como evidencia confirmatoria;
- tratar paráfrasis como réplicas independientes;
- promover outcomes sintéticos a evidencia externa;
- usar el corpus en decisiones personales, clínicas o de seguridad.

La documentación sigue el espíritu de las propuestas de
[*Datasheets for Datasets*](https://arxiv.org/abs/1803.09010) y
[*Data Statements for NLP*](https://aclanthology.org/Q18-1041/): composición,
procedencia, usos y límites deben acompañar cualquier inferencia.

