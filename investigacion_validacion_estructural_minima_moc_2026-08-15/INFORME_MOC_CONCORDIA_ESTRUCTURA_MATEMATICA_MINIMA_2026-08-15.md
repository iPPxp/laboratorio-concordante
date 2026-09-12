# Fundamentos geométricos, proyectivos y combinatorios de MOC y concordIA

**Fecha:** 2026-08-15  
**Estatus:** informe de investigación provisional; no canoniza MOC, no activa concordIA y no constituye validación clínica ni empírica.  
**Método:** lectura de fuentes MOC y Concordante Lab, análisis matemático adversarial y contraste bibliográfico.  

## Convención epistemológica

Se usarán cinco niveles: **N0** coincidencia; **N1** analogía; **N2** isomorfismo estructural parcial; **N3** modelo formal de estados y operaciones; **N4** modelo predictivo con predicciones nuevas y falsables. Una propiedad matemática de un candidato no hereda automáticamente significado MOC.

La evidencia consultada distingue tres autoridades: (i) los documentos MOC fijan semántica; (ii) Concordante Lab conserva estructuras locales auditables; (iii) bibliografía matemática fija resultados matemáticos. Ninguna prueba de software demuestra eficacia psicológica ni convierte una hipótesis en canon.

## 1. Resumen ejecutivo

La respuesta provisional es que **ningún poliedro concreto es la estructura fundamental mínima**. El objeto más parsimonioso que conserva lo actualmente requerido es un **sistema relacional dinámico, tipado y parcialmente observable**, con cinco variables/componentes distinguidos, relaciones declaradas de aridad variable, contexto, operadores de evaluación/intervención y trazas de transición:

\[
\mathfrak M=(P,X,\mathcal R,\Theta,\mathcal T,\mathcal I,\mathcal O),
\qquad |P|=5.
\]

Aquí (P) contiene los cinco roles MOC; (X=\prod_i X_i) es el espacio de estados; (\mathcal R) es una familia **no necesariamente completa** de relaciones tipadas; (\Theta) representa contexto/condiciones; (\mathcal T) contiene transformaciones; (\mathcal I) contiene invariantes o restricciones declaradas; y (\mathcal O) especifica observaciones, evidencia y trazabilidad.

Su implementación mínima es un **hipergrafo dirigido, atribuido y temporal** (o, equivalentemente, tablas de incidencia dispersas más funciones de transición), complementado con vectores para atributos. Esta elección permite pares y relaciones de orden superior sin afirmar que todas existan; admite asimetría, pesos, signo, tipos, tiempo, contexto y provenance. Un grafo ordinario es un caso particular. Un complejo simplicial sólo debe construirse cuando las interacciones sean genuinamente colectivas y además satisfagan cierre por caras; el 4-símplex completo es una visualización/completación máxima, no un hecho MOC.

Resultados principales:

1. La fila (1,5,10,10,5,1) es una consecuencia necesaria del conjunto potencia de cinco etiquetas. Por sí sola está en **N0** respecto de MOC.
2. (K_5) es el 1-esqueleto del 4-símplex y representa diez pares, pero “completo” presupone diez relaciones existentes y homogéneas. Como plantilla de posibilidades está en **N1–N2**; como modelo MOC actual, no alcanza N3.
3. El 4-símplex organiza todos los subconjuntos y formaliza la biyección vértice–faceta opuesta. La interpretación elemento–cuaterna complementaria no está documentada como operación MOC; hoy es **N1**.
4. La hipótesis (4+1) tiene una variante plausible, pero no es “cuatro componentes más un quinto componente observador”: los cinco componentes canónicos siguen siendo componentes. Lo que sí aparece con estatuto distinto es (\Phi_\psi/\mathrm{TrueSelf}_\psi), evaluador/retroalimentador del Pentacoro, exterior al conjunto de cinco componentes. Por tanto, la evidencia favorece provisionalmente **5 + operador/contexto**, no una partición interna 4+1.
5. Razón doble, cuaternas armónicas y cuadrilátero completo son matemáticamente rigurosos, pero requieren colinealidad/incidencia y transformaciones proyectivas que MOC aún no define. No deben llamarse “armónicos” estados equilibrados. Quedan en N0–N1 hasta construir un observable proyectivo y contrastarlo.
6. Pentágono, pentagrama, proporción áurea y tetrakis hexaedro añaden propiedades métricas/simétricas no exigidas. Se descartan como fundamentos actuales.
7. La parte más fértil no es una figura sino la teoría de transformaciones: distinguir coordenadas/mediciones de estructura relacional, especificar qué puede cambiar y qué debe conservarse, y comparar modelos por predicción fuera de muestra.

