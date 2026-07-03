# AUD-001 - Criterios de completitud del Auditor

Estatus: criterios provisionales de expediente.

ID: `COMP-AUD-V0-CRIT-001`.

Objeto: completitud documental/operativa v0 del Auditor.

## Proposito

Definir que significa "Auditor completo" dentro de `AUD-001` sin confundirlo con suite ejecutable completa, Regla R4 formal, `Gamma` formal o promocion de `REPORT_LAYER` a Nivel C.

## Fuentes locales

- `02_Documentos/C-001_Especificacion_Tecnica_Auditor.md`
- `03_Expedientes/AUD-001_Casos_Prueba_Auditor.md`
- `03_Expedientes/AUD-001_Contrato_Reportes.md`
- `03_Expedientes/AUD-001_Simulaciones.md`
- `03_Expedientes/AUD-001_Validaciones.md`
- `03_Expedientes/AUD-001_R4-CANDIDATA.md`
- `03_Expedientes/AUD-001_REPORT_LAYER_Candidata.md`
- `03_Expedientes/AUD-001_Compatibilidad_REPORT_LAYER_DO_CHECK.md`
- `03_Expedientes/HB-001_Deuda_Viva_H-B.md`
- `03_Expedientes/DO-001_DO-CHECK-001.md`
- `03_Expedientes/DO-001_Regla_Permiso_Actualizacion.md`
- `03_Expedientes/DO-001_Decision_Modo_Operativo_Auditor.md`

## Definicion de completitud v0

El Auditor queda completo en version documental/operativa v0 cuando existe una descripcion local suficiente para:

- saber que revisa;
- saber que no decide por si mismo;
- distinguir lectura, calculo, decision, propuesta y ejecucion;
- reportar fallas con contratos estables de expediente;
- bloquear transformaciones no fundadas;
- aprobar un caso limpio sin transformar;
- cubrir objetos no automatas relevantes;
- delimitar deudas vivas sin usarlas como fundamento.

## Compuertas

| Compuerta | Criterio | Evidencia minima | Resultado esperado |
| --- | --- | --- | --- |
| C1 | Especificacion tecnica vigente | `C-001_Especificacion_Tecnica_Auditor.md` | alcance del Auditor existe en Nivel C |
| C2 | Modo operativo y permiso | `DO-CHECK`, `PERMISO-ACT-001`, `MODO-AUD-001` | el Auditor opera como lectura no mutante salvo permiso posterior |
| C3 | Contratos de reporte | `AUD-001_Contrato_Reportes.md` | reportes normalizados para `Mp`, `Cr`, `tau`, `D`, `Tr` y reversion |
| C4 | Matriz basal | `AUD-T00` a `AUD-T09` | cada caso tiene simulacion y validacion |
| C5 | Frontera R4 | `R4-CANDIDATA` y validaciones `VAL-017` a `VAL-021` | R4 queda como candidata operativa, no formal |
| C6 | `REPORT_LAYER` | `REPORT-LAYER-CAND-001`, `VAL-022`, `VAL-028` | capa abstracta local y puente conceptual con `DO_CHECK_REPORT` |
| C7 | Deuda viva | `HB-001_Deuda_Viva_H-B.md` y deudas de R4/Gamma | las deudas no bloquean v0 porque no se usan como fundamento |
| C8 | Limites declarados | este documento y sintesis asociada | lo no incluido queda fuera del cierre v0 |

## Exclusiones

La completitud v0 no incluye:

- suite ejecutable completa;
- parser real de archivos;
- serializacion JSON externa mientras la pausa temporal siga vigente;
- escritura automatica en expedientes o Canon;
- reversion material o cuarentena materializada;
- Regla R4 formal;
- formalizacion de `Gamma`;
- promocion de `REPORT_LAYER` a Nivel C;
- absorcion de `DO_CHECK_REPORT` por `AUD-001_Contrato_Reportes.md`;
- cierre de deudas `H-B.6` y `H-B.7`.

## Regla de decision

Si las compuertas C1 a C8 pasan, `AUD-001` puede declarar completo el Auditor v0 en alcance documental/operativo.

Si alguna compuerta falla, el expediente debe conservar estatus abierto y registrar la deuda concreta antes de declarar completitud.

## Resultado esperado

Estos criterios habilitan una sintesis de completitud, una auditoria local y una decision de estatus v0 dentro de `AUD-001`.
