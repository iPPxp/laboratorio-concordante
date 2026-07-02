# DO-001 - Decision de alcance de SPEC-AUD-001

Estatus: decision provisional de expediente.

Expediente padre: `DO-001`.

Fecha: 2026-07-01.

Identificador: `ALC-SPEC-AUD-001`.

Objeto: definir que parte de `DO-001` pasa a Especificacion Tecnica del Auditor.

## Decision

`DO-001` puede producir una especificacion tecnica candidata del Auditor, identificada como `SPEC-AUD-001_Candidata`.

La candidata debe permanecer en `03_Expedientes` hasta que exista una decision de promocion a documento oficial.

No se crea todavia un documento oficial en `02_Documentos`; `NIVEL-C-001` solo habilita la auditoria de promocion.

## Contenido exportable

Las siguientes partes de `DO-001` quedan autorizadas para pasar a la especificacion candidata:

- proposito y alcance del Auditor como asistente de auditoria y trazabilidad
- fuentes locales autorizadas y entradas permitidas
- entradas que no pueden tratarse como autoridad
- salidas permitidas y salidas prohibidas
- modo operativo mixto definido por `MODO-AUD-001`
- superficie no mutante `DO-CHECK-001`
- estructura minima de `DO_CHECK_REPORT`
- regla de permiso `PERMISO-ACT-001`
- secuencia operacional minima `Mp -> Cr -> tau -> D -> Tr`
- contratos de reportes de `AUD-001` por referencia, no como Canon
- reglas de promocion, auditoria y deuda conceptual
- verificacion posterior obligatoria para cambios ejecutados
- actualizacion de estado operativo solo bajo permiso valido

## Contenido no exportable todavia

Las siguientes partes deben permanecer como expediente, deuda o referencia provisional:

- narrativa historica de exploracion
- generalizacion de `R4-AUD` a `R4` formal
- construccion formal de `Gamma`
- transformaciones no triviales no validadas
- reversion real ejecutada sobre archivos locales
- cuarentena materializada como carpeta, copia o estatus documental
- reglas de modificacion de Canon mas alla de restricciones negativas
- cualquier cierre automatico de expediente
- implementacion concreta de herramienta o codigo ejecutable completo

## Forma de salida autorizada

La salida autorizada en esta fase es:

```text
03_Expedientes/DO-001_SPEC-AUD-001_Candidata.md
```

Esta salida tiene estatus de expediente. No es Canon, no es documento oficial y no autoriza implementacion completa.

## Condiciones para promocion futura

`SPEC-AUD-001_Candidata` solo puede pasar a documento oficial si antes se cumple:

- decidir si el destino es `02_Documentos` u otra superficie de especificaciones
- registrar alcance, fuentes, efectos y problemas abiertos afectados
- conservar como deudas separadas `R4`, `Gamma`, reversion real y transformaciones no triviales

## Resultado

El objetivo no es escribir la especificacion oficial, sino fijar su frontera.

La parte tecnica exportable queda separada de la parte exploratoria y de las deudas conceptuales abiertas.

## Criterio de cierre

Esta decision queda registrada si:

- existe este archivo asociado a `DO-001`
- existe `DO-001_SPEC-AUD-001_Candidata.md`
- existe validacion local de la candidata
- `DO-001` referencia la decision y la candidata
- el estado del proyecto mueve el siguiente objetivo a decidir la promocion de `SPEC-AUD-001_Candidata`
