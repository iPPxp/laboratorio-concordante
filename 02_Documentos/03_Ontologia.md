# 03 - Ontologia

Estatus: documento oficial consolidado.

Decision de consolidacion: `D-2026-07-03-011`.

Fuentes principales: documento semilla previo, `SRC-010`, `SRC-012`, `SRC-013`, `SRC-023`, Canon vigente, `AUD-001`, `AO-001`, estado vigente del proyecto.

## Proposito

Este documento fija las entidades principales del Laboratorio Concordante y sus relaciones.

La ontologia del Laboratorio es operacional: no intenta decidir que existe en la realidad, sino que entidades necesita el repositorio para distinguir estatus, autoridad, evidencia, operaciones y cambios.

## Principio ontologico local

Una entidad del Laboratorio existe operativamente cuando cumple al menos una de estas funciones:

- clasificar una afirmacion;
- declarar un estatus;
- conservar trazabilidad;
- permitir auditoria;
- sostener una decision;
- delimitar una operacion;
- marcar una deuda;
- impedir una promocion indebida.

Si una entidad no cumple ninguna funcion operativa, debe justificarse o retirarse.

## Entidades de gobierno

### Laboratorio

Arquitectura de investigacion y repositorio local que gobierna modelos explicativos, documentos, expedientes, decisiones y trazabilidad.

### Canon

Conjunto minimo de reglas fundamentales que limita como cambia el Laboratorio.

### Documento oficial

Texto vigente por tema. Representa conocimiento aceptado del Laboratorio, subordinado al Canon y al estado.

### Documento de Nivel C

Especificacion tecnica oficial. Vive en `02_Documentos`, pero su funcion es mas tecnica y acotada que la de los documentos generales.

### Expediente

Unidad de investigacion. Puede proponer, probar, auditar y preparar cambios, pero no es verdad vigente por si mismo.

### Registro historico

Zona de trazabilidad. Conserva fuentes, conversaciones y paquetes previos. No es autoridad directa.

### Estado del proyecto

Superficie operativa que resume que esta vigente, abierto, cerrado, congelado, transferido o pendiente.

### Decision

Acto explicito que cambia o fija estatus: abre, acepta, cierra, congela, rechaza, transfiere, incorpora o promueve.

### Auditoria

Evaluacion de coherencia, estatus, dependencias, deudas, impacto y frontera de una intervencion.

### Validacion

Prueba local de una afirmacion, algoritmo, criterio o compatibilidad bajo condiciones declaradas.

## Entidades de contenido

### Definicion

Fija vocabulario y alcance.

### Hipotesis

Propuesta activa o materializada, no demostrada ni canonizada.

### Teorema

Resultado demostrado dentro de hipotesis y frontera declaradas.

### Algoritmo

Procedimiento ejecutable o formalizable con entrada, salida y condicion de terminacion.

### Deuda conceptual

Dependencia, ambiguedad o ausencia que impide usar una afirmacion como fundamento pleno.

### Problema abierto

Pregunta reconocida sin resolucion estable.

### Criterio

Regla de evaluacion que permite aceptar, detener, bloquear, escalar o comparar.

### Protocolo

Secuencia de pasos para admision, auditoria, validacion, reduccion, demolicion, actualizacion o cierre.

## Entidades de modelos explicativos

### Modelo

Objeto estructural auditado.

Una definicion funcional incorporada desde `SRC-023` dice que una estructura es modelo si:

1. selecciona un dominio;
2. distingue estados;
3. restringe transiciones;
4. relaciona observaciones con transiciones permitidas.

### Explicacion

Estructura justificativa que permite sostener por que un modelo merece continuar frente a alternativas.

### Dominio

Espacio operacional o conjunto de posibilidades donde se definen estados, observaciones, restricciones y transiciones.

### Observacion

Elemento admisible para evaluar, distinguir o activar una transicion dentro de un dominio.

### Estado

Configuracion distinguible dentro de un modelo o artefacto.

### Transicion

Paso permitido o bloqueado entre estados.

### Restriccion

Condicion que limita transiciones, operaciones o interpretaciones.

### Firma estructural

Patron tipado que puede ser satisfecho por un modelo.

### Firma preservable

Firma estructural designada como preservable por un protocolo de auditoria.

### Invariante

Firma preservable efectivamente satisfecha por el modelo auditado.

### Grafo de acoplamiento

Grafo que relaciona invariantes por solapamiento estructural.

### Ruptura

Perdida de satisfaccion de una firma preservable.

### Componente de ruptura

Zona de riesgo estructural asociada a una ruptura.

## Entidades operacionales

### Artefacto

