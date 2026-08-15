# F0.2 — Baseline de autoridad semántica MOC

```text
ARTIFACT_ROLE = AUTHORITY_AUDIT_ONLY
SEMANTIC_AUTHORITY = MOC
COMPUTATIONAL_AUTHORITY = VALIDATION_ONLY
CANONICAL_STATUS_CHANGE = NOT_AUTHORIZED
MODEL_TRAINING_EXECUTED = NO
MOC_FACTORIZATION_VALIDATION = NOT_TESTED
```

## Dictamen ejecutivo

La autoridad MOC vigente sí fija que el Pentacoro está compuesto por cinco átomos funcionales:

```text
Pi5_psi = <P_psi, Eaf_psi, Act_psi, V_psi, S_psi>
```

También proporciona una semántica nominal mínima y algunos límites negativos. Sin embargo, las fuentes no contienen criterios observacionales completos para decidir, desde una narración, `PRESENT`, `ABSENT`, `AMBIGUOUS` o `UNKNOWN`, ni para separar `presence` de `change`. Tampoco cierran las fronteras instrumentales exigidas por F0.2.

Por tanto:

```text
P   = SEMANTIC_DEFINITION_INSUFFICIENT
Eaf = SEMANTIC_DEFINITION_INSUFFICIENT
Act = SEMANTIC_DEFINITION_INSUFFICIENT
V   = SEMANTIC_DEFINITION_INSUFFICIENT
S   = SEMANTIC_DEFINITION_INSUFFICIENT

SEMANTIC_BASELINE_LOCATED = YES
INSTRUMENTAL_OPERATIONALIZATION_READY = NO
G0_MANUAL_CALIBRATION_AUTHORIZED = NO
G1_SEMANTIC_IDENTIFIABILITY_AUTHORIZED = NO
G2_DATASET_READINESS_AUTHORIZED = NO
```

Este resultado no niega la arquitectura MOC ni redefine sus componentes. Indica solamente que el significado autorizado aún no basta para construir un instrumento narrativo reproducible sin añadir decisiones semánticas nuevas.

## Alcance y límites de acceso

Se auditó la cadena de autoridad y las fuentes MOC primarias pertinentes. No se leyeron F0 o F0.1, sus anotaciones, outcomes, world states ni resultados. No se consultaron artefactos generados por este programa como fuente de autoridad. No se generaron ejemplos y no se evaluó ningún artefacto propio.

No se encontró un `AGENTS.md` aplicable en la raíz del workspace ni en los niveles ascendentes inspeccionados; tampoco en la raíz o carpeta `psicologia` del repositorio MOC v1.5.2.

## Regla de autoridad aplicada

`INDEX.md` del Laboratorio Concordante fija, en caso de conflicto:

1. Canon.
2. Estado del proyecto.
3. Documentos oficiales.
4. Decisiones registradas.
5. Expedientes.
6. Automatización y reportes como evidencia operativa, no como autoridad superior.
7. Registro histórico.

`M-000` prohíbe la promoción automática y obliga a tratar como deuda conceptual toda dependencia no registrada. `M-001` exige identificar fuentes, estatus, dependencias, deudas y superficies afectadas.

La cadena local de Concordante Lab no define por sí sola la semántica del Pentacoro:

- `01_Canon/LAB-RESEARCH-PROVENANCE-001_Corpus_Canonico.md` canoniza identidad y procedencia de otro corpus, pero declara `MOC_SEMANTIC_AUTHORITY_GRANTED_BY_THIS_RECORD=NO`.
- `CURRENT_STATE.md` y `05_Estado_Proyecto/ESTADO_ACTUAL.md` mantienen el expediente local `MOC-001` como no canónico, no clínico y sin ejecución empírica. Sus automatizaciones no pueden fijar significado.
- La candidata aislada de investigación declarada por `README.md` e `INDEX.md` no concede autoridad semántica MOC.

La semántica MOC se toma de la fuente primaria materializada en `C:\Users\IximM\OneDrive\Documentos\v.1.5.2`, porque su arquitectura de autoridad declara:

