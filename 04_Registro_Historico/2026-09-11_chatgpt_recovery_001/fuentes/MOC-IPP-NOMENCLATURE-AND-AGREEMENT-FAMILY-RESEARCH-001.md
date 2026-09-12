# MOC/iPP — Investigación de nomenclatura humano-formal y familia «acuerdo»

## Alcance y método

Informe externo de lectura, realizado sin alterar los repositorios ni ejecutar operaciones Git. La fuente normativa de MOC se leyó desde el worktree local incorporado de `MOC-CAN-ENM-001-R2.1`; su disponibilidad local no convierte por sí misma los borradores vecinos en canon. iPP se trata como frente práctico-documental cuyo documento base permanece congelado.

Jerarquía aplicada:

1. `MOC-AX-001` AX-16..AX-21 y `MOC-CANON-001`: autoridad humano-formal documentada.
2. Documentos `MOC-IPP-*`: estado documental y límites; las propuestas no desplazan el congelamiento de `MOC-IPP-001`.
3. `registro/`, `CHANGELOG.md`, `ROADMAP.md` y bitácoras: evidencia histórica, no autoridad normativa independiente.
4. ConcordIA y Concordante Lab: infraestructura, validación computacional o procedencia; no autoridad semántica.

### Nota de consistencia

`MOC-CANON-001` conserva en su lista inicial la frase histórica «AX-17 = TrueSelf como Phi_psi evaluador», pero su fórmula central y la formulación vigente de AX-17 establecen `TrueSelf_psi(t) ≡ G_psi(t)` y `Phi_psi` como operador distinto. Se registra como **CONTRADICTORIO** de redacción histórica dentro del acta, no como autorización para volver a identificar `G_psi`, `TrueSelf_psi` y `Phi_psi`.

## Parte I — Inventario humano-formal MOC

