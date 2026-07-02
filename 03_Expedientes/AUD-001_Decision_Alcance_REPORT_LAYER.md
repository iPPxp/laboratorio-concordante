# AUD-001 - Decision de alcance de REPORT_LAYER

Estatus: decision provisional de expediente.

ID: `ALC-REPORT-LAYER-001`.

Expediente padre: `AUD-001`.

Objeto decidido: alcance actual de `REPORT-LAYER-CAND-001`.

Fuentes principales:

- `03_Expedientes/AUD-001_REPORT_LAYER_Candidata.md`
- `03_Expedientes/AUD-001_Origen_REPORT_LAYER.md`
- `03_Expedientes/AUD-001_Simulaciones.md` (`AUD-SIM-022`)
- `03_Expedientes/AUD-001_Validaciones.md` (`VAL-022`)

## Decision

`REPORT_LAYER` queda, por ahora, como capa abstracta local de `AUD-001`.

Estatus asignado:

```text
REPORT_LAYER = candidata provisional local de AUD-001
```

No se abre todavia ruta de Nivel C, expediente propio ni especificacion oficial.

## Motivo

`VAL-022` valida provisionalmente que `REPORT_LAYER` puede extraerse de fuentes internas del Laboratorio sin depender de los nombres locales de reportes.

Eso basta para usarlo dentro de `AUD-001`, pero no basta para promoverlo fuera del expediente.

Todavia faltan:

- probar compatibilidad con reportes producidos por herramientas ejecutables futuras;
- decidir serializacion;
- decidir relacion estable con `DO_CHECK_REPORT`;
- auditar contra `NIVEL-C-001` si se quiere documento oficial;
- justificar que su uso rebasa `AUD-001`.

## Alcance permitido

Dentro de `AUD-001`, `REPORT_LAYER` puede usarse para:

- hablar de reportes equivalentes sin exigir nombres locales como `MP_FAIL_REPORT` o `D_REPORT`;
- sostener lecturas de `R4-CANDIDATA`;
- comparar objetos no automatas contra una cadena de reporte, decision, permiso y ejecucion;
- registrar validaciones teoricas adicionales;
- preparar una futura candidata de Nivel C si se decide despues.

## Alcance no permitido

`REPORT_LAYER` no puede usarse todavia para:

- modificar `C-001`;
- obligar a otros expedientes a usar su formato;
- reemplazar `OPERATOR_REPORT`;
- absorber `DO_CHECK_REPORT`;
- definir una serializacion ejecutable;
- promover `R4-CANDIDATA`;
- resolver R4 formal o `Gamma`.

## Fronteras internas

| Elemento | Estado frente a `REPORT_LAYER` |
| --- | --- |
| `OPERATOR_REPORT` | gramatica concreta local de `AUD-001`; fuente de abstraccion |
| Reportes especializados de `AUD-001` | instancias concretas, no nombres obligatorios fuera de `AUD-001` |
| `DO_CHECK_REPORT` | reporte propio de `DO-001`; compatible solo por puente futuro, no absorbido |
| `C-001` | documento oficial que permite reportes normalizados; no queda modificado |
| `R4-CANDIDATA` | puede usar `REPORT_LAYER` como capa abstracta interna |
| Nivel C | ruta bloqueada hasta nueva decision, auditoria y alcance exportable |

## Rutas futuras posibles

### Ruta A - Permanecer local

`REPORT_LAYER` queda como vocabulario abstracto de `AUD-001`.

Estado: ruta vigente.

### Ruta B - Preparar Nivel C

Requiere:

- candidata separada de especificacion;
- alcance exportable;
- auditoria contra `M-000`, `M-001` y `NIVEL-C-001`;
- decision de promocion.

Estado: diferida.

### Ruta C - Abrir expediente propio

Requiere que `REPORT_LAYER` empiece a gobernar mas de un frente o genere deudas propias no contenibles en `AUD-001`.

Estado: no abierta.

### Ruta D - Integracion ejecutable

Requiere serializacion, pruebas de herramienta y permiso operativo.

Estado: bloqueada.

## Resultado operativo

El alcance actual queda acotado:

```text
uso teorico local en AUD-001
sin promocion oficial
sin obligacion para otros expedientes
sin implementacion ejecutable
```

## Siguiente paso

Definir compatibilidad minima entre `REPORT_LAYER` y `DO_CHECK_REPORT` solo como puente de lectura futuro, sin absorcion ni cambio de estatus.

Objetivo cumplido posteriormente por `AUD-001_Compatibilidad_REPORT_LAYER_DO_CHECK.md`.

Siguiente paso vigente: decidir si se requiere una validacion teorica del puente o si basta conservarlo como frontera conceptual.

## Veredicto

`REPORT_LAYER`: local de `AUD-001` por ahora.

Nivel C: no procede todavia.

Expediente propio: no procede todavia.
