# Diseño de investigación

## Preguntas

\[
H_D:\quad MOC_C\not\equiv B_0,B_1,B_2,B_3,B_4
\]

en al menos una propiedad predefinida que no dependa de información o capacidad adicional.

`B4` falsó esta forma general sobre el dominio probado; la no-equivalencia sólo sobrevivió frente a `B0`–`B3`.

\[
H_M:\quad Policy_t\rightarrow Evaluate(Policy_t)\rightarrow Policy_{t+1}
\]

puede producir una mejora fuera de muestra, versionada y reversible.

## Igualdad experimental

Cada controlador recibe el mismo objeto `Scenario`, que contiene:

- acciones y acción automática por defecto;
- task score y reward;
- restricciones duras;
- ajuste contextual;
- estabilidad de trayectoria;
- coste de intervención;
- valores activos y umbrales.

No se permite que `MOC_C` observe variables ocultas a los controles. El benchmark no modela lenguaje ni diferencias de cómputo: las capacidades son deterministas e iguales salvo la política declarada.

## Familias

1. rutina suficiente;
2. fricción de valores formalmente segura;
3. tensión irreducible;
4. restricción dura de seguridad;
5. dirección ausente;
6. cambio contextual;
7. inversión local/temporal;
8. alternativa suficiente que no maximiza reward.

## Falsadores

- Si `B1` reproduce todas las salidas relevantes con igual coste, el nombre concordancia no añade arquitectura.
- Si `B2` o un CMDP preserva todas las tensiones sin escalarización oculta, la oposición reward/concordancia está mal planteada.
- Si `MOC_C` sólo gana bajo el oracle diseñado para él y pierde bajo evaluadores independientes, no hay ventaja demostrada.
- Si `Xi` nunca pausa un caso permitido donde seguridad no interviene, no tiene valor distintivo local.
- Si el meta-update no mejora holdout o no puede revertirse, no hay meta-reorganización respaldada.
- Si `B4_RELATIONAL_GENERIC` iguala a `MOC_C`, la implementación actual no posee distintividad algorítmica. Este falsador se ejecutó y coincidió en status, acción, intervención y métricas sobre los ocho fixtures.
