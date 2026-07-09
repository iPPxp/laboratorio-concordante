# MOC-001 - Compuerta de grafo hacia Canon y Documento 04

Estatus: compuerta preparatoria aceptada.

Fecha: 2026-07-09.

Decision asociada: `D-2026-07-09-002`.

## Proposito

`MOC-GRAPH-CANON-DOC04-GATE-001` define como el grafo local de experiencia puede tocar el perimetro de Canon y Documento 04 sin alterar todavia los archivos oficiales.

La compuerta autoriza contacto documental preparatorio, no incorporacion oficial.

## Entradas

- `MOC-EXP-GRAPH-001_Grafo_Experiencia_Local.md`.
- `MOC-GEO-METR-LAB-001_Metrica_Geometrica_Local.md`.
- `MOC-AO-GEO-BRIDGE-001_Puente_AO_Operator_Trace.md`.
- `MOC-001_Autorizacion_Derechos_Grafo_Canon_Doc04.md`.
- `Licencia_y_Derechos.md`.
- `01_Canon/M-000_Reglas_Fundamentales.md`.
- `01_Canon/M-001_Auditoria_Arquitectonica.md`.
- `02_Documentos/04_Algebra_Operacional.md`.

## Salidas permitidas

```text
autorizacion_interna_preparatoria
propuesta_candidata_requerida
rechazo_por_alcance
rechazo_por_derechos
rechazo_por_autoridad
```

## Criterios de paso

La compuerta queda en `autorizacion_interna_preparatoria` si:

- la titularidad interna esta declarada;
- `Licencia_y_Derechos.md` permanece vigente;
- el uso queda dentro del repositorio local;
- el grafo conserva uso no clinico y no regulado;
- no hay personas reales;
- no hay uso externo;
- no hay modo mutante;
- no hay incorporacion oficial directa;
- existe decision posterior obligatoria para cualquier cambio real.

## Criterios de rechazo

La compuerta rechaza si:

- falta titularidad interna;
- se solicita publicacion o redistribucion;
- se solicita uso clinico o regulado;
- se intenta admitir `H-Xi`;
- se intenta canonizar `Xi`, `Phi`, `TrueSelf` o `psi`;
- se intenta editar directamente Canon o Documento 04;
- se intenta cerrar Confluencia global o Equivalencia global;
- se intenta convertir `operator_trace` en autoridad canonica.

## Dictamen

La compuerta queda aceptada con salida:

```text
autorizacion_interna_preparatoria
```

El grafo puede preparar propuesta candidata para Canon y Documento 04. La incorporacion oficial queda pendiente de una decision posterior separada.

