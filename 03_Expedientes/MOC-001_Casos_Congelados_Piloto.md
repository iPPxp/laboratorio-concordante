# MOC-001 - Casos congelados para piloto futuro

ID: `MOC-PILOT-CASE-FREEZE-001`.

Ruta: `MOC-ROUTE-008`.

Fecha: 2026-07-06.

Estatus: paquete congelado documental, no ejecutado.

Decision asociada: `D-2026-07-06-004`.

## Proposito

Congelar la bateria sintetica no clinica que podria usarse en un piloto futuro si una decision posterior autorizara ejecucion.

Este congelamiento no ejecuta piloto, no recluta evaluadores, no recoge respuestas reales y no produce resultado empirico.

## Fuente congelada

Archivo fuente:

```text
06_Automatizacion/fixtures/moc_cases.json
```

Identificador de suite:

```text
suite_id = MOC-SYN-001
```

Hash SHA256 del fixture:

```text
6D440C687EFDD43B88EB46BED3F0C0FB24754CD8CD0AB82791D7EF684BB77549
```

Si el fixture cambia, este paquete deja de describir la version congelada y requiere nueva decision.

## Casos congelados

| Caso | Dominio sintetico | Xi esperado | Estado MOC esperado | Clase | Deuda |
| --- | --- | --- | --- | --- | --- |
| `MOC-CASE-001` | `tablero_tareas_sintetico` | `redundante` | `concordancia_local` | coincidencia exacta | conservar trazabilidad |
| `MOC-CASE-002` | `paquete_software_juguete` | `util_acotado` | `concordancia_local` | coincidencia exacta | no exportar como regla global |
| `MOC-CASE-003` | `flujo_editorial_sintetico` | `limitado` | `friccion_operativa` | coincidencia parcial | resolver conflicto de regla local |
| `MOC-CASE-004` | `registros_abstractos` | `no_comparable` | `no_comparable` | seguridad | redefinir unidad minima |
| `MOC-CASE-005` | `fuera_de_alcance` | `bloqueado` | `bloqueo_de_concordancia` | seguridad | retirar caso o abrir decision separada |
| `MOC-CASE-006` | `rutas_reporte_sinteticas` | `util_acotado` | `discordancia_global` | desacuerdo justificado | Confluencia y Equivalencia global abiertas |
| `MOC-CASE-007` | `matriz_criterios_sintetica` | `util_acotado` | `concordancia_parcial` | coincidencia parcial | completar trazabilidad secundaria |
| `MOC-CASE-008` | `tabla_prioridades_sintetica` | `limitado` | `friccion_operativa` | ambiguedad de regla | precisar si regla es friccion o bloqueo |
| `MOC-CASE-009` | `cola_eventos_sintetica` | `util_acotado` | `concordancia_parcial` | deuda secundaria | completar eje TCS `automation_bounded` |
| `MOC-CASE-010` | `doble_autoridad_sintetica` | `limitado` | `friccion_operativa` | conflicto de autoridad local | resolver autoridad sin invocar Confluencia global |
| `MOC-CASE-011` | `frontera_parcial_friccion_sintetica` | `util_acotado` | `concordancia_parcial` | frontera concordancia/friccion | precisar umbral de deuda no bloqueante |

## Cobertura minima

La bateria congelada cubre:

- redundancia;
- reorganizacion estable;
- friccion operativa;
- no comparabilidad;
- bloqueo por alcance;
- discordancia global;
- concordancia parcial por deuda secundaria;
- ambiguedad de regla;
- conflicto de autoridad local;
- frontera entre deuda no bloqueante y friccion.

## Restricciones

- Los casos no son personas.
- Los casos no contienen datos personales.
- Los casos no son clinicos ni regulados.
- Los casos no autorizan ejecucion real.
- Los casos no validan empiricamente el MOC.
- Los casos no modifican `Documento 04`, Canon ni Nivel C.

## Uso permitido

Uso permitido solo como paquete documental congelado para preparar una fase posterior.

Uso prohibido como evidencia empirica real, como resultado de piloto, como material clinico o como base para promocion canonica.
