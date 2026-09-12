# Modelo candidato MOC_R

## Estatuto

`MOC_R` es una hipótesis computacional de laboratorio. No es canon, operación
vigente, validación psicológica ni capacidad atribuida a Xi.

Se preserva:

```text
Pi5_psi = {P_psi, Eaf_psi, Act_psi, V_psi, S_psi}
Act_psi != CONDUCTA
Act_psi != ACT_psi
G_psi != Phi_psi != Xi_psi
C_psi != R_MOC
```

## Contrato

Sea `X=(Pi5,D,R,K,A,Q)`, con `A=Gamma(Pi5,D,R,K,S)`. Un script `e_1...e_n`
contiene ediciones atómicas `ADD/REMOVE/UPSERT` sobre `D`, `R` o `K`. La
implementación candidata:

1. exige exactamente los tipos `P,EAF,ACT,V,S`;
2. valida incidencias relacionales;
3. aplica cada edición de forma inmutable;
4. conserva un evento de provenance con digest before/after;
5. regenera `A` sólo después de cambiar entradas estructurales;
6. mantiene la elección final como operación separada.

La operación fuerte ensayada es por tanto:

\[
(D_t,R_t,K_t)\xrightarrow{e_1\cdots e_n}(D_{t+1},R_{t+1},K_{t+1})
\xrightarrow{\Gamma}\mathcal A_{t+1}.
\]

## Qué no demuestra

- El script se compila de un objetivo exógeno; no se aprende ni descubre.
- El test no demuestra endogeneidad psicológica.
- `D` neutral funciona en este prototipo como nodos/valores y no como ledger
  semántico completo de distinciones. Siete expectativas quedan no observables.
- `T` es un proxy de solapamiento/cambio de score, no una teoría validada de
  accesibilidad experiencial.
- La validación de tipos añade control e interpretabilidad, no una operación que
  B6 no pueda ejecutar.

## Falsador que sobrevivió

B6 recibe el mismo script y aplica las mismas ediciones sin vocabulario MOC. El
mapeo congelado elimina actor, IDs y nombres, pero conserva estados, incidencias,
operaciones, campos, decisiones, orden causal, provenance y coste. Fue exacto en
12/12 trazas, incluidos 6/6 tipos de transformación holdout.

Así, en este dominio:

```text
ALGORITHMIC_UNIQUENESS = NOT_SUPPORTED
MOC_R_AS_TYPED_AUDIT_ONTOLOGY = PLAUSIBLE_BUT_UNVALIDATED
```

