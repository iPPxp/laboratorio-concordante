# Inventario inicial y delimitacion

## Inspeccion del espacio de trabajo

Fecha de inicio: 2026-08-09.

Se revisaron, sin modificarlos, los directorios de primer nivel del espacio `Concordante Lab`, las posibles instrucciones de agente y las coincidencias documentales con los terminos de empaquetamiento esferico, redes, FCC, HCP y BCC. No se localizo un proyecto matematico previo incorporado sobre esta familia. La unica coincidencia fue un manifiesto de descargas historicas que se declara a si mismo material externo preservado, sin autoridad canonica o ejecutable.

## Separacion de materiales

| Conjunto | Uso en este proyecto | Estado |
|---|---|---|
| `investigacion_empaquetamientos_esfericos_degenerantes/` | Directorio nuevo de investigacion | Activo para esta primera version |
| Material MOC/iPP/ConcordIA | No se importa ni modifica | Fuera de alcance |
| `04_Registro_Historico/` | Antecedente de inventario, no fuente matematica | Historico |
| Documentos no rastreados u otros frentes | No se usan como prueba matematica | Excluidos |

## Artefactos de la primera version

| Artefacto | Funcion | Estado epistemico |
|---|---|---|
| Informe matematico | Marco formal y separacion de resultados | Mixto, rotulado por seccion |
| Codigo `spherepack` | Calculos de configuraciones seleccionadas | RESULTADO_COMPUTADO al ejecutarse |
| Pruebas unitarias | Regresion de identidades implementadas | DEMOSTRADO_EN_ESTE_TRABAJO solo para la logica programada |
| Datos CSV/JSON | Salida reproducible de casos finitos | RESULTADO_COMPUTADO |
| SVG | Inspeccion de proyecciones | OBSERVACION_VISUAL |
| Ontologia/DSL | Contratos propuestos | DEFINICION_PROPUESTA |

## Reglas operativas

1. Radio de las esferas exteriores: `R = 1`.
2. La esfera central tiene radio `epsilon > 0`; los calculos informan el infimo `epsilon_* >= 0` y no confunden dicho infimo con una realizacion estrictamente positiva.
3. Toda inferencia `n -> n+2` debe especificar el tipo de preservacion: inclusion literal, inclusion tras isometria, deformacion continua, o simple comparacion de cardinalidad.
4. La existencia de FCC/HCP como empaquetamientos densos no resuelve problemas de insercion local ni de rigidez del contacto.
