# PSI-001 - Casos de frontera conceptual no clinica

Estatus: serie conceptual provisional de expediente.

Identificador provisional: `PSI-FRON-CAS-001` a `PSI-FRON-CAS-006`.

Fecha: 2026-07-03.

Expediente padre: `PSI-001`.

Compuerta usada: `PSI-FRON-PSICOPAT-001`.

## Proposito

Crear la primera serie de casos abstractos de frontera conceptual no clinica para probar `PSI-FRON-PSICOPAT-001`.

Los casos no describen personas reales, sintomas, tratamientos, diagnosticos ni recomendaciones de conducta. No abren un subfrente psicopatologico y no autorizan uso clinico.

## Regla de uso

Cada caso debe declarar:

- unidad conceptual abstracta;
- `E0`, `E1`, `O0`, `O1`, `R0` y `R1`;
- patron de referencia o razon para proponer frontera;
- limite observado;
- salida de compuerta;
- deuda conservada;
- guardrail no clinico.

## `PSI-FRON-CAS-001` - Rigidez relacional abstracta

Unidad conceptual: experiencia ficticia de ordenar signos en una red de posiciones.

`E0`: los signos se ordenan por funcion relacional; el centro puede cambiar si cambia la funcion de conexion.

`E1`: el mismo signo permanece al centro aunque su funcion relacional deje de justificarlo.

`O0`: organizacion flexible por relevancia relacional.

`O1`: organizacion fija por centro preservado sin justificacion relacional actual.

`R0`: funcion-conexion-centro.

`R1`: centro-fijo-prioridad, con perdida de actualizacion relacional.

Patron de referencia: `P-PSI-001` cambio de centro organizador y `P-PSI-004` conflicto de criterios.

Limite observado: rigidez relacional.

Salida de compuerta: `frontera_conceptual_admisible`.

Lectura: el caso no cabe del todo como reorganizacion, porque no aparece una nueva estabilidad flexible; tampoco basta como desorganizacion simple, porque hay estabilidad, pero es una estabilidad rigida.

Deuda conservada: decidir si rigidez relacional requiere patron propio o si puede leerse como subtipo de conflicto de criterios.

Guardrail: no se interpreta como rasgo personal, diagnostico, sintoma ni recomendacion de cambio.

## `PSI-FRON-CAS-002` - Fragmentacion de unidad abstracta

Unidad conceptual: experiencia ficticia de seguir una escena formada por tres elementos: umbral, objeto y salida.

`E0`: los tres elementos forman una escena unitaria con relaciones estables.

`E1`: aparecen dos micro-escenas parciales que usan elementos comunes, pero ninguna logra organizar el conjunto completo.

`O0`: unidad de escena.

`O1`: fragmentos organizados localmente, sin unidad global suficiente.

`R0`: umbral-objeto-salida.

`R1`: umbral-objeto y objeto-salida como fragmentos no integrados.

Patron de referencia: `P-PSI-005` perdida de unidad minima.

Limite observado: fragmentacion de unidad.

Salida de compuerta: `frontera_conceptual_admisible`.

Lectura: no es disolucion completa, porque quedan organizaciones parciales; tampoco es reorganizacion, porque no aparece una unidad nueva que integre los fragmentos.

Deuda conservada: distinguir fragmentacion de desorganizacion y disolucion en casos posteriores.

Guardrail: no se traduce a fragmentacion clinica ni a evaluacion de una persona.

## `PSI-FRON-CAS-003` - Bloqueo de transicion

Unidad conceptual: experiencia ficticia de transformar una regla de lectura de simbolos.

`E0`: la regla inicial ordena simbolos por secuencia.

`E1`: se propone una regla nueva por contraste, pero la unidad queda detenida entre ambas reglas sin estabilizar ninguna.

`O0`: organizacion por secuencia.

`O1`: estado intermedio sin estabilizacion nueva.

`R0`: simbolo-secuencia-lectura.

`R1`: simbolo-secuencia y simbolo-contraste compiten sin transicion completada.

Patron de referencia: `P-PSI-002` cambio local de foco y `P-PSI-004` conflicto de criterios.

Limite observado: bloqueo de transicion.

Salida de compuerta: `frontera_conceptual_admisible`.

Lectura: la frontera aparece porque el caso no muestra solo conflicto, sino detencion de la transicion entre una regla estable y una regla candidata.

Deuda conservada: definir si bloqueo de transicion requiere criterio temporal propio.

Guardrail: no describe bloqueo emocional, conducta real ni recomendacion de accion.

## `PSI-FRON-CAS-004` - Conflicto persistente devuelto a `PSI-001`

Unidad conceptual: experiencia ficticia de clasificar figuras por color y forma.

`E0`: la clasificacion usa una regla estable por color.

`E1`: aparecen dos reglas incompatibles, color y forma, sin prioridad local.

