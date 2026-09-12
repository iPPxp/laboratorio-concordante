# Manual común de anotación F0.1

Los anotadores leen sólo `raw/model_input.jsonl`. No deben buscar cinco elementos
por obligación. Cada componente puede estar `PRESENT`, `ABSENT`, `AMBIGUOUS` o
`UNKNOWN`.

## Componentes

- `P`: interpretación, evaluación, expectativa o regla expresada por el sujeto.
- `EAF`: señal afectiva atribuible al sujeto/configuración analizada; vocabulario
  emocional referido a otra persona o citado como dato no basta.
- `ACT`: modo de respuesta o disponibilidad interna; no equivale a conducta,
  output, acción ejecutada ni `ACT_psi`.
- `V`: dirección, prioridad o criterio; no es reward escalar ni mero gusto.
- `S`: condición situacional funcionalmente relevante; un detalle incidental no
  cuenta por aparecer en el texto.

## Registro por componente

```text
status
evidence_spans[]
reason
confidence = LOW | MEDIUM | HIGH
scope = TARGET_SUBJECT | OTHER_SUBJECT | INCIDENTAL | UNKNOWN
```

Un span puede apoyar dos componentes sólo si las razones son distintas y
específicas. Copiar la misma razón entre constructos se marca para adjudicación.

## Relaciones

Sólo anotar una relación si el texto la expresa. Campos:

```text
source, target, kind, status, evidence_span, reason
```

No inferir causalidad de coaparición.

## Casos difíciles

- palabra afectiva de otra persona: no implica EAF del sujeto objetivo;
- conducta observada: no implica por sí sola ACT;
- “quiero” puede ser preferencia, dirección o cita ambigua;
- tiempo/lugar incidental: no implica S funcional;
- una frase puede hacer inseparables P/V: usar AMBIGUOUS, no forzar;
- si el texto carece de señal suficiente: UNKNOWN; ABSENT exige evidencia de
  ausencia funcional o un negativo explícito.

Los anotadores no conocen cuotas, celdas contrafactuales ni condiciones DECOY.

