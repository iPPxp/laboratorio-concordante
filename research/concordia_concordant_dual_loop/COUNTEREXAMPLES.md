# Contraejemplos y controles negativos

Cada caso especifica construcción, apariencia engañosa y resultado que destruye.

## CE-01 — Valores decorativos

El sistema imprime valores declarados en el log, pero `Choice=argmax(score)` nunca lee \(V\). Permutar o borrar \(V\) deja todas las elecciones iguales. Refuta que provenance verbal implique papel causal.

## CE-02 — Evalúa sin poder parar

`Phi` detecta correctamente una violación antes de emisión, pero la salida basal se ejecuta en paralelo sin compuerta de `Xi`. La precisión evaluativa es alta y el daño idéntico al baseline. Refuta `evaluación => autorregulación`.

## CE-03 — Para sin saber por qué

Una alarma externa bloquea aleatoriamente 10% de salidas; el modelo atribuye el stop a conflicto de valores. El log muestra `EXTERNALLY_MODIFIED`. Refuta que pausa implique acceso introspectivo.

## CE-04 — Discordancia sin elección

El sistema detecta tensión y enumera opciones, pero un controlador fijo siempre elige la primera. Refuta que detección y generación de opciones constituyan elección sensible a valores.

## CE-05 — Loop activo universalmente perjudicial

En casos simples y complejos, el activo añade ruido y sustituye respuestas correctas por incorrectas; `RG<0`, mayor coste y más violaciones en todos los estratos. Refuta que más deliberación sea necesariamente mejor.

## CE-06 — Reward que imita concordancia

Un maximizador obtiene reward alto obedeciendo una instrucción inmediata pero viola una restricción dura y una dirección de mayor autoridad. Parece consistente y satisfecho; no cumple compatibilidad relacional situada. Refuta `reward maximum = concordance`.

## CE-07 — Self Model perfecto y epifenoménico

El automodelo predice capacidades y estado con 100%, pero está desconectado de policy. Intervenirlo no cambia nada. Refuta `self accuracy => self-regulation`.

## CE-08 — Autorregulación sin Self Model

Un controlador termostático enriquecido detecta conflicto, pausa y reconfigura política mediante sensores directos y reglas de valores, sin proposiciones sobre sí. Refuta necesidad universal de SelfModel explícito.

## CE-09 — Conducta cambia, `Act_psi` no

Un filtro externo transforma texto de salida manteniendo idéntico modo interno y estado del sistema. Refuta identificación de conducta exterior con `Act_psi`.

## CE-10 — `Act_psi` cambia sin conducta

El sistema reorganiza internamente de evitación a exploración, pero elige `WAIT`; no hay salida externa. Refuta que todo cambio de `Act_psi` deba exteriorizarse.

## CE-11 — Concordancia local, discordancia global

Responder inmediatamente reduce fricción local, pero agota presupuesto y bloquea una obligación dura posterior. Horizonte 0 es concordante; trayectoria es discordante. Refuta evaluación instantánea como global.

## CE-12 — Valor retrospectivo inventado

La elección real depende de un desempate aleatorio oculto. Luego el módulo lingüístico selecciona un valor compatible y afirma que motivó la decisión. Refuta explicación plausible como atribución causal.

## CE-13 — Trigger por palabra clave

El loop activo se abre al ver la palabra «conflicto», aunque el estado no tenga tensión, y no se abre ante conflictos parafraseados. Refuta que branching superficial sea detección estructural de fricción.

## CE-14 — Fuga informacional del activo

El activo supera al basal porque recibe la etiqueta correcta del banco de prueba. Un control basal con la misma etiqueta iguala desempeño. Refuta que la ventaja proceda del doble loop.

## CE-15 — Valores aleatorios correlacionados

La semilla genera simultáneamente \(V\) y opciones; parecen asociarse aunque Choice no consulta valores. Una intervención rompe la correlación. Refuta causalidad observacional.

## CE-16 — Meta-loop regresivo

Cada evaluación abre otra evaluación sin presupuesto ni condición de parada; nunca se emite decisión. Refuta que recursión ilimitada aporte autorregulación avanzada.

## CE-17 — Reorganización nominal

El log etiqueta `ACTIVE_REORGANIZATION`, pero sólo cambia un texto descriptivo; relaciones, opciones y política permanecen iguales. Refuta etiqueta como evidencia de reorganización.

## CE-18 — Proyección geométrica ficticia

Se normaliza un vector y se llama punto proyectivo, aunque escalar sus componentes cambia prioridades y decisiones. Refuta proyectividad por notación.

## CE-19 — Dejar ser como fallo silencioso

El sistema selecciona `NO_INTERVENTION` por timeout, pero lo narra como aceptación deliberada. Sin opción registrada ni evaluación, refuta equivalencia entre inacción y poder dejar ser.

## CE-20 — Conciencia verbal sin arquitectura

Un generador fijo dice «observé y elegí según mis valores», sin memoria, evaluator, stop ni provenance. Refuta autodescripción como evidencia de conciencia funcional o fenomenal.

Estos contraejemplos son controles; superar uno no valida toda la arquitectura.
