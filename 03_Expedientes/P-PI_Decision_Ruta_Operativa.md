# P-PI - Decision de ruta operativa

Estatus: decision provisional de expediente, superada operativamente para trabajo acotado por `D-2026-07-02-032`.

ID: `RUTA-PPI-001`.

Fecha de ratificacion local: 2026-07-02.

Expedientes afectados: `P-PI.0` y `P-PI.1`.

Objeto decidido: ruta operativa previa de `P-PI.0` y `P-PI.1`.

Compuerta aplicada: `P-PI_Decision_Estatus_Criterios_Cierre.md`.

Estado posterior: `P-PI_Decision_Reactivacion_Frente_Matematico.md` reactiva `P-PI.0` y `P-PI.1` de forma acotada para Equivalencia de proyecciones y Confluencia. Esta decision conserva valor historico y de guardrail, pero ya no define el frente activo inmediato.

## Fuentes leidas

- `HANDOFF.md`
- `CURRENT_STATE.md`
- `05_Estado_Proyecto/ESTADO_ACTUAL.md`
- `05_Estado_Proyecto/DECISION_Siguiente_Frente_Activo_P-PI.md`
- `03_Expedientes/P-PI.0.md`
- `03_Expedientes/P-PI.1.md`
- `03_Expedientes/P-PI_Criterios_Cierre.md`
- `03_Expedientes/P-PI_Auditoria_Criterios_Cierre.md`
- `03_Expedientes/P-PI_Decision_Estatus_Criterios_Cierre.md`
- `01_Canon/M-000_Reglas_Fundamentales.md`
- `01_Canon/M-001_Auditoria_Arquitectonica.md`

## Decision

`P-PI.0` y `P-PI.1` quedan abiertos en pausa operativa.

Estatus asignado:

```text
P-PI.0 = abierto en pausa operativa
P-PI.1 = abierto en pausa operativa
```

La decision queda ratificada tras aplicar explicitamente la compuerta aceptada.

## Alcance permitido

La decision permite:

- retirar `P-PI.0` y `P-PI.1` del frente activo inmediato
- conservar ambos expedientes como abiertos
- mantener Confluencia y Equivalencia de proyecciones como problemas abiertos
- reconocer que falta material historico o local suficiente para trabajo sustantivo inmediato
- reactivar cualquiera de los dos expedientes si aparece material local registrado o una decision posterior define una accion concreta

## Alcance no permitido

La decision no permite:

- cerrar `P-PI.0`
- cerrar `P-PI.1`
- congelar definitivamente los expedientes
- absorberlos en otro expediente o documento
- resolver Confluencia por declaracion
- resolver Equivalencia de proyecciones por declaracion
- usar fuentes historicas no registradas como autoridad directa
- modificar Canon o documentos oficiales

## Aplicacion de la compuerta

La compuerta aceptada exige una ruta explicita antes de cambiar el estatus operativo de los expedientes.

Tambien exige separar alcance local, problemas abiertos, dependencias externas, fuentes leidas, afirmaciones clasificadas, impacto sobre estado y advertencia contra cierres que aparenten resolver problemas matematicos.

Con el material local disponible:

- ambos expedientes solo contienen proposito pendiente de consolidacion
- ambos conservan relacion directa con Confluencia y Equivalencia de proyecciones
- no hay accion local concreta que pueda ejecutarse sin material historico adicional
- no hay destino de absorcion definido
- no hay base suficiente para cierre operativo

La ruta de pausa operativa cumple la compuerta sin inflar el estatus de los expedientes.

## Clasificacion de afirmaciones relevantes

| Afirmacion | Clasificacion |
| --- | --- |
| `P-PI.0` y `P-PI.1` existen como expedientes locales | expediente |
| `P-PI_Criterios_Cierre.md` es compuerta aceptada | decision / criterio provisional de expediente |
| Confluencia permanece sin resolver | problema abierto |
| Equivalencia de proyecciones permanece sin resolver | problema abierto |
| Falta consolidar proposito desde fuentes historicas o documentos previos | deuda conceptual |
| No hay accion local concreta ejecutable sin material adicional | deuda conceptual / restriccion operativa |
| Pausa operativa de `P-PI.0` y `P-PI.1` | decision |

