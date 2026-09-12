# MOC-FRON-ONT-001: Auditoría II — Fase 2, operadores canónicos

**Estatus:** auditoría adversarial del canon; resultado condicional por régimen.  
**Fecha:** 5 de agosto de 2026.  
**Fuente normativa principal:** *El pentacoro experiencial de MOC: formalización y operativa iPP*, integrado con la enmienda MOC-MED-001.  
**Pregunta de decisión:** ¿la información atribuida a \(\mathcal F_{\psi,C}\) exige un componente formal independiente o es definible mediante los operadores canónicos?

---

## 0. Dictamen ejecutivo

### Resultado

**No se justifica introducir \(\mathcal F_{\psi,C}\) como primitivo formal independiente.**

En los regímenes canónicos, la relación de configuraciones admisibles puede definirse como el grafo —o, en el caso recursivo, la relación de soluciones— inducido por \(G_\psi\) y \(H_\psi\). Por ello, HIP-2 de la Fase 1 (“\(\mathcal F\) no es completamente derivable de operadores ya definidos”) no queda satisfecha frente al canon disponible.

La conclusión no es que la información relacional sea innecesaria. La conclusión es más precisa:

> La información de compatibilidad puede ser necesaria para responder las consultas de \(Q_{\text{transición}}\), pero el canon ya proporciona posiciones formales capaces de codificarla: principalmente \(G_\psi\) y \(H_\psi\), y analíticamente \(\Phi_\psi^{(1)}\), `Coh` y el perfil opcional \(m_k\). Una \(\mathcal F_{\psi,C}\) explícita sería una relación derivada o una herramienta metateórica, no un nuevo primitivo.

### Clasificación final

| Tesis | Dictamen | Clasificación |
|---|---|---|
| Preservar compatibilidades exige contenido relacional | Aceptada condicionalmente, relativa a \(Q_{\text{transición}}\) | `[ARG]` |
| \(\mathcal F_{\psi,C}\) debe añadirse como componente explícito independiente | Rechazada con el canon actual | `[RESULTADO CONDICIONAL]` |
| \(\mathcal F_{\psi,C}\) puede definirse desde \(G_\psi,H_\psi\) | Sí, por construcción del grafo/relación de soluciones | `[PROP]` |
| El canon especifica efectivamente todas las compatibilidades | No; los operadores permanecen parcialmente esquemáticos | `[INDETERMINADO / SUBESPECIFICADO]` |
| Existe una tercera entidad ontológica | No demostrada; no se sigue del formalismo | `[NO DEMOSTRADA]` |
| Debe construirse ahora el cubo como necesidad canónica | No | `[NO PROCEDE]` |

---

## 1. Criterio riguroso de auditoría

### 1.1 Dos preguntas que no deben confundirse

1. **Definibilidad:** ¿puede reconstruirse una relación de admisibilidad a partir de los operadores canónicos?
2. **Especificación efectiva:** ¿ofrece el canon reglas suficientemente concretas para decidir, en cada caso, qué configuraciones pertenecen a esa relación?

Una respuesta afirmativa a la primera bloquea la independencia formal de \(\mathcal F_{\psi,C}\). Una respuesta negativa a la segunda solo muestra subespecificación del canon; no demuestra que haga falta un nuevo tipo de objeto.

### 1.2 Criterio de suficiencia respecto de consultas

Sea \(Q_{\text{transición}}\) la clase de consultas fijada en Fase 1. Una representación canónica \(K\) es suficiente respecto de \(Q_{\text{transición}}\) si existe un procedimiento de traducción \(T\) tal que, para toda consulta \(q\) cuyo valor esté definido:

\[
q(\mathcal F_{\psi,C})=q(T(K)).
\]

No se exige isomorfismo ontológico ni identidad sintáctica. Se exige conservación de respuestas.

---

## 2. Reconstrucción de la relación inducida por el canon

Para evitar la colisión de símbolos, se absorbe \(C\) como parámetro de la relación. Para cada contexto fijo \(C\), se definen las siguientes relaciones.

### 2.1 Forma acoplada no recursiva

El canon declara:

\[
Z=G_\psi(V,C),\qquad R=H_\psi(V,Z,C),\qquad Z=(I,E,A).
\]

Definimos:

\[
\mathcal F^{\mathrm{nr}}_{\psi,C}:=
\{(V,I,E,A,R):
(I,E,A)=G_\psi(V,C)\land
R=H_\psi(V,(I,E,A),C)\}.
\]

