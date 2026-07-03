# AUD-001 - Gamma formal local

Estatus: construccion formal local de expediente.

Fecha: 2026-07-03.

ID: `GAMMA-FORMAL-AUD-001`.

Expediente padre: `AUD-001`.

## Proposito

Construir formalmente `Gamma` como operador parcial local de generalizacion controlada.

Esta construccion toma `GAMMA-DEF-001` como definicion inicial y la convierte en forma formal local, apoyada por `R4-FORMAL-AUD-001`.

No es Canon, no es Nivel C y no autoriza transformaciones materiales.

## Fuentes locales

- `03_Expedientes/AUD-001_Gamma_Ruta1_Definicion_Local.md`
- `03_Expedientes/AUD-001_R4_Formal_Local.md`
- `03_Expedientes/AUD-001_Relacion_Gamma_Ruta1_R4_Formal.md`
- `03_Expedientes/AUD-001_REPORT_LAYER_Candidata.md`
- `03_Expedientes/AUD-001_Simulaciones.md`
- `03_Expedientes/AUD-001_Validaciones.md`
- `01_Canon/M-000_Reglas_Fundamentales.md`
- `01_Canon/M-001_Auditoria_Arquitectonica.md`

## Objetos formales

Un paquete de evidencia es:

```text
E = (S, sigma, V, B)
```

donde:

- `S` es un conjunto no vacio de fuentes locales;
- `sigma` es el estatus declarado de la evidencia;
- `V` es un conjunto de validaciones, auditorias o decisiones locales;
- `B` es el objeto base que se intenta generalizar.

Un contexto es:

```text
C = (dominio, objetivo, nivel, permiso)
```

donde:

- `dominio` delimita donde opera la generalizacion;
- `objetivo` declara que se quiere extraer;
- `nivel` declara el nivel documental;
- `permiso` declara el efecto operativo permitido.

Un testigo de generalizacion es:

```text
W = (p, Inv, Res, Deu, Safe)
```

donde:

- `p` es una proyeccion desde el objeto base hacia una forma candidata;
- `Inv` es el conjunto de invariantes que deben conservarse;
- `Res` es el conjunto de restricciones y exclusiones;
- `Deu` es el conjunto de deudas que permanecen;
- `Safe` es el conjunto de salidas de seguridad si la generalizacion falla.

## Bien formacion

`WF(E, C, W)` se satisface si:

1. todas las fuentes de `S` existen localmente;
2. `sigma` esta clasificado segun `M-000.2`;
3. `V` contiene evidencia local suficiente para el estatus de `B`;
4. `dominio` y `objetivo` estan declarados antes de generalizar;
5. `nivel` no excede el nivel permitido por las fuentes;
6. `permiso = ninguno` salvo decision separada;
7. `p` declara que conserva y que descarta;
8. `Inv` no esta vacio;
9. `Res` incluye separacion de niveles y no promocion automatica;
10. `Safe` contiene una salida no transformativa.

## Operador Gamma formal local

`Gamma_AUD` es una funcion parcial:

```text
Gamma_AUD(E, C, W) = G
```

si y solo si `WF(E, C, W)` se satisface.

La salida es:

```text
G = (forma, sigma_G, Inv, Res, Deu, autoridad)
```

donde:

- `forma = p(B)`;
- `sigma_G` es un estatus local permitido;
- `Inv` son invariantes conservados;
- `Res` son restricciones activas;
- `Deu` son deudas que no se cierran;
- `autoridad = expediente`.

Los estatus permitidos para `sigma_G` son:

- `hipotesis_operativa_de_expediente`;
- `definicion_formal_local_de_expediente`;
- `criterio_formal_local_de_expediente`;
- `deuda_refinada`;
- `problema_abierto_delimitado`.

Los estatus prohibidos para salida automatica son:

- Canon;
- documento oficial;
- Nivel C;
- teorema global;
- permiso de transformacion;
- cierre de problema externo.

## Salida de seguridad

Si `WF(E, C, W)` falla, `Gamma_AUD` no produce `G`.

Debe producir una de estas salidas:

```text
gamma_bloqueada_por_fuente_ausente
gamma_bloqueada_por_estatus_insuficiente
gamma_bloqueada_por_contexto_ausente
gamma_bloqueada_por_invariante_ausente
gamma_degradada_a_deuda
gamma_degradada_a_problema_abierto
```

Ninguna salida de seguridad habilita transformacion material.

## Teorema local de conservacion de permiso

Teorema `GAMMA-SAFE-001`:

Si `Gamma_AUD(E, C, W) = G`, entonces `G` no aumenta el permiso operativo de sus fuentes.

## Demostracion local

Por `WF(E, C, W)`, el componente `permiso` de `C` debe ser `ninguno` salvo decision separada.

La salida `G` fija `autoridad = expediente` y solo permite estatus locales.

Los estatus prohibidos incluyen permiso de transformacion, Canon, documento oficial y Nivel C.

Por tanto, `G` no puede contener un permiso operativo mayor que el declarado en `C`.

Si ese requisito no se cumple, `WF(E, C, W)` falla y `Gamma_AUD` produce salida de seguridad.

Luego, toda salida exitosa de `Gamma_AUD` conserva o reduce permiso.

## Teorema local de trazabilidad

Teorema `GAMMA-TRACE-001`:

Si `Gamma_AUD(E, C, W) = G`, entonces cada invariante de `G` esta trazado a fuentes locales en `S` o queda marcado como deuda.

## Demostracion local

Por `WF(E, C, W)`, `Inv` no puede estar vacio y `p` debe declarar que conserva y que descarta.

La salida `G` copia `Inv` y `Deu`.

Si un invariante no puede sostenerse por `S`, debe pasar a `Deu` o la bien formacion falla.

Por tanto, ningun invariante puede entrar a `G` como fundamento silencioso.

## Relacion con Gamma_1

`Gamma_1` queda como la primera instancia operativa de `Gamma_AUD`:

```text
Gamma_1(E, C) = Gamma_AUD(E, C, W)
```

cuando el testigo `W` se declara explicitamente en el caso de prueba.

## Relacion con R4 formal

`R4-FORMAL-AUD-001` puede ser usado como evidencia formal local para `Gamma_AUD`.

La relacion no es circular:

- `R4-FORMAL-AUD-001` define validez de trazas con transformacion;
- `Gamma_AUD` define como generalizar evidencia local sin aumentar permiso;
- `Gamma_AUD` puede usar `R4-FORMAL-AUD-001` como fuente, pero no lo crea por si misma.

## No cubre

Esta construccion no cubre:

- teoria global de generalizacion;
- prueba fuera de `AUD-001`;
- canonizacion;
- Nivel C;
- implementacion ejecutable obligatoria;
- permiso de transformacion;
- cierre de Confluencia o Equivalencia de proyecciones.

## Veredicto

`GAMMA-FORMAL-AUD-001` construye formalmente `Gamma` como operador parcial local de expediente.

La deuda "construir Gamma formal dentro de AUD-001" queda atendida localmente, pero toda promocion, exportacion o generalizacion fuera del expediente requiere decision separada.
