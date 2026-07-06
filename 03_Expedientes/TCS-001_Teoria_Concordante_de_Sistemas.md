# TCS-001 - Teoria Concordante de Sistemas

Estatus: propuesta teorica inicial de expediente.

Fecha: 2026-07-02.

Nombre provisional: `Teoria Concordante de Sistemas`.

Nombre alternativo: `Concordance Theory`.

## Objeto

`TCS-001` propone convertir `Concordance` de concepto rector a teoria minima sobre gobernanza de sistemas heterogeneos.

La teoria no queda canonizada por este documento. Este expediente solo fija una formulacion inicial para auditoria, comparacion, critica y desarrollo posterior.

## Tesis central

Un sistema complejo no es gobernable solo porque sus componentes esten coordinados, alineados, controlados o en cumplimiento.

Un sistema es concordante cuando preserva relaciones coherentes entre conocimiento, autoridad, permisos, decisiones, responsabilidades y procesos computacionales mientras cambia.

## Axiomas fundacionales

### Axioma I - Los sistemas operativos generan afirmaciones

Todo sistema operativo produce continuamente afirmaciones explicitas o implicitas sobre su estado, entorno, objetivos o conducta esperada.

Sin afirmaciones, la gobernanza no tiene objeto.

### Axioma II - Las afirmaciones poseen estatus

Toda afirmacion tiene un estatus epistemico u operativo.

El estatus puede ser provisional, validado, rechazado, historico, ejecutable o canonico.

La gobernanza empieza al conservar la diferencia entre estos estatus.

### Axioma III - La autoridad deriva del estatus

La autoridad no surge por repeticion, conveniencia o generacion computacional.

La autoridad se asigna explicitamente mediante mecanismos reconocidos de gobernanza.

### Axioma IV - Las decisiones requieren autoridad explicita

Ninguna recomendacion, observacion, inferencia o salida automatizada se convierte en decision salvo que un proceso autorizado de gobernanza la transforme en decision.

### Axioma V - La trazabilidad precede a la responsabilidad

Un sistema no puede responder por acciones cuyo origen, justificacion o autorizacion no pueden reconstruirse.

### Axioma VI - La automatizacion nunca implica autorizacion

La automatizacion puede asistir la gobernanza.

La automatizacion nunca reemplaza la gobernanza.

### Axioma VII - La gobernanza permanece revisable

Los metodos mismos quedan sujetos a inspeccion, critica y revision controlada.

Ningun componente del marco de gobernanza queda permanentemente exento de auditoria.

### Axioma VIII - La concordancia se preserva mediante revision explicita

Los sistemas estables no son los que evitan el cambio.

Los sistemas estables son capaces de cambiar sin perder la coherencia de su estructura de autoridad.

## Definicion propuesta

`Concordance` es una propiedad observable y auditable de sistemas heterogeneos que describe su capacidad para preservar relaciones coherentes entre conocimiento, autoridad, permisos, decisiones, responsabilidades y procesos computacionales mientras se adaptan a restricciones cambiantes.

Por tanto, `Concordance` no es una medida de acuerdo.

Es una propiedad de gobernanza.

## Frase rectora

El acuerdo puede existir sin concordancia. La concordancia tambien puede existir pese al desacuerdo. La concordancia concierne a la gobernanza del desacuerdo, no a su eliminacion.

## Diferenciacion conceptual

| Concepto | Pregunta primaria |
| --- | --- |
| Management | Como se ejecuta el trabajo? |
| Coordination | Como interactuan las actividades? |
| Control | Como se restringe la conducta? |
| Compliance | Se siguen las reglas? |
| Alignment | Son compatibles los objetivos? |
| Governance | Quien posee autoridad legitima? |
| Concordance | El sistema preserva autoridad coherente bajo cambio? |

## Ontologia minima de investigacion

```text
System
|
+-- Agent
+-- Institution
+-- Model
+-- Constraint
+-- Protocol
+-- Claim
|   |
|   +-- Evidence
|   +-- Status
|   +-- Decision
|
+-- Governance
    |
    +-- Authority
    +-- Permission
    +-- Accountability
    +-- Concordance
```

