# Ontologia humana y contrato de maquina inicial

## Alcance

**[DEFINICION_PROPUESTA]** Esta ontologia solo describe objetos y afirmaciones del proyecto de empaquetamientos. No asigna significado humano, autoridad MOC, diagnostico, valor moral o funcion clinica a sus clases.

## Entidades humanas

| Tipo | Definicion operativa | Campos minimos |
|---|---|---|
| `Sphere` | Bola o hiperesfera geometrica con centro y radio en dimensión declarada | `id`, `ambient_dimension`, `center`, `radius`, `role` |
| `CenteredConfiguration` | Central y exteriores situadas a radio comun declarado en `R^d` | `n`, `ambient_dimension`, `epsilon`, `directions`, `centeredness_evidence` |
| `ContactRelation` | Par de esferas y su holgura | `source`, `target`, `delta`, `relation` |
| `SphericalCode` | Direcciones unitarias de `S^(d-1)` con separacion angular | `ambient_dimension`, `directions`, `min_angle`, `domain` |
| `Lattice` | Red discreta o red periodica con base | `vectors`, `basis`, `kind` |
| `Shell` | Vecinos de una esfera central a distancia definida | `parent_configuration`, `coordination_number` |
| `SimplexInterstitial` | `d+1` anfitrionas simplex y la bola desigual que toca a todas | `ambient_dimension`, `host_count`, `host_radius`, `interstitial_radius`, `contact_graph` |
| `KissingShell` | Vecinas congruentes que tocan una central congruente | `ambient_dimension`, `neighbour_count`, `common_radius`, `contact_graph` |
| `TwoHostCollinearLimit` | Familia `n=2` seleccionada por punto medio y colinealidad | `host_radius`, `central_radius`, `host_center_distance`, `limit_status` |
| `TransitionQuery` | Pregunta tipada entre configuraciones | `source`, `target`, `preservation_mode` |
| `Claim` | Afirmacion con etiqueta epistemica y procedencia | `label`, `scope`, `evidence` |
| `ExperimentRun` | Ejecucion local determinista de un script | `command`, `environment`, `outputs` |

## Relaciones

| Relacion | Dominio -> codominio | Regla |
|---|---|---|
| `has_center` | `Sphere -> PointD` | Un centro unico de dimensión compatible por esfera |
| `surrounds` | `CenteredConfiguration -> Sphere` | La esfera central tiene radio `epsilon` |
| `has_direction` | `CenteredConfiguration -> UnitVectorD` | Una direccion de `S^(d-1)` por exterior |
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
9. Todas las filas de una configuración pertenecen al mismo `R^d`; operaciones
   entre configuraciones de dimensiones diferentes fallan cerradas.
10. `SimplexInterstitial(d)` exige `host_count == d+1`; su grafo anfitrión es
    `K_(d+1)` y el grafo con la central es `K_(d+2)`.
11. `KissingShell(d)` usa vecinas y central congruentes; no se identifica con
    `SimplexInterstitial(d)`. En `d=4`, la realización incorporada tiene 24
    vecinas `D4`, 96 contactos exteriores y 120 contactos totales.
12. En `TwoHostCollinearLimit`, `D == 2(R+r)`. `r>0` es una bola realizada;
    `r=0` es solamente el límite puntual y no una esfera positiva.

## Ambiguedades conservadas como no resueltas

- `Centered`: puede significar centro en la envolvente convexa, baricentro,
  simetria, o interior de dimensión completa. El codigo informa certificado por
  pesos iguales y rango afín respecto de `ambient_dimension`, sin fingir que
  son equivalentes.
- `Degenerante`: aun no tiene una definicion unica. Podra referir limite `epsilon -> 0`, perdida de rango, cambio de grafo de contacto o colision de celda. Cada uso futuro debe declarar cual.
- `Estabilidad`: no se identifica con no solapamiento. Rigidez infinitesimal, jamming y estabilidad energetica son predicados distintos.
