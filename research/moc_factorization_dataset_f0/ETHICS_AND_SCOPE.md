# Ética, alcance y prohibiciones

## Alcance

F0 admite exclusivamente casos sintéticos o documentales creados para probar factorización, anotación, provenance, relaciones e incertidumbre. No contiene datos personales ni reconstrucciones de personas reales.

## Veto humano y clínico

Está prohibido afirmar o insinuar que el dataset o modelo mide, diagnostica o explica a una persona; detecta patología, emoción verdadera, intención o riesgo; recomienda tratamiento, intervención o conducta; predice resultados humanos; demuestra eficacia psicológica; demuestra fenomenología; o justifica decisiones educativas, laborales, financieras, jurídicas o sanitarias.

Lenguaje permitido: “en los casos sintéticos”, “según lo declarado”, “la anotación codifica”, “el modelo reprodujo la etiqueta”. No permitido: “la persona siente”, “MOC demuestra”, “el sistema entiende la experiencia” o “la intervención funcionará”.

## Minimización y privacidad

- No incluir identificadores, contactos, historiales o combinaciones reidentificables.
- No convertir relatos reales en sintéticos mediante cambios superficiales.
- No solicitar datos sensibles para mejorar F0.
- Ante sospecha de material real: detener, marcar `QUARANTINED` y excluir hasta revisión humana.

## Riesgos epistémicos

1. Confundir coherencia diseñada con validez externa.
2. Circularidad entre reglas de diseño y resultado del modelo.
3. Leakage por nombres, orden o texto.
4. Usar conducta como prueba directa de `Act_psi`.
5. Usar reward como definición de `V_psi`.
6. Registrar relectura interna como cambio del mundo.
7. Convertir coocurrencia en relación, dirección o causalidad.
8. Convertir accuracy en Canon o evidencia humana.

Toda publicación F0 incluye:

```text
SYNTHETIC_OR_DOCUMENTARY_ONLY = YES
PERSON_LEVEL_USE = PROHIBITED
CLINICAL_USE = PROHIBITED
HUMAN_VALIDATION = NO
MOC_CANONIZATION = NO
```

Un buen resultado no amplía permisos; un resultado negativo no autoriza rediseñar el holdout retrospectivamente.
