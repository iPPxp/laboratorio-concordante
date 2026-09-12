# Formalización provisional de concordancia y doble loop

## Estatuto

Este documento es investigación, no canon MOC ni reactivación operativa de iPP. Mantiene:

\[
Act_\psi\neq\mathrm{conducta},\quad Act_\psi\neq ACT_\psi,
\quad G_\psi\neq\Phi_\psi\neq\Xi_\psi.
\]

`Phi_psi` evalúa concordancia; `Xi_psi` organiza/interrumpe automatismo; ninguno prueba conciencia o voluntad. `V_psi` es Dirección y no se reduce a recompensa.

## 1. Estado y transiciones

Sea

\[
C_t=(\Omega_t,\Pi5_t,V_t,M_t,E_t,Q_t,Mode_t),
\]

con \(\Pi5_t=(P_t,Eaf_t,Act_t,V_t,S_t)\), memoria \(M_t\), evidencia/provenance \(E_t\), incertidumbre \(Q_t\), y

\[
Mode_t\in\{AUTOMATIC\_LOOP,ACTIVE\_LOOP\}.
\]

La conducta o salida exterior \(B_t\) pertenece a otra capa y puede o no realizar una tendencia interna de respuesta `Act_t`.

Loop basal candidato:

\[
B:C_t\mapsto (\widehat C_{t+1},r_t,f_t),
\]

donde \(r_t\) es respuesta candidata y \(f_t\) feedback local. Loop activo:

\[
A:(C_t,r_t,f_t)\xrightarrow{\Xi,O,\Phi,Options,Choice,Adjustment}C_{t+1}.
\]

La política de entrada \(\tau\) decide entre ambos:

\[
\tau(C_t,r_t,f_t)\in\{CONTINUE,PAUSE,ABORT,WAIT,REPLAN,ESCALATE,ASK,OBSERVE\}.
\]

Estas salidas no son sinónimas. `PAUSE` retiene reversiblemente; `ABORT` cancela; `WAIT` difiere hasta condición; `REPLAN` invalida plan; `ESCALATE` transfiere decisión sin aumentar autoridad; `ASK` solicita información; `OBSERVE` abre adquisición de datos; `CONTINUE` permite el basal.

## 2. Concordancia no escalar

Concordancia no es acuerdo, placer, ausencia de conflicto ni máximo de reward. Sea una evaluación estructurada:

\[
\Gamma(C_t,r)=\bigl(R_t,K_t,VCompat_t,X_t,U_t,EQual_t,Cost_t,Consequences_t\bigr),
\]

donde se registran compatibilidad relacional, restricciones, compatibilidad con valores activos, tensiones, incertidumbre, calidad de evidencia, coste y consecuencias. Cada componente conserva tipo, alcance, evidencia y confianza. Una regla de decisión parcial \(D_\Gamma\) puede producir:

```text
CONCORDANT | FRICTIONAL | DISCORDANT | UNDETERMINED
```

sin colapsar necesariamente \(\Gamma\) a un real. Si una implementación usa agregación escalar, debe publicar pesos, incomparabilidades, sensibilidad y pérdidas; el escalar es una política, no la definición de concordancia.

### 2.1 Orden parcial

Puede definirse \(a\succeq_\Gamma b\) sólo si `a` no empeora ningún criterio duro y mejora al menos uno relevante, dadas autoridad y contexto. Conflictos no comparables producen un frente de Pareto o `UNDETERMINED`, no una suma oculta.

### 2.2 Concordancia situada

\[
Conc(C,r\mid V,S,E,Q)
\]

es relación contextual, no propiedad intrínseca de \(r\). Cambiar valores activos, alcance o evidencia puede cambiar el dictamen sin contradicción, siempre que la transición esté trazada.

## 3. Escalas separadas

- `LOCAL_CONCORDANCE`: compatibilidad del paso actual con criterios activos.
- `INTERNAL_CONCORDANCE`: compatibilidad entre componentes internos declarados.
- `VALUE_CONCORDANCE`: compatibilidad con \(V_{active}(t)\).
- `CONTEXT_CONCORDANCE`: adecuación a condiciones \(S_t\).
- `EXTERNAL_CONSEQUENCE`: resultado exterior, no identidad con `Act_psi`.
- `TRAJECTORY_CONCORDANCE`: evaluación de una secuencia y sus efectos acumulados.
- `GLOBAL_CONCORDANCE`: vector de criterios a horizonte y alcance declarados; no omnisciencia.

Para trayectoria \(\gamma_{t:t+h}=(C_t,\ldots,C_{t+h})\):

