# MOC-PSI-GEO-BRIDGE-001 — Puente 4-simplex y 24-cell

Estatus: puente documental aceptado entre geometría del Lab y autoridad
semántica externa de Psicología Concordante.

Fecha: 2026-09-12.

Expediente: `MOC-001`.

Decisión asociada: `D-2026-09-12-001`.

## Propósito

Relacionar los portadores geométricos verificados en Concordante Lab con su
lectura MOC/PSI sin trasladar la autoridad semántica al repositorio equivocado.

```text
LAB = geometría, código, resultados y pruebas
PSI = definiciones y estatus semánticos
BRIDGE = correspondencias tipadas y referencias exactas
```

## Fuentes congeladas

### Geometría del Lab

```text
SOURCE_COMMIT_INTERSTITIAL_MULTILEVEL=679e898b66b28e4f72d1f7bd38bc5469e940ad7a
SOURCE_COMMIT_R4_4SIMPLEX_24CELL=d65aab858df6bd0cc11609ec24a09b40eb8fec12
PREPARED_LAB_HEAD=8b7ad0e02ca231a0f35ddd2ccff7c4d2d18ef2db
```

### Semántica de Psicología Concordante

```text
REPOSITORY=https://github.com/iPPxp/psicologia-concordante.git
COMMIT=f068faf9dca98408b1a3b93b43f97401f8768795
TREE=e47e28e752ab6ad00f2fa97b6e92a81754547d0b
PSI_CANON_003=cf223249204c3aae24904d242dbe8862946e898f
PSI_CANON_004=6ece278c588ed188ddfb8e89a3d6805fab26bf92
PSI_D4_LOCAL_CARRIER=053e41ae7d041b8b33ef3148fb1aa748afec62b8
PSI_D4_VERIFIER=e571f7331b9f8b76e49acaf256bc2669cc85e81a
```

`PSI-CANON-004` es la autoridad semántica del 4-simplex. El documento
`PSI-D4-LOCAL-CARRIER-001` es investigación, no Canon.

## Correspondencia 4-simplex

| Geometría verificada | Lectura semántica gobernante en PSI |
| --- | --- |
| cinco vértices de `Delta^4` | cinco posiciones tipadas de `Pi5_psi` |
| 1-esqueleto `K5` | diez posiciones relacionales posibles |
| complejo completo | portador `Delta^4_psi` |
| subestructura activa y tipada | organización presente `O_psi,t` |
| interior/4-bola intersticial y su frontera hiperesférica | representación disponible de `g_t` |
| referencia del centro | `G_psi := core := núcleo := centro` |

El vector `(5,10,10,5,1)` y el 1-esqueleto `K5` son consecuencias del
portador aprobado en PSI. El significado psicológico individual de caras y
facetas permanece investigación.

En la realización regular, el radio intersticial es:

\[
\frac rR=\sqrt{\frac85}-1\approx0.2649110641.
\]

Las cinco 4-bolas anfitrionas y la 4-bola central —cada una con frontera
hiperesférica— producen el grafo completo `K6`, con 15 aristas. **Este `K6`
completo no es el ciclo `C6`**, que tiene seis
aristas y conserva su propio estatus de investigación HEART.

## Correspondencia 24-cell

El Lab verifica para la shell `D4`:

```text
VERTICES=24
CONTACT_EDGES=96
DEGREE=8
ANTIPODAL_PAIRS=12
OCTAHEDRAL_CELLS=24
```

La lectura PSI candidata la estudia como carta local de movimientos o ramas
contrafactuales alrededor del presente. Esta lectura permanece en
investigación; los 24 vértices no se convierten en 24 componentes nuevos del
Pentácoro.

En cada celda octaédrica pueden coexistir, como tipos distintos:

- dos caras triangulares opuestas como slots candidatos para `C3_H` y `C3_A`;
- un cinturón de seis contactos cruzados candidato para `C6`;
- tres pares no-contacto como matching candidato de `Theta_psi`.

La celda no selecciona por sí sola las etiquetas, la biyección ni su estabilidad
semántica.

## Frontera `A4`–`D4`

El sistema natural de diferencias orientadas del 4-simplex es `A4`, con 20
raíces. El 24-cell usa `D4`, con 24 raíces. Comparten rango cuatro, pero:

```text
20 != 24
A4_ROOT_SET_BIJECTION_D4_ROOT_SET=NO
CANONICAL_A4_D4_MAP=OPEN
```

No existe una biyección entre sus conjuntos de raíces. Un puente entre ambos
requiere un dato adicional; `Theta_psi`, Mente/coder y el contexto presente son
candidatos explícitos, no una consecuencia automática de compartir dimensión.

## Intersticio entre dos

La suite del Lab contiene la prueba
`test_tiny_positive_center_between_two_has_twice_its_radius_as_gap`. Para dos
anfitrionas colineales, una burbuja central positiva de radio `epsilon` cabe con
una separación adicional total `2*epsilon`; al tomar `epsilon -> 0+` se obtiene
el límite degenerado. La intuición de una burbuja diminuta entre dos ya forma
parte del contrato matemático y computacional.

## Preguntas que permanecen abiertas

- `RAT`: terna Relaciones–Accesibilidad–Trayectoria;
- `RLF`: terna Referencia–Lectura–Feedback;
- lugar exacto de Higher Mind respecto de la frontera, rama y `Link_C`;
- factorización entre Personalidad, Mente/coder y `Theta_psi`;
- mapa parcial, muchos-a-muchos o contextual entre `A4` y `D4`;
- significado de los cuatro ejes y de sus signos;
- selección y estabilidad de `C3_H`, `C3_A`, `C6` y sus seis biyecciones;
- dinámica global de ramificación, colapso, feedback y recentrado.

## Resultado del puente

```text
LAB_4D_GEOMETRY_AVAILABLE=YES
PSI_4SIMPLEX_SEMANTIC_AUTHORITY=PSI_CANON_004
PSI_24CELL_STATUS=RESEARCH
K6_COMPLETE_EQUALS_C6_CYCLE=NO
A4_D4_CANONICAL_BIJECTION=NO
RAT_RLF_HIGHER_MIND_PERSONALITY_STATUS=OPEN_RESEARCH
PSI_PROJECT_REOPENED_INSIDE_LAB=NO
```
