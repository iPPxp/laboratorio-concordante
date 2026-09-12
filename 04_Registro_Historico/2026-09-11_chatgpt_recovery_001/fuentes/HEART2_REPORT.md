# Fase ❤️❤️ — factorización, redundancia y fibras de información alrededor de c

## Veredicto

**c -> C6 -> (C3+,C3-) -> c IS NOT JUST A VISUAL IDENTITY.**

Tiene una factorización informacional precisa, pero dependiente de la consulta.

Resultados centrales:

1. cada C3 embebido reconstruye c por sí solo;
2. cada C3 contiene 4 DOF continuos: `(c_x,c_y,phi,r)`;
3. el par alternante contiene sólo 5 DOF, no 8;
4. por tanto hay 3 DOF estructuralmente redundantes entre ambas ternas;
5. para recuperar rho, la segunda terna aporta esencialmente su radio;
6. para reconstruir la frontera, una sola terna deja un continuo 1D de triángulos compatibles;
7. las dos ternas colapsan ese continuo a **dos** fronteras equilateralmente compatibles;
8. una distinción binaria adicional de matching/chirality elige una;
9. en el punto autodual rho=2, esas dos fronteras coinciden y el bit deja de ser necesario;
10. en la corona A2 de radio k hay exactamente **2k C3 disjuntos**, cada uno con centroide c.

---

## 1. Corrección tipológica

No deben confundirse:

- `C6_link`: ciclo abstracto de seis vecinos de c;
- `D6(c)`: seis direcciones radiales;
- `P6_boundary`: seis puntos donde esas rayas contactan la frontera;
- `C3+`, `C3-`: ternas alternantes embebidas de esos contactos/direcciones.

La reconstrucción por centroide requiere geometría embebida. Un C3 abstracto como grafo no contiene coordenadas suficientes para producir c.

---

## 2. Factorización continua de cada C3

Una terna equilateral/rotacional embebida puede parametrizarse como:

**C3 = (c_x,c_y,phi,r).**

Son 4 DOF:

- 2 para c;
- 1 para fase/orientación modulo 120 grados;
- 1 para radio.

Para las dos ternas alternantes:

**C3+ = (c_x,c_y,phi,r_plus)**

**C3- = (c_x,c_y,phi+60deg,r_minus).**

Por tanto el par conjunto tiene:

**(c_x,c_y,phi,r_plus,r_minus)**

= **5 DOF**.

Si se sumaran ingenuamente las dos ternas habría 8 DOF.

La diferencia:

**8 - 5 = 3**

es redundancia estructural diferencial.

Esos tres DOF corresponden a:
- c_x compartido;
- c_y compartido;
- fase común, ya que la segunda fase está fijada por la relación de 60 grados.

Los radios son las contribuciones no redundantes.

---

## 3. Cada terna contiene c completo

Para cualquier órbita rotacional de orden 3:

**p + Rp + R^2p = 3c.**

Por tanto:

**centroid(C3+) = c**
y
**centroid(C3-) = c.**

Para la consulta:

**Q = "¿dónde está c?"**

las dos ternas son sustitutos redundantes: cualquiera basta.

La segunda terna aporta cero información necesaria adicional para esa consulta.

---

## 4. Pero una sola C3 no determina la frontera

Sea una C3 centrada en c, radio r y fase phi.

Para cualquier parámetro delta con:

**|delta| < 60deg**

puede construirse un triángulo equilátero centrado en c cuyas rectas de lado tienen normal:

**phi + delta + 120deg*j**

e inradio:

**h = r cos(delta).**

Su lado mide:

**L(delta) = 2 sqrt(3) r cos(delta).**

Los tres puntos de la C3 permanecen sobre sus lados.

Se muestrearon 23 valores de delta entre -55 y 55 grados y todos produjeron fronteras válidas.

Así:

**one C3 -> one-dimensional continuum of compatible outer triangles.**

Una C3 es suficiente para c, pero no para la frontera.

---

## 5. La segunda C3 colapsa el continuo, pero no a unicidad

Con las seis posiciones de contacto se enumeraron los 15 perfect matchings posibles de seis puntos.

Sólo sobreviven los dos matchings alternantes naturales del C6:

**M0=((0, 1), (2, 3), (4, 5))**

