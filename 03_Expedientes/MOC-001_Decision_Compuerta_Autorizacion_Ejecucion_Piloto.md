# MOC-001 - Decision de compuerta de autorizacion de ejecucion de piloto

ID: `D-2026-07-06-003`.

Fecha: 2026-07-06.

Estatus: decision provisional de expediente.

## Decision

Se acepta `MOC-GATE-PILOT-EXEC-001` como compuerta aplicada a la ejecucion del piloto empirico futuro.

Resultado: no se autoriza ejecucion real.

Documento base: `03_Expedientes/MOC-001_Compuerta_Autorizacion_Ejecucion_Piloto.md`.

Auditoria: `03_Expedientes/MOC-001_Auditoria_Compuerta_Autorizacion_Ejecucion_Piloto.md`.

## Declaracion de compuerta

```text
piloto_autorizado = false
resultado_compuerta = no_autorizar_ejecucion
ejecucion_permitida = false
transformacion_permitida = false
```

## Razon

La evidencia local permite preparar el piloto, pero no autoriza ejecutarlo.

Siguen pendientes paquete congelado de casos, plantilla de respuesta, version congelada de reglas/protocolo, metodo de registro sin datos personales, responsable de auditoria y criterio operativo completo para participantes/evaluadores.

## Alcance permitido

Se permite trabajo documental preparatorio sin ejecucion:

- congelar casos sinteticos;
- preparar plantilla de respuesta;
- fijar version de reglas y protocolo;
- preparar metodo de registro sin datos personales;
- preparar matriz de auditoria.

## No cubre

No ejecuta piloto empirico, no recluta evaluadores, no recopila respuestas reales, no evalua personas reales, no recopila datos personales, no abre uso clinico, no admite `H-Xi`, no canoniza `Xi`, no modifica `Documento 04`, no crea Nivel C, no cierra Confluencia global, no cierra Equivalencia global y no presenta validacion empirica del MOC.

## Consecuencia

`MOC-ROUTE-007` queda ejecutada como compuerta de no autorizacion.

La siguiente ruta recomendada es `MOC-ROUTE-008`: preparar paquete documental pre-ejecucion de piloto, sin reclutamiento ni ejecucion.
