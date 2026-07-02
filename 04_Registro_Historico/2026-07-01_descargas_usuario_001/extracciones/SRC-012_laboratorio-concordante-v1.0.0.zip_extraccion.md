# SRC-012 - extraccion textual

Fuente: `laboratorio-concordante-v1.0.0.zip`

Estatus: material historico extraido automaticamente; no autoridad directa.

## Texto

## laboratorio-concordante-v1.0.0/README.md

# Laboratorio Concordante

**Canon v1.0.0 — Baseline estable**

El Laboratorio Concordante es un protocolo formal para auditar la estructura de justificación de modelos explicativos.

No determina la verdad de una teoría.  
No sustituye la evidencia empírica.  
No modifica automáticamente los modelos auditados.

Su función es verificar:

- auditabilidad;
- coherencia estructural;
- reproducibilidad;
- trazabilidad;
- terminación del procedimiento.

## Componentes principales

- `CANON/`: principios normativos del Laboratorio.
- `ARQUITECTURA/`: objetos operativos del sistema.
- `MATEMATICA/`: notación, definiciones y teoremas.
- `PROTOCOLOS/`: procedimientos de auditoría.
- `IMPLEMENTACION/`: implementación de referencia del AAU v0.1.
- `STRESS_TESTS/`: casos diseñados para intentar romper el sistema.
- `EXPEDIENTES/`: registros de investigación y auditoría.

## Estado

Esta versión debe considerarse una línea base de implementación, no un cierre definitivo.


## laboratorio-concordante-v1.0.0/INDEX.md

# INDEX — Arquitectura del Programa

## 0. Alcance

El Laboratorio audita la estructura de justificación de modelos. No decide verdad empírica.

## 1. Canon

- `CANON/C-000_Principio_de_Alcance.md`
- `CANON/M-000_Auditoria_Interna.md`
- `CANON/M-001_Presuncion_de_Reducibilidad.md`
- `CANON/C-001_Reduccion_Conceptual.md`
- `CANON/C-002_Criterio_de_Parada.md`
- `CANON/EF-001_Economia_Formal.md`
- `CANON/Clausula_de_Incompletitud.md`
- `CANON/COMPATIBILIDAD.md`

## 2. Arquitectura

- `ARQUITECTURA/Firmas_Estructurales.md`
- `ARQUITECTURA/Invariantes.md`
- `ARQUITECTURA/Grafo_Acoplamiento_Invariantes.md`
- `ARQUITECTURA/R4.md`
- `ARQUITECTURA/AAU.md`
- `ARQUITECTURA/SE-001.md`

## 3. Implementación

- `IMPLEMENTACION/auditor_laboratorio.py`
- `IMPLEMENTACION/tests/test_aau.py`

## 4. Investigación abierta

- `EXPEDIENTES/P-110_Asimetria_Explicativa.md`
- `EXPEDIENTES/P-111_Auditoria_del_Modelo.md`


## laboratorio-concordante-v1.0.0/BASELINE.md

# BASELINE — Laboratorio Concordante Canon v1.0.0

## Estado

**Baseline estable** para todas las implementaciones futuras del Laboratorio Concordante.

Toda modificación posterior deberá justificar explícitamente el problema que resuelve y declarar su compatibilidad con esta versión.

## Alcance

El Laboratorio Concordante es un protocolo formal para auditar la estructura de justificación de modelos.

No determina la verdad de una teoría.  
No sustituye la evidencia empírica.  
No modifica automáticamente los modelos auditados.

## Núcleo operativo

### Entrada

- Modelo `G`
- `Presv`
- `Activas(G)`

### Objetos derivados

- `Inv(G)`
- `G_I`
- `Break(F_k)`

### Motor

- `AAU v0.1`
- `R4`

### Estados

- `APROBADO`
- `SUSPENDIDO`
- `INCONSISTENTE`
- `NO AUDITABLE`

