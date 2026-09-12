# LAB-INC-SCI-002 — Incorporación de geometría y observabilidad MOC/RC1

Estatus: expediente de incorporación abierto con conflicto de variante; payload
no incorporado.

Fecha: 2026-09-12.

```text
SOURCE_TREE_COMMIT=902f369395590a5f5850292f9fa2c24600bd3ad4
ALTERNATIVE_REVIEW_COMMIT=725635d5e1b479edf70e292d897eb4d44169b331
ALTERNATIVE_REVIEW_COMMIT_IN_ORIGIN_MAIN=NO
MANIFEST_PATH=research/moc_pentacoro_observability_001/FAMILY_INCORPORATION_MANIFEST.sha256
MANIFEST_SHA256=d2387dc5526217e747e1cf90d4e3590545f8300957a7e84efc3f4b2b4916717d
MANIFEST_ENTRIES=30
COMMITTED_BLOBS_VERIFIED=30/30
LOCAL_TESTS=26/26
PAYLOAD_IN_ORIGIN_MAIN=NO
INCORPORATION_DECISION=PENDING
CANONIZATION=NO
ACTIVATION=NO
```

## Alcance candidato

- `research/moc_pentacoro_observability_001/`;
- `research/moc_rc1_geometry_extension/`;
- cuaderno DOCX de decisión semántica;
- paquete reproducible RC1 y su SHA-256.

La fuente `902f369...` preserva la candidata original. La rama local
`725635d...` contiene una aprobación parcial posterior de observabilidad y no es
idéntica a esa candidata. Ninguna variante puede incorporarse hasta reconciliar
el diff, la decisión humana y los hashes de salida.

## Compuertas pendientes

1. elegir expresamente la variante de observabilidad;
2. confirmar el mapping humano de las cinco filas `P/Eaf/Act/V/S`;
3. conservar conducta como salida exteriorizada, no sexto componente;
4. mantener distancia geométrica como no semántica salvo decisión separada;
5. validar compatibilidad RC1 sin mutar el baseline;
6. mantener G0, entrenamiento, canonización y activación cerrados.

## Próxima decisión permitida

`RECONCILIAR_VARIANTES_Y_SOMETER_A_REVISION_HUMANA`.
