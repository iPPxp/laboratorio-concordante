# DO-001 - SPEC-AUD-001 Candidata

Estatus: especificacion tecnica candidata promovida.

Expediente padre: `DO-001`.

Fecha: 2026-07-01.

Identificador: `SPEC-AUD-001_Candidata`.

Fuente de alcance: `03_Expedientes/DO-001_Decision_Alcance_SPEC-AUD-001.md`.

## Advertencia de estatus

Este archivo no es documento oficial.

Fue promovida a `02_Documentos/C-001_Especificacion_Tecnica_Auditor.md` por `PROM-SPEC-AUD-001`.

Su funcion actual es conservar la trazabilidad de la fuente candidata que dio origen a `C-001`.

## Proposito

Definir el alcance tecnico candidato del Auditor del Laboratorio Concordante.

El Auditor debe revisar trazabilidad, estatus, dependencias, reportes, permisos y cambios acotados sin convertirse en autoridad autonoma.

## Fuentes normativas locales

- `01_Canon/M-000_Reglas_Fundamentales.md`
- `01_Canon/M-001_Auditoria_Arquitectonica.md`
- `03_Expedientes/DO-001.md`
- `03_Expedientes/DO-001_DO-CHECK-001.md`
- `03_Expedientes/DO-001_Regla_Permiso_Actualizacion.md`
- `03_Expedientes/DO-001_Decision_Modo_Operativo_Auditor.md`
- `05_Estado_Proyecto/NIVEL_C_ESPECIFICACIONES.md`
- `03_Expedientes/AUD-001_Contrato_Reportes.md`
- `03_Expedientes/AUD-001_Validaciones.md`

## Alcance v0

El alcance candidato cubre:

- lectura de fuentes locales autorizadas
- verificacion de estatus de afirmaciones
- deteccion de dependencias no materializadas
- deteccion de uso indebido del Registro Historico como autoridad
- deteccion de efectos sobre Canon, documentos oficiales o expedientes cerrados
- emision de reportes normalizados
- comparacion entre decision emitida y decision permitida
- aplicacion de `PERMISO-ACT-001` antes de cambios reales
- registro de evidencia antes y despues cuando exista ejecucion autorizada
- verificacion posterior obligatoria

## Fuera de alcance v0

Queda fuera de esta candidata:

- modificacion automatica de Canon
- promocion automatica de hipotesis
- cierre automatico de expedientes
- importacion de Registro Historico como autoridad vigente
- resolucion formal de `R4`
- construccion formal de `Gamma`
- transformaciones no triviales
- reversion real ejecutada
- cuarentena materializada
- implementacion completa de herramienta ejecutable

## Modo operativo

El Auditor opera en modo mixto segun `MODO-AUD-001`.

```text
calculo y reporte -> ejecutable
autoridad y permiso -> asistido o decision registrada
ejecucion real -> ejecutable solo si esta previamente autorizada
```

## Entradas permitidas

- archivo local del repositorio
- conjunto acotado de archivos locales
- expediente abierto
- propuesta de cambio con alcance declarado
- reporte normalizado producido por otro operador
- instruccion humana explicita dentro del alcance permitido

## Entradas no permitidas como autoridad

- conversaciones historicas sin decision registrada
- referencias mencionadas pero no materializadas
- hipotesis sin demostracion, auditoria o decision
- salida de herramienta sin estatus declarado
- deuda conceptual usada como fundamento positivo

## Salidas permitidas

- `DO_CHECK_REPORT`
- `OPERATOR_REPORT` y reportes derivados de `AUD-001` por referencia
- hallazgos clasificados segun `M-001`
- deudas conceptuales nuevas
- recomendacion de bloquear, escalar o continuar sin transformar
- propuesta de actualizacion de estado
- propuesta de changelog
- registro de ejecucion acotada solo si existe autorizacion valida

## Salidas prohibidas

- promocion de hipotesis a Canon
- cierre de expediente sin decision explicita
- modificacion de documentos oficiales sin decision registrada
- modificacion de Canon sin decision canonica o arquitectonica
- transformacion ejecutada sin autorizacion previa
- aprobacion fundada en reporte bloqueante
- eliminacion silenciosa de deuda conceptual

## Componentes candidatos

### DO-CHECK-001

Componente ejecutable no mutante.

Lee fuentes locales, verifica trazabilidad y emite `DO_CHECK_REPORT`.

No modifica archivos, no cierra expedientes, no promueve estatus y no autoriza transformaciones.

### Reportes de AUD-001

Los contratos de `AUD-001` definen una gramatica provisional de reportes para operadores del Auditor.

La candidata puede referenciarlos como contratos de expediente activos, no como Canon.

### PERMISO-ACT-001

Compuerta obligatoria entre recomendacion y cambio real.

Ningun cambio ejecutado es valido sin autorizacion previa, alcance acotado y verificacion posterior.

### MODO-AUD-001

Define la frontera entre algoritmo ejecutable y protocolo asistido.

Impide que la automatizacion cree autoridad propia.

## Secuencia operacional candidata

```text
1. Leer fuentes minimas.
2. Clasificar estatus, dependencias y riesgos de nivel.
3. Emitir reporte normalizado.
4. Si hay recomendacion, conservarla como recomendacion.
5. Si hay autorizacion valida, ejecutar solo el cambio acotado.
6. Registrar evidencia antes y despues.
7. Ejecutar verificacion posterior.
8. Actualizar estado operativo solo si el permiso lo cubre.
```

## Invariantes

- una fuente de nivel inferior no modifica por si misma una fuente superior
- toda afirmacion relevante conserva estatus declarado
- toda dependencia no materializada se registra como deuda antes de usarse
- una recomendacion no equivale a autorizacion
- una autorizacion no equivale a ejecucion
- una ejecucion fallida no equivale a ejecucion valida
- el estado posterior de un cambio debe verificarse antes de registrarse como valido

## Estado de validacion

La candidata se apoya en validaciones provisionales existentes:

- `DO-VAL-001` a `DO-VAL-003` para `DO-CHECK-001`
- `PERM-VAL-001` a `PERM-VAL-003` para `PERMISO-ACT-001`
- `MODO-VAL-001` a `MODO-VAL-004` para `MODO-AUD-001`
- `VAL-001` a `VAL-008` para contratos de `AUD-001`

Validacion propia: `03_Expedientes/DO-001_Validaciones_SPEC-AUD-001.md`.

Auditoria de Nivel C: `03_Expedientes/DO-001_Auditoria_SPEC-AUD-001_NIVEL-C.md`.

Decision de promocion: `03_Expedientes/DO-001_Decision_Promocion_SPEC-AUD-001.md`.

Documento oficial derivado: `02_Documentos/C-001_Especificacion_Tecnica_Auditor.md`.

## Limites abiertos

- falta validar transformaciones no triviales
- falta validar reversion real y cuarentena materializada

## Criterio de promocion

`SPEC-AUD-001_Candidata` fue promovida a `C-001`; este archivo queda como fuente trazable de la promocion.
