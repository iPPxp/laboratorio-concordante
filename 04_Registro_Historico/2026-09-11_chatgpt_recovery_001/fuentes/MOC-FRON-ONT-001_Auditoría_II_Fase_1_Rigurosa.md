# MOC-FRON-ONT-001: Auditoría II Fase 1 Rigurosa

**Estatus:** Auditoría adversarial. Sin compromiso con conclusión previa.  
**Fecha:** 5 de agosto de 2026.  
**Criterio central:** Invariancia informacional, no eliminabilidad sintáctica.

---

## 0. PRELIMINARES: Definiciones sin presunción de tercero

### 0.1 Diferencia simple

**[DEF]** Una diferencia simple es un predicado binario:
```
diff(x, y) := x ≠ y
```
bajo una relación de igualdad (identidad total, isomorfismo, equivalencia bajo R, etc.).

**Propiedades:**
- Binario: envuelve exactamente dos términos.
- Proposicional: verdadero/falso en contexto.
- **Sin estructura:** no especifica naturaleza ni regulación de la diferencia.

---

### 0.2 Distinción

**[DEF]** Una distinción es un predicado ternario enriquecido:
```
Dist(x, y, C) := ⟨x ≠ y respecto de criterio C⟩
```
donde C es un criterio: conjunto de propiedades, regla, relación o función proposicional que especifica respecto de qué x e y son diferentes.

**Propiedades:**
- Ternaria en estructura.
- Especifica **eje de diferencia** (el criterio C).
- Aún sin describir **regulación del acoplamiento**.

**Ejemplo:**
- `diff(rojo, azul)` = ambos son colores; no idénticos.
- `Dist(rojo, azul, color)` = "difieren en la propiedad cromática".
- Sin especificar cómo rojo y azul **interactúan** o **se acoplan** si ambos están presentes.

---

### 0.3 Organización (sin presuponer ρ)

**[DEF]** Una organización de dos términos es un sistema donde:
1. x e y son distinguibles (al menos bajo algún criterio C).
2. x e y **no son independientes**: sus estados o transiciones están acoplados.
3. El acoplamiento admite **descripción estructural**: hay reglas o restricciones que gobiernan cómo uno afecta al otro.

**Notas:**
- Esta definición **no presupone** la forma o existencia de esa estructura relacional.
- Solo afirma que existe *alguna* regulación entre x e y.

---

## 1. RELACIÓN DE TRANSICIÓN COMO DEFINICIÓN BASE

### 1.1 Motivación

En MOC, la organización central es una **transición** `V_k ↦ R_k` mediada por componentes internos I, E, A bajo condiciones C.

**Pregunta:** ¿Qué estructura mínima especifica esta transición sin presuponer la forma de la mediación?

**Respuesta:** Una relación de transición admisible.

---

### 1.2 Definición formal: relación de transición

**[DEF — Tipo base]:**
```
ℱ_ψ,C ⊆ 𝒱 × ℐ × ℰ × 𝒜 × ℛ
```

Donde:
- 𝒱 = espacio de entradas (estados V_k)
- ℐ = espacio de interpretaciones
- ℰ = espacio de emociones (modalidades E_m,k)
- 𝒜 = espacio de acciones
- ℛ = espacio de resultados (estados R_k)
- ψ = índice de agente/contexto
- C = criterio de organización

**Interpretación:** ℱ_ψ,C especifica exactamente qué quíntuples (V, I, E, A, R) son **configuraciones admisibles** bajo el régimen ψ y criterio C.

---

### 1.3 Fibra como especificación de transición

Para cada V ∈ 𝒱 fijado, definimos:

```
ℱ_ψ,C(V) := {(I, E, A, R) : (V, I, E, A, R) ∈ ℱ_ψ,C}
```

**Interpretación:** La fibra `ℱ_ψ,C(V)` especifica, para entrada V, todas las configuraciones (I, E, A, R) compatibles.

**Propiedades:**
- Si `ℱ_ψ,C(V)` es un singleton, la transición es **determinista**.
- Si `ℱ_ψ,C(V)` tiene múltiples elementos, es **no-determinista** o **subdeterminada** (varias salidas R posibles para el mismo V bajo diferentes IEA).
- Si `ℱ_ψ,C(V) = ∅`, la entrada V no admite salida bajo ψ, C (transición bloqueada).

