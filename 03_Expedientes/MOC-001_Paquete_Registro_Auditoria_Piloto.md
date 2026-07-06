# MOC-001 - Paquete de registro y auditoria de piloto

ID: `MOC-PILOT-REG-AUDIT-PACK-001`.

Ruta: `MOC-ROUTE-009`.

Fecha: 2026-07-06.

Estatus: paquete documental preparado, ejecucion real bloqueada.

Decision asociada: `D-2026-07-06-005`.

## Proposito

Cerrar la deuda documental inmediata posterior a `MOC-ROUTE-008`: metodo de registro sin datos personales y matriz de auditoria de piloto.

El paquete no ejecuta el piloto. Solo prepara las condiciones de registro y auditoria que una decision posterior tendria que revisar antes de cualquier cambio de compuerta.

## Componentes

| Componente | ID | Archivo | Estado |
| --- | --- | --- | --- |
| Metodo de registro sin datos personales | `MOC-PILOT-NODATA-REG-001` | `MOC-001_Metodo_Registro_Sin_Datos_Personales.md` | preparado |
| Matriz de auditoria de piloto | `MOC-PILOT-AUDIT-MATRIX-001` | `MOC-001_Matriz_Auditoria_Piloto.md` | preparada |

## Resultado de ruta

`MOC-ROUTE-009` avanza el frente sin ejecutar piloto.

Quedan atendidas:

- deuda de metodo de registro sin datos personales;
- deuda de rol funcional de auditoria;
- deuda de matriz de auditoria previa;
- regla de rechazo de datos personales;
- criterio documental de bloqueo por perdida de trazabilidad.

## Sigue bloqueado

Sigue bloqueado:

- ejecucion real del piloto;
- reclutamiento de evaluadores;
- recopilacion de respuestas reales;
- uso de personas reales como casos;
- recopilacion de datos personales;
- uso clinico o regulado;
- validacion empirica general;
- modificacion de Canon, Nivel C, `Documento 04` o repositorio por resultados;
- promocion de `Xi`, MOC, R4/Gamma o TCS.

## Banderas vigentes

```text
piloto_autorizado = false
ejecucion_permitida = false
reclutamiento_permitido = false
respuestas_reales_permitidas = false
datos_personales_permitidos = false
uso_clinico = false
modifica_documentos = false
```

## Deudas restantes

- decidir si el piloto queda solo como simulacion documental;
- decidir numero y perfil de evaluadores si alguna vez se autorizan humanos;
- definir condiciones externas de consentimiento si alguna vez hubiera participantes humanos;
- definir formato de reporte agregado final;
- definir criterio de reapertura de compuerta;
- relacion futura con `C-001` / `C-002`;
- Confluencia global;
- Equivalencia global de proyecciones;
- maduracion posterior de `TCS-001`.

## Ruta siguiente recomendada

`MOC-ROUTE-010`: decidir rutas posteriores despues del paquete de registro/auditoria, priorizando si el MOC permanece en simulacion documental, si se prepara criterio de evaluadores sin reclutamiento o si el frente entra en mantenimiento.

