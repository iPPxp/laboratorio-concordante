# AUD-001 - Relacion Gamma ruta 1 y R4 formal

Estatus: relacion provisional de expediente.

Fecha: 2026-07-03.

ID: `REL-GAMMA-R4-001`.

Expediente padre: `AUD-001`.

## Proposito

Precisar como se relacionan `Gamma_1`, `R4-CANDIDATA` y una eventual Regla R4 formal sin promover ninguna por implicacion.

## Relacion minima

La relacion vigente es:

```text
R4-CANDIDATA -> evidencia local posible para Gamma_1
R4-FORMAL-AUD-001 -> regla formal local de expediente
Gamma_1(E, C) -> instancia operativa de Gamma_AUD
G -> salida local con limites
R4 canonica u oficial -> no creada
```

`Gamma_1` puede usar `R4-CANDIDATA` como evidencia `E` porque esta candidata ya tiene fuentes locales, pruebas no automata, auditorias y decisiones de estatus dentro de `AUD-001`.

`Gamma_1` no convierte esa evidencia en Regla R4 formal.

Precision posterior: `R4-FORMAL-AUD-001` fue construido en `AUD-001_R4_Formal_Local.md` y aceptado localmente por `D-2026-07-03-010`. Esto reemplaza la deuda local de construir R4 formal dentro de `AUD-001`, pero no crea Regla R4 canonica u oficial.

## Uso permitido

`Gamma_1` puede producir una salida provisional como:

```text
G_R4_PROC-CAND-001 = {
  tipo: hipotesis_operativa_de_expediente,
  base: R4-CANDIDATA,
  contexto: procedimientos auditables con reportes, decision y transformacion,
  afirmacion: transformar requiere decision fundada, reportes suficientes, terminacion segura, permiso acotado, evidencia y verificacion posterior,
  estatus: provisional,
  permiso_material: ninguno
}
```

Esta salida puede servir para:

- refinar deudas;
- formular criterios de prueba;
- comparar controles positivos y negativos;
- preparar una ruta futura de R4 formal;
- decidir que falta antes de cualquier promocion.

## Uso no permitido

La relacion no permite:

- llamar `R4-CANDIDATA` Regla R4 formal;
- llamar `G_R4_PROC-CAND-001` teorema;
- modificar Canon, `C-001` o `C-002`;
- promover `REPORT_LAYER` a Nivel C;
- convertir `Gamma_1` en permiso de transformacion;
- cerrar la deuda de R4 formal;
- cerrar la construccion formal de `Gamma`.

## Frontera con R4 formal

R4 formal local dentro de `AUD-001` queda cubierto por `R4-FORMAL-AUD-001`.

Una Regla R4 canonica u oficial fuera de `AUD-001` requeriria, como minimo, una forma propia para:

- declarar premisas generales;
- declarar dominio de aplicacion;
- declarar restricciones de operadores;
- especificar condiciones de satisfaccion y violacion;
- probar o validar que la forma no depende solo de ejemplos;
- decidir su estatus documental.

`Gamma_1` puede sugerir una forma candidata a partir de evidencia local.

Esa sugerencia no satisface por si misma los requisitos anteriores.

## Relacion con AUD-SIM-025

`AUD-SIM-025` sigue siendo el control negativo: bloquea una invocacion de `Gamma` como resultado formal o generalizacion canonica.

`AUD-SIM-030` funciona como control positivo acotado: valida que `Gamma_1` puede operar si la evidencia, el contexto, los invariantes, las restricciones y el estatus provisional estan declarados.

## Veredicto

`REL-GAMMA-R4-001` permite usar `Gamma_1` y `Gamma_AUD` para ordenar la relacion entre evidencia local, R4 formal local y salidas generalizadas.

No autoriza R4 canonica, R4 oficial, `Gamma` canonica ni `Gamma` fuera de `AUD-001`.
