# P-PI - Decision de reactivacion del frente matematico

Estatus: decision provisional de expediente.

ID: `D-2026-07-02-032`.

Fecha: 2026-07-02.

Expedientes afectados:

- `P-PI.0`
- `P-PI.1`

Marco aceptado: `P-PI_Marco_Inicial_Confluencia_Equivalencia.md`.

Auditoria asociada: `P-PI_Auditoria_Marco_Inicial_Confluencia_Equivalencia.md`.

## Decision

Se reactiva `P-PI.0` / `P-PI.1` como frente matematico acotado.

Estatus asignado:

```text
P-PI.0 = activo acotado para Equivalencia de proyecciones
P-PI.1 = activo acotado para Confluencia
```

Tambien se acepta `PPI-MARCO-CORE-001` como marco provisional de expediente.

## Alcance permitido

La decision permite:

- usar `PPI-MARCO-CORE-001` como vocabulario minimo local;
- construir casos de prueba de equivalencia de proyecciones;
- construir casos de prueba de confluencia local;
- usar ejemplos ya registrados del Auditor solo como casos locales, no como demostracion general;
- actualizar el estado del proyecto para retirar `P-PI` de pausa operativa.

## Alcance no permitido

La decision no permite:

- cerrar Confluencia;
- cerrar Equivalencia de proyecciones;
- modificar Canon o documentos oficiales;
- importar historial como autoridad directa;
- tratar los vision papers inactivos como fuente;
- declarar propiedades globales de `~_C` sin casos locales;
- promover `PPI-MARCO-CORE-001` al Documento 02 sin decision separada.

## Motivo

`P-PI.0` y `P-PI.1` estaban en pausa porque no habia accion local concreta.

La instruccion operativa actual pide desactivar vision papers y avanzar en frentes sustantivos. `PPI-MARCO-CORE-001` provee una accion concreta, limitada y auditable: definir vocabulario minimo, separar equivalencia de proyecciones de confluencia y preparar casos locales.

## Consecuencia operativa

`P-PI.0` y `P-PI.1` dejan de estar en pausa operativa general.

La nueva ruta activa no resuelve los problemas, pero habilita trabajo sustantivo:

1. ejecutar `PPI-EQ-001`;
2. ejecutar `PPI-EQ-002`;
3. usar esos resultados para preparar `PPI-CONF-001`.

## Deudas que permanecen

- Consolidar material historico si aparece fuente local pertinente.
- Ejecutar los casos de prueba propuestos.
- Decidir si `P-PI.0` y `P-PI.1` conservan esta division local o si se abren subexpedientes separados.
- Mantener Confluencia y Equivalencia de proyecciones como problemas abiertos.
- Mantener `VISION_PAPER_PROPUESTA.md` y `VISION_PAPER_FINAL_REFERENCIAS.md` inactivos hasta nueva decision.

## Veredicto

`P-PI.0`: activo acotado.

`P-PI.1`: activo acotado.

Marco inicial: aceptado como provisional de expediente.

Problemas abiertos: no resueltos.
