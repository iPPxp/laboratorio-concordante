# 02 - Fundamentos Matematicos

Estatus: documento oficial consolidado.

Decision de consolidacion: `D-2026-07-03-011`.

Fuentes principales: `SRC-010`, `SRC-012`, `SRC-013`, `SRC-023`, `P-PI`, `AUD-001_R4_Formal_Local.md`, `AUD-001_Gamma_Formal_Local.md`, `AO-001`.

## Alcance

Este documento contiene los fundamentos matematicos aceptados como base documental del Laboratorio.

La aceptacion documental no convierte todos los resultados en teoremas globales ni en Canon. Cuando un resultado es local a un expediente, se declara su frontera.

## Regla de prudencia

Una afirmacion matematica solo puede aparecer aqui con uno de estos estatus:

- definicion;
- notacion;
- teorema con demostracion local;
- algoritmo;
- resultado local de expediente;
- problema abierto;
- deuda conceptual.

Si una afirmacion no esta demostrada o aceptada explicitamente, debe registrarse como hipotesis, deuda conceptual o problema abierto.

## Nucleo historico AAU/R4

Las fuentes `SRC-010`, `SRC-012` y `SRC-013` estabilizan un nucleo operativo historico:

### Entradas

- `G`: modelo auditado.
- `Presv`: conjunto de firmas preservables.
- `Activas(G)`: afirmaciones vigentes o activas del modelo.

### Objetos derivados

- `Inv(G)`: invariantes satisfechos por `G`.
- `G_I`: grafo de acoplamiento de invariantes.
- `Break(F_k)`: componente de ruptura asociada a una firma rota.

### Motor

- `AAU`: Algoritmo de Auditoria Unico.
- `R4`: propagacion de ruptura.

### Estados de salida

- `APROBADO`.
- `SUSPENDIDO`.
- `INCONSISTENTE`.
- `NO AUDITABLE`.

## Notacion basica

| Simbolo | Lectura | Estatus |
| --- | --- | --- |
| `G` | modelo auditado | notacion historica incorporada |
| `F` | firma estructural | notacion historica incorporada |
| `Presv` | firmas preservables | notacion historica incorporada |
| `Activas(G)` | afirmaciones activas del modelo | notacion historica incorporada |
| `Inv(G)` | invariantes satisfechos por `G` | notacion historica incorporada |
| `G_I` | grafo de acoplamiento de invariantes | notacion historica incorporada |
| `Break(F_k)` | componente de ruptura | notacion historica incorporada |
| `AAU` | Algoritmo de Auditoria Unico | algoritmo historico incorporado como base |
| `R4` | propagacion de ruptura | concepto historico, con formalizacion local posterior en `AUD-001` |

## Definiciones basicas

### Modelo auditado

Objeto estructural sobre el cual se evaluan firmas.

La version historica `SRC-023` agrega una definicion funcional: una estructura es modelo si selecciona un dominio, distingue estados, restringe transiciones y relaciona observaciones con transiciones permitidas.

### Firma estructural

Una firma estructural es un patron tipado que puede ser satisfecho por un modelo `G`.

La relacion de satisfaccion se escribe:

```text
G |= F
```

### Firma preservable

Firma estructural incluida en `Presv`.

### Invariante

Firma preservable satisfecha por `G`.

Forma:

```text
Inv(G) = { F in Presv : G |= F }
```

### Grafo de acoplamiento

`G_I` es un grafo no dirigido cuyos nodos son invariantes en `Inv(G)`.

Dos invariantes `F_a` y `F_b` estan acoplados si existe al menos un embedding testigo de cada uno que comparte algun nodo o arista del modelo `G`.

Esta relacion no afirma causalidad ni direccion. Solo afirma riesgo estructural compartido.

### Ruptura

Una ruptura es la perdida de satisfaccion de una firma preservable.

Dado un invariante roto `F_k`, se define:

```text
Break(F_k)
```

como la componente conexa de `F_k` en `G_I`.

## Estados AAU/R4

La clasificacion historica es:

- si no hay ruptura: `APROBADO`;
- si hay ruptura y no hay conflicto con `Activas(G)`: `SUSPENDIDO`;
- si `Activas(G)` intersecta `Break(F_k)`: `INCONSISTENTE`;
- si faltan entradas decidibles o estructura minima: `NO AUDITABLE`.

## Algoritmo AAU v0.1

Entrada:

- modelo `G`;
- `Presv`;
- `Activas(G)`.

Flujo:

1. Validar decidibilidad de firmas preservables.
2. Calcular `Inv(G)`.
3. Construir `G_I`.
4. Detectar rupturas.
5. Ejecutar `R4`.
6. Clasificar estado.
7. Emitir salida minima reproducible.

Salida:

- estado;
- codigo de falla;
- firmas afectadas;
- componente de ruptura;
- justificacion minima;
- recomendacion no interventiva.

