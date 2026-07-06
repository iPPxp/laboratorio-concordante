# R001_TABLE_CHECK_REPORT

report_id: R001-TABLE-CHECK-20260706-134840
expediente: R001-001
algoritmo: R001-TABLE-CHECK-001
relacion_formal_ao: R001-TB-001
resultado: ok
recomendacion: aprobar_lectura
transformacion_permitida: false

## Resumen

- checks: 20
- passed: 20
- failed: 0

## Relacion formal AO

- id: `R001-TB-001`
- puente: `AO-PPI-BRIDGE-001`
- alcance: `local_no_canonico`

## Guardas de alcance

- No canoniza `Xi`.
- No admite `H-Xi`.
- No cierra `P-200`.
- No autoriza transformaciones materiales.

## Resultados

- PASS `finite_mu_phi_boundary_omega_stable`: Omega remains stable when Phi changes from direct to reachability.
- PASS `finite_mu_phi_boundary_phi_changes`: Phi is declared differently before constructing xi.
- PASS `finite_mu_phi_boundary_xi_changes`: Effective transition relation changes traceably with Phi.
- PASS `finite_mu_phi_boundary_p000`: Both effective couplings preserve the four P-000 functions.
- PASS `finite_mu_xi_effective_added`: Reachability adds the derived path and nothing else.
- PASS `finite_mu_xi_effective_preserved`: Direct transitions remain preserved.
- PASS `finite_mu_xi_effective_removed`: No prior direct transition is removed.
- PASS `finite_p200_direct_edges`: P-200 equivalence depends on declared O_adm.
- PASS `finite_p200_reachability`: P-200 equivalence depends on declared O_adm.
- PASS `finite_p200_mixed`: P-200 equivalence depends on declared O_adm.
- PASS `finite_p200_oadm_changes_result`: Changing O_adm changes the equivalence result.
- PASS `finite_xi_to_layered`: mu_decouple requires scope, equivalence, and lower layered cost.
- PASS `compiler_xi_to_layered`: mu_decouple requires scope, equivalence, and lower layered cost.
- PASS `decouple_without_equivalence`: mu_decouple requires scope, equivalence, and lower layered cost.
- PASS `map_same_omega_not_same_model`: Same Omega can yield different effective couplings.
- PASS `map_mixed_oadm_non_equivalent`: Mixed route and school observations distinguish the models.
- PASS `map_domain_only_trivial`: Domain membership alone is only trivial equivalence.
- PASS `recipe_shared_good_local_equivalence`: Shared-good recipe observation is locally equivalent.
- PASS `recipe_unsafe_runny_non_equivalent`: Safety and texture diverge on unsafe-runny.
- PASS `recipe_safe_dry_non_equivalent`: Safety and texture diverge on safe-dry.

## Hallazgos

- Sin hallazgos bloqueantes.
