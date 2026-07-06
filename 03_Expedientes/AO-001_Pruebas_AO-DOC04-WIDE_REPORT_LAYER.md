# AO-001 - Pruebas de AO-DOC04-WIDE-001 y REPORT_LAYER

Identificador: `AO-DOC04-WIDE-TEST-001`.

Estatus: prueba local no mutante aceptada.

Fecha: 2026-07-06.

Decision: `D-2026-07-06-007`.

Herramienta: `06_Automatizacion/ao_doc04_wide_tests.py`.

Fixture: `06_Automatizacion/fixtures/ao_doc04_wide_cases.json`.

Reportes: `06_Automatizacion/reportes/ao_doc04_wide_report.md` y `06_Automatizacion/reportes/ao_doc04_wide_report.json`.

## Proposito

Probar `AO-DOC04-WIDE-001` contra casos sinteticos no regulados y no mutantes, con atencion especial a la relacion entre `Pi_doc`, `Pi_rep`, `Pi_op`, `Eq_local`, `Conf_local`, `Gate_AO`, R4/Gamma restringidos y `REPORT_LAYER`.

## Casos

| Caso | Operacion | Resultado esperado | Funcion |
| --- | --- | --- | --- |
| `AO-WIDE-001` | `Eq_local` | `equivalencia_local` | `Pi_doc` y `Pi_rep` coinciden bajo testigo con `REPORT_LAYER` completo |
| `AO-WIDE-002` | `Conf_local` | `confluencia_local` | `Pi_op` y `Pi_rep` conservan regla ganadora y deuda visible |
| `AO-WIDE-003` | `Eq_local` | `bloqueo_por_testigo` | falta testigo operativo |
| `AO-WIDE-004` | `Gate_AO` | `no_autorizado_sin_transformar` | recomendacion favorable no equivale a permiso |
| `AO-WIDE-005` | `Eq_local` | `bloqueo_por_autoridad` | una proyeccion de expediente intenta elevarse a Nivel C |
| `AO-WIDE-006` | `Eq_local` | `divergencia_clasificada` | dos proyecciones comparables divergen |
| `AO-WIDE-007` | `R4Gamma_AO` | `bloqueo_exportacion_r4_gamma` | intento de exportacion general R4/Gamma |
| `AO-WIDE-008` | `Eq_local` | `bloqueo_report_layer_incompleto` | `REPORT_LAYER` no conserva campos minimos |

## Resultado de la corrida

Resultado esperado y obtenido:

```text
cases: 8
passed: 8
failed: 0
resultado: ok
transformacion_permitida: false
```

La herramienta queda integrada a `DO-LAB-RUN-001` como paso no mutante `AO-DOC04-WIDE-TEST-001`.

## Lectura de REPORT_LAYER

La prueba conserva esta relacion:

```text
REPORT_LAYER -> Pi_rep(REPORT_LAYER, C, W) -> R_rep | B
```

`REPORT_LAYER` se acepta solo como estructura local de reporte que puede alimentar `Pi_rep`.

No sustituye:

- `Op_AO`;
- decision;
- permiso;
- verificacion posterior;
- Nivel C;
- cierre global de Confluencia o Equivalencia.

## Deudas abiertas

- Probar casos adicionales con reportes heterogeneos reales o semirreales no regulados.
- Precisar si `REPORT_LAYER` requiere serializacion formal si se vuelve interfrente.
- Relacion futura con `C-001` / `C-002` solo mediante decision separada.
- Confluencia global.
- Equivalencia global.
- Exportacion general R4/Gamma, bloqueada por compuerta vigente.

## Estado

`AO-DOC04-WIDE-TEST-001` queda aceptado como prueba local no mutante de Documento 04 amplio v0.

No modifica Canon, no crea Nivel C, no autoriza transformaciones y no cierra problemas globales.
