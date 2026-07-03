# AO-001 - Marco inicial de Algebra Operacional

Estatus: marco inicial provisional aceptado por `D-2026-07-03-009`.

Fecha: 2026-07-03.

Expediente: `AO-001`.

ID: `AO-MARCO-001`.

## Proposito

Proponer una primera forma local de la Algebra Operacional del Laboratorio sin convertirla todavia en documento oficial, teorema, Canon ni especificacion de Nivel C.

## Tesis provisional

La Algebra Operacional debe describir operaciones sobre artefactos con estatus, no solo cambios sobre objetos abstractos.

Su pregunta inicial es:

```text
Que operaciones preservan trazabilidad, estatus, autoridad, permisos e invariantes cuando un artefacto cambia?
```

## Objetos candidatos

| Simbolo | Lectura provisional | Estatus |
| --- | --- | --- |
| `A` | artefacto local | objeto operacional |
| `S` | estatus de una afirmacion o artefacto | objeto operacional |
| `E` | evidencia local materializada | objeto operacional |
| `C` | contexto declarado de aplicacion | objeto operacional |
| `R` | reporte estructurado | objeto operacional |
| `D` | decision emitida | objeto operacional |
| `P` | permiso acotado | objeto operacional |
| `I` | invariante declarado | objeto operacional |
| `T` | transformacion propuesta o ejecutada | objeto operacional |
| `B` | bloqueo, deuda o problema abierto | salida de seguridad |

Estos objetos no son todavia tipos formales. Son nombres de trabajo para ordenar el expediente.

## Operadores candidatos

La primera base operacional viene del Auditor v0:

```text
Mp -> Cr -> tau -> D -> Tr
```

Lectura candidata:

| Operador | Forma provisional | Funcion |
| --- | --- | --- |
| `Mp` | `Mp(A) = M` | mapea un artefacto a una estructura legible |
| `Cr` | `Cr(M) = R` | calcula o verifica sobre la estructura mapeada |
| `tau` | `tau(R) = cierre` | decide terminacion, bloqueo o escalamiento |
| `D` | `D(R, cierre) = d` | emite decision restringida por evidencia previa |
| `Tr` | `Tr(A, d, P) = A'` | propone o ejecuta transformacion solo si hay permiso valido |

Regla provisional:

```text
Tr(A, d, P) = A'
```

solo esta bien formada como ejecucion si `P` declara `transformacion_permitida = true`, existe alcance acotado, evidencia previa, evidencia posterior y verificacion posterior.

Si falta cualquiera de esas condiciones, la salida debe ser `B`, no `A'`.

## Relacion con Gamma

`GAMMA-DEF-001` aporta un operador candidato de generalizacion controlada:

```text
Gamma_1(E, C) = G
```

Lectura para `AO-001`:

- `Gamma_1` no es todavia construccion formal de `Gamma`;
- `E` debe estar materializada y tener estatus declarado;
- `C` debe estar delimitado antes de generalizar;
- `G` solo puede salir como candidata provisional, deuda refinada o problema abierto;
- `Gamma_1` no produce permiso de transformacion.

## Invariantes operacionales iniciales

### AO-I1 - Separacion de niveles

Una operacion sobre un nivel inferior no modifica por si misma un nivel superior.

### AO-I2 - Estatus preservado

Toda salida relevante conserva o declara estatus. Si no puede declarar estatus, la salida se degrada a deuda conceptual.

### AO-I3 - Evidencia antes de transformacion

Toda transformacion ejecutada requiere evidencia previa materializada.

### AO-I4 - Decision no equivale a permiso

Una decision favorable no basta para ejecutar una transformacion si falta permiso acotado.

### AO-I5 - Recomendacion no equivale a decision

Una recomendacion puede fundar una decision posterior, pero no la sustituye.

### AO-I6 - Reporte bloqueante no habilita cambio

Si un reporte bloquea, la salida operacional debe ser bloqueo, deuda o escalamiento.

### AO-I7 - Generalizacion no promueve estatus

Una generalizacion candidata no cambia por si misma el estatus de la evidencia que generaliza.

## Formas de salida

Una operacion operacional debe producir una de estas salidas:

- `continuar_sin_transformar`;
- `bloquear`;
- `escalar`;
- `proponer_cambio_acotado`;
- `ejecutar_cambio_acotado` solo con permiso valido;
- `registrar_deuda`;
- `registrar_problema_abierto`;
- `emitir_candidata_provisional`.

## Antipatrones

- Usar una salida correcta como autorizacion.
- Promover un operador local a regla general por analogia.
- Llamar transformacion a una recomendacion.
- Llamar verificacion a una lectura sin criterio.
- Llamar `Gamma` a cualquier generalizacion narrativa.
- Tratar `R4-CANDIDATA` como Regla R4 formal.

## Preguntas abiertas

- Que tipos minimos necesita el Documento 04?
- Conviene separar algebra de lectura, algebra de decision y algebra de transformacion?
- La verificacion posterior debe ser operador formal propio o condicion de `Tr`?
- Como se expresa composicion de operadores sin ocultar permisos?
- Que relacion hay entre confluencia local y preservacion de invariantes?
- Que equivalencias de proyeccion son suficientes para pasar de expediente a documento oficial?

## Criterio de avance

Este marco puede avanzar si produce:

- una notacion minima estable;
- una tabla de operadores con dominios, codominios y salidas de seguridad;
- casos positivos y negativos;
- auditoria favorable;
- decision de estatus como marco provisional aceptado.

## Veredicto provisional

La Algebra Operacional debe nacer como algebra de operaciones gobernadas, no como formalismo decorativo.

Su primera unidad no es la transformacion pura, sino la transformacion con estatus, evidencia, decision, permiso e invariante.
