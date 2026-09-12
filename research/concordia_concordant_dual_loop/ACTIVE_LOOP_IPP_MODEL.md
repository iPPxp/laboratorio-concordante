# Modelo provisional del bucle activo iPP

**Estatus:** hipótesis formal de investigación, no canon, no implementación activa y no reapertura de iPP/P-PI.

## Propósito y frontera

Este modelo pregunta si una intervención procedimental puede modular una dinámica experiencial sin confundir el procedimiento con los componentes MOC. No afirma eficacia humana, causalidad psicológica ni conciencia. Su objeto inmediato es una máquina de estados auditable sobre casos sintéticos.

## Separación de capas

Sea un estado MOC tipado:

\[
m_t=(P_t,Eaf_t,Act_t,V_t,S_t,r_t),
\]

donde `r_t` conserva relaciones, contexto, evidencia e incertidumbre. Ninguna coordenada debe asumirse numérica ni métrica sin operacionalización.

Se proponen tres capas distintas:

1. **Bucle basal:** evaluación/actualización continua declarada como hipótesis MOC, representada por `Phi_psi`; no es conciencia ni agente.
2. **Bucle activo iPP:** secuencia procedimental deliberada que modifica condiciones de actualización o selección de respuesta.
3. **Capa conductual:** salida exteriorizada situada; puede depender de `Act_psi`, pero no es `Act_psi`.

Forma mínima:

\[
m_t \xrightarrow{\Phi_\psi,\,contexto} \tilde m_t
\xrightarrow{u_t\in U_{iPP}} m_{t+1}
\xrightarrow{\kappa} conducta_{t+1}.
\]

`u_t` es una operación procedimental, no un “poder” causal demostrado; `kappa` es una realización situada no identificada con `Act_psi`.

## Operaciones candidatas

Cuando el mandato MOC independiente las autorice, el vocabulario procedimental puede conservar las cuatro operaciones deliberadas históricamente descritas como parar, evaluar, decidir concordantemente y soltar expectativas/ser expectante. En este repositorio no se encontraron como Canon activo; por ello aquí son etiquetas de propuesta:

| Operación candidata | Definición computable provisional | Veto semántico |
|---|---|---|
| `STOP` | suspender temporalmente una transición automática elegible | no implica inmovilidad, supresión ni eficacia experiencial |
| `EVALUATE` | ampliar o revisar la evidencia y alternativas del estado | no es `Phi_psi`, conciencia ni juicio verdadero |
| `DECIDE` | seleccionar una transición bajo criterios declarados | no equivale a `V_psi`, voluntad ni conducta ejecutada |
| `RELEASE_EXPECTATION` | reducir la rigidez de una predicción/condición de resultado | no es resignación ni garantía de resultado |

## Semántica de transición

Una transición activa candidata es:

\[
(m_t,q_t)\xrightarrow{u_t,e_t,c_t}(m_{t+1},q_{t+1}),
\]

donde `q` registra fuente, confianza, permisos, regla aplicada y deuda. La política de selección puede depender de `V_psi`, pero no debe reducirlo a una recompensa escalar:

\[
u_t\sim \pi(U\mid m_t,\mathcal C_t,\mathcal K_t),
\qquad V_\psi \not\equiv r\in\mathbb R.
\]

Una implementación puede usar señales escalares auxiliares, siempre etiquetadas `COMPUTATIONAL_PROXY`, con análisis de pérdida semántica y sin reclamar equivalencia.

## Qué significaría “dual”

El término sólo sobrevive si se demuestran dos dinámicas operacionalmente distinguibles:

- una actualización basal que ocurre sin invocar el procedimiento activo;
- una intervención activa que altera de forma reproducible una transición, su evidencia o su política.

No basta nombrar dos bucles. Debe existir una prueba de intervención/ablación y una predicción que un modelo de un solo bucle no explique con igual parsimonia.

## Experimentos sintéticos mínimos

1. **Ablación:** comparar trayectoria con y sin `u_t`, manteniendo estado y contexto.
2. **Intervención inversa:** aplicar y retirar una modificación procedimental; comprobar reversibilidad cuando corresponda.
3. **Control de renombrado:** sustituir etiquetas MOC/iPP por símbolos neutros; el resultado formal debe conservarse.
4. **Separación Act/conducta:** construir dos casos con igual `Act_psi` candidato y distinta salida situada, y viceversa.
5. **V no escalar:** comparar política multi-criterio con reward escalar; documentar qué ordenamientos se pierden.
6. **Phi/Xi:** intercambiar evaluador y organizador en un control negativo; si nada cambia, la distinción funcional no está operacionalizada.
7. **Baseline simple:** comparar contra una sola máquina de transición sin bucle dual.

## Falsadores

- Si toda trayectoria del modelo dual tiene una representación de un solo bucle igualmente simple y predictiva, `DUAL_LOOP_NECESSITY = NOT_SUPPORTED`.
- Si `STOP/EVALUATE/DECIDE/RELEASE_EXPECTATION` sólo renombran transiciones ya existentes, `IPP_ADDITIONAL_VALUE = NOT_SUPPORTED`.
- Si conducta determina por definición `Act_psi`, la implementación viola el baseline.
- Si una reward escalar sustituye `V_psi` sin pérdida sólo porque los datos fueron construidos así, no se ha demostrado equivalencia general.
- Si `Phi_psi` o `Xi_psi` carecen de firmas de entrada/salida distintas, su diferenciación computacional queda `INSUFFICIENT_EVIDENCE`.
- Si casos sintéticos favorables no generalizan a datos independientes, no hay evidencia empírica sobre experiencia.

## Salida provisional

```text
ACTIVE_LOOP_IPP_MODEL = HYPOTHESIZED
DUAL_LOOP_NECESSITY = INSUFFICIENT_EVIDENCE
IPP_ADDITIONAL_VALUE = INSUFFICIENT_EVIDENCE
HUMAN_EXPERIENTIAL_EFFECT = UNTESTED
CLINICAL_USE = PROHIBITED
IPP_REACTIVATION = NO
```
