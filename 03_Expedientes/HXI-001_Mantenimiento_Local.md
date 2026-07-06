# HXI-001 - Mantenimiento local

Estatus: regimen de mantenimiento local de expediente.

Fecha: 2026-07-05.

Codigo: `HXI-MAINT-001`.

## Proposito

Mantener `HXI-001` abierto en mantenimiento local despues de la compuerta aplicada por `HXI-GATE-001`.

El mantenimiento conserva `Xi_eval` como herramienta local y mantiene `H-Xi` como hipotesis externa no admitida.

## Base

- `HXI-001_Decision_Resultado_Compuerta_Admision_Formal.md`: resultado `mantener_Xi_eval`.
- `HXI-001_Evaluacion_Compuerta_Admision_Formal.md`: evidencia de compuerta aplicada.
- `HXI-001_Reporte_Consistencia_Notacion_Xi-R.md`: consistencia de las cinco salidas de `Xi_eval`.
- `HXI-001_Notacion_Minima_Xi-R.md`: notacion local vigente dentro del expediente.
- `HXI-001_Dictamen_Utilidad_Local_Xi.md`: utilidad local acotada.

## Regimen de mantenimiento

`HXI-001` queda abierto, pero no como frente activo de admision.

El expediente puede mantenerse para:

- conservar trazabilidad de `H-Xi` como hipotesis externa no admitida;
- conservar `Xi_eval` como herramienta local de lectura;
- consultar las salidas `redundante`, `util_acotado`, `limitado`, `no_comparable` y `bloqueado`;
- recibir evidencia futura si existe decision explicita de reapertura de evaluacion;
- servir como antecedente local para comparar herramientas o criterios relacionales.

## No cubre

El mantenimiento local no cubre:

- admision de `H-Xi`;
- canonizacion de `Xi`;
- declaracion de `Xi` como operador vigente;
- reapertura de la compuerta sin evidencia nueva;
- promocion documental o formal;
- modificacion de Canon, documentos oficiales o Nivel C;
- reapertura de `PSI-001` dentro del Laboratorio;
- restauracion de copias locales `PSI-001*`;
- uso clinico, diagnostico, tratamiento o consejo profesional;
- resolucion de `P-107`;
- transformaciones materiales del repositorio.

## Condiciones para salir de mantenimiento

`HXI-001` solo debe salir de mantenimiento local si existe una decision posterior que indique una de estas rutas:

- nueva evidencia local suficiente para reabrir evaluacion;
- decision puente hacia el proyecto independiente `Psicologia Concordante`;
- comparacion formal con otro operador o herramienta local;
- cierre definitivo del expediente;
- promocion separada, con expediente, auditoria y decision propias.

## Deudas abiertas

- `H-Xi` sigue no admitida.
- `Xi` no es operador vigente.
- `P-107` sigue abierto.
- Faltan pruebas en dominios independientes si se quisiera superar el alcance local.
- Cualquier dependencia psicologica sustantiva requiere decision puente externa.

## Resultado

`HXI-001` queda abierto en mantenimiento local.

No queda como frente activo inmediato.

El trabajo activo puede volver a frentes sustantivos abiertos como `AO-001`, Confluencia, Equivalencia de proyecciones o formalizacion posterior del Documento 04.
