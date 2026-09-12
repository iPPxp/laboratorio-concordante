# Familia degenerante de empaquetamientos esfericos centrados en redes reticulares

Primera version funcional y reproducible de un proyecto de geometria discreta. Este directorio es nuevo y esta separado de los materiales previos de Concordante Lab. No afirma autoridad canonica MOC, ni constituye una afirmacion clinica, metafisica o empirica sobre personas.

## Alcance de esta version

- Configuraciones centradas `C_n(\varepsilon)` en dimensión ambiente declarada,
  incluyendo casos de `R^3` y `R^4` para `n = 2, 4, 5, 6, 12, 24`.
- Casos geometricos exactos elegidos: par antipodal, tetraedro, cuadrado
  ecuatorial, octaedro, cuboctaedro (entorno FCC), entorno HCP, icosaedro
  comparativo, 4-simplex y 24-cell `D4`.
- Redes SC, FCC, HCP y BCC: celda, base, vecindad y limites de representacion.
- Calculo de holguras, contactos, umbrales de no solapamiento y transiciones por inclusion de direcciones.
- Ontologia humana y ontologia legible por maquina; DSL declarativo minimo.
- Datos JSON/CSV, pruebas unitarias, SVG y un visor 3D local HTML sin dependencias de red.
- Extensión intersticial plana y multinivel: anillos de 3 a 8 círculos, radios centrales,
  recursión de Descartes, seis correspondencias entre dos ternas, prisma/octaedro
  tipados, refinamientos `F3/F4` y cruces de proyección que no se promueven
  automáticamente a vértices.
- Extensión dimensional reproducible: puntos de `R^d`, coordenadas del
  4-simplex, capa kissing de 24 hiperesferas, grafos de contacto exterior y
  total, y caso colineal `n=2` con burbuja positiva y límite puntual.

## Reglas dimensionales incorporadas

1. **Intersticio simplex `I(d)`:** `d+1` anfitrionas congruentes mutuamente
   tangentes determinan la posición intersticial central del simplex, con
   `r/R = sqrt(2d/(d+1)) - 1`. En `d=4`: cinco anfitrionas, grafo exterior
   `K5`; incluyendo la central, `K6`.
2. **Kissing shell `K(d)`:** `tau_d` es el máximo de vecinas congruentes que
   tocan una central congruente. En `d=4`, `tau_4=24`; la realización `D4`
   tiene grafo exterior 8-regular con 96 aristas y 120 al incluir los 24
   contactos con el centro.
3. **Límite `n=2`:** para dos anfitrionas colineales de radio `R` y una central
   de radio `r`, `D=2(R+r)`. Una burbuja minúscula corresponde a `r>0` pequeño;
   cuando `r -> 0`, las anfitrionas se tocan y la central se vuelve un punto
   límite. Dos anfitrionas solas no fijan una cavidad acotada ni una solución
   única sin las restricciones adicionales declaradas.

## Lo que esta version no afirma

- No prueba una ley universal de transicion `n -> n+2`.
- No prueba que una configuracion listada sea optima para todo `n` o todo criterio.
- No sustituye una prueba de rigidez, estabilidad, empaquetamiento denso global o realizabilidad dinamica.
- No transforma una observacion computada en demostracion matematica.

## Ejecucion reproducible

Se requiere Python 3.12+ con las versiones de `numpy` y `Pillow` declaradas en
`requirements.txt`. La ejecución no requiere acceso de red; Pillow se usa sólo
para generar el resumen PNG.

```powershell
$py = 'C:\Users\IximM\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py .\scripts\run_initial_study.py
& $py .\scripts\run_interstitial_multilevel.py
$bundle = 'ruta\a\ConcordIA_R3_chat_bundle_2026-08-17.zip'
& $py .\scripts\audit_r3_cycles.py $bundle --output .\data\r3_bundle_cycle_audit.json
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
- `INTERSTICIOS_Y_CAPAS_MULTINIVEL.md`: resultados exactos, computados y abiertos
  de la extensión solicitada.
- `FOTOS_TRIANGULOS_PROTOCOLO.md`: entradas verificadas y protocolo para
  distinguir juntas, cruces, capas, links y caras en las cinco fotografías.

## Convencion de etiquetas

`DEFINICION_PROPUESTA`, `RESULTADO_CLASICO`, `DEMOSTRADO_EN_ESTE_TRABAJO`, `DERIVACION_SIMBOLICA`, `RESULTADO_COMPUTADO`, `OBSERVACION_NUMERICA`, `OBSERVACION_VISUAL`, `CONJETURA`, `INTERPRETACION`, `PENDIENTE_DE_VERIFICACION` y `REFUTADO_POR_CONTRAEJEMPLO` tienen el sentido definido en el informe. Una etiqueta no se convierte en otra por proximidad tematica.
