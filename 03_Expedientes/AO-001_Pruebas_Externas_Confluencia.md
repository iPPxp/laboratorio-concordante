# AO-001 - Pruebas externas de Confluencia

Estatus: validacion provisional ejecutada.

Fecha: 2026-07-05.

ID: `AO-EXT-CONF-EXEC-001`.

Expediente padre: `AO-001`.

Nota posterior: `D-2026-07-05-008` usa esta evidencia como apoyo para `AO-DOC04-FORM-001`, incorporacion acotada de `Pi_tb` / `Eq_tb` al Documento 04. Esto no convierte estas pruebas en cierre global de Confluencia o Equivalencia.

Algoritmo ejecutable: `AO-EXT-CONF-001`.

Fixture: `06_Automatizacion/fixtures/ao_ext_confluence_cases.json`.

Reporte Markdown: 06_Automatizacion/reportes/ao_ext_confluence_report.md.

Reporte JSON: 06_Automatizacion/reportes/ao_ext_confluence_report.json.

## Proposito

Ejecutar `EXT-CONF-001` y agregar al menos una segunda prueba externa no regulada de criterios de Confluencia, sin cerrar Confluencia global ni Equivalencia global.

## Pruebas ejecutadas

| ID | Dominio | Rutas | Casos | Resultado |
| --- | --- | --- | --- | --- |
| `EXT-CONF-001` | tabla de datos sintetica | normalizacion CSV vs normalizacion JSON | `EXT-CONF-001A` a `EXT-CONF-001D` | pasa |
| `EXT-CONF-002` | paquete de software de juguete | manifiesto del paquete vs reporte de dependencias | `EXT-CONF-002A` a `EXT-CONF-002C` | pasa |

## Resultados locales

La ejecucion `AO-EXT-CONF-001` reporta:

- 7 casos ejecutados;
- 7 casos aprobados;
- 0 fallos;
- `EXT-CONF-001` ejecutado;
- `EXT-CONF-002` agregado y ejecutado como segunda prueba externa no regulada;
- `transformacion_permitida: false`;
- recomendacion: `mantener_deudas_globales_abiertas`.

## Lectura de EXT-CONF-001

`EXT-CONF-001` prueba una tabla sintetica mediante dos rutas:

- ruta A: normalizacion CSV;
- ruta B: normalizacion JSON;
- testigo: esquema declarado y observables admitidos.

Casos:

- `EXT-CONF-001A`: confluencia local positiva;
- `EXT-CONF-001B`: bloqueo compartido por testigo incompleto;
- `EXT-CONF-001C`: equivalencia bajo testigo con columna extra filtrada;
- `EXT-CONF-001D`: divergencia clasificada.

## Lectura de EXT-CONF-002

`EXT-CONF-002` agrega una segunda prueba externa no regulada:

- dominio: paquete de software de juguete;
- ruta A: manifiesto del paquete;
- ruta B: reporte de dependencias;
- observables: nombre, version, licencia y dependencias declaradas.

Casos:

- `EXT-CONF-002A`: confluencia local positiva;
- `EXT-CONF-002B`: bloqueo compartido por licencia faltante;
- `EXT-CONF-002C`: divergencia clasificada por version distinta.

## Alcance

La validacion permite usar `AO-EXT-CONF-001` como evidencia local de que los criterios de Confluencia pueden probarse fuera del Laboratorio en dominios sinteticos no regulados.

Tambien atiende la condicion cuantitativa minima de dos pruebas externas antes de considerar una incorporacion posterior de `Pi_tb` / `Eq_tb` al Documento 04.

## No cubre

Esta validacion no:

- cierra Confluencia global;
- cierra Equivalencia global;
- modifica Documento 04;
- modifica Canon;
- crea Nivel C;
- promueve ni exporta `R4-FORMAL-AUD-001`;
- promueve ni exporta `GAMMA-FORMAL-AUD-001`;
- canoniza o cierra `TCS-001`;
- abre dominios clinicos, juridicos, financieros o institucionales;
- autoriza transformaciones materiales.

## Deudas que permanecen abiertas

- Confluencia global;
- Equivalencia global de proyecciones;
- formalizacion posterior de Documento 04;
- decision de ubicacion de `Pi_tb` / `Eq_tb` entre Documento 04 y posible especificacion posterior;
- exportacion general de `R4-FORMAL-AUD-001`;
- exportacion general de `GAMMA-FORMAL-AUD-001`;
- maduracion de `TCS-001`.

## Siguiente accion

Conservar `AO-EXT-CONF-001` como evidencia local aceptable si la auditoria lo valida.

No abrir incorporacion a Documento 04 hasta decision separada con auditoria especifica del texto a incorporar.
