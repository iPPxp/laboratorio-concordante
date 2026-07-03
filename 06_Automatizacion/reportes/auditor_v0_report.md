# AUDITOR_V0_REPORT

report_id: AUDITOR-V0-20260702-185608
expediente: AUD-001
algoritmo: AUDITOR-V0-001
base_normativa: C-002
modo: no_mutante
conforme_c002: true
transformacion_permitida: false

## Resumen

- casos revisados: 10
- casos obligatorios faltantes: 0
- ok: 1
- advertencia: 2
- bloqueado: 7
- reportes de operador: 11
- errores de esquema: 0

## Casos

### AUD-T00 - ok

- D / ok / sin_hallazgo_bloqueante: La lectura no detecta hallazgos bloqueantes. Decision: aprobar. Transformacion: false.

### AUD-T01 - bloqueado

- Mp / falla / ambiguedad: El automata declara completitud, pero faltan transiciones. Decision: bloquear. Transformacion: false.

### AUD-T02 - advertencia

- Cr / escalado / deuda_conceptual: Existe estado final inalcanzable desde el estado inicial. Decision: escalar. Transformacion: false.

### AUD-T03 - bloqueado

- Cr / falla / contradiccion: La declaracion de determinismo contradice transiciones duplicadas. Decision: bloquear. Transformacion: false.

### AUD-T04 - bloqueado

- D / bloqueado / dependencia_no_registrada: La afirmacion requiere una dependencia local no materializada. Decision: bloquear. Transformacion: false.

### AUD-T05 - bloqueado

- Mp / falla / dependencia_no_registrada: El mapeo referencia estados o simbolos no declarados. Decision: bloquear. Transformacion: false.
- Tr / bloqueado / violacion_r4_aud: Se detecta transformacion ejecutada sin decision fundada. Decision: bloquear. Transformacion: false.

### AUD-T06 - bloqueado

- D / bloqueado / deuda_conceptual: La afirmacion promueve una construccion formal sin definicion local. Decision: bloquear. Transformacion: false.

### AUD-T07 - bloqueado

- D / bloqueado / dependencia_no_registrada: El Registro Historico aparece como autoridad directa sin decision registrada. Decision: bloquear. Transformacion: false.

### AUD-T08 - bloqueado

- D / bloqueado / violacion_r4_aud: Un expediente intenta modificar Canon sin decision explicita. Decision: bloquear. Transformacion: false.

### AUD-T09 - advertencia

- Mp / escalado / deuda_conceptual: El texto introduce un termino nuevo sin estatus declarado. Decision: continuar_sin_transformar. Transformacion: false.

## Fuentes

- 02_Documentos/C-002_RFC_Operativo_Auditor_v0.md
- 02_Documentos/C-001_Especificacion_Tecnica_Auditor.md
- 03_Expedientes/AUD-001_Casos_Prueba_Auditor.md
- 03_Expedientes/AUD-001_Contrato_Reportes.md
- 03_Expedientes/DO-001_Regla_Permiso_Actualizacion.md
