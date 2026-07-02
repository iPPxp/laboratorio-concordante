# P-PI - Criterios de cierre para P-PI.0 y P-PI.1

Estatus: criterios provisionales de expediente.

ID: `CRIT-CIERRE-P-PI-001`.

Expedientes padre: `P-PI.0` y `P-PI.1`.

Fuente principal: `05_Estado_Proyecto/DECISION_Siguiente_Frente_Activo_P-PI.md`.

Auditoria asociada: `03_Expedientes/P-PI_Auditoria_Criterios_Cierre.md`.

Decision de estatus asociada: `03_Expedientes/P-PI_Decision_Estatus_Criterios_Cierre.md`.

Decision de ruta asociada: `03_Expedientes/P-PI_Decision_Ruta_Operativa.md`.

## Proposito

Definir criterios de cierre para `P-PI.0` y `P-PI.1` sin resolver por declaracion los problemas abiertos asociados.

Estos criterios no cierran los expedientes. Solo fijan que condiciones deberian cumplirse antes de cerrarlos, congelarlos, absorberlos o mantenerlos abiertos.

## Fuentes locales

- `03_Expedientes/P-PI.0.md`
- `03_Expedientes/P-PI.1.md`
- `05_Estado_Proyecto/ESTADO_ACTUAL.md`
- `05_Estado_Proyecto/DECISION_Siguiente_Frente_Activo_P-PI.md`
- `01_Canon/M-000_Reglas_Fundamentales.md`
- `01_Canon/M-001_Auditoria_Arquitectonica.md`

## Estado actual

`P-PI.0` y `P-PI.1` estan abiertos.

Ambos declaran como problemas relacionados:

- Confluencia
- Equivalencia de proyecciones

Ambos indican que su criterio de cierre debe definirse antes de cerrar el expediente.

## Principios de cierre

Todo cierre futuro debe respetar estas reglas:

- cerrar un expediente no equivale a resolver todos los problemas relacionados
- una deuda matematica puede permanecer abierta si queda trasladada al estado del proyecto
- la ausencia de fuentes historicas no debe rellenarse por inferencia
- una decision de cierre debe declarar que afirma, que no afirma y que deudas conserva
- si una fuente historica falta, debe registrarse como dependencia no materializada
- si el expediente se absorbe, debe existir destino explicito y alcance absorbido
- si el expediente se congela, deben declararse condiciones de reactivacion
- si el expediente continua abierto, debe tener objetivo operativo siguiente

## Rutas posibles

| Ruta | Resultado | Criterio minimo |
| --- | --- | --- |
| Mantener abierto | el expediente sigue activo | objetivo operativo siguiente definido |
| Pausar | el expediente queda abierto sin accion inmediata | frente no prioritario y deudas conservadas |
| Congelar | se conserva la traza sin trabajo activo | falta material local suficiente o dependencia externa bloqueante |
| Absorber | el contenido pasa a otro expediente o documento | destino explicito y alcance absorbido |
| Cerrar | el expediente termina operativamente | decision de cierre, deudas trasladadas y no promocion indebida |

## Criterios comunes obligatorios

Antes de cerrar, congelar, pausar o absorber cualquiera de los dos expedientes, debe existir:

- identificacion del expediente afectado
- declaracion de alcance local
- relacion explicita con Confluencia y Equivalencia de proyecciones
- separacion entre problemas resueltos, problemas abiertos y dependencias externas
- lista de fuentes locales leidas
- lista de fuentes historicas o externas faltantes, si aplica
- clasificacion de afirmaciones relevantes como definicion, hipotesis, problema, deuda o decision
- decision de ruta: abierto, pausa, congelado, absorbido o cerrado
- efecto sobre `ESTADO_ACTUAL.md`
- advertencia de que el cierre operativo no prueba confluencia ni equivalencia de proyecciones

## Criterios para cierre

`P-PI.0` o `P-PI.1` solo puede cerrarse si:

- su proposito local queda suficientemente identificado
- no quedan acciones internas sin registrar
- las deudas no resueltas quedan trasladadas a problemas abiertos o deudas conceptuales
- existe decision de cierre separada
- la decision de cierre declara que no resuelve por si misma Confluencia ni Equivalencia de proyecciones
- no modifica Canon, documentos oficiales ni expedientes cerrados

## Criterios para congelamiento

`P-PI.0` o `P-PI.1` puede congelarse si:

- no hay material local suficiente para trabajo sustantivo
- depende de fuentes historicas no incorporadas
- no existe objetivo operativo inmediato responsable
- se conservan condiciones de reactivacion
- los problemas relacionados permanecen abiertos en el estado del proyecto

## Criterios para absorcion

`P-PI.0` o `P-PI.1` puede absorberse si:

- otro expediente o documento contiene todo su trabajo operativo vigente
- la decision identifica el destino de absorcion
- la decision identifica que queda fuera de la absorcion
- las deudas no absorbidas permanecen en el estado del proyecto

## Criterios para continuidad abierta

`P-PI.0` o `P-PI.1` debe mantenerse abierto si:

- existe una accion local concreta y verificable
- la accion no depende de material historico ausente
- el objetivo siguiente no intenta resolver problemas abiertos por declaracion
- el expediente conserva una frontera clara respecto de documentos oficiales y Canon

## Aplicacion inicial

Con el material local actual, no procede cerrar `P-PI.0` ni `P-PI.1` todavia.

Si no aparece material adicional, la ruta mas probable sera congelamiento o pausa operativa, no cierre.

Antes de decidir esa ruta, estos criterios deben auditarse contra `M-000` y `M-001`.

## Deudas que permanecen

- Auditar estos criterios contra `M-000` y `M-001`. Cumplido posteriormente por `P-PI_Auditoria_Criterios_Cierre.md`.
- Decidir ruta operativa de `P-PI.0` y `P-PI.1` usando estos criterios. Cumplido posteriormente por `P-PI_Decision_Ruta_Operativa.md`.
- Mantener Confluencia y Equivalencia de proyecciones como problemas abiertos hasta tratamiento propio.
- No importar ni usar fuentes historicas como autoridad directa sin registro local.

## Resultado operativo

Objetivo cumplido posteriormente por `P-PI_Auditoria_Criterios_Cierre.md` y `P-PI_Decision_Ruta_Operativa.md`.

## Veredicto

Criterios de cierre para `P-PI.0` y `P-PI.1`: redactados.

Cierre de expedientes: no autorizado por este documento.
