# Fase ❤️❤️❤️ — cambio de coder, proyección y qué sobrevive

## Pregunta

No se supone que la realidad sea triangular.

Se prueba la hipótesis formal:

**una estructura latente X puede producir geometrías/resonancias diferentes bajo coders K distintos.**

La fase separa cuatro niveles:

1. propiedades del objeto fuente;
2. propiedades del coder;
3. propiedades conjuntas fuente+coder;
4. invariantes que sobreviven a una clase de cambios de coder.

No se prueba que el cerebro humano use un coder triangular.

---

## 1. Mismo objeto 3D, geometrías visibles distintas

### Tetraedro regular

Se usó el mismo tetraedro centrado con vértices:

`(1,1,1), (1,-1,-1), (-1,1,-1), (-1,-1,1)`.

Coder ortográfico A, dirección `(1,1,1)`:
- un vértice proyecta al centro;
- los otros tres forman el hull;
- hull visible: **triángulo equilátero**.

Coder ortográfico B, dirección `(1,0,0)`:
- los cuatro vértices proyectados forman:
- hull visible: **cuadrado**.

Por tanto:

**same 3D tetrahedron -> triangle OR square**

dependiendo del coder.

### Cubo

Mismo cubo centrado.

Coder dirección `(0,0,1)`:
- hull: **cuadrado**.

Coder dirección `(1,1,1)`:
- hull: **hexágono regular**.

Por tanto:

**same 3D cube -> square OR hexagon**

dependiendo del coder.

Esto prueba que el orden poligonal visible no pertenece exclusivamente al objeto 3D.

---

## 2. Pero el coder tampoco puede producir cualquier cosa

El cubo es centralmente simétrico:

**x in X => -x in X.**

Todo coder lineal K preserva:

**K(-x) = -K(x).**

Por tanto toda proyección lineal del cubo sigue siendo centralmente simétrica.

En 3000 proyecciones ortográficas aleatorias:
- fallos de simetría central: **0**;
- hull triangular observado: **0**.

Así, aunque el coder cambie la apariencia, existen restricciones heredadas de la fuente.

Resultado:

**OUTPUT = SOURCE x CODER, not CODER alone.**

---

## 3. c sí tiene un núcleo que sobrevive

Para cualquier conjunto finito X y coder afín:

**K(x)=Ax+b**

se cumple exactamente:

**K(centroid(X)) = centroid(K(X)).**

Se verificó en 2000 nubes aleatorias 3D y mapas afines 3D->2D.

Error numérico máximo:

**9.930e-16.**

Esto es además un teorema lineal, no sólo un resultado computacional.

Por tanto el centroide tiene una propiedad de **naturalidad entre coders afines**.

Esto distingue fuertemente:

- `c as barycentric/centroidal reference` — puede sobrevivir;
- `C6 around c` — puede cambiar;
- `C3+C3` — puede cambiar;
- resonancias concretas — pueden cambiar.

La hipótesis semántica `c = Heart` sigue sin probarse, pero matemáticamente el centro es más portable entre coders que su vecindad triangular.

---

## 4. Familia de coders regulares D_n

Se generalizó el coder triangular a un coder regular n-fold.

Para coder n:
- simetría D_n;
- marco radial de 2n rayos;
- dos órbitas alternantes C_n + C_n.

La razón de contactos análoga es:

**rho_n(alpha) = cos(theta-alpha)/cos(theta+alpha)**

donde:

**theta = pi/(2n)**

y:

**0 <= alpha <= theta.**

En el extremo:

**rho_n,max = sec(pi/n).**

Así el valor especial depende del coder.

Ejemplos:
- n=3: 2;
- n=4: sqrt(2);
- n=6: 2/sqrt(3);
- otros n producen otros números algebraicos.

El `2` triangular no es universal.

---

## 5. La aritmética de resonancia también cambia

Se tomó el punto medio del dominio:

**alpha = theta/2 = pi/(4n).**

Su razón es:

**rho_n* = cos(pi/(4n)) / cos(3pi/(4n)).**

Se calculó el polinomio mínimo exacto para n=3,...,12.

Grados algebraicos obtenidos:

{"3": 2, "4": 4, "5": 4, "6": 4, "7": 6, "8": 8, "9": 6, "10": 8, "11": 10, "12": 8}

Los grados NO son constantes entre coders.

Esto significa que la aritmética cuadrática/Pell encontrada en el coder triangular no puede elevarse sin prueba a ley independiente del coder.

En particular:

**PELL/sqrt(3) = triangular-coder arithmetic candidate, not cross-coder invariant.**

Otros coders inducen otros campos algebraicos y otros problemas diofánticos.

---

## 6. C6 y C3+C3 son una instancia de un patrón más general

Con coder regular n:

**2n rays = C_n^(+) disjoint-union C_n^(-).**

Entonces:
- triangular: `C6 -> C3 + C3`;
- square coder: `C8 -> C4 + C4`;
- pentagonal: `C10 -> C5 + C5`;
- hexagonal: `C12 -> C6 + C6`.

