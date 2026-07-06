# MOC-001 - Plantilla de respuesta de evaluadores

ID: `MOC-PILOT-RESPONSE-TPL-001`.

Ruta: `MOC-ROUTE-008`.

Fecha: 2026-07-06.

Estatus: plantilla documental, no usada en ejecucion real.

Decision asociada: `D-2026-07-06-004`.

## Proposito

Definir la plantilla que podria recibir un evaluador en un piloto futuro autorizado.

Esta plantilla no recluta evaluadores, no recoge respuestas reales y no abre ejecucion del piloto.

## Identificacion minima

```text
response_id:
case_id:
evaluador_codigo:
fecha_respuesta:
version_casos: MOC-PILOT-CASE-FREEZE-001
version_reglas: MOC-PILOT-RULE-FREEZE-001
```

`evaluador_codigo` debe ser un codigo no personal si alguna decision futura autorizara participacion humana. No debe registrar nombre, correo, institucion, telefono, ubicacion, identificador laboral ni otro dato personal.

## Entrada recibida por evaluador

```text
R0:
R1:
Dist(R0,R1):
Res(R0 -> R1):
alcance:
evidencia:
restricciones:
ejes_TCS:
operator_trace_disponible: si/no
ao_bridge_disponible: si/no
```

## Respuesta requerida

```text
salida_Xi:
estado_MOC:
familia_estado:
regla_ganadora:
justificacion_breve:
deuda:
uso_positivo_permitido: si/no
review_required: si/no
```

## Opciones cerradas

### salida_Xi

- `redundante`
- `util_acotado`
- `limitado`
- `no_comparable`
- `bloqueado`

### estado_MOC

- `concordancia_local`
- `concordancia_parcial`
- `friccion_operativa`
- `discordancia_global`
- `bloqueo_de_concordancia`
- `no_comparable`

### familia_estado

- `concordante`
- `friccion`
- `seguridad`

### uso_positivo_permitido

- `si`, solo para `concordancia_local` o `concordancia_parcial` y siempre como evidencia local no canonica;
- `no`, para seguridad, bloqueo, no comparabilidad o cualquier uso fuera de alcance.

## Justificacion breve

La justificacion debe tener una forma auditable:

```text
Elijo <salida_Xi>/<estado_MOC> porque <regla o evidencia>, con deuda <deuda>.
```

No se permiten inferencias sobre personas, rasgos, salud mental, diagnostico, capacidad, intencion ni patologia.

## Campo de desacuerdo

Si el evaluador detecta desacuerdo con la traza propuesta o ambiguedad de regla:

```text
eje_desacuerdo:
opcion_preferida:
motivo:
deuda_para_micro_revision:
```

Ejes permitidos:

- `sin_desacuerdo`
- `regla_xi`
- `estado_moc`
- `familia_moc`
- `regla_tcs`
- `rol_ao`
- `alcance`
- `evidencia`

## Prohibiciones de registro

La plantilla no debe recoger:

- nombres;
- correos;
- datos personales;
- datos de personas evaluadas;
- experiencia clinica;
- diagnosticos;
- datos laborales o institucionales reales;
- respuestas sobre casos reales.

## Resultado

`MOC-PILOT-RESPONSE-TPL-001` queda lista como plantilla documental para una fase futura. No habilita ejecucion real.
