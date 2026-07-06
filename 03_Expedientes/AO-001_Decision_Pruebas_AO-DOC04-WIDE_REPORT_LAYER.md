# Decision - Pruebas AO-DOC04-WIDE-001 y REPORT_LAYER

Identificador: `D-2026-07-06-007`.

Fecha: 2026-07-06.

Estatus: decision de expediente aceptada.

Expediente: `AO-001`.

Artefactos aceptados:

- `AO-DOC04-WIDE-TEST-001`.
- `AO-REPORT-LAYER-BRIDGE-001`.

## Decision

Se acepta la bateria local no mutante `AO-DOC04-WIDE-TEST-001` para probar `AO-DOC04-WIDE-001` contra casos sinteticos.

Se acepta `AO-REPORT-LAYER-BRIDGE-001` como precision local de la relacion entre `REPORT_LAYER` y Documento 04 amplio.

## Resultado

La corrida local esperada queda:

```text
cases: 8
passed: 8
failed: 0
resultado: ok
transformacion_permitida: false
```

`REPORT_LAYER` queda precisado como entrada proyectable por `Pi_rep`:

```text
Pi_rep(REPORT_LAYER, C, W) -> R_rep | B
```

## No cubre

Esta decision no:

- modifica Canon;
- crea Nivel C;
- promueve `REPORT_LAYER`;
- absorbe `DO_CHECK_REPORT`;
- sustituye `Op_AO`;
- convierte reportes en decisiones;
- convierte recomendaciones en permisos;
- autoriza transformaciones;
- cierra Confluencia global;
- cierra Equivalencia global;
- exporta R4/Gamma.

## Consecuencia

La deuda inmediata de "probar Documento 04 amplio contra casos y precisar `REPORT_LAYER`" queda atendida en grado local no mutante.

Permanecen abiertas:

- pruebas no triviales adicionales con reportes heterogeneos;
- posible serializacion formal de `REPORT_LAYER` si aparece necesidad interfrente;
- Confluencia global;
- Equivalencia global;
- exportacion general R4/Gamma;
- maduracion de `TCS-001`.
