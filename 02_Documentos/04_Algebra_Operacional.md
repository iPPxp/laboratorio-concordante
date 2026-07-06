# 04 - Algebra Operacional

Estatus: documento oficial actualizado, version amplia v0.

Decision de incorporacion inicial: `D-2026-07-03-011`.

Decision de formalizacion amplia v0: `D-2026-07-06-006`.

Fuentes principales: `AO-001`, `AO-MARCO-001`, `AO-DOC04-FORM-001`, `AO-DOC04-WIDE-001`, `AO-PPI-BRIDGE-001`, `R001-TB-001`, `MOC-AO-BRIDGE-001`, `SRC-010`, `SRC-012`, `SRC-013`, `SRC-023`, `AUD-001_R4_Formal_Local.md`, `AUD-001_Gamma_Formal_Local.md`, `C-001`, `C-002`.

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
| `W` | testigo operativo de comparabilidad o aplicacion | objeto operacional |
| `rho_op` | traza operacional de operador | objeto derivado |
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

## Proyeccion tabular local bajo testigo

Incorporacion acotada por `D-2026-07-05-008`, desde `R001-TB-001`, `AO-DOC04-FORM-CHK-001` y `AO-EXT-CONF-EXEC-001`.

Sea:

```text
C = (Omega, Phi, Pi, T)
```

donde:

- `Omega` es el soporte observado;
- `Phi` es la regla de lectura;
- `Pi` es el conjunto de piezas visibles;
- `T` es la relacion efectiva de transiciones.

Sea `O_adm` un conjunto no vacio de observaciones admitidas y declaradas como testigo.

La proyeccion tabular local es:

```text
Pi_tb(C, O_adm) = {(o, Phi(o)) | o en O_adm}
```

Dos configuraciones `C1` y `C2` son equivalentes bajo el testigo `O_adm` si y solo si:

```text
Eq_tb(C1, C2, O_adm) <=> Pi_tb(C1, O_adm) = Pi_tb(C2, O_adm)
```

Lectura operacional:

- `Pi_tb` es una instancia local de proyeccion operacional bajo testigo declarado.
- `Eq_tb` es una equivalencia local, no una equivalencia global.
- Si `O_adm` solo prueba pertenencia de dominio, la salida es equivalencia trivial y no cierre fuerte.
- Todo uso debe conservar testigo, estatus, evidencia, salida segura, ausencia de permiso material y deuda abierta.

Esta construccion no cierra `P-200`, `P-107`, Confluencia global ni Equivalencia global de proyecciones.

## Formalizacion operacional amplia v0

Incorporacion amplia por `D-2026-07-06-006`, desde `AO-DOC04-WIDE-001`.

La Algebra Operacional usa operadores ejecutables solo cuando declaran contrato, testigo, regla de salida y salida segura. Una formula conceptual no cuenta como operador ejecutable si no especifica combinacion, prioridad, conflicto y salida.

### Contrato comun de operador

Un operador operacional bien formado tiene la forma:

```text
Op_AO := <id, entrada, contexto, testigo, estatus_entrada,
          evidencia, permiso, invariantes, regla,
          salida, salida_segura, deuda, rho_op>
```

donde:

- `entrada` es el artefacto, reporte, decision, traza o paquete de evidencia que se evalua;
- `contexto` delimita el uso permitido;
- `testigo` declara contra que observaciones, reglas o casos se compara la salida;
- `estatus_entrada` conserva la autoridad de origen;
- `evidencia` debe ser localmente ubicable;
- `permiso` solo habilita transformacion si es explicito y acotado;
- `invariantes` declaran lo que no puede perderse;
- `regla` identifica la regla ganadora si hay varias reglas candidatas;
- `salida` es una de las salidas operacionales reconocidas;
- `salida_segura` es la salida obligatoria ante fallo de evidencia, alcance, permiso o autoridad;
- `deuda` registra lo que queda abierto;
- `rho_op` conserva la traza local del operador.

La traza de operador se expresa como:

```text
operator_trace(Op_AO) =
  <precondiciones, reglas_candidatas, regla_ganadora,
   salida_emitida, salida_segura, deuda>
```

`operator_trace` sirve como evidencia local de regla ganadora. No sustituye una demostracion global ni autoriza una transformacion material.

### Proyecciones operacionales

La familia minima de proyecciones es:

```text
Pi_doc(A, C, W) -> R_doc | B
Pi_rep(R, C, W) -> R_rep | B
Pi_op(rho_op, C, W) -> R_op | B
```

Cada salida `R_*` debe declarar forma, estatus, evidencia, autoridad, invariantes, restricciones y deuda. Si falta `C`, `W`, evidencia o estatus, la salida correcta es `B`.

Lectura:

- `Pi_doc` proyecta un artefacto documental sin mutarlo.
- `Pi_rep` proyecta un reporte o resultado de verificacion.
- `Pi_op` proyecta una traza operacional y conserva la regla ganadora.

### Relacion con REPORT_LAYER

Precision local por `D-2026-07-06-007`, desde `AO-REPORT-LAYER-BRIDGE-001` y `AO-DOC04-WIDE-TEST-001`.

`REPORT_LAYER` puede entrar en Algebra Operacional solo como entrada de `Pi_rep`:

```text
Pi_rep(REPORT_LAYER, C, W) -> R_rep | B
```

Lectura:

