# Semántica provisional de reorganización relacional endógena

**Estatus:** hipótesis de investigación restringida por el baseline de autoridad. No declara a `Xi` operador vigente.

## Distinciones mínimas

Sea `R_t` una configuración relacional declarada dentro de una unidad y alcance específicos. Una diferencia `R_t != R_{t+1}` sólo prueba cambio, no reorganización.

Se propone llamar **reorganización relacional estable** a una transición candidata cuando, bajo evidencia suficiente:

1. se conserva la unidad mínima comparable;
2. cambia al menos una relación o restricción relevante, no sólo el contenido;
3. aparece una configuración posterior coherente dentro del alcance;
4. las restricciones son compatibles con la transición;
5. el cambio no se clasifica mejor como conflicto sin estabilidad, disolución, no comparabilidad o bloqueo.

Esto resume la lógica local de `Xi_eval`; no añade semántica humana ni causalidad.

## Evaluar no es producir

La operación documentada localmente es:

```text
Xi_eval_MOC(R0, R1, Dist, Res, alcance, evidencia, restricciones)
  -> {redundante, util_acotado, limitado, no_comparable, bloqueado}
```

Un operador generativo de reorganización tendría otra firma, todavía hipotética:

```text
Xi_reorg(R0, contexto, restricciones, evidencia)
  -> candidatos_R1 + trazas
```

No se permite derivar `Xi_reorg` de la existencia de `Xi_eval`. Evaluar una pareja conocida no demuestra capacidad para detener, descomponer, reencuadrar o editarla.

## Clasificación de capacidades atribuidas a Xi

Definiciones de estado:

- `DOCUMENTED`: la fuente vigente/local describe explícitamente esa operación con una firma compatible.
- `SUPPORTED_INFERENCE`: consecuencia estrecha de fuentes documentadas, sin elevarla a operación ejecutiva.
- `HYPOTHESIS`: extensión falsable plausible, no establecida.
- `NOT_SUPPORTED`: atribución ausente o contradicha por el alcance actual.

| Capacidad propuesta | Clasificación | Evidencia y límite |
|---|---|---|
| `stop` | `NOT_SUPPORTED` | `Xi_eval` puede emitir `no_comparable` o `bloqueado`, pero eso detiene una evaluación; no documenta que `Xi` detenga una dinámica experiencial. |
| `decompose` | `SUPPORTED_INFERENCE` sólo como análisis | `H-Xi` propone distinguir posibilidades y `Xi_eval` usa `Dist(R0,R1)`; inferir una partición analítica es razonable. Descomponer causalmente una experiencia sigue `HYPOTHESIS`. |
| `reframe` | `NOT_SUPPORTED` | no se recuperó una operación explícita de reencuadre en las fuentes vigentes inspeccionadas. Reetiquetar una relación no basta. |
| `relation edit` | `HYPOTHESIS` | la utilidad local documentada concierne a describir cambios de relaciones entre `R0` y `R1`. `Xi_eval` no produce ni edita `R1`; una edición endógena requiere operador nuevo. |
| `constraint edit` | `HYPOTHESIS` | `H-Xi` y `Xi_eval` representan restricciones de transición, pero no autorizan ni ejecutan su edición. |
| `possibility reopen` | `NOT_SUPPORTED` como capacidad Xi | `H-Xi` distingue posibilidades y el grafo auxiliar contiene `A_exp`/apertura de expectativa, pero ninguna fuente inspeccionada atribuye a Xi la reapertura operativa de posibilidades. |

Resumen sin ambigüedad:

```text
XI_STOP = NOT_SUPPORTED
XI_DECOMPOSE_ANALYTIC = SUPPORTED_INFERENCE
XI_DECOMPOSE_CAUSAL = HYPOTHESIS
XI_REFRAME = NOT_SUPPORTED
XI_RELATION_EDIT = HYPOTHESIS
XI_CONSTRAINT_EDIT = HYPOTHESIS
XI_POSSIBILITY_REOPEN = NOT_SUPPORTED
```

## `C_psi` y `R_MOC`

En el grafo local importado, `C_psi` es una **relación elegible** bajo objeto, límite y criterio, y puede habilitar recomposición o salida. `R_MOC` se utiliza aquí como nombre de una configuración o conjunto relacional MOC declarado. Por tanto:

```text
C_psi != R_MOC
```

Posibles relaciones futuras —miembro, selección, proyección, salida o testigo— deben especificarse y probarse; no se asume ninguna. Tampoco:

```text
C_psi != R_geo
C_psi != concordancia_global
C_psi != permiso_de_transformacion
```

## Endogeneidad

Una reorganización sólo sería endógena respecto de una frontera `B` si el cambio se produce por variables y transiciones internas a `B`, sin que una intervención externa no registrada sea la causa suficiente. Deben distinguirse:

- `ENDOGENOUS_CAUSE`: mecanismo interno auditado;
- `ENDOGENOUS_ACCESS`: el sistema accede a variables internas;
- `ENDOGENOUS_REPORT`: el sistema describe el cambio;
- `EXTERNAL_TRIGGER`: entrada externa inicia una ruta interna;
- `EXTERNAL_OVERRIDE`: una fuente externa sustituye la transición.

Reporte o acceso no demuestran causalidad endógena. Un trigger externo puede coexistir con reorganización interna; una modificación externa oculta no debe atribuirse a Xi.

## Pruebas y falsadores futuros

1. **Ablación de Xi generativo:** si retirar el supuesto operador no cambia candidatos ni transiciones, su papel causal no está sustentado.
2. **Baseline evaluador:** comparar `Xi_reorg` con búsqueda/edición relacional genérica de igual capacidad.
3. **Intervención controlada:** modificar relación y restricción por separado; comprobar firmas distintas.
4. **Control de contenido:** cambio de contenido con patrón relacional estable debe resultar `redundante`.
5. **Control de conflicto:** restricciones incompatibles sin nueva estabilidad deben resultar `limitado`, no reorganización.
6. **Control de unidad:** pérdida de unidad comparable debe producir `no_comparable`.
7. **Control de fuente:** una edición externa oculta debe etiquetarse externa, no endógena.
8. **Control C/R:** sustituir una relación elegible `C_psi` no debe reemplazar automáticamente toda `R_MOC`.

## Dictamen de fase 1

```text
RELATIONAL_REORGANIZATION_AS_LOCAL_CLASSIFICATION = DOCUMENTED
XI_EVAL_AS_LOCAL_COMPARATOR = DOCUMENTED
XI_AS_ENDOGENOUS_TRANSFORMER = HYPOTHESIS
XI_GENERAL_OPERATIONAL_STATUS = NOT_SUPPORTED
C_PSI_EQUALS_R_MOC = FALSIFIED_BY_BASELINE
HXI_001_REACTIVATED = NO
CANONIZATION = NO
```