---

### 1.4 IEA como trayectoria, no frontera

**[DEF — Rechazo de decreto]:** No declaramos ⟨I, E, A⟩ = "la frontera" por mera etiquetación.

**[DEF — Realización interna]:** Una configuración (I_k, E_k, A_k) ∈ ℐ × ℰ × 𝒜 es una **trayectoria interna** de la transición V_k ↦ R_k si existe un par (V_k, R_k) tal que:
```
(V_k, I_k, E_k, A_k, R_k) ∈ ℱ_ψ,C
```

Es decir, (I,E,A) es una de las configuraciones admisibles que conectan V con R.

**Nota crucial:** La relación ℱ_ψ,C **no es** reducible a una función `f: 𝒱 → ℛ` (que ignoraría IEA). Tampoco es reducible a IEA aislado (que ignoraría V, R). Es una relación sobre todo el producto 𝒱 × ℐ × ℰ × 𝒜 × ℛ.

---

## 2. INFORMACIÓN CODIFICADA POR ℱ_ψ,C

### 2.1 Información anidada en la relación

**[TEO]** La relación ℱ_ψ,C codifica información que **no está disponible** en los términos aislados V, I, E, A, R.

**Prueba por casos:**

**Caso 1: Compatibilidad**
- El conjunto V × ℐ × ℰ × 𝒜 × ℛ (producto cartesiano completo) contiene todas las combinaciones posibles.
- ℱ_ψ,C ⊆ (ese producto) es un subconjunto **propio** (generalmente).
- La información "cuáles combinaciones son compatibles" no se sigue de los espacios individuales.

**Caso 2: Restricciones**
- Si decimos "I y A no pueden coexistir en ciertos estados bajo criterio C", esa regla **no está codificada** en I ni en A aisladamente.
- Solo ℱ_ψ,C codifica esa restricción (excluyendo ciertos (V, I, E, A, R) del conjunto).

**Caso 3: Dependencia contextual**
- Si R depende no solo de V, sino del acoplamiento específico de (I, E, A), entonces **representar solo V → R perdería información**.
- Ejemplo: R₁ y R₂ pueden ser producidos por el mismo V bajo diferentes (I, E, A). Eso es información en ℱ_ψ,C que falta en una función `f: V ↦ R`.

**Conclusión:** ℱ_ψ,C codifica compatibilidad, restricciones y contexto-dependencia que los términos aislados no contienen. ✓

---

### 2.2 Información contenida en ℱ vs. en términos aislados

**Definición:** Decimos que una representación R₁ es **informativamente completa** respecto de R₂ si toda información contenida en R₂ puede extraerse de R₁ sin pérdida.

**Pregunta:** ¿Es la estructura ℱ_ψ,C informativamente completa respecto de V, I, E, A, R aislados?

**Respuesta (provisional):** No necesariamente.

Ejemplo:
- ℱ_ψ,C especifica compatibilidad.
- Pero **no especifica** por qué esa compatibilidad existe (mecanismo causal, propósito, historia).
- Los términos aislados (V, I, E, A, R como espacios abstractos) tampoco lo especifican.

Por tanto: la completitud informacional es **parcial en ambos casos**, pero **diferente**:
- V, I, E, A, R aislados cuentan qué puede ocurrir en cada aspecto.
- ℱ_ψ,C especifica qué **puede ocurrir conjuntamente**.

Son complementarios, no redundantes.

**[Conclusión]:** La información en ℱ_ψ,C **no está contenida sin residuo** en los términos aislados. ✓

---

## 3. INVARIANCIA INFORMACIONAL: Criterio de necesidad estructural

### 3.1 Definición de invariancia

**[DEF]** Una información I es **invariante bajo recodificación** si, cuando se reexpresa en otro lenguaje formal, la información **no se desplaza a un nivel metalógico** o **no se pierde**.

**[DEF]** Decimos que ℱ_ψ,C es **informativamente irreducible** si toda recodificación de su contenido requiere conservar estructura relacional (aunque no sea explícitamente un símbolo separado llamado ρ o ℱ).

