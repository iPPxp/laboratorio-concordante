# 04 - Algebra Operacional

Estatus: documento oficial actualizado, version inicial consolidada.

Decision de incorporacion: `D-2026-07-03-011`.

Fuentes principales: `AO-001`, `AO-MARCO-001`, `SRC-010`, `SRC-012`, `SRC-013`, `SRC-023`, `AUD-001_R4_Formal_Local.md`, `AUD-001_Gamma_Formal_Local.md`, `C-001`, `C-002`.

## Proposito

La Algebra Operacional describe operaciones gobernadas sobre artefactos, modelos, evidencias, reportes, decisiones, permisos, invariantes y transformaciones.

Su pregunta inicial es:

```text
Que operaciones preservan trazabilidad, estatus, autoridad, permisos e invariantes cuando un artefacto cambia?
```

La unidad basica no es la transformacion pura. Es la transformacion con estatus, evidencia, decision, permiso, alcance, invariante y verificacion.

## Alcance

Este documento incorpora el marco inicial de `AO-001` y las fuentes previas relacionadas con AAU/R4, Gamma, modelos, mutaciones y equivalencia.

No convierte automaticamente esas fuentes en Canon.

No autoriza transformaciones materiales.

No cierra Confluencia, Equivalencia de proyecciones, P-108, P-200, R4 global ni Gamma global.

## Capas algebraicas

La Algebra Operacional se organiza en cinco capas:

1. Algebra de artefactos locales.
2. Algebra de auditoria de modelos.
3. Algebra de trazas y decisiones fundadas.
4. Algebra de generalizacion controlada.
5. Algebra de mutaciones y equivalencia de modelos.

Estas capas pueden interactuar, pero ninguna promueve por si misma el estatus de otra.

## Objetos operacionales de artefacto

| Simbolo | Lectura | Estatus |
| --- | --- | --- |
| `A` | artefacto local | objeto operacional |
| `S` | estatus de afirmacion o artefacto | objeto operacional |
| `E` | evidencia local materializada | objeto operacional |
| `C` | contexto declarado de aplicacion | objeto operacional |
| `R` | reporte estructurado | objeto operacional |
| `D` | decision emitida | objeto operacional |
| `P` | permiso acotado | objeto operacional |
| `I` | invariante declarado | objeto operacional |
| `T` | transformacion propuesta o ejecutada | objeto operacional |
| `B` | bloqueo, deuda o problema abierto | salida de seguridad |

Estos objetos son tipos de trabajo para ordenar operaciones. Su formalizacion completa queda abierta.

## Objetos de auditoria de modelos

| Simbolo | Lectura | Estatus |
| --- | --- | --- |
| `G` | modelo auditado | notacion historica incorporada |
| `F` | firma estructural | notacion historica incorporada |
| `Presv` | firmas preservables | notacion historica incorporada |
| `Activas(G)` | afirmaciones activas del modelo | notacion historica incorporada |
| `Inv(G)` | invariantes satisfechos | objeto derivado |
| `G_I` | grafo de acoplamiento de invariantes | objeto derivado |
| `Break(F_k)` | componente de ruptura | objeto derivado |
| `AAU` | Algoritmo de Auditoria Unico | motor historico |
| `R4_Break` | propagacion de ruptura sobre `G_I` | lectura historica de R4 |

## Objetos de traza

Una traza operacional es:

```text
rho = <e_1, e_2, ..., e_n>
```

donde cada `e_i` puede ser reporte, decision, propuesta, ejecucion, fallo o verificacion.

La relacion:

```text
antes(e_i, e_j, rho)
```

indica que `e_i` aparece antes que `e_j` en la traza.

## Operadores base del Auditor

La primera base operacional local viene del Auditor v0:

```text
Mp -> Cr -> tau -> D -> Tr
```

Lectura:

