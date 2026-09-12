# F0.1 — preregistro de generación y readiness

**Fecha de congelación:** 2026-08-15.  
**Estatus:** protocolo sintético adversarial, no canónico, no clínico, sin
entrenamiento. Este documento precede a todo dato F0.1.

## Objetivo

Construir un corpus con poder para apoyar, igualar o perjudicar una
representación MOC sin que el resultado quede precocinado por diseño.

## Tamaño y splits

```text
INDEPENDENT_FAMILIES = 60
TEXTS_PER_FAMILY = 1
TRAIN_FAMILIES = 35
VALIDATION_FAMILIES = 10
TEST_FAMILIES = 15
```

La unidad estadística es la familia. No se añaden paráfrasis como réplicas.

## Núcleo contrafactual

Para cada una de las diez fronteras A/B se crean cuatro familias:

```text
00: A estable, B estable
01: A estable, B cambia
10: A cambia, B estable
11: A cambia, B cambia
```

Total: 40 familias core. Las 20 restantes son adversariales: Eaf explícito,
implícito, ausente y DECOY; no intervención; contexto incidental; Act sin
conducta; simultaneidad; negativos no pentacóricos; outcome incierto.

## Cobertura observada requerida

Después de dos anotaciones ciegas y antes de adjudicar, cada componente debe
tener en cada split al menos:

| Split | PRESENT | ABSENT | AMBIGUOUS o UNKNOWN |
|---|---:|---:|---:|
| train | 8 | 6 | 4 |
| validation | 2 | 2 | 2 |
| test | 3 | 3 | 2 |

No se corrigen casos para alcanzar cuotas después de ver predicciones de modelos.
Si falla, F0.1 no pasa gate y se preserva.

## Intervenciones y outcomes

- mínimo 12/60 familias con intervención no disponible;
- mínimo dos no disponibles en cada split;
- outcomes derivados de reglas del mundo selladas antes de narrar;
- narrador no conoce outcome futuro completo;
- outcome author no lee textos ni anotaciones;
- `UNKNOWN` se conserva cuando la regla no identifica una consecuencia.

## Anotación

Dos anotadores ciegos usan el mismo manual. No conocen pares/celdas, outcomes,
slots manipulados ni hipótesis del benchmark. Un adjudicador distinto entra sólo
tras congelar ambos manifests.

Gate descriptivo mínimo por componente:

```text
RAW_AGREEMENT >= 0.65
BINARY_PRESENT_AGREEMENT >= 0.70
UNKNOWN_RATE <= 0.65
```

Se reportan matrices completas; superar umbrales no prueba validez ontológica.

## Contaminación y permutación

- cero duplicados textuales;
- familias no cruzan splits;
- auditoría de similitud por shingles de palabras;
- spans compartidos requieren razones específicas por constructo;
- se congela una permutación de labels que preserve marginales y rompa
  asociaciones por caso;
- el performance sanity check queda `PENDING_MODEL_PHASE`, porque F0.1 no entrena.

## Regla de no reparación

F0.1 se congela antes de auditoría. Cualquier corrección crea F0.2; no se reemplaza
silenciosamente un registro para pasar el gate.