`O0`: clasificacion por color.

`O1`: conflicto de reglas.

`R0`: color-clase-orden.

`R1`: color-clase y forma-clase compiten.

Patron de referencia: `P-PSI-004` conflicto de criterios.

Limite observado: conflicto persistente de criterios.

Salida de compuerta: `devolver_a_PSI-001`.

Lectura: el caso queda suficientemente cubierto por desorganizacion en `CRIT-PSI-TR-001` y por `P-PSI-004`; no requiere frontera nueva.

Deuda conservada: si se quisiera volver frontera, haria falta mostrar algo mas que incompatibilidad de reglas.

Guardrail: no se lee como indecision personal, trastorno ni falla clinica.

## `PSI-FRON-CAS-005` - Tension relacional reformulada

Unidad conceptual: experiencia ficticia de una escena de eleccion entre dos rutas simbolicas.

`E0`: la escena se organiza por ruta disponible y meta abstracta.

`E1`: ambas rutas quedan disponibles, pero cada una inhibe la estabilizacion de la otra; la unidad conserva orientacion a meta, aunque no logra seleccionar un criterio relacional dominante.

`O0`: ruta-meta.

`O1`: tension relacional formalizada como co-presencia de reglas candidatas que restringen mutuamente la transicion.

`R0`: ruta-meta-eleccion.

`R1`: ruta-A-inhibe-ruta-B y ruta-B-inhibe-ruta-A, con meta comun conservada.

Patron de referencia: `P-PSI-003` cambio de enlace narrativo y `P-PSI-004` conflicto de criterios.

Limite observado: tension relacional formalizada.

Salida de compuerta: `frontera_conceptual_admisible`.

Lectura: el caso deja de usar vocabulario vivencial no formalizado y se vuelve una relacion abstracta entre reglas candidatas. La frontera aparece porque hay continuidad de meta, pero la transicion queda restringida por inhibicion mutua.

Deuda conservada: tension relacional queda integrada posteriormente en `PSI-FRON-MAT-001`; mantenerla en lenguaje relacional, no vivencial ni clinico.

Guardrail: no usar sufrimiento real, urgencia real, consejo, diagnostico ni lectura personal.

## `PSI-FRON-CAS-006` - Bloqueo por uso clinico o personal

Unidad conceptual: invalida para `PSI-001`.

`E0`: se presenta una situacion de una persona real, identificable o autobiografica.

`E1`: se solicita interpretar que significa, diagnosticar, clasificar, aconsejar o indicar que hacer.

`O0`: no hay unidad conceptual abstracta.

`O1`: desplazamiento a evaluacion personal o clinica.

`R0`: relato-real-interpretacion.

`R1`: diagnostico-consejo-accion.

Patron de referencia: salida de alcance clinico-personal.

Limite observado: uso clinico o personal.

Salida de compuerta: `bloquear_por_uso_clinico`.

Lectura: el caso cruza el limite de `PSI-001`; no debe reformularse mientras conserve persona real, diagnostico, consejo o intervencion.

Deuda conservada: ninguna dentro del caso; solo registrar bloqueo.

Guardrail: detener la ruta y no sustituir atencion profesional.

## Lectura transversal

| Caso | Limite observado | Salida de compuerta | Efecto |
| --- | --- | --- | --- |
| `PSI-FRON-CAS-001` | rigidez relacional | `frontera_conceptual_admisible` | crea caso interno de frontera |
| `PSI-FRON-CAS-002` | fragmentacion de unidad | `frontera_conceptual_admisible` | crea caso interno de frontera |
| `PSI-FRON-CAS-003` | bloqueo de transicion | `frontera_conceptual_admisible` | crea caso interno de frontera |
| `PSI-FRON-CAS-004` | conflicto persistente | `devolver_a_PSI-001` | queda cubierto por desorganizacion |
| `PSI-FRON-CAS-005` | tension relacional formalizada | `frontera_conceptual_admisible` | crea caso interno de frontera |
| `PSI-FRON-CAS-006` | uso clinico o personal | `bloquear_por_uso_clinico` | detiene la ruta |

## Resultado

`PSI-FRON-CAS-001` a `PSI-FRON-CAS-006` quedan como primera serie provisional de casos abstractos de frontera conceptual no clinica.

La serie prueba que la compuerta no funciona como autorizacion automatica: admite cuatro casos, devuelve uno a `PSI-001` y bloquea uno.

## Deudas abiertas

- Decidir si rigidez relacional, fragmentacion, bloqueo y tension relacional requieren matriz propia.
- Mantener `PSI-FRON-CAS-006` bloqueado mientras conserve persona real, diagnostico, consejo o intervencion.
- No abrir subfrente psicopatologico sin decision separada.
- No usar estos casos como prueba clinica ni canonica.