| Operador | Forma provisional | Funcion |
| --- | --- | --- |
| `Mp` | `Mp(A) = M` | mapea un artefacto a una estructura legible |
| `Cr` | `Cr(M) = R` | calcula o verifica sobre la estructura mapeada |
| `tau` | `tau(R) = cierre` | decide terminacion, bloqueo o escalamiento |
| `D` | `D(R, cierre) = d` | emite decision restringida por evidencia previa |
| `Tr` | `Tr(A, d, P) = A'` | propone o ejecuta transformacion solo si hay permiso valido |

Regla:

```text
Tr(A, d, P) = A'
```

solo esta bien formada como ejecucion si `P` declara `transformacion_permitida = true`, existe alcance acotado, evidencia previa, evidencia posterior y verificacion posterior.

Si falta cualquiera de esas condiciones, la salida es `B`, no `A'`.

## Operador R4 historico

Sobre el nucleo AAU/R4:

```text
R4_Break(F_k, G_I) = Break(F_k)
```

donde `Break(F_k)` es la componente conexa de `F_k` en `G_I`.

Estados asociados:

- sin ruptura: `APROBADO`;
- ruptura sin conflicto con `Activas(G)`: `SUSPENDIDO`;
- interseccion entre `Activas(G)` y `Break(F_k)`: `INCONSISTENTE`;
- falta de estructura decidible: `NO AUDITABLE`.

Esta lectura queda incorporada como base historica, no como Regla R4 canonica global.

## Operador R4 formal local

`AUD-001` define:

```text
R4_AUD(rho) := para todo t:
  si ejecucion(t) en rho,
  entonces valida(t, rho)
```

Una ejecucion `t` es valida si existe decision fundada previa, alcance, evidencia previa, evidencia posterior, verificacion posterior e invariante declarado.

Uso dentro de Algebra Operacional:

- `R4_AUD` sirve como criterio local de validez de transformaciones en trazas.
- No autoriza transformaciones por si mismo.
- No promueve R4 fuera de `AUD-001`.

## Operador Gamma formal local

`AUD-001` define `Gamma` como operador parcial local:

```text
Gamma_AUD(E, C, W) = G
```

si `WF(E, C, W)` se satisface.

`E` es paquete de evidencia, `C` es contexto, `W` es testigo de generalizacion y `G` es salida generalizada con forma, estatus, invariantes, restricciones, deudas y autoridad.

Instancia operativa:

```text
Gamma_1(E, C) = Gamma_AUD(E, C, W)
```

cuando `W` esta declarado.

Uso dentro de Algebra Operacional:

- generaliza evidencia local bajo contexto;
- conserva o reduce permiso;
- no produce Canon;
- no produce Nivel C;
- no produce documento oficial;
- no produce permiso de transformacion;
- si falla, devuelve bloqueo, deuda o problema abierto.

## Algebra historica de mutaciones

`SRC-023` conserva una algebra de mutaciones con modelo preliminar:

```text
M = <P, G>
```

donde:

- `P`: restricciones primitivas;
- `G`: reglas generadoras.

Mutaciones internas candidatas:

- `+P`: anadir restriccion primitiva;
- `-P`: eliminar restriccion primitiva;
- `+G`: anadir regla generadora;
- `-G`: eliminar regla generadora.

Estas mutaciones quedan incorporadas como vocabulario operacional historico, no como reglas ejecutables vigentes.

## Arquitectura candidata `M = <Omega, Xi>`

`SRC-023` tambien registra una arquitectura candidata:

```text
M = <Omega, Xi>
```

donde:

- `Omega`: dominio operacional o espacio de posibilidades;
- `Xi`: operador de acoplamiento distincion-restriccion.

Operaciones candidatas:

- `Phi`: operador de evaluacion;
- `Psi`: operador de revision o metaevaluador del Laboratorio.

Frontera:

- `Xi` no queda admitido al Canon por este documento;
- `Omega` no queda demostrado como dominio independiente;
- `Phi` y `Psi` son operadores candidatos;
- la relacion con `H-Xi`, `P-107` y `H-107.1` sigue abierta.

