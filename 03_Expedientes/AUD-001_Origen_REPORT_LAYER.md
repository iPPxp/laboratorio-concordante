# AUD-001 - Origen interno de REPORT_LAYER

Estatus: mapa provisional de extraccion de expediente.

Expediente padre: `AUD-001`.

Objeto: `REPORT-LAYER-CAND-001`.

Documento asociado: `03_Expedientes/AUD-001_REPORT_LAYER_Candidata.md`.

## Pregunta

De donde dentro del Laboratorio se extrae la capa abstracta `REPORT_LAYER`?

## Respuesta corta

`REPORT_LAYER` se extrae por abstraccion desde cinco superficies internas ya registradas:

1. `M-000` y `M-001`: reglas de estatus, trazabilidad, deuda y auditoria.
2. `C-001`: especificacion tecnica oficial del Auditor.
3. `AUD-001_Contrato_Reportes.md`: gramatica concreta de reportes.
4. `AUD-001_Validaciones.md` y `AUD-001_Simulaciones.md`: casos que muestran que partes de la gramatica sobreviven fuera de automatas.
5. `DO-001_DO-CHECK-001.md`, `DO-001_Regla_Permiso_Actualizacion.md` y `DO-001_Decision_Modo_Operativo_Auditor.md`: frontera entre reporte, recomendacion, permiso y ejecucion.

La capa abstracta no se extrae del Registro Historico, de `Gamma`, de una Regla R4 formal inexistente ni de una teoria externa.

## Principio de extraccion

La extraccion permitida es:

```text
contratos concretos -> campos comunes -> funcion procedural -> capa abstracta
```

No es:

```text
hipotesis narrativa -> autoridad general -> especificacion oficial
```

Por tanto, `REPORT_LAYER` conserva solo lo que ya aparece repetidamente como requisito operativo en reportes, decisiones, validaciones y reglas de permiso.

## Superficie 1 - Canon minimo

De `M-000` se extraen obligaciones que todo reporte debe respetar:

- estatus obligatorio de afirmaciones;
- separacion de niveles;
- no promocion automatica;
- trazabilidad minima;
- historial no operativo;
- deuda conceptual antes de fundamento.

De `M-001` se extrae la forma de auditoria:

- fuentes leidas;
- hallazgos;
- impacto;
- deudas;
- recomendacion.

Esto justifica que `REPORT_ITEM` tenga campos como `estatus_afirmacion`, `dependencias`, `deudas_generadas`, `evidencia` y `decision_emitida`.

## Superficie 2 - C-001

De `C-001_Especificacion_Tecnica_Auditor.md` se extrae el alcance tecnico oficial del Auditor:

- lectura de fuentes locales autorizadas;
- verificacion de estatus;
- deteccion de dependencias no materializadas;
- deteccion de uso indebido del Registro Historico;
- emision de reportes normalizados;
- comparacion entre decision emitida y decision permitida;
- aplicacion de `PERMISO-ACT-001`;
- evidencia antes y despues;
- verificacion posterior.

Esto justifica que `REPORT_LAYER` no sea solo un formato de hallazgos, sino una capa de decision, permiso, ejecucion y verificacion.

## Superficie 3 - Contratos concretos de AUD-001

De `AUD-001_Contrato_Reportes.md` se extrae la gramatica concreta inicial:

- `OPERATOR_REPORT`;
- `MP_FAIL_REPORT`;
- `CR_FAIL_REPORT`;
- `TAU_REPORT`;
- `D_REPORT`;
- `TR_PROPOSAL_REPORT`;
- `TR_EXECUTION_REPORT`;
- `TR_EXECUTION_FAIL_REPORT`;
- `REVERSAL_REPORT`.

La abstraccion no copia los nombres como Canon. Los proyecta a funciones:

