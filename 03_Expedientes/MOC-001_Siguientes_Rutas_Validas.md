# MOC-001 - Siguientes rutas validas

ID: `MOC-NEXT-ROUTES-001`.

Fecha: 2026-07-05.

Estatus: matriz provisional de rutas posteriores.

## Punto de partida

`MOC-ROUTE-EXEC-001` queda ejecutada favorablemente:

- `MOC-EVAL-001`: 7 casos, 7 aprobados, 0 fallos.
- protocolo: 4 coincidencias exactas, 3 coincidencias parciales, 0 desacuerdos justificados.
- guardas: sin admision de `H-Xi`, sin canonizacion de `Xi`, sin uso clinico y sin transformacion.

## Rutas validas inmediatas

### Ruta 2 - Ampliar bateria sintetica no clinica

ID sugerido: `MOC-ROUTE-002`.

Objetivo:

- agregar casos sinteticos no clinicos con desacuerdo justificado;
- agregar casos donde falte un eje TCS secundario;
- agregar casos de conflicto de autoridad no global;
- agregar casos limite entre `concordancia_parcial` y `friccion_operativa`.

Razon:

La primera ruta ya cubre salidas y estados, pero no fuerza desacuerdos justificados. La bateria debe incluir friccion interpretativa controlada.

Resultado esperado:

- `MOC-EVAL-001` ampliado sin mutacion;
- reporte con coincidencia exacta, coincidencia parcial y desacuerdo justificado mayor que 0.

### Ruta 3 - Formalizar puente MOC/TCS

ID sugerido: `MOC-ROUTE-003`.

Objetivo:

- mapear salidas de `Xi_eval_MOC` contra ejes TCS;
- precisar cuando una deuda TCS degrada un estado MOC;
- definir reglas de desempate entre `bloqueo_de_concordancia`, `no_comparable`, `friccion_operativa` y `discordancia_global`.

Razon:

`MOC-001` usa TCS, pero todavia falta una correspondencia formal entre ejes, estados y deuda.

Resultado esperado:

- documento de puente `MOC-TCS-BRIDGE-001`;
- casos de prueba adicionales o fixture ampliado.

### Ruta 4 - Formalizar puente MOC/AO

ID sugerido: `MOC-ROUTE-004`.

Objetivo:

- conectar estados MOC con testigos de `AO-PPI-BRIDGE-001`;
- precisar cuando una salida MOC puede servir como evidencia auxiliar para Confluencia o Equivalencia local;
- conservar `Documento 04` sin cambios.

Razon:

`MOC-001` debe relacionarse con proyecciones y confluencia sin cerrar problemas globales ni modificar el documento oficial.

Resultado esperado:

- documento de puente `MOC-AO-BRIDGE-001`;
- prueba local no regulada que use reportes MOC como evidencia auxiliar.

### Ruta 5 - Refinar protocolo de evaluadores

ID sugerido: `MOC-ROUTE-005`.

Objetivo:

- separar desacuerdo por friccion, falta de evidencia, ambiguedad de regla y conflicto de autoridad;
- definir formato minimo de justificacion;
- definir tratamiento de desacuerdo repetido.

Razon:

La primera prueba muestra coincidencia parcial, pero todavia no estresa desacuerdo justificado.

Resultado esperado:

- protocolo v0.2 no canonico;
- plantilla de evaluacion mas estricta.

### Ruta 6 - Preparar piloto empirico no ejecutado

ID sugerido: `MOC-ROUTE-006`.

Objetivo:

- convertir `MOC-EMP-STUDY-001` en protocolo de piloto futuro;
- mantenerlo documental, sin reclutamiento y sin personas reales;
- definir criterios minimos para una decision posterior de ejecucion.

Razon:

El MOC ya tiene diseno empirico futuro, pero no debe ejecutarse sin compuerta.

Resultado esperado:

- protocolo de piloto no ejecutado;
- lista de condiciones de apertura futura.

## Rutas bloqueadas por ahora

- Admision de `H-Xi`.
- Canonizacion de `Xi`.
- Promocion del MOC a Canon o Nivel C.
- Uso clinico, patologico, diagnostico o terapeutico.
- Evaluacion de personas reales.
- Reapertura de `PSI-001` dentro del Laboratorio.
- Modificacion de `Documento 04`.
- Cierre de Confluencia global o Equivalencia global.
- Exportacion general de R4/Gamma.

## Ruta recomendada

La ruta mas defensible es `MOC-ROUTE-002`: ampliar la bateria sintetica no clinica para incluir desacuerdos justificados y casos limite.

Justificacion:

- conserva el alcance no clinico;
- fortalece el protocolo antes de formalizar puentes externos;
- produce evidencia local ejecutable;
- no modifica Canon, Nivel C ni `Documento 04`;
- prepara mejor `MOC-ROUTE-003` y `MOC-ROUTE-004`.
