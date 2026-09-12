# Modelo formal mínimo

Artefacto de investigación; no canoniza MOC ni activa iPP. Guardas: \(Act_\psi\neq conducta\), \(Act_\psi\neq ACT_\psi\), \(G_\psi\neq\Phi_\psi\neq\Xi_\psi\).

## Estado

\[
X_t=(\Pi5_t,D_t,R_t,K_t,\mathcal P_t,Q_t),\quad
\mathcal P_t=(\mathcal A_t,T_t),
\]

con componentes tipados \(\Pi5=(P,Eaf,Act,V,S)\), distinciones \(D\), relaciones \(R\), restricciones \(K\), posibilidades y transitabilidad \(\mathcal P\), y evidencia/incertidumbre/provenance \(Q\). La separación es de auditoría; no prueba independencia ni primitividad.

\[
\mathcal A_t=\Gamma(\Pi5_t,D_t,R_t,K_t,S_t),\quad T_t:\mathcal A_t\to\mathcal T.
\]

Una reorganización candidata es una edición activa trazable

\[
R_M:X_t\mapsto X_{t+1}
\]

que modifica al menos uno de \(D,R,K\) o una entrada estructural de \(\Gamma\), y cuya intervención causa un cambio justificable en estructura o campo de posibilidades. Cambio de \(\Pi5\) solo no basta.

## Operaciones no equivalentes

- `SELECTION`: elige \(a\in\mathcal A_t\); no cambia campo.
- `FILTERING`: restringe por predicado fijo \(\mathcal A'_t\subseteq\mathcal A_t\).
- `GENERATION`: añade candidatos por búsqueda sin editar estructura.
- `REPLANNING`: cambia secuencia/plan sobre modelo vigente; puede generar opciones.
- `STRUCTURE_EDITING`: edita \(D,R,K,\Gamma\), genéricamente.
- `MOC_REORGANIZATION_CANDIDATE`: structure editing tipado MOC con traza causal y semántica preservada.

Una opción nueva no identifica su mecanismo. Igual outcome con diferente traza requiere prueba estructural; diferente output con \(D,R,K\) iguales es `SELECTION_CHANGE`, no reorganización.

## Local/global

Sea soporte de edición \(supp(\Delta)=\{u:X_t(u)\neq X_{t+1}(u)\}\). `LOCAL` significa soporte acotado al subgrafo declarado. `GLOBAL` exige efecto reproducible en múltiples regiones/relaciones o en reglas de \(\Gamma\); no se fija umbral canónico. Debe pre-registrarse alcance y falsador.

## Causalidad

Para edición \(e\), la contribución causal al campo se prueba comparando

\[
\mathcal P(do(e))\quad vs\quad\mathcal P(do(no\ e))
\]

con contexto, presupuesto, información y azar controlados. Una explicación o diff correlacionado no basta. `C_psi` selecciona intervenir/pausar/observar/etc.; no es \(R_M\). `Xi` como stop está documentado en el baseline del encargo; descomponer/reencuadrar/editar relación o constraint permanecen hipótesis hasta autoridad adicional.

## Dictamen inicial

```text
REORGANIZATION_FORMALIZATION = PARTIALLY_SUPPORTED
MOC_ALGORITHMIC_UNIQUENESS = INSUFFICIENT_EVIDENCE
REPRESENTATIONAL_INCREMENTAL_VALUE = INSUFFICIENT_EVIDENCE
```
