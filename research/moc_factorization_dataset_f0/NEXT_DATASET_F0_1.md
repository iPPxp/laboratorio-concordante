# Especificación correctiva F0.1

F0 no se modifica post-hoc. F0.1 será un nuevo corpus congelado y debe corregir
los bloqueantes antes de combinarse con F0.

## Requisitos mínimos

1. al menos 10 familias test independientes y no tres paráfrasis como réplicas;
2. cobertura explícita PRESENT/ABSENT/AMBIGUOUS/UNKNOWN para cada componente en
   cada split, sin mostrar las cuotas al anotador;
3. casos afectivos explícitos, implícitos, ausentes y engañosos;
4. intervenciones disponibles, no disponibles, contraindicadas e indeterminadas;
5. outcomes generados por un autor/fuente diferente al diseñador de textos;
6. dos anotadores MOC ciegos más adjudicador independiente;
7. evidencia textual no reutilizable automáticamente entre componentes;
8. inventario completo de posibilidades sólo en un subconjunto diseñado para
   esa tarea; UNKNOWN fuera de él;
9. bloques contrafactuales de cuatro celdas y controles de simultaneidad;
10. splits sellados antes de anotar y auditoría de contaminación por plantillas.

## Gate

```text
F0_1_DATA_GENERATION = ALLOWED_AS_SYNTHETIC_INSTRUMENT_WORK
F0_1_MODEL_TRAINING = FORBIDDEN_UNTIL_REAUDIT
F1_NATURALISTIC_ADVANCE = BLOCKED
```

