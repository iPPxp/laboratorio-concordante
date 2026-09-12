# Falsador de isomorfismo MOC_R / B6

## Objetos de traza

Modelar cada traza como sistema etiquetado

\[
\mathcal T=(N,E,\ell_N,\ell_E,O,Prov),
\]

con estados/entidades, transiciones, etiquetas semánticas normalizadas, opciones y DAG de provenance. Se eliminan nombres superficiales (`Xi/gate`, `Phi/evaluator`).

## Mapeo

Buscar biyección o equivalencia conductual acotada \(f:N_M\to N_B\) y mapeos de tipos \(g,h\) que preserven:

1. estados observacionalmente relevantes;
2. aridad/dirección/incidencia de relaciones;
3. pre/post de ediciones D/R/K/\(\Gamma\);
4. \(\mathcal P\), transitabilidad y decisiones;
5. orden causal y provenance;
6. incertidumbre/unknowns;
7. coste dentro de tolerancia declarada.

Un mapeo sencillo se predefine por complejidad descriptiva: tabla de renombrado + transformaciones locales sin reglas especiales por fixture. Ajustes caso a caso invalidan sencillez.

## Procedimiento ciego

Normalizar trazas, ocultar sistema de origen, aprender mapeo en desarrollo y congelarlo. Evaluar holdout de casos y transformaciones. Comparar isomorfismo exacto, parcial y sólo-outcome. Un auditor independiente identifica la primera propiedad no preservada.

## Falsadores

- Si un único mapeo simple preserva 1–7 en holdout: `MOC_TRACE_DISTINCTIVENESS=NOT_SUPPORTED`.
- Si preserva outcome pero falla estructura, especificar testigo mínimo (p. ej., tipado predice edición/posibilidad no codificada en B6).
- Si B6 recibe menos información, presupuesto o ediciones, la comparación es inválida.
- Nombres, orden de serialización y dimensionalidad elegida no rompen isomorfismo.

`GENERIC_ISOMORPHISM_RATE` reporta fracción con mapeo congelado e intervalo. Resultado intermedio permitido: `ALGORITHMIC_UNIQUENESS=NOT_SUPPORTED`, `REPRESENTATIONAL_VALUE=SUPPORTED`.