**M1=((5, 0), (1, 2), (3, 4)).**

Cada matching agrupa dos contactos sobre cada uno de tres lados y genera un triángulo equilátero compatible.

En la barrida 0°,...,60°:

- hubo dos fronteras geométricamente distintas en todos los ángulos salvo 30°;
- a 30° ambas construcciones coinciden.

Por tanto, genéricamente:

**C3+ + C3- -> 2 compatible boundaries.**

La fibra continua de una C3 se ha reducido a una fibra discreta de cardinalidad 2.

---

## 6. Las dos fronteras son conjugadas por reflexión

Sea gamma la fase de vértices de una frontera compatible y psi la fase del marco de seis rayos.

La otra frontera satisface:

**gamma_dagger = 2 psi - gamma (mod 120deg).**

Es exactamente la reflexión angular de gamma respecto del eje psi.

Error máximo de esta relación en la barrida:

**5.684e-14 grados.**

Las dos fronteras tienen:

- el mismo c;
- la misma escala;
- los mismos seis contactos;
- diferente orientación/chirality salvo en el punto autodual.

Esto produce una **pareja geométrica conjugada**, no dos polos introducidos como primitivas.

La dualidad aparece porque se perdió cuál de los dos perfect matchings del C6 corresponde a los lados reales.

---

## 7. El bit residual de frontera

Para reconstruir una frontera única a partir de los contactos hacen falta:

**(C3+, C3-, chi_boundary)**

donde:

**chi_boundary in {+,-}**

elige uno de los dos matchings/reflexiones.

Así, genéricamente:

**residual boundary information = 1 bit.**

Pero no es un bit universal del centro.

Es relativo a la consulta:

**"¿cuál de las dos fronteras compatibles era la original?"**

En el punto autodual de la barrida, 30°, las dos fronteras coinciden.

Allí:

**rho = 2**

y:

**residual boundary bit = 0.**

---

## 8. Relación con los radios y rho

Una C3 aporta su radio.

La segunda aporta el otro.

Por tanto:

**rho = max(r_plus,r_minus)/min(r_plus,r_minus)**

requiere ambas ternas.

Si r_s es el radio corto y r_l el largo:

**rho = r_l/r_s.**

En el dominio fundamental puede escribirse:

**rho = cos(delta) / cos(60deg-delta)**

con 0 <= delta <= 30deg.

Entonces:

**tan(delta) = (2-rho)/(sqrt(3) rho).**

Y la escala exterior se recupera como:

**h = r_s cos(delta)**

**L = 2 sqrt(3) h.**

Lo que queda indeterminado tras conocer rho es el signo/reflexión:

**boundary phase = phi_s ± delta.**

Ésa es precisamente la fibra binaria descrita arriba.

---

## 9. Jerarquía infinity -> 2 -> 1 para recuperar c

También aparece el mismo patrón dentro de una sola órbita C3.

Si sólo se conoce un punto perteneciente a una C3:
- hay un continuo de centros posibles.

Con dos puntos no ordenados y sabiendo que pertenecen a una misma órbita equilateral:
- existen exactamente dos centros espejo.

Con dos puntos y chirality/orientación del giro ±120:
- el centro es único.

Con los tres puntos:
- el centro es único por centroide.

Por tanto:

**1 point -> continuum**
**2 unordered points -> 2**
**3 points -> 1**

La dualidad binaria vuelve a aparecer como **residuo después de reducir una ambigüedad continua**, no como objeto inicial.

---

## 10. Generalización radial: cada C_(6k) contiene 2k copias C3 de c

En la retícula infinita A2, la corona:

**S_k(c) ~= C_(6k)**

se descompone bajo la rotación de 120 grados en:

**2k órbitas disjuntas C3.**

Para cada una:

**centroid(orbit) = c**

exactamente.

Verificado para k=1,...,100 con error entero exacto cero.

Así:

**C_(6k) = disjoint union of 2k C3-orbits**

y cada una reconstruye c.

Para k=1:
- 2 órbitas = las dos ternas originales.

Para k=2:
- 4 órbitas.

Para k=100:
- 200 reconstrucciones C3 disjuntas de la misma referencia c.

Esto da una ley exacta de redundancia radial:

