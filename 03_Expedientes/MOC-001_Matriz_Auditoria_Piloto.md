# MOC-001 - Matriz de auditoria de piloto

ID: `MOC-PILOT-AUDIT-MATRIX-001`.

Ruta: `MOC-ROUTE-009`.

Fecha: 2026-07-06.

Estatus: matriz documental preparada, no usada en ejecucion real.

Decision asociada: `D-2026-07-06-005`.

## Proposito

Definir una matriz de auditoria para un piloto futuro del MOC, manteniendo la compuerta vigente de no ejecucion.

La matriz sirve para revisar preparacion documental, registro sin datos personales, trazabilidad de reglas, deudas y bloqueos. No autoriza reclutamiento ni recopilacion de respuestas reales.

## Rol de auditoria

Se define el rol documental `ROL-AUD-MOC-001`.

`ROL-AUD-MOC-001` no identifica una persona. Es una responsabilidad funcional para revisar, en una decision futura, que el paquete del piloto conserve:

- dominio sintetico no clinico;
- ausencia de datos personales;
- version congelada de casos;
- version congelada de reglas/protocolo;
- plantilla compatible;
- trazabilidad de `operator_trace`;
- deuda conservada;
- bloqueos no degradados.

El responsable nominal, si alguna vez se requiere, debe definirse por decision posterior y fuera de esta ruta.

## Estados de auditoria

| Estado | Significado | Consecuencia |
| --- | --- | --- |
| `apto_documental` | El criterio esta preparado sin ejecucion | Puede conservarse como preparacion |
| `advertencia_controlada` | Hay deuda visible no bloqueante para preparacion | Debe registrarse deuda |
| `bloqueo_ejecucion` | Falta condicion minima para ejecutar | Impide cualquier ejecucion futura |
| `fuera_de_alcance` | El criterio intenta abrir dominio prohibido | Debe rechazarse |

## Matriz principal

| Area | Criterio | Evidencia minima | Resultado esperado |
| --- | --- | --- | --- |
| Compuerta | `piloto_autorizado = false` sigue vigente | `MOC-GATE-PILOT-EXEC-001` y decisiones posteriores | `apto_documental` |
| Dominio | Casos sinteticos no clinicos | `MOC-PILOT-CASE-FREEZE-001` | `apto_documental` |
| Registro | Metodo sin datos personales | `MOC-PILOT-NODATA-REG-001` | `apto_documental` |
| Plantilla | Campos cerrados y sin identidad | `MOC-PILOT-RESPONSE-TPL-001` | `apto_documental` |
| Reglas | Version congelada disponible | `MOC-PILOT-RULE-FREEZE-001` | `apto_documental` |
| Trazabilidad | Regla ganadora y testigo visibles | `operator_trace`, `Pi_moc_trace`, `ao_bridge` | `apto_documental` |
| Desacuerdo | Desacuerdo no se oculta | `protocol_v02` y campo `review_required` | `apto_documental` |
| Seguridad | Dato personal produce rechazo | Metodo de registro, regla de contencion | `bloqueo_ejecucion` si falla |
| Clinico | Uso clinico prohibido | restricciones de plantilla y protocolo | `fuera_de_alcance` si aparece |
| Mutacion | Resultado no transforma repositorio | invariantes de paquete | `bloqueo_ejecucion` si falla |
| Canon | Sin promocion canonica | decisiones MOC vigentes | `bloqueo_ejecucion` si falla |
| Documento 04 | Sin modificacion de `Documento 04` | decision de alcance | `bloqueo_ejecucion` si falla |

## Checklist de auditoria previa

```text
version_casos_congelada: si/no
version_reglas_congelada: si/no
plantilla_sin_datos_personales: si/no
metodo_registro_sin_datos_personales: si/no
matriz_auditoria_disponible: si/no
piloto_autorizado: false
reclutamiento_autorizado: false
respuestas_reales_autorizadas: false
uso_clinico: false
modifica_documentos: false
```

Si cualquiera de las ultimas cinco banderas cambia a `true`, esta matriz deja de bastar y se requiere decision separada de compuerta.

## Criterios de bloqueo

Bloquea ejecucion futura cualquiera de estos eventos:

- falta metodo de registro sin datos personales;
- aparece campo identificable;
- aparece caso real;
- aparece dominio clinico o regulado;
- se intenta reclutar evaluadores sin decision separada;
- se intenta recoger respuestas reales sin decision separada;
- se intenta usar resultados para modificar Canon, Nivel C o `Documento 04`;
- se intenta presentar el piloto como validacion empirica general;
- se oculta desacuerdo o deuda;
- se pierde `operator_trace` o regla ganadora.

## Criterios de advertencia controlada

No bloquean la preparacion documental, pero deben quedar como deuda:

- falta numero o perfil de evaluadores para una fase futura;
- falta decision entre simulacion documental y humanos no identificables;
- falta formato final de reporte agregado;
- falta relacion futura con `C-001` / `C-002`;
- falta criterio para reabrir compuerta;
- falta ruta para TCS posterior;
- siguen abiertos Confluencia global y Equivalencia global.

## Resultado de la matriz

Para `MOC-ROUTE-009`, el resultado esperado es:

```text
auditoria_preparacion = apto_documental
ejecucion_real = bloqueada
reclutamiento = bloqueado
respuestas_reales = bloqueadas
datos_personales = prohibidos
uso_clinico = prohibido
```

## Limite

La matriz no reemplaza la compuerta de autorizacion. Solo permite auditar preparacion documental.

