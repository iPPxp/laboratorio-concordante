# RAG EXTREMO POST-v2 — Exact-Trace Threshold/Extremal Program

Date: 2026-08-24
Target: `EXACT_TRACE_THRESHOLD_EXTREMAL_PACKAGE_V2_2026-08-23.zip`
Mode: adversarial / reject-if-gap.

## Executive verdict

**Do not keep the unconditional global `(tau,eta)` classification at `PROVED_AFTER_REPAIR` yet.**

No explicit mathematical counterexample was found. The determinant-combinatorics chain and the explicit single-rung constructions remain strong. However, the package still contains two proof-completeness gaps that matter to the `eta=2/3` branch:

1. **Phase VI bounded-port replacement does not track connectivity.** The four-state cut automaton tracks selected rail edges / parity, not the connectivity partition of partial path components. The statement that odd slabs carry one through-strand and even slabs carry two order-preserving strands is not a consequence of those four states alone. A connectivity-aware transfer automaton (or an explicit finite terminal/pairing table) is required.
2. **Three-link triangular reductions still omit the finite end-splice table.** Phase 5 itself says a publication proof should contain it. Therefore the universal `eta=2/3` claims for generic balanced triples and the nondivisible horizontal+balanced branch are structurally persuasive but not yet referee-complete.

A third, smaller gap remains in the exceptional threshold proofs `tau(U_1)=tau(U_{1,2})=3`: the package invokes a “finite local case split” / “local splice” without listing the cases. This is probably repairable and has strong computational support, but an extreme referee should request the explicit boundary-entry bridge lemma/table.

Thus the correct extreme-audit status is:

- global `tau` classification: **SURVIVES MATHEMATICALLY; MINOR FORMAL REPAIR REQUIRED** (exceptional bridge table);
- singleton/determinant theorems: **SURVIVE**;
- all single-rung `eta=1` branches: **SURVIVE**;
- terminal-constrained canonical strip theorem: **SURVIVES**;
- universal `eta(U_1)=2/3`: **DOWNGRADE TO CONDITIONAL / PROOF GAP** pending connectivity-aware bounded-port lemma;
- nondivisible horizontal+balanced `(2,2/3)`: **DOWNGRADE TO CONDITIONAL / PROOF GAP** pending finite end-splice/terminal lemma;
- every balanced triple has `eta=2/3`: **DOWNGRADE TO CONDITIONAL**;
- global `eta in {1,2/3}` and five-pair `(tau,eta)` classification: **DOWNGRADE TO CONDITIONAL**.

## Critical finding R1 — Phase VI loses connectivity information

Phase VI correctly proves support-edge sparsity and that any unbounded parallel interaction in `U_1` is triangular. It also correctly reduces four-link orientation words to at most one unbounded triangular core.

The gap occurs in the bounded-port replacement step. The four cut states `(a_i,b_i)` determine local selected rail edges and, after parity, the diagonal edge. They do **not** encode whether the partial selected subgraph already joins the frontier vertices, whether a replacement creates a closed cycle, or how boundary stubs are paired through the slab.

In odd parity, state `11` corresponds to all three cut edges being selected. Hence “odd slab = one through-strand” is not implied by parity/state alone. Connectivity/pairing must be added to the transfer state.

This is a proof gap, not a disproof. A connectivity-aware exhaustive slab computation performed during this RAG supports the intended bound: for every feasible boundary-stub set and induced pairing for symmetric triangular slabs of lengths 1 through 12, the optimal turn count never exceeded `2|V|/3 + 7/3`. The worst terminal types were simple top-to-bottom single-strand cases. This strongly suggests the missing lemma is true with an absolute terminal constant, but computation is not a universal proof.

### Required repair

Prove a `Bounded-Port Connectivity-Aware Strip Lemma` using one of:

- a finite transfer automaton whose state includes frontier degrees **and connectivity partition**;
- an explicit finite table of all feasible terminal-stub/pairing types with a period-3 pumping rule;
- a direct constructive path-cover classification.

The proof must show, for each feasible terminal type `sigma`,

`K_sigma(T_n) <= 2|V(T_n)|/3 + C_sigma`,

and then take the maximum over the finite state set.

## Critical finding R2 — Three-link eta=2/3 end-splices are not fully written

Phase 5 states that the three-link balanced reduction leaves a triangular interval strip up to bounded ends, but explicitly notes that a publication proof should include the finite end-splice table. Package v2 nevertheless promotes the associated global `eta=2/3` claims to `PROVED_AFTER_REPAIR`.

For an extreme referee, “no structural obstacle remains” is not a proof. The required table is finite and likely easy, but it must exist in the formal chain because the exact strip theorem is terminal-constrained, not free-endpoint.

Affected claims:

- horizontal+balanced nondivisible branch `(tau,eta)=(2,2/3)`;
- generic determinant-balanced triples with `eta=2/3`;
- therefore the global intensity classification.

## Formal finding R3 — Exceptional low-two-turn bridge is still a prose placeholder

The Phase-2 file says:

- for `U_1`, connector length `ell=1` and a primitive boundary bridge is “always available after the finite local case split”;
- for `U_{1,2}`, `ell<=2` and “remaining local configurations are finite” and permit a local splice.

