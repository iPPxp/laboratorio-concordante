# PSI-001 - Matriz de frontera conceptual no clinica

Estatus: matriz provisional de expediente.

Identificador provisional: `PSI-FRON-MAT-001`.

Fecha: 2026-07-03.

Expediente padre: `PSI-001`.

Base:

- `PSI-FRON-PSICOPAT-001`
- `PSI-FRON-CAS-001` a `PSI-FRON-CAS-006`

## Proposito

Sintetizar los casos admisibles de frontera conceptual no clinica en una matriz provisional estrictamente local a `PSI-001`.

La matriz no abre subfrente psicopatologico, no usa categorias clinicas, no nombra trastornos, no evalua personas, no canoniza contenido y no modifica documentos oficiales.

## Entrada

La matriz usa solo los casos aceptados como `frontera_conceptual_admisible`:

- `PSI-FRON-CAS-001`: rigidez relacional.
- `PSI-FRON-CAS-002`: fragmentacion de unidad.
- `PSI-FRON-CAS-003`: bloqueo de transicion.
- `PSI-FRON-CAS-005`: tension relacional formalizada.

Casos no incorporados como patrones de matriz:

- `PSI-FRON-CAS-004`: devuelto a `PSI-001` por quedar cubierto por desorganizacion ordinaria.
- `PSI-FRON-CAS-006`: bloqueado por uso clinico o personal; se conserva solo como control negativo.

## Matriz principal

| Patron de frontera | Caso fuente | Continuidad conservada | Restriccion dominante | Salida de compuerta | Lectura no clinica |
| --- | --- | --- | --- | --- | --- |
| Rigidez relacional | `PSI-FRON-CAS-001` | unidad de red y centro identificable | centro fijo sin actualizacion relacional | `frontera_conceptual_admisible` | estabilidad demasiado fija para reorganizacion flexible |
| Fragmentacion de unidad | `PSI-FRON-CAS-002` | fragmentos locales organizados | falta integracion global | `frontera_conceptual_admisible` | no es disolucion completa ni reorganizacion global |
| Bloqueo de transicion | `PSI-FRON-CAS-003` | regla inicial y regla candidata identificables | transicion detenida entre reglas | `frontera_conceptual_admisible` | no basta como conflicto; importa la detencion de paso |
| Tension relacional | `PSI-FRON-CAS-005` | meta comun y rutas disponibles | inhibicion mutua entre reglas candidatas | `frontera_conceptual_admisible` | tension formalizada sin lenguaje vivencial ni clinico |

## Control negativo

`PSI-FRON-CAS-006` permanece bloqueado.

No entra a la matriz como patron. Su funcion es conservar visible el limite: cualquier persona real, diagnostico, consejo, tratamiento, evaluacion personal o recomendacion de conducta detiene la ruta.

## Relacion con casos devueltos

`PSI-FRON-CAS-004` no entra a la matriz porque el conflicto persistente ya queda cubierto por `desorganizacion` y `P-PSI-004`.

La matriz no debe inflarse con casos que `CRIT-PSI-TR-001` ya puede clasificar sin frontera nueva.

## Regla de lectura

Para usar `PSI-FRON-MAT-001`:

1. Confirmar que la unidad es abstracta.
2. Verificar que no hay persona real ni uso clinico.
3. Identificar continuidad conservada.
4. Identificar restriccion dominante.
5. Comparar con los cuatro patrones de matriz.
6. Devolver a `PSI-001` si una categoria ordinaria basta.
7. Bloquear si aparece uso clinico o personal.

## Salidas permitidas

| Salida | Uso |
| --- | --- |
| `rigidez_relacional` | estabilidad fija que impide actualizacion relacional |
| `fragmentacion_unidad` | organizaciones parciales sin integracion global |
| `bloqueo_transicion` | paso detenido entre regla inicial y regla candidata |
| `tension_relacional` | inhibicion mutua entre rutas o reglas candidatas |
| `devolver_a_PSI-001` | el caso cabe en categorias ordinarias ya aceptadas |
| `bloquear_por_uso_clinico` | aparece persona real, diagnostico, consejo o intervencion |

## Guardrails

- No abrir subfrente psicopatologico.
- No usar lenguaje de trastornos.
- No diagnosticar ni evaluar personas.
- No recomendar tratamiento, conducta, terapia o intervencion.
- No convertir los patrones en categorias clinicas.
- No promover a Canon, documento oficial o criterio general.
- No vincular con `HXI-001`, `H-Xi`, `P-107` o Concordancia sin decision separada.

## Deudas abiertas

- Probar `PSI-FRON-MAT-001` con nuevos casos abstractos solo si una decision posterior lo autoriza.
- Decidir si el nombre `psicopatologia conceptual no clinica` debe sustituirse por una etiqueta menos ambigua.
- Mantener `PSI-FRON-CAS-006` bloqueado como control negativo.
- No abrir subfrente patologico ni clinico.
- No tratar la matriz como Canon ni criterio clinico.

## Resultado

`PSI-FRON-MAT-001` queda como matriz provisional no clinica de frontera conceptual dentro de `PSI-001`.

No abre subfrente patologico.

No habilita uso clinico.

No canoniza contenido.
