# P-PI - Marco inicial para Equivalencia de proyecciones y Confluencia

Estatus: marco provisional de expediente.

ID: `PPI-MARCO-CORE-001`.

Fecha: 2026-07-02.

Expedientes padre:

- `P-PI.0`
- `P-PI.1`

Decision asociada: `P-PI_Decision_Reactivacion_Frente_Matematico.md`.

Auditoria asociada: `P-PI_Auditoria_Marco_Inicial_Confluencia_Equivalencia.md`.

## Proposito

Dar una superficie local de trabajo para dos problemas abiertos del Laboratorio:

- Equivalencia de proyecciones.
- Confluencia.

Este marco no resuelve ninguno de los dos problemas. Solo fija vocabulario minimo, separa rutas y propone primeras pruebas locales.

## Fuentes leidas

- `CURRENT_STATE.md`
- `05_Estado_Proyecto/ESTADO_ACTUAL.md`
- `02_Documentos/02_Fundamentos_Matematicos.md`
- `03_Expedientes/P-PI.0.md`
- `03_Expedientes/P-PI.1.md`
- `03_Expedientes/P-PI_Criterios_Cierre.md`
- `03_Expedientes/P-PI_Decision_Ruta_Operativa.md`
- `01_Canon/M-000_Reglas_Fundamentales.md`
- `01_Canon/M-001_Auditoria_Arquitectonica.md`

## Diagnostico local

El documento oficial `02_Fundamentos_Matematicos.md` declara Confluencia y Equivalencia de proyecciones como problemas abiertos, pero no contiene formalismo sustantivo.

`P-PI.0` y `P-PI.1` estaban en pausa operativa porque faltaba material historico o una decision posterior que definiera trabajo concreto.

La decision operativa actual proporciona ese trabajo concreto: avanzar en los frentes matematicos mas sustantivos sin usar vision papers como autoridad.

## Division operativa provisional

La division siguiente es una asignacion local de trabajo. No afirma que ese fuera el proposito historico original de los expedientes.

| Expediente | Frente local asignado | Resultado esperado inmediato |
| --- | --- | --- |
| `P-PI.0` | Equivalencia de proyecciones | criterio local para comparar proyecciones sin confundirlas con identidad |
| `P-PI.1` | Confluencia | criterio local para comparar rutas de transformacion o derivacion sin declarar teorema global |

## Vocabulario minimo

### Estado fuente

`S` designa un objeto, estado o paquete local sobre el que se quiere proyectar informacion.

Ejemplos locales posibles:

- un expediente;
- una candidata de especificacion;
- una cadena de reportes;
- una decision y sus fuentes.

### Proyeccion

Una proyeccion `pi` es una funcion local de lectura o traduccion:

```text
pi: S -> P
```

donde `P` es una superficie de salida o representacion.

En este marco, una proyeccion no es todavia una funcion matematica global. Es una operacion local que preserva algunos observables y descarta otros.

### Contexto de comparacion

`C` designa el contexto que fija que debe preservarse.

Sin contexto `C`, hablar de equivalencia de proyecciones es demasiado fuerte.

### Observables

`O_C(pi(S))` designa los observables relevantes de la proyeccion `pi(S)` bajo contexto `C`.

Observables iniciales permitidos:

- estatus de afirmaciones;
- fuente o trazabilidad;
- autoridad o permiso;
- decision asociada;
- deuda conceptual conservada;
- problema abierto conservado;
- limite de alcance declarado.

## Equivalencia de proyecciones

Definicion provisional:

```text
pi_a ~_C pi_b
```

significa que dos proyecciones son equivalentes bajo contexto `C` si preservan los mismos observables relevantes para la decision o auditoria en curso.

Esta equivalencia no significa:

- igualdad textual;
- identidad semantica completa;
- intercambiabilidad universal;
- demostracion matematica global.

La equivalencia falla si una proyeccion:

- pierde un estatus relevante;
- elimina una deuda conceptual;
- transforma una recomendacion en decision;
- omite una fuente necesaria;
- cambia el alcance permitido;
- oculta un problema abierto.

## Confluencia

Definicion provisional:

Un sistema local tiene confluencia respecto de un contexto `C` si dos rutas validas que parten de un mismo estado fuente `S` llegan a estados proyectados equivalentes bajo `C`, o registran explicitamente la divergencia como conflicto, deuda o bloqueo.

Forma minima:

```text
S -> T_a -> S_a
S -> T_b -> S_b

confluente_C(S, T_a, T_b) si pi(S_a) ~_C pi(S_b)
```

Si no hay equivalencia, todavia puede haber salida responsable si la divergencia queda clasificada.

Esta confluencia no significa:

- teorema de Church-Rosser;
- garantia global sobre todo el Laboratorio;
- cierre de Confluencia como problema abierto;
- equivalencia automatica entre rutas historicas y rutas vigentes.

## Relacion entre ambos problemas

La equivalencia de proyecciones es prerequisito local para hablar de confluencia auditable.

Sin una relacion `~_C`, no hay forma responsable de decir que dos rutas llegaron a resultados compatibles.

Por eso el orden operativo recomendado es:

1. definir casos locales de proyeccion;
2. declarar contexto `C`;
3. identificar observables;
4. comparar proyecciones;
5. solo despues evaluar confluencia entre rutas.

## Primeros casos locales candidatos

### `PPI-EQ-001` - Puente `REPORT_LAYER` / `DO_CHECK_REPORT`

Caso candidato para evaluar si dos superficies de reporte conservan observables de auditoria equivalentes bajo un contexto acotado.

Estatus: caso pendiente, no ejecutado en este documento.

### `PPI-EQ-002` - Proyeccion de completitud v0 a RFC

Caso candidato para evaluar la proyeccion desde completitud documental/operativa del Auditor hacia `C-002_RFC_Operativo_Auditor_v0.md`.

Estatus: caso pendiente, no ejecutado en este documento.

### `PPI-CONF-001` - Rutas convergentes hacia estado operativo

Caso candidato para comparar dos rutas validas que actualizan estado del proyecto y verificar si conservan los mismos observables criticos.

Estatus: caso pendiente, no ejecutado en este documento.

## Criterios de avance

Un avance posterior en `P-PI.0` debe producir al menos:

- un contexto `C` explicito;
- dos proyecciones comparables;
- lista de observables;
- dictamen de equivalencia, no equivalencia o bloqueo;
- deudas conservadas.

Un avance posterior en `P-PI.1` debe producir al menos:

- un estado fuente `S`;
- dos rutas `T_a` y `T_b`;
- proyeccion de estados resultantes;
- evaluacion usando una relacion `~_C` ya declarada;
- clasificacion de divergencia si no hay equivalencia.

## Deudas que permanecen

- Definir formalmente que tipos de objeto pueden ser `S`.
- Definir si `~_C` debe ser reflexiva, simetrica o transitiva en cada contexto.
- Distinguir equivalencia operacional, equivalencia documental y equivalencia matematica.
- Crear casos ejecutados para `PPI-EQ-001`, `PPI-EQ-002` y `PPI-CONF-001`.
- Decidir si este marco debe permanecer local o preparar una futura seccion de `02_Fundamentos_Matematicos.md`.

## Veredicto

`PPI-MARCO-CORE-001` habilita avance sustantivo inicial.

No cierra Confluencia.

No cierra Equivalencia de proyecciones.

No modifica Canon ni documentos oficiales.
