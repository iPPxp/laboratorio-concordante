# AUD-001 - SPEC-RFC-AUDITOR-V0 Candidata

Estatus: especificacion candidata de expediente.

ID: `SPEC-RFC-AUDITOR-V0`.

Objeto: documento tipo RFC operativo del Auditor.

Destino propuesto: `02_Documentos/C-002_RFC_Operativo_Auditor_v0.md`.

## Proposito

Preparar un documento tipo RFC para estabilizar el uso operativo del Auditor v0.

La candidata traduce la completitud documental de `AUD-001` a una especificacion de lectura, reporte, decision, permisos y conformidad.

## Fuentes normativas locales

- `01_Canon/M-000_Reglas_Fundamentales.md`
- `01_Canon/M-001_Auditoria_Arquitectonica.md`
- `05_Estado_Proyecto/NIVEL_C_ESPECIFICACIONES.md`
- `02_Documentos/C-001_Especificacion_Tecnica_Auditor.md`
- `03_Expedientes/AUD-001_Decision_Estatus_Auditor_v0.md`
- `03_Expedientes/AUD-001_Criterios_Completitud_Auditor.md`
- `03_Expedientes/AUD-001_Sintesis_Completitud_Auditor_v0.md`
- `03_Expedientes/AUD-001_Auditoria_Completitud_Auditor_v0.md`
- `03_Expedientes/AUD-001_Contrato_Reportes.md`
- `03_Expedientes/AUD-001_Validaciones.md`
- `03_Expedientes/AUD-001_Compatibilidad_REPORT_LAYER_DO_CHECK.md`

## Alcance exportable

La especificacion candidata cubre:

- lenguaje normativo local;
- roles del Auditor;
- entradas permitidas y prohibidas;
- ciclo `Mp`, `Cr`, `tau`, `D`, `Tr`;
- contratos de reporte por referencia;
- modo no mutante por defecto;
- permisos para cambios acotados;
- manejo de fallos y reversion documental;
- criterios de conformidad;
- matriz minima de pruebas;
- limites y deudas vivas.

## Fuera de alcance

La candidata no cubre:

- implementacion ejecutable completa;
- parser real;
- modificacion automatica de Canon;
- cierre automatico de expedientes;
- Regla R4 formal;
- `Gamma` formal;
- promocion de `REPORT_LAYER` a Nivel C;
- reversion material o cuarentena materializada.

## Forma tipo RFC

El documento oficial propuesto debe incluir:

1. estado del memo;
2. resumen;
3. lenguaje normativo;
4. fuentes normativas;
5. terminos;
6. modelo operacional;
7. modelo de reportes;
8. procedimiento;
9. permisos y seguridad;
10. conformidad;
11. matriz de pruebas;
12. limites abiertos.

## Condicion de promocion

La candidata solo puede promoverse a `02_Documentos` si:

- existe validacion local de contenido;
- existe auditoria contra `M-000`, `M-001` y `NIVEL-C-001`;
- existe decision de promocion con destino documental declarado;
- las deudas fuera de alcance quedan preservadas.

## Veredicto de candidata

`SPEC-RFC-AUDITOR-V0` tiene alcance exportable suficiente para auditoria de Nivel C.

No queda promovida por este archivo.
