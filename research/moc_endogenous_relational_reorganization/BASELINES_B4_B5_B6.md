# Controles genéricos B4, B5 y B6

## Alcance

También se implementan controles inferiores B0–B3: B0 toma la respuesta
automática; B1 hace una segunda evaluación sin ampliar alternativas; B2 aplica
`argmax` al score sin identificarlo con V; B3 filtra acciones prohibidas y luego
optimiza sin editar la restricción. Todos conservan D/R/K/G y quedan subsumidos
por la comparación más fuerte con B4 para el dictamen principal.

Estos controles no contienen vocabulario ni estructura semántica de dominio. No usan fixtures, oráculos ni una relación privilegiada. Su finalidad es impedir que cualquier mejora atribuida a una reorganización específica sea explicable por selección, generación genérica o edición estructural genérica.

El estado es:

\[
S=(D,R,K,G,P,A),
\]

donde `D` es un mapa de elementos y atributos escalares, `R` relaciones genéricas, `K` restricciones simbólicas, `G` un generador versionado, `P` provenance y `A` la acción seleccionada. Ningún nombre prescribe interpretación.

## B4 — selector relacional

B4 genera un campo fijo desde `D/R/K/G` y selecciona el candidato con mayor puntuación, con desempate determinista. Puede cambiar `A`, pero no reorganiza la estructura. Es el control de **selección sin reorganización**.

Dictamen de contrato: `STRUCTURE_CHANGED=False`, expansión y contracción cero, transitabilidad uno.

## B5 — replanner generativo

B5 edita únicamente `G`: añade una operación genérica, incrementa la revisión y regenera el campo. No modifica directamente `D/R/K`. Toda edición registra actor, fuente, tiempo, razón, estado anterior/posterior y reversibilidad.

Sirve para preguntar si ampliar posibilidades basta sin una reorganización de relaciones o restricciones.

## B6 — editor estructural genérico

B6 puede hacer `UPSERT/REMOVE` en `D`, `ADD/REMOVE` en `R` y `ADD/REMOVE` en `K`. Valida que todo extremo de relación exista en `D`. No conoce cuál edición sería correcta para un dominio.

Una reorganización puede no cambiar la acción: añadir una restricción que el generador actual no usa cambia la estructura y conserva el campo. Este control separa **reorganización** de **cambio conductual**.

## Campo de posibilidades y métricas

Un campo contiene candidatos, operación de origen, puntuación y fuentes. La comparación informa:

- expansión: candidatos añadidos;
- contracción: candidatos retirados;
- retenidos;
- transitabilidad provisional: Jaccard de candidatos retenidos sobre la unión.

La transitabilidad aquí mide continuidad entre campos, no alcanzabilidad semántica ni valor de una transición.

## Provenance

Cada edición registra `event_id`, tiempo, actor, operación, objetivo, huellas estructurales anterior/posterior, fuentes, tipo de fuente, razón y reversibilidad. La marca de reversibilidad no ejecuta una reversión automática ni concede autoescritura.

## Casos que deben permanecer distinguibles

| Caso | Estructura | Acción | Campo |
|---|---:|---:|---:|
| B4 selección | igual | puede cambiar desde `None` | igual |
| B5 generación | cambia `G` | puede cambiar o no | puede expandirse/contraerse |
| B6 edición efectiva | cambia `D/R/K` | puede cambiar | puede cambiar |
| B6 edición neutral | cambia `D/R/K` | igual | igual |

## Límites

Pasar pruebas unitarias sólo demuestra contratos de software. No demuestra endogeneidad, utilidad causal, correspondencia semántica, superioridad frente a un control ni validez sobre datos futuros. Estos módulos no deben conocer el test final; cualquier evaluación discriminante debe mantenerse externamente aislada.
