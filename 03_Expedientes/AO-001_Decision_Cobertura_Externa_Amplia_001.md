# D-2026-07-06-022 - Cobertura externa amplia sintetica

Fecha: 2026-07-06.

Estado: aceptada.

## Decision

Se acepta `AO-EXT-COV-001` como bateria local no mutante de cobertura externa amplia sintetica no regulada.

Documento base: `03_Expedientes/AO-001_Cobertura_Externa_Amplia_001.md`.

Auditoria: `03_Expedientes/AO-001_Auditoria_Cobertura_Externa_Amplia_001.md`.

Herramienta: `06_Automatizacion/ao_ext_cov_001.py`.

## Alcance aceptado

La condicion `AO-PPI-GC-006` queda reducida a `parcial_local`: hay cobertura heterogenea fuerte, pero no independiente ni global.

## Limites

No se usan dominios regulados, clinicos ni personas reales.

No se modifica Documento 04, Canon, Nivel C ni `C-002`.

## Deudas abiertas

- Cobertura externa independiente.
- Protocolo AO reproducible independiente.
- Cierre global de Confluencia y Equivalencia.
