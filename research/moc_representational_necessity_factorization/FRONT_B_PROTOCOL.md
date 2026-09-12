# Frente B — MOC frente a representación aprendida

## Entrada común

Ambas familias reciben únicamente `case_id`, texto crudo, índice temporal y un
contexto no semántico. Quedan prohibidos en inferencia: P/Eaf/Act/V/S, D/R/K,
estado futuro, edit objetivo y efecto de intervención.

## Modelos

| ID | Representación | Supervisión | Finalidad |
|---|---|---|---|
| G-E2E | embedding genérico aprendido | targets | baseline predictivo libre |
| G-SLOTS | cinco slots anónimos | conceptos con nombres permutados | controla número de slots y label budget |
| M-CBM | cuello de botella P/Eaf/Act/V/S | conceptos MOC | prueba tipado interpretable |
| M-REL | M-CBM + relaciones | conceptos + relaciones | prueba valor relacional incremental |
| M-DROP | ablaciones drop-one | igual | no redundancia |
| M-MERGE | fusiones por pares | igual | minimalidad |
| M-PERM | tipos permutados | igual | nombres vs estructura |
| G-CAP | genérico con igual capacidad/parámetros | igual presupuesto | control adversarial fuerte |

La supervisión conceptual se cuenta como recurso. Comparar M-CBM anotado con un
G-E2E sin esas etiquetas responde “¿ayuda la supervisión?”, no “¿ayuda MOC?”. El
resultado principal exige un control con igual label budget.

## Tareas holdout

1. transición `t→t+1`;
2. posibilidades que aparecen/desaparecen;
3. predicción de `do(P)`, `do(Eaf)`, `do(Act)`, `do(V)`, `do(S)`;
4. invariantes bajo paráfrasis;
5. transferencia de dominio;
6. tipo de intervención no visto;
7. eficiencia de muestra;
8. calibración y abstención.

## Resultado positivo fuerte

MOC debe mejorar al menos una tarea primaria en holdout con corrección por
comparaciones, no empeorar seguridad/calibración más allá del margen y conservar
la ventaja frente a G-SLOTS, G-CAP, M-PERM, drop-one y merge. Interpretabilidad
humana se evalúa aparte y no compensa automáticamente peor predicción.

