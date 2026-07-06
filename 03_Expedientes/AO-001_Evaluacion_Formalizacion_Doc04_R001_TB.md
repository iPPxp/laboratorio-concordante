# AO-001 - Evaluacion de formalizacion en Documento 04

Estatus: evaluacion provisional.

Fecha: 2026-07-05.

ID: `AO-DOC04-FORM-CHK-001`.

Expediente padre: `AO-001`.

Relacion evaluada: `R001-TB-001`.

Documento oficial evaluado: `02_Documentos/04_Algebra_Operacional.md`.

Nota posterior: `AO-EXT-CONF-EXEC-001` ejecuto `EXT-CONF-001` y agrego `EXT-CONF-002` por `D-2026-07-05-007`; esto atiende la condicion minima de dos pruebas externas solo en grado local y no autoriza incorporacion automatica a Documento 04.

Nota posterior: `AO-DOC04-FORM-001` queda aceptado por `D-2026-07-05-008` e incorpora `Pi_tb` / `Eq_tb` al Documento 04 solo en grado acotado bajo testigo. Esta incorporacion no cierra `P-200`, `P-107`, Confluencia global ni Equivalencia global.

## Proposito

Evaluar si `R001-TB-001` debe formalizarse ahora dentro del Documento 04 o si debe permanecer como candidata de expediente hasta contar con pruebas externas de Confluencia.

## Evidencia local

El Documento 04 ya contiene:

- objetos operacionales de artefacto;
- operadores base `Mp -> Cr -> tau -> D -> Tr`;
- `R4_AUD` como criterio local de trazas;
- `Gamma_AUD` como operador parcial local;
- arquitectura candidata `M = <Omega, Xi>`;
- problema `P-200` como equivalencia operacional entre modelos;
- invariantes operacionales y salidas seguras.

`R001-TB-001` agrega:

- `C = (Omega, Phi, Pi, T)`;
- `O_adm` como testigo declarado;
- `Pi_tb(C, O_adm)` como proyeccion tabular local;
- `Eq_tb(C1, C2, O_adm)` como equivalencia local bajo testigo;
- relacion con `AO-PPI-EQ-001` y `AO-PPI-CONF-001`.

La herramienta `R001-TABLE-CHECK-001` reporta 20 chequeos, 20 aprobados y 0 fallos.

## Diagnostico

La formalizacion es madura para quedar como candidata de Documento 04.

No es madura todavia para incorporarse al Documento 04 oficial porque:

- `R001-TB-001` solo cubre una instancia tabular local;
- falta probar criterios de Confluencia fuera del Laboratorio;
- `P-200` sigue abierto;
- Equivalencia global de proyecciones sigue abierta;
- Confluencia global sigue abierta;
- falta decidir si `Pi_tb` debe vivir en Documento 04 o en una especificacion posterior de proyecciones/reportes.

## Seccion candidata

La siguiente seccion puede usarse como candidata futura para Documento 04, sin incorporacion inmediata:

```text
## Proyeccion tabular local

Sea C = (Omega, Phi, Pi, T), donde Omega es soporte observado, Phi es regla de lectura, Pi es conjunto de piezas visibles y T es relacion efectiva de transiciones.

Sea O_adm un conjunto no vacio de observaciones admitidas.

Pi_tb(C, O_adm) = {(o, Phi(o)) | o en O_adm}

Eq_tb(C1, C2, O_adm) si y solo si Pi_tb(C1, O_adm) = Pi_tb(C2, O_adm).

La equivalencia tabular depende del testigo O_adm. Si O_adm solo prueba pertenencia de dominio, la salida es equivalencia trivial y no cierre fuerte.

Pi_tb puede funcionar como instancia local de Pi_op para pruebas de Equivalencia de proyecciones y Confluencia, siempre que el reporte conserve testigo, estatus, salida segura, ausencia de permiso material y deuda abierta.

Esta construccion no cierra P-200, P-107, Equivalencia global de proyecciones ni Confluencia global.
```

## Condiciones antes de incorporar

Antes de cambiar el Documento 04 debe existir:

- decision separada de incorporacion documental;
- auditoria especifica contra Documento 04;
- al menos dos pruebas externas no reguladas de Confluencia; atendido en grado local por `AO-EXT-CONF-EXEC-001`, sin autorizar incorporacion automatica;
- confirmacion de `riesgo_activo: 0`;
- confirmacion de que no se promueve `Xi`;
- confirmacion de que no se cierra `P-200` ni `P-107`;
- criterio de ubicacion: Documento 04 frente a especificacion futura de proyecciones/reportes.

## Ruta recomendada

Nota posterior: la recomendacion original de no incorporar todavia queda superada parcialmente por `D-2026-07-05-008`.

Conservar `R001-TB-001` como base formal local de apoyo a `AO-DOC04-FORM-001`.

Seguir avanzando con pruebas de Confluencia y Equivalencia bajo `AO-001` sin convertir la incorporacion acotada en cierre global.

## No cubre

Esta evaluacion no:

- produce cambios al Documento 04;
- produce cambios al Canon;
- produce cambios de Nivel C;
- canoniza `Xi`;
- admite `H-Xi`;
- cierra `P-200`;
- resuelve `P-107`;
- cierra Equivalencia global;
- cierra Confluencia global;
- autoriza transformaciones materiales.
