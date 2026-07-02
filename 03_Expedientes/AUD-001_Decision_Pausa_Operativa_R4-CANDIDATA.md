# AUD-001 - Decision de pausa operativa tras R4-CANDIDATA

Estatus: decision provisional de expediente.

ID: `PAUSA-AUD-001-R4-CANDIDATA-001`.

Expediente padre: `AUD-001`.

Objeto decidido: pausa operativa de `AUD-001` despues de la ruta elegida para `R4-CANDIDATA`.

Fuente principal: `AUD-001_Decision_Ruta_Siguiente_R4-CANDIDATA.md`.

## Decision

`AUD-001` queda en pausa operativa.

La pausa no es cierre, rechazo ni promocion. El expediente permanece abierto y retomable, pero sin frente inmediato activo.

Estado asignado:

```text
AUD-001 = expediente abierto en pausa operativa
R4-CANDIDATA = hipotesis operativa robustecida dentro de AUD-001
```

## Motivo

La cadena tecnica del Auditor quedo validada provisionalmente hasta `VAL-016`.

`R4-CANDIDATA` tiene una primera ronda no automata registrada, sintetizada, auditada y cerrada provisionalmente.

La compuerta de criterios fue aceptada y la ruta elegida conserva la candidata como hipotesis operativa robustecida.

No queda una ruta inmediata de promocion formal abierta. Las rutas superiores requieren decisiones y artefactos nuevos: especificacion de `REPORT_LAYER`, auditoria de Nivel C, definicion formal de R4 o tratamiento de `Gamma`.

Por eso procede pausar `AUD-001` en vez de forzar otra ronda por continuidad inercial.

## Alcance permitido

La decision permite:

- usar `HANDOFF.md` y `HANDOFF_PACKAGE.md` como punto de entrega operativo
- conservar `AUD-001` como expediente abierto y retomable
- citar `R4-CANDIDATA` solo como hipotesis operativa robustecida dentro de `AUD-001`
- reactivar `AUD-001` mediante decision explicita posterior
- elegir otro frente activo del Laboratorio sin cerrar `AUD-001`

## Alcance no permitido

La decision no permite:

- cerrar `AUD-001`
- promover `R4-CANDIDATA` a Canon, documento oficial, Nivel C o Regla R4 formal
- convertir `REPORT_LAYER` en especificacion oficial
- modificar Canon o documentos oficiales
- ejecutar transformaciones materiales
- tratar la pausa como resolucion de `R4` formal o `Gamma`

## Condiciones de reactivacion

`AUD-001` puede reactivarse si una decision posterior elige alguno de estos frentes:

- preparar promocion formal de `R4-CANDIDATA`
- redactar una especificacion separada de `REPORT_LAYER`
- ampliar pruebas no automatas con objetivo declarado
- conectar `R4-CANDIDATA` con una definicion formal de R4
- tratar `Gamma` con material local nuevo
- auditar cierre formal de `AUD-001`

## Consecuencia operativa

El paquete de handoff queda listo para traspaso operativo.

No hay siguiente objetivo obligatorio dentro de `AUD-001`.

El siguiente objetivo del Laboratorio es elegir un frente activo desde las deudas de alto nivel.

## Deudas que permanecen

- Si se busca promocion formal, redactar una especificacion separada de `REPORT_LAYER`.
- Si se busca promocion formal, justificar si la primera ronda no automata basta o ampliar pruebas especificas.
- Mantener abiertos `R4` formal y `Gamma` hasta definicion local.
- Elegir el siguiente frente activo del Laboratorio desde deudas de alto nivel.

## Resultado operativo

El siguiente objetivo queda definido como:

```text
Elegir siguiente frente activo del Laboratorio desde deudas de alto nivel.
```

## Veredicto

`AUD-001`: pausa operativa.

`R4-CANDIDATA`: hipotesis operativa robustecida.

Handoff: listo para traspaso operativo.
