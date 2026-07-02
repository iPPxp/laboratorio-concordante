# PSI-001 - Matriz de Patrones de Transformacion No Clinica

Estatus: matriz provisional de expediente.

Identificador provisional: `PSI-MAT-PAT-001`.

Fecha: 2026-07-02.

## Proposito

Sintetizar `CAS-PSI-001` a `CAS-PSI-006` en una matriz de patrones no clinicos de transformacion dentro de `PSI-001`.

La matriz no diagnostica, no clasifica personas, no recomienda tratamiento y no autoriza intervencion psicologica. Su funcion es ordenar patrones formales de cambio en la organizacion de la experiencia psicologica.

## Base de entrada

- `DEF-PSI-ORG-001`: definicion provisional de organizacion de la experiencia psicologica.
- `CRIT-PSI-TR-001`: criterio provisional de transformacion, reorganizacion, desorganizacion, disolucion y no auditable.
- `CAS-PSI-001` a `CAS-PSI-006`: serie breve de casos conceptuales no clinicos.

## Matriz principal

| Patron | Caso fuente | Cambio principal | Continuidad minima | Cambio en `R` | Clasificacion | Bloqueo |
| --- | --- | --- | --- | --- | --- | --- |
| Relevancia relacional | `CAS-PSI-001` | El centro deja de depender de prominencia inmediata y pasa a depender de funcion relacional. | Se conservan signos y unidad de ordenamiento. | `brillo-foco-centro` pasa a `funcion-conexion-centro`. | `reorganizacion` | Ninguno. |
| Foco estructural local | `CAS-PSI-002` | El foco cambia de entrada inicial a contraste interno. | Se conserva la secuencia de tonos. | `tono-entrada-secuencia` pasa a `tono-contraste-secuencia`. | `transformacion` | Ninguno. |
| Dependencia narrativa | `CAS-PSI-003` | El enlace cambia de orden temporal a dependencia de sentido. | Se conservan escenas y unidad narrativa abstracta. | `antes-despues-secuencia` pasa a `condicion-explicacion-escena`. | `reorganizacion` | Ninguno. |
| Conflicto de reglas | `CAS-PSI-004` | Dos reglas incompatibles compiten sin prioridad. | Se conservan fragmentos comparables de clasificacion. | `forma-clase-orden` se divide en relaciones incompatibles de forma y posicion. | `desorganizacion` | Falta estabilidad nueva. |
| Perdida de trayecto | `CAS-PSI-005` | La unidad de itinerario se pierde y quedan elementos aislados. | Continuidad insuficiente. | `origen-transito-destino` se pierde como relacion comun. | `disolucion` | Falta unidad minima comparable. |
| Salida de alcance | `CAS-PSI-006` | La descripcion se desplaza a persona real, interpretacion o consejo. | No aplica. | `relato-real-interpretacion` pasa a `interpretacion-consejo-accion`. | `no auditable` | Uso clinico o personal. |

## Patrones abstractos derivados

### P-PSI-001 - Cambio de centro organizador

Un patron de cambio de centro organizador ocurre cuando la unidad conserva contenidos comparables, pero cambia el criterio que decide que elemento queda al centro.

Puede producir `reorganizacion` si el nuevo criterio estabiliza relaciones.

### P-PSI-002 - Cambio local de foco

Un cambio local de foco ocurre cuando se desplaza la atencion dentro de una unidad estable sin alterar el patron relacional completo.

Puede producir `transformacion` sin llegar a `reorganizacion`.

### P-PSI-003 - Cambio de enlace narrativo

Un cambio de enlace narrativo ocurre cuando los mismos contenidos pasan de una organizacion por secuencia a una organizacion por dependencia de sentido.

Puede producir `reorganizacion` si aparece una nueva estabilidad descriptible.

### P-PSI-004 - Conflicto de criterios

Un conflicto de criterios ocurre cuando dos o mas reglas organizadoras compiten sin prioridad local suficiente.

Puede producir `desorganizacion` si quedan fragmentos comparables, pero no aparece una nueva estabilidad.

### P-PSI-005 - Perdida de unidad minima

La perdida de unidad minima ocurre cuando ya no puede sostenerse que `E1` continue la misma unidad conceptual que `E0`.

Produce `disolucion` dentro de `PSI-001`.

### P-PSI-006 - Salida de alcance clinico-personal

La salida de alcance ocurre cuando una descripcion abstracta se convierte en relato personal real, diagnostico, consejo, tratamiento o evaluacion de una persona.

Produce `no auditable` y debe detener el expediente o exigir reformulacion abstracta.

## Regla de lectura

Para usar la matriz, seguir este orden:

1. Delimitar la unidad conceptual.
2. Identificar `E0`, `E1`, `O0`, `O1`, `R0` y `R1`.
3. Preguntar que se conserva: contenido, unidad, continuidad relacional o solo fragmentos.
4. Preguntar que cambia: foco, centro, enlace, regla, unidad o alcance.
5. Clasificar con `CRIT-PSI-TR-001`.
6. Bloquear como `no auditable` si aparece persona real, diagnostico, tratamiento, consejo profesional o admision automatica de `H-Xi`.

## Guardrails

- No diagnosticar personas.
- No nombrar trastornos como resultado de la matriz.
- No recomendar tratamiento, terapia o conducta.
- No convertir desorganizacion o disolucion conceptual en psicopatologia clinica.
- No admitir `H-Xi` ni reabrir `HXI-001`.
- No modificar Canon ni documentos oficiales.

## Valor para continuidad

La matriz deja una base ordenada para una futura frontera entre psicologia no clinica y psicopatologia conceptual.

Esa frontera debera estudiar patrones como rigidez, fragmentacion, bloqueo, sufrimiento abstracto y perdida de flexibilidad solo como formas conceptuales, no como diagnosticos.

## Resultado

`PSI-MAT-PAT-001` queda como matriz provisional de patrones no clinicos de transformacion dentro de `PSI-001`.

La siguiente pieza natural es definir una compuerta de frontera para psicopatologia conceptual no clinica, antes de abrir cualquier subfrente psicopatologico.
