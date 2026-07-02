# C-001 - Especificacion Tecnica del Auditor

Estatus: documento oficial de Nivel C.

Fecha: 2026-07-01.

Identificador: `C-001`.

Fuente de promocion: `03_Expedientes/DO-001_Decision_Promocion_SPEC-AUD-001.md`.

Fuente candidata: `03_Expedientes/DO-001_SPEC-AUD-001_Candidata.md`.

## Proposito

Definir la especificacion tecnica inicial del Auditor del Laboratorio Concordante.

El Auditor revisa trazabilidad, estatus, dependencias, reportes, permisos y cambios acotados sin convertirse en autoridad autonoma.

## Fuentes normativas locales

- `01_Canon/M-000_Reglas_Fundamentales.md`
- `01_Canon/M-001_Auditoria_Arquitectonica.md`
- `05_Estado_Proyecto/NIVEL_C_ESPECIFICACIONES.md`
- `03_Expedientes/DO-001.md`
- `03_Expedientes/DO-001_Decision_Modo_Operativo_Auditor.md`
- `03_Expedientes/DO-001_Regla_Permiso_Actualizacion.md`
- `03_Expedientes/AUD-001_Contrato_Reportes.md`
- `03_Expedientes/DO-001_Auditoria_SPEC-AUD-001_NIVEL-C.md`

## Alcance oficial v0

Esta especificacion cubre:

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

Esta especificacion no cubre:

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

La automatizacion puede ser ejecutable en el calculo, pero no autonoma en la autoridad.

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

## Componentes oficiales iniciales

### DO-CHECK-001

Componente ejecutable no mutante.

Lee fuentes locales, verifica trazabilidad y emite `DO_CHECK_REPORT`.

No modifica archivos, no cierra expedientes, no promueve estatus y no autoriza transformaciones.

### Contratos de AUD-001

Los contratos de `AUD-001` definen una gramatica provisional de reportes para operadores del Auditor.

Esta especificacion puede referenciarlos como contratos activos de expediente, no como Canon.

### PERMISO-ACT-001

Compuerta obligatoria entre recomendacion y cambio real.

Ningun cambio ejecutado es valido sin autorizacion previa, alcance acotado y verificacion posterior.

### MODO-AUD-001

Define la frontera entre algoritmo ejecutable y protocolo asistido.

Impide que la automatizacion cree autoridad propia.

## Secuencia operacional minima

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

Esta especificacion se apoya en:

- `DO-001_Validaciones_DO-CHECK-001.md`
- `DO-001_Validaciones_PERMISO-ACT-001.md`
- `DO-001_Validaciones_MODO-AUD-001.md`
- `DO-001_Validaciones_SPEC-AUD-001.md`
- `DO-001_Auditoria_SPEC-AUD-001_NIVEL-C.md`
- `AUD-001_Validaciones.md` para contratos de reportes e hipotesis operativas, incluyendo hasta `VAL-021`

## Limites abiertos

- falta validar transformaciones no triviales
- falta validar reversion real y cuarentena materializada
- falta definir formalmente `R4`
- falta construir formalmente `Gamma`
- falta implementar una herramienta ejecutable completa

## Regla de uso

`C-001` puede usarse como referencia oficial para el diseno y auditoria inicial del Auditor.

No autoriza por si mismo modificaciones de Canon, cierre de expedientes ni ejecuciones fuera de alcance.
