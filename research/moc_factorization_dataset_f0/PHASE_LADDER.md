# Escalera de fases F0-F3

La fase limita qué afirmación es admisible. El ascenso no es automático ni modifica autoridad MOC.

## F0 — Factibilidad sintética y semántica

Casos sintéticos o texto diseñado; anotación de componentes, relaciones e incertidumbre. Puede establecer representabilidad, aplicabilidad del protocolo, consistencia, cobertura y rendimiento sintético. No establece correspondencia humana, validez psicológica, clínica, causal o ecológica, ni eficacia de MOC/concordIA.

## F1 — Factibilidad documental externa no clínica

Materiales no personales, no clínicos e independientes del diseño, con derechos y procedencia claros. Requiere decisión explícita, muestreo preregistrado, política de uso, acuerdo entre anotadores y análisis de drift. Evalúa generalización documental, no personas.

## F2 — Investigación humana no clínica

Datos de participantes reales en investigación no clínica. Requiere gobernanza ética, consentimiento, minimización, privacidad, protocolo aprobado, plan estadístico y supervisión humana competente. No se abre por éxito F0/F1.

## F3 — Contexto clínico o regulado

Cualquier uso clínico, diagnóstico, terapéutico, de riesgo, elegibilidad o decisión material. Permanece fuera de alcance; exigiría un proceso regulatorio, clínico y de seguridad independiente.

| Transición | Evidencia necesaria | No basta |
|---|---|---|
| F0 → F1 | protocolo estable, fiabilidad, auditoría de leakage, decisión de apertura | tests verdes o accuracy sintética |
| F1 → F2 | necesidad científica y aprobaciones éticas/privacidad | generalización documental |
| F2 → F3 | proceso regulatorio y clínico independiente | significancia aislada |

```text
CURRENT_PHASE = F0
F1_AUTHORIZED = NO
F2_AUTHORIZED = NO
F3_AUTHORIZED = NO
HUMAN_VALIDATION = NO
CLINICAL_VALIDATION = NO
```