## 2. Definiciones matemáticas necesarias

### 2.1 Conjunto, relaciones y aridad

Sea (P=\{p_1,\ldots,p_5\}). Una relación binaria es (R\subseteq P\times P). Una relación de aridad (k) es (R_k\subseteq P^k), o sobre subconjuntos si el orden no importa. Tipos, dirección, signo y peso no son propiedades del conjunto: deben declararse.

Un grafo (G=(V,E)) sólo representa relaciones binarias. Un hipergrafo (H=(V,\mathcal E)) permite hiperaristas (e\subseteq V) de tamaño variable. Un complejo simplicial (K\subseteq 2^V) exige **cierre descendente**: si (\sigma\in K) y (\tau\subseteq\sigma), entonces (\tau\in K). Esto es una afirmación sustantiva: una interacción colectiva de cinco elementos obligaría a incluir todas sus subinteracciones como caras, aunque no a darles el mismo peso.

### 2.2 Símplex y vector de caras

El símplex abstracto completo sobre cinco vértices es (\Delta(P)=2^P\setminus\{\varnothing\}). Sus caras de dimensión (k) tienen (k+1) vértices:

\[
f_k=\binom{5}{k+1},\qquad (f_0,f_1,f_2,f_3,f_4)=(5,10,10,5,1).
\]