| Área | Nombre humano | Identificador formal | Definición breve documentada | Estado | Fuente exacta |
| --- | --- | --- | --- | --- | --- |
| Unidad situada | experiencia situada | `Omega_psi(t)` | Activación situada de la organización experiencial; la salida de los loops es nueva experiencia. | CANONIZADO | `psicologia/MOC-AX-001_Axiomas_Base.md`, AX-05, AX-19..21 |
| Molécula interna | Pentacoro / pentacoron experiencial | `Pi5_psi=<P_psi,Eaf_psi,Act_psi,V_psi,S_psi>` | Molécula experiencial de cinco átomos funcionales. | CANONIZADO | `psicologia/MOC-AX-001_Axiomas_Base.md`, AX-16 |
| Átomo funcional | patrón/posición | `P_psi` | Uno de los cinco átomos funcionales del pentacoro; no se aporta una glosa autónoma más precisa en las fuentes leídas. | CANONIZADO | `psicologia/MOC-AX-001_Axiomas_Base.md`, AX-16 |
| Átomo funcional | afecto/emoción | `Eaf_psi` | Átomo funcional del pentacoro. | CANONIZADO | `psicologia/MOC-AX-001_Axiomas_Base.md`, AX-16 |
| Átomo funcional | acción/no acción/pauta expresiva | `Act_psi` | Vértice interno de acción, no acción o pauta expresiva; no equivale a conducta exterior. | CANONIZADO | `psicologia/MOC-AX-001_Axiomas_Base.md`, AX-04 y AX-16 |
| Átomo funcional | valores/dirección | `V_psi` | Componente y canal directo de orientación; no define el centroide. | CANONIZADO | `psicologia/MOC-AX-001_Axiomas_Base.md`, AX-16 y AX-18 |
| Átomo funcional | situación/cuerpo/contexto/tiempo/espacio | `S_psi` | Átomo funcional situado; las fuentes no lo descomponen en una firma adicional única. | CANONIZADO | `psicologia/MOC-AX-001_Axiomas_Base.md`, AX-16; `MOC-GEO-001` |
| Conducta derivada | conducta o exteriorización | `B_psi` / `K_psi` | Expresión exteriorizada derivada; está explícitamente fuera de `Pi5_psi`. | CANONIZADO | `psicologia/MOC-AX-001_Axiomas_Base.md`, AX-04 y AX-16 |
| Representación formal | incrustación | `Z_psi(t):=embed_psi(Pi5_psi(t))` | Representación previa necesaria para usar centroide o tensión. | CANONIZADO | `psicologia/MOC-AX-001_Axiomas_Base.md`, AX-17 |
| Punto integrador | centroide | `G_psi(t):=centroid_psi(Z_psi(t))` | Centroide del pentacoro representado; no es un sexto átomo. | CANONIZADO | `psicologia/MOC-AX-001_Axiomas_Base.md`, AX-17 |
| Alias interpretativo | True Self local | `TrueSelf_psi(t)≡G_psi(t)` | Alias local de `G_psi`; no esencia metafísica ni operador evaluativo. | CANONIZADO | `psicologia/MOC-AX-001_Axiomas_Base.md`, AX-17 |
| Evaluación | operador evaluativo interno | `Phi_psi:M_psi×O_psi×K_phi→R_psi_v2` | Operador separado de `G_psi`/TrueSelf; reutiliza la tensión ya calculada y produce salida estructurada. | CANONIZADO | `psicologia/MOC-AX-001_Axiomas_Base.md`, AX-17 y AX-21 |
| Acoplamiento | descomposición/acoplamiento activo | `Xi_psi` | Componente del bucle activo, explícitamente distinto de TrueSelf. | CANONIZADO | `psicologia/MOC-AX-001_Axiomas_Base.md`, AX-17 y AX-21 |
| Tensión | tensión estructural | `Tau_psi(t):=tension_psi(Z_psi(t),G_psi(t))` | Tensión calculada desde representación y centroide; no tiene segunda fórmula vigente. | CANONIZADO | `psicologia/MOC-AX-001_Axiomas_Base.md`, AX-17 |
| Salida | resultado estructurado | `R_psi_v2` | Codominio vigente de `Phi_psi`; antecedente `R_psi_v1` sólo histórico. | APROBADO_EN_RAMA_LOCAL | `psicologia/MOC-CANON-001_Acta_Canonizacion_Pentacoron_Phi_Ejes.md`, fórmula central; commit local R2.1 documentado |
| Dictamen | proyección evaluativa | `dictamen_psi` | Proyección de la salida estructurada junto con tensión y retroalimentación. | APROBADO_EN_RAMA_LOCAL | `psicologia/MOC-CANON-001_Acta_Canonizacion_Pentacoron_Phi_Ejes.md`, loop activo |
| Retroalimentación | feedback basal | `Phi_feedback_psi` | Retroalimentación continua de la evaluación sobre la experiencia; no técnica deliberada por sí sola. | CANONIZADO | `psicologia/MOC-AX-001_Axiomas_Base.md`, AX-20 |
| Elección situada | poder elegir | `C_psi` | Elección desde dirección concordante; no controla resultados externos. | CANONIZADO | `psicologia/MOC-AX-001_Axiomas_Base.md`, AX-19 y AX-21 |
| Resultado relacional | concordancia | `Conc_psi` / concordancia | Alineación suficiente del prisma completo más `A_exp`; no consenso interpersonal ni resultado garantizado. | CANONIZADO | `psicologia/MOC-AX-001_Axiomas_Base.md`, AX-08 |
| Resultado relacional | fricción | fricción | Tensión, resistencia, ruido o contradicción que requiere lectura. | CANONIZADO | `psicologia/MOC-AX-001_Axiomas_Base.md`, AX-09 |
| Resultado relacional | discordancia | discordancia | Fricción estabilizada como desalineación relevante del prisma. | CANONIZADO | `psicologia/MOC-AX-001_Axiomas_Base.md`, AX-10 |
| Resultado relacional | disolución | disolución | Pérdida de unidad suficiente para describir configuración concordante, friccional o discordante. | CANONIZADO | `psicologia/MOC-AX-001_Axiomas_Base.md`, AX-11 |
| Cambio activo | reorganización | reorganización | Cambio activo en la experiencia; puede ser natural o provocado. | CANONIZADO | `psicologia/MOC-AX-001_Axiomas_Base.md`, AX-12 |
| Cambio basal | transformación | transformación | Cambio siempre presente; no equivale a mejora ni a resultado logrado. | CANONIZADO | `psicologia/MOC-AX-001_Axiomas_Base.md`, AX-13 |
| Eje basal | reorganización automática | `H_psi` | `Omega_psi + Pi5_psi + Phi_feedback_psi → Omega_psi'`; evaluación continua no deliberada. | CANONIZADO | `psicologia/MOC-AX-001_Axiomas_Base.md`, AX-20 |
| Eje activo | reorganización activa | `V_axis_psi` | Loop `Omega→Xi→Pi5→Phi→herramientas→C→ajuste→Omega'`. | CANONIZADO | `psicologia/MOC-AX-001_Axiomas_Base.md`, AX-21 |
| Herramienta | poder parar | `P_stop_psi` | Herramienta mínima del eje activo. | CANONIZADO | `psicologia/MOC-AX-001_Axiomas_Base.md`, AX-21 |
| Herramienta | poder evaluar | `P_eval_psi` | Herramienta mínima del eje activo. | CANONIZADO | `psicologia/MOC-AX-001_Axiomas_Base.md`, AX-21 |
| Herramienta | poder decidir concordantemente | `P_decide_psi` | Herramienta mínima del eje activo. | CANONIZADO | `psicologia/MOC-AX-001_Axiomas_Base.md`, AX-21 |
| Herramienta | soltar expectativas / sostener apertura | `P_aexp_psi` / `A_exp` | Apertura activa sin expectativa fija; condición necesaria local de concordancia. | CANONIZADO | `psicologia/MOC-AX-001_Axiomas_Base.md`, AX-08 y AX-21 |
| Geometría auxiliar | prisma/pirámide | `project_prism_psi` / proyección prismática | Proyección auxiliar: punta valores/dirección; base definición, emoción, conducta y encarnación situada. No es la geometría interna canónica. | CANONIZADO | `psicologia/MOC-AX-001_Axiomas_Base.md`, AX-03..04; `psicologia/MOC-GEO-001_Geometria_Prismatica_Tiempo_Espacio.md` |
| Geometría auxiliar | caras, punta | NO_DOCUMENTED como términos del pentacoro | «Punta» pertenece a la pirámide/prisma auxiliar. «Cara» no fue localizada como término formal del pentacoro. | NO_DOCUMENTADO | `psicologia/MOC-AX-001_Axiomas_Base.md`, AX-03..04 |
| Geometría auxiliar | tetra-nodo | NO_DOCUMENTED | No se localizó definición ni identificador formal vigente. | NO_DOCUMENTADO | Búsqueda documental del árbol R2.1 |
| Familia no impuesta | corazón / cor / cordis | NO_DOCUMENTED | No hay definición canónica ni identificador formal localizado; no se infiere por semejanza lingüística. | NO_DOCUMENTADO | Búsqueda documental del árbol R2.1 |

