# AUD-001 - R4 formal local

Estatus: construccion formal local de expediente.

Fecha: 2026-07-03.

ID: `R4-FORMAL-AUD-001`.

Expediente padre: `AUD-001`.

## Proposito

Construir una forma formal local de `R4` dentro de `AUD-001`, usando la evidencia ya registrada por `R4-CANDIDATA`, `REPORT_LAYER`, `C-002` y las validaciones del Auditor.

Esta construccion no es Canon, no modifica documentos oficiales y no convierte `R4-CANDIDATA` en regla fuera de `AUD-001`.

## Fuentes locales

- `01_Canon/M-000_Reglas_Fundamentales.md`
- `01_Canon/M-001_Auditoria_Arquitectonica.md`
- `02_Documentos/C-002_RFC_Operativo_Auditor_v0.md`
- `03_Expedientes/AUD-001_R4-CANDIDATA.md`
- `03_Expedientes/AUD-001_REPORT_LAYER_Candidata.md`
- `03_Expedientes/AUD-001_Relacion_Gamma_Ruta1_R4_Formal.md`
- `03_Expedientes/AUD-001_Simulaciones.md`
- `03_Expedientes/AUD-001_Validaciones.md`

## Dominio formal local

Sea `A` el conjunto de artefactos locales auditables.

Sea `R` el conjunto de reportes normalizados compatibles con `REPORT_LAYER`.

Sea `D` el conjunto de decisiones emitibles por el Auditor:

```text
D = {
  bloquear,
  escalar,
  continuar_sin_transformar,
  registrar_propuesta,
  continuar_con_cambio_acotado
}
```

Sea `T` el conjunto de transformaciones documentales o materiales posibles sobre artefactos.

Sea `I` el conjunto de invariantes declarables antes de una transformacion.

Una traza local es una secuencia finita:

```text
rho = <e_1, e_2, ..., e_n>
```

donde cada evento `e_i` puede ser reporte, decision, propuesta, ejecucion, fallo o verificacion.

La relacion `antes(e_i, e_j, rho)` significa que `e_i` aparece antes que `e_j` en la traza.

## Predicados basicos

```text
reporte(e)
decision(e)
ejecucion(e)
verificacion(e)
bloqueante(e)
terminacion_segura(e)
permite_transformacion(e)
alcance(e)
invariante(e)
evidencia_previa(e)
evidencia_posterior(e)
```

`compatible(e, d)` significa que el evento `e` no contradice la decision `d`.

`subalcance(t, d)` significa que la transformacion `t` no excede el alcance autorizado por `d`.

`verifica(v, i, a, a')` significa que la verificacion `v` confirma el invariante `i` entre el estado previo `a` y el estado posterior `a'`.

## Decision fundada

Una decision `d` esta fundada en una traza `rho` para una transformacion posible `t` si y solo si:

1. `decision(d)`;
2. `d` aparece antes que `t`;
3. existe al menos un reporte de mapeo o lectura antes de `d`;
4. existe al menos un reporte de calculo, verificacion o falla normalizada antes de `d`;
5. existe un cierre de terminacion antes de `d`;
6. ningun reporte bloqueante anterior a `d` queda sin reflejo en la decision;
7. `d = continuar_con_cambio_acotado`;
8. `permite_transformacion(d) = true`;
9. `alcance(d)` esta declarado;
10. si el cambio no es trivial, existe `invariante(d)` declarado antes de ejecutar.

Forma:

```text
fundada(d, t, rho)
```

## Ejecucion valida

Una ejecucion `t` es valida en `rho` si y solo si:

1. `ejecucion(t)`;
2. existe una decision `d` tal que `fundada(d, t, rho)`;
3. `subalcance(t, d)`;
4. existe evidencia previa `a`;
5. existe evidencia posterior `a'`;
6. existe una verificacion `v` posterior a `t`;
7. existe un invariante `i` declarado antes de `t`;
8. `verifica(v, i, a, a')`;
9. ninguna fuente de nivel inferior se usa como autoridad directa para modificar una fuente de nivel superior.

Forma:

```text
valida(t, rho)
```

## Regla R4 formal local

`R4-FORMAL-AUD-001` se satisface sobre una traza `rho` si y solo si toda ejecucion registrada en `rho` es valida:

```text
R4_AUD(rho) := para todo t:
  si ejecucion(t) en rho,
  entonces valida(t, rho)
```

Forma equivalente:

```text
R4_AUD(rho) :=
  forall t in rho.
    ejecucion(t) -> exists d, a, a', v, i.
      antes(d, t, rho)
      and fundada(d, t, rho)
      and subalcance(t, d)
      and evidencia_previa(a, t)
      and evidencia_posterior(a', t)
      and antes(t, v, rho)
      and verifica(v, i, a, a')
```

## Teorema local de seguridad

Teorema `R4-SAFE-001`:

Si `R4_AUD(rho)` se satisface, entonces no hay transformacion ejecutada valida sin decision fundada previa.

## Demostracion local

Por definicion, `R4_AUD(rho)` exige que para toda `t` con `ejecucion(t)` exista una decision `d` anterior a `t` tal que `fundada(d, t, rho)`.

La definicion de `valida(t, rho)` incluye esa decision fundada como condicion necesaria.

Por tanto, si una transformacion no tiene decision fundada previa, no satisface `valida(t, rho)`.

Luego, bajo `R4_AUD(rho)`, ninguna transformacion ejecutada sin decision fundada previa puede contar como valida.

## Casos de violacion

`R4_AUD(rho)` falla si ocurre cualquiera de estos patrones:

- `t` se ejecuta sin decision previa;
- `t` se ejecuta con una decision que no declara alcance;
- `t` excede el alcance de la decision;
- `t` se apoya en reporte bloqueante no reflejado en `D`;
- `t` usa recomendacion como decision;
- `t` no registra evidencia previa o posterior;
- `t` no tiene verificacion posterior;
- `t` cierra una deuda conceptual por ejecucion;
- `t` modifica Canon o documento oficial desde expediente sin decision de nivel.

## Relacion con R4-CANDIDATA

`R4-CANDIDATA` queda absorbida solo como antecedente local de construccion.

La diferencia de estatus es:

```text
R4-CANDIDATA = hipotesis operativa robustecida
R4-FORMAL-AUD-001 = construccion formal local de expediente
Regla R4 canonica u oficial = no creada
```

## Relacion con Gamma

`R4-FORMAL-AUD-001` puede funcionar como evidencia formal local para `Gamma`.

Esto no significa que `Gamma` promueva `R4` fuera de `AUD-001`.

## No cubre

Esta construccion no cubre:

- promocion a Canon;
- promocion a Nivel C;
- implementacion ejecutable obligatoria;
- prueba global fuera de trazas locales;
- transformacion material;
- cierre de otros problemas matematicos.

## Veredicto

`R4-FORMAL-AUD-001` construye una Regla R4 formal local de expediente.

La deuda "definir formalmente R4 dentro de AUD-001" queda atendida localmente, pero toda promocion fuera de `AUD-001` sigue requiriendo auditoria y decision separadas.
