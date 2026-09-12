# Resultados

## Diseño ejecutado

Se ejecutaron 12 fixtures sintéticos congelados: 6 de desarrollo y 6 de holdout
de transformación. Cubren R-P, R-EAF, R-ACT, R-V, R-S, cambio sólo relacional,
distinción nueva/fusión/refinamiento, límite falso/real, expansión, contracción y
cruce entre acción y reorganización. Fixture, oracle y políticas tuvieron autores
separados.

Los cuatro sistemas recibieron la misma acción solicitada para desacoplar
selección de edición. B6 y MOC_R recibieron el mismo script estructural derivado
sin usar `case_id`. B5 recibió la misma especificación experimental, pero su
capacidad se limitó a revisar el generador; B4 conservó el campo fijo.

## Métricas agregadas

| Sistema | Estructura objetivo | Campo objetivo | Clasificación de reorganización | Fidelidad de traza | Atribución causal estricta | Estructura holdout |
|---|---:|---:|---:|---:|---:|---:|
| B4 | 8.3% | 41.7% | 16.7% | 63.3% | 8.3% | 16.7% |
| B5 | 0.0% | 0.0% | 91.7% | 35.0% | 0.0% | 0.0% |
| B6 | 100% | 100% | 100% | 100% | 100% | 100% |
| MOC_R | 100% | 100% | 100% | 100% | 100% | 100% |

Todas las tasas son descriptivas del conjunto sintético finito. No hay intervalos
inferenciales ni generalización a personas o dominios externos.

## Lecturas adversariales

1. **B4:** conseguir la acción solicitada no basta. Al no editar estructura,
   falla 10/12 etiquetas de reorganización y sólo coincide con un objetivo
   estructural negativo.
2. **B5:** ampliar el generador no reproduce la transición objetivo. Su 91.7% en
   la etiqueta gruesa “reorganización” es un falso consuelo: el oracle considera
   significativo editar el generador, pero la atribución causal estricta exige
   además acertar qué estructura cambió y cae a 0%.
3. **B6 y MOC_R:** empatan en todas las medidas ejecutadas. El tipado MOC no
   produjo ventaja de capacidad, generalización o traza.
4. **Isomorfismo:** 12/12 global y 6/6 holdout con un único normalizador, sin
   reglas por fixture ni testigo que rompa el mapeo.
5. **Distinciones:** 7/12 cambios semánticos esperados no son observables en `D`;
   el oracle devuelve `UNKNOWN`. Ésta es deuda representacional, no evidencia a
   favor de MOC_R.

## Separaciones demostradas localmente

- Una acción puede cambiar sin reorganización (`HOLD-ACT-001`).
- Puede haber reorganización relacional con la acción estable (`HOLD-ACT-002`).
- Añadir un límite real contrae; retirar una restricción falsa expande.
- Una relación puede cambiar con los cinco nodos fijos y alterar el campo.
- Una etiqueta de cambio no establece la causa correcta.

## Límites

- El objetivo estructural se suministra; no se predice.
- Los fixtures son diseñados y sintéticos, no muestreo empírico.
- B5 es un replanner elemental, no un planificador generativo de frontera.
- B4 conserva la familia funcional del control previo, pero esta interfaz no
  reproduce toda su lógica histórica de suficiencia conjunta; B4/B5 son por ello
  comparaciones parciales. El falsador decisivo es B6.
- B6 es fuerte respecto a edición, pero no aprende reglas desde datos.
- Transitabilidad usa un proxy de conjunto/score.
- La ventaja representacional MOC no fue evaluada por humanos ciegos ni en
  transferencia externa.

## Verificación

```text
TESTS = 14/14 OK
GENERIC_ISOMORPHISM_RATE = 1.0
HOLDOUT_GENERIC_ISOMORPHISM_RATE = 1.0
FIXTURE_INTEGRITY = OK
ORACLE_RUBRIC_INTEGRITY = OK
```
