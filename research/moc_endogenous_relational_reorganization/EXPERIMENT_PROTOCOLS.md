# Protocolos y 27 predicciones falsables

Todos los estados son `HYPOTHESIZED`. Autores de fixture, oracle, política y evaluación deben separarse en ejecución futura; aquí no se implementa ninguno. Campos: ID, claim, constructo MOC, baseline, transformación, observable, traza, medición, desconfirmación y replicación.

| ID | CLAIM | MOC_CONSTRUCT | BASELINE | TRANSFORMATION | OBSERVABLE | STRUCTURAL_TRACE | MEASUREMENT | DISCONFIRMING_RESULT | REPLICATION_CRITERION | STATUS |
|---|---|---|---|---|---|---|---|---|---|---|
| P01 | Reencuadre P puede abrir posibilidad | P | B5/B6 | P_REFRAME | opción nueva | P→K/R→A | PE,CAA | B5/B6 igualan estructura/coste | 2 dominios, 3 semillas | HYPOTHESIZED |
| P02 | Cambio P no fuerza cambio relacional | P/R | control nulo | P_VALUE_EDIT | estados four-valued | P edit + R audit | matriz M | todo R marcado changed sin evidencia | 50 pares independientes | HYPOTHESIZED |
| P03 | Relación cambia campo con vértices fijos | R | vector-only/B6 | RELATION_REORGANIZATION | ΔP | R edit→Gamma | RC,PC,CAA | vector-only iguala o no cambia P | 3 relaciones tipadas | HYPOTHESIZED |
| P04 | Nueva distinción útil altera consultas | D | B6 | DISTINCTION_REFINEMENT | clasificación/opciones | D refine→R/K/A | DC,PE,TF | sólo renombra | holdout vocabulario | HYPOTHESIZED |
| P05 | Fusión puede mejorar parsimonia | D | add-only | DISTINCTION_MERGE | conflicto/coste | merge→simplify | DC,coste,error | empeora o es relabel | 2 familias | HYPOTHESIZED |
| P06 | Quitar constraint falso expande | K/S | B4/B5/B6 | FALSE_CONSTRAINT_REMOVAL | nuevas viables | evidence→K remove→A | KC,PE,CAA | expansión sin causalidad o B6 iguala | 30 casos ciegos | HYPOTHESIZED |
| P07 | Añadir límite real contrae correctamente | S/K | always-expand | REAL_LIMIT_ADD | opciones retiradas | observe S→K add→A | KC,PR,violaciones | mantiene inviables | 30 casos | HYPOTHESIZED |
| P08 | Más opciones no implica mejor reorganización | P-field | B5 | SEARCH_EXPANSION | calidad/viabilidad | search only | PE,TF,outcome | PE predice siempre éxito | 2 presupuestos | HYPOTHESIZED |
| P09 | Transitabilidad cambia sin nueva opción | Act/R | B6 | TRANSITABILITY_EDIT | T(a) | R/Act→T | TC,CAA | requiere PE o no cambia T | 3 opciones existentes | HYPOTHESIZED |
| P10 | Nueva acción puede ser selección | C_choose | B0 | SELECTION_ONLY | output distinto | A fixed→choice | DC/RC/KC=0 | estructura cambia | 50 pares | HYPOTHESIZED |
| P11 | Reorganización puede conservar acción | R_MOC | B6 | STRUCTURE_EDIT_SAME_ACTION | action igual | D/R/K edit→same choice | SRP,TF | no hay cambio estructural | 20 casos | HYPOTHESIZED |
| P12 | Act no equivale output | Act | filtro externo | OUTPUT_FILTER | output/Act | external edit | divergence | Act necesariamente cambia | 3 filtros | HYPOTHESIZED |
| P13 | Act puede cambiar sin output | Act/Xi | wait control | ACT_MODE_REORGANIZATION | Act/output nulo | Act edit→WAIT | state diff | sólo cambia al emitir | 3 modos | HYPOTHESIZED |
| P14 | V clarificado no siempre cambia campo | V | B6 | V_CLARIFICATION | PC/TC | V edit audit | four-valued SRP | se fuerza cambio siempre | 30 contexts | HYPOTHESIZED |
| P15 | S nuevo puede contraer o expandir | S/K | static-S | S_CONSTRAINT_DISCOVERY | PE/PR | S→K→A | PC,CAA | efecto unidireccional fijo | límites y recursos | HYPOTHESIZED |
| P16 | B5 puede igualar outcome sin estructura | R_MOC | B5 | GENERATIVE_REPLAN | action/options | search trace vs edit | outcome+TF | B5 preserva toda estructura | 2 domains | HYPOTHESIZED |
| P17 | B6 puede ser isomorfo a MOC_R | tipado MOC | B6 | matched edits | mapping | normalized traces | GIR | mapping falla por propiedad estable | holdout transformaciones | HYPOTHESIZED |
| P18 | Nombres MOC no añaden capacidad | semántica | renamed B6 | VOCABULARY_PERMUTE | desempeño | alpha-renaming | delta metrics | nombres solos mejoran holdout | 5 permutaciones | HYPOTHESIZED |
| P19 | Tipado MOC puede mejorar generalización | Pi5 typing | untyped B6 | TYPE_HOLDOUT | transform prediction | type→edit prior | HTG,TF | B6 iguala con presupuesto | 2 holdouts externos | HYPOTHESIZED |
| P20 | Tipado puede aportar sólo explicación | Pi5 typing | B6 | matched capability | outcome/trace | equivalent operations | GIR,TF | ni TF mejora | blinded auditors | HYPOTHESIZED |
| P21 | UNKNOWN evita falsa propagación | Q/R | binary diff | PARTIAL_OBSERVATION | calibration | missing→UNKNOWN | unknown accuracy | binary iguala sin falsos negativos | 3 missingness levels | HYPOTHESIZED |
| P22 | NA no equivale unchanged | R | naive matrix | OUT_OF_DOMAIN | denominadores | NA propagation | rate bias | no diferencia | 100 sparse graphs | HYPOTHESIZED |
| P23 | Edición de Gamma es distinguible de búsqueda | Gamma | B5 | GENERATOR_EDIT | distribution support | rule diff | TF,novelty holdout | búsqueda iguala con coste | equal compute | HYPOTHESIZED |
| P24 | Xi-stop no prueba Xi-organize | Xi | stop-only | PAUSE | structural diff | gate trace | SRP | stop siempre edita D/R/K | 30 events | HYPOTHESIZED |
| P25 | Choice no es reorganización | C | chooser | CHOOSE_REORGANIZE | downstream edit | choice→optional operator | CAA | choice solo reproduce edit | intervention ablation | HYPOTHESIZED |
| P26 | Holdout de transformación es más difícil | R_MOC | B6 | UNSEEN_TYPE | generalización | frozen models | HTG gap | case holdout predice igual | 2 rounds sealed | HYPOTHESIZED |
| P27 | Meta-threshold no es meta-reorganización | R2 | tuner | THRESHOLD_UPDATE | D/R/K(policy) | parameter-only | policy SRP | modifica distinciones/constraints del policy | 3 tuners | HYPOTHESIZED |

## Protocolos integradores

1. `E-INDEPENDENT-COMPONENT`: intervenir P/Eaf/Act/V/S, mantener lo demás, registrar DC/RC/KC/PC/TC y unknowns.
2. `E-RELATION-ONLY`: vértices aproximadamente constantes, editar una relación y comparar vector-only/B6/MOC_R.
3. `E-CONSTRAINT-POLARITY`: falsa restricción removida y límite real añadido.
4. `E-DISTINCTION`: refinar y fusionar; penalizar complejidad.
5. `E-OUTCOME-CROSSED`: acción cambia sin estructura y estructura cambia sin acción.
6. `E-B5-B6`: igualar información/cómputo; evaluar outcome y trazas normalizadas.
7. `E-ISOMORPHISM`: mapping congelado, evaluación ciega en holdout de transformación.

No ejecutar políticas u oracles en esta fase documental.