## Cambio de fase

A partir de esta versión, el desarrollo deja de centrarse en ampliar el Canon y pasa a:

1. implementación de referencia;
2. suite de pruebas;
3. casos de estudio;
4. revisión externa.


## laboratorio-concordante-v1.0.0/CHANGELOG.md

# CHANGELOG

## 1.0.0

- Congelación del Canon como baseline estable.
- Definición del AAU v0.1.
- Definición de R4 como propagación sobre componente conexa.
- Separación entre `Presv`, `Inv(G)` y `Activas(G)`.
- Implementación mínima de referencia.


## laboratorio-concordante-v1.0.0/CANON/C-000_Principio_de_Alcance.md

# C-000 — Principio de Alcance

## Objeto de estudio

El Laboratorio Concordante estudia las condiciones bajo las cuales una explicación puede ser auditada, comparada, modificada y rechazada mediante procedimientos explícitos.

No estudia directamente la realidad física.  
No determina qué teoría es verdadera.  
No produce teorías científicas.  
Produce protocolos para evaluar estructuras de justificación.

## Lo que garantiza

- Terminación procedimental bajo condiciones definidas.
- Reproducibilidad.
- Trazabilidad.
- Coherencia interna.
- Auditabilidad.

## Lo que no garantiza

- Verdad.
- Correspondencia con la realidad.
- Éxito predictivo.
- Superioridad filosófica.

## Principio de neutralidad

Dos modelos incompatibles pueden recibir el mismo dictamen si poseen la misma estructura de auditabilidad.


## laboratorio-concordante-v1.0.0/CANON/M-000_Auditoria_Interna.md

# M-000 — Auditoría Interna

M-000 impide que el Laboratorio convierta sus propios criterios en dogma.

Toda afirmación del Laboratorio debe poder ser auditada, incluida la afirmación sobre qué cuenta como auditoría.

## Función

Detectar:

- lenguaje inflado;
- afirmaciones no demostradas;
- conceptos introducidos sin necesidad;
- cierre dogmático del Canon;
- expansión no justificada del alcance.


## laboratorio-concordante-v1.0.0/CANON/M-001_Presuncion_de_Reducibilidad.md

# M-001 — Presunción de Reducibilidad

Todo candidato a fundamento se presume reducible hasta demostrar lo contrario.

Un concepto sólo puede adquirir estatus canónico si demuestra:

1. irreductibilidad;
2. necesidad;
3. rendimiento formal;
4. compatibilidad con el Canon vigente;
5. apertura a auditoría futura.


## laboratorio-concordante-v1.0.0/CANON/C-001_Reduccion_Conceptual.md

# C-001 — Reducción Conceptual

C-001 exige descomponer todo concepto candidato en componentes más simples antes de aceptarlo.

La reducción se detiene únicamente cuando una nueva reducción destruye auditabilidad o rendimiento explicativo, según C-002.


## laboratorio-concordante-v1.0.0/CANON/C-002_Criterio_de_Parada.md

# C-002 — Criterio de Parada

La reducción conceptual debe detenerse cuando continuar reduciendo destruye la capacidad del sistema para auditar, distinguir o reconstruir la justificación del modelo.


## laboratorio-concordante-v1.0.0/CANON/EF-001_Economia_Formal.md

# EF-001 — Economía Formal

Todo concepto o módulo nuevo debe justificar su costo estructural.

Un incremento de complejidad sólo se acepta si produce una ganancia demostrable en auditabilidad, trazabilidad, terminación, discriminación o reproducibilidad.


## laboratorio-concordante-v1.0.0/CANON/Clausula_de_Incompletitud.md

# Cláusula de Incompletitud

Ningún componente del Laboratorio queda exento de revisión.

El Canon v1.0.0 es una línea base estable, no un cierre definitivo.


## laboratorio-concordante-v1.0.0/CANON/COMPATIBILIDAD.md

