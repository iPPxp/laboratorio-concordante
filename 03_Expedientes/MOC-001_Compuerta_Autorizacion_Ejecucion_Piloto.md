# MOC-001 - Compuerta de autorizacion de ejecucion de piloto

ID: `MOC-GATE-PILOT-EXEC-001`.

Ruta: `MOC-ROUTE-007`.

Fecha: 2026-07-06.

Estatus: compuerta aplicada, ejecucion no autorizada.

Decision asociada: `D-2026-07-06-003`.

## Objeto

Aplicar la compuerta posterior a `MOC-EMP-PILOT-PROTO-001` para decidir si procede autorizar la ejecucion de un piloto empirico futuro.

Esta compuerta no ejecuta piloto, no recluta evaluadores, no usa personas reales, no recopila datos personales y no produce evidencia empirica.

## Evidencia revisada

- `MOC-001_Protocolo_Piloto_Empirico_Futuro.md`.
- `MOC-001_Rutas_Posteriores_Ruta_006.md`.
- `MOC-001_Protocolo_Evaluacion_v0_2.md`.
- `MOC-001_Casos_No_Clinicos.md`.
- `06_Automatizacion/fixtures/moc_cases.json`.
- `06_Automatizacion/reportes/moc_eval_report.json`.
- `06_Automatizacion/reportes/lab_executive_summary.md`.

## Criterios de autorizacion

Para autorizar ejecucion real tendrian que estar satisfechos todos estos criterios:

| Criterio | Estado local | Resultado |
| --- | --- | --- |
| Protocolo documental preparado | existe `MOC-EMP-PILOT-PROTO-001` | satisfecho |
| Dominio sintetico no clinico | definido como frontera obligatoria | satisfecho |
| Ausencia de personas reales | exigida por protocolo | satisfecho como restriccion |
| Ausencia de datos personales | exigida por protocolo | satisfecho como restriccion |
| Paquete congelado de casos | identificado, pero no congelado para piloto | no satisfecho |
| Version congelada de reglas y protocolo | existe base v0.2, pero no hay congelamiento de piloto | no satisfecho |
| Plantilla de respuesta de evaluadores | pendiente | no satisfecho |
| Numero y perfil de evaluadores | pendiente | no satisfecho |
| Metodo de registro de respuestas | pendiente | no satisfecho |
| Tratamiento de anonimato o confirmacion formal de no recoleccion | pendiente | no satisfecho |
| Responsable de auditoria del piloto | pendiente | no satisfecho |
| Criterios operativos de interrupcion y cierre | esbozados, no convertidos en paquete operativo | no satisfecho |

## Resultado de compuerta

```text
piloto_autorizado = false
resultado_compuerta = no_autorizar_ejecucion
dominio = sintetico_no_clinico
casos_reales = false
datos_personales = false
uso_clinico = false
modifica_documentos = false
ejecucion_permitida = false
transformacion_permitida = false
```

## Razon operativa

La ruta mas defensible es no autorizar ejecucion real todavia.

El Laboratorio cuenta con protocolo, reglas, software no mutante y casos sinteticos, pero todavia no cuenta con paquete congelado de piloto, plantilla de respuesta, perfil de evaluadores, metodo cerrado de registro, responsable de auditoria ni tratamiento documental completo de anonimato/no recoleccion.

Autorizar ejecucion en este punto confundiria preparacion documental con estudio empirico real.

## Alcance permitido despues de la compuerta

Queda permitido preparar, sin ejecutar:

- paquete congelado de casos sinteticos para piloto;
- plantilla de respuesta de evaluadores;
- version congelada de reglas y protocolo;
- formato de registro de respuestas sin datos personales;
- matriz de auditoria para piloto futuro;
- relacion documental con `C-001` / `C-002`, si se decide abrirla despues.

## Alcance bloqueado

Queda bloqueado:

- ejecutar piloto empirico;
- reclutar evaluadores;
- recopilar respuestas reales;
- usar personas reales como casos;
- recopilar datos personales;
- abrir uso clinico, patologico, juridico, financiero, laboral, educativo real o institucional regulado;
- presentar resultados como validacion empirica del MOC;
- canonizar `Xi`, admitir `H-Xi`, crear Nivel C o modificar `Documento 04`;
- cerrar Confluencia global o Equivalencia global de proyecciones.

## Deudas abiertas

- congelar paquete de casos sinteticos de piloto;
- crear plantilla de respuesta de evaluadores;
- definir version congelada de reglas/protocolo;
- definir metodo de registro de respuestas sin datos personales;
- definir responsable de auditoria;
- decidir si el piloto futuro puede usar evaluadores humanos o solo simulacion documental;
- relacion futura con `C-001` / `C-002`;
- Confluencia global;
- Equivalencia global de proyecciones;
- maduracion posterior de `TCS-001`.

## Ruta siguiente recomendada

`MOC-ROUTE-008`: preparar paquete documental pre-ejecucion de piloto, sin reclutamiento ni ejecucion, centrado en casos congelados, plantilla de respuesta y reglas de registro sin datos personales.