Principio: el Laboratorio diagnostica; el autor repara; el modelo no se modifica automaticamente.

## Teoremas historicos incorporados

Estos resultados provienen del nucleo v1.0.0. Quedan incorporados como teoremas documentales bajo sus hipotesis declaradas.

### T-R4.2 - Finitud de `Inv(G)`

Enunciado: si el universo de firmas es finito y `Presv` es subconjunto suyo, entonces `Inv(G)` es finito.

Demostracion: `Inv(G)` es subconjunto de `Presv`, y `Presv` es subconjunto del universo finito de firmas. Por tanto, `Inv(G)` es finito.

### T-R4.3 - Construccion finita y determinista de `G_I`

Enunciado: dado `G` finito, `G_I` esta bien definido, es unico y finito.

Demostracion: las aristas de `G_I` son subconjunto de `Inv(G) x Inv(G)`. Como `Inv(G)` es finito y el predicado de acoplamiento es decidible, `G_I` es finito. Si el predicado de acoplamiento esta fijado, la construccion es unica.

### T-R4.4 - Terminacion de R4

Enunciado: si `G_I` es finito, R4 termina.

Demostracion: R4 calcula una componente conexa mediante busqueda sobre un grafo finito. Todo nodo se visita a lo sumo una vez.

### AAU-1 - Terminacion del AAU

Enunciado: si sus entradas son finitas y decidibles, el AAU termina.

Demostracion: cada etapa opera sobre estructuras finitas o decidibles. Por composicion de procedimientos terminantes, el AAU termina.

## Formalizacion local posterior: R4 sobre trazas

`AUD-001` construyo `R4-FORMAL-AUD-001` como regla formal local de expediente.

Objeto:

```text
rho = <e_1, e_2, ..., e_n>
```

donde `rho` es una traza finita de reportes, decisiones, propuestas, ejecuciones, fallos o verificaciones.

Regla local:

```text
R4_AUD(rho) := para todo t:
  si ejecucion(t) en rho,
  entonces valida(t, rho)
```

Una ejecucion valida exige decision fundada previa, alcance, evidencia previa, evidencia posterior, verificacion posterior, invariante declarado y no uso de niveles inferiores como autoridad directa para modificar niveles superiores.

Teorema local `R4-SAFE-001`: si `R4_AUD(rho)` se satisface, entonces no hay transformacion ejecutada valida sin decision fundada previa.

Frontera: `R4-FORMAL-AUD-001` es formalizacion local de `AUD-001`; no es Regla R4 canonica ni documento de Nivel C.

## Formalizacion local posterior: Gamma

`AUD-001` construyo `GAMMA-FORMAL-AUD-001` como operador parcial local de generalizacion controlada.

Forma:

```text
Gamma_AUD(E, C, W) = G
```

solo si se satisface `WF(E, C, W)`.

La salida conserva invariantes, restricciones, deudas y autoridad de expediente. No aumenta permiso operativo.

Teoremas locales:

- `GAMMA-SAFE-001`: si `Gamma_AUD(E, C, W) = G`, entonces `G` no aumenta el permiso operativo de sus fuentes.
- `GAMMA-TRACE-001`: si `Gamma_AUD(E, C, W) = G`, cada invariante de `G` esta trazado a fuentes locales o queda marcado como deuda.

Frontera: `GAMMA-FORMAL-AUD-001` es formalizacion local de `AUD-001`; no es teoria global de generalizacion ni Nivel C.

## Fundamentos de equivalencia y confluencia

El frente `P-PI` dejo evidencia local para:

- equivalencia minima entre `REPORT_LAYER` y `DO_CHECK_REPORT` bajo contexto declarado;
- equivalencia documental-operativa entre completitud v0 del Auditor y `C-002`;
- confluencia local de continuidad operativa entre ruta de expedientes y ruta de estado.

Estos casos no demuestran equivalencia formal total ni confluencia global.

## Problemas abiertos

Permanecen abiertos:

- Confluencia.
- Equivalencia de proyecciones.
- P-110: direccionalidad o asimetria explicativa.
- P-111: auditoria del concepto de modelo.
- P-107: independencia ontologica del dominio.
- P-108: regla de viabilidad mutacional.
- P-200: equivalencia entre modelos.
- Exportacion o promocion de `R4-FORMAL-AUD-001` fuera de `AUD-001`.
- Exportacion o uso de `GAMMA-FORMAL-AUD-001` fuera de `AUD-001`.
- Relacion entre algebra operacional, mutaciones y modelos equivalentes.

## Estado

Documento 02 queda consolidado como fundamento matematico oficial del Laboratorio.

Sus resultados globales son los que declaran hipotesis finitas y decidibles. Sus formalizaciones locales posteriores conservan su frontera de expediente.