**number of disjoint center-reconstructing triplets = 2k.**

---

## 11. Robustez de esa redundancia

Como las 2k órbitas son disjuntas, un adversario que quiera destruir **todas** las reconstrucciones completas por tripleta debe borrar al menos un punto de cada órbita.

Por tanto necesita al menos:

**2k point erasures.**

Con hasta:

**2k-1 erasures**

siempre queda al menos una C3 intacta y c sigue reconstruible por centroide.

Esto es combinatorio, no probabilístico.

También se incluyó un control condicional de borrado independiente con:

**P(at least one intact C3) = 1 - [1-(1-e)^3]^(2k).**

La ley probabilística depende del modelo de borrado; la cota adversarial 2k no.

---

## 12. La factorización depende de la pregunta

### Consulta: recuperar c

Una sola C3 basta.

**C3+ and C3- are redundant.**

### Consulta: recuperar rho

Una sola C3 no basta.

La segunda aporta el segundo radio.

### Consulta: recuperar escala exterior

Ambos radios permiten recuperar |delta| e inradio h.

### Consulta: recuperar frontera única

Ambos radios/contactos todavía dejan dos reflexiones.

Hace falta un bit de matching/chirality.

Por tanto no existe una sola cantidad llamada "la información de C3".

La suficiencia depende de la consulta, exactamente como en las fases de equivalencia operacional anteriores.

---

## 13. Estructura informacional resultante

Para el contact system embebido:

**C3+ = (c, phi, r_plus)**

**C3- = (c, phi+60deg, r_minus)**

De modo que:

**C3+ + C3- = (c, phi, r_plus, r_minus).**

Y después:

**(r_plus,r_minus) -> rho**

mientras:

**(c,phi,r_plus,r_minus) -> {boundary+, boundary-}.**

Finalmente:

**+ chi_boundary -> unique boundary.**

Así:

**c -> C6 -> C3+ + C3- -> c**

es una red con:
- redundancia para c;
- complementariedad para rho;
- una fibra binaria para reconstrucción de frontera.

---

## 14. Resultado conceptual fuerte

El patrón observado dos veces es:

**continuous ambiguity -> binary conjugate ambiguity -> unique reconstruction.**

No se introdujeron dos polos como primitiva.

La dualidad aparece sólo después de proporcionar suficiente información para reducir una familia continua a dos soluciones conjugadas.

Esto es un resultado geométrico; no se traduce todavía a semántica MOC.

---

## 15. Veredicto

C3_PLUS_RECONSTRUCTS_c=YES
C3_MINUS_RECONSTRUCTS_c=YES

SINGLE_C3_CONTINUOUS_DOF=4
C3_PAIR_CONTINUOUS_DOF=5
NAIVE_SUM_INDIVIDUAL_DOF=8
STRUCTURAL_REDUNDANCY_DOF=3

SECOND_C3_NEW_CONTINUOUS_INFORMATION=ONE_RADIUS
RHO_REQUIRES_BOTH_RADII=YES

ONE_C3_BOUNDARY_FIBER=ONE_DIMENSIONAL_CONTINUUM
TWO_C3_BOUNDARY_FIBER=2_GENERICALLY
TWO_C3_SELF_DUAL_FIBER_AT_RHO_2=1
UNIQUE_BOUNDARY_REQUIRES_MATCHING_BIT=YES_GENERICALLY

TWO_BOUNDARIES_ARE_REFLECTION_CONJUGATES=YES
BINARY_DUALITY_PRIMITIVE=NO
BINARY_DUALITY_EMERGES_AS_RESIDUAL_FIBER=YES

CENTER_FROM_ONE_POINT=NONIDENTIFIABLE
CENTER_FROM_TWO_UNORDERED_C3_POINTS=2_CANDIDATES
CENTER_FROM_THREE_C3_POINTS=UNIQUE

A2_SHELL_C6k_DECOMPOSES_INTO=2k_DISJOINT_C3_ORBITS
EVERY_C3_ORBIT_RECONSTRUCTS_c=YES
MIN_ADVERSARIAL_ERASURES_TO_DESTROY_ALL_C3_RECONSTRUCTIONS=2k

SEMANTIC_HEART_FUNCTION_TESTED=NO