## Viabilidad mutacional

Problema `P-108`:

```text
Dada una mutacion mu, bajo que condiciones el modelo resultante M' permanece dentro de la variedad de modelos viables?
```

Forma tentativa incorporada:

```text
viable(mu) si balance(
  ganancia_restriccion_util,
  error_empirico,
  costo_formal,
  perdida_informacion
) > 0
```

Estatus: problema abierto. No existe todavia regla algebraica consolidada que determine viabilidad de una mutacion.

## Equivalencia operacional entre modelos

Problema `P-200`:

```text
Cuando dos modelos diferentes son, operacionalmente, el mismo modelo?
```

Hipotesis historica incorporada:

```text
M1 == M2 si Phi_M1(O) = Phi_M2(O)
para toda observacion admisible O
```

Estatus: problema abierto. No demuestra equivalencia formal total ni sustituye el frente de Equivalencia de proyecciones.

## Invariantes operacionales

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

## Salidas operacionales

Una operacion debe producir una de estas salidas:

- `continuar_sin_transformar`;
- `bloquear`;
- `escalar`;
- `proponer_cambio_acotado`;
- `ejecutar_cambio_acotado` solo con permiso valido;
- `registrar_deuda`;
- `registrar_problema_abierto`;
- `emitir_candidata_provisional`.

Las salidas AAU/R4 historicas se conservan para auditoria de modelos:

- `APROBADO`;
- `SUSPENDIDO`;
- `INCONSISTENTE`;
- `NO AUDITABLE`.

## Antipatrones

- Usar una salida correcta como autorizacion.
- Promover un operador local a regla general por analogia.
- Llamar transformacion a una recomendacion.
- Llamar verificacion a una lectura sin criterio.
- Llamar `Gamma` a cualquier generalizacion narrativa.
- Tratar `R4_Break` o `R4_AUD` como Regla R4 canonica global.
- Otorgar autoridad vigente al registro historico sin decision.
- Cerrar una deuda conceptual por ejecucion.
- Ejecutar cambios de nivel superior desde evidencia de nivel inferior.

## Criterio de buena formacion operacional

Una operacion `Op` esta bien formada si declara:

- objetos de entrada;
- contexto;
- estatus de entrada;
- operador aplicado;
- salida esperada;
- salida segura si falla;
- evidencia usada;
- autoridad de la fuente;
- permiso requerido;
- invariantes preservados;
- verificacion posterior si hay transformacion.

Si falta cualquiera de estos elementos y la operacion pretende modificar un artefacto, debe bloquearse o degradarse a propuesta.

## Preguntas abiertas

- Que tipos formales minimos necesita la Algebra Operacional?
- Conviene separar algebra de lectura, algebra de decision y algebra de transformacion?
- La verificacion posterior debe ser operador formal propio o condicion de `Tr`?
- Como se expresa composicion de operadores sin ocultar permisos?
- Que relacion hay entre confluencia local y preservacion de invariantes?
- Que equivalencias de proyeccion bastan para pasar de expediente a documento oficial?
- Como se integra `M = <Omega, Xi>` sin admitir `H-Xi` indebidamente?
- Como se formaliza `P-108` sin convertir costo formal en criterio unico?
- Como se prueba `P-200` contra casos no triviales?

## Siguiente trabajo

El siguiente avance natural es crear una bateria `AO-CASE` para probar:

- caso positivo sin transformacion;
- propuesta de cambio sin permiso;
- ejecucion valida con permiso acotado;
- bloqueo por reporte bloqueante;
- generalizacion `Gamma_AUD` sin promocion;
- mutacion candidata que queda como problema abierto;
- equivalencia operacional fallida por observacion admisible.

## Estado

Documento 04 deja de estar reservado y queda actualizado como version inicial consolidada de Algebra Operacional.

Permanece abierto el trabajo de formalizacion, casos y eventuales promociones futuras.