Objeto local sobre el que puede operar el Laboratorio: documento, expediente, reporte, decision, fuente, traza, algoritmo o pieza de estado.

### Estatus

Clasificacion obligatoria que evita promocion tacita.

### Evidencia

Fuente local materializada que sostiene una afirmacion, auditoria, validacion o decision.

### Reporte

Salida estructurada de lectura, calculo, falla, decision, propuesta, ejecucion o verificacion.

### Permiso

Autorizacion acotada que habilita o bloquea una transformacion. No se deduce automaticamente de una decision favorable.

### Transformacion

Cambio propuesto o ejecutado sobre un artefacto.

### Verificacion

Comprobacion posterior de que una transformacion conservo las condiciones declaradas.

### Bloqueo

Salida segura cuando faltan evidencia, estatus, permiso, invariantes, contexto o verificacion.

### Traza

Secuencia finita de eventos operativos: reportes, decisiones, propuestas, ejecuciones, fallos o verificaciones.

### Generalizacion controlada

Operacion que extrae una forma candidata desde evidencia local, con contexto, invariantes, restricciones, deudas y salida segura.

## Relaciones de gobierno

- El Canon limita documentos, expedientes, decisiones y automatizaciones.
- El estado del proyecto orienta la lectura operativa vigente.
- Un documento oficial puede incorporar resultados de expedientes.
- Un expediente puede depender de hipotesis activas.
- Una decision puede abrir, aceptar, cerrar, congelar, transferir, incorporar o rechazar.
- Una auditoria puede recomendar, pero no decide por si misma.
- Una validacion puede apoyar una decision, pero no promueve automaticamente.
- Una deuda conceptual puede bloquear una promocion.
- El registro historico puede justificar trazabilidad, pero no autoridad directa.

## Relaciones de modelos

- Un modelo opera sobre un dominio.
- Un dominio admite observaciones, estados y transiciones.
- Una restriccion limita transiciones o interpretaciones.
- Una firma puede ser satisfecha por un modelo.
- Una firma preservable satisfecha se vuelve invariante.
- Los invariantes pueden acoplarse en `G_I`.
- Una ruptura produce una componente `Break(F_k)`.
- Si `Activas(G)` intersecta una componente de ruptura, la salida puede ser `INCONSISTENTE`.

## Relaciones operacionales

- Un reporte debe preceder a una decision fundada.
- Una decision fundada no equivale a permiso material.
- Un permiso debe declarar alcance.
- Una transformacion valida requiere evidencia previa, decision fundada, permiso acotado, invariante y verificacion posterior.
- Un reporte bloqueante produce bloqueo, deuda o escalamiento, no transformacion.
- Una generalizacion controlada no aumenta el permiso operativo de sus fuentes.
- Una fuente de nivel inferior no modifica por si misma una fuente de nivel superior.

## Estatus de afirmaciones

Toda afirmacion relevante debe clasificarse como una de estas categorias:

- definicion;
- hipotesis;
- teorema;
- algoritmo;
- expediente;
- decision;
- deuda conceptual;
- problema abierto.

Si no puede clasificarse, debe tratarse como deuda conceptual.

## Estados de artefactos y frentes

Un expediente o frente puede estar:

- abierto;
- activo acotado;
- en pausa operativa;
- cerrado;
- congelado;
- transferido;
- rechazado;
- absorbido;
- incorporado a documento;
- promovido a Canon o Nivel C solo por proceso explicito.

## Fronteras ontologicas vigentes

- `H-Xi` esta materializada pero no admitida como Canon ni documento oficial.
- `R4-FORMAL-AUD-001` es construccion formal local de `AUD-001`, no regla canonica global.
- `GAMMA-FORMAL-AUD-001` es operador parcial local de `AUD-001`, no teoria global.
- `PSI-001` fue independizado; su contenido queda como copia de traspaso, no frente interno activo.
- `Concordance` puede investigarse como propiedad dinamica o teoria de sistemas, pero no esta canonizada.

## Deudas ontologicas abiertas

Permanecen abiertas:

- diferencia formal completa entre modelo y explicacion;
- independencia ontologica del dominio;
- equivalencia entre modelos;
- viabilidad mutacional;
- relacion entre `Xi`, dominio, restricciones y observaciones;
- estatuto formal de concordancia;
- exportacion de R4/Gamma fuera de `AUD-001`;
- tipologia completa de operaciones de la Algebra Operacional.

## Estado

Documento 03 queda consolidado como ontologia oficial del Laboratorio.

Debe auditarse contra nuevos expedientes reales cada vez que una entidad cambie de funcion o autoridad.
