# Schema de outcomes F0.1

El autor de outcomes lee `world/world_states.jsonl`, no la narrativa ni las
anotaciones. Produce targets genéricos:

```text
schema
case_id
family_id
split
next_state_class
changed_slot_count
change_signature_hash
stability_change
possibilities_added[]
possibilities_removed[]
possibility_change
intervention_available
intervention_class
intervention_effect
uncertainty
source_world_digest
outcome_author
```

Quedan prohibidas claves o valores que revelen P/Eaf/Act/V/S, pair/cell o el
codebook de slots. El hash de firma permite comparar outcomes sin exponer la
semántica manipulada.

`intervention_effect` puede ser `POSITIVE`, `NEGATIVE`, `NULL`, `UNKNOWN` o
`NOT_AVAILABLE`. No se convierte un sucesor sintético en efecto causal humano.

