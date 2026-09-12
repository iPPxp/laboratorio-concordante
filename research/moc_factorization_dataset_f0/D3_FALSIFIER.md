# Falsador de D3 como operación separada

## 1. Hipótesis competidoras

`DIFFERENTIATE(x,y)` puede ser:

- D0: etiqueta descriptiva sin operación;
- D1: creación/refinamiento real de una distinción;
- D2: macro útil pero reducible;
- D3: operación estructural con poder incremental;
- alternativa A: `Update(P)`;
- alternativa B: `Update(R)`;
- alternativa C: `Update(K)`;
- alternativa D: composición de A–C.

No se presupone que D3 exista en canon ni que `D` sea un sexto componente.

## 2. Semántica operacional neutral

Una operación candidata recibe estado estructurado \(X=(D,P,R,K,\mathcal P)\) y devuelve pre/post más traza. D3 sólo merece separación computacional si existe al menos una familia holdout donde ningún programa simple compuesto por updates P/R/K preserve conjuntamente:

1. partición o distinción resultante;
2. relaciones y restricciones;
3. campo/transitabilidad;
4. outcomes sellados;
5. provenance y coste dentro de tolerancia.

## 3. Prueba de equivalencia

Para cada traza D3 buscar traducción congelada

\[
f:D3\to Update(P,R,K)^*
\]

sin reglas por caso. Comparar equivalencia exacta, observacional y de outcomes. Penalizar longitud de programa, excepciones y acceso informacional. Nombres diferentes no rompen equivalencia.

## 4. M-D3-ABL y M-D3-SUB

- `M-D3-ABL`: retirar D3; si no cae ningún criterio fuera de muestra, necesidad no demostrada.
- `M-D3-SUB`: sustituir cada D3 por la mejor composición P/R/K con presupuesto igual.
- `M-D3-PERM`: asignar la marca D3 a updates que no diferencian; detecta dependencia nominal.
- `M-D3-NULL`: ejecutar D3 sin cambio estructural; controla narración de distinción.

## 5. Outcomes independientes

Evaluar sólo outcomes sellados de trayectoria: resolución de restricciones, viabilidad futura, error, revisión, recursos y secuencias observables. No usar “acertó la distinción MOC” como outcome primario.

## 6. Resultado desconfirmante

Si una traducción simple preserva estructura, campo, outcomes y provenance en transformaciones no vistas:

```text
D3_SEPARATE_OPERATION = NOT_SUPPORTED
D3_EQUIVALENT_TO_UPDATE_PRK = SUPPORTED_IN_TESTED_DOMAIN
```

Si sólo preserva outcomes pero D3 comprime trazas o generaliza mejor, registrar valor representacional, no irreducibilidad. Si el dataset no contiene casos identificadores suficientes: `INSUFFICIENT_EVIDENCE`.

## 7. Casos mínimos adversariales

1. acción/resultado se separan y sólo cambia P;
2. misma separación codificada como tipo de R;
3. separación implementada como constraint de incompatibilidad;
4. D3 nominal sin efecto;
5. P/R/K cambian simultáneamente;
6. distinción nueva no cambia outcome;
7. distinción cambia transitabilidad sin acción nueva;
8. fusión inversa mejora outcome;
9. vocabulario permutado;
10. holdout con distinción no vista.

El falsador se decide antes de observar anotaciones MOC.
