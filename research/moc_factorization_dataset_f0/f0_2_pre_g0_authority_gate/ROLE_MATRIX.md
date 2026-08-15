# F0.2 — Matriz de roles y accesos

```text
SEPARATION_TYPE = PROCEDURAL
CRYPTOGRAPHIC_BLINDING_CLAIMED = NO
```

| Rol | Entradas permitidas | Salidas permitidas | Prohibiciones principales | Estado |
|---|---|---|---|---|
| AuthorityAuditor | mandato, autoridad vigente MOC/Lab | `AUTHORITY_BASELINE.md` | ejemplos, F0/F0.1, evaluación propia | completado |
| MappingCustodian | mandato | mapping sellado y manifest | semántica, ejemplos, evaluación | completado |
| ManualAuthor | baseline autorizado | manual y definiciones operacionales | inventar semántica | no autorizado |
| WorldGenerator | variables neutrales `U_i` | estados neutrales | mapping MOC, textos | no ejecutado |
| ProjectionDesigner | estados neutrales | proyecciones observables | mapping MOC, anotaciones | no ejecutado |
| Narrator | proyecciones | textos | mundo, mapping, objetivos | no ejecutado |
| AnnotatorA/B | manual congelado y textos | anotaciones | mundo, mapping, cuotas, otra anotación | no ejecutado |
| Adjudicator | manual, textos, A/B | adjudicación | mundo, mapping, targets | no ejecutado |
| PreG0GateEvaluator | mandato, baseline, manifests | dictamen previo | crear semántica o ejemplos | ejecutado independientemente |
| GateEvaluator G1 | artefactos congelados y mapping revelado tras freeze | métricas y gate | alterar inputs | no autorizado |

## Secuencia efectiva

```text
AuthorityAudit ─┬─> PRE_G0_BLOCKED
                └─> ManualAuthor NOT_AUTHORIZED

MappingCustodian -> SEALED_BEFORE_EXAMPLES
```

El mapping se selló antes de ejemplos, pero la insuficiencia semántica impidió activar el resto de la cadena. Ningún rol posterior recibió autorización.