**[PROP-1]** Si \(G_\psi\) y \(H_\psi\) son funciones totales, \(\mathcal F^{\mathrm{nr}}_{\psi,C}\) queda determinada por ellas y no añade información extensional.

**Consecuencia:** para cada \(V,C\) existe una única tríada \(Z\) y un único \(R\). Por tanto, el régimen es determinista tanto en realización interna como en resultado, salvo que “función” se use informalmente o se introduzcan parámetros latentes/aleatoriedad no declarados.

### 2.2 Forma acoplada recursiva

El canon admite:

\[
Z=G_\psi(V,Z,C),\qquad R=H_\psi(V,Z,C).
\]

La relación inducida es:

\[
\mathcal F^{\mathrm{fp}}_{\psi,C}:=
\{(V,I,E,A,R):
Z=(I,E,A)\land Z=G_\psi(V,Z,C)\land
R=H_\psi(V,Z,C)\}.
\]

**[PROP-2]** La posible multiplicidad de realizaciones procede de la multiplicidad de puntos fijos de \(G_\psi\), no de una \(\mathcal F\) independiente.

Para cada \(V,C\), sea

\[
\operatorname{Fix}_{\psi,C}(V)=\{Z:Z=G_\psi(V,Z,C)\}.
\]

Entonces:

- no hay transición si \(\operatorname{Fix}_{\psi,C}(V)=\varnothing\);
- hay una realización interna si su cardinalidad es uno;
- hay varias realizaciones internas si su cardinalidad es mayor que uno;
- el resultado es determinista exactamente cuando
  \[
  \left|\{H_\psi(V,Z,C):Z\in\operatorname{Fix}_{\psi,C}(V)\}\right|=1.
  \]

El canon reconoce que esta forma requiere condiciones de existencia de punto fijo, pero no fija criterios de existencia, unicidad ni selección. Eso deja el régimen **subespecificado**, no formalmente independiente.

### 2.3 Factorización secuencial

El canon también admite la hipótesis fuerte:

\[
\begin{aligned}
I&=I_\psi(V,C),\\
E&=E_\psi(V,I,C),\\
A&=A_\psi(V,I,E,C),\\
R&=R_\psi(V,I,E,A,C).
\end{aligned}
\]

Se induce:

\[
\mathcal F^{\mathrm{seq}}_{\psi,C}:=
\{(V,I,E,A,R):
I=I_\psi(V,C)\land E=E_\psi(V,I,C)\land
A=A_\psi(V,I,E,C)\land R=R_\psi(V,I,E,A,C)\}.
\]

**[PROP-3]** Bajo funciones totales, esta relación también es un grafo derivado y es determinista. Su costo adicional es la hipótesis de triangularidad \(I\to E\to A\), no una nueva estructura relacional independiente.

---

## 3. Auditoría operador por operador

| Operador | Papel canónico | ¿Codifica compatibilidad? | ¿Hace independiente a \(\mathcal F\)? |
|---|---|---|---|
| \(G_\psi\) | Genera conjuntamente \(Z=(I,E,A)\); admite forma recursiva | Sí: fija qué tríadas son soluciones para \((V,C)\) | No; induce la parte interna de \(\mathcal F\) |
| \(H_\psi\) | Produce \(R\) desde \((V,Z,C)\) | Sí: fija la asociación de realizaciones con resultados | No; completa el grafo inducido |
| \(\Phi_\psi^{(0)}\) | Evalúa globalmente \(\Omega\) y abre/cierra la compuerta | No reconstruye realizaciones; clasifica a grano grueso | No; no es sustituto generativo de \(G/H\) |
| \(\Phi_\psi^{(1)}\) | Evalúa la tupla descompuesta y localiza incompatibilidades | Sí, analíticamente, si sus predicados están especificados | No; puede alojar descriptores derivados |
| `Coh` / \(\delta_k\) | Predicado o medida de coherencia/discordancia | Solo una compresión de compatibilidad; puede perder detalle | No; responde un subconjunto de consultas |
| \(Q_{\mathrm{med},\psi}\), \(m_k\) | Perfil opcional subordinado a \(\Phi^{(1)}\) | Puede discriminar patrones relacionales | No; el canon lo declara auxiliar, posdescomposición y no causal |

### 3.1 \(G_\psi\): posición principal de la compatibilidad interna

