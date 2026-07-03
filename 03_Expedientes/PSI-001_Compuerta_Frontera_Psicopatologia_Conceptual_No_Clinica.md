# PSI-001 - Compuerta de frontera para psicopatologia conceptual no clinica

Estatus: compuerta provisional de expediente.

Identificador provisional: `PSI-FRON-PSICOPAT-001`.

Fecha: 2026-07-03.

Expediente padre: `PSI-001`.

## Proposito

Definir una compuerta para evaluar propuestas de psicopatologia conceptual no clinica antes de abrir cualquier subfrente psicopatologico.

La compuerta no abre psicopatologia. Solo fija condiciones minimas para distinguir una frontera conceptual legitima de un uso clinico, diagnostico o personal no permitido.

## Fuentes internas

- `PSI-001.md`
- `PSI-001_Definicion_Organizacion_Experiencia_Psicologica.md`
- `PSI-001_Criterio_Transformacion_Experiencia_Psicologica.md`
- `PSI-001_Ejemplos_Conceptuales_No_Clinicos.md`
- `PSI-001_Casos_Transformacion_No_Clinicos.md`
- `PSI-001_Matriz_Patrones_Transformacion_No_Clinica.md`
- `PSI-001_Auditoria_Matriz_Patrones_Transformacion_No_Clinica.md`
- `PSI-001_Decision_Estatus_Matriz_Patrones_Transformacion_No_Clinica.md`

## Definicion local

`Psicopatologia conceptual no clinica` designa, solo dentro de `PSI-001`, el estudio abstracto de formas limite de organizacion de la experiencia psicologica donde aparecen perdida de flexibilidad, rigidez relacional, fragmentacion, bloqueo o perdida de unidad minima.

Esta definicion no equivale a psicopatologia clinica, no nombra trastornos, no clasifica personas y no autoriza diagnostico, tratamiento, consejo profesional ni intervencion.

## Entrada admisible

Una propuesta puede pasar a evaluacion de frontera solo si declara:

- unidad conceptual abstracta;
- `E0`, `E1`, `O0`, `O1`, `R0` y `R1`;
- patron de referencia en `PSI-MAT-PAT-001` o razon trazable para proponer un patron nuevo;
- tipo de limite observado: rigidez, fragmentacion, bloqueo, conflicto persistente, perdida de flexibilidad o perdida de unidad;
- evidencia documental interna;
- ausencia de persona real, diagnostico, tratamiento, consejo o recomendacion de conducta.

## Entrada inadmisible

La propuesta debe bloquearse si:

- usa una persona real, caso personal, historial clinico o situacion autobiografica;
- nombra trastornos como resultado de la matriz;
- diagnostica, evalua, aconseja, prescribe o recomienda intervencion;
- convierte `desorganizacion` o `disolucion` en patologia clinica;
- usa fuentes historicas como autoridad directa;
- admite automaticamente `H-Xi`, `P-107`, Concordancia o cualquier operador externo;
- modifica Canon, documentos oficiales o expedientes ajenos;
- pretende abrir un subfrente psicopatologico sin decision separada.

## Criterios de paso

Una propuesta pasa la compuerta como frontera conceptual si cumple todos los criterios siguientes:

| Criterio | Pregunta | Resultado requerido |
| --- | --- | --- |
| Abstraccion | La unidad es conceptual y no una persona real? | si |
| Trazabilidad | Deriva de `DEF-PSI-ORG-001`, `CRIT-PSI-TR-001` y `PSI-MAT-PAT-001`? | si |
| No clinico | Evita diagnostico, tratamiento, consejo y clasificacion de personas? | si |
| Limite formal | Explica que frontera conceptual aparece y por que no basta una lectura ordinaria de transformacion? | si |
| Conservacion de deuda | Declara deudas y limites sin cerrar `PSI-001`? | si |
| Separacion HXI | No reabre `HXI-001` ni admite `H-Xi`? | si |
| Autoridad documental | No modifica Canon ni documentos oficiales? | si |

## Salidas permitidas

La compuerta puede emitir una de estas salidas:

| Salida | Significado | Efecto |
| --- | --- | --- |
| `frontera_conceptual_admisible` | La propuesta puede trabajarse como caso abstracto de frontera. | Permite crear caso dentro de `PSI-001`, no abre subfrente. |
| `reformular_abstraccion` | La propuesta tiene intuicion util, pero esta demasiado cerca de caso clinico o personal. | Exige reformulacion abstracta antes de continuar. |
| `devolver_a_PSI-001` | La propuesta cabe en transformacion, reorganizacion, desorganizacion, disolucion o no auditable ya existentes. | No requiere frontera psicopatologica. |
| `bloquear_por_uso_clinico` | La propuesta cruza a diagnostico, tratamiento, consejo, persona real o clasificacion clinica. | Detiene la ruta dentro del Laboratorio. |
| `requiere_decision_de_subfrente` | La propuesta podria justificar un subfrente futuro. | Exige decision separada antes de abrirlo. |

## Relacion con `no auditable`

`no auditable` queda estabilizado como salida de seguridad de `PSI-001` para casos donde falta delimitacion conceptual o aparece uso clinico/personal.

La compuerta no elimina `no auditable`; lo vuelve una frontera explicita.

## Temas candidatos no admisorios

Los temas siguientes pueden preparar casos abstractos posteriores, pero no abren subfrente por si mismos:

- rigidez relacional;
- fragmentacion de unidad;
- bloqueo de transicion;
- conflicto persistente de criterios;
- perdida de flexibilidad organizativa;
- perdida de continuidad minima;
- tension abstracta sin lectura clinica.

## Orden de uso

1. Formular la unidad conceptual.
2. Verificar que no hay persona real ni uso clinico.
3. Mapear `E0`, `E1`, `O0`, `O1`, `R0` y `R1`.
4. Comparar contra `PSI-MAT-PAT-001`.
5. Identificar si el fenomeno exige frontera o si vuelve a una categoria existente.
6. Emitir una salida permitida.
7. Registrar deudas y limites.

## Deudas abiertas

- Mantener la matriz provisional de frontera aceptada posteriormente dentro de alcance no clinico y no canonico.
- Decidir si los temas candidatos requieren un subfrente o pueden permanecer como casos dentro de `PSI-001`.
- Definir si `psicopatologia conceptual no clinica` debe conservar ese nombre o recibir una etiqueta menos ambigua.
- Mantener separada toda posible relacion futura con `HXI-001`, `P-107` o Concordancia.
- No convertir esta compuerta en criterio clinico.

## Veredicto

`PSI-FRON-PSICOPAT-001` habilita evaluacion de frontera conceptual no clinica dentro de `PSI-001`.

La primera serie de casos fue creada posteriormente en `PSI-001_Casos_Frontera_Conceptual_No_Clinica.md`.

La matriz provisional fue creada posteriormente en `PSI-001_Matriz_Frontera_Conceptual_No_Clinica.md`.

No abre psicopatologia.

No habilita uso clinico.

No cierra `PSI-001`.
