# AO-001 - Relacion entre REPORT_LAYER y Documento 04 Amplio

Identificador: `AO-REPORT-LAYER-BRIDGE-001`.

Estatus: precision local aceptada.

Fecha: 2026-07-06.

Decision: `D-2026-07-06-007`.

## Proposito

Precisar como `REPORT_LAYER` se relaciona con la formalizacion amplia de Documento 04 sin promover `REPORT_LAYER` a Nivel C, sin absorber `DO_CHECK_REPORT` y sin convertir reportes en decisiones o permisos.

## Fuentes

- `02_Documentos/04_Algebra_Operacional.md`.
- `03_Expedientes/AO-001_Formalizacion_Amplia_Doc04.md`.
- `03_Expedientes/AUD-001_REPORT_LAYER_Candidata.md`.
- `03_Expedientes/AUD-001_Compatibilidad_REPORT_LAYER_DO_CHECK.md`.
- `03_Expedientes/AUD-001_Ficha_Alcance_REPORT_LAYER_Pre-C.md`.
- `02_Documentos/C-002_RFC_Operativo_Auditor_v0.md`.

## Relacion formal local

`REPORT_LAYER` no se convierte en operador de Algebra Operacional.

Su relacion formal es de entrada proyectable:

```text
Pi_rep(REPORT_LAYER, C, W) -> R_rep | B
```

Donde:

- `REPORT_LAYER` aporta `REPORT_ITEM` o conjunto ordenado de `REPORT_ITEM`;
- `C` declara contexto de uso;
- `W` declara testigo de comparabilidad;
- `R_rep` es una proyeccion de reporte con estatus, evidencia, permiso y deuda;
- `B` aparece si faltan campos minimos, testigo, evidencia, estatus o frontera de permiso.

## Campos minimos para uso en AO

Un `REPORT_ITEM` solo puede alimentar `Pi_rep` si conserva:

- `report_id`;
- `objeto`;
- `operador_abstracto`;
- `clase_reporte`;
- `resultado`;
- `evidencia`;
- `estatus_afirmacion`;
- `decisiones_permitidas`;
- `decision_emitida`;
- `transformacion_permitida`;
- `deudas_generadas`.

Si falta `decision_emitida` o `transformacion_permitida`, `Pi_rep` debe bloquear porque no puede distinguir recomendacion, decision y permiso.

## Usos permitidos

- Comparar `Pi_rep` con `Pi_doc` bajo `Eq_local`.
- Comparar `Pi_rep` con `Pi_op` bajo `Conf_local`.
- Usar `REPORT_ITEM` como evidencia de reporte.
- Registrar deuda visible si la compatibilidad es parcial.
- Identificar campos faltantes antes de una eventual serializacion formal.

## Usos prohibidos

- Tratar `REPORT_LAYER` como `Op_AO`.
- Tratar `REPORT_LAYER` como decision emitida.
- Tratar `REPORT_LAYER` como permiso de transformacion.
- Tratar `REPORT_LAYER` como verificacion posterior.
- Promover `REPORT_LAYER` a Nivel C por uso en AO.
- Exportar R4/Gamma desde `REPORT_LAYER`.
- Cerrar Confluencia global o Equivalencia global por compatibilidad local.

## Resultado

`REPORT_LAYER` queda precisado para AO como capa local de reporte proyectable por `Pi_rep`.

La deuda viva ya no es si `REPORT_LAYER` puede mencionarse en Documento 04 amplio. Puede mencionarse, pero solo bajo la frontera anterior.

La deuda viva queda en:

- probar reportes heterogeneos adicionales;
- decidir serializacion formal solo si se vuelve necesaria;
- no promover a Nivel C sin candidata, auditoria y decision separada.
