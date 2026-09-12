# Baseline de autoridad MOC/iPP para el bucle dual

**Fecha de inspección:** 2026-08-15  
**Alcance:** lectura de autoridad; este archivo es investigación nueva, no Canon, documento oficial, Nivel C ni reapertura de iPP/P-PI.

## Jerarquía aplicada

La jerarquía vigente es: `01_Canon` → estado del proyecto → documentos oficiales → decisiones registradas → expedientes → automatización/reportes como evidencia operativa → registro histórico. Una fuente inferior no modifica una superior y una prueba local no promueve semántica.

| Ruta leída | Estado declarado | Uso permitido aquí |
|---|---|---|
| `01_Canon/M-000_Reglas_Fundamentales.md` | Canon | gobierna niveles, no promoción automática, trazabilidad y reapertura explícita |
| `01_Canon/M-001_Auditoria_Arquitectonica.md` | Canon | obliga a separar Canon, documento, expediente, prohibición y deuda |
| `CURRENT_STATE.md` | estado operativo resumido | orientación vigente; confirma cierres, transferencias y no autorizaciones |
| `05_Estado_Proyecto/ESTADO_ACTUAL.md` | estado operativo vigente | confirma `P-PI.0/P-PI.1` cerrados, `PSI-001` transferido y `MOC-001` sin ejecución empírica |
| `02_Documentos/03_Ontologia.md` | documento oficial consolidado | vocabulario operativo de modelo, estado, transición, evidencia, restricción y permiso |
| `03_Expedientes/P-PI_Decision_Cierre_Frente_Matematico_Acotado.md` | decisión de cierre, `D-2026-07-03-002` | prohíbe reabrir `P-PI.0/P-PI.1` sin decisión separada |
| `03_Expedientes/AO-001_Cierre_Local_AO_PPI_001.md` y decisión asociada | cierre local aceptado, `D-2026-07-06-024` | conserva `global_closure_authorized: false` y `p_pi_status: cerrado_como_frente` |
| `03_Expedientes/MOC-001_Semantica_Provisional.md` | propuesta semántica provisional no canónica | antecedente local no clínico; no es baseline experiencial MOC |
| `03_Expedientes/MOC-EXP-GRAPH-001_Grafo_Experiencia_Local.md` | evidencia estructural auxiliar de expediente | muestra notación local/importada; no canoniza `Phi_psi`, `Xi_psi` ni `Pi5_psi` |

`README.md` e `INDEX.md` confirman que el historial no es autoridad directa, los vision papers están inactivos y `PSI-001` no continúa dentro del Laboratorio. La presencia de un corpus de procedencia tampoco canoniza como verdaderas sus afirmaciones científicas o matemáticas ni activa operación.

## Baseline semántico obligatorio del encargo

Las siguientes guardas son restricciones explícitas del programa de investigación y se conservan literalmente:

```text
Act_psi != conducta
Act_psi != ACT_psi
G_psi != Phi_psi != Xi_psi
V_psi != reward_escalar
Phi_psi != conciencia
Xi_psi != voluntad
```

Baseline interpretativo permitido:

- `Act_psi`: modo de respuesta experiencial; puede incluir acción, no acción o pauta interna. La conducta exteriorizada pertenece a otra capa.
- `G_psi`: centroide o punto integrador local únicamente bajo una representación declarada.
- `Phi_psi`: evaluador; no sujeto, conciencia, TrueSelf ni autoridad externa.
- `Xi_psi`: operador de organización; no voluntad, intención fenomenal ni agencia por sí mismo.
- `V_psi`: dirección; una función de recompensa puede ser una señal computacional, pero no equivale semánticamente a `V_psi`.

**Estatus de este bloque:** baseline obligatorio del encargo, compatible con las prohibiciones locales inspeccionadas, pero no presentado como texto incorporado al Canon actual del Laboratorio. El repositorio inspeccionado incluso prohíbe promover la notación `psi` a vocabulario oficial por acumulación de casos.

## Clasificación de autoridad

| Afirmación | Clasificación |
|---|---|
| Las reglas M-000/M-001 gobiernan esta investigación | `CANON` |
| `P-PI.0/P-PI.1` permanecen cerrados | `CURRENT_OPERATIONAL_STATE` + decisión aceptada |
| `PSI-001` está transferido y sin continuidad interna | `CURRENT_OPERATIONAL_STATE` |
| Existe un “bucle dual” MOC/iPP operativo | `NOT_ESTABLISHED` |
| iPP puede modelarse como bucle activo | `RESEARCH_PROPOSAL` |
| `Phi_psi` es evaluación basal continua | `MOC_BASELINE_SUPPLIED_BY_RESEARCH_MANDATE`; requiere ruta MOC independiente para incorporación |
| El bucle activo produce efectos experienciales reales | `EMPIRICALLY_UNVALIDATED` |

## Vetos

Se veta cualquier lectura que:

1. reactive `P-PI.0`, `P-PI.1`, `PSI-001`, `HXI-001` o iPP por crear estos archivos;
2. presente el bucle dual como Canon, sistema activo, validación clínica o resultado empírico;
3. convierta `Act_psi` en conducta o `ACT_psi`;
4. reduzca `V_psi` a reward, utilidad o meta escalar;
5. convierta `Phi_psi` en conciencia, Self, TrueSelf, observador o voluntad;
6. convierta `Xi_psi` en voluntad, intención, agencia o autoridad semántica;
7. iguale `G_psi`, `Phi_psi` y `Xi_psi`;
8. use simulaciones, tests, grafos o trazas como validación psicológica;
9. trate evidencia histórica, material transferido o propuesta como autoridad vigente;
10. autorice modificación, intervención sobre personas, uso clínico o activación.

## Dictamen

```text
MOC_SEMANTIC_AUTHORITY = EXTERNAL_TO_THIS_RESEARCH_FOLDER
DUAL_LOOP_STATUS = RESEARCH_PROPOSAL
IPP_REACTIVATED = NO
P_PI_REACTIVATED = NO
EMPIRICAL_VALIDATION = NO
CANON_MODIFIED = NO
OPERATIONAL_ACTIVATION = NO
```
