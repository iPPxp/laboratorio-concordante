# Familia degenerante de empaquetamientos esfericos centrados en redes reticulares

Primera version funcional y reproducible de un proyecto de geometria discreta. Este directorio es nuevo y esta separado de los materiales previos de Concordante Lab. No afirma autoridad canonica MOC, ni constituye una afirmacion clinica, metafisica o empirica sobre personas.

## Alcance de esta version

- Configuraciones centradas (C_n(\varepsilon)) para `n = 2, 4, 6, 12`.
- Casos geometricos exactos elegidos: par antipodal, tetraedro, cuadrado ecuatorial, octaedro, cuboctaedro (entorno FCC), entorno HCP e icosaedro comparativo.
- Redes SC, FCC, HCP y BCC: celda, base, vecindad y limites de representacion.
- Calculo de holguras, contactos, umbrales de no solapamiento y transiciones por inclusion de direcciones.
- Ontologia humana y ontologia legible por maquina; DSL declarativo minimo.
- Datos JSON/CSV, pruebas unitarias, SVG y un visor 3D local HTML sin dependencias de red.

## Lo que esta version no afirma

- No prueba una ley universal de transicion `n -> n+2`.
- No prueba que una configuracion listada sea optima para todo `n` o todo criterio.
- No sustituye una prueba de rigidez, estabilidad, empaquetamiento denso global o realizabilidad dinamica.
- No transforma una observacion computada en demostracion matematica.

## Ejecucion reproducible

Se requiere Python 3.12+ y `numpy` (no hay dependencias de red ni de visualizacion de terceros).

```powershell
$py = 'C:\Users\IximM\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py .\scripts\run_initial_study.py
$env:PYTHONPATH = (Join-Path $PWD 'src')
& $py -m unittest discover -s tests -v
```

Los artefactos se regeneran en `data/` y `visualizations/`. Se debe interpretar cada salida con la etiqueta epistemica incluida en los informes.

## Estructura

- `INFORME_MATEMATICO_INICIAL.md`: definiciones, derivaciones y resultados separados por estatus.
- `BIBLIOGRAFIA.md`: fuentes primarias o institucionales y necesidades de verificacion.
- `ONTOLOGIA.md` y `ONTOLOGIA.json`: vocabulario humano y contrato de tipos.
- `ESPECIFICACION_DSL.md`, `examples/initial_cases.json`: lenguaje declarativo inicial.
- `src/spherepack/`: modelo reproducible.
- `tests/`: controles de identidades geometricas y limites de transicion.

## Convencion de etiquetas

`DEFINICION_PROPUESTA`, `RESULTADO_CLASICO`, `DEMOSTRADO_EN_ESTE_TRABAJO`, `DERIVACION_SIMBOLICA`, `RESULTADO_COMPUTADO`, `OBSERVACION_NUMERICA`, `OBSERVACION_VISUAL`, `CONJETURA`, `INTERPRETACION`, `PENDIENTE_DE_VERIFICACION` y `REFUTADO_POR_CONTRAEJEMPLO` tienen el sentido definido en el informe. Una etiqueta no se convierte en otra por proximidad tematica.