---

### 3.2 Recodificaciones posibles

**Recodificación 1: Enriquecimiento de estados**

Definir estados enriquecidos:
```
x' := (x, ρ_C(x, y))
```

Entonces, un diagrama `x' → y'` podría contener la información de relación.

**Análisis:**
- Formalmente, la información se **trasladó**, no se eliminó.
- Pero ahora `x'` es más complejo; contiene como componente ρ_C.
- La información sigue existiendo en la estructura, solo reembalada.

**Conclusión sobre R1:** Recodificación sintácticamente válida, pero **la información relacional no desaparece**; se absorbe en la definición de x'. El "costo" es aumentar la complejidad de los estados.

---

**Recodificación 2: Función con memoria**

Definir una función `f: (𝒱 × 𝒮) → 𝒮` donde 𝒮 es un espacio de "memoria de contexto":
```
(R, S') = f(V, S)
```

Donde S codifica información sobre restricciones y acoplamiento.

**Análisis:**
- La información de ℱ_ψ,C se absorbe en la dinámica de S.
- Pero nuevamente: se trasladó, no se eliminó.
- La estructura relacional reaparece en la regla de transición S → S'.

**Conclusión sobre R2:** Recodificación válida, pero traslada la carga relacional a otro objeto (S). Requiere especificar S explícitamente.

---

**Recodificación 3: Operador distribuido**

Definir un operador Ψ que capte la transición completa:
```
R = Ψ(V, C)
```

donde Ψ encapsula toda la lógica relacional.

**Análisis:**
- Formalmente, Ψ es un símbolo único.
- Pero Ψ debe estar **definido en términos de** las restricciones que antes especificaba ℱ_ψ,C.
- La estructura relacional se esconde en la caja negra Ψ.

**Conclusión sobre R3:** El símbolo ℱ desaparece notacionalmente, pero su contenido informacional se requiere para definir Ψ. No es verdadera eliminación.

---

### 3.3 Prueba de invariancia informacional

**[TEO]** En toda recodificación formal equivalente de una organización de V, I, E, A, R:

1. **La información de compatibilidad/restricción debe conservarse en algún lugar del modelo.**
2. **Ese lugar es estructuralmente análogo a una relación, incluso si no se etiqueta como tal.**
3. **Por tanto, ℱ_ψ,C (o algo isomorfo) es informativamente irreducible.**

**Prueba informal:**

Supongamos que pudiera eliminarse toda mención de restricción relacional del modelo. Entonces:
- Cada transición V_k ↦ R_k sería **completamente determinada** por V_k y parámetros globales.
- No habría lugar para múltiples (I, E, A) compatibles con un mismo (V, R).
- No habría **variabilidad interna**.

Pero en MOC:
- Hay múltiples caminos internos de V a R (múltiples configuraciones IEA).
- Algunos (I, E, A) son compatibles; otros, no.
- Esta estructuración **exige una descripción relacional**.

Por tanto: **la información relacional no puede eliminarse sin perder la descripción de variabilidad interna.**

**[Conclusión]:** ℱ_ψ,C (o su equivalente formal) es **necesaria descriptivamente** para captar organizaciones no-triviales. ✓

---

## 4. DISTINCIONES DE NECESIDAD

### 4.1 Necesidad descriptiva

**[DEF]** Una estructura S es **descriptivamente necesaria** si, para describir un fenómeno P de forma completa, debe representarse S explícitamente (o su equivalente isomorfo).

**Ejemplo:** Para describir transiciones V_k ↦ R_k con variabilidad interna (múltiples IEA), es descriptivamente necesario representar restricciones de compatibilidad. De ahí: ℱ_ψ,C.

**Estatus:** Probado matemáticamente (sección 3).

---

### 4.2 Necesidad estructural

**[DEF]** Una estructura S es **estructuralmente necesaria** si, en el modelo formal de MOC, S debe estar presente (no solo como equivalencia lógica, sino como componente del esquema operativo).

**Ejemplo:** ¿Debe ℱ_ψ,C estar presente como un operador explícito en pentacoro, o puede quedar implícita en la definición de otros operadores (G_ψ, H_ψ)?

**Análisis:**

