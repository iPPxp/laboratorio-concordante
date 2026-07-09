# AO-EXT-REAL-001 - Evidencia externa independiente real

Fecha: 2026-07-06.

Estatus: admitida preliminarmente, no ejecutada.

Expediente: `AO-001`.

## Objeto

Registrar la primera evidencia externa independiente real para `AO-001` bajo la compuerta `AO-EXT-EVID-GATE-001`.

La ruta no ejecuta estudio empirico, no transforma artefactos del Laboratorio, no descarga corpus externo y no reabre `P-PI.0` / `P-PI.1`. Solo evalua manifiestos de fuente real contra criterios de admisibilidad documental.

## Fuentes externas usadas

Se aceptan como fuentes reales identificables:

- RFC 9457, `Problem Details for HTTP APIs`, fuente: `https://www.rfc-editor.org/info/rfc9457/`.
- Registro IANA `HTTP Problem Types`, fuente: `https://www.iana.org/assignments/http-problem-types`.

Ambas fuentes son externas al Laboratorio, publicas, tecnicas, no clinicas, no personales y no generadas por fixtures locales.

## Unidad comparable

La unidad comparable no es el contenido tecnico completo de HTTP.

La unidad comparable usada para AO es:

```text
artefacto tecnico externo con fuente identificable
+ unidad registral/documental
+ testigo publico
+ autoridad documental externa
+ trazabilidad por URI
-> admisibilidad preliminar
```

Esta unidad permite probar la compuerta de evidencia externa real sin convertir el estandar externo en autoridad del Laboratorio.

## Resultado de compuerta

La herramienta no mutante `AO-EXT-EVID-GATE-001` debe producir para el fixture real:

```text
external_evidence_ready: true
external_evidence_executed: false
global_closure_authorized: false
global_export_authorized: false
global_equivalence_authorized: false
global_confluence_authorized: false
report_layer_promoted: false
r4_gamma_global_export_authorized: false
```

## Alcance

`AO-EXT-REAL-001` puede:

- contar como evidencia externa independiente real admisible de forma preliminar;
- reducir la deuda "no existe fuente externa real aportada";
- habilitar una decision posterior sobre si conviene reconsiderar compuertas globales;
- alimentar auditorias futuras como testigo documental real.

`AO-EXT-REAL-001` no puede:

- cerrar Confluencia global;
- cerrar Equivalencia global de proyecciones;
- promover `REPORT_LAYER`;
- exportar R4/Gamma;
- modificar Canon, Documento 04, Nivel C o `C-002`;
- reabrir `P-PI.0` / `P-PI.1`;
- autorizar modo mutante;
- convertir la autoridad externa en autoridad interna del Laboratorio.

## Deudas abiertas

- Decidir si la evidencia real admisible basta para reejecutar o revisar `AO-GLOBAL-READINESS-001`.
- Disenar, si se autoriza, una matriz posterior de uso de evidencia externa real.
- Mantener no autorizadas Confluencia global y Equivalencia global hasta nueva decision.
- Mantener `REPORT_LAYER` local pre-C.
- Mantener R4/Gamma sin exportacion general.
- Madurar `TCS-001` por via propia.
