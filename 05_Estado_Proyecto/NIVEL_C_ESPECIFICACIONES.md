# Nivel C - Especificaciones

Estatus: definicion local de proyecto.

Fecha: 2026-07-01.

Identificador: `NIVEL-C-001`.

## Proposito

Definir localmente que significa `Nivel C - Especificaciones` dentro del Laboratorio Concordante.

Esta definicion permite distinguir entre una especificacion tecnica candidata de expediente y una especificacion tecnica oficial.

## Definicion

`Nivel C - Especificaciones` es el subnivel documental destinado a estabilizar procedimientos, contratos, interfaces, formatos, pruebas y condiciones de ejecucion.

Nivel C no es Canon.

Nivel C no reemplaza documentos marco ni resuelve problemas abiertos por si mismo.

Nivel C convierte una propuesta tecnica suficientemente auditada en una especificacion operativa oficial, siempre subordinada a `M-000`, `M-001` y a los documentos oficiales de marco general.

## Ubicacion jerarquica

Nivel C no crea una zona superior nueva al Canon. Opera dentro del nivel de documentos oficiales.

Jerarquia local:

```text
Canon
-> documentos oficiales de marco general
-> Nivel C: especificaciones tecnicas oficiales
-> expedientes, candidatas y validaciones provisionales
-> registro historico
```

Una especificacion tecnica oficial puede gobernar implementaciones y pruebas, pero no puede modificar Canon ni documentos marco por implicacion.

## Estados permitidos

### Especificacion candidata

Ubicacion: `03_Expedientes`.

Estatus: expediente.

Funcion: separar un nucleo tecnico exportable sin promoverlo todavia a documento oficial.

No tiene autoridad oficial por si misma.

### Especificacion tecnica oficial

Ubicacion inicial permitida: `02_Documentos`.

Estatus: documento oficial de Nivel C.

Funcion: fijar una superficie tecnica estable para uso operativo, validacion, implementacion o auditoria.

Requiere decision de promocion y auditoria previa.

## Contenido permitido en Nivel C

Una especificacion de Nivel C puede contener:

- proposito tecnico
- alcance y fuera de alcance
- fuentes normativas locales
- entradas permitidas y entradas prohibidas
- salidas permitidas y salidas prohibidas
- contratos de datos o reportes
- procedimientos operativos
- invariantes verificables
- reglas de permiso y autorizacion
- criterios de validacion
- condiciones de fallo y reversion
- deudas conceptuales que quedan fuera de la especificacion

## Contenido prohibido en Nivel C

Una especificacion de Nivel C no puede:

- modificar Canon
- promover hipotesis a teoremas
- cerrar problemas abiertos por redaccion
- convertir historial en autoridad vigente
- reemplazar una decision de promocion
- cerrar o reabrir expedientes por si misma
- autorizar implementaciones fuera de su alcance declarado
- ocultar deudas conceptuales necesarias

## Requisitos minimos de promocion

Una candidata puede pasar a especificacion tecnica oficial solo si existe:

- archivo candidato en `03_Expedientes`
- alcance exportable declarado
- fuentes normativas locales citadas
- validacion provisional de contenido
- auditoria contra `M-000`, `M-001` y `NIVEL-C-001`
- decision de promocion registrada
- destino documental declarado
- deudas fuera de alcance conservadas como deudas

## Regla de nombrado provisional

Las candidatas pueden usar la forma:

```text
03_Expedientes/<EXPEDIENTE>_SPEC-<TEMA>_Candidata.md
```

Las especificaciones oficiales pueden usar la forma:

```text
02_Documentos/C-<ID>_<Nombre_Especificacion>.md
```

El nombre oficial exacto debe decidirse en la decision de promocion.

## Relacion con SPEC-AUD-001_Candidata

`SPEC-AUD-001_Candidata` ya tiene forma de candidata valida para auditoria de Nivel C.

Esta definicion no la promueve automaticamente a documento oficial.

`SPEC-AUD-001_Candidata` fue auditada favorablemente contra `NIVEL-C-001` y promovida a `02_Documentos/C-001_Especificacion_Tecnica_Auditor.md`.

## Criterio de cierre

`NIVEL-C-001` queda definido localmente si:

- existe este archivo en `05_Estado_Proyecto`
- `05_Estado_Proyecto/DECISIONES.md` registra la decision arquitectonica
- existe validacion local de `NIVEL-C-001`
- `CURRENT_STATE.md` y `ESTADO_ACTUAL.md` retiran la deuda activa de definir Nivel C
- el siguiente objetivo pasa a decidir cierre o continuacion de `DO-001`
