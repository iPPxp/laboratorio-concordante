# Formulario de decisión humana MOC

```text
REVIEW_STATUS = PENDING
REVIEWER_ROLE = SOLE_HUMAN_MOC_AUTHORITY
PACKAGE = MOC-PENTACORO-OBSERVABILITY-001
```

## Decisiones por artefacto

Marcar una opción y registrar enmiendas textuales exactas.

| Artefacto | APPROVE | APPROVE_WITH_AMENDMENT | REJECT | DEFER_AS_DEBT | Enmienda/razón |
|---|---:|---:|---:|---:|---|
| State semantics | ☐ | ☐ | ☐ | ☐ | |
| Attribution rules | ☐ | ☐ | ☐ | ☐ | |
| P/V boundary | ☐ | ☐ | ☐ | ☐ | |
| Eaf/S boundary | ☐ | ☐ | ☐ | ☐ | |
| Eaf/V boundary | ☐ | ☐ | ☐ | ☐ | |
| Act/conduct boundary | ☐ | ☐ | ☐ | ☐ | |
| Act/choice-intention boundary | ☐ | ☐ | ☐ | ☐ | |
| V/preference boundary | ☐ | ☐ | ☐ | ☐ | |
| S/incidental-context boundary | ☐ | ☐ | ☐ | ☐ | |
| P component sheet | ☐ | ☐ | ☐ | ☐ | |
| Eaf component sheet | ☐ | ☐ | ☐ | ☐ | |
| Act component sheet | ☐ | ☐ | ☐ | ☐ | |
| V component sheet | ☐ | ☐ | ☐ | ☐ | |
| S component sheet | ☐ | ☐ | ☐ | ☐ | |

## Gate de suficiencia semántica

Completar sólo después de resolver todas las enmiendas:

```text
SEMANTIC_DEFINITION_SUFFICIENT_P = YES | NO
SEMANTIC_DEFINITION_SUFFICIENT_EAF = YES | NO
SEMANTIC_DEFINITION_SUFFICIENT_ACT = YES | NO
SEMANTIC_DEFINITION_SUFFICIENT_V = YES | NO
SEMANTIC_DEFINITION_SUFFICIENT_S = YES | NO

SEMANTIC_DEFINITION_SUFFICIENT_COMPONENTS = __/5
MOC_OPERATIONAL_PACKAGE_APPROVED = YES | NO
```

## Decisión separada sobre G0

La aprobación semántica no autoriza el piloto automáticamente:

```text
G0_AUTHORIZED = YES | NO
G0_AUTHORIZATION_DECISION_ID =
G0_AUTHORIZATION_DATE =
G0_SCOPE = 10_TO_20_DISPOSABLE_SYNTHETIC_FRAGMENTS
```

Si `MOC_OPERATIONAL_PACKAGE_APPROVED=YES` y `G0_AUTHORIZED=NO`, el paquete queda aprobado pero inactivo.

## Firma de decisión

```text
HUMAN_REVIEWER =
DECISION_DATE =
DECISION_ID =
SIGNATURE_OR_ATTESTATION =
```
