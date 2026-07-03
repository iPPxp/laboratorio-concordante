# AUD-001 - Gamma ruta 1: definicion local provisional

Estatus: definicion provisional de expediente.

Fecha: 2026-07-03.

ID: `GAMMA-DEF-001`.

Expediente padre: `AUD-001`.

Ruta: `GAMMA-RUTA-1`.

## Proposito

Definir localmente que puede significar `Gamma` dentro de `AUD-001` sin convertirla todavia en teorema, Canon, documento oficial, Regla R4 formal ni contrato obligatorio para otros frentes.

Esta ruta atiende el primer punto permitido por `AUD-001_Ficha_Alcance_Gamma.md`: una definicion local de la construccion.

## Definicion provisional

`Gamma` es una operacion de generalizacion controlada que toma una evidencia local ya auditada y produce una forma candidata de aplicacion mas general, siempre con sus condiciones, invariantes, limites y deudas visibles.

Forma minima:

```text
Gamma_1(E, C) = G
```

Donde:

- `E` es evidencia local registrada dentro del Laboratorio.
- `C` es el contexto declarado de aplicacion.
- `G` es una generalizacion candidata, no una verdad canonica.

`Gamma_1(E, C)` solo queda bien formada si puede registrar:

1. fuente local de `E`;
2. estatus de `E`;
3. contexto `C`;
4. invariantes que se conservan al generalizar;
5. restricciones que no pueden omitirse;
6. deudas que quedan abiertas;
7. salida segura si la generalizacion falla.

## Lectura dentro de AUD-001

Dentro del Auditor, `Gamma` no significa "generalizacion canonica".

Significa:

```text
tomar una estructura local validada
-> declarar que parte se intenta generalizar
-> declarar bajo que contexto se conserva
-> declarar que no se conserva
-> producir una candidata con estatus provisional
```

## Condiciones de aplicacion

`Gamma_1(E, C)` puede aplicarse solo si:

- `E` esta materializada en un archivo local;
- `E` tiene estatus declarado;
- `E` no depende del Registro Historico como autoridad directa;
- `C` esta delimitado antes de generalizar;
- existe al menos un invariante local explicitado;
- las restricciones de nivel quedan visibles;
- la salida no aumenta permisos de transformacion.

## Salidas permitidas

La salida `G` puede tener uno de estos estatus:

- hipotesis operativa de expediente;
- definicion provisional de expediente;
- criterio provisional de expediente;
- deuda conceptual refinada;
- problema abierto delimitado.

`G` no puede salir como:

- Canon;
- teorema;
- documento oficial;
- Regla R4 formal;
- permiso de transformacion;
- cierre de problema abierto.

## Salidas de seguridad

Si falta fuente local, contexto, invariante, estatus o restriccion, la operacion no produce `G`.

La salida debe ser una de estas:

- `gamma_bloqueada_por_fuente_ausente`;
- `gamma_bloqueada_por_contexto_ausente`;
- `gamma_bloqueada_por_invariante_ausente`;
- `gamma_degradada_a_deuda`;
- `gamma_degradada_a_problema_abierto`.

## Relacion con R4-CANDIDATA

`R4-CANDIDATA` puede aportar evidencia para `Gamma_1`, porque ya dispone de pruebas no automata y de una capa local `REPORT_LAYER`.

Pero `Gamma_1` no convierte `R4-CANDIDATA` en Regla R4 formal.

Precision posterior: la relacion local queda detallada en `AUD-001_Relacion_Gamma_Ruta1_R4_Formal.md` (`REL-GAMMA-R4-001`). Esa ficha permite usar `R4-CANDIDATA` como evidencia `E` y producir una salida candidata `G_R4_PROC-CAND-001`, sin cerrar R4 formal.

La relacion permitida es:

```text
R4-CANDIDATA = evidencia local posible
Gamma_1 = generalizacion candidata controlada
R4 formal = deuda separada
```

## Relacion con AUD-SIM-025 y VAL-025

`AUD-SIM-025` y `VAL-025` siguen siendo validos para bloquear cualquier uso de `Gamma` como teorema o resultado formal sin construccion local suficiente.

`GAMMA-DEF-001` no invalida ese bloqueo.

Solo cambia la situacion de trabajo:

```text
antes: Gamma invocada sin definicion local -> dependencia no registrada
ahora: Gamma tiene definicion local provisional -> todavia requiere prueba de aplicacion
```

Por tanto, una afirmacion como:

```text
Gamma(A) produce la generalizacion canonica del automata A
```

sigue bloqueada.

Una afirmacion admisible tendria que declarar:

```text
Gamma_1(E, C) produce una generalizacion candidata de expediente con estatus provisional, invariantes y limites declarados.
```

## Criterio minimo de exito

Una aplicacion futura de `Gamma_1` pasa solo si puede responder:

| Pregunta | Exigencia |
| --- | --- |
| Que evidencia local se generaliza? | archivo e identificador |
| Que estatus tiene esa evidencia? | definido antes de aplicar `Gamma_1` |
| Que contexto se declara? | dominio y limites |
| Que invariante se conserva? | formulacion explicita |
| Que no se conserva? | restricciones y exclusiones |
| Que permiso produce? | ninguno, salvo decision posterior separada |
| Que pasa si falla? | deuda o problema abierto, no teorema |

## No cubre

Esta definicion no cubre:

- demostracion formal de `Gamma`;
- sintaxis completa para todas las rutas futuras;
- validacion ejecutable;
- promocion a Nivel C;
- modificacion de `C-001` o `C-002`;
- cierre de la deuda `Construccion formal de Gamma`;
- cierre de `R4` formal;
- autoridad para otros expedientes.

## Deudas abiertas

- Probar `Gamma_AUD` fuera de `AUD-001` si se busca exportacion.
- Definir si una ruta posterior requiere `GAMMA-REPORT` o basta `REPORT_LAYER`.
- Decidir si `R4-FORMAL-AUD-001` debe permanecer local o preparar promocion.
- Decidir si `GAMMA-FORMAL-AUD-001` debe permanecer local o preparar promocion.

## Veredicto

`GAMMA-DEF-001` establece una primera definicion local provisional.

La ruta de `Gamma` ya tiene definicion local provisional, primer caso positivo validado por `VAL-030`, segunda prueba positiva validada por `VAL-031` y construccion formal local en `GAMMA-FORMAL-AUD-001`.