```text
CANONICAL_AUTHORITY = MOC
FORMAL_VALIDATION_AUTHORITY = CONCORDIA_WITHOUT_SEMANTIC_AUTHORITY
```

`MOC-ARCH-AUTH-001` asigna a MOC significado, canon y límites psicológicos; a ConcordIA le asigna comprobación formal sin autoridad semántica; y al Lab, custodia y procedencia. Ésta es la base de:

```text
SEMANTIC_AUTHORITY = MOC
COMPUTATIONAL_AUTHORITY = VALIDATION_ONLY
```

## Fuentes primarias exactas y estatus

### Gobierno del repositorio receptor

| Fuente | Estatus o función | SHA-256 |
|---|---|---|
| `README.md` | orientación vigente del Laboratorio; no define P/Eaf/Act/V/S | `64e4c9c83d477a0a297c625b65a7ba8745d7eff0523adc85e226189691acf3eb` |
| `INDEX.md` | mapa de lectura y jerarquía de autoridad | `bc3aa3149d316e8465bd167b33d91bc5485a490d9b73569eac435b8096d25107` |
| `CURRENT_STATE.md` | estado operativo vigente; MOC local sin promoción semántica | `84fdc65b1c714c4cddd3868b8740875a5ec0c4f9a4c7b702b53c8900809218c4` |
| `05_Estado_Proyecto/ESTADO_ACTUAL.md` | estado operativo detallado | `6a04638e44a65501a3097c1e23426271f2543735f867a95fd9486964ae71f46f` |
| `01_Canon/M-000_Reglas_Fundamentales.md` | Canon de gobierno: niveles, estatus, no promoción, deuda | `7ca53a0e370913ed60e65a7b78c25c0a43758b2455b63fd3151141bb43a31db2` |
| `01_Canon/M-001_Auditoria_Arquitectonica.md` | Canon de auditoría y matriz de superficies | `51f718061bd638565f59ba5d8ca5774c635aaf776b8778ef0f961b9876e3a59c` |
| `01_Canon/LAB-RESEARCH-PROVENANCE-001_Corpus_Canonico.md` | registro de identidad/procedencia; niega conceder autoridad semántica MOC | `41f811863d7eff0b2f23e17ef0510bc261fd3313d790e74df600a1a1230793cc` |

### Autoridad MOC primaria

| Fuente absoluta | Estatus declarado o confirmado | Uso autorizado aquí | SHA-256 |
|---|---|---|---|
| `C:\Users\IximM\OneDrive\Documentos\v.1.5.2\README.md` | estado v1.5.2; identifica `MOC-AX-001` como canon MOC actual y `MOC-CANON-001` como acta canónica | ruta de entrada y estatus | `287464c252c28997573c16113d80a5b5cbb09f543a4fa45b3b1ae0259bd5a50e` |
| `C:\Users\IximM\OneDrive\Documentos\v.1.5.2\ESTADO_ACTUAL.md` | estado operativo; confirma AX-16..AX-21 como canon vigente y la deuda de migración de conducta | verificación de vigencia y deuda | `35dbf21c4a6dba3424db3e190a13222343c32ee6f571733557bd9338a9020da3` |
| `C:\Users\IximM\OneDrive\Documentos\v.1.5.2\psicologia\MOC-ARCH-AUTH-001_MOC_iPP_ConcordIA_Lab_v3.md` | `CANONICAL_STATUS=ACCEPTED_AND_INCORPORATED_IN_LOCAL_ISOLATED_COMMIT`; publicación local | contrato de autoridad | `016aabf93c40573dec72da84ae533404812744c0fb5b2bcbb68fffc309b41d24` |
| `C:\Users\IximM\OneDrive\Documentos\v.1.5.2\psicologia\MOC-CANON-001_Acta_Canonizacion_Pentacoron_Phi_Ejes.md` | acta canónica formulada; AX-16..AX-21 canonizados | identidad del Pentacoro y límites canónicos | `d2d369b8bc48f467c1eda1bcff0ba9c612369bc7a01bc059b9df4711e177357d` |
| `C:\Users\IximM\OneDrive\Documentos\v.1.5.2\psicologia\MOC-AX-001_Axiomas_Base.md` | base axiomática; el estado/README la identifican como canon MOC vigente | AX-16 y distinción Act/conducta | `ad4ce582d9fe7316c604e964250bd496fb62ce1b8bff3257035e94ec5511fc05` |
| `C:\Users\IximM\OneDrive\Documentos\v.1.5.2\psicologia\MOC-CAN-AX-001_Evaluacion_Canonizacion_Axiomas_Pentacoron.md` | evaluación formal integrada en `MOC-AX-001` con enmiendas | glosa tipada más precisa y deuda explícita | `e2285c53de6a8a76be8ad045d4b6a84944ee44dbd2c1a00ca99424ba8780fe20` |
| `C:\Users\IximM\OneDrive\Documentos\v.1.5.2\psicologia\MOC-PENT-001_Pentacoron_Centroide_Oscilacion.md` | hipótesis formal canonizada con enmiendas por `MOC-CANON-001` | semántica nominal de los cinco vértices | `26d94a3ad8ae0d263a86713bc4c3e54ef5de080fdb200f65cab993f9f4192128` |

