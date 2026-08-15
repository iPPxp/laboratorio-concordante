# G2 — Especificación condicional no activada

```text
G2_SPECIFICATION_STATUS = CONDITIONAL_ONLY
G2_AUTHORIZED = NO
G1_SEMANTIC_IDENTIFIABILITY = NOT_RUN
```

G2 sólo podrá diseñarse materialmente después de que un futuro G0 y un futuro G1 pasen con artefactos nuevos y congelados. En ese caso deberá incluir familias independientes, splits por familia, test no visto, balance por condición observacional, vecinos negativos, auditoría de leakage, doble anotación, adjudicación, manifests y sanity check de permutación preregistrado.

Este archivo conserva el contrato de dependencia:

```text
G2_AUTHORIZED iff G0=PASSED and G1=PASSED
```

No contiene tamaño de corpus, ejemplos, plantillas ni cuotas, porque fijarlos antes de cerrar semántica permitiría optimizar el instrumento alrededor de definiciones aún inexistentes.
