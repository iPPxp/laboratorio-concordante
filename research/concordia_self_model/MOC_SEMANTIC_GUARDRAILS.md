# Guardas semánticas MOC

**Estado:** contrato de investigación provisional. No es canon MOC ni modifica autoridad semántica.

## Autoridad y regla de uso

MOC conserva autoridad sobre el significado experiencial. ConcordIA sólo formaliza, simula, contrasta y devuelve resultados con estado `RESEARCH_RESULT`, `HYPOTHESIS`, `COUNTEREXAMPLE`, `FORMAL_CONSEQUENCE` o `EMPIRICAL_RESULT`. Ningún resultado computacional canoniza una lectura MOC.

| Símbolo | Baseline preservado | Inferencia prohibida sin nueva autoridad |
|---|---|---|
| `P_psi` | Interpretación | tokens, embedding o creencia aislada |
| `Eaf_psi` | Afecto | emoción artificial o fenomenología |
| `Act_psi` | modo de respuesta experiencial | conducta exterior, salida o `ACT_psi` |
| `V_psi` | Dirección | recompensa, objetivo o utilidad sin más |
| `S_psi` | Situación | mundo externo completo o contexto computacional sin definición |
| `G_psi` | centroide/punto integrador local bajo representación declarada | `Phi_psi`, Self o TrueSelf |
| `Phi_psi` | evaluador | conciencia, Self o centroide |
| `Xi_psi` | operador de organización | voluntad, agencia o conciencia |

Invariantes semánticos obligatorios:

```text
Act_psi != CONDUCTA
Act_psi != ACT_psi
G_psi != Phi_psi != Xi_psi
FUNCTIONAL_ANALOGUE != HUMAN_EXPERIENCE
REPORTABILITY != PHENOMENOLOGY
```

`Act_psi` puede incluir acción, no acción o pauta expresiva interna. Una acción computacional pertenece a otra capa. Si se ensaya una proyección MOC de ConcordIA, el análogo de `Act_psi` debe ser un modo interno de respuesta operacionalizado independientemente de la salida.

## Protocolo para una proyección MOC

Toda propuesta `Pi_MOC(C_t)` debe declarar por componente: variable observable, dominio, método de medición, información perdida, contexto de validez, falsador y nivel de evidencia. Debe usar términos como `FUNCTIONAL_ANALOGUE` y no afirmar equivalencia con experiencia humana.

Veto del MOC Guardian cuando una propuesta:

- convierte `Eaf_psi` en afecto sentido porque existe valencia, prioridad, coste, error o urgencia;
- identifica `V_psi` con una función de recompensa sin prueba semántica;
- convierte `Act_psi` en conducta, salida o selección de herramienta;
- mezcla estado interno y condiciones externas en `S_psi`;
- reduce `P_psi` a tokens o embeddings;
- identifica `G_psi` con Self, `Phi_psi` con conciencia o `Xi_psi` con voluntad;
- infiere fenomenología de lenguaje en primera persona, autorreporte, acceso global o autorregulación.

## Dos polos de lenguaje

El polo humano puede decir “ConcordIA intenta entenderse”, pero el registro técnico debe expresar la operación comprobable, por ejemplo `Self_t = f(memory, capabilities, goals, uncertainty, provenance)`. La paráfrasis humana nunca eleva el estado ontológico de una afirmación.

## Registro mínimo de claims

Cada claim debe conservar `claim_id`, texto, fuente, `source_type`, fecha, agente, evidencia, confianza, estado, `supersedes` y `contradicts`. Estados permitidos: `OBSERVED`, `DECLARED`, `INFERRED`, `DERIVED`, `HYPOTHESIZED`, `REJECTED`, `UNRESOLVED`.

Las afirmaciones verbales del propio sistema son datos de reportabilidad; no son evidencia independiente de acceso introspectivo, autoría, identidad ni conciencia.