### Elaboraciones MOC subordinadas

Estas fuentes amplían el vocabulario, pero sus propios estados son `Componente inicial formulado` o `Taxonomía inicial formulada`; no pueden corregir ni ampliar el canon por sí solas.

| Fuente | Aporte | SHA-256 |
|---|---|---|
| `...\psicologia\MOC-DPSI-001_Definicion_Prismatica.md` | significado/interpretación bajo el símbolo histórico `D_psi` | `c102d652a3bbb794e9804d054d46c76d0b4647beced67371ac90e83e9a81c503` |
| `...\psicologia\MOC-EPSI-001_Emocion_Prismatica.md` | respuesta afectiva situada bajo `E_af` | `f228d85e495318464b39b2ecca2184188c410fba27fe1c7addb3a3c0a70e508e` |
| `...\psicologia\MOC-CON-001_Conducta_Prismatica.md` | nota canónica que separa `Act_psi` interno de `B_psi/K_psi` exteriorizado | `34430c7614a9ce6dfac51bd9832f5983fbce61121beca4147fbe70006cbc9116` |
| `...\psicologia\MOC-VPSI-001_Valores_Direccion_Prismatica.md` | valores/dirección y restricciones frente a preferencia inmediata | `e47e089d7677f570359ea58933dc9f4d59faaf76faffccd8de8a9dfcb440596e` |
| `...\psicologia\MOC-ENC-001_Taxonomia_Encarnacion_Situada.md` | cuerpo, tiempo, recursos, límites, entorno y posibilidad percibida | `7a06e4afb13b96f390b1be8ff67676202150ef38898547e46f0ff7871f15d83c` |

El prefijo `...` de esta tabla significa exactamente `C:\Users\IximM\OneDrive\Documentos\v.1.5.2`.

## Definiciones autorizadas y dictamen por componente

### P — `P_psi`

Semántica autorizada mínima:

```text
P_psi = pensamiento / definición / interpretación
```

La elaboración subordinada `MOC-DPSI-001` describe un integrador activo de significado e interpretación, que puede expresarse como definición, creencia, expectativa, regla o lectura activa.

Insuficiencias bloqueantes:

- el canon no fija la relación de identidad o migración entre `P_psi` y el símbolo subordinado `D_psi`;
- no establece qué evidencia narrativa basta para atribuir pensamiento, definición o interpretación al sujeto objetivo;
- no separa operacionalmente interpretación/evaluación P de criterio/dirección V;
- no define negativos P-like, evidencia implícita, alcance de citas o atribuciones a terceros;
- no distingue reglas de presencia frente a reglas de cambio o estabilidad.

```text
P = SEMANTIC_DEFINITION_INSUFFICIENT
```

### Eaf — `Eaf_psi`

Semántica autorizada mínima:

