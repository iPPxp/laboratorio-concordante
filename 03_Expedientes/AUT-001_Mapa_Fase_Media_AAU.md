# AUT-001 - Mapa fase media AAU

Estatus: mapa tecnico provisional de expediente.

Fecha: 2026-07-01.

## Proposito

Definir la fase media de `AUT-001` como puente entre `DO-CHECK-MIN-001`, `C-001` y el AAU historico localizado en `SRC-013`.

Este mapa no importa el codigo historico ni canoniza sus definiciones. Solo extrae una equivalencia funcional suficiente para una herramienta no mutante de lectura y reporte.

## Fuentes

- `03_Expedientes/AUT-001.md`
- `06_Automatizacion/do_check_min.py`
- `02_Documentos/C-001_Especificacion_Tecnica_Auditor.md`
- `03_Expedientes/DO-001_DO-CHECK-001.md`
- `03_Expedientes/DO-001_Regla_Permiso_Actualizacion.md`
- `03_Expedientes/REC-001_Mapa_Reconciliacion_Canon_Baselines.md`
- `04_Registro_Historico/2026-07-01_descargas_usuario_001/extracciones/SRC-013_laboratorio-concordante-v1.0.0-fase2-nucleo-ejecutable.zip_extraccion.md`

## Equivalencia funcional

| AAU historico | Fase media vigente | Uso permitido |
| --- | --- | --- |
| `Presv` | controles preservables `MED-*` | lista de checks no mutantes |
| `Activas(G)` | estado operativo, permisos, expedientes cerrados y superficies sensibles | contexto local vigente |
| `Inv(G)` | controles que pasan sin hallazgo | evidencia de estabilidad parcial |
| `Break(Fk)` | hallazgos emitidos por el reporte | zona de riesgo documental |
| `APROBADO` | `resultado = ok` | lectura aprobada sin transformar |
| `SUSPENDIDO` | `resultado = advertencia` | continuar sin transformar |
| `INCONSISTENTE` | `resultado = bloqueado` | bloquear |
| `NO AUDITABLE` | fuente minima ausente o entrada insuficiente | escalar o bloquear |

## Controles medios

`DO-CHECK-MED-001` debe revisar:

- `MED-FUENTES`: fuentes minimas disponibles.
- `MED-ESTATUS`: estatus visible en superficies que lo requieren.
- `MED-REFERENCIAS`: referencias locales materializadas.
- `MED-HISTORIAL`: Registro Historico o `SRC-*` usado como autoridad vigente.
- `MED-NIVELES`: acciones sensibles sobre Canon, documentos oficiales, expedientes cerrados o hipotesis.
- `MED-CERRADOS`: intento de afectar expedientes cerrados.
- `MED-REPORTES`: definiciones de reportes normalizados con campos minimos.
- `MED-ESTADO`: consistencia minima del estado operativo.
- `MED-ASCII`: politica ASCII fuera de zonas historicas permitidas.

## Alcance

La fase media puede:

- leer archivos Markdown locales;
- emitir reportes Markdown o JSON;
- distinguir advertencia, bloqueo y aprobacion de lectura;
- mapear hallazgos a una lectura funcional del AAU historico;
- revisar superficies sensibles sin modificarlas;
- dejar evidencia conservada en `06_Automatizacion/reportes`.

## Fuera de alcance

La fase media no puede:

- modificar Canon;
- modificar documentos oficiales;
- cerrar o reabrir expedientes;
- ejecutar transformaciones;
- importar el AAU historico como implementacion vigente;
- definir formalmente `R4` o `Gamma`;
- abrir psicologia automaticamente.

## Dictamen

`REC-DEUDA-003` queda atendida en grado operativo inicial: el AAU historico fue comparado con `C-001`, `DO-CHECK-001` y `DO-CHECK-MIN-001`, y se deriva una fase media no mutante.

La deuda no queda cerrada en sentido matematico: `Presv`, `Inv(G)`, `Activas(G)`, `Break(Fk)`, `R4` y `Gamma` siguen pendientes de formalizacion si se abre el frente matematico.