## Parte II — Inventario actual de iPP

| Elemento iPP | Nombre humano | Identificador o documento | Estado actual | Qué permite | Qué prohíbe | Fuente exacta |
| --- | --- | --- | --- | --- | --- | --- |
| Base iPP | Ingeniería Psicológica Práctica | `MOC-IPP-001` | HISTÓRICO / CONGELADO | Diseñar, seleccionar o secuenciar posibilidades de acción, percepción o reorganización dentro de la evaluación del prisma. | No garantiza resultado externo; no establece uso clínico, diagnóstico o terapia. | `psicologia/MOC-IPP-001_Ingenieria_Psicologica_Practica.md`, Estado y §§ Autorización práctica |
| Alcance documental | documentación iPP | `MOC-IPP-REACT-001` | BORRADOR | Preparar decisión auditable para sandbox documental y preclínico. | No reactiva iPP ni permite personas reales o atención clínica. | `psicologia/MOC-IPP-REACT-001_Propuesta_Reactivacion_Limitada_iPP.md`, Estado |
| Identificador solicitado | `IPP-DOC-REACT-001` | NO_DOCUMENTED | NO_DOCUMENTADO | Ninguno acreditado. El documento localizado es `MOC-IPP-REACT-001`, no el identificador solicitado. | No debe sustituirse por una supuesta identidad equivalente. | Inventario de `psicologia/` del worktree R2.1 |
| Sandbox | sandbox documental y preclínico | `MOC-DEC-IPP-001` | BORRADOR / INACTIVO | Sólo construir fichas y simulaciones si hubiera firma humana posterior. | No descongela iPP para personas reales; no clínica, tratamiento ni investigación con humanos. | `psicologia/MOC-DEC-IPP-001_Borrador_Decision_iPP_Sandbox.md`, Estado y alcance |
| Auditoría de precondiciones | Estado 1 / sandbox | `MOC-PRECOND-001` | APROBADO_EN_RAMA_LOCAL, no autorización de uso | Documentar preparación para decisión humana. | No aprueba Estado 1, no activa iPP, no abre investigación formal. | `psicologia/MOC-PRECOND-001_Auditoria_Precondiciones_Estado1_iPP.md`, Estado y dictamen |
| Procedimiento situado | posibilidad situada | `MOC-IPP-001` | HISTÓRICO / CONGELADO | Autoriza internamente posibilidad de práctica o reorganización; debe someterse a evaluación del prisma. | No causa externamente el resultado. | `psicologia/MOC-IPP-001_Ingenieria_Psicologica_Practica.md`, §§ Autorización práctica |
| Pausa | no intervención elegida | `P_stop_psi` y `MOC-IPP-REACT-001` | CANONIZADO para la herramienta; iPP operativo congelado | Parar como herramienta del loop activo. | No equivale a ausencia de elección. | `psicologia/MOC-AX-001_Axiomas_Base.md`, AX-21; `MOC-IPP-REACT-001`, prohibiciones |
| Dar/recibir | NO_DOCUMENTED | NO_DOCUMENTED | NO_DOCUMENTADO | No se encontró elemento iPP formal con ese nombre en las fuentes leídas. | No debe atribuirse un protocolo interpersonal a iPP. | Búsqueda documental del árbol R2.1 |
| Elección | elección situada | `C_psi` | CANONIZADO en MOC; no activa iPP | Elegir desde dirección concordante dentro del loop. | No controla exterior ni garantiza concordancia. | `psicologia/MOC-AX-001_Axiomas_Base.md`, AX-19 y AX-21 |
| Revisión del proceso | auditoría / precondiciones | `MOC-PRECOND-001` | APROBADO_EN_RAMA_LOCAL | Revisión documental y compuertas previas. | No reemplaza decisión humana ni revisión externa. | `psicologia/MOC-PRECOND-001_Auditoria_Precondiciones_Estado1_iPP.md` |
| Relación con Pi5 y loops | autorización dentro de evaluación | `MOC-IPP-001`, `MOC-AX-001` | MOC CANONIZADO; iPP CONGELADO | Vincula una posibilidad práctica con evaluación del prisma y elección. | No convierte iPP en operador que sustituya `Phi_psi`, `Xi_psi` o `C_psi`. | `psicologia/MOC-IPP-001_Ingenieria_Psicologica_Practica.md`; `MOC-AX-001`, AX-14 y AX-21 |