| Contrato concreto | Funcion abstracta |
| --- | --- |
| `MP_FAIL_REPORT` | reportar falla de mapeo |
| `CR_FAIL_REPORT` | reportar falla de calculo o verificacion |
| `TAU_REPORT` | cerrar terminacion segura |
| `D_REPORT` | emitir decision fundada |
| `TR_PROPOSAL_REPORT` | registrar propuesta no ejecutada |
| `TR_EXECUTION_REPORT` | registrar ejecucion autorizada |
| `TR_EXECUTION_FAIL_REPORT` | cortar ejecucion fallida |
| `REVERSAL_REPORT` | clasificar politica posterior al fallo |

De esa proyeccion salen `operador_abstracto` y `clase_reporte`.

## Superficie 4 - Validaciones y simulaciones

De `AUD-001_Validaciones.md` y `AUD-001_Simulaciones.md` se extrae que la estructura no depende solo de automatas.

La primera ronda no automata muestra:

- `VAL-017`: objeto documental no automata exige estatus, autoridad y bloqueo de promocion indebida.
- `VAL-018`: tabla de decisiones conflictiva exige interseccion responsable de permisos.
- `VAL-019`: expediente con Registro Historico exige distinguir traza de autoridad vigente.
- `VAL-020`: algoritmo textual exige terminacion segura.
- `VAL-021`: documento oficial incompleto exige autoridad parcial sin permiso transformativo implicito.

Estas validaciones justifican que `REPORT_LAYER` sea una capa abstracta de auditoria procedimental y no una extension de la teoria de automatas.

## Superficie 5 - DO-CHECK, permiso y modo operativo

De `DO-001_DO-CHECK-001.md` se extrae la existencia de un reporte no mutante que lee archivos y propone sin ejecutar.

De `DO-001_Regla_Permiso_Actualizacion.md` se extrae que una recomendacion no equivale a autorizacion.

De `DO-001_Decision_Modo_Operativo_Auditor.md` se extrae que:

```text
calculo y reporte -> ejecutable
autoridad y permiso -> asistido o decision registrada
ejecucion real -> ejecutable solo si esta previamente autorizada
```

Esto justifica la frontera entre:

- reporte;
- recomendacion;
- decision;
- permiso;
- ejecucion.

## Que se descarta

No se incorpora a `REPORT_LAYER`:

- estructura especifica de automatas: `Q`, `Sigma`, `delta`, `q0`, `F`;
- nombres concretos como obligatorios fuera de `AUD-001`;
- historia conversacional como autoridad;
- definicion formal de R4, porque no existe localmente;
- `Gamma`, porque no existe construccion local;
- serializacion ejecutable definitiva;
- politica de reversion materializada.

## Regla local de extraccion

Un elemento puede entrar en `REPORT_LAYER` solo si cumple las tres condiciones:

1. aparece como campo, regla o invariante en una fuente local vigente;
2. cumple una funcion procedural necesaria para decision, permiso, ejecucion o bloqueo;
3. puede expresarse sin depender del dominio automata.

Si un elemento falla alguna condicion, queda como campo local de `AUD-001` o deuda conceptual, no como parte de la capa abstracta.

## Resultado

`REPORT_LAYER` se saca principalmente de `AUD-001_Contrato_Reportes.md`, pero solo despues de filtrar esos contratos por:

- las reglas de autoridad de `M-000`;
- el procedimiento de auditoria de `M-001`;
- el alcance oficial de `C-001`;
- las validaciones no automata `VAL-017` a `VAL-021`;
- la frontera de permiso de `DO-001`.

Esa combinacion produce una capa abstracta interna, auditable y todavia provisional.

## Siguiente paso

Usar este mapa para construir una validacion de `REPORT-LAYER-CAND-001` contra una instancia no automata que no dependa de los nombres locales `MP_FAIL_REPORT`, `CR_FAIL_REPORT`, `TAU_REPORT`, `D_REPORT`, `TR_*` o `REVERSAL_REPORT`.
