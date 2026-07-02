# HXI-001 - Decision de ruta operativa

Estatus: decision provisional de expediente.

Fecha: 2026-07-02.

## Decision

Se elige la ruta 2: continuidad acotada con notacion minima de expediente.

`HXI-001` continua abierto para formalizar una notacion minima `Xi-R` limitada al expediente, sin admitir `H-Xi` ni declarar `Xi` operador vigente.

## Base

- `HXI-001_Dictamen_Utilidad_Local_Xi.md`.
- `HXI-001_Decision_Estatus_Dictamen_Utilidad_Local.md`.
- `HXI-001_Matriz_Pruebas_HXI-R.md`.
- `HXI-001_Criterios_Evaluacion.md`.

## Rutas descartadas por ahora

### Ruta 1 - Pausa operativa

No se elige porque el dictamen encontro utilidad local acotada suficiente para una formalizacion minima.

### Ruta 3 - Preparacion de admision formal posterior

No se elige porque la evidencia local todavia mezcla caso positivo, limites y controles negativos. Eso no basta para abrir admision formal de `H-Xi`.

## Alcance de la ruta elegida

La continuidad acotada permite:

- crear notacion minima de expediente para `R0`, `R1`, `Dist(R)` y `Res(R0 -> R1)`;
- conservar salidas tecnicas `redundante`, `util_acotado`, `limitado`, `no_comparable` y `bloqueado`;
- aplicar la notacion a la matriz `HXI-R` como prueba de consistencia;
- mantener separada cualquier admision formal futura.

## No cubre

La decision no cubre:

- admision de `H-Xi`;
- canonizacion de `Xi`;
- declaracion de `Xi` como operador vigente;
- modificacion de documentos oficiales;
- cierre de `PSI-001`;
- resolucion de `P-107`;
- uso clinico, diagnostico, tratamiento o consejo profesional;
- transformaciones materiales del repositorio.

## Consecuencia

La accion inmediata es crear y auditar `HXI-001_Notacion_Minima_Xi-R.md` como herramienta local de expediente.

Despues de aceptar la notacion, el siguiente paso limpio sera aplicarla a `HXI-R-001` a `HXI-R-005` como reporte de consistencia.
