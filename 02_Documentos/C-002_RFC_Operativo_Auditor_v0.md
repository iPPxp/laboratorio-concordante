# C-002 - RFC Operativo del Auditor v0

Estatus: documento oficial de Nivel C.

Formato: tipo RFC local.

Fecha: 2026-07-02.

Actualizacion: 2026-07-03.

Identificador: `C-002`.

Fuente de promocion: `03_Expedientes/AUD-001_Decision_Promocion_SPEC-RFC-AUDITOR-V0.md`.

Fuente candidata: `03_Expedientes/AUD-001_SPEC-RFC-AUDITOR-V0_Candidata.md`.

## 1. Estado del memo

Este documento especifica el uso operativo del Auditor del Laboratorio Concordante en version v0.

`C-002` complementa `C-001_Especificacion_Tecnica_Auditor.md`.

No reemplaza Canon, no modifica `M-000`, no modifica `M-001` y no cierra problemas formales fuera de su alcance.

## 2. Resumen

El Auditor es un procedimiento de lectura, calculo, reporte y decision restringida.

Su funcion es revisar trazabilidad, estatus, dependencias, permisos, reportes y cambios acotados sin convertirse en autoridad autonoma.

Por defecto, el Auditor es no mutante: puede leer, reportar, bloquear, escalar o proponer; solo puede ejecutar cambios reales si existe autorizacion previa, alcance acotado y verificacion posterior.

## 3. Lenguaje normativo local

Las palabras `DEBE`, `NO DEBE`, `PUEDE` y `REQUIERE` tienen fuerza normativa dentro de este documento.

- `DEBE`: requisito obligatorio para conformidad.
- `NO DEBE`: prohibicion obligatoria.
- `PUEDE`: comportamiento permitido, no obligatorio.
- `REQUIERE`: condicion previa sin la cual una accion no es valida.

Estas palabras no importan normas externas; su significado es local a este documento.

## 4. Fuentes normativas

- `01_Canon/M-000_Reglas_Fundamentales.md`
- `01_Canon/M-001_Auditoria_Arquitectonica.md`
- `05_Estado_Proyecto/NIVEL_C_ESPECIFICACIONES.md`
- `02_Documentos/C-001_Especificacion_Tecnica_Auditor.md`
- `03_Expedientes/AUD-001_Contrato_Reportes.md`
- `03_Expedientes/AUD-001_Decision_Estatus_Auditor_v0.md`
- `03_Expedientes/DO-001_Decision_Modo_Operativo_Auditor.md`
- `03_Expedientes/DO-001_Regla_Permiso_Actualizacion.md`

## 5. Terminos

`Artefacto`: archivo, fragmento, expediente, reporte, afirmacion o conjunto acotado de fuentes locales revisado por el Auditor.

`Reporte`: salida estructurada que conserva evidencia, estatus, decision permitida y permiso de transformacion.

`Decision`: seleccion explicita de aprobar, bloquear, escalar, continuar sin transformar o continuar con cambio acotado.

`Recomendacion`: sugerencia emitida por una lectura o herramienta. Una recomendacion NO DEBE tratarse como decision.

`Transformacion`: cambio material o documental sobre un artefacto.

`REPORT_LAYER`: capa abstracta local de expediente para leer reportes de forma uniforme. En `C-002` no queda promovida a Nivel C como contrato independiente.

## 6. Modelo operacional

El Auditor DEBE distinguir cinco operadores:

```text
Mp -> Cr -> tau -> D -> Tr
```

- `Mp` mapea el artefacto a una estructura legible.
- `Cr` calcula o verifica sobre la estructura mapeada.
- `tau` cierra, bloquea o escala la terminacion del procedimiento.
- `D` emite decision restringida por reportes previos.
- `Tr` propone o ejecuta transformaciones.

`Tr_ejecucion` REQUIERE una decision previa fundada y permiso explicito.

`D = aprobar` NO DEBE interpretarse como permiso de transformacion.

## 7. Entradas

El Auditor PUEDE recibir:

- archivos locales;
- expedientes abiertos;
- documentos oficiales;
- reportes normalizados;
- propuestas de cambio con alcance declarado;
- instrucciones humanas dentro de alcance permitido.

El Auditor NO DEBE usar como autoridad directa:

- conversaciones historicas sin decision registrada;
- referencias mencionadas pero no materializadas;
- hipotesis sin estatus;
- deudas conceptuales como fundamento positivo;
- recomendaciones de herramienta como decisiones.

## 8. Reportes

El Auditor DEBE emitir reportes compatibles con `AUD-001_Contrato_Reportes.md` o con la lectura conceptual permitida por `REPORT_LAYER`.

Los reportes DEBEN conservar:

- identificador;
- artefacto revisado;
- operador o fase;
- resultado;
- tipo de hallazgo;
- ubicacion;
- evidencia;
- estatus de afirmacion;
- decisiones permitidas;
- decision emitida, si aplica;
- permiso de transformacion;
- dependencias;
- deudas generadas.

Un reporte bloqueante NO DEBE habilitar transformacion.

## 9. Procedimiento obligatorio

Una ejecucion conforme DEBE seguir esta secuencia minima:

```text
1. Leer fuentes autorizadas.
2. Mapear el artefacto.
3. Verificar estatus, dependencias, permisos y riesgos de nivel.
4. Cerrar terminacion.
5. Emitir reporte.
6. Emitir decision solo si corresponde.
7. Conservar propuesta como propuesta si no hay permiso.
8. Ejecutar cambio solo con decision y autorizacion validas.
9. Registrar evidencia antes/despues si hubo ejecucion.
10. Verificar estado posterior.
```

Si cualquier paso previo falla, el Auditor DEBE bloquear, escalar o continuar sin transformar segun el reporte.

## 10. Permisos y transformaciones

