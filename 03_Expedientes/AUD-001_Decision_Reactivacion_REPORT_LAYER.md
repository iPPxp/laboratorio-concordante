# AUD-001 - Decision de reactivacion para REPORT_LAYER

Estatus: decision provisional de expediente.

ID local: `D-2026-07-02-025`.

Expediente padre: `AUD-001`.

Objeto decidido: reactivacion acotada de `AUD-001` para separar `REPORT_LAYER` como candidata provisional de expediente.

Fuente principal: instruccion operativa de continuar con el Auditor, leida contra `AUD-001_Decision_Pausa_Operativa_R4-CANDIDATA.md`.

## Decision

`AUD-001` se reactiva de forma acotada.

Ruta elegida:

```text
Ruta D - Separar especificacion de REPORT_LAYER
```

La reactivacion permite redactar `AUD-001_REPORT_LAYER_Candidata.md` como especificacion candidata provisional de expediente.

## Motivo

La pausa operativa de `AUD-001` no fue cierre. Esa decision permitia reactivar el expediente si una decision posterior elegia, entre otras rutas, redactar una especificacion separada de `REPORT_LAYER`.

`REPORT_LAYER` aparece como deuda bloqueante para cualquier promocion futura de `R4-CANDIDATA`, porque la candidata usa una capa abstracta de reportes sin que esa capa tenga todavia forma propia fuera de los nombres locales de `AUD-001`.

Por eso el siguiente avance responsable no es promover `R4-CANDIDATA`, sino separar la capa que permitiria auditar si sus reportes pueden generalizarse.

## Fuentes leidas

- `CURRENT_STATE.md`
- `05_Estado_Proyecto/ESTADO_ACTUAL.md`
- `01_Canon/M-000_Reglas_Fundamentales.md`
- `01_Canon/M-001_Auditoria_Arquitectonica.md`
- `02_Documentos/C-001_Especificacion_Tecnica_Auditor.md`
- `03_Expedientes/AUD-001_Contrato_Reportes.md`
- `03_Expedientes/AUD-001_R4-CANDIDATA.md`
- `03_Expedientes/AUD-001_Criterios_Promocion_R4-CANDIDATA.md`
- `03_Expedientes/AUD-001_Decision_Ruta_Siguiente_R4-CANDIDATA.md`
- `03_Expedientes/AUD-001_Decision_Pausa_Operativa_R4-CANDIDATA.md`

## Alcance permitido

Esta decision permite:

- reactivar `AUD-001` como frente activo acotado;
- redactar `AUD-001_REPORT_LAYER_Candidata.md`;
- mapear `REPORT_LAYER` contra los reportes locales ya validados en `AUD-001`;
- auditar la candidata contra `M-000` y `M-001`;
- decidir su estatus como candidata provisional de expediente.

## Alcance no permitido

Esta decision no permite:

- promover `REPORT_LAYER` a Canon, documento oficial o Nivel C;
- modificar `C-001`;
- promover `R4-CANDIDATA` a Regla R4 formal;
- resolver `Gamma`;
- ejecutar transformaciones materiales;
- convertir reportes provisionales en demostracion formal.

## Condicion de continuidad

La continuidad de `AUD-001` queda limitada a `REPORT_LAYER`.

Cualquier salto posterior hacia Nivel C, Regla R4 formal, `Gamma`, implementacion ejecutable completa o modificacion de documentos oficiales requiere nueva decision y auditoria proporcional.

## Consecuencia operativa

La accion inmediata es redactar y auditar `AUD-001_REPORT_LAYER_Candidata.md`.

Objetivo cumplido posteriormente por `AUD-001_REPORT_LAYER_Candidata.md`, `AUD-001_Auditoria_REPORT_LAYER_Candidata.md` y `AUD-001_Decision_Estatus_REPORT_LAYER_Candidata.md`.

El siguiente objetivo vigente es validar `REPORT-LAYER-CAND-001` o decidir que permanece local.

## Veredicto

`AUD-001` queda reactivado de forma acotada.

Ruta elegida: `REPORT_LAYER`.

Promocion formal: no procede por esta decision.