```text
Eaf_psi = emoción-afecto situado
```

La elaboración subordinada `MOC-EPSI-001` usa `E_af` para la respuesta afectiva situada e insiste en que informa la relación activa, pero no decide significado, acción, verdad ni valor.

Insuficiencias bloqueantes:

- el canon no fija explícitamente la relación entre `Eaf_psi` y la notación subordinada `E_af`;
- no define cómo observar Eaf implícito sin vocabulario afectivo;
- no define el rechazo de vocabulario afectivo referido a otra persona, citado o usado como señuelo;
- no separa de forma instrumental afecto, disposición, activación corporal S y dirección V;
- no ofrece reglas de presencia, ausencia, estabilidad y cambio independientes.

```text
Eaf = SEMANTIC_DEFINITION_INSUFFICIENT
```

### Act — `Act_psi`

Semántica autorizada mínima, con la enmienda canónica más restrictiva:

```text
Act_psi = acción / no acción / pauta expresiva interna o actual
B_psi o K_psi = conducta derivada / expresión exteriorizada
B_psi notin Pi5_psi
```

Insuficiencias bloqueantes:

- “acción / no acción / pauta expresiva” no constituye todavía un criterio observacional para un modo interno narrado;
- no se fija qué hace positiva a Act cuando sólo hay disponibilidad, ensayo, impulso, inhibición, omisión o acción posible;
- no se cierra la frontera entre `Act_psi`, `C_psi/PODER_ELEGIR` y `B_psi/K_psi`;
- `MOC-CAN-AX-001` y `ESTADO_ACTUAL.md` registran como deuda pendiente la migración documental completa de conducta derivada;
- no existen reglas separadas de presencia y cambio.

```text
Act = SEMANTIC_DEFINITION_INSUFFICIENT
```

### V — `V_psi`

Semántica autorizada mínima:

```text
V_psi = valores / dirección / criterio orientador
V_psi = lo que importa sostener en esta experiencia
```

MOC establece que V orienta, no ocupa el centroide, no define `G_psi`, no decide por la persona y no obliga a elegir lo preferido. `MOC-VPSI-001` incluye “preferencia profunda” dentro de su formulación inicial, pero distingue esa dirección de la preferencia inmediata.

Insuficiencias bloqueantes:

- no existe umbral operacional autorizado entre preferencia profunda, preferencia simple, deseo, gusto, meta instrumental y criterio de importancia;
- no se especifica cómo identificar V implícito ni cómo tratar criterios en conflicto;
- no se cierra la frontera P/V cuando una evaluación expresa lo deseable, relevante u obligatorio;
- no se define evidencia suficiente de ausencia de V;
- no se separan presencia, estabilidad y cambio.

```text
V = SEMANTIC_DEFINITION_INSUFFICIENT
```

### S — `S_psi`

Semántica autorizada mínima:

```text
S_psi = situación encarnada / representación experiencial del entorno
S_psi = situación encarnada tal como opera en la experiencia
```

El desarrollo subordinado incluye cuerpo, condición material, recursos, tiempo, energía, entorno, soporte, límites, posibilidad percibida y situación encarnada. El canon añade que un elemento de realidad o situación no trae función psicológica fija por sí mismo.

Insuficiencias bloqueantes:

- no hay una regla observacional que separe contexto meramente narrado de situación funcionalmente operante;
- la taxonomía es inclusiva, pero no fija el umbral de relevancia para presencia de S;
- no se cierra la frontera entre entorno, representación experiencial, estado corporal, recurso y posibilidad percibida;
- no se define cuándo la ausencia de contexto narrativo permite `ABSENT` y cuándo obliga a `UNKNOWN`;
- no se separan presencia, estabilidad y cambio.

```text
S = SEMANTIC_DEFINITION_INSUFFICIENT
```

## Vetos semánticos vigentes

Los siguientes vetos son obligatorios para cualquier cierre posterior. Algunos están formulados directamente por MOC y otros vienen impuestos por el mandato F0.2; ninguno autoriza una definición positiva nueva.