- `REPORT_LAYER` aporta estructura abstracta de reporte para comparar salidas.
- `REPORT_ITEM` puede servir como evidencia local de reporte si conserva evidencia, estatus, decisiones permitidas, decision emitida, permiso de transformacion y deudas.
- `Pi_rep` puede compararse con `Pi_doc` o `Pi_op` bajo `Eq_local` o `Conf_local`.
- Si `REPORT_LAYER` esta incompleto, la salida correcta es `B`, no equivalencia.

Frontera:

- `REPORT_LAYER` no sustituye `Op_AO`.
- `REPORT_LAYER` no sustituye una decision.
- `REPORT_LAYER` no crea permiso de transformacion.
- `REPORT_LAYER` no sustituye verificacion posterior.
- `REPORT_LAYER` no se promueve a Nivel C por esta relacion.
- `REPORT_LAYER` no exporta R4/Gamma ni cierra Confluencia o Equivalencia global.

### Equivalencia local de proyecciones

La equivalencia local entre dos proyecciones se define bajo testigo:

```text
Eq_local(Pi_a, Pi_b, W) <=> compatible(Pi_a(W), Pi_b(W))
```

`compatible` exige:

- mismo testigo operativo o testigo declaradamente equivalente;
- salidas comparables;
- estatus y autoridad no incrementados;
- invariantes preservados;
- deuda conservada o explicitamente refinada;
- ausencia de permiso material nuevo.

Si cualquiera de estas condiciones falta, `Eq_local` devuelve `B`, `registrar_deuda` o `registrar_problema_abierto`.

`Eq_local` no implica equivalencia global.

### Confluencia local de rutas

Dos rutas operacionales `r1` y `r2` son localmente confluentes bajo testigo si:

```text
Conf_local(r1, r2, W) <=>
  Eq_local(Pi_op(r1, C, W), Pi_op(r2, C, W), W)
  y no_incremento(autoridad, permiso)
  y deuda_preservada_o_refinada
```

La confluencia local solo compara salidas trazadas dentro del testigo. No cierra Confluencia global ni demuestra que toda ruta futura converge.

Si hay dos reglas candidatas en conflicto, gana la regla que:

1. preserva mayor cantidad de invariantes declarados;
2. no aumenta autoridad;
3. no crea permiso de transformacion;
4. deja deuda explicita;
5. bloquea o escala si las condiciones anteriores no distinguen una salida.

### Compuerta de autorizacion operacional

La compuerta comun se expresa como:

```text
Gate_AO(Op_AO, C, E, P) -> autorizado | no_autorizado | B
```

Reglas:

- si falta contexto, evidencia o estatus, la salida es `B`;
- si falta permiso material, la salida puede ser `continuar_sin_transformar`, `proponer_cambio_acotado`, `registrar_deuda` o `bloquear`, pero no `ejecutar_cambio_acotado`;
- si la operacion toca Canon, Nivel C o documento oficial, requiere expediente, auditoria y decision separada;
- si la operacion invoca R4/Gamma fuera de `AUD-001`, aplica la compuerta restringida de `D-2026-07-05-009`.

### Perfil restringido de R4/Gamma en AO

Dentro de Algebra Operacional, R4 y Gamma solo pueden aparecer como perfiles restringidos:

```text
R4_AO_res(rho_op, C, W) -> valido_local | deuda | bloqueo
Gamma_AO_res(E, C, W) -> candidata_local | deuda | bloqueo
```

Uso permitido:

- referencia formal local;
- prueba local controlada;
- puente de problema para equivalencia o confluencia;
- comparacion de trazas bajo testigo.

Uso prohibido:

- promocion canonica;
- cambio de Nivel C;
- permiso de transformacion;
- teorema global;
- cierre de `P-107`, `P-200`, Confluencia global o Equivalencia global.

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
- testigo o razon explicita de ausencia de testigo;
- estatus de entrada;
- operador aplicado;
- salida esperada;
- salida segura si falla;
- evidencia usada;
- autoridad de la fuente;
- permiso requerido;
- invariantes preservados;
- deuda resultante;
- traza de operador cuando hay regla ganadora;
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

El siguiente avance natural, despues de la prueba local inicial aceptada por `D-2026-07-06-007`, es ampliar solo donde haya deuda global o evidencia heterogenea faltante:

- equivalencias heterogeneas adicionales entre `Pi_doc`, `Pi_rep` y `Pi_op`;
- rutas de confluencia local con testigos externos adicionales;
- serializacion o variantes interfrente de `REPORT_LAYER` si una decision futura lo exige;
- criterios de separacion entre cierre local, cierre documental y cierre global;
- maduracion de `TCS-001` sin crear Nivel C;
- una posible especificacion posterior si alguna parte debe pasar a contrato tecnico.

## Estado

Documento 04 deja de estar reservado y queda actualizado como version amplia v0 de Algebra Operacional.

La formalizacion amplia v0 incorpora contratos ejecutables, proyecciones, equivalencia local, confluencia local, compuerta operacional y perfil restringido R4/Gamma.

Permanecen abiertos Confluencia global, Equivalencia global de proyecciones, `P-107`, `P-200`, exportacion general de R4/Gamma, pruebas heterogeneas o serializacion futura de `REPORT_LAYER` si se exige, maduracion de `TCS-001` y eventuales promociones futuras.
