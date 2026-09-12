# Fuentes metodológicas primarias

Estas fuentes justifican controles experimentales generales; no validan MOC.

1. Locatello, F. et al. (2019), [*Challenging Common Assumptions in the
   Unsupervised Learning of Disentangled Representations*](https://proceedings.mlr.press/v97/locatello19a.html),
   ICML/PMLR. Falsador: la descomposición no supervisada no es identificable sin
   sesgos inductivos y supervisión; el disentanglement tampoco garantiza por sí
   solo menor complejidad de muestra.
2. Koh, P. W. et al. (2020), [*Concept Bottleneck Models*](https://proceedings.mlr.press/v119/koh20a.html),
   ICML/PMLR. Aporta el comparador M-CBM y la posibilidad de intervenir conceptos;
   obliga a contabilizar anotaciones conceptuales y comparar desempeño.
3. Schölkopf, B. et al. (2021), [*Towards Causal Representation
   Learning*](https://arxiv.org/abs/2102.11107). Sitúa el problema de descubrir
   variables causales de alto nivel desde observaciones de bajo nivel; no permite
   asumir que las variables MOC sean causales.
4. Locatello, F. et al. (2020), [*Weakly-Supervised Disentanglement Without
   Compromises*](https://proceedings.mlr.press/v119/locatello20a.html), ICML/PMLR.
   Motiva contrafactuales/pares con cambios controlados y el reporte explícito de
   supervisión débil.
5. Kamath, P. et al. (2021), [*Does Invariant Risk Minimization Capture
   Invariance?*](https://proceedings.mlr.press/v130/kamath21a), AISTATS/PMLR.
   Advierte que una pérdida denominada “invariante” no garantiza recuperar las
   invariancias naturales; por ello la transferencia requiere holdouts reales y
   falsadores específicos.

