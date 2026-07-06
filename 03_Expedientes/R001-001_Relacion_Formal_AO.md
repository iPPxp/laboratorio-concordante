# R001-001 - Relacion formal con AO

Estatus: relacion formal local cerrada.

Fecha: 2026-07-05.

ID: `R001-TB-001`.

Expediente padre: `R001-001`.

Puente AO relacionado: `AO-PPI-BRIDGE-001`.

Herramienta ejecutable relacionada: `R001-TABLE-CHECK-001`.

## Proposito

Precisar como los chequeos tabulares `R-001` / `Xi` se conectan formalmente con `AO-001` sin convertirlos en Canon, teorema global o cierre de problemas abiertos.

`R001-TB-001` define una relacion local entre:

- un acoplamiento tabular `C = (Omega, Phi, Pi, T)`;
- un conjunto de observaciones admitidas `O_adm`;
- una proyeccion operacional tabular;
- el puente `AO-PPI-BRIDGE-001`.

## Forma local

Sea:

```text
C = (Omega, Phi, Pi, T)
```

donde:

- `Omega` es el soporte observado;
- `Phi` es la regla de lectura o evaluacion;
- `Pi` es el conjunto de piezas visibles para la prueba;
- `T` es la relacion efectiva de transiciones;
- `O_adm` es el testigo de observaciones admitidas.

La proyeccion tabular local se define como:

```text
Pi_tb(C, O_adm) = {(o, Phi(o)) | o en O_adm}
```

La equivalencia tabular local queda:

```text
Eq_tb(C1, C2, O_adm) <=> Pi_tb(C1, O_adm) = Pi_tb(C2, O_adm)
```

con tres restricciones:

- `O_adm` debe estar declarado y no vacio;
- la equivalencia depende del testigo elegido;
- equivalencia por solo pertenencia de dominio se marca como trivial, no como cierre fuerte.

## Correspondencia con AO

| Elemento R001 | Lectura AO local | Funcion |
| --- | --- | --- |
| `Omega` | soporte operacional observado | delimita el dominio local de lectura |
| `Phi` | proyeccion operacional local | produce salida legible por caso |
| `Pi` | piezas visibles del artefacto | evita comparar material no declarado |
| `T` | relacion efectiva | permite leer delta sin transformacion |
| `O_adm` | testigo compartido | fija alcance de equivalencia |
| `Pi_tb` | `Pi_op` tabular | instancia local de proyeccion operacional |
| `Eq_tb` | equivalencia local bajo testigo | instancia acotada de `AO-PPI-EQ-001` |
| `decouple_status` | compuerta operacional local | separa alcance, equivalencia y costo |
| reporte `R001` | ruta de reporte | evidencia para confluencia local |

## Relacion con Equivalencia de proyecciones

`R001-TB-001` aporta una instancia local para `AO-PPI-EQ-001`:

```text
Pi_doc(A) ~ Pi_rep(A) ~ Pi_op(A)
```

En este caso:

```text
Pi_op(A) = Pi_tb(C, O_adm)
```

La equivalencia local pasa solo si la lectura documental, el reporte generado y la proyeccion tabular conservan:

- identificador de caso;
- testigo `O_adm`;
- salida esperada;
- estatus `equivalent`, `non_equivalent`, `trivial_equivalence` o bloqueo local;
- ausencia de permiso de transformacion.

## Relacion con Confluencia

`R001-TB-001` aporta una instancia local para `AO-PPI-CONF-001`:

```text
ruta_estado(A) + ruta_decision(A) + ruta_reporte(A) -> salida compatible
```

En este caso hay confluencia local si:

- la ruta de estado conserva `R001-001` como expediente tecnico provisional;
- la ruta de decision conserva `D-2026-07-05-004` y la decision posterior de `R001-TB-001`;
- la ruta de reporte conserva `R001-TABLE-CHECK-001` como `ok`;
- las tres rutas comparten el mismo testigo local;
- ninguna ruta aumenta autoridad ni transforma artefactos.

## Casos cubiertos

`R001-TB-001` cubre la relacion local con `AO-001` para:

- equivalencia dependiente de `O_adm`;
- no equivalencia por cambio de observacion admitida;
- equivalencia trivial por solo pertenencia de dominio;
- bloqueo por falta de equivalencia;
- bloqueo por costo no menor;
- lectura de delta sin mutacion;
- reporte ejecutable sin permiso material.

## No cubre

`R001-TB-001` no:

- canoniza `Xi`;
- admite `H-Xi`;
- declara `Xi` operador vigente;
- cierra `P-200`;
- resuelve `P-107`;
- cierra Equivalencia global de proyecciones;
- cierra Confluencia global;
- produce cambios al Canon;
- produce cambios a documentos oficiales;
- produce cambios de Nivel C;
- incorpora resultados al Documento 04;
- autoriza transformaciones materiales.

## Resultado

`R001-TB-001` cierra la deuda local de relacion formal entre `R001-TABLE-CHECK-001` y `AO-PPI-BRIDGE-001`.

Permanecen abiertas la Equivalencia global, la Confluencia global y cualquier incorporacion posterior al Documento 04.

Nota posterior 2026-07-06: `R001-001` queda cerrado tecnicamente por `D-2026-07-06-009`. `R001-TB-001` se conserva como relacion formal local aceptada con `AO-PPI-BRIDGE-001`, sin mantener abierto el expediente.
