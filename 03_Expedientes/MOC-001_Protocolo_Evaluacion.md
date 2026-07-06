# MOC-001 - Protocolo de evaluacion

ID: `MOC-EVAL-PROTO-001`.

Estatus: protocolo reproducible provisional.

Decision asociada: `D-2026-07-05-013`.

## Proposito

Definir un procedimiento para que distintos evaluadores apliquen `Xi_eval_MOC` y los estados metricos del MOC sobre los mismos casos sinteticos no clinicos.

El objetivo es obtener resultados comparables sin ocultar desacuerdos.

## Material comun para evaluadores

Cada evaluador recibe:

- el mismo caso sintetico;
- la misma plantilla de entrada;
- la tabla de reglas de `Xi_eval_MOC`;
- la tabla de estados metricos;
- la lista de prohibiciones de alcance;
- la instruccion de no evaluar personas reales ni dominios clinicos.

## Plantilla de entrada

```text
caso_id:
R0:
R1:
Dist(R0,R1):
Res(R0 -> R1):
alcance:
evidencia:
restricciones:
ejes_TCS:
deuda_visible:
```

## Salida de cada evaluador

Cada evaluador debe emitir:

- `salida_Xi`: una de `redundante`, `util_acotado`, `limitado`, `no_comparable`, `bloqueado`;
- `estado_MOC`: uno de los seis estados metricos;
- `justificacion_breve`: razon de la clasificacion;
- `deuda`: deuda abierta o `sin_deuda_bloqueante`.

## Medicion de concordancia entre evaluadores

- Coincidencia exacta: todos los evaluadores emiten la misma `salida_Xi` y el mismo `estado_MOC`.
- Coincidencia parcial: los evaluadores discrepan en estado puntual, pero quedan dentro de la misma familia de salida.
- Desacuerdo justificado: los evaluadores caen en familias distintas y explican una razon auditable.

## Clasificacion de desacuerdos

Los desacuerdos no se borran ni se promedian. Deben clasificarse como:

- `friccion`: reglas aplicadas de forma distinta pero con evidencia suficiente.
- `falta_de_evidencia`: el caso no contiene testigos suficientes.
- `ambiguedad_de_regla`: la regla de prioridad no distingue el caso.
- `conflicto_de_autoridad`: hay fuentes o decisiones incompatibles.

## Criterio de aceptacion local

La bateria inicial se considera aceptable si:

- todos los casos conservan alcance sintetico no clinico;
- al menos tres evaluadores simulados pueden aplicar la plantilla;
- los desacuerdos quedan clasificados;
- no se fuerza unanimidad artificial;
- las salidas bloqueantes se respetan como bloqueantes.

## Restricciones

El protocolo no es estudio empirico real. No recluta personas, no evalua personas reales y no produce conclusiones estadisticas.

Cualquier estudio empirico posterior requiere decision separada, diseno ampliado y dominio no regulado.

## Nota posterior

El protocolo v0.1 queda refinado localmente por `MOC-EVAL-PROTO-002` en `MOC-001_Protocolo_Evaluacion_v0_2.md`, aceptado por `D-2026-07-05-024`.

El refinamiento agrega `operator_trace`, `Pi_moc_trace`, `ao_bridge`, ejes de desacuerdo, regla de desempate local y tratamiento de revision si el desacuerdo se repite. No canoniza el protocolo, no abre estudio empirico real y no modifica `Documento 04`.