El 4-símplex o pentácoro es autodual y su 1-esqueleto es (K_5); tiene cinco facetas tetraédricas, diez caras triangulares, diez aristas y cinco vértices ([MathWorld, Pentatope](https://mathworld.wolfram.com/Pentatope.html)).

### 2.3 Razón doble

Para cuatro puntos distintos y ordenados (A,B,C,D\in\mathbb P^1), en una carta afín:

\[
[A,B;C,D]=\frac{(c-a)(d-b)}{(c-b)(d-a)}
\]

(según convención, puede aparecer una permutación equivalente). Es invariante bajo (\mathrm{PGL}(2)); valor (-1) define una cuaterna armónica. El valor depende del orden y sus permutaciones producen, en general, seis valores relacionados. Véanse [Encyclopedia of Mathematics](https://encyclopediaofmath.org/wiki/Cross_ratio) y las [notas de geometría proyectiva de UCR](https://math.ucr.edu/~res/progeom/pg-all.pdf).

### 2.4 Cuadrángulo completo

Cuatro puntos en un plano proyectivo, sin tres colineales, determinan seis rectas; sus pares de lados opuestos determinan tres puntos diagonales. Esto es el **cuadrángulo completo** (no confundir con el cuadrilátero completo, que parte de cuatro rectas). La construcción puede inducir cuaternas armónicas en rectas apropiadas, pero esa incidencia es geométrica y no se deduce de cuatro categorías abstractas ([UCR, capítulo sobre cuadriláteros completos y conjuntos armónicos](https://math.ucr.edu/~res/math205B-2021/progeom/pgnotes05.pdf)).

### 2.5 Sistemas dinámicos e invariantes

Una configuración experiencial es (x_t\in X), con contexto (\theta_t\in\Theta). Una transformación es

\[
x_{t+1}=T_a(x_t,\theta_t),
\]

donde (a) identifica acción/intervención. Un invariante (I) respecto de una familia (\mathcal G) satisface (I(gx)=I(x)) para todo (g\in\mathcal G). Una cantidad equivarante satisface (F(gx)=\rho(g)F(x)). Antes de buscar invariantes hay que especificar la familia de transformaciones admisibles.

## 3. Propiedades conocidas de MOC que requieren representación

De los documentos MOC consultados se extraen, con autoridad semántica interna pero **sin afirmación de validación empírica**, las siguientes exigencias:

| Requisito MOC documentado | Consecuencia formal mínima |
|---|---|
| (\Pi^5_\psi=\langle P_\psi,Eaf_\psi,Act_\psi,V_\psi,S_\psi\rangle) | cinco roles tipados; no cinco cantidades intercambiables |
| (\Phi_\psi=\mathrm{TrueSelf}_\psi\), (\Xi_\psi\ne\mathrm{TrueSelf}_\psi) | operadores/roles externos distinguibles, no un sexto vértice improvisado |
| (\Omega_t\to\Xi\to\Pi^5_t\to\Phi\to C\to\Omega_{t+1}) | composición dirigida y temporal de operadores |
| retroalimentación basal y bucle activo | al menos dos regímenes de transición |
| ajuste activo de átomos funcionales | transformaciones sobre componentes individuales o subconjuntos |
| conducta derivada de (Act_\psi) y configuración situada | salida/observable, no componente sexto |
| objeto, límite, criterio, evidencia y deuda | contexto tipado, restricciones y provenance |
| no sumar/multiplicar sin `embed_psi` y `metric_psi` | separar semántica, codificación y métrica |
| relación local, no identidad global | índices de tiempo/caso y alcance explícito |
| estados de concordancia/fricción/discordancia/disolución | observables ordinales o categóricos, no distancias asumidas |

Estas propiedades requieren más que un vector estático. También muestran que “cinco componentes simétricos” es falso semánticamente: los tipos difieren, y (V_\psi) tiene directividad especial. Sin embargo, diferencia de tipos no equivale a partición geométrica 4+1.

## 4. Estructura combinatoria del sistema de cinco elementos

El polinomio binomial

\[
(1+x)^5=1+5x+10x^2+10x^3+5x^4+x^5
\]

enumera subconjuntos por cardinalidad. La simetría (\binom5k=\binom5{5-k}) proviene de la biyección complemento (S\mapsto P\setminus S).

| Cardinalidad | Cantidad | Lectura matemática | Estatus MOC actual |
|---:|---:|---|---|
| 0 | 1 | conjunto vacío | sin semántica MOC declarada |
| 1 | 5 | componentes | hecho estructural documentado, N2 |
| 2 | 10 | pares posibles | espacio de hipótesis; no diez relaciones demostradas |
| 3 | 10 | tríadas posibles | espacio de hipótesis; no sinergias demostradas |
| 4 | 5 | cuaternas complementarias | biyección matemática; interpretación MOC abierta |
| 5 | 1 | conjunto completo | unidad Pentacoro declarada; interacción irreducible no demostrada |

**Contraejemplo destructor:** cinco colores, cinco carpetas o cinco números generan exactamente la misma fila. Por tanto, la secuencia no explica MOC. Adquiere contenido sólo si se demuestra que una función o relación asociada a una tríada/cuaterna no puede reconstruirse a partir de órdenes inferiores.

## 5. Hipótesis 5 frente a 4+1

Se deben distinguir tres modelos:

1. **5 homogéneo:** acción del grupo (S_5); cualquier permutación conserva estructura. Lo contradicen los tipos semánticos y la directividad especial de (V_\psi).
2. **4+1 interno:** cuatro componentes forman base y uno actúa como ápice/operador. La proyección prismática histórica aproxima esta idea con (V_\psi), pero la auditoría MOC la subordina a la geometría pentacórica y afirma que (V_\psi) sigue siendo componente.
3. **5 + operador/contexto:** cinco componentes tipados forman (\Pi^5_\psi); (\Phi_\psi), (\Xi_\psi), (\Omega_\psi), contexto y elección cumplen otras funciones. Este modelo corresponde mejor al flujo documentado.

Formalmente, el modelo 4+1 interno reduce simetría de (S_5) a (S_4\times S_1). Para discriminarlo se necesita evidencia de que existe un índice (j) tal que:

\[
T(x)_j=f_j(x_j,\theta),\qquad T(x)_{-j}=F(x_{-j};x_j,\theta),
\]

y que ningún otro componente puede ocupar ese papel sin perder predicción. Si el papel cambia por caso, conviene un tipo/rol contextual, no una geometría 4+1 fija.

**Conclusión:** se rechaza 5 homogéneo; no se confirma 4+1 interno; sobrevive 5 tipado + operadores externos (N2 documental, N3 sólo cuando se especifiquen dominios y transiciones ejecutables).

## 6. Análisis de las cinco cuaternas

Las cuaternas (Q_i=P\setminus\{p_i\}) son:

\[
\begin{aligned}
Q_P&=\{Eaf,Act,V,S\}, & Q_{Eaf}&=\{P,Act,V,S\},\\
Q_{Act}&=\{P,Eaf,V,S\}, & Q_V&=\{P,Eaf,Act,S\},\\
Q_S&=\{P,Eaf,Act,V\}.&&
\end{aligned}
\]

En el 4-símplex cada (Q_i) es la faceta opuesta a (p_i). Esto demuestra una dualidad combinatoria, no una compensación experiencial. Tres interpretaciones contrastables:

- **ablación:** (Q_i) representa lo observable/modelable cuando (p_i) falta o queda enmascarado;
- **predicción condicionada:** inferir (p_i) desde (Q_i), (\hat x_i=f_i(x_{-i},\theta));
- **dependencia irreducible:** medir cuánto empeora una predicción o reconstrucción al retirar (p_i).

La dualidad tendría contenido MOC si las cinco ablaciones produjeran perfiles diferenciados y reproducibles. Si todos los modelos de cuatro componentes rinden igual, o si dos componentes bastan, la lectura por facetas queda refutada. No debe suponerse que “lo opuesto” a un componente es “los otros cuatro” en sentido psicológico.

## 7. Geometría proyectiva y razón doble

La geometría proyectiva separa coordenadas de incidencias e invariantes bajo homografías. Es atractiva para narrativas que cambian de escala o punto de vista, pero la razón doble exige:

1. un observable unidimensional (z:\mathcal C\to\mathbb P^1);
2. cuatro posiciones ordenadas distintas (z_A,z_B,z_C,z_D);
3. una justificación de que los cambios relevantes actúan como (z\mapsto(az+b)/(cz+d));
4. datos suficientes para comprobar conservación.

Sin estos cuatro pasos, (P,Eaf,Act,V,S) no son cinco puntos proyectivos: son tipos heterogéneos. Tampoco hay razón para que cuatro de ellos sean colineales.

Una prueba válida sería seleccionar cuatro **estados del mismo observable** antes/después de cambios de encuadre, estimar homografías y comparar el error de conservación de razón doble contra alternativas afines, monótonas y no paramétricas. La hipótesis armónica adicional es ( [A,B;C,D]=-1 ); debe preregistrarse, no buscarse retrospectivamente.

**Veredicto:** la razón doble es una herramienta potencial para invariancia de medición, no una ontología del Pentacoro. Nivel actual N1; podría alcanzar N3 sólo con observable, transformación y procedimiento de estimación definidos.

El cuadrángulo completo representa “relaciones entre relaciones” mediante intersecciones de seis rectas. Pero un cruce dibujado no es automáticamente un nuevo fenómeno. Para MOC se requeriría una operación (h(R_{ij},R_{kl})\to q) con salida observable. Sin ella, la emergencia es gráfica, no formal.

## 8. Comparación de figuras y estructuras candidatas

Escala: 1 muy bajo, 5 muy alto. En “riesgo”, 5 es peor. Las puntuaciones miden adecuación con la evidencia actual, no belleza matemática.

| Candidato | Parsimonia | Correspondencia | Explicativo | Predictivo | Computable | Invariantes | Falsable | Riesgo | Nivel actual | Veredicto |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| Recta proyectiva + 4 puntos | 2 | 1 | 2 | 3 | 4 | 5 | 4 | 5 | N1 | útil sólo para observables proyectivos definidos |
| Cuadrángulo completo | 2 | 1 | 2 | 2 | 3 | 4 | 3 | 5 | N0–N1 | no hay incidencia MOC demostrada |
| Tetraedro | 3 | 1 | 1 | 1 | 4 | 2 | 3 | 4 | N1 | sólo si se valida 4+1 interno |
| Pentágono/pentagrama | 2 | 1 | 1 | 1 | 4 | 2 | 3 | 5 | N0–N1 | orden cíclico y razón áurea no derivados |
| (K_5) | 4 | 3 | 3 | 3 | 5 | 3 | 4 | 3 | N1–N2 | buena plantilla binaria, demasiado completo |
| Complejo simplicial de 5 | 3 | 3 | 4 | 4 | 4 | 4 | 5 | 3 | N1–N2 | usar sólo si hay interacciones colectivas y cierre |
| 4-símplex | 3 | 3 | 3 | 3 | 4 | 4 | 4 | 4 | N1–N2 | realización del complejo completo, no fundamento probado |
| Tetrakis hexaedro | 1 | 1 | 1 | 1 | 2 | 2 | 2 | 5 | N0 | descartar como fundamento |
| Hipergrafo tipado temporal | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 2 | N2; candidato N3 | mejor arquitectura mínima provisional |
| Sistema relacional dinámico | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 1 | N2; candidato N3 | estructura fundamental recomendada |

Notas:

- (K_5) tiene diez aristas y es no planar; cualquier pentágono/pentagrama plano es un dibujo con cruces o una selección de aristas, no una equivalencia geométrica plana sin pérdida ([MathWorld, Complete Graph](https://mathworld.wolfram.com/CompleteGraph.html)).
- El tetrakis hexaedro es un poliedro de 24 caras, dual del octaedro truncado y construido por aumento de un cubo; esas cardinalidades y su simetría no se derivan de los cinco componentes ([MathWorld, Tetrakis Hexahedron](https://mathworld.wolfram.com/TetrakisHexahedron.html)).
- La proporción áurea pertenece al pentágono regular métrico; cinco puntos generales o un (K_5) no la implican.

## 9. Invariantes y transformaciones

La unidad correcta de análisis es una trayectoria:

\[
\mathcal C_t=(x_t,H_t,\theta_t,q_t),\qquad
\mathcal C_{t+1}=T_a(\mathcal C_t).
\]

(x_t) contiene atributos de componentes; (H_t) relaciones activas; (\theta_t) contexto; (q_t) traza/evidencia. Los candidatos a invariantes deben clasificarse:

- **semánticos:** identidad de tipos y prohibiciones (por ejemplo, conducta no se vuelve sexto componente);
- **estructurales:** patrones de incidencia, conectividad o dependencia condicional;
- **ordinales:** orden de estados si las escalas sólo soportan comparación;
- **proyectivos:** razón doble, únicamente bajo homografías justificadas;
- **operativos:** objeto, límite, criterio, regla ganadora, deuda y provenance;
- **topológicos:** componentes conexas/ciclos persistentes, sólo si existe una filtración métrica o de pesos justificable.

Reversibilidad no debe inferirse de una flecha. (T) es reversible si es inyectiva sobre el dominio relevante y existe (T^{-1}). Pérdida de información por agregación, umbral, olvido de contexto o salida ordinal suele hacerla no invertible.

Dos narrativas pueden considerarse equivalentes si existe un isomorfismo tipado (\varphi) que preserva relaciones, atributos relevantes y traza, o una equivalencia más débil definida antes del análisis. La renominación libre de los cinco roles no es válida si sus tipos difieren.

## 10. Implicaciones para concordIA

| Representación | Representa/conserva | Pierde o presupone | Coste típico | Uso recomendado |
|---|---|---|---|---|
| vector (x\in\mathbb R^d) | atributos, ML estándar | incidencia explícita; exige escalas/embedding | (O(d)) | atributos de nodos/contexto |
| matriz de adyacencia | pares, dirección, pesos | interacciones irreducibles superiores | (O(n^2)), aquí pequeño | baseline grafo |
| grafo atribuido | nodos/aristas tipadas | órdenes superiores salvo reificación | (O(|V|+|E|)) | pipeline/trazas |
| hipergrafo | relaciones de cualquier aridad | no impone cierre/topología | incidencia (O(\sum|e|)) | **núcleo recomendado** |
| tensor denso | interacciones k-arias | explosión (O(n^k)), ceros, poca trazabilidad | alto | sólo módulos pequeños |
| complejo simplicial | jerarquía de caras, orientación | exige cierre descendente | depende de caras | si datos validan sinergias colectivas |
| coordenadas homogéneas | equivalencia de escala, homografías | requiere observable proyectivo | bajo/moderado | módulo experimental |
| embedding aprendido | similitud/predicción | interpretabilidad y autoridad semántica | variable | capa auxiliar, nunca canon |
| sistema dinámico | transiciones, control, invariantes | requiere datos longitudinales | variable | arquitectura temporal |

La literatura de aprendizaje geométrico propone incorporar simetrías/regularidades como sesgos inductivos, no elegir geometría por simbolismo ([Bronstein et al., *Geometric Deep Learning*](https://arxiv.org/abs/2104.13478)). Las HGNN modelan correlaciones de orden superior ([Feng et al.](https://arxiv.org/abs/1809.09401)); las redes simpliciales hacen message passing sobre complejos y pueden distinguir estructuras que GNN ordinarias no distinguen ([Bodnar et al.](https://arxiv.org/abs/2103.03212)). Esas ventajas generales no prueban que los datos MOC contengan tales interacciones.

### Esquema computacional mínimo

```text
ExperienceState
  id, time, scope, context, evidence
  nodes: [component_id, semantic_type, observed_attributes, uncertainty]
  relations: [relation_id, ordered_endpoints, arity, type, sign, weight,
              validity_interval, evidence_id]
  operators: [operator_type, preconditions, parameters, version]
  transition: [source_id, operator_id, target_id, reversible_status]
  trace: [rules, debt, missingness, provenance, prohibited_uses]
```

Un vector y una configuración relacional no son alternativas excluyentes: el hipergrafo conserva estructura; vectores codifican atributos de nodos, hiperaristas y contexto. La semántica debe residir en un esquema versionado, no en la posición geométrica aprendida.

## 11. Contraejemplos y objeciones

1. **Pascal inevitable:** cualquier conjunto de cinco categorías produce 5–10–10–5–1. No distingue MOC.
2. **Compleción espuria:** pasar de algunas relaciones a (K_5) inventa las ausentes; pasar de (K_5) al 4-símplex inventa tríadas y órdenes superiores.
3. **Interacción superior reducible:** una puntuación de tríada puede ser suma de tres pares. En ese caso el hipergrafo no añade explicación.
4. **Cierre simplicial falso:** puede existir una interacción de cinco vías aunque ninguna subinteracción aislada sea significativa; eso es hipergrafo, no complejo simplicial interpretado semánticamente.
5. **Colinealidad inventada:** cuatro variables heterogéneas pueden siempre dibujarse en una recta después de codificarlas; la razón doble resultante depende del embedding.
6. **Armonía nominal:** “armónico” matemático significa razón doble (-1), no equilibrio psicológico.
7. **No identificabilidad:** muchos embeddings/vectores pueden producir las mismas salidas; sin restricciones, la geometría latente no es interpretable.
8. **Contexto omitido:** dos configuraciones con los mismos cinco valores pueden tener distinta lectura por objeto, límite, criterio, tiempo o evidencia.
9. **Causalidad:** una arista o hiperarista predictiva no demuestra influencia causal.
10. **Pequeño (n):** con sólo cinco tipos de componente, un modelo profundo puede sobreajustar; la complejidad debe justificarse por número de casos y tareas, no por número de caras posibles.

## 12. Hipótesis descartadas

Se descartan **como fundamentos actuales**, no como visualizaciones exploratorias:

- tetrakis hexaedro: N0, cardinalidad y geometría no derivadas;
- proporción áurea/pentágono regular: N0;
- pentagrama como estructura necesaria: N0–N1;
- cuaterna armónica como sinónimo de concordancia: error categorial;
- (K_5) como afirmación de que todas las relaciones existen: no documentado;
- 4-símplex completo como prueba de interacciones de todos los órdenes: no se sigue del número cinco;
- cinco componentes plenamente simétricos: contradicho por tipos/roles documentados;
- quinto componente como observador externo: contradice que los cinco sigan siendo componentes y confunde (V_\psi) con (\Phi_\psi).

## 13. Hipótesis que sobreviven

1. **H-RDS:** MOC se representa mejor como sistema relacional dinámico tipado (N2 documental; candidato N3).
2. **H-HYP:** algunas propiedades pueden depender de relaciones irreducibles de aridad (>2); abierta y falsable.
3. **H-5OP:** cinco componentes tipados más operadores/contexto externos explica mejor el flujo que 5 homogéneo o 4+1 interno.
4. **H-ABL:** las cinco cuaternas son útiles como familias de ablación/predicción condicionada, no como “opuestos” semánticos.
5. **H-PROJ:** invariantes proyectivos pueden ser útiles para observables específicos si se define una acción de (\mathrm{PGL}(2)); no para los cinco componentes como tales.
6. **H-MULTI:** concordIA debe combinar estructura relacional con vectores de atributos y dinámica temporal.

## 14. Experimentos matemáticos/computacionales propuestos

### E1. Censo relacional y prueba de aridad

Crear un diccionario semántico, aprobado por autoridad MOC, de relaciones candidatas con endpoints, orden, tipo, signo, contexto y evidencia. Comparar por validación fuera de muestra:

\[
M_0:\text{atributos},\quad M_1:\text{pares},\quad
M_2:\text{hiperaristas seleccionadas},\quad M_3:\Delta(P)\text{ completo}.
\]

Usar penalización por complejidad y calibración. Si (M_2/M_3) no mejora predicción o explicación reproducible frente a (M_1), rechazar orden superior.

### E2. Cinco ablaciones

Para cada (i), entrenar/evaluar (f_i(x_{-i},H_{-i},\theta)\to x_i) y medir pérdida, incertidumbre y estabilidad. Preregistrar qué patrón apoyaría una faceta complementaria significativa.

### E3. 5 frente a 4+1

Comparar modelos con parámetros compartidos (S_5), parámetros (S_4\times S_1), y tipos completamente distinguidos. La mejor generalización decide el sesgo útil; no la apariencia de una pirámide.

### E4. Interacciones irreducibles

Para cada subconjunto (S), estimar un efecto de sinergia (por ejemplo, diferencia entre desempeño conjunto y mejor descomposición de órdenes inferiores), con corrección por múltiples pruebas. Exigir replicación.

### E5. Invariancia narrativa

Construir pares de narrativas con la misma estructura declarada y vocabulario/superficie distintos, más pares adversariales superficialmente similares pero estructuralmente distintos. Medir si concordIA preserva clases relacionales y detecta diferencias.

### E6. Hipótesis proyectiva acotada

Definir un único observable ordinal/continuo, cuatro anclas y transformaciones de reencuadre. Comparar conservación de razón doble contra modelos afines, monótonos y libres. No probar (-1) salvo hipótesis preregistrada.

### E7. Dinámica y reversibilidad

Registrar secuencias sintéticas con precondiciones, operador y salida. Verificar composición, idempotencia, conmutación/no conmutación, pérdida de información y existencia de inversa en dominios acotados.

### E8. TDA sólo después de métrica

Si existe una disimilitud justificada, construir filtraciones y persistencia; repetir bajo perturbaciones. TDA puede estudiar estabilidad topológica de datos, pero una nube de puntos en un símplex estándar no valida semántica ([Edelsbrunner, Virk y Wagner](https://arxiv.org/abs/1903.08510)).

## 15. Predicciones falsables

| ID | Predicción | Refutación |
|---|---|---|
| P1 | un modelo relacional supera a vector plano en casos con igual marginal y distinta configuración | rendimiento equivalente con control de capacidad |
| P2 | al menos una relación de orden (>2) mejora generalización sobre todos los pares | ninguna mejora replicada |
| P3 | los cinco tipos distinguidos superan simetría (S_5) | modelo (S_5) igual o mejor fuera de muestra |
| P4 | 5+operador supera 4+1 interno fijo | 4+1 gana establemente y el mismo quinto rol es identificable |
| P5 | al menos una ablación (Q_i) tiene firma específica reproducible | perfiles intercambiables/inestables |
| P6 | narrativas estructuralmente equivalentes reciben salidas equivalentes | sensibilidad dominante al vocabulario superficial |
| P7 | una familia de reencuadres preserva razón doble mejor que baselines | no conservación o dependencia del embedding |
| P8 | ciertas operaciones MOC no conmutan de forma reproducible | orden de operaciones irrelevante |
| P9 | deuda/contexto mejora calibración y abstención | no mejora o introduce ruido |
| P10 | el complejo simplicial aporta señal sólo cuando hay cierre empírico por caras | desempeño igual al hipergrafo más simple o cierre contradicho |

Ninguna de estas predicciones autoriza conclusiones clínicas. Primero deben probarse en casos sintéticos/documentales autorizados; cualquier estudio con personas requiere gobernanza y diseño separados.

## 16. Programa de investigación posterior

**Fase A — especificación semántica:** aprobar tipos, dominios, relaciones permitidas/prohibidas, observables y condiciones de equivalencia. Entregable: esquema versionado y conjunto de contraejemplos.

**Fase B — baseline mínimo:** implementar vector, grafo dirigido y hipergrafo con idénticos atributos y presupuesto de parámetros. Entregable: evaluación comparativa reproducible.

**Fase C — dinámica:** definir operadores (T_a), precondiciones, composición, trazas e incertidumbre. Entregable: álgebra parcial de transformaciones, no promesas de eficacia.

**Fase D — orden superior:** admitir una hiperarista sólo si posee definición MOC y ganancia explicativa/predictiva. Convertir a complejo simplicial únicamente si el cierre por caras es defendible.

**Fase E — invariantes:** probar primero invariantes tipados/operativos; después ordinales y, sólo con coordenadas justificadas, proyectivos o topológicos.

**Fase F — validación independiente:** preregistro, conjunto externo, análisis de fallos y decisión humana separada sobre cualquier promoción.

## Respuesta final obligatoria

Si se eliminan nombres, simbolismos y preferencias geométricas previas, el objeto más simple que conserva lo esencial es:

\[
\boxed{\text{estructura fundamental}=
\text{sistema relacional dinámico, tipado, contextual y trazable}}
\]

No es todavía un espacio métrico, un (K_5), un 4-símplex ni una recta proyectiva. Es una estructura de cinco roles más relaciones parciales de aridad declarada y transformaciones sujetas a restricciones.

\[
\boxed{\text{representación/visualización}=
\text{grafo o hipergrafo; 4-símplex sólo como mapa de posibilidades}}
\]

(K_5), el pentágono, el tetraedro o proyecciones del 4-símplex pueden ayudar a visualizar cortes específicos. Ninguno debe introducir relaciones, orden, simetría o métrica no demostrados.

\[
\boxed{\text{implementación computacional}=
\text{hipergrafo dirigido atribuido temporal + vectores + transiciones + provenance}}
\]

### Arquitectura mínima provisional

**Demostrado matemáticamente:** conteos binomiales; complementariedad (S\leftrightarrow P\setminus S); equivalencia entre (K_5) y el 1-esqueleto del 4-símplex; propiedades de razón doble; capacidad formal de grafos/hipergrafos/complejos.

**Documentado como semántica MOC:** cinco componentes tipados; distinción de (\Phi_\psi), (\Xi_\psi), conducta y contexto; bucle basal/activo; configuración y transformación; necesidad de embedding/métrica antes de aritmética; restricciones y trazabilidad. Esto es autoridad interna del modelo, no constatación científica externa.

**Hipótesis de modelización:** que relaciones de orden superior sean irreducibles; que cinco ablaciones posean significado; que 5+operador sea predictivamente superior; que existan equivalencias narrativas estructurales; que algún observable admita invariancia proyectiva.

**Requiere validación empírica:** toda afirmación sobre personas/experiencias reales, mejora cualitativa, invariantes observados, causalidad, generalización de concordIA y ventaja predictiva de una geometría.

La regla de avance es sencilla: empezar con relaciones tipadas parciales; agregar aridad, métrica, topología o geometría únicamente cuando una definición MOC y una prueba discriminante lo exijan.

## Bibliografía académica esencial

- M. Bronstein, J. Bruna, T. Cohen y P. Veličković, [*Geometric Deep Learning: Grids, Groups, Graphs, Geodesics, and Gauges*](https://arxiv.org/abs/2104.13478), 2021.
- Y. Feng et al., [*Hypergraph Neural Networks*](https://arxiv.org/abs/1809.09401), 2018.
- C. Bodnar et al., [*Weisfeiler and Lehman Go Topological: Message Passing Simplicial Networks*](https://arxiv.org/abs/2103.03212), 2021.
- H. Edelsbrunner, Ž. Virk y H. Wagner, [*Topological Data Analysis in Information Space*](https://arxiv.org/abs/1903.08510), 2019.
- R. Schultz, [*Essential Concepts of Projective Geometry*](https://math.ucr.edu/~res/progeom/pg-all.pdf), notas académicas, University of California, Riverside.
- [*Cross ratio*](https://encyclopediaofmath.org/wiki/Cross_ratio), Encyclopedia of Mathematics (referencia a Coxeter, *Projective Geometry*).
- E. Weisstein, [*Pentatope*](https://mathworld.wolfram.com/Pentatope.html), [*Complete Graph*](https://mathworld.wolfram.com/CompleteGraph.html) y [*Tetrakis Hexahedron*](https://mathworld.wolfram.com/TetrakisHexahedron.html), MathWorld.

## Fuentes internas consultadas

- `C:\Users\IximM\OneDrive\Documentos\v.1.5.2\psicologia\MOC-AX-001_Axiomas_Base.md`
- `C:\Users\IximM\OneDrive\Documentos\v.1.5.2\psicologia\MOC-CAN-AX-003_Ejes_Horizontal_Vertical.md`
- `C:\Users\IximM\OneDrive\Documentos\v.1.5.2\psicologia\MOC-CANON-001_Acta_Canonizacion_Pentacoron_Phi_Ejes.md`
- `C:\Users\IximM\OneDrive\Documentos\v.1.5.2\psicologia\MOC-MATH-AUD-001_Auditoria_Canon_Matematico.md`
- `C:\Users\IximM\OneDrive\Documentos\Concordante Lab\03_Expedientes\MOC-001_Semantica_Provisional.md`
- `C:\Users\IximM\OneDrive\Documentos\Concordante Lab\03_Expedientes\MOC-EXP-GRAPH-001_Grafo_Experiencia_Local.md`
- `C:\Users\IximM\OneDrive\Documentos\Concordante Lab\03_Expedientes\MOC-001_Tabla_Operaciones_Formales.md`

