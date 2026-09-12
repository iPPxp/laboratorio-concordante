# Requisitos F0.2

F0.1 queda congelado. F0.2 debe ser una nueva generación y resolver antes de
crear texto:

1. codebook sellado `U1..U5 -> P/Eaf/Act/V/S`, visible sólo al generador y al
   evaluador después del freeze;
2. separar dos ejes de anotación:
   `presence_status=PRESENT/ABSENT/AMBIGUOUS/UNKNOWN` y
   `change_status=CHANGED/STABLE/AMBIGUOUS/UNKNOWN`;
3. piloto independiente para calibrar el manual antes de crear el corpus de test;
4. escenas sin S funcional y escenas con contexto puramente incidental;
5. Eaf explícito del sujeto, implícito, negado/ausente y DECOY de otro sujeto;
6. V expresado como criterio/dirección, no sólo “inclinación”;
7. cuotas latentes auditables por split, pero desconocidas por anotadores;
8. conservar outcome/narrador independientes e intervenciones NOT_AVAILABLE;
9. no usar la adjudicación para fabricar cobertura faltante;
10. label permutation materializada sólo en la fase de modelado.

F0.2 tampoco entrenará hasta pasar su gate congelado.

