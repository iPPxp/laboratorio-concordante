# Modelo automático de doble bucle

## Contrato

El prototipo implementa dos rutas computacionales, no dos entidades psicológicas.

```text
Observe -> Infer -> Phi -> Choice -> Allow/Act -> Xi stop
                         ^                    |
                         |------ feedback ----|
```

El bucle basal ejecuta un ciclo y termina. El activo se habilita por un disparador explícito y puede realimentar contexto hasta que `Xi` detecta `ALLOW`, falta de observación o profundidad máxima. `Allow` es una elección positiva de no actuar; no es fallo ni conducta encubierta.

`Phi` es un evaluador estructurado: devuelve puntajes por valor, agregado, identificadores de valores/evidencia e incertidumbre. No es conciencia. `Xi` organiza y detiene; no es voluntad. `Choice` selecciona entre alternativas definidas, pero no crea permisos ni autoridad.

## Reutilización del frente Self Model

| Dictamen | Elemento | Razón |
|---|---|---|
| REUSE | dataclasses inmutables, ledger de provenance, determinismo | Favorecen auditoría y pruebas causales |
| ADAPT | transición única a doble bucle con eventos por fase | Se necesita distinguir orden, trigger y feedback |
| SUBSUME | historial y digest dentro de `ConcordiaState` | El estado del bucle incorpora trazabilidad temporal |
| KEEP_AS_CONTROL | política simple `Self -> Action` | Baseline útil contra la arquitectura doble |
| REJECT | inferir acceso introspectivo desde lenguaje o nombre de campo | No es evidencia causal |

No se importa el módulo anterior: se preserva aislamiento experimental y se reutilizan contratos, no estado ni autoridad.

## Ablaciones obligatorias

`experiments.ablation_suite` compara `FULL_DUAL` con ausencia de V, Xi, Phi, contexto, feedback, cambio de orden y control automático de un bucle. Una diferencia es un efecto dentro del programa; sólo replicación sobre tareas discriminantes podría sustentar utilidad general.

## Recursividad

La recursividad está acotada por `xi_max_steps`. El cambio de metapolítica exige intervención identificada y sólo la última intervención enlazada puede revertirse. No existe autoescritura, mutación de permisos ni selección autónoma de valores.