En el canon pentacoro:
```
Z_k = G_ψ(V_k, C_k)  [genera tríada]
R_k = H_ψ(V_k, Z_k, C_k)  [genera resultado]
```

¿Están ℱ_ψ,C implícitas en G_ψ y H_ψ?

- Si H_ψ contiene la lógica completa de restricciones, entonces ℱ_ψ,C es **computable desde H_ψ**, no adicional.
- Si H_ψ es un "agujero negro" que no especifica restricciones, entonces ℱ_ψ,C es **independiente** y estructuralmente necesaria.

**Conclusión:** La necesidad estructural **depende de la especificación de G_ψ y H_ψ en MOC.** No se deduce solo de la matemática.

**Estatus:** Indeterminado sin ampliar definiciones canónicas. [INDETERMINADO]

---

### 4.3 Necesidad ontológica

**[DEF]** Una estructura S es **ontológicamente necesaria** si existe en la realidad de la experiencia (no solo en el modelo formal de ella).

**Ejemplo:** ¿Existen realmente restricciones de compatibilidad entre (I, E, A) en la experiencia psicológica, o son solo artefactos de nuestro modelado?

**Análisis:**

La respuesta exige una **premisa-puente** que conecte modelo formal con ontología. Algunas opciones:

1. **Realismo estructuralista:** Si una estructura es formalmente necesaria para el modelo, entonces es ontológicamente real.  
   → Bajo esta premisa: ℱ_ψ,C es real.

2. **Instrumentalismo:** El modelo es una herramienta; solo los términos primitivos (V, I, E, A, R como energía psicológica, procesos neurales, etc.) son ontológicamente reales.  
   → Bajo esta premisa: ℱ_ψ,C es convención de representación, no entidad.

3. **Pluralismo:** Existen diferentes niveles de realidad (fenomenológica, neurocognitiva, comportamental); estructuras pueden ser reales en unos niveles pero no otros.  
   → Bajo esta premisa: ℱ_ψ,C es real en el nivel de **organización relacional**, no en el nivel de sustancia.

**Conclusión:** La necesidad ontológica **depende de una premisa metafísica sobre MOC que aún no está explicitada en axiomas.**

**Estatus:** Indeterminado sin decisión ontológica. [INDETERMINADO]

---

## 5. SEPARACIÓN RIGUROSA DE CONCLUSIONES

### 5.1 Lo que la matemática **demuestra**

```
✓ ℱ_ψ,C codifica información no disponible en términos aislados.
✓ Toda recodificación equivalente requiere conservar información relacional.
✓ ℱ_ψ,C es descriptivamente necesaria para fenómenos con variabilidad interna.
✓ Un "tercer término formal" (relación, restricción, operador) es requerido en la descripción.
```

**Clasificación:** Necesidad descriptiva. [TEO]

---

### 5.2 Lo que **depende del modelo MOC**

```
? ℱ_ψ,C es estructuralmente independiente de G_ψ, H_ψ (o está contenida en ellos).
? El pentacoro debe especificar ℱ_ψ,C explícitamente (o puede dejarla implícita).
? IEA realiza ℱ_ψ,C o solo es una descripción analítica post-hoc.
```

**Clasificación:** Necesidad estructural. [INDETERMINADO]

---

### 5.3 Lo que **requiere premisa ontológica**

```
? ℱ_ψ,C existe en la realidad psicológica (no solo en el modelo).
? La compatibilidad es una característica del sistema psicológico (no solo de nuestra descripción).
? Hablar de "frontera" es legítimo ontológicamente (o es solo metáfora de modelado).
```

**Clasificación:** Necesidad ontológica. [INDETERMINADO sin premisa-puente]

---

## 6. EL PROBLEMA DE IEA REDEFINIDO

### 6.1 Lo que **no podemos afirmar** (sin riesgo de circularidad)

❌ "IEA es la frontera entre V y R" (por definición de frontera: no demostrado).

❌ "IEA media la transición" (por definición de mediación: no demostrado).

❌ "IEA constituye el tercer término" (por definición de tercer término: no demostrado).

---

### 6.2 Lo que **sí podemos afirmar**

✓ (I_k, E_m,k, A_k) son componentes internos cuyas configuraciones conjuntas especifican qué resultado R es compatible con entrada V.

