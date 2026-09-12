# D: estado, relación derivada u operación

El `UNKNOWN=7/12` del frente anterior impide declarar `D` como sexta primitiva.
Se comparan cuatro modelos:

```text
D0 = no existe D explícita
D1 = D es estado primitivo
D2 = D es relación derivada entre contenidos/tipos
D3 = D es operación de diferenciación sobre P/S/R/delimitaciones
```

Ejemplo:

```text
antes: P(action,result)=equivalent
operación: DIFFERENTIATE(action,result)
después: P(action,result)=distinct
```

En D3, la distinción no es un nodo persistente por defecto. Es una transformación
con precondición, objeto, alcance, resultado, provenance y reversibilidad. Puede
materializar una nueva relación o modificar P sin añadir un sexto campo.

## Comparación

Cada variante recibe idénticos datos, presupuesto y objetivos. Se mide:

- predicción de transición;
- precisión del efecto de intervención;
- complejidad descriptiva;
- consistencia entre anotadores;
- transferencia;
- tasa de distinciones inútiles;
- capacidad de fusión y reversión.

`D_AS_OPERATION` sólo se apoyará si D3 supera D0/D1/D2 fuera de muestra y la
ventaja no proviene de etiquetas adicionales.

