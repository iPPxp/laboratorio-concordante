# 25 predicciones falsables

Todas están `HYPOTHESIZED`; ninguna es resultado de este módulo.

| ID | Claim | Comparador | Observable | Desconfirmación |
|---|---|---|---|---|
| F01 | P y V tienen efectos diferenciables | merge P/V | outcome de contrafactual | merge queda equivalente |
| F02 | P y Eaf son separables | merge P/Eaf | transición holdout | no hay pérdida al fusionar |
| F03 | P y Act son separables | merge P/Act | do(P) vs do(Act) | efectos indistinguibles |
| F04 | P y S son separables | merge P/S | transferencia | fusión iguala |
| F05 | Eaf y Act son separables | merge Eaf/Act | estado siguiente | equivalencia dentro de margen |
| F06 | Eaf y V son separables | merge Eaf/V | intervención | efectos iguales |
| F07 | Eaf y S son separables | merge Eaf/S | OOD | sin gap |
| F08 | Act y V son separables | merge Act/V | posibilidades | fusión iguala |
| F09 | Act y S son separables | merge Act/S | accesibilidad | fusión iguala |
| F10 | V y S son separables | merge V/S | transición | fusión iguala |
| F11 | Los cinco son conjuntamente suficientes | G-CAP | error holdout | G-CAP mejora materialmente |
| F12 | Ninguno es redundante | drop-one | pérdida pareada | algún drop queda equivalente |
| F13 | Cinco supera cuatro factores | 4-slot | transferencia | 4-slot iguala |
| F14 | Cinco no requiere sexto D | M+D-state | perfil predictivo/coste | D-state mejora replicablemente |
| F15 | D-operación supera D-estado | D1 vs D3 | intervención y complejidad | D1 iguala o supera |
| F16 | M-CBM mejora eficiencia de muestra | G-CAP | curva n→score | curvas equivalentes |
| F17 | M-CBM mejora transición | G-CAP | métrica primaria | no hay diferencia |
| F18 | M-REL mejora campo de posibilidades | M-CBM | F1 PE/PR | relaciones no añaden valor |
| F19 | MOC mejora intervención | G-SLOTS | error de efecto | slots igualan |
| F20 | MOC mejora transferencia | G-E2E/G-CAP | OOD gap | genérico iguala |
| F21 | MOC mejora calibración | G-CAP | Brier/ECE | no mejora o empeora |
| F22 | Ventaja no depende de nombres | M-PERM | delta de desempeño | permutar conserva todo |
| F23 | Ventaja sobrevive igual label budget | G-SLOTS | tarea primaria | desaparece con supervisión igualada |
| F24 | Conceptos son estables temporalmente | encoder longitudinal | consistencia | factores permutan/derivan |
| F25 | Intervenciones tienen especificidad de tipo | do(component) | matriz de efectos | filas no distinguibles |

Una sola frontera positiva no prueba minimalidad del conjunto completo. Una sola
tarea negativa tampoco elimina valor humano o descriptivo.

