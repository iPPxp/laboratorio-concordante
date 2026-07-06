# MOC-001 - Decision de paquete documental pre-ejecucion de piloto

ID: `D-2026-07-06-004`.

Fecha: 2026-07-06.

Estatus: decision provisional de expediente.

## Decision

Se acepta `MOC-PREEXEC-PACK-001` como paquete documental pre-ejecucion de piloto.

Documento base: `03_Expedientes/MOC-001_Paquete_PreEjecucion_Piloto.md`.

Auditoria: `03_Expedientes/MOC-001_Auditoria_Paquete_PreEjecucion_Piloto.md`.

## Componentes aceptados

- `MOC-SEM-PROV-001`: semantica provisional local del MOC.
- `MOC-OPS-FORMAL-001`: tabla de operaciones formales.
- `MOC-PILOT-CASE-FREEZE-001`: paquete congelado de 11 casos sinteticos.
- `MOC-PILOT-RESPONSE-TPL-001`: plantilla de respuesta de evaluadores.
- `MOC-PILOT-RULE-FREEZE-001`: version congelada de reglas/protocolo.

## Resultado

`MOC-ROUTE-008` queda ejecutada como preparacion documental pre-ejecucion.

El piloto empirico real permanece no autorizado.

```text
piloto_autorizado = false
ejecucion_permitida = false
reclutamiento_permitido = false
respuestas_reales_permitidas = false
datos_personales_permitidos = false
uso_clinico = false
```

## No cubre

No ejecuta piloto empirico, no recluta evaluadores, no recopila respuestas reales, no evalua personas reales, no recopila datos personales, no abre uso clinico, no admite `H-Xi`, no canoniza `Xi`, no modifica `Documento 04`, no crea Nivel C, no cierra Confluencia global, no cierra Equivalencia global y no presenta validacion empirica del MOC.

## Consecuencia

La siguiente ruta recomendada es `MOC-ROUTE-009`: preparar metodo de registro sin datos personales y matriz de auditoria de piloto, sin reclutamiento ni ejecucion.