✓ La multiplicidad de (I,E,A) compatibles con (V,R) es información que debe representarse: es decir, ℱ_ψ,C.

✓ Esta información relacional es **descripitivamente necesaria** aunque sea redundante formalmente (puede recodificarse).

---

### 6.3 IEA como fibra o trayectoria

**[DEF revisada]** Dado (V_k, R_k), una configuración (I_k, E_k, A_k) es **una realización interna posible** si:

```
(V_k, I_k, E_k, A_k, R_k) ∈ ℱ_ψ,C
```

Múltiples realizaciones pueden coexistir:
```
ℱ_ψ,C(V_k, R_k) := {(I, E, A) : (V_k, I, E, A, R_k) ∈ ℱ_ψ,C}
```

**[Interpretación]:**
- No una única "interfaz" IEA predeterminada.
- Un espacio de interfaces admisibles.
- Bajo concordancia: el sistema opera sin especificar cuál (psicológicamente invisible).
- Bajo discordancia: Φ_ψ^{(1)} examina cuáles están actualizadas.

---

## 7. CONCLUSIÓN ABIERTA

### 7.1 Resultado de Fase 1 Rigurosa

**[TEO] Necesidad descriptiva:**
```
Una organización V ↦ R con variabilidad interna (múltiples IEA)
exige una descripción relacional ℱ_ψ,C que especifique compatibilidades.
```

**Estatus:** Probado. Clasificación: [TEO] matemático.

---

**[INDETERMINADO] Necesidad estructural:**
```
¿Debe ℱ_ψ,C ser un componente explícito del canon MOC,
o está implícita en la definición de operadores existentes?
```

**Condición para resolver:**
- Especificación rigurosa de dominio y codominio de G_ψ, H_ψ en el pentacoro.
- Verificación de si esos operadores especifican restricciones de compatibilidad.

---

**[INDETERMINADO] Necesidad ontológica:**
```
¿Existe realmente una estructura relacional de compatibilidad
en la experiencia psicológica, o es un artefacto de modelado?
```

**Condición para resolver:**
- Decisión explícita sobre premisa-puente: realismo estructuralista, instrumentalismo u otra.
- Esa decisión va más allá de la auditoría matemática; es decisión ontológica de MOC.

---

### 7.2 ¿Puede concluirse que la tesis fuerte es falsa?

**Sí, bajo ciertos supuestos:**

Si se demuestra que:
1. G_ψ y H_ψ ya especifican completamente las restricciones de compatibilidad.
2. No hay información adicional en una ℱ_ψ,C explícita.
3. Toda recodificación que incluye ℱ es redundante respecto del pentacoro.

Entonces: **El "tercer término formal" no es necesario; es computable desde operadores existentes.**

**Esa conclusión no se rechaza a priori.** La auditoría adversarial debe permitir su posibilidad.

---

### 7.3 Recomendación para Fase 2

Antes de construir el cubo (que presupone la necesidad de ℱ_ψ,C), se debe:

1. **Auditar los operadores canónicos** (G_ψ, H_ψ, Φ_ψ^{(0)}, Φ_ψ^{(1)}).
   - ¿Especifican explícitamente restricciones de compatibilidad?
   - ¿O hay un vacío que ℱ_ψ,C debe llenar?

2. **Si hay un vacío:** ℱ_ψ,C es estructuralmente necesaria. Proceder a cubo.

3. **Si no hay vacío:** Rechazar la hipótesis del "tercer término formal". Auditoría concluye: "La tesis fuerte es falsa".

---

## Cierre

**Resultado de Auditoría II Fase 1 Rigurosa:**

| Tesis | Estatus | Clasificación |
|-------|---------|---------------|
| Necesidad descriptiva de relación | ✓ Probada | [TEO] |
| Necesidad estructural en MOC | ? Indeterminada | [INDETERMINADO] |
| Necesidad ontológica en experiencia | ? Indeterminada | [INDETERMINADO] |
| Tesis fuerte (tercer término en todo) | ? Falsable | [CONJ] bajo evaluación |

**Siguiente paso:** Auditar operadores canónicos para decidir si hay vacío que llenar.
