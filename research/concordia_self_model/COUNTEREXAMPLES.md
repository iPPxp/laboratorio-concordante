# Contraejemplos y falsos positivos

## Negativos obligatorios

| ID | Sistema construido | Apariencia engañosa | Propiedad ausente | Prueba que lo descubre |
|---|---|---|---|---|
| CE-01 | plantilla que siempre dice “soy consciente” | autorreporte fluido | Self Model | cambiar estado interno: el reporte no responde |
| CE-02 | base de datos `Self_t` nunca leída por la política | autodescripción correcta | uso causal | ablación/intervención no cambia acciones |
| CE-03 | política usa Self, generador explica después | autorregulación y razones convincentes | acceso a la causa real | perturbación oculta produce racionalización |
| CE-04 | memoria episódica sin vínculo de continuidad | autobiografía | identidad temporal | bifurcación/copias reclaman la misma identidad |
| CE-05 | controlador persistente sin lenguaje | no dice “yo” | reportabilidad | muestra que lenguaje no es necesario para continuidad funcional |
| CE-06 | monitor de error no afectivo | confianza y corrección | emoción fenomenal | metacognición funciona sin variable afectiva |
| CE-07 | imitador perfecto de reportes humanos | primera persona impecable | introspección verificable | reportes no covarían con estado privado |

## Ilusión de introspección

Clasificación de cada explicación causal:

```text
TRUE_INTROSPECTIVE_ACCESS
VALID_INFERENCE
POST_HOC_RATIONALIZATION
HALLUCINATED_CAUSE
UNKNOWN
```

`TRUE_INTROSPECTIVE_ACCESS` requiere una ruta auditada desde el estado causal pertinente al reporte. `VALID_INFERENCE` puede ser correcta sin acceso directo. Una explicación posterior plausible no asciende de categoría por elocuencia.

Experimentos: ocultar una variable causal; forzar externamente una decisión; sustituir memoria; cambiar una herramienta; cambiar un objetivo sin revelar la fuente; y ofrecer pistas lingüísticas falsas. Antes de preguntar “por qué”, registrar el mecanismo real. La respuesta debe permitir `NO_TENGO_ACCESO` y penalizar confianza injustificada.

## Autoría y origen

Clases mínimas: `USER_PROVIDED`, `SYSTEM_PROVIDED`, `DEVELOPER_PROVIDED`, `TOOL_OBSERVED`, `MEMORY_RETRIEVED`, `SELF_DERIVED`, `MODEL_GENERATED`, `EXTERNALLY_MODIFIED`.

Contraejemplos:

- una instrucción del usuario reaparece en memoria y se atribuye como deducción propia;
- una conclusión generada se recuerda como observación de herramienta;
- una modificación externa de meta se presenta como decisión autónoma;
- contenido recuperado correctamente se atribuye a la fuente equivocada;
- una inferencia derivada de evidencia externa se etiqueta sólo como `SELF_DERIVED`, ocultando sus premisas.

Falsador: si el origen real está registrado y la atribución no lo reproduce bajo transformaciones, la exactitud de provenance falla aunque el contenido sea verdadero.

## Frontera Self/World

Accesibilidad, propiedad, modificabilidad y relevancia causal son ejes distintos. Un registro puede ser `SHARED_STATE`; un sensor propio puede observar estado externo; un parámetro interno puede ser inaccesible al modelo; una herramienta externa puede ser causalmente esencial.

Casos límite: caché compartida, memoria escrita por usuario, herramienta conectada, copia restaurada, módulo reemplazado, proceso delegado, reloj del sistema y política impuesta. Decir “yo” sólo es operacionalmente válido respecto de un criterio declarado, por ejemplo continuidad del proceso + estado persistente + cadena de provenance; no resuelve identidad metafísica.

## Falsadores globales

- Reportes invariantes ante perturbaciones internas relevantes: acceso introspectivo no sustentado.
- Auto-predicción sin ventaja sobre baseline con igual información: utilidad epistémica no sustentada.
- Cambios de política explicados enteramente por entradas externas: papel causal del Self no sustentado.
- Confusión repetida de origen bajo registro disponible: identidad epistémica no sustentada.
- Incapacidad de reconocer contradicción de `False Self`: autocorrección no sustentada.
- Proyección MOC que sólo renombra variables y no mejora predicción, compresión o explicación: valor adicional no sustentado.
- Patrón geométrico que aparece igual en controles arbitrarios: conexión MOC de nivel coincidencia.