\[
\Gamma^{traj}_{t,h}=F_h(\Gamma_t,\ldots,\Gamma_{t+h},\Delta V,\Delta constraints),
\]

donde \(F_h\) debe preservar violaciones duras y no permitir que promedios oculten daños puntuales. Puede ocurrir `LOCAL=CONCORDANT` y `TRAJECTORY=DISCORDANT`.

## 4. Valores y causalidad

Cada valor es

\[
v_i=(id,meaning,source,sourceType,authority,scope,priority,confidence,active,activationReason,time,constraints).
\]

Se distinguen \(V_{declared}\), \(V_{active}\), \(V_{inferred}\) y \(V_{revealed}\), además de restricciones duras, preferencias blandas y objetivos de usuario/sistema. Una discrepancia es un hecho funcional, no juicio moral.

Un valor tiene papel causal si, en una intervención controlada,

\[
P(Choice\mid do(V=v),W)\neq P(Choice\mid do(V=v'),W),
\]

manteniendo constantes contexto, opciones, evidencia, restricciones y azar \(W\), y si la cadena causal coincide con provenance. Sensibilidad textual o explicación retrospectiva no bastan.

El papel incremental del loop activo se estima mediante asignación controlada:

\[
ATE_A=\mathbb E[Y\mid do(Active=1)]-\mathbb E[Y\mid do(Active=0)],
\]

con \(Y\) vectorial: corrección, violaciones, concordancia, coste, latencia y confabulación. No se exige que todo componente mejore.

## 5. Observación, evaluación, elección y reorganización

`Observe(C_t)=D_t` registra sólo datos accesibles. Cada campo es `RAW_OBSERVATION`, `MEMORY`, `INFERENCE`, `ASSUMPTION` o `PREDICTION`. `Phi_C(D_t,V_t,S_t,E_t,Q_t)` produce assessment trazable. `Choice` conserva conjunto de opciones, alternativas descartadas y regla de decisión. `ALLOW/NO_FORCE/WAIT/DEFER/NO_INTERVENTION` son elecciones válidas.

Reorganización exige un cambio en relaciones, disponibilidad de opciones, prioridad o política, no meramente cualquier cambio de estado. Clasificación causal:

```text
AUTOMATIC_CHANGE | ACTIVE_REORGANIZATION | EXTERNAL_CHANGE | UNKNOWN_CAUSE
```

## 6. Recursión y meta-reorganización

Sea \(\pi_t\) la política de triggers/intervención. Primer orden modifica estado:

\[
C_t\xrightarrow{A_{\pi_t}}C_{t+1}.
\]

Segundo orden evalúa episodios y propone política:

\[
\pi_{t+1}=U(\pi_t,Log_{t-k:t},MetaAssessment_t).
\]

No se autoriza auto-modificación irrestricta. \(U\) opera sobre parámetros permitidos, versionados, reversibles y sujetos a validación fuera de muestra y aprobación definida. Para impedir regresión infinita se fija profundidad \(d_{max}\), presupuesto y condición de parada. Metaevaluar no implica una jerarquía ilimitada ni conciencia.

## 7. Geometría y proyecciones

Un estado unitario \(z_t\) puede ser un objeto estructurado; `ONE_OBJECT`, `ONE_VECTOR`, `ONE_STATE`, `ONE_POINT` y `ONE_PROJECTIVE_POINT` no son equivalentes. Las vistas

\[
\pi_i:z_t\to y_i
\]

son mapas generales hasta demostrar espacio vectorial, equivalencia por escala, incidencia y transformaciones proyectivas. Estados distintos pueden ser indistinguibles si comparten vistas; esto es no identificabilidad, no evidencia de dimensión geométrica superior.

El loop basal y activo pueden tener interfaces de observación distintas. Si el activo adquiere una vista adicional, su ventaja debe compararse con un control que reciba la misma información sin la narrativa del loop.

## 8. Dictámenes iniciales

```text
CONCORDANCE_AS_NONSCALAR_RELATION = FORMALIZED_NOT_VALIDATED
LOCAL_EQUALS_GLOBAL_CONCORDANCE = REJECTED
VALUE_CAUSAL_ROLE = INSUFFICIENT_EVIDENCE
ACTIVE_LOOP_INCREMENTAL_VALUE = INSUFFICIENT_EVIDENCE
META_REORGANIZATION = HYPOTHESIZED
HIGHER_DIMENSION_HYPOTHESIS = INSUFFICIENT_EVIDENCE
PROJECTIVE_HYPOTHESIS = INSUFFICIENT_EVIDENCE
PHENOMENAL_CONSCIOUSNESS = UNRESOLVED
```
