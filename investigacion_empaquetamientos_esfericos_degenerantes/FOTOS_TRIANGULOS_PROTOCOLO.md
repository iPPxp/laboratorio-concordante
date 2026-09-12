# Protocolo de digitalización de las cinco fotografías de triángulos

**Fecha:** 2026-09-12  
**Estatus:** diseño de experimento reproducible; anotación completa pendiente  
**Fuente preservada:** `ConcordIA_R3_chat_bundle_2026-08-17.zip`  
**SHA-256 del bundle:** `C40AB025189F39666D8421A205BE363D5FDE3534D4D488C5706A33C50CA84562`

## 1. Entradas

| Imagen | SHA-256 | Descripción piloto |
|---|---|---|
| `74398.jpg` | `EE1B9550373AAA08C7A2CF22246C8746C283B0B2BC172363B283F9C5FDD0D534` | malla física compatible visualmente con R3 |
| `74399.jpg` | `583D4C914E2A3CE497160040ABE1A5FF95C4AC9EED0A8B9AF93A4F60C6F4E58D` | carrier parecido a R3 con una capa triangular dorada |
| `image-1786985486350.jpg` | `ACCB303F62E410CBE9A526ADDF448A760C8B1AFCF65428F43428061ED3CD7403` | marcos triangulares proyectados o solapados |
| `image-1786985573717.jpg` | `1144C72882ED55BEAE47427E5885F448DB23A3B99039671426494910C22235ED` | triángulo exterior con hub de tres radios |
| `image-1786986209100.jpg` | `53B1DCA40FA7168C07C93BE4BD2BDE91B0FC453DBAAF572BDA3208FC7E647E57` | hub y seis direcciones aparentes con encuentros cercanos |

Las descripciones son inspección visual inicial y no sustituyen la anotación de
incidencias.

## 2. Unidad de anotación

Dos anotadores registrarán, por imagen:

- eje central de cada varilla o trazo;
- extremos visibles y extremos ocluidos;
- material/color/capa;
- ancho local de varilla `w`;
- cada encuentro como `J` (unión), `X` (cruce sin unión), `T` (contacto terminal),
  `A` (ambiguo) o `N` (near-miss);
- evidencia visual usada para la etiqueta.

No se resolverá silenciosamente una etiqueta `A`: cada combinación plausible
se conserva como una hipótesis topológica distinta.

## 3. Reconstrucción por hipótesis

Para cada asignación de encuentros:

1. construir el multigrafo bruto por capas;
2. conservar vértices de grado uno y varillas coincidentes;
3. registrar aparte cualquier extracción de núcleo;
4. fijar el orden rotacional antes de enumerar caras;
5. distinguir ciclos del 1-esqueleto, caras celulares, links y polígonos regulares;
6. calcular:

\[
(V,E,componentes,grados,\#C3,\#C4,\#C6,\beta_1,F3,F4,\chi).
\]

La comparación con R3, prisma, octaedro, `2C3`, `C6`, `K4` y `W5` se hará por
isomorfismo exacto e invariantes parciales, conservando todos los candidatos no
separados por los datos.

## 4. Geometría y robustez

- Para una hipótesis plana R3, ajustar la realización ideal mediante homografía
  o transformación afín y reportar el error de transferencia simétrico dividido
  por `w`.
- Para una hipótesis 3D de prisma u octaedro, una sola fotografía se trata como
  proyección; la recuperación métrica requiere calibración o vistas adicionales.
- Perturbar extremos en `±w` y repetir la fusión con umbrales `w`, `1.5w` y `2w`.
- Informar la frecuencia con la que sobrevive cada topología.

## 5. Hipótesis piloto por fotografía

| Imagen | Hipótesis de arranque | Distinción que debe decidirse |
|---|---|---|
| `74398` | R3 físico | si cada unión aparente es una junta real |
| `74399` | R3 + capa triangular | si las varillas coincidentes cambian multiplicidad o sólo color |
| `...5486350` | `2C3` o prisma proyectado | cuáles cruces son vértices y cuáles oclusiones |
| `...5573717` | subdivisión plana `K4` o tetraedro proyectado | dimensión y orden de profundidad |
| `...6209100` | estrella `K1,6` o tres ejes | existencia de enlaces perimetrales necesaria para hablar de `C6` |

## 6. Criterio de salida

El experimento termina con un conjunto de topologías compatibles por foto, no
con una figura elegida por parecido. Una clasificación única sólo se registra
si todas las asignaciones de cruces y perturbaciones admisibles conservan el
mismo tipo.
