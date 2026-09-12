# F0.1 sealed synthetic world schema

## Scope and authority

This directory is the exclusive output of `WORLD_GENERATOR`. Its declared
inputs are `PREREGISTRATION.md`, `ROLE_MATRIX.md`, and `GATE_0_1.md`. It contains
only a sealed synthetic world and the restricted projection handed to the
narrator. It contains no authored narrative, annotation, adjudication, generic
outcome, model output, or human/clinical record.

The statistical unit is `family_id`. Every identifier occurs exactly once in
each JSONL file. Identifiers are join keys only; their lexical order carries no
design meaning.

## `world_states.jsonl`

Each line is one sealed world record:

| Field | Type | Meaning |
|---|---|---|
| `family_id` | string | Opaque family join key. |
| `split` | enum | `train`, `validation`, or `test`. |
| `design` | enum | `core` or `adversarial`. |
| `pair_block` | string, core only | One of ten pairwise blocks. |
| `cell` | enum, core only | `00`, `01`, `10`, or `11`. |
| `challenge` | string, adversarial only | Sealed challenge code. |
| `manipulated_slots` | array | Neutral slot identifiers only. |
| `state_t0` | length-5 integer array | Baseline in fixed order `U1..U5`. |
| `observed_delta` | length-5 integer array | Change observable before narration, in order `U1..U5`. |
| `latent_signal_mode` | enum | `explicit`, `implicit`, `absent`, or `decoy`. |
| `intervention` | object | Present availability and opaque option code. |
| `sealed_future_rule` | object | Rule available to the outcome author, never to the narrator. |
| `setting` | string | Synthetic everyday setting code. |
| `synthetic_nonclinical` | boolean | Must be `true`. |

The five slots remain deliberately neutral. This layer does not provide a
semantic codebook from `U1..U5` to theory labels. The preregistered four-mode
signal condition is represented by `latent_signal_mode`; it is not a sixth
slot. Its four values provide the explicit/implicit/absent/decoy gate
condition without exposing that condition to the narrator as metadata.

### Core construction

The ten blocks exhaust all unordered pairs of five neutral slots:

```text
B01 U1-U2   B02 U1-U3   B03 U1-U4   B04 U1-U5
B05 U2-U3   B06 U2-U4   B07 U2-U5
B08 U3-U4   B09 U3-U5
B10 U4-U5
```

Within each block, the two bits in `cell` correspond, in pair order, to
whether the observed delta for that slot is zero or nonzero. Each block has
exactly one record in each of `00`, `01`, `10`, and `11`. No cell code or pair
metadata is copied to the narrator projection.

### Sealed future rules

Let `x1 = state_t0 + observed_delta`, element by element. The outcome author
may derive a later state using the rule named in `sealed_future_rule`:

- `carry_known`: later state equals `x1`.
- `dampen_known`: each nonzero coordinate of `x1` moves one integer step
  toward zero.
- `amplify_known`: each nonzero coordinate moves one integer step farther in
  its current direction, capped to `[-2, 2]`.
- `cross_known`: the first nonzero coordinate in `x1` adds its sign to the next
  coordinate cyclically, capped to `[-2, 2]`; if all coordinates are zero,
  later state equals `x1`.
- `opaque_unknown`: the rule intentionally does not identify a later state;
  downstream coding must preserve `UNKNOWN`.

`driver` records whether an opaque synthetic option or no option participates
in the rule. These rules are world mechanics, not an authored outcome table.

## `narrator_projection.jsonl`

Each line contains only:

| Field | Type | Meaning |
|---|---|---|
| `family_id` | string | Opaque join key. |
| `split` | enum | Frozen split. |
| `setting` | string | Everyday nonclinical scene. |
| `present_scene` | string | Surface description up to the narration boundary. |
| `surface_hint` | string | What is perceptible in the current scene. |
| `available_step` | string | Whether a present, concrete next step can be accessed. |
| `narration_guard` | string | Prohibition against inventing later consequences. |

The projection omits `design`, `pair_block`, `cell`, `challenge`, all neutral
slot identifiers, observed arrays, latent-mode labels, rule identifiers, and
every later state. Surface prose may instantiate a condition needed to narrate
the current scene, but it does not name the hidden design variable.

## Frozen counts

```text
families = 60
core = 40
adversarial = 20
train / validation / test = 35 / 10 / 15
intervention unavailable = 12 (train 6, validation 3, test 3)
latent signal modes = 15 each
human or clinical records = 0
```

