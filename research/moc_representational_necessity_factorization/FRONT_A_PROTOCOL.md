# Frente A — ontología mínima del Pentacoro

## Unidad experimental

Un bloque contiene al menos cuatro observaciones construidas o seleccionadas por
autores independientes:

1. estado base;
2. contrafactual A-only;
3. contrafactual B-only;
4. control donde ambos o ninguno cambia.

Los anotadores no conocen la predicción del modelo. Un segundo equipo adjudica
si los componentes supuestamente estables permanecieron aproximadamente
constantes y marca `UNKNOWN` cuando no puede establecerlo.

## Outcomes ciegos

Las etiquetas de factorización se producen antes, pero los outcomes usados para
validarla se mantienen ocultos:

- estado siguiente;
- posibilidades añadidas/retiradas;
- persistencia de elementos;
- efecto de una intervención definida;
- cambio de accesibilidad;
- incertidumbre y desacuerdo.

## Criterio por frontera

Una frontera A/B queda `SUPPORTED_LOCALLY` sólo si:

1. hay fiabilidad de anotación suficiente y pre-registrada;
2. A-only y B-only generan distribuciones de outcomes distinguibles;
3. la diferencia replica en familias y dominio holdout;
4. el resultado resiste controles por longitud, léxico, intensidad y contexto;
5. un modelo que fusiona A/B pierde rendimiento con intervalo de equivalencia
   excluido.

Si A y B no pueden separarse o su separación no cambia ninguna predicción,
`A_B_COMPUTATIONAL_BOUNDARY=NOT_SUPPORTED`.