# Compatibilidad

## Patch — 1.0.x

Correcciones, aclaraciones y demostraciones nuevas sin alterar el Canon.

## Minor — 1.x.0

Nuevos protocolos o módulos compatibles con el Canon vigente.

## Major — x.0.0

Cambios en axiomas, definiciones fundamentales o comportamiento del AAU.


## laboratorio-concordante-v1.0.0/MATEMATICA/Notacion.md

# Notación

- `G`: modelo auditado.
- `F`: firma estructural.
- `Presv`: firmas preservables.
- `Inv(G)`: invariantes satisfechos.
- `G_I`: grafo de acoplamiento de invariantes.
- `Break(F_k)`: componente de ruptura.
- `AAU`: Algoritmo de Auditoría Único.
- `R4`: propagación de ruptura.


## laboratorio-concordante-v1.0.0/MATEMATICA/Definiciones.md

# Definiciones

## Def. Modelo auditado

Objeto estructural sobre el cual se evalúan firmas.

## Def. Firma preservable

Firma estructural incluida en `Presv`.

## Def. Invariante

Firma preservable satisfecha por `G`.

## Def. Grafo de acoplamiento

Grafo no dirigido construido sobre `Inv(G)` mediante solapamiento de embeddings.

## Def. Ruptura

Pérdida de satisfacción de una firma preservable.


## laboratorio-concordante-v1.0.0/MATEMATICA/Teoremas.md

# Teoremas

## T-R4.2 — Finitud de Inv(G)

Si el universo de firmas es finito y `Presv` es subconjunto suyo, entonces `Inv(G)` es finito.

## T-R4.3 — Construcción finita y determinista de G_I

Dado `G` finito, `G_I` está bien definido, es único y finito.

## T-R4.4 — Terminación de R4

Si `G_I` es finito, R4 termina.

## AAU-1 — Terminación del AAU

Si sus entradas son finitas y decidibles, el AAU termina.


## laboratorio-concordante-v1.0.0/MATEMATICA/Demostraciones.md

# Demostraciones

## T-R4.2

`Inv(G) ⊆ Presv ⊆ Firmas`. Si `Firmas` es finito, entonces `Inv(G)` es finito.

## T-R4.3

Las aristas de `G_I` son subconjunto de `Inv(G) × Inv(G)`. Como `Inv(G)` es finito y el predicado de acoplamiento es decidible, `G_I` es finito y único.

## T-R4.4

R4 calcula una componente conexa mediante BFS/DFS sobre un grafo finito. Todo nodo se visita a lo sumo una vez.

## AAU-1

Cada etapa opera sobre estructuras finitas o decidibles; por composición de procedimientos terminantes, el AAU termina.


## laboratorio-concordante-v1.0.0/MATEMATICA/Problemas_Abiertos.md

# Problemas Abiertos

- P-110: direccionalidad explicativa.
- P-111: reducción del concepto de modelo.
- Dependencia dirigida estricta.
- Acoplamiento ponderado.
- Propagación probabilística.


## laboratorio-concordante-v1.0.0/ARQUITECTURA/Firmas_Estructurales.md

# Firmas Estructurales

Una Firma Estructural es un patrón tipado que puede ser satisfecho por un modelo `G`.

La relación de satisfacción se denota:

`G ⊨ F`

donde `F` es una firma.

Las firmas permiten expresar propiedades estructurales sin convertirlas automáticamente en invariantes.


## laboratorio-concordante-v1.0.0/ARQUITECTURA/Invariantes.md

# Invariantes

## Presv

`Presv` es el subconjunto fijo de Firmas Estructurales designadas como preservables por el protocolo de auditoría.

## Inv(G)

`Inv(G) = { F ∈ Presv : G ⊨ F }`

Un invariante preservable es una firma preservable efectivamente satisfecha por el modelo auditado.


## laboratorio-concordante-v1.0.0/ARQUITECTURA/Grafo_Acoplamiento_Invariantes.md

