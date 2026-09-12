# F0.2 — Definiciones semánticas disponibles y deuda instrumental

```text
ARTIFACT_STATUS = BLOCKED_SEMANTIC_BASELINE
SEMANTIC_AUTHORITY = MOC
COMPUTATIONAL_AUTHORITY = VALIDATION_ONLY
INSTRUMENTAL_OPERATIONALIZATION_READY = NO
```

Este documento no propone definiciones nuevas. Resume la semántica nominal que la auditoría de autoridad pudo localizar y registra lo que falta para convertirla en reglas de observación narrativa. La evidencia completa y sus huellas están en `AUTHORITY_BASELINE.md`.

| Componente | Semántica nominal localizada | Dictamen instrumental |
|---|---|---|
| `P_psi` | pensamiento, definición, interpretación | `SEMANTIC_DEFINITION_INSUFFICIENT` |
| `Eaf_psi` | emoción-afecto situado | `SEMANTIC_DEFINITION_INSUFFICIENT` |
| `Act_psi` | acción/no acción o pauta expresiva interna/actual; no conducta exteriorizada | `SEMANTIC_DEFINITION_INSUFFICIENT` |
| `V_psi` | valores, dirección o criterio orientador; lo que importa sostener | `SEMANTIC_DEFINITION_INSUFFICIENT` |
| `S_psi` | situación encarnada o representación experiencial del entorno | `SEMANTIC_DEFINITION_INSUFFICIENT` |

## Distinciones autorizadas como vetos, no como definiciones positivas

```text
presence != change
contexto narrado != S
preferencia o deseo != V
palabra emocional != Eaf
Act != conducta observada
AMBIGUOUS != UNKNOWN
```

Estos vetos permiten rechazar errores, pero no bastan para decidir de forma reproducible `PRESENT`, `ABSENT`, `AMBIGUOUS`, `UNKNOWN`, `STABLE` o cambio.

## Cierre semántico requerido

Antes de G0, autoridad MOC debe fijar por componente:

1. condiciones observacionales positivas y negativas;
2. frontera con sus vecinos semánticos;
3. tratamiento de evidencia explícita, implícita, contrastiva y negativa;
4. atribución al sujeto frente a terceros, citas o detalles incidentales;
5. reglas independientes de presencia y cambio;
6. criterios para `ABSENT`, `AMBIGUOUS`, `UNKNOWN`, `STABLE` y `NOT_APPLICABLE`;
7. resolución de `P_psi/D_psi`, `Eaf_psi/E_af` y de la frontera `Act_psi` frente a `B_psi/K_psi` y `C_psi`.

Hasta entonces:

```text
SEMANTIC_DEFINITION_SUFFICIENT_COMPONENTS = 0/5
G0_MANUAL_CALIBRATION_AUTHORIZED = NO
```