Así:

**C3+C3 is coder-specific**

pero la forma abstracta:

**two alternating n-fold orbits sharing a center**

sí generaliza dentro de esta familia de coders.

Eso es un posible invariante de la *clase de arquitectura*, no del número 3.

---

## 7. La secuencia infinito -> 2 -> 1 tampoco es universal

Se construyó un control abstracto:

**K_m(theta)=exp(i m theta)**

sobre el círculo latente S1.

Para observación genérica:
- m=2 produce fibra 2;
- m=3 produce fibra 3;
- ...
- m=12 produce fibra 12.

Añadir la rama exacta colapsa a 1.

Así pueden realizarse:

**continuum -> m -> 1**

para cualquier m ensayado 2,...,12.

Este control es deliberadamente construido; no prueba que esos coders existan en humanos.

Sí refuta la universalidad del `2`.

---

## 8. La ley más general que sobrevivió

Sea G_res el grupo residual de transformaciones que el coder todavía no distingue.

Para un estado x:

**fiber size = |G_res . x| = |G_res| / |Stab(x)|**

cuando la fibra coincide con la órbita residual.

Así:
- estabilizador trivial -> fibra máxima;
- simetría parcial -> fibra menor;
- punto fijo total -> fibra 1.

El `2` de ❤️❤️ corresponde al caso residual Z2.

En otro coder puede aparecer 3,4,5,... o incluso una fibra continua.

La multiplicidad no es una constante universal.

La estructura más general es:

**latent family -> quotient by unobserved symmetry -> residual orbit -> branch information -> unique state.**

---

## 9. Clasificación final de lo que tenemos

### Candidato cross-coder

**c as centroid/natural reference**
bajo coders afines.

### Fuente-invariante bajo coders lineales

Ejemplo:
**central symmetry** del cubo.

### Coder-relative

- número de rayos;
- C6 vs C8 vs C10 vs C12;
- C3+C3 vs C4+C4 vs ...;
- valores especiales de rho;
- polinomios mínimos;
- aritmética diofántica específica.

### Fuente + coder

- triángulo/cuadrado/hexágono visible;
- multiplicidades concretas;
- degeneraciones.

---

## 10. Consecuencia para la hipótesis del coder humano

La fase NO demuestra:

**HUMAN_CODER = TRIANGULAR.**

Sí demuestra que la arquitectura que hemos estudiado debe formularse condicionalmente:

**IF coder is triangular/A2-like, THEN C6, C3+C3, rho-family and associated arithmetic follow.**

No:

**Reality itself is C6/Pell.**

La prueba correcta de una hipótesis humana triangular necesitaría datos independientes de percepción/cognición/representación que predigan estas estructuras mejor que coders alternativos.

---

## 11. Nueva formulación de c

La fase favorece distinguir:

**c_triangle = geometric manifestation under triangular coder**

de un posible objeto abstracto:

**c_bar = coder-natural reference**

tal que para coders admisibles K:

**K(c_bar_X) = c_(K(X)).**

No se afirma que `c_bar = Heart`.

Pero esta naturalidad es una candidata mucho más fuerte a propiedad profunda que el hecho accidental de que su Link triangular sea C6.

---

## 12. Veredicto

SAME_3D_OBJECT_CAN_PROJECT_TO_DIFFERENT_2D_GEOMETRIES=YES

TETRAHEDRON_TRIANGLE_AND_SQUARE=YES
CUBE_SQUARE_AND_HEXAGON=YES

CODER_CAN_PRODUCE_ARBITRARY_OUTPUT_INDEPENDENT_OF_SOURCE=NO
SOURCE_CONSTRAINTS_SURVIVE_SOME_CODERS=YES
CENTRAL_SYMMETRY_PRESERVED_BY_LINEAR_CODER=YES

CENTROID_NATURALITY_UNDER_AFFINE_CODERS=YES

C6_CROSS_CODER_INVARIANT=NO
C3_PLUS_C3_CROSS_CODER_INVARIANT=NO
TRIANGULAR_RHO_VALUES_CROSS_CODER_INVARIANT=NO
PELL_SQRT3_CROSS_CODER_INVARIANT=NO

REGULAR_n_CODER_PATTERN=2n_RAYS_TO_Cn_PLUS_Cn
CODER_ORDER_CHANGES_RESONANCE_SIGNATURE=YES
ALGEBRAIC_DEGREE_CHANGES_WITH_CODER=YES

INFINITY_TO_2_TO_1_UNIVERSAL=NO
INFINITY_TO_m_TO_1_REALIZABLE=YES

GENERAL_RESIDUAL_FIBER_LAW=
ORBIT_STABILIZER_UNDER_UNOBSERVED_SYMMETRY

STRONGEST_CROSS_CODER_CANDIDATE=
CENTROIDAL_REFERENCE_NATURALITY

HUMAN_TRIANGULAR_CODER=HYPOTHESIS_NOT_ESTABLISHED