# G_I — Grafo de Acoplamiento de Invariantes

`G_I` es un grafo no dirigido cuyos nodos son invariantes en `Inv(G)`.

Dos invariantes `F_a` y `F_b` están acoplados si existe al menos un embedding testigo de cada uno que comparte algún nodo o arista del modelo `G`.

Esta relación no afirma causalidad ni dirección. Sólo afirma riesgo estructural compartido.


## laboratorio-concordante-v1.0.0/ARQUITECTURA/R4.md

# R4 — Propagación de ruptura

R4 calcula la zona de riesgo estructural de una ruptura.

Dado un invariante roto `F_k`, se define:

`Break(F_k)`

como la componente conexa de `F_k` en `G_I`.

## Estados relacionados

- Si no hay ruptura: `APROBADO`.
- Si hay ruptura y no hay conflicto con `Activas(G)`: `SUSPENDIDO`.
- Si `Activas(G) ∩ Break(F_k) ≠ ∅`: `INCONSISTENTE`.


## laboratorio-concordante-v1.0.0/ARQUITECTURA/AAU.md

# AAU v0.1 — Algoritmo de Auditoría Único

## Entrada

- Modelo `G`
- `Presv`
- `Activas(G)`

## Salida

- `APROBADO`
- `SUSPENDIDO`
- `INCONSISTENTE`
- `NO AUDITABLE`

## Flujo

1. Validar decidibilidad de firmas preservables.
2. Calcular `Inv(G)`.
3. Construir `G_I`.
4. Detectar rupturas.
5. Ejecutar `R4`.
6. Clasificar estado.
7. Emitir salida mínima reproducible.


## laboratorio-concordante-v1.0.0/ARQUITECTURA/SE-001.md

# SE-001 — Especificación de Salida

Toda auditoría debe devolver un objeto con estructura fija:

- Estado
- Código de falla
- Firmas afectadas
- Componente de ruptura
- Justificación mínima
- Recomendación no interventiva

## Principio de Justificación Mínima

El Auditor devuelve únicamente el conjunto mínimo de hechos suficientes para justificar el estado.

## Separación diagnóstico/reparación

El Laboratorio diagnostica.  
El autor repara.  
El modelo no es modificado automáticamente.


## laboratorio-concordante-v1.0.0/PROTOCOLOS/Auditoria.md

# Protocolo de Auditoría

1. Recibir modelo.
2. Validar `Presv`.
3. Calcular `Inv(G)`.
4. Construir `G_I`.
5. Ejecutar AAU.
6. Registrar salida.


## laboratorio-concordante-v1.0.0/PROTOCOLOS/Admision.md

# Protocolo de Admisión

Un modelo sólo entra a auditoría si:

- declara firmas preservables;
- dichas firmas son decidibles;
- posee estructura suficiente para construir `G_I`.


## laboratorio-concordante-v1.0.0/PROTOCOLOS/Reduccion.md

# Protocolo de Reducción

Todo concepto nuevo se presume reducible por M-001.

Debe demostrar necesidad antes de ser incorporado al Canon.


## laboratorio-concordante-v1.0.0/PROTOCOLOS/Validacion.md

# Protocolo de Validación

La validación del Laboratorio es procedimental, no empírica.

Evalúa si la auditoría termina, es reproducible y produce un dictamen trazable.


## laboratorio-concordante-v1.0.0/PROTOCOLOS/Demolicion.md

# Protocolo de Demolición

El Laboratorio intenta romper conceptos mediante:

- contraejemplos;
- ambigüedad terminológica;
- circularidad;
- no decidibilidad;
- costo formal injustificado.


## laboratorio-concordante-v1.0.0/IMPLEMENTACION/auditor_laboratorio.py

