# DSL declarativa inicial: `spherepack.dsl.initial.v1`

## Proposito

**[DEFINICION_PROPUESTA]** La DSL describe instancias finitas y preguntas de transicion. No ejecuta optimizadores, simuladores dinamicos, modelos de IA ni llamadas de red.

## Caso minimo

```json
{
  "case_id": "C6-octahedral-threshold",
  "kind": "CENTERED_CONFIGURATION",
  "n": 6,
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
| `outer_radius` | numero | Debe ser exactamente `1` en v1 |
| `central_radius` | numero | Estrictamente positivo para una instancia materializada |
| `directions` | lista de triples | Se normalizan para calculo; la entrada no acredita optimalidad |
| `epistemic_status` | enumeracion | Una de las etiquetas del proyecto |

## Consulta de transicion propuesta

```json
{
  "case_id": "T-square-to-octahedron",
  "kind": "TRANSITION_QUERY",
  "n": 4,
  "outer_radius": 1,
  "central_radius": 0.414214,
  "directions": [[1,0,0], [0,1,0], [-1,0,0], [0,-1,0]],
  "target_case_id": "C6-octahedral-threshold",
  "preservation_mode": "INCLUSION_LITERAL_DE_DIRECCIONES",
  "epistemic_status": "RESULTADO_COMPUTADO"
}
```

El validador estructural actual no infiere `preservation_mode`; una futura version debera incorporarlo como campo requerido para `TRANSITION_QUERY` y validar sus valores sin ejecutar ningun proceso fisico.

## Semantica de salida

Los estados permitidos son `SEPARACION`, `TANGENCIA_EXACTA` y `SOLAPAMIENTO_FISICO`; se derivan solo del signo de la holgura con tolerancia publicada. `WITNESS_FOR_THIS_REPRESENTATIVE_ONLY` nunca significa teorema universal de transicion.
