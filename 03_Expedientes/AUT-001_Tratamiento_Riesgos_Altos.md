# AUT-001 - Tratamiento Inicial de Riesgos Activos Altos

Estatus: tratamiento provisional no mutante aceptable para decision posterior.

Fecha: 2026-07-02.

## Objeto

Registrar tratamiento inicial de los riesgos activos altos detectados por `DO-LAB-RISK-001`, sin modificar Canon, documentos oficiales, expedientes cerrados ni reportes fuente.

## Regla de tratamiento

- Un riesgo alto no se borra por ser falso positivo.
- Un riesgo alto puede quedar como `controlado` si la evidencia muestra una regla de proteccion, una prohibicion o una compuerta.
- Un riesgo alto requiere decision posterior si propone o ejecuta transformacion real.
- Todo tratamiento conserva `transformacion_permitida: false`.

## Riesgos altos actuales

### AUT-RISK-HIGH-001

- archivo: `01_Canon/M-001_Auditoria_Arquitectonica.md`
- check: `MED-NIVELES`
- tipo: `accion_de_nivel_sensible`
- severidad operativa: `alta`
- estatus de tratamiento: `controlado_provisionalmente`
- detalle: La linea parece tocar Canon, documento oficial, expediente cerrado o hipotesis.
- evidencia: 8. Indicar si la intervencion modifica documentos, expedientes, estado o Canon.
- tratamiento: Mantener como alerta de superficie de autoridad. La evidencia es una regla de auditoria que exige indicar si se modifica Canon; no ejecuta modificacion.
- accion permitida ahora: lectura y conservacion del riesgo; ninguna transformacion.

### AUT-RISK-HIGH-002

- archivo: `05_Estado_Proyecto/DECISION_Siguiente_Frente_Activo_B-001.5.md`
- check: `MED-CERRADOS`
- tipo: `expediente_cerrado_afectado`
- severidad operativa: `alta`
- estatus de tratamiento: `controlado_provisionalmente`
- detalle: La linea parece afectar expediente cerrado: B-001, CP-001, EF-001
- evidencia: - reabrir `B-001`, `CP-001`, `EF-001`, Procedimiento o Auditoria
- tratamiento: Mantener como alerta de expediente cerrado. La evidencia prohibe o condiciona reaperturas; no ejecuta reapertura.
- accion permitida ahora: lectura y conservacion del riesgo; ninguna transformacion.

## Resultado provisional

Los riesgos altos quedan controlados provisionalmente como alertas utiles de gobierno. No bloquean el cierre tecnico provisional de `AUT-001`, pero si bloquean cualquier cierre operativo completo o transformacion real sin decision posterior.

## Siguiente accion

Decidir si `AUT-001` pasa a cierre tecnico provisional o si se abre una ronda de refinamiento sobre los riesgos activos medios y documentales.