"""
Laboratorio Concordante — AAU v0.1
Implementación de referencia del Auditor.

Estado: Baseline estable.
Esta implementación diagnostica auditabilidad, suspensión e inconsistencia.
No repara modelos ni decide verdad empírica.
"""

from dataclasses import dataclass
from typing import Set, Dict, FrozenSet


@dataclass(frozen=True)
class Invariante:
    id: str
    is_computable: bool
    is_satisfied: bool
    embedding_nodes: FrozenSet[str]
    embedding_edges: FrozenSet[str]


@dataclass
class AuditoriaSalida:
    estado: str
    componente_ruptura: Set[str]
    justificacion: str


class AuditorLaboratorio:
    def __init__(self, presv: Set[Invariante], afirmaciones: Set[str]):
        self.presv = presv
        self.activas = afirmaciones
        self.grafo_gi: Dict[str, Set[str]] = {}

    def construir_gi(self, inv_satisfechos: Set[Invariante]) -> None:
        self.grafo_gi = {f.id: set() for f in inv_satisfechos}
        invariantes = list(inv_satisfechos)

        for i, fa in enumerate(invariantes):
            for fb in invariantes[i + 1:]:
                comparten_nodos = bool(fa.embedding_nodes & fb.embedding_nodes)
                comparten_aristas = bool(fa.embedding_edges & fb.embedding_edges)

                if comparten_nodos or comparten_aristas:
                    self.grafo_gi[fa.id].add(fb.id)
                    self.grafo_gi[fb.id].add(fa.id)

    def ejecutar_aau(self) -> AuditoriaSalida:
        if not self.presv:
            return AuditoriaSalida("NO AUDITABLE", set(), "Presv no definido o vacío")

        if any(not f.is_computable for f in self.presv):
            no_decidibles = {f.id for f in self.presv if not f.is_computable}
            return AuditoriaSalida("NO AUDITABLE", set(), f"Firmas no decidibles: {no_decidibles}")

        inv_g = {f for f in self.presv if f.is_satisfied}

        if not inv_g:
            return AuditoriaSalida("NO AUDITABLE", set(), "No hay invariantes satisfechos auditables")

        self.construir_gi(inv_g)

        rupturas = {f for f in self.presv if not f.is_satisfied}

        if not rupturas:
            return AuditoriaSalida("APROBADO", set(), "Sin rupturas detectadas")

        break_fk: Set[str] = set()

        for f in rupturas:
            if f.id in self.grafo_gi:
                break_fk.update(self._obtener_componente_conexa(f.id))
            else:
                break_fk.add(f.id)

        conflicto = self.activas & break_fk

        if conflicto:
            return AuditoriaSalida(
                "INCONSISTENTE",
                break_fk,
                f"Activas(G) intersecta Break(Fk): {conflicto}"
            )

        return AuditoriaSalida("SUSPENDIDO", break_fk, "Zona de riesgo estructural detectada")

    def _obtener_componente_conexa(self, start_id: str) -> Set[str]:
        visitados = set()
        pila = [start_id]

        while pila:
            actual = pila.pop()

            if actual in visitados:
                continue

            visitados.add(actual)

            for vecino in self.grafo_gi.get(actual, set()):
                if vecino not in visitados:
                    pila.append(vecino)

        return visitados


## laboratorio-concordante-v1.0.0/IMPLEMENTACION/pseudocodigo.md

# Pseudocódigo AAU v0.1

```
si Presv está vacío:
    NO AUDITABLE

si existe F en Presv no decidible:
    NO AUDITABLE

Inv(G) = firmas en Presv satisfechas por G

si Inv(G) está vacío:
    NO AUDITABLE

construir G_I por acoplamiento de embeddings

rupturas = firmas en Presv no satisfechas

si rupturas está vacío:
    APROBADO

Break = unión de componentes conexas de rupturas

si Activas(G) intersecta Break:
    INCONSISTENTE
si no:
    SUSPENDIDO
```


