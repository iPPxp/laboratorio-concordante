# D-2026-07-06-021 - Criterio local de autoridad entre niveles

Fecha: 2026-07-06.

Estado: aceptada.

## Decision

Se acepta `AO-AUTH-GLOBAL-001` como criterio local no mutante de comparabilidad entre niveles.

Documento base: `03_Expedientes/AO-001_Criterio_Autoridad_Global_001.md`.

Auditoria: `03_Expedientes/AO-001_Auditoria_Criterio_Autoridad_Global_001.md`.

Herramienta: `06_Automatizacion/ao_authority_global_001.py`.

## Alcance aceptado

La condicion `AO-PPI-GC-005` queda reducida a `parcial_local`: existe criterio local defensivo, pero no autoridad global real.

## Limites

No hay promocion de autoridad por repeticion, historial, reporte automatizado ni recomendacion.

No se modifica Canon, Nivel C, Documento 04 ni `C-002`.

## Deudas abiertas

- Autoridad global real sigue no autorizada.
- Protocolo AO reproducible independiente.
- Cierre global de Confluencia y Equivalencia.
