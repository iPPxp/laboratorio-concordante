# DSL declarativa dimensional: `spherepack.dsl.dimension-aware.v2`

## Proposito

**[DEFINICION_PROPUESTA]** La DSL describe instancias finitas y preguntas de transicion. No ejecuta optimizadores, simuladores dinamicos, modelos de IA ni llamadas de red.

## Caso minimo

```json
{
  "case_id": "C6-octahedral-threshold",
  "kind": "CENTERED_CONFIGURATION",
  "n": 6,
  "ambient_dimension": 3,
  "outer_radius": 1,
  "central_radius": 0.414214,
  "directions": [[1,0,0], [-1,0,0], [0,1,0], [0,-1,0], [0,0,1], [0,0,-1]],
  "epistemic_status": "RESULTADO_COMPUTADO"
}
```

## Campos y reglas

| Campo | Tipo | Regla |
|---|---|---|
| `case_id` | cadena | Identificador local, no identificador canonico |
| `kind` | enumeracion | `CENTERED_CONFIGURATION`, `LATTICE_REFERENCE` o `TRANSITION_QUERY` |
| `n` | entero | Debe coincidir con el numero de direcciones |
| `ambient_dimension` | entero positivo | Longitud común de cada dirección; declara `R^d` |
| `outer_radius` | numero | Debe ser exactamente `1` en v2; otras escalas se comparan fuera de la DSL normalizada |
| `central_radius` | numero | Estrictamente positivo para una instancia materializada |
| `directions` | matriz `n x d` finita | Filas no nulas de longitud `ambient_dimension`; se normalizan para calculo |
| `epistemic_status` | enumeracion | Una de las etiquetas del proyecto |

## Consulta de transicion propuesta

```json
{
  "case_id": "T-square-to-octahedron",
  "kind": "TRANSITION_QUERY",
  "n": 4,
  "ambient_dimension": 3,
  "outer_radius": 1,
  "central_radius": 0.414214,
  "directions": [[1,0,0], [0,1,0], [-1,0,0], [0,-1,0]],
  "target_case_id": "C6-octahedral-threshold",
  "preservation_mode": "INCLUSION_LITERAL_DE_DIRECCIONES",
  "epistemic_status": "RESULTADO_COMPUTADO"
}
```

El validador estructural no infiere `preservation_mode`; una futura version
debera incorporarlo como campo requerido para `TRANSITION_QUERY` y validar sus
valores sin ejecutar ningun proceso fisico. El motor geométrico rechaza una
comparación de direcciones cuando origen y destino pertenecen a dimensiones
ambiente distintas.

## Ejemplo 4D: cinco direcciones del 4-simplex

```json
{
  "case_id": "C5-4-simplex",
  "kind": "CENTERED_CONFIGURATION",
  "n": 5,
  "ambient_dimension": 4,
  "outer_radius": 1,
  "central_radius": 0.2649110640673518,
  "directions": [
    [0.790569415042095, 0.456435464587638, 0.322748612183951, 0.25],
    [-0.790569415042095, 0.456435464587638, 0.322748612183951, 0.25],
    [0, -0.912870929175277, 0.322748612183951, 0.25],
    [0, 0, -0.968245836551854, 0.25],
    [0, 0, 0, -1]
  ],
  "epistemic_status": "DERIVACION_SIMBOLICA"
}
```

Estas coordenadas son la evaluación numérica de la construcción de Helmert;
el contrato exacto es `||u_i||=1` y `u_i . u_j=-1/4` para `i!=j`.

## Semantica de salida

Los estados permitidos son `SEPARACION`, `TANGENCIA_EXACTA` y
`SOLAPAMIENTO_FISICO`. Para conservar la clasificación bajo cambios de escala,
la comparación usa la holgura adimensional `delta / outer_radius` y una
tolerancia publicada en esas unidades. La holgura física continúa reportándose
en las unidades de entrada. `WITNESS_FOR_THIS_REPRESENTATIVE_ONLY` nunca
significa teorema universal de transicion.
