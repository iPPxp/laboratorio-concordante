# AO-001 - Opciones de prueba externa de Confluencia

Estatus: opciones provisionales de prueba.

Fecha: 2026-07-05.

ID: `AO-CONF-EXT-OPTIONS-001`.

Expediente padre: `AO-001`.

Relacion base: `R001-TB-001`.

Nota posterior: `AO-EXT-CONF-EXEC-001` ejecuta `EXT-CONF-001` y agrega `EXT-CONF-002` como segunda prueba externa no regulada por `D-2026-07-05-007`.

## Proposito

Identificar opciones de prueba para criterios de Confluencia fuera del Laboratorio, sin abrir dominios clinicos, juridicos, financieros ni institucionales regulados.

## Criterio comun

Una prueba externa de Confluencia debe declarar:

- estado fuente `S`;
- dos rutas validas `T_a` y `T_b`;
- estados resultantes `S_a` y `S_b`;
- contexto `C`;
- observables `O_C`;
- proyeccion `pi`;
- relacion de equivalencia local `~_C`;
- clasificacion de divergencia si no hay equivalencia;
- reporte no mutante.

La prueba pasa si:

```text
pi(S_a) ~_C pi(S_b)
```

o si la divergencia queda registrada como conflicto, deuda o bloqueo sin aumento de autoridad.

## Opciones candidatas

| ID | Dominio externo | Rutas | Observables | Motivo |
| --- | --- | --- | --- | --- |
| `EXT-CONF-001` | tabla de datos sintetica | normalizacion CSV vs normalizacion JSON | claves, tipos, nulos, estatus de fila, advertencias | Es el puente mas cercano a `R001-TB-001`. |
| `EXT-CONF-002` | paquete de software de juguete | manifiesto del paquete vs reporte de dependencias | nombre, version, licencia, advertencias, bloqueo | Prueba confluencia de proyecciones tecnicas sin dominio regulado. |
| `EXT-CONF-003` | flujo documental no oficial | changelog sintetico vs resumen de estado | version, decision, deuda, permiso, salida segura | Prueba rutas documentales fuera del Laboratorio. |
| `EXT-CONF-004` | tablero de tareas sintetico | exportacion CSV vs API simulada | id, estatus, responsable abstracto, bloqueo, fecha logica | Prueba conservacion de estatus entre rutas operativas. |

## Opcion recomendada

La primera prueba externa debe ser `EXT-CONF-001`.

Motivos:

- permite `O_adm` explicito;
- no depende de autoridad humana real;
- permite casos positivos, negativos y triviales;
- se puede ejecutar con fixtures locales sinteticos;
- conecta directamente con `Pi_tb` y `Eq_tb`;
- evita dominios sensibles.

## Matriz minima para EXT-CONF-001

| Caso | Entrada | Ruta A | Ruta B | Resultado esperado |
| --- | --- | --- | --- | --- |
| `EXT-CONF-001A` | tabla con tipos claros | normalizar CSV | normalizar JSON equivalente | confluencia local |
| `EXT-CONF-001B` | tabla con campo faltante | normalizar CSV | normalizar JSON incompleto | bloqueo compartido |
| `EXT-CONF-001C` | tabla con columna extra no admitida | filtrar por `O_adm` | proyectar por esquema | equivalencia bajo testigo |
| `EXT-CONF-001D` | tabla con diferencia relevante | normalizar CSV | normalizar JSON divergente | divergencia clasificada |

## Criterio de salida segura

Cada prueba externa debe terminar en una de estas salidas:

- `confluencia_local`;
- `equivalencia_bajo_testigo`;
- `equivalencia_trivial`;
- `divergencia_clasificada`;
- `bloqueo_por_testigo`;
- `bloqueo_por_deuda`;
- `no_comparable`.

## No cubre

Estas opciones no:

- prueban Confluencia global;
- prueban Equivalencia global;
- usan datos reales de personas;
- abren dominios clinicos, juridicos, financieros o institucionales;
- producen cambios al Documento 04;
- producen cambios al Canon;
- producen cambios de Nivel C;
- autorizan transformaciones materiales.

## Resultado posterior

`EXT-CONF-001` queda ejecutado como fixture sintetico no mutante.

`EXT-CONF-002` queda agregado y ejecutado como segunda prueba externa no regulada.

Los resultados no cierran Confluencia global, Equivalencia global ni formalizacion posterior de Documento 04.

## Siguiente accion propuesta

Conservar los resultados como evidencia local de `AO-001` y decidir por separado si se requieren mas pruebas externas antes de cualquier incorporacion documental acotada.
