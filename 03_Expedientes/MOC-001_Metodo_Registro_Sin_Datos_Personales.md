# MOC-001 - Metodo de registro sin datos personales

ID: `MOC-PILOT-NODATA-REG-001`.

Ruta: `MOC-ROUTE-009`.

Fecha: 2026-07-06.

Estatus: metodo documental preparado, no usado en ejecucion real.

Decision asociada: `D-2026-07-06-005`.

## Proposito

Definir el metodo minimo para registrar respuestas de un piloto futuro del MOC sin recopilar datos personales.

Este metodo no ejecuta piloto, no recluta evaluadores, no recoge respuestas reales y no autoriza participacion humana. Solo fija reglas de registro para que una decision futura pueda auditar si el canal propuesto respeta la compuerta vigente.

## Principio de minimizacion

El registro permitido se limita a informacion necesaria para auditar una respuesta sobre casos sinteticos no clinicos:

- identificador de respuesta;
- identificador de caso sintetico;
- codigo no personal de evaluador;
- version de casos;
- version de reglas/protocolo;
- salida `Xi_eval`;
- estado MOC;
- regla ganadora;
- deuda;
- justificacion breve;
- banderas de revision.

No se registra identidad, contacto, ubicacion, institucion, experiencia profesional, historial, diagnostico, dato clinico ni metadato tecnico personal.

## Identificadores permitidos

### `response_id`

Forma permitida:

```text
MOC-RSP-<lote>-<numero>
```

Ejemplo documental:

```text
MOC-RSP-SYN-001-0001
```

`response_id` solo identifica una respuesta dentro del lote. No debe derivarse de nombre, correo, iniciales, usuario, telefono, direccion IP, dispositivo, ubicacion ni marca temporal precisa.

### `evaluador_codigo`

Forma permitida:

```text
EVAL-SYN-A
EVAL-SYN-B
EVAL-SYN-C
```

En una ejecucion futura autorizada con humanos, el codigo deberia asignarse fuera del repositorio y entrar al Laboratorio solo como etiqueta no reversible. Mientras no exista autorizacion, los codigos son puramente documentales o simulados.

## Campos permitidos de registro

```text
registro_id:
response_id:
case_id:
evaluador_codigo:
lote:
fecha_lote:
version_casos:
version_reglas:
version_plantilla:
salida_Xi:
estado_MOC:
familia_estado:
regla_ganadora:
operator_trace_id:
ao_bridge_role:
justificacion_breve:
deuda:
uso_positivo_permitido:
review_required:
motivo_revision:
```

`fecha_lote` debe ser granular a dia o version de lote. No se debe registrar hora exacta de respuesta si pudiera funcionar como identificador indirecto.

## Campos prohibidos

Quedan prohibidos:

- nombre;
- correo;
- telefono;
- institucion;
- cargo;
- ubicacion;
- direccion IP;
- identificador de dispositivo;
- cuenta de plataforma;
- firma;
- edad;
- genero;
- historial personal;
- experiencia clinica;
- diagnostico;
- caso real;
- respuesta libre con datos identificables;
- metadatos de navegador o sistema.

## Regla de aceptacion de una respuesta

Una respuesta solo seria registrable si cumple todas las condiciones:

```text
caso_sintetico = true
datos_personales_detectados = false
dominio_clinico = false
dominio_regulado = false
version_casos = MOC-PILOT-CASE-FREEZE-001
version_reglas = MOC-PILOT-RULE-FREEZE-001
plantilla = MOC-PILOT-RESPONSE-TPL-001
campos_cerrados_validos = true
```

Si una condicion falla, la respuesta no entra al registro ordinario.

## Rechazo y contencion

Si aparece dato personal o indicio de caso real:

1. no incorporar el contenido al repositorio;
2. registrar solo un evento abstracto de rechazo;
3. marcar `registro_aceptado = false`;
4. marcar `motivo = dato_personal_o_caso_real`;
5. bloquear cualquier reporte agregado que dependa de esa respuesta;
6. conservar la deuda como bloqueo de ejecucion futura.

El evento abstracto no debe copiar el dato personal.

## Registro agregado permitido

El registro agregado permitido puede contener:

- conteo de respuestas aceptadas;
- conteo de respuestas rechazadas por motivo abstracto;
- distribucion de salidas `Xi_eval`;
- distribucion de estados MOC;
- coincidencia exacta;
- coincidencia parcial;
- desacuerdo justificado;
- deuda conservada;
- bloqueos conservados;
- casos con `review_required`.

El registro agregado no debe permitir reidentificar evaluadores ni reconstruir secuencias individuales si hubiera humanos en una fase futura.

## Ubicacion documental futura

Mientras no exista autorizacion de ejecucion, no se crea archivo de respuestas reales.

Si una decision futura autorizara solo simulacion documental, los registros sinteticos podrian vivir como fixture o reporte no mutante en `06_Automatizacion/reportes`.

Si una decision futura autorizara humanos sin datos personales, tendria que declarar antes:

- canal de registro;
- confirmacion de no recoleccion de datos personales;
- responsable de auditoria;
- criterio de rechazo;
- formato agregado de reporte;
- tratamiento de cualquier incidente de datos.

## Invariantes

- El metodo no autoriza ejecucion real.
- El metodo no recluta evaluadores.
- El metodo no recopila respuestas reales.
- El metodo no recopila datos personales.
- El metodo no evalua personas reales.
- El metodo no abre uso clinico.
- El metodo no modifica Canon, Nivel C ni `Documento 04`.
- El metodo no cierra Confluencia global ni Equivalencia global.
- El metodo no convierte resultados futuros en validacion empirica general.

## Resultado

`MOC-PILOT-NODATA-REG-001` queda como metodo documental de registro sin datos personales para una fase futura aun bloqueada.