Toda transformacion ejecutada REQUIERE:

- `Mp` valido o reporte que permita continuidad;
- `Cr` terminado sin hallazgo bloqueante;
- `tau = exito`;
- `D_REPORT` con `decision_emitida = continuar_con_cambio_acotado`;
- `transformacion_permitida = true`;
- alcance acotado;
- evidencia previa;
- evidencia posterior;
- verificacion posterior.

El Auditor NO DEBE:

- modificar Canon por inferencia;
- modificar documentos oficiales sin decision registrada;
- cerrar expedientes sin decision explicita;
- reparar una deuda conceptual por intuicion;
- usar historial como estado previo local;
- reintentar una ejecucion fallida sin nueva autorizacion.

## 11. Fallos y reversion

Si una ejecucion falla, el Auditor DEBE emitir un reporte de fallo y prohibir nuevas transformaciones hasta nueva decision.

La reversion material queda fuera de `C-002`.

`REVERSAL_REPORT` PUEDE clasificar acciones permitidas, pero NO DEBE ejecutar restauracion por si mismo.

La cuarentena en `C-002` es documental salvo decision operativa posterior.

## 12. DO_CHECK_REPORT

`DO_CHECK_REPORT` PUEDE leerse como evidencia documental no mutante.

`DO_CHECK_REPORT.recomendacion` NO DEBE convertirse en `decision_emitida`.

`DO_CHECK_REPORT.cambios_propuestos` NO DEBE convertirse en `Tr_ejecucion`.

La compatibilidad con `REPORT_LAYER` es conceptual y no absorbe `DO_CHECK_REPORT` en `AUD-001_Contrato_Reportes.md`.

La implementacion de referencia PUEDE usar un adaptador no mutante para traducir `DO_CHECK_REPORT` a `REPORT_ITEM` operativo.

Ese adaptador NO DEBE emitir `OPERATOR_REPORT`, NO DEBE decidir autoridad, NO DEBE permitir transformacion y NO DEBE convertir recomendaciones en decisiones.

## 13. Conformidad

Una revision documental es conforme si:

- cita fuentes locales;
- clasifica afirmaciones;
- conserva evidencia;
- emite reporte;
- no transforma artefactos;
- registra deudas;
- respeta separacion de niveles.

Una herramienta no mutante es conforme si:

- implementa lectura acotada;
- produce reportes;
- no escribe cambios;
- no decide autoridad;
- no promueve estatus.

La implementacion local de referencia `06_Automatizacion/auditor_v0.py` opera en modo no mutante.

Con JSON reactivado, esa implementacion PUEDE usar la matriz interna `AUD-T00` a `AUD-T09` o cargar casos externos por `--case-file`, siempre dentro del repositorio.

La salida JSON PUEDE emitirse por `--format json`, pero no autoriza transformaciones, no sustituye decisiones registradas y DEBE conservar `transformacion_permitida = false` salvo decision futura de herramienta mutante.

Los archivos externos de casos PUEDEN declararse contra el esquema operativo `AUDITOR-V0-CASE-SCHEMA-001`.

El esquema DEBE distinguir variantes por `kind` y la implementacion DEBE registrar errores de forma en `schema_errors`.

Un fixture parcial PUEDE ejecutarse para validar clases de entradas, pero NO DEBE declarar `conforme_c002 = true` si omite los casos obligatorios `AUD-T00` a `AUD-T09`.

Una herramienta de referencia conforme DEBE cumplir simultaneamente:

- todos los casos obligatorios presentes;
- cero `schema_errors`;
- `transformacion_permitida = false` en reporte global, casos y reportes internos;
- ninguna recomendacion tratada como decision de autoridad.

Una herramienta mutante futura solo sera conforme si ademas implementa `PERMISO-ACT-001`, evidencia antes/despues, verificacion posterior y manejo de fallo.

## 14. Matriz minima de pruebas

La conformidad v0 DEBE cubrir al menos:

- `AUD-T00`: control positivo sin hallazgos bloqueantes;
- `AUD-T01`: transicion faltante;
- `AUD-T02`: estado final inalcanzable;
- `AUD-T03`: contradiccion de determinismo;
- `AUD-T04`: equivalencia sin algoritmo;
- `AUD-T05`: transformacion sin decision;
- `AUD-T06`: `Gamma` no materializada;
- `AUD-T07`: Registro Historico como autoridad directa;
- `AUD-T08`: modificacion de Canon desde expediente;
- `AUD-T09`: termino nuevo sin estatus.

La cobertura vigente esta registrada en `AUD-001_Validaciones.md` hasta `VAL-029`.

La matriz externa completa vigente esta en `06_Automatizacion/fixtures/auditor_v0_cases.json`.

El fixture documental parcial vigente esta en `06_Automatizacion/fixtures/auditor_v0_documental_cases.json`.

El esquema operativo vigente esta en `06_Automatizacion/fixtures/auditor_v0_case_schema.json`.

## 15. Seguridad operacional

El riesgo principal del Auditor es crear autoridad aparente.

Por eso, toda salida DEBE separar:

- evidencia;
- recomendacion;
- decision;
- permiso;
- ejecucion.

El Auditor NO DEBE usar una salida correcta como autorizacion de cambio.

## 16. Limites abiertos

Quedan fuera de `C-002`:

- Regla R4 formal;
- `Gamma` formal;
- suite ejecutable completa;
- parser real;
- reversion material;
- cuarentena materializada;
- promocion de `REPORT_LAYER` a Nivel C;
- cierre de `H-B.6` y `H-B.7`.

## 17. Criterio de uso

`C-002` puede usarse como referencia oficial para revisar si una lectura, herramienta o propuesta de implementacion se comporta como Auditor v0.

No autoriza por si mismo ninguna transformacion real.