La forma acoplada evita imponer una cascada causal y permite dependencia simultánea \(I\leftrightarrow E\leftrightarrow A\). Por tanto, la afirmación de Fase 1 de que “la información vive únicamente en \(\mathcal F\)” es demasiado fuerte: la misma información puede vivir en la ecuación de punto fijo de \(G_\psi\).

Falta en el canon:

- dominio/codominio completos en la variante recursiva;
- condiciones de existencia y unicidad;
- regla de selección cuando hay múltiples puntos fijos;
- tratamiento explícito de parámetros latentes o estocásticos.

Ninguna de esas carencias exige por sí misma un sexto componente. Exige especificar mejor \(G_\psi\) o declarar una semántica relacional/estocástica.

### 3.2 \(H_\psi\): posición principal de la compatibilidad transición–resultado

Al tomar \(Z\) como argumento, \(H_\psi(V,Z,C)\) ya representa la dependencia del resultado respecto de la configuración interna. La enmienda MOC-MED-001 es explícita: interponer un operador causal autónomo entre \(G_\psi\) y \(H_\psi\) es redundante mientras no se demuestre una etapa independiente.

Falta en el canon una regla extensional concreta de \(H_\psi\). Por eso no pueden resolverse empíricamente todas las consultas de \(Q_{\text{transición}}\). Pero añadir el símbolo \(\mathcal F\) sin axiomas nuevos solo renombraría la misma caja negra.

### 3.3 \(\Phi_\psi^{(0)}\): evaluador global, no generador de compatibilidades

\(\Phi_\psi^{(0)}:\mathcal O\to\{C,F,D,X\}\) decide la compuerta sin descomposición previa. Su función es económica y clasificatoria. Por construcción no conserva el detalle necesario para responder qué realizaciones \((I,E,A)\) producen cada \(R\).

No llena ni crea el supuesto vacío de \(\mathcal F\); simplemente opera a otro grano.

### 3.4 \(\Phi_\psi^{(1)}\): análisis detallado posterior

\(\Phi_\psi^{(1)}\) recibe la configuración ya realizada y puede localizar incompatibilidades. Puede además producir \(m_k\) mediante \(Q_{\mathrm{med},\psi}\). Esto preserva una representación explícita de patrones relacionales cuando aporta valor incremental.

Pero su dirección es analítica:

\[
(V,I,E,A,R)\longmapsto \text{dictamen/perfil}.
\]

No genera por sí sola el conjunto de configuraciones posibles. Por tanto, complementa a \(G/H\), pero no demuestra una entidad mediadora causal.

---

## 4. Resultado sobre HIP-1, HIP-2 y HIP-3

| Hipótesis de Fase 1 | Resultado de Fase 2 | Razón |
|---|---|---|
| HIP-1: \(\mathcal F\) no trivial | No establecida universalmente | Depende de las funciones, puntos fijos y dominios concretos |
| HIP-2: \(\mathcal F\) no derivable de \(G/H\) | **Refutada en sentido definicional** | Las ecuaciones anteriores construyen \(\mathcal F\) como grafo/relación de soluciones |
| HIP-3: existen consultas distinguidoras | Plausible, pero requiere operacionalización | \(\Phi^{(1)}\), `Coh` y \(m_k\) presuponen diferencias evaluables |

Como el argumento de irreducibilidad explícita exigía conjuntamente HIP-1/2/3, la refutación definicional de HIP-2 impide concluir necesidad estructural independiente.

---

## 5. Prueba de suficiencia relativa a \(Q_{\text{transición}}\)

Sea \(K_{\psi,C}=(G_\psi,H_\psi)\). Defínase el traductor:

\[
T(K_{\psi,C})=\mathcal F^{\mathrm{nr}}_{\psi,C}
\quad\text{o}\quad
T(K_{\psi,C})=\mathcal F^{\mathrm{fp}}_{\psi,C},
\]

según el régimen.

**[ARG-1]** Toda consulta de \(Q_{\text{transición}}\) formulada sobre pertenencia, proyección, cardinalidad o compatibilidad en \(\mathcal F\) puede reformularse sobre las ecuaciones de \(G/H\):

- “¿Es posible \(V\to R\)?” equivale a preguntar si existe un \(Z\) que satisfaga las ecuaciones y produzca \(R\).
- “¿Qué configuraciones realizan \((V,R)\)?” equivale a obtener los \(Z\) solución con \(H(V,Z,C)=R\).
- “¿Es determinista el resultado?” equivale a contar la imagen por \(H\) del conjunto de soluciones de \(G\).
- “¿Qué restricciones internas existen?” equivale a caracterizar el conjunto de soluciones de la ecuación generadora.

