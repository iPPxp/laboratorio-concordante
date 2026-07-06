# MOC-001 - Protocolo documental de piloto empirico futuro

ID: `MOC-EMP-PILOT-PROTO-001`.

Ruta: `MOC-ROUTE-006`.

Fecha: 2026-07-06.

Estatus: protocolo documental preparado, no ejecutado.

Decision asociada: `D-2026-07-06-001`.

## Proposito

Preparar un protocolo de piloto empirico futuro para comparar el MOC con baselines simples en tareas sinteticas no clinicas.

Este documento no ejecuta el piloto, no recluta evaluadores, no usa personas reales, no recoge datos personales y no produce resultado empirico. Solo fija condiciones, materiales, variables y compuertas para que una decision posterior pueda decidir si procede ejecutar un piloto.

## Pregunta de piloto

Pregunta principal:

```text
Si distintos evaluadores aplican el MOC a los mismos casos sinteticos no clinicos,
la combinacion de Xi_eval, estados MOC, operator_trace, ao_bridge y protocolo v0.2
produce clasificaciones mas reproducibles y trazables que baselines simples?
```

Preguntas secundarias:

- El MOC conserva mejor la deuda que una evaluacion narrativa libre?
- `operator_trace` reduce ambiguedad de regla sin borrar desacuerdos?
- `ao_bridge` ayuda a distinguir evidencia local, friccion, bloqueo y deuda global?
- El protocolo v0.2 identifica desacuerdos repetibles sin forzar unanimidad?

## Alcance permitido

El piloto futuro solo podria usar:

- casos sinteticos no clinicos;
- datos ficticios o abstractos;
- tareas de clasificacion documental;
- evaluadores sobre plantillas, no sobre personas;
- salidas ordinales/cualitativas;
- reportes de concordancia, desacuerdo y deuda.

## Alcance prohibido

Queda prohibido:

- usar personas reales como casos;
- evaluar salud mental, rasgos psicologicos, diagnostico, tratamiento o patologia;
- usar dominios clinicos, juridicos, financieros, laborales, educativos reales o institucionales regulados;
- recopilar datos personales;
- ejecutar intervenciones;
- cualquier cambio de repositorio, Canon, documentos oficiales o Nivel C derivado del piloto;
- presentar resultados como validacion empirica general del MOC.

## Materiales documentales

Materiales que deberian congelarse antes de cualquier ejecucion futura:

- `MOC-001_Casos_No_Clinicos.md`;
- `06_Automatizacion/fixtures/moc_cases.json`;
- `MOC-001_Formalizacion_Xi_eval.md`;
- `MOC-001_Metricas_Estados.md`;
- `MOC-001_Protocolo_Evaluacion.md`;
- `MOC-001_Protocolo_Evaluacion_v0_2.md`;
- `MOC-001_Puente_Formal_MOC_TCS.md`;
- `MOC-001_Puente_Formal_MOC_AO.md`;
- `MOC-001_Disenio_Estudio_Empirico.md`.

## Tareas candidatas

### Tarea A - Clasificacion MOC

Cada evaluador recibe un caso sintetico y emite:

- salida `Xi_eval`;
- estado MOC;
- deuda;
- justificacion breve;
- ejes de desacuerdo si aplica.

### Tarea B - Checklist simple

Cada evaluador recibe el mismo caso y usa solo una checklist de evidencia:

- evidencia presente;
- autoridad declarada;
- decision registrada;
- deuda visible;
- bloqueo o no bloqueo.

### Tarea C - Lectura narrativa libre

Cada evaluador produce una clasificacion libre con justificacion breve, sin reglas de prioridad.

### Tarea D - Lectura TCS minima

Cada evaluador clasifica solo ejes TCS, sin `Xi_eval` ni puente AO.

## Salidas comparables

Las salidas comparables serian:

- coincidencia exacta;
- coincidencia parcial por familia;
- desacuerdo justificado;
- deuda conservada;
- bloqueo conservado;
- casos con `review_required`;
- casos con perdida de trazabilidad.

## Medidas cualitativas

El piloto futuro mediria de forma cualitativa ordinal:

| Medida | Definicion | Fuente |
| --- | --- | --- |
| `coincidencia_exacta` | misma salida y mismo estado | protocolo MOC |
| `coincidencia_parcial` | misma familia, estado distinto | protocolo MOC |
| `desacuerdo_justificado` | familias distintas con razon auditable | protocolo v0.2 |
| `deuda_visible` | deuda reportada sin cierre artificial | reporte de evaluador |
| `bloqueo_conservado` | caso bloqueado sin uso positivo | salida MOC/AO |
| `trazabilidad_de_regla` | existe regla ganadora y testigo | `operator_trace` / `ao_bridge` |

No se definen metricas numericas universales.

## Condiciones minimas para ejecutar en el futuro

Una decision posterior tendria que definir:

- version congelada del paquete de casos;
- version congelada de reglas y protocolo;
- numero y perfil de evaluadores, si fueran humanos;
- ausencia de datos personales;
- forma de consentimiento si hubiera participantes humanos;
- plan de anonimato o confirmacion de no recoleccion de datos personales;
- metodo de registro de respuestas;
- criterio de interrupcion;
- criterio de exito y fracaso;
- tratamiento de desacuerdos;
- formato de reporte final;
- responsable de auditoria.

## Compuerta de ejecucion futura

La ejecucion futura queda bloqueada hasta que exista una decision separada que declare:

```text
piloto_autorizado = true
dominio = sintetico_no_clinico
casos_reales = false
datos_personales = false
uso_clinico = false
modifica_documentos = false
```

Sin esa decision, el protocolo permanece preparado pero inactivo.

## Reporte futuro esperado

Si una decision futura autorizara ejecucion, el reporte deberia incluir:

- version exacta de materiales;
- matriz de respuestas por evaluador;
- comparacion entre MOC y baselines;
- tabla de desacuerdos;
- deuda conservada;
- bloqueos conservados;
- limites;
- recomendacion no canonica.

## Criterios de fallo futuro

El piloto futuro deberia fallar o detenerse si:

- aparece informacion personal o caso real;
- un evaluador intenta hacer inferencias clinicas;
- se usa el resultado como validacion general;
- aparecen cambios documentales derivados del resultado del piloto;
- se oculta deuda o se fuerza unanimidad;
- se intenta cerrar Confluencia global o Equivalencia global.

## Deudas abiertas

- decision futura de autorizacion o no autorizacion del piloto;
- paquete congelado de casos para piloto;
- plantilla de respuesta de evaluadores;
- relacion futura con `C-001` / `C-002`;
- Confluencia global;
- Equivalencia global de proyecciones;
- maduracion posterior de `TCS-001`.
