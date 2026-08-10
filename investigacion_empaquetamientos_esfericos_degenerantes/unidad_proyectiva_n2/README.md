# Unidad proyectiva, polaridad aparente y emergencia relacional — estudio n=2

Investigación mínima, reproducible y epistemológicamente delimitada del cociente antipodal

\[
S^2/(u\sim -u)\cong\mathbb{RP}^2.
\]

El estudio conserva como objeto principal un solo eje no orientado y sus dos representantes antipodales. No postula energías, fuerzas, conciencia, causalidad central, dimensión espacial adicional ni observadores cuánticos.

## Resultado resumido

```text
RESEARCH_SCOPE=n2_PRIMARY
PROJECTIVE_EQUIVALENCE_STATUS=RESULTADO_CLASICO_ESTABLECIDO
OBSERVER_DEPENDENCE_STATUS=SIGN_CHOICE_FORMALIZED_PHYSICAL_DEPENDENCE_NOT_DETERMINED
CENTRAL_SOURCE_STATUS=NO_DETERMINADO_WITHOUT_DYNAMICS
RELATIONAL_EMERGENCE_STATUS=NONADDITIVITY_DEMONSTRATED_FOR_ANTIPODALITY_RELATION
STRONG_EMERGENCE_STATUS=REFUTED_WITHIN_CURRENT_INFORMATION_COMPLETE_MODEL
NOVELTY_STATUS=KNOWN_WITH_DIFFERENT_TERMINOLOGY
EXPANSION_TO_n4=NO
EXPANSION_TO_n6=NO
EXPANSION_TO_n12=NO
```

## Estructura

- `INFORME_UNIDAD_PROYECTIVA_N2.md`: informe científico completo.
- `AUDITORIA_NOVEDAD.md`: antecedentes y dictamen de novedad.
- `MODELOS_Y_PRUEBAS.md`: modelos M0–M4 y pruebas discriminantes.
- `GLOSARIO.md`: separación de entidades y niveles.
- `BIBLIOGRAFIA.md`: fuentes primarias o académicas verificables.
- `src/projective_n2.py`: verificaciones algebraicas mínimas.
- `tests/test_projective_n2.py`: controles reproducibles.
- `data/results_n2.json`: resultado computado, regenerable.

## Reproducción

```powershell
$py = 'C:\Users\IximM\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
$env:PYTHONDONTWRITEBYTECODE = '1'
& $py .\scripts\run_verification.py
$env:PYTHONPATH = (Join-Path $PWD 'src')
& $py -B -m unittest discover -s tests -v
```

El cálculo verifica identidades finitas. No sustituye las demostraciones topológicas incluidas en el informe ni establece un modelo físico.