Lectura de estado requerida, respaldada por las fuentes:

```text
IPP_DOCUMENTARY_SCOPE=ACTIVE
IPP_OPERATIONAL_SCOPE=FROZEN
SANDBOX=INACTIVE
```

El primer valor significa que existen documentos y propuestas auditables; no implica ejecución. Los dos últimos se respaldan expresamente en `MOC-IPP-001`, `MOC-IPP-REACT-001`, `MOC-PRECOND-001` y `MOC-DEC-IPP-001`.

## Parte III — Familia «acordar / acuerdo / concordar / concordancia / discordancia»

### Cronología reconstruida

1. **Antecedentes históricos:** `registro/Revision_Historica_Modelo_Psicologico_Concordante.md` registra Concordancia como candidata a principio organizador o medida de ajuste; declara que no está probado que hubiera superado la etapa 3 de admisión.
2. **Formulación MOC:** `MOC-AX-001` AX-07..AX-10 convierte concordancia, fricción y discordancia en resultados relacionales de experiencia situada.
3. **Canon vigente:** AX-08 especifica concordancia como alineación suficiente del prisma completo + `A_exp`; AX-10 define discordancia como desalineación estabilizada. No los presenta como acuerdo entre personas.
4. **Uso histórico complementario:** `MOC-PHI-001` y `MOC-REPRO-001` usan «acuerdo entre evaluadores» en reproducción local. Es un uso procedimental distinto de `Conc_psi`.

