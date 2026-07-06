# Decision - Estatus de pruebas externas de Confluencia AO-001

ID: `D-2026-07-05-007`.

Estatus: decision provisional de expediente.

Fecha: 2026-07-05.

## Decision

Se acepta `AO-EXT-CONF-EXEC-001` como validacion provisional ejecutada de pruebas externas no reguladas de Confluencia.

Documento base: `03_Expedientes/AO-001_Pruebas_Externas_Confluencia.md`.

Auditoria: `03_Expedientes/AO-001_Auditoria_Pruebas_Externas_Confluencia.md`.

Evidencia ejecutable: `06_Automatizacion/ao_ext_confluence.py`.

Fixture: `06_Automatizacion/fixtures/ao_ext_confluence_cases.json`.

Reportes: 06_Automatizacion/reportes/ao_ext_confluence_report.md y 06_Automatizacion/reportes/ao_ext_confluence_report.json.

## Alcance

La decision acepta:

- `EXT-CONF-001` ejecutado sobre tabla de datos sintetica;
- `EXT-CONF-002` agregado y ejecutado sobre paquete de software de juguete;
- `AO-EXT-CONF-001` como herramienta no mutante integrada a `06_Automatizacion`;
- los resultados locales como evidencia de apoyo para `AO-PPI-BRIDGE-001`.

## No cubre

La decision no:

- cierra Confluencia global;
- cierra Equivalencia global de proyecciones;
- modifica Documento 04;
- incorpora `Pi_tb` / `Eq_tb` a Documento 04;
- modifica Canon;
- crea Nivel C;
- promueve ni exporta `R4-FORMAL-AUD-001`;
- promueve ni exporta `GAMMA-FORMAL-AUD-001`;
- canoniza o cierra `TCS-001`;
- abre dominios clinicos, juridicos, financieros o institucionales;
- autoriza transformaciones materiales.

## Consecuencia

`EXT-CONF-001` queda ejecutado.

`EXT-CONF-002` queda agregado como segunda prueba externa no regulada.

La condicion minima de dos pruebas externas queda atendida en grado local, pero no basta por si sola para modificar Documento 04.

Nota posterior: `D-2026-07-05-008` usa esta evidencia para incorporar `Pi_tb` / `Eq_tb` al Documento 04 solo en grado acotado.

Nota posterior: `D-2026-07-05-009` bloquea la exportacion general de R4/Gamma y `D-2026-07-05-010` acepta maduracion provisional de `TCS-001`.

Permanecen abiertas Confluencia global, Equivalencia global, formalizacion posterior amplia de Documento 04, exportacion general de R4/Gamma y maduracion posterior de `TCS-001`.
