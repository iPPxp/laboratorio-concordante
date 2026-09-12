# Modelo de relaciones y propagación

\(R_t\) es un hipergrafo tipado y parcial; una relación registra `id, endpoints, arity, type, direction, scope, source, evidence, confidence, status`. No se presume completitud, simetría ni cierre simplicial.

Una edición relacional puede cambiar tipo, dirección, fuerza ordinal, condición contextual o endpoint sin cambiar inicialmente los vértices. Esto permite probar \(R_{P,V}\), \(R_{P,S}\), \(R_{Act,V}\) y relaciones superiores sin inventarlas como MOC.

## Propagación

Para cada relación \(r_{ij}\),

```text
CHANGED | UNCHANGED | UNKNOWN | NOT_APPLICABLE
```

`CHANGED` exige evidencia comparable de before/after; `UNCHANGED`, medición suficiente compatible con igualdad definida; `UNKNOWN`, medición ausente/insuficiente; `NOT_APPLICABLE`, relación fuera del dominio. Nunca inferir \(\Delta P\Rightarrow\Delta R_{P,*}\).

La matriz \(M_{ij}\) almacena uno de esos estados más evidencia; no es matriz causal completa. Para composición conservadora: cualquier dependencia relevante `UNKNOWN` impide declarar propagación completa; `NA` se excluye del denominador, no se trata como cero.

Falsador de irreducibilidad relacional: un vector de vértices con igual presupuesto predice \(\Delta\mathcal P\) tan bien como el modelo relacional en casos con vértices controlados.
