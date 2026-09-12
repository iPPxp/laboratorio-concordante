# MOC-RC1-GEOMETRY-EXTENSION-001

## Dictamen de arquitectura

El objeto mínimo útil incorporado es un **sistema relacional dinámico tipado**:

```text
X_t = (N, O_t, R_t, H_t, U_t, Prov_t)
```

donde:

- `N = {P,Eaf,Act,V,S}` es el conjunto fijo de nombres admitidos;
- `O_t` contiene observaciones, presencia, cambio y vectores declarados;
- `R_t` contiene relaciones tipadas y dirigidas;
- `H_t` conserva comparación temporal;
- `U_t` conserva ambigüedad, desconocimiento y confianza;
- `Prov_t` conserva fuentes, atribución y operaciones.

No se adopta una figura como ontología primaria. `K5`, el 4-símplex, el
pentágono y cualquier dibujo son vistas posibles de una estructura que debe
existir antes que ellos.

## Separación de objetos

```text
ESTRUCTURA_FUNDAMENTAL = sistema_relacional_dinamico_tipado
REPRESENTACION = inventario_simplicial_o_proyeccion_declarada
IMPLEMENTACION = sidecar_inmutable_sobre_RC1
```

### Estructura fundamental

Conserva cinco componentes, relaciones no necesariamente simétricas,
incertidumbre, procedencia y tiempo. Las relaciones pueden estar ausentes,
presentes o sólo catalogadas como hipótesis.

### Representación

La enumeración del conjunto de cinco elementos produce necesariamente:

```text
5 vértices
10 pares
10 tríadas
5 cuaternas
1 conjunto completo
```

La extensión calcula ese inventario, pero no le atribuye por sí mismo contenido
MOC. También calcula la correspondencia de cada elemento con su cuaterna
complementaria sin interpretarla psicológicamente.

Una vista 2D sólo se permite mediante `ProjectionSpec`. El resultado informa
colisiones y, cuando se declara métrica euclídea, distorsión de distancias. Toda
vista se marca `is_visualization_only=True`.

### Implementación

`adapt_rc1_matrix` exige una biyección declarada entre las cinco filas presentes
en `MatrixQ` y `P/Eaf/Act/V/S`. No existe mapeo por defecto. El adaptador no
muta RC1, no añade relaciones observadas y registra que la correspondencia fue
suministrada por quien llama.

## Diez relaciones candidatas

`candidate_relation_catalogue()` registra exactamente una entrada por cada par.
Sus estatutos son desiguales:

- `P→Eaf` y `P↔Act`: apoyo textual en el corpus revisado;
- `P↔S`, `Eaf→Act`, `Eaf↔S`, `V→Act`, `Act↔S`: candidatas parciales;
- `V→P`, `Eaf↔V`, `V↔S`: hipótesis que requieren decisión y prueba;
- `Eaf↔S` se registra como mediada por `P`;
- ninguna se instancia como arista observada por defecto.

Esto impide que el simple hecho de tener cinco elementos produzca un `K5`
semántico ficticio.

## Falsadores

La extensión debe rechazarse o revisarse si:

1. necesita inferir automáticamente `I=P`;
2. introduce `conducta` como sexto componente;
3. una arista candidata aparece como observación sin evidencia;
4. presencia y cambio vuelven a colapsarse;
5. `ABSENT` puede surgir del mero silencio;
6. una proyección 2D se presenta como representación completa;
7. distancia geométrica se presenta como distancia semántica sin contrato;
8. simetría, centroide o proporción áurea reciben significado automático;
9. la extensión muta bytes cubiertos por el freeze de RC1;
10. un test local se presenta como validación psicológica o científica.

## Estado epistemológico

```text
MATHEMATICAL_COMBINATORICS = ESTABLISHED
SOFTWARE_CONTRACT = LOCALLY_TESTABLE
PAIRWISE_RELATION_CATALOGUE = CANDIDATE_AND_HYPOTHESIS
RC1_COMPATIBILITY = SIDE_CAR_ONLY
MOC_SEMANTIC_APPROVAL = NOT_GRANTED
SCIENTIFIC_VALIDATION = NOT_TESTED
```
