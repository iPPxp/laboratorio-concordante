# AO-001 - Formalizacion acotada en Documento 04

Estatus: incorporacion documental acotada.

Fecha: 2026-07-05.

ID: `AO-DOC04-FORM-001`.

Expediente padre: `AO-001`.

Documento modificado: `02_Documentos/04_Algebra_Operacional.md`.

Decision: `D-2026-07-05-008`.

## Proposito

Incorporar al Documento 04 una formalizacion minima de `Pi_tb` y `Eq_tb` como proyeccion tabular local bajo testigo, sin convertirla en cierre global de Equivalencia de proyecciones, Confluencia o `P-200`.

## Evidencia usada

- `R001-TABLE-CHECK-001`: 20 chequeos tabulares, 20 aprobados, 0 fallos.
- `R001-TB-001`: relacion formal local entre `R001-TABLE-CHECK-001` y `AO-PPI-BRIDGE-001`.
- `AO-DOC04-FORM-CHK-001`: evaluacion previa de ruta para Documento 04.
- `AO-EXT-CONF-EXEC-001`: ejecucion de `EXT-CONF-001` y `EXT-CONF-002`, con 7 casos aprobados y 0 fallos.
- `DO-LAB-RISK-001`: riesgo activo 0 en la corrida previa a la incorporacion.

## Texto incorporado

Se incorpora al Documento 04 la seccion:

```text
## Proyeccion tabular local bajo testigo
```

La seccion define:

```text
C = (Omega, Phi, Pi, T)
Pi_tb(C, O_adm) = {(o, Phi(o)) | o en O_adm}
Eq_tb(C1, C2, O_adm) <=> Pi_tb(C1, O_adm) = Pi_tb(C2, O_adm)
```

## Condiciones de validez

La incorporacion solo es valida bajo estas condiciones:

1. `O_adm` debe estar declarado como testigo.
2. La equivalencia resultante depende de `O_adm`.
3. El reporte debe conservar estatus, evidencia y deuda abierta.
4. La construccion no autoriza transformaciones materiales.
5. La construccion no promueve `Xi`, `R4` ni `Gamma`.
6. La construccion no cierra problemas globales.

## Alcance

La formalizacion permite usar `Pi_tb` como instancia local de proyeccion operacional y `Eq_tb` como equivalencia local bajo testigo dentro de la Algebra Operacional.

## No cubre

No cubre:

- cierre de `P-200`;
- cierre de `P-107`;
- cierre de Confluencia global;
- cierre de Equivalencia global de proyecciones;
- admision formal de `H-Xi`;
- canonizacion de `Xi`;
- exportacion general de R4/Gamma;
- creacion de Nivel C;
- permiso de transformacion.

## Deudas que permanecen abiertas

- definir si habra una especificacion posterior de proyecciones/reportes;
- probar equivalencias no triviales fuera de tablas locales;
- conectar `Pi_tb` con casos mas fuertes de Confluencia;
- decidir si una futura capa `REPORT_LAYER` debe absorber parte de esta notacion;
- mantener separada la equivalencia local bajo testigo de la Equivalencia global de proyecciones.