This is enough to identify the correct mechanism, but not enough for a line-by-line journal proof. The package should add the actual finite cases / coordinates and the confined splice for each.

Affected claims:

- `tau(U_1)=3`;
- `tau(U_{1,2})=3`;
- formally, the global `tau` classification depends on them.

No counterexample was found; existing exact scans support the claims.

## Surviving strong chain

The following survived this extreme audit without a new substantive objection:

- Paper IIII qualitative unbounded-gap classification;
- universal one-turn obstruction;
- rectilinear low-turn rigidity and `tau(U_square)=4`;
- repaired top-gap, consecutive-block, full-initial-block and coset-normalization mechanisms (subject to ordinary line editing);
- bounded-to-linear `Gamma` transition once `tau` is fixed;
- explicit rectilinear, `U_12`, `U_23`, `U_{m,m+1}` and nonhorizontal-singleton single-rung extremal families;
- balanced-triple algebra `w=u+v`;
- Singleton Determinant Theorem;
- Nonhorizontal Singleton Bridge;
- height-divisible horizontal+balanced `eta=1` branch;
- Distinguished Singleton Theorem;
- paired-star parity collapse;
- `|U|>=5 => (tau,eta)=(2,1)`;
- terminal-constrained canonical triangular-strip exact theorem, provided it is stated with its terminal conditions.

## Package/integrity audit

The canonical ZIP is intact:

- SHA-256: `a134354f9fdbcc627004a497b52dc195f0945bd8a995d6ccd91e4d942a87014a`;
- ZIP CRC test: PASS;
- internal `sha256sum -c SHA256SUMS.txt`: PASS after extracting the ZIP;
- `RUN_QUICK_CHECKS.sh`: PASS;
- original Paper IIII Online Resource 1 reproduction: PASS before the combined all-check command reached the environment time limit.

The loose `/mnt/data/EXACT_TRACE_THRESHOLD_EXTREMAL_PACKAGE_V2_2026-08-23/` directory is **not** a faithful extraction of the ZIP in the current runtime: it lacks `code/`, `data/`, run scripts and inventory even though its manifest names them. Treat the ZIP as canonical and do not use the loose directory for integrity verification.

## Documentation inconsistency

`11_PHASE4_SINGLETON_AND_BALANCED_CLASSIFICATION.md` still writes the triangular-strip result as an unrestricted `K_H(T_n)=floor(2|V|/3)` statement, while the v2 audit correctly says the exact theorem is **terminal-constrained** and that free endpoints are a different problem. This file must be corrected in the next package revision.

## Computational adversarial controls

Existing package quick checks passed:

- rectilinear low-turn scan: 5,072 normalized traces, no low-turn violation;
- determinant singleton search: 91,390 four-sets + 658,008 five-sets, no counterexample;
- terminal-constrained strip regression: PASS;
- Phase-VI four-link scan: 7,898 normalized traces, 7,731 admissible; max observed `K_H - 2|S|/3 = 1/3` under its finite convention.

Additional connectivity-aware slab enumeration in this RAG exhaustively enumerated feasible spanning linear-forest/path-cover configurations for all boundary stub subsets and induced pairings for strip lengths `m=1,...,12`. Across all feasible terminal types, the maximum of the **optimal** turn excess over `2|V|/3` was at most `7/3`. This is evidence for the missing bounded-port lemma, not a proof.

## Extreme status table

| Claim family | Extreme RAG status |
|---|---|
| Paper IIII baseline | SURVIVES |
| One-turn obstruction | SURVIVES |
| Rectilinear rigidity / tau=4 | SURVIVES |
| `tau(U_1)=3`, `tau(U_12)=3` | NEEDS EXPLICIT FINITE BRIDGE TABLE |
| Global tau values `{infty,4,3,2}` | STRONGLY SUPPORTED; FORMAL DEPENDENCY REPAIR |
| Single-rung eta=1 results | SURVIVE |
| Singleton Determinant Theorem | SURVIVES |
| Distinguished Singleton Theorem | SURVIVES |
| `|U|>=5 => (2,1)` | SURVIVES |
| Terminal-constrained exact strip theorem | SURVIVES |
| Nondivisible horizontal+balanced eta=2/3 | CONDITIONAL: END-SPLICE TABLE NEEDED |
| `eta(U_1)=2/3` | CONDITIONAL: CONNECTIVITY-AWARE PORT LEMMA NEEDED |
| Every balanced triple eta=2/3 | CONDITIONAL |
| Global `eta in {1,2/3}` | NOT FROZEN |
| Five-pair `(tau,eta)` classification | NOT FROZEN |

## Recommended next action

Do **not** open a new speculative phase. Perform a targeted `v2.1 proof-completion repair` with exactly two mathematical deliverables and one editorial cleanup:

1. explicit exceptional boundary-entry bridge table for `U_1` and `U_{1,2}`;
2. connectivity-aware finite-state/terminal-pairing strip lemma, which also supplies the missing three-link end-splice table;
3. correct all files to say “terminal-constrained strip theorem”.

If those two lemmas are formally written and pass another RAG, then the global five-pair classification can legitimately return to `PROVED_AFTER_REPAIR`.