## Fuentes faltantes o no usadas como autoridad

- Fuentes historicas o documentos previos que consoliden el proposito de `P-PI.0`.
- Fuentes historicas o documentos previos que consoliden el proposito de `P-PI.1`.
- Tratamiento formal propio de Confluencia.
- Tratamiento formal propio de Equivalencia de proyecciones.

Estas fuentes pueden motivar una reapertura o una ruta distinta cuando existan como material local trazable. Mientras falten, no se usan para cerrar, congelar, absorber ni resolver los expedientes.

## Motivo

La evidencia local favorece una salida defensiva: no hay contenido suficiente para continuidad activa ni cierre, y tampoco hay destino de absorcion.

El congelamiento seria posible si los expedientes funcionaran solo como trazas sin uso operativo actual. Sin embargo, `P-PI.0` y `P-PI.1` siguen enlazados a problemas abiertos vigentes del Laboratorio.

Por eso la ruta mas defensible es pausa operativa: conserva la traza, evita cierre prematuro, no borra la deuda vinculada a Confluencia y Equivalencia de proyecciones, y libera el frente activo inmediato.

## Ruta por expediente

| Expediente | Evidencia local | Ruta aplicada | Problemas conservados |
| --- | --- | --- | --- |
| `P-PI.0` | proposito pendiente de consolidacion; sin accion local inmediata | abierto en pausa operativa | Confluencia; Equivalencia de proyecciones |
| `P-PI.1` | proposito pendiente de consolidacion; sin accion local inmediata | abierto en pausa operativa | Confluencia; Equivalencia de proyecciones |

## Condiciones de reactivacion

Cualquiera de los dos expedientes puede reactivarse si ocurre al menos una de estas condiciones:

- se incorpora material historico como archivo local trazable
- se identifica una accion local concreta que no dependa de historial ausente
- una decision posterior define que `P-PI.0` o `P-PI.1` debe pasar a cierre, congelamiento, absorcion o continuidad activa
- Confluencia o Equivalencia de proyecciones reciben tratamiento propio que requiera usar estos expedientes

## Consecuencia operativa

`P-PI.0` y `P-PI.1` dejan de ser el frente activo inmediato.

Ambos permanecen abiertos en pausa operativa.

`05_Estado_Proyecto/ESTADO_ACTUAL.md`, `CURRENT_STATE.md` y `HANDOFF.md` deben conservarlos como expedientes abiertos en pausa operativa, no como cerrados, congelados ni absorbidos.

El siguiente objetivo vigente del Laboratorio permanece fuera de `P-PI`: continuar el frente conceptual activo ya registrado, salvo decision posterior.

## Deudas que permanecen

- Mantener Confluencia y Equivalencia de proyecciones como problemas abiertos hasta tratamiento propio.
- Consolidar el proposito de `P-PI.0` desde fuentes historicas o documentos previos antes de cualquier trabajo sustantivo.
- Consolidar el proposito de `P-PI.1` desde fuentes historicas o documentos previos antes de cualquier trabajo sustantivo.
- Registrar cualquier fuente historica antes de usarla como fundamento.
- No cerrar, congelar ni absorber `P-PI.0` o `P-PI.1` sin decision separada.
- No tratar la pausa como resolucion de Confluencia, Equivalencia de proyecciones, `R4` o `Gamma`.

## Veredicto

`P-PI.0`: abierto en pausa operativa.

`P-PI.1`: abierto en pausa operativa.

Cierre, congelamiento o absorcion: no procede por esta decision.

Resolucion de Confluencia o Equivalencia de proyecciones: no procede por esta decision.
