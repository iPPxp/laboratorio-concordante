# Ontologia humana y contrato de maquina inicial

## Alcance

**[DEFINICION_PROPUESTA]** Esta ontologia solo describe objetos y afirmaciones del proyecto de empaquetamientos. No asigna significado humano, autoridad MOC, diagnostico, valor moral o funcion clinica a sus clases.

## Entidades humanas

| Tipo | Definicion operativa | Campos minimos |
|---|---|---|
| `Sphere` | Esfera geometrica con centro y radio | `id`, `center`, `radius`, `role` |
| `CenteredConfiguration` | Esfera central y exteriores situadas a radio comun declarado | `n`, `epsilon`, `directions`, `centeredness_evidence` |
| `ContactRelation` | Par de esferas y su holgura | `source`, `target`, `delta`, `relation` |
| `SphericalCode` | Direcciones unitarias con separacion angular | `directions`, `min_angle`, `domain` |
| `Lattice` | Red discreta o red periodica con base | `vectors`, `basis`, `kind` |
| `Shell` | Vecinos de una esfera central a distancia definida | `parent_configuration`, `coordination_number` |
| `TransitionQuery` | Pregunta tipada entre configuraciones | `source`, `target`, `preservation_mode` |
| `Claim` | Afirmacion con etiqueta epistemica y procedencia | `label`, `scope`, `evidence` |
| `ExperimentRun` | Ejecucion local determinista de un script | `command`, `environment`, `outputs` |

## Relaciones

| Relacion | Dominio -> codominio | Regla |
|---|---|---|
| `has_center` | `Sphere -> Point3` | Un centro unico por esfera |
| `surrounds` | `CenteredConfiguration -> Sphere` | La esfera central tiene radio `epsilon` |
| `has_direction` | `CenteredConfiguration -> UnitVector3` | Una direccion por exterior |
| `has_clearance` | `ContactRelation -> Real` | Signo de `delta` define la lectura de contacto |
| `induced_by` | `CenteredConfiguration -> SphericalCode` | Solo en el modelo cosferico declarado |
| `has_basis` | `Lattice -> Basis` | HCP conserva base explicita |
| `queries` | `TransitionQuery -> CenteredConfiguration` | Debe declarar clase de preservacion |
| `supports` | `Evidence -> Claim` | No cambia automaticamente la etiqueta epistemica |

## Restricciones que deben fallar cerradas

1. `outer_radius == 1` en la version normalizada.
2. `epsilon > 0` para una realizacion, aunque el informe pueda guardar un infimo cero.
3. `delta < 0` invalida una configuracion fisica de esferas duras.
4. `HCP.kind != BRAVAIS_SIMPLE`.
5. Toda transicion debe declarar una `preservation_mode`; el salto de cardinalidad no la infiere.
6. `RESULTADO_COMPUTADO` requiere comando, version de codigo, entradas y artefactos de salida.
7. Un `Claim` de tipo `DEMOSTRADO_EN_ESTE_TRABAJO` requiere una prueba legible o un certificado verificable, no solo una imagen o un test.
8. Un resultado sobre un conjunto finito no se eleva a teorema universal sin cuantificadores y prueba correspondiente.

## Ambiguedades conservadas como no resueltas

- `Centered`: puede significar centro en la envolvente convexa, baricentro, simetria, o interior tridimensional. El codigo informa certificado por pesos iguales y rango affine, sin fingir que son equivalentes.
- `Degenerante`: aun no tiene una definicion unica. Podra referir limite `epsilon -> 0`, perdida de rango, cambio de grafo de contacto o colision de celda. Cada uso futuro debe declarar cual.
- `Estabilidad`: no se identifica con no solapamiento. Rigidez infinitesimal, jamming y estabilidad energetica son predicados distintos.