## laboratorio-concordante-v1.0.0/EXPEDIENTES/P-110_Asimetria_Explicativa.md

# P-110 — Asimetría Explicativa

Problema abierto: una restricción simétrica no basta para generar dirección explicativa.

Caso base: asta y sombra.

Estado: abierto.


## laboratorio-concordante-v1.0.0/EXPEDIENTES/P-111_Auditoria_del_Modelo.md

# P-111 — Auditoría del concepto de Modelo

Pregunta: ¿modelo es primitivo o puede reducirse a restricciones, firmas y dominios?

Estado: pendiente.


## laboratorio-concordante-v1.0.0/STRESS_TESTS/Horoscopo.md

# Stress Test — Horoscopo

Pendiente de formalización.


## laboratorio-concordante-v1.0.0/STRESS_TESTS/Bacteria.md

# Stress Test — Bacteria

Pendiente de formalización.


## laboratorio-concordante-v1.0.0/STRESS_TESTS/Empresa.md

# Stress Test — Empresa

Pendiente de formalización.


## laboratorio-concordante-v1.0.0/STRESS_TESTS/Red_Neuronal.md

# Stress Test — Red_Neuronal

Pendiente de formalización.


## laboratorio-concordante-v1.0.0/STRESS_TESTS/Delirio.md

# Stress Test — Delirio

Pendiente de formalización.


## laboratorio-concordante-v1.0.0/STRESS_TESTS/Ajedrez.md

# Stress Test — Ajedrez

Pendiente de formalización.


## laboratorio-concordante-v1.0.0/HISTORIA/H-000_Nacimiento_del_Programa.md

# H-000 — Nacimiento del Programa

El Laboratorio Concordante surge como un programa formal para auditar modelos explicativos sin afirmar verdad empírica.


## laboratorio-concordante-v1.0.0/HIPOTESIS/HIPOTESIS_ACTIVAS.md

# Hipótesis activas

- P-110: direccionalidad explicativa.
- P-111: reducción del concepto de modelo.
- Variantes D-R4.8b/8c/8d.


## laboratorio-concordante-v1.0.0/GLOSARIO/Glosario.md

# Glosario

- `Presv`: firmas preservables.
- `Inv(G)`: firmas preservables satisfechas.
- `Activas(G)`: afirmaciones vigentes del modelo.
- `G_I`: grafo de acoplamiento de invariantes.
- `Break(F_k)`: componente conexa asociada a una ruptura.


## laboratorio-concordante-v1.0.0/IMPLEMENTACION/tests/test_aau.py

from IMPLEMENTACION.auditor_laboratorio import Invariante, AuditorLaboratorio


def inv(id, computable=True, satisfied=True, nodes=(), edges=()):
    return Invariante(id, computable, satisfied, frozenset(nodes), frozenset(edges))


def test_no_auditable_por_no_decidible():
    f1 = inv("F1", computable=False)
    salida = AuditorLaboratorio({f1}, set()).ejecutar_aau()
    assert salida.estado == "NO AUDITABLE"


def test_aprobado_sin_rupturas():
    f1 = inv("F1", nodes=("A",))
    salida = AuditorLaboratorio({f1}, set()).ejecutar_aau()
    assert salida.estado == "APROBADO"


def test_suspendido_por_ruptura_sin_conflicto():
    f1 = inv("F1", satisfied=False, nodes=("A",))
    f2 = inv("F2", satisfied=True, nodes=("A",))
    salida = AuditorLaboratorio({f1, f2}, set()).ejecutar_aau()
    assert salida.estado == "SUSPENDIDO"


def test_inconsistente_por_activa_en_break():
    f1 = inv("F1", satisfied=False, nodes=("A",))
    f2 = inv("F2", satisfied=True, nodes=("A",))
    salida = AuditorLaboratorio({f1, f2}, {"F1"})
    resultado = salida.ejecutar_aau()
    assert resultado.estado == "INCONSISTENTE"
