# Decision - Integracion R001 table checks

ID: `D-2026-07-05-004`.

Estatus: decision provisional de expediente.

Fecha: 2026-07-05.

## Decision

Se acepta `R001-TABLE-CHECK-001` como herramienta local no mutante del Laboratorio.

Documento base: `03_Expedientes/R001-001_Integracion_Table_Checks.md`.

Auditoria: `03_Expedientes/R001-001_Auditoria_Integracion_Table_Checks.md`.

Implementacion: `06_Automatizacion/r001_table_checks.py`.

## Alcance

La decision permite:

- conservar la bateria de 20 chequeos tabulares como prueba local;
- generar reportes Markdown y JSON;
- ejecutar la prueba dentro de `DO-LAB-RUN-001`;
- usar el resultado como evidencia tecnica auxiliar en `AO-001`;
- usarlo como control negativo contra promocion prematura de `Xi`.

## No cubre

La decision no:

- canoniza `Xi`;
- admite `H-Xi`;
- declara `Xi` operador vigente;
- reabre admision de `H-Xi`;
- cierra `P-200`;
- resuelve `P-107`;
- demuestra Equivalencia global de proyecciones;
- demuestra Confluencia global;
- produce cambios al Canon;
- produce cambios a documentos oficiales;
- produce cambios de Nivel C;
- reabre `PSI-001`;
- restaura copias locales `PSI-001*`;
- habilita uso clinico;
- autoriza transformaciones materiales.

## Consecuencia

`R001-TABLE-CHECK-001` queda integrado a `06_Automatizacion` y al comando unico del Laboratorio.

`R001-001` queda como expediente tecnico provisional aceptado, no como frente activo principal.

El frente operativo principal sigue siendo `AO-001`, con foco en Confluencia, Equivalencia de proyecciones y formalizacion posterior del Documento 04.

`HXI-001` permanece abierto en mantenimiento local por `D-2026-07-05-003`.

## Deudas abiertas

- Equivalencia global de proyecciones.
- Confluencia global.
- Relacion formal posterior entre `R001-TABLE-CHECK-001` y `AO-PPI-BRIDGE-001`.
- Eventual decision puente para incorporar resultados al Documento 04.
- Separacion estricta entre utilidad local de `Xi` y admision de `H-Xi`.
