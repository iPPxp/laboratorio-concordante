# MOC-001 - Relacion documental controlada con C-001 y C-002

ID: `MOC-C001-C002-REL-001`.

Ruta: `MOC-ROUTE-012`.

Fecha: 2026-07-06.

Estatus: puente documental provisional de expediente.

Decision asociada: `D-2026-07-06-013`.

## Proposito

Relacionar `MOC-001` con los documentos oficiales de Nivel C `C-001` y `C-002` sin modificar esos documentos, sin promover el MOC a Nivel C y sin convertir `Xi_eval`, estados MOC o `MOC-EVAL-001` en autoridad operativa general.

Este puente solo fija una lectura de conformidad local para tratar productos del MOC como artefactos auditables por el Auditor.

## Fuentes

- `02_Documentos/C-001_Especificacion_Tecnica_Auditor.md`.
- `02_Documentos/C-002_RFC_Operativo_Auditor_v0.md`.
- `03_Expedientes/MOC-001.md`.
- `03_Expedientes/MOC-001_Formalizacion_Xi_eval.md`.
- `03_Expedientes/MOC-001_Puente_Formal_MOC_AO.md`.
- `03_Expedientes/MOC-001_Protocolo_Evaluacion_v0_2.md`.
- `03_Expedientes/MOC-001_Rutas_Posteriores_Ruta_010.md`.

## Lectura desde C-001

`C-001` permite leer el MOC como artefacto tecnico de expediente bajo las reglas iniciales del Auditor:

- fuente local con estatus declarado;
- conjunto acotado de archivos locales;
- expediente abierto no canonico;
- propuesta teorico-operativa con alcance declarado;
- salida de herramienta no mutante si conserva evidencia, resultado y deuda.

Desde `C-001`, el MOC no puede operar como:

- autoridad autonoma;
- fuente de permiso;
- cierre automatico de expediente;
- modificador de Canon, documentos oficiales o Nivel C;
- sustituto del Auditor;
- evidencia empirica real.

## Lectura desde C-002

`C-002` permite leer una ejecucion documental del MOC bajo el procedimiento operativo del Auditor:

```text
leer -> mapear -> verificar -> cerrar terminacion -> reportar -> decidir solo si corresponde -> conservar propuesta -> no transformar
```

En esta relacion, `MOC-EVAL-001` puede aportar reportes no mutantes si cumple:

- fuentes locales declaradas;
- casos sinteticos no clinicos;
- salida con resultado y deuda;
- `operator_trace` como evidencia local de regla ganadora;
- `transformacion_permitida = false`;
- ninguna decision de autoridad;
- ningun dato personal;
- ningun uso clinico, patologico o regulado.

## Mapa formal local

| Elemento MOC | Rol bajo C-001 | Rol bajo C-002 | Limite |
| --- | --- | --- | --- |
| `Xi_eval` | operador local de evaluacion | calculo/reporte no mutante | no canoniza `Xi`, no admite `H-Xi` |
| estado MOC | resultado ordinal local | campo de resultado auditable | no equivale a conformidad C |
| `operator_trace` | evidencia de regla ganadora | evidencia de reporte | no es decision ni permiso |
| `Pi_moc_trace` | proyeccion local | evidencia estructurada | no cierra equivalencia global |
| `ao_bridge` | puente de expediente | relacion con reporte/artefacto | no modifica Documento 04 |
| protocolo v0.2 | procedimiento local reproducible | secuencia revisable | no valida evaluadores reales |
| plantilla de respuesta | artefacto documental | entrada futura solo si se autoriza | no habilita reclutamiento |
| paquete de piloto | propuesta bloqueada | material preparatorio | no autoriza ejecucion |
| `MOC-EVAL-001` | herramienta no mutante local | generador de reporte | no sustituye Auditor v0 |

## Reporte puente local

Si una ruta futura necesita revisar el MOC contra `C-001` / `C-002`, el reporte local minimo debe conservar:

```text
report_id
artefacto_moc
fuentes_moc
fuentes_c
alcance
resultado_moc
operator_trace
estatus_afirmacion
dependencias
deudas_generadas
decision_permitida
transformacion_permitida = false
```

Este reporte puente no es `OPERATOR_REPORT` oficial, no es `REPORT_LAYER` promovido y no crea contrato de Nivel C.

## Criterio de compatibilidad

Un artefacto MOC es compatible documentalmente con `C-001` / `C-002` si:

1. declara alcance y estatus;
2. usa solo fuentes locales autorizadas;
3. conserva evidencia y traza;
4. separa resultado, recomendacion, decision y permiso;
5. registra deudas;
6. mantiene `transformacion_permitida = false`;
7. no usa personas reales, datos personales ni dominios clinicos o regulados;
8. no modifica Canon, documentos oficiales, Nivel C ni expedientes cerrados.

## Incompatibilidad

Un uso del MOC no es compatible con `C-001` / `C-002` si:

- presenta el MOC como validado empiricamente;
- ejecuta piloto real sin compuerta nueva;
- usa `Xi_eval` como operador general vigente;
- trata `operator_trace` como decision;
- usa resultados MOC para cerrar Confluencia global o Equivalencia global;
- promueve `REPORT_LAYER`, R4 o Gamma;
- modifica `C-001` o `C-002` por inferencia;
- evalua personas reales o recolecta datos personales.

## Resultado

`MOC-ROUTE-012` queda formulada como relacion documental controlada con `C-001` y `C-002`.

La deuda previa de relacion entre `MOC-001` y Nivel C queda atendida solo en grado documental local.

No se modifica `C-001`, no se modifica `C-002`, no se crea `C-003`, no se modifica Canon, no se autoriza ejecucion real y no se promueve el MOC.

## Deudas abiertas

- Eventual especificacion tecnica futura si el MOC necesitara herramienta auditora propia.
- Eventual compuerta nueva si se propone ejecucion empirica real.
- Confluencia global.
- Equivalencia global de proyecciones.
- Maduracion posterior de `TCS-001`.
- Exportacion general de R4/Gamma.
