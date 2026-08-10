# Modelos rivales y pruebas discriminantes

## Modelos M0–M4

| Campo | M0: dos fuentes | M1: eje apolar | M2: centro + medida | M3: centro anisótropo | M4: ruptura espontánea |
|---|---|---|---|---|---|
| Primitivos | Dos fuentes | \([u]\) | Centro, aparato | Centro, \([u]\) | Estado y potencial degenerado |
| Estado | Debe definirse | \(\mathbb{RP}^2\) | Centro + variables del aparato | \((0,[u])\) | Órbita de mínimos |
| Signo físico | Posible | No | Puede ser instrumental | No necesariamente | Depende del orden polar/apolar |
| Papel del observador | Medición | Etiqueta/orienta localmente | Interacción causal | Etiqueta o mide | Selecciona o detecta un mínimo |
| Dinámica disponible | No | No necesaria para geometría | No | No | No |
| Estado actual | `INCOMPLETO` | `MATEMATICAMENTE_COMPLETO` | `HIPOTESIS` | `MODELO_POSIBLE` | `MODELO_POSIBLE` |

## Predicciones discriminantes

| Prueba | M1 apolar | Modelo polar | Centro isotrópico | Medición inductora |
|---|---|---|---|---|
| (u\mapsto -u\) | Mismo estado | Estado distinto | No hay eje intrínseco | Depende del aparato |
| Observable impar | Debe anularse/no ser estado | Puede cambiar signo | No selecciona signo | Puede aparecer con acoplamiento |
| Observable par | Puede ser no nulo | Puede ser no nulo | Isotrópico | Puede adquirir anisotropía |
| Rotar solo coordenadas | No cambia física | No cambia física | No cambia física | No cambia interacción real |
| Rotar aparato respecto al sistema | No debe crear polaridad por convenio | Respuesta material posible | Puede seleccionar eje si acopla | Debe cambiar respuesta según ley |

## Condiciones de falsación

### M1 — Eje apolar

Se debilita como descripción física si existe un observable reproducible, intrínseco y sensible al signo que distinga (u\) de \(-u\) sin depender del aparato.

### M2 — Eje inducido por medición

Se refuta para un sistema si el eje persiste con orientación determinada al retirar el aparato y las condiciones de frontera, o si no existe el acoplamiento postulado.

### M3 — Anisotropía interna

Requiere detectar una variable interna que determine \([u]\). Se refuta el mecanismo propuesto si esa variable no existe o no predice el eje.

### M4 — Ruptura espontánea

Requiere leyes simétricas, múltiples estados degenerados y selección de un estado. La mera presencia de dos dibujos opuestos no basta.

## Experimento mínimo aún ausente

No hay sistema físico declarado. Antes de diseñar instrumentalmente una prueba deben especificarse:

```text
SYSTEM
STATE_VARIABLE
FIELD_OR_ENERGY_FUNCTIONAL
UNITS
CONTROL_PARAMETERS
MEASUREMENT_OPERATOR
NOISE_MODEL
PREDICTION_M0
PREDICTION_M1
PREDICTION_M2
FALSIFICATION_THRESHOLD
```

Sin estos campos, la comparación permanece matemática y conceptual.