1. No deducir significado desde nombres, geometría, embeddings, métricas, código o validadores.
2. No tratar los cinco átomos funcionales como cantidades intercambiables ni sumarlos literalmente sin `embed_psi` y `metric_psi` declarados.
3. No convertir conducta observada o salida exteriorizada en `Act_psi`; `B_psi/K_psi` no es un sexto vértice.
4. No convertir elección o `C_psi/PODER_ELEGIR` en `Act_psi`.
5. No convertir preferencia, deseo, gusto, objetivo instrumental o reward escalar en V sin criterio MOC adicional.
6. No convertir una palabra afectiva en Eaf por coincidencia léxica; debe conservarse atribución y función situada.
7. No convertir tiempo, lugar, personas, objetos o contexto narrado en S sin función experiencial autorizada.
8. No confundir presencia con cambio: estabilidad no es ausencia.
9. No usar confianza para sustituir `PRESENT`, `ABSENT`, `AMBIGUOUS` o `UNKNOWN`.
10. No interpretar `AMBIGUOUS` como falta de información ni `UNKNOWN` como evidencia de ausencia.
11. No usar las automatizaciones o resultados computacionales como autoridad semántica.
12. No promover esta auditoría, un futuro manual o una prueba local a Canon MOC.
13. No extender el resultado a diagnóstico, evaluación de personas, uso terapéutico o eficacia clínica.

## Insuficiencias transversales que debe resolver autoridad MOC

Antes de iniciar G0, una decisión semántica MOC autorizada debe fijar, para cada componente:

- definición positiva mínima y condiciones necesarias/suficientes de observación narrativa;
- frontera explícita con sus vecinos semánticos;
- regla para evidencia explícita, implícita, contrastiva y negativa;
- regla de atribución al sujeto objetivo frente a terceros, narrador, cita o detalle incidental;
- criterio de `PRESENT`, `ABSENT`, `AMBIGUOUS` y `UNKNOWN`;
- separación independiente entre `presence_status` y `change_status`;
- criterio de `STABLE` y `NOT_APPLICABLE`;
- regla para spans compartidos con razones distintas;
- resolución canónica de las correspondencias `P_psi/D_psi` y `Eaf_psi/E_af`;
- cierre de la deuda `Act_psi` frente a `B_psi/K_psi` y `C_psi`;
- criterios específicos para V frente a preferencia/objetivo y para S frente a contexto incidental.

Estas condiciones son solicitudes de cierre semántico, no definiciones propuestas por el auditor.

## Consecuencia para los gates F0.2

El mandato exige detener la fase correspondiente cuando la autoridad MOC no permite distinguir operacionalmente un componente. Como los cinco dictámenes son insuficientes, no procede que este rol redacte el manual, genere piloto, mapping, mundos, narrativas o negativos vecinos.

```text
AUTHORITY_AUDIT = COMPLETE
SEMANTIC_DEFINITION_SUFFICIENT_COMPONENTS = 0/5
SEMANTIC_DEFINITION_INSUFFICIENT_COMPONENTS = 5/5
G0_MANUAL_CALIBRATION = NOT_RUN
G1_SEMANTIC_IDENTIFIABILITY = NOT_RUN
G2_DATASET_READINESS = NOT_RUN
MODEL_TRAINING_EXECUTED = NO
MOC_FACTORIZATION_VALIDATION = NOT_TESTED
CANONICAL_STATUS_CHANGE = NOT_AUTHORIZED
```

La continuación requiere autoridad semántica MOC explícita. Una validación computacional puede comprobar posteriormente que un manual cumple el contrato, pero no puede escribir el significado faltante.

## Provenance de esta auditoría

Mandato leído:

```text
C:\Users\IximM\.codex\attachments\ed6af203-625b-46cd-9b88-684f2900b99c\pasted-text.txt
SHA-256 = f51ac2ed373144597f585a1d5a04bf6e09cec445f6daaa13532ff92fee6a6093
```

No se ejecutó Git, no se modificó ninguna fuente y no se creó ningún otro artefacto por este rol.
