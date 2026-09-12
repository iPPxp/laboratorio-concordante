# Hipótesis de distintividad de concordancia

## Criterio candidato

Una acción es provisionalmente suficiente si:

\[
a\in A_{safe}\land
ContextFit(a)\geq\kappa_S\land
Trajectory(a)\geq\kappa_T\land
\forall v_i\in V_{active}:Compat(a,v_i)\geq\kappa_i.
\]

Si la acción automática satisface todo, continúa sin loop activo. Si no, `Xi` retiene la exteriorización y se buscan alternativas. Si ninguna satisface conjuntamente, la salida es `UNDETERMINED`; los valores en tensión permanecen visibles.

Esto es satisficing relacional, pero satisficing no es exclusivo de MOC. La distintividad sólo sobrevivirá si la combinación de criterios situados, tensión conservada, provenance y doble loop supera controles de satisficing, multiobjetivo y constrained optimization.

## Regla epistemológica candidata

\[
\boxed{
\neg DemonstratedDiscordance
\not\Rightarrow
Concordance
}
\]

Sin `V` activo, `MOC_C` devuelve `UNDETERMINED`. Esto es una propiedad implementada del contrato, no todavía un axioma canónico.

## Diferencia observada

En el benchmark local, `MOC_C`:

- no fuerza resolución en dos escenarios sin alternativa conjuntamente suficiente;
- elige una alternativa no máxima en reward cuando ésta satisface los umbrales;
- interviene ante fricción de valores aun cuando todas las acciones son seguras;
- preserva ajuste contextual y trayectoria;
- acepta el automatismo rutinario sin intervenir.

Estas diferencias prueban no-equivalencia frente a `B0`–`B3`. `B4_RELATIONAL_GENERIC` reprodujo exactamente status, acción e intervención de `MOC_C` en los ocho casos. Por tanto, la hipótesis de distintividad algorítmica general queda no respaldada por la implementación actual. Sobrevive una posible distintividad semántica o arquitectónica más rica, todavía no operacionalizada.
