# R001-001 - Integracion de table checks R-001 / Xi

Estatus: integracion tecnica provisional.

Fecha: 2026-07-05.

Identificador local: `R001-TABLE-CHECK-001`.

Fuente recibida: `C:\Users\IximM\OneDrive\Documentos\v.1.5.2\checks\r001_table_checks.py`.

Archivo integrado: `06_Automatizacion/r001_table_checks.py`.

## Proposito

Integrar una bateria local de chequeos tabulares para mini-pruebas `R-001` / `Xi` como herramienta de lectura no mutante del Laboratorio.

La integracion sirve para revisar si una familia acotada de modelos conserva sus guardas declaradas sobre:

- preservacion minima `P-000`;
- dependencia de `P-200` respecto de observaciones admitidas `O_adm`;
- limites de `mu_decouple`;
- equivalencia local, no equivalencia local y equivalencia trivial;
- frontera entre uso local de `Xi` y promocion formal.

## Evidencia integrada

El archivo se incorpora como herramienta local con salida Markdown y JSON.

La herramienta genera:

- `06_Automatizacion/reportes/r001_table_checks_report.md`;
- `06_Automatizacion/reportes/r001_table_checks_report.json`.

La prueba unitaria queda registrada en:

- `06_Automatizacion/test_r001_table_checks.py`.

La corrida actual de la herramienta reporta:

- `checks`: 20;
- `passed`: 20;
- `failed`: 0;
- `resultado`: `ok`;
- `transformacion_permitida`: `false`.

## Alcance permitido

`R001-TABLE-CHECK-001` puede usarse como:

- prueba local controlada de consistencia tabular;
- evidencia tecnica auxiliar para leer problemas de equivalencia local;
- puente limitado hacia trabajo posterior en `AO-001`, Confluencia y Equivalencia de proyecciones;
- control negativo contra promociones prematuras de `Xi`.

## No cubre

Esta integracion no:

- canoniza `Xi`;
- admite `H-Xi`;
- declara `Xi` operador vigente;
- cierra `P-200`;
- resuelve `P-107`;
- produce cambios al Canon;
- produce cambios a documentos oficiales;
- produce cambios de Nivel C;
- reabre `PSI-001`;
- habilita uso clinico;
- autoriza transformaciones materiales.

## Relacion con frentes activos

`HXI-001` permanece abierto en mantenimiento local por `D-2026-07-05-003`.

`AO-001` sigue siendo el frente operativo principal para profundizar `AO-PPI-BRIDGE-001`, Confluencia, Equivalencia de proyecciones y formalizacion posterior del Documento 04.

`R001-001` no reemplaza a `AO-001` ni convierte `P-PI.0` / `P-PI.1` en frentes activos. Es una pieza tecnica local que puede alimentar evidencia futura bajo decision separada.

## Deudas abiertas

- Relacion formal entre `R001-TABLE-CHECK-001` y una futura teoria general de equivalencia de proyecciones.
- Relacion formal global entre los chequeos tabulares y Confluencia global.
- Eventual decision puente si algun resultado debe incorporarse al Documento 04.
- Eventual especificacion posterior si `R001-TABLE-CHECK-001` debe salir del nivel de herramienta local.
- Separacion estricta entre utilidad local de `Xi` y admision de `H-Xi`.

## Resultado provisional

La integracion es aceptable como automatizacion local no mutante, sujeta a auditoria y decision espejo.