Por construcción, las respuestas coinciden cuando los operadores están especificados.

**Conclusión:** \(G/H\) son suficientes para las consultas de \(Q_{\text{transición}}\) en sentido definicional. Si no puede calcularse una respuesta, el defecto es la falta de especificación de los operadores, no la ausencia lógica de \(\mathcal F\).

---

## 6. Qué sí aportaría una \(\mathcal F\) explícita

Aunque no sea primitiva, puede ser útil como:

1. **Semántica extensional derivada:** el grafo conjunto de \(G/H\).
2. **Instrumento de auditoría:** permite comparar regímenes deterministas, recursivos o estocásticos con una notación uniforme.
3. **Contrato de consultas:** hace explícitas las preguntas que el canon debe poder responder.
4. **Especificación empírica:** puede aproximarse mediante datos cuando \(G/H\) no tengan forma cerrada.

En todos estos usos debe etiquetarse como objeto derivado:

\[
\boxed{\mathcal F_{\psi,C}:=\operatorname{Graph/Sol}(G_\psi,H_\psi)}
\]

y no como sexto vértice, tercer término causal o dominio ontológico adicional.

---

## 7. Correcciones pendientes en el documento de Fase 1

La versión examinada declara haber reclasificado la tesis, pero conserva tres residuos contradictorios:

1. **§4.1:** aún usa “explícitamente (o su equivalente isomorfo)”. Debe decir “explícitamente o mediante una representación suficiente respecto de la clase de consultas pertinente”.
2. **§4.1:** afirma “Estatus: probado matemáticamente (sección 3)”. Debe decir “argumentado condicionalmente bajo HIP-1/2/3”.
3. **§7.1:** presenta “[TEO] Necesidad descriptiva” y “Estatus: Probado”. Debe reclasificarse como `[ARG]` condicional y eliminar la formulación universal.

Además, en §2.1 las consultas se tipan todas como funciones con codominio \(\{V,F,?\}\), pero el ejemplo \(q_3\) devuelve un conjunto de pares \((I,E)\). La formalización correcta requiere codominios dependientes de cada consulta, o un universo común de respuestas:

\[
q\colon \mathcal P(X)\to A_q,
\]

donde \(A_q\) es el tipo de respuesta de la consulta \(q\). La equivalencia informacional debe comparar respuestas dentro del mismo \(A_q\).

---

## 8. Decisión sobre el cubo

### No procede como consecuencia necesaria

Construir el cubo ahora introduciría una geometría que no se deriva de la auditoría de operadores. El propio canon sostiene que el símplex es opcional y que la geometría no añade poder expresivo a las ecuaciones. Con mayor razón, una nueva figura no puede presentarse como solución necesaria a una carencia que no ha sido demostrada.

### Único camino admisible para retomarlo

El cubo podría estudiarse después como **representación heurística o analítica**, siempre que:

1. se defina qué variables, caras y aristas representan;
2. se pruebe qué consultas responde que el pentacoro o el grafo de \(G/H\) no responden;
3. se establezca validez incremental empírica o inferencial;
4. se etiquete como `[AN-G]` o `[HIP-CI]`, nunca como ontología derivada.

---

## 9. Conclusión defendible de Fase 2

> El canon MOC ya contiene estructura relacional suficiente en sentido definicional: \(G_\psi\) determina las configuraciones internas admisibles —directamente o como puntos fijos— y \(H_\psi\) determina sus resultados. \(\Phi_\psi^{(1)}\), `Coh` y el perfil opcional \(m_k\) permiten análisis relacional posterior. Por tanto, \(\mathcal F_{\psi,C}\) no es estructuralmente independiente; puede conservarse como relación derivada para auditoría y consulta. La insuficiencia vigente es de especificación efectiva de los operadores, no de inventario formal u ontológico. No se justifica un tercer término causal, un sexto vértice ni la construcción necesaria del cubo.

### Próximo trabajo correcto

No añadir una entidad. Especificar contratos de \(G_\psi\) y \(H_\psi\):

- totalidad o parcialidad;
- determinismo, estocasticidad o multivaluación;
- condiciones de existencia/unicidad de punto fijo;
- regla de selección entre soluciones;
- observables y falsadores;
- relación exacta con `Coh`, \(\Phi^{(1)}\) y \(m_k\).

Solo después puede evaluarse si el canon responde efectivamente —no solo definicionalmente— a \(Q_{\text{transición}}\).
