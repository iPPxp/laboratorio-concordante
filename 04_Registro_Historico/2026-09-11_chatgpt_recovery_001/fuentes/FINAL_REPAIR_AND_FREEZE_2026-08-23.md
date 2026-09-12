# Final Repair and Freeze Decision

Date: 23 August 2026

## 1. Repair objective

The final referee pass identified three items that prevented a clean freeze of the Phase-1/2/3 foundation:

1. the exceptional lower bounds for `U_1` and `U_{12}` still referred to an unlisted finite local case split;
2. the global `Gamma` theorem skipped the bounded-gap/`Theta(p)` step needed to convert an explicit parameter family into a lower bound for every large `N`;
3. the statement `sup_U tau_H(U)=4` needed its domain restricted because one-direction alphabets have infinite threshold.

A minor Phase-1 wording overlap and a newly available size-four determinant theorem were repaired at the same time.

## 2. Exceptional thresholds closed

For

\[
U_1=\{h,v,d_1\},\qquad
U_{12}=\{h,v,d_1,d_2\},
\]

the final repair proves

\[
\boxed{K_{\rm free}(S;U)\le2\implies K_H(S;U)\le12|U|+3.}
\]

The proof has three exhaustive branches for a split three-link witness:

- all three supports pairwise nonparallel: bounded number of primitive inter-support edges;
- outer supports parallel but no direct rail edge: again bounded support transitions;
- outer supports parallel with a direct rail edge: determinant identity bounds the support separation and an explicit first-host bridge table gives a confined splice.

For `U_1`, the connector length is always `ell=1`. For `U_{12}`, `ell<=2`; after host geometry excludes horizontal outer rails, `ell=2` only occurs for outer rail `d_2` with middle class `v` or `d_1`. The possible visible intermediate vertex is handled explicitly by a `v,d_1` or `d_1,v` two-edge splice.

Hence

\[
\boxed{\tau_H(U_1)=3,\qquad\tau_H(U_{12})=3.}
\]

No unnamed local cases remain.

## 3. Global threshold theorem

With the exceptional rows closed, the generic/pencil dichotomy and exhaustive pencil split give

\[
\boxed{
\tau_H(U)=
\begin{cases}
\infty,&|U|=1,\\
2,&\text{determinant-generic branch},\\
4,&J=\varnothing,\\
3,&J=\{1\}\text{ or }J=\{1,2\},\\
2,&\text{all other pencils}.
\end{cases}}
\]

The correct maximal-finite-threshold statement is

\[
\boxed{\sup_{\tau_H(U)<\infty}\tau_H(U)=4.}
\]

## 4. Extremal theorem repaired

The explicit families are now used with the quantitative facts

\[
|S_p|=\Theta_U(p),\qquad K_H(S_p)=\Omega_U(p),
\]

on parameter sets with bounded gaps. Choosing the largest admissible parameter whose trace has at most `N` vertices gives `p=Theta_U(N)`, so

\[
\boxed{
\Gamma_U(k,N)=
\begin{cases}
O_{U,k}(1),&k<\tau_H(U),\\
\Theta_U(N),&k\ge\tau_H(U).
\end{cases}}
\]

This closes C12 without inferring `Omega(N)` from `O(p)` alone.

## 5. Four-direction determinant theorem

A new rank-two Pluecker argument proves:

\[
\boxed{\text{every set of exactly four distinct direction classes has a singleton determinant class}.}
\]

If no singleton existed, each row of the six pairwise determinant magnitudes would have all three values equal, forcing all six magnitudes to a common `D`. The Pluecker identity

\[
p_{12}p_{34}-p_{13}p_{24}+p_{14}p_{23}=0
\]

would then reduce, after division by `D^2`, to a sum of three signs equal to zero, impossible.

The remaining open singleton problem therefore begins at `|U|>=5`.

## 6. Freeze-safe theorem core

The following claims are safe to freeze under the exact definitions in `01_DEFINITIONS_AND_NOTATION.md`:

`C00`–`C18` except that the superseded historical claims are not part of the core; specifically the proved chain includes C00, C01, C02, C03, C04, C05, C06, C07, C08, C09, C10, C11, C12, C13, C14, C15, C16, C17, C18, C20, and C23A.

Their proof dependencies are recorded in `THEOREM_DEPENDENCY_GRAPH.md`.

## 7. Not frozen as theorems

The following remain deliberately outside the theorem core:

- `C19`: `eta(U_1)=2/3` — `CONJECTURE`;
- `C21`: every determinant-balanced triple has intensity `2/3` — `CONJECTURE`;
- `C22`: singleton determinant class implies generic-host intensity `1` — `CONJECTURE`;
- `C23B`: every primitive direction set with `|U|>=5` has a singleton determinant class — `OPEN`;
- `C24`: bounded exhaustive singleton search — `COMPUTATION_ONLY`;
- `C25`, `C26`: historical superseded claims.

## 8. Reproducibility status

`RUN_ALL_CHECKS.sh` runs:

1. the recovered original Paper IIII reproducibility package;
2. post-paper finite family regression;
3. rectilinear low-turn scan;
4. exceptional clipping bridge-table certificate;
5. determinant singleton finite search.

These checks are controls. The threshold theorem and the new four-direction determinant theorem are proved independently of finite enumeration.

## 9. Final decision

\[
\boxed{\text{PHASES 1--3 PROVED CORE: SAFE TO FREEZE AFTER THIS REPAIR.}}
\]

The freeze applies only to claims marked `PROVED` or `PROVED_AFTER_REPAIR` in the corrected `CLAIMS_MATRIX.csv`. Conjectural and open claims retain their stated status.
