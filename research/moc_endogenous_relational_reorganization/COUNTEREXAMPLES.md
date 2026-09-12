# 22 contraejemplos exactos

1. **Acción nueva sin reorganización:** búsqueda enumera `pedir ayuda`; D/R/K permanecen iguales. Es generación, no reorganización.
2. **Reorganización sin nueva acción:** se separa acción/resultado, pero se elige la misma acción; DC>0, PE=0.
3. **Cambio P sin cambio relacional:** se corrige una errata interpretativa irrelevante; toda R comparable es UNCHANGED.
4. **Cambio relacional sin vértices:** P y V iguales; `equivalencia obligatoria` pasa a `compatibilidad contextual`; RC>0.
5. **Expansión espuria:** generador añade 100 opciones imposibles; PE alto, transitabilidad nula y peor coste.
6. **Contracción correcta:** aparece límite externo real y se eliminan opciones inviables; PR>0 es mejora.
7. **Restricción falsa eliminada:** `debe entregarse hoy` carece de fuente; al retirarla aparece diferir justificadamente.
8. **B5 idéntico en resultado:** replanner produce `versión suficiente` sin editar D/R/K; outcome no distingue mecanismos.
9. **B6 isomorfo:** renombrar tipos MOC por `type1..5` preserva estados, ediciones, campo, decisión y provenance; distintividad no soportada.
10. **Nombres MOC, operación genérica:** se etiqueta un threshold update como `Xi`; nomenclatura no crea estructura.
11. **Opción por búsqueda más amplia:** duplicar beam encuentra alternativa; ningún generador/constraint cambia.
12. **Output sin Act:** postprocesador externo cambia texto, modo interno intacto.
13. **Act sin output:** modo interno cambia urgencia→pausa y Xi retiene emisión.
14. **V sin efecto:** se clarifica un valor no activo y no cambia campo; forzar PC sería falso positivo.
15. **S con efecto:** nueva información revela recurso y abre opción; no requiere cambio subjetivo de P.
16. **Distinción inútil:** crear rojo/no-rojo en tarea sin color sólo aumenta complejidad.
17. **Fusión útil:** dos etiquetas duplicadas se fusionan, reduce conflicto y preserva decisiones.
18. **Transitabilidad empeora:** reencuadre hace `pedir ayuda` conceptualmente presente pero viola permiso; TC negativo.
19. **Local no global:** una relación cambia en subgrafo aislado sin afectar Gamma global.
20. **Meta-loop falso:** sólo sube threshold de trigger; D/R/K de la política no cambian.
21. **Propagación inventada:** P cambia y auditor marca todas R como CHANGED sin medirlas; deben ser UNKNOWN.
22. **Promedio engañoso:** gran PE compensa numéricamente una violación hard en un score medio; perfil conjuntivo lo rechaza.

Cada caso debe competir como fixture futuro generado independientemente; aquí sólo define el control conceptual.
