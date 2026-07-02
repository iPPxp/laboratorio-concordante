# AUD-001 - Criterios de promocion de R4-CANDIDATA

Estatus: criterios provisionales de expediente.

Expediente padre: `AUD-001`.

Fuente principal: `AUD-001_Decision_Siguiente_Fase_R4-CANDIDATA.md`.

Auditoria asociada: `AUD-001_Auditoria_Criterios_Promocion_R4-CANDIDATA.md`.

Decision de estatus asociada: `AUD-001_Decision_Estatus_Criterios_Promocion_R4-CANDIDATA.md`.

Decision de ruta asociada: `AUD-001_Decision_Ruta_Siguiente_R4-CANDIDATA.md`.

Decision de pausa asociada: `AUD-001_Decision_Pausa_Operativa_R4-CANDIDATA.md`.

## Proposito

Definir compuertas para cualquier decision futura sobre `R4-CANDIDATA`.

Este documento no promueve `R4-CANDIDATA`. Solo fija criterios para distinguir rutas posibles y deudas bloqueantes.

## Fuentes locales

- `01_Canon/M-000_Reglas_Fundamentales.md`
- `01_Canon/M-001_Auditoria_Arquitectonica.md`
- `05_Estado_Proyecto/NIVEL_C_ESPECIFICACIONES.md`
- `03_Expedientes/AUD-001_R4-CANDIDATA.md`
- `03_Expedientes/AUD-001_Decision_Estatus_R4-CANDIDATA.md`
- `03_Expedientes/AUD-001_Decision_Capa_Reportes_R4-CANDIDATA.md`
- `03_Expedientes/AUD-001_Decision_Cierre_Ronda_No_Automata_R4-CANDIDATA.md`
- `03_Expedientes/AUD-001_Decision_Siguiente_Fase_R4-CANDIDATA.md`
- `03_Expedientes/AUD-001_Auditoria_Post-No-Automata_R4-CANDIDATA.md`
- `03_Expedientes/AUD-001_Sintesis_Cobertura_No_Automata_R4-CANDIDATA.md`

## Estado actual de R4-CANDIDATA

`R4-CANDIDATA` esta en este estado:

```text
hipotesis operativa robustecida de expediente dentro de AUD-001
```

Este estatus permite seguir trabajando dentro de `AUD-001`, pero no permite usar la candidata como Canon, documento oficial, Nivel C ni Regla R4 formal.

## Principios de promocion

Toda promocion futura debe respetar estas compuertas:

- no hay promocion automatica por acumulacion de pruebas
- toda promocion requiere decision explicita
- toda decision requiere auditoria previa proporcional al nivel de destino
- la autoridad de `AUD-001` no alcanza por si sola para modificar Canon ni documentos oficiales
- `REPORT_LAYER` sigue local mientras no exista especificacion separada o decision equivalente
- Regla R4 formal no puede derivarse solo por analogia con `R4-CANDIDATA`
- cualquier ruta debe conservar trazabilidad de fuentes, deudas y limites

## Rutas posibles

| Ruta | Resultado posible | Estado actual | Compuerta |
| --- | --- | --- | --- |
| Mantener hipotesis robustecida | `R4-CANDIDATA` sigue dentro de `AUD-001` | disponible | decision simple de continuidad |
| Definicion provisional de expediente | forma estable para uso interno mas fuerte | posible, no decidida | auditoria de criterios y decision explicita |
| Documento oficial o Nivel C | especificacion tecnica exportable | bloqueada | requiere alcance, auditoria de Nivel C y decision de promocion |
| Especificacion separada de `REPORT_LAYER` | contrato abstracto fuera de nombres locales | bloqueada | requiere documento o expediente propio |
| Propuesta hacia Regla R4 formal | puente hacia regla general | bloqueada | requiere definicion formal de R4 y tratamiento de `Gamma` |
| Congelar o rechazar | detener evolucion de la candidata | disponible si aparece bloqueo | decision explicita con motivo |

## Criterios por ruta

### Ruta A - Mantener hipotesis operativa robustecida

Criterios suficientes:

- estatus actual declarado
- auditoria inicial favorable
- primera ronda no automata cerrada provisionalmente
- ausencia de promocion indebida
- deudas formales reconocidas como abiertas