| Término | Etimología o uso lingüístico documentado | Uso dentro del ecosistema | Estado | Riesgo de ambigüedad | Recomendación |
| --- | --- | --- | --- | --- | --- |
| acordar | NO_DOCUMENTED etimológicamente en las fuentes internas; aparece como verbo ordinario en documentación de acuerdos de alcance. | No tiene identificador MOC ni definición formal localizada. | NO_DOCUMENTADO | Alto: puede confundirse con consenso interpersonal o con `C_psi`. | No canonizar ni usar como sinónimo técnico sin definición separada. |
| acuerdo | Uso ordinario procedimental («acuerdo entre evaluadores» y acuerdos de alcance). | Reproducibilidad/decisiones documentales, no resultado relacional MOC. | HISTÓRICO / DOCUMENTAL | Alto si se iguala a concordancia. | Reservarlo para acuerdo explícito entre personas o evaluadores. |
| concordar | No se localizó entrada técnica autónoma. | Verbo derivado informal de «concordancia», sin firma formal. | NO_DOCUMENTADO | Medio-alto: puede sugerir acto entre agentes. | Evitarlo como nombre de operador. |
| concordancia | Uso interno definido como resultado relacional del patrón/experiencia; no consenso. | Condición relacional de alineación suficiente más `A_exp`; puede figurar como `Conc_psi`. | CANONIZADO | Medio: el español común puede sugerir acuerdo. | Usar «concordancia estructural/situada» cuando haya riesgo de lectura interpersonal. |
| discordancia | Uso interno definido formalmente por AX-10. | Fricción estabilizada como desalineación relevante del prisma. | CANONIZADO | Medio: puede moralizarse o confundirse con error. | Describirla como tensión/desalineación formal, no diagnóstico ni fallo moral. |

### Respuestas con evidencia

- **¿«acuerdo» equivale a «concordancia»?** No. «Acuerdo» aparece en usos procedimentales entre evaluadores; `concordancia` es una condición estructural/relacional de experiencia en AX-08.
- **¿«acordar» nombra una acción humana, una condición estructural o ambas?** En el material localizado sólo tiene uso humano/procedimental ordinario; no hay definición estructural formal. Resultado: **NO_DOCUMENTED** como término MOC.
- **¿«concordancia» puede presentarse como consenso entre personas?** No. El canon la define por alineación del prisma y `A_exp`, no por acuerdo interpersonal.
- **¿«discordancia» es diagnóstico, fallo moral o descripción formal de tensión?** Descripción formal de fricción estabilizada/desalineación relevante. No es diagnóstico ni juicio moral.
- **¿La familia «acordar/acuerdo» está aprobada, descartada o pendiente?** **PENDIENTE / NO_DOCUMENTADA** como familia técnica. Sólo `concordancia` y `discordancia` tienen definición canónica; ello no aprueba sus supuestos sinónimos.

## Límites de la investigación

- No se inventaron etimologías. No se usaron fuentes lingüísticas externas porque el informe resuelve el uso interno con las fuentes disponibles; por ello, la etimología de la familia queda **NO_DOCUMENTED**.
- No se trató «corazón», `cor`, `cordis`, «cara» o «tetra-nodo» como términos MOC sin definición localizada.
- No se elevó a autoridad normativa ningún archivo de registro, propuesta, expediente externo ni validación computacional.

```text
CANONICAL_TERM_COUNT=29
APPROVED_LOCAL_BRANCH_TERM_COUNT=3
DRAFT_TERM_COUNT=4
HISTORICAL_TERM_COUNT=4
NO_DOCUMENTED_TERM_COUNT=6
CONTRADICTION_COUNT=1
AGREEMENT_FAMILY_STATUS=PENDIENTE_NO_DOCUMENTADA_COMO_FAMILIA_TECNICA
REPOSITORIES_MODIFIED=NO
GIT_OPERATION_EXECUTED=NO
```

El informe recupera nombres y estados documentados sin crear autoridad nueva. MOC conserva la autoridad humano-formal; iPP permanece activo sólo en alcance documental; ConcordIA no recibió autoridad semántica.