## Relacion con el Laboratorio Concordante

El Laboratorio Concordante puede tratarse como el primer sistema experimental de `TCS-001`.

Sus capas actuales ya expresan componentes teoricos:

- Canon: reglas de autoridad superior.
- Documentos oficiales: estado vigente estabilizado.
- Expedientes: investigacion no canonizada.
- Registro Historico: memoria sin autoridad operativa directa.
- Estado del Proyecto: continuidad operacional.
- Auditor: automatizacion no mutante para trazabilidad, estatus y permisos.

La teoria no se deduce automaticamente de estas capas, pero puede formalizarlas.

## Preguntas de investigacion

- Que condiciones minimas hacen que un sistema sea concordante?
- Como se detecta perdida de concordancia?
- Puede haber concordancia local y discordancia global?
- Que diferencia formal existe entre alineacion y concordancia?
- Como se representa el estatus de una afirmacion en sistemas humano-IA?
- Que tipo de automatizacion puede asistir la concordancia sin producir autoridad ilegitima?
- Como se revisa un metodo sin destruir la continuidad del sistema que depende de el?

## Criterios de avance

`TCS-001` podria avanzar hacia teoria mas robusta si produce:

- definiciones estables de `System`, `Claim`, `Status`, `Authority`, `Permission`, `Decision` y `Concordance`;
- ejemplos positivos y negativos de concordancia;
- una tipologia de fallos de concordancia;
- operadores o protocolos para preservar, restaurar o auditar concordancia;
- relacion formal con `C-001` y el Auditor;
- casos de prueba no triviales fuera del propio Laboratorio;
- criterios para distinguir teoria, metodologia y plataforma.

## Avance provisional 2026-07-03

El paquete minimo aceptado por `D-2026-07-03-019` atiende el primer nivel de esta deuda:

- `TCS-001_Definiciones_Minimas.md`: `TCS-DEF-MIN-001`.
- `TCS-001_Tipologia_Fallos_Concordancia.md`: `TCS-FAIL-TYP-001`.
- `TCS-001_Casos_Prueba.md`: `TCS-CASE-BAT-001`.

El paquete no canoniza `Concordance`, no crea Nivel C y no convierte `TCS-001` en teoria completa.

## Avance provisional 2026-07-05

La maduracion provisional aceptada por `D-2026-07-05-010` agrega:

- `TCS-001_Maduracion_Provisional.md`: `TCS-MAT-PROV-001`.
- `TCS-METRIC-PROV-001`: metrica cualitativa provisional de concordancia local.
- `TCS-EXT-CASE-001`: casos externos no regulados sobre paquete de software de juguete.
- `TCS-AUTH-CONF-001`: patron de conflicto entre autoridades validas.

Este avance no canoniza `Concordance`, no crea Nivel C, no abre dominios regulados y no convierte `TCS-001` en teoria completa.

## Riesgos conceptuales

- Convertir `Concordance` en sinonimo decorativo de alineacion.
- Confundir concordancia con consenso.
- Tratar la teoria como Canon antes de auditarla.
- Usar lenguaje institucional sin definiciones operativas.
- Ignorar dominios donde autoridad y responsabilidad estan reguladas externamente.

## Siguiente accion recomendada

Extender `TCS-001` desde el paquete minimo aceptado hacia:

- metricas o semantica formal de concordancia;
- casos externos;
- conflicto entre autoridades validas;
- relacion con dominios regulados;
- distincion entre teoria, metodologia y plataforma.

`VISION_PAPER_PROPUESTA.md` y `VISION_PAPER_FINAL_REFERENCIAS.md` quedan inactivos por `D-2026-07-02-031` y no deben usarse como fuente activa para esta auditoria.

`TCS-001` queda como propuesta teorica abierta y provisional; cualquier promocion futura requiere auditoria y decision separada.