Estado: ruta disponible.

### Ruta B - Convertir en definicion provisional de expediente

Criterios minimos:

- redactar forma definicional separada de la hipotesis narrativa
- declarar alcance interno exacto dentro de `AUD-001`
- auditar que no se use como Canon ni documento oficial
- decidir expresamente el cambio de estatus
- registrar deudas que siguen bloqueando promocion formal

Estado: posible, pero no autorizada todavia.

### Ruta C - Preparar documento oficial o Nivel C

Criterios minimos:

- justificar por que el contenido pertenece a `02_Documentos` y no solo a `AUD-001`
- definir alcance tecnico exportable
- separar ejemplos de automatas de la regla procedimental general
- resolver o acotar `REPORT_LAYER` como contrato reusable
- auditar contra `NIVEL-C-001` si se propone Nivel C
- registrar decision de promocion de nivel

Estado: bloqueada por falta de alcance oficial y falta de especificacion de `REPORT_LAYER`.

### Ruta D - Separar especificacion de REPORT_LAYER

Criterios minimos:

- decidir si `REPORT_LAYER` sale de `AUD-001`
- definir campos abstractos obligatorios y opcionales
- mapear compatibilidad con reportes locales de `AUD-001`
- probar al menos una instancia fuera de `AUD-001` o declarar que sigue local
- auditar contra `M-000` y `M-001`

Estado: bloqueada hasta decision de alcance.

### Ruta E - Derivar propuesta hacia Regla R4 formal

Criterios minimos:

- definir localmente que cuenta como Regla R4 formal
- distinguir restriccion procedimental de implementacion del Auditor
- decidir relacion con `Gamma`
- demostrar o declarar explicitamente los limites de generalidad
- auditar la propuesta como cambio de nivel superior
- registrar decision canonica o arquitectonica si afecta Canon

Estado: bloqueada por falta de definicion formal de R4 y `Gamma`.

### Ruta F - Congelar o rechazar

Criterios posibles:

- aparece contradiccion con `M-000` o `M-001`
- `REPORT_LAYER` no puede separarse ni mantenerse local sin ambiguedad
- la candidata depende de una nocion formal no materializada
- se decide que basta conservarla como evidencia historica de `AUD-001`

Estado: disponible solo por decision explicita.

## Criterios bloqueantes comunes

Bloquean cualquier promocion fuera de hipotesis robustecida:

- falta de decision explicita de cambio de estatus
- uso de `AUD-001` como autoridad suficiente para documento oficial o Canon
- ausencia de auditoria del nivel de destino
- uso de `REPORT_LAYER` como especificacion oficial sin decidirlo
- confundir validaciones provisionales con demostracion formal
- no resolver la frontera entre `R4-CANDIDATA` y Regla R4 formal

## Criterio operativo actual

Con la evidencia disponible, la ruta recomendada es:

```text
mantener R4-CANDIDATA como hipotesis operativa robustecida
y auditar estos criterios antes de decidir una ruta nueva
```

Lectura posterior: la auditoria y decision de estatus de criterios quedaron registradas, y la ruta elegida posteriormente fue mantener `R4-CANDIDATA` como hipotesis operativa robustecida.

## Deudas que permanecen

- Auditar este documento de criterios contra `M-000` y `M-001`. Cumplido posteriormente por `AUD-001_Auditoria_Criterios_Promocion_R4-CANDIDATA.md`.
- Decidir si la siguiente ruta sera mantener, definir provisionalmente, separar `REPORT_LAYER`, preparar Nivel C, proponer R4 formal o congelar. Cumplido posteriormente por `AUD-001_Decision_Ruta_Siguiente_R4-CANDIDATA.md`.
- Mantener abiertos `R4` formal y `Gamma` hasta definicion local.

## Veredicto

Los criterios quedan redactados como compuerta provisional de expediente.

No autorizan promocion formal.

## Siguiente paso recomendado

Objetivo cumplido posteriormente por `AUD-001_Auditoria_Criterios_Promocion_R4-CANDIDATA.md` y `AUD-001_Decision_Ruta_Siguiente_R4-CANDIDATA.md`.
