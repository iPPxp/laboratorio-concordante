# PSI-TRASPASO-001 - Decision de eliminacion de copia local

ID decision: `D-2026-07-03-012`.

Estatus: decision operativa de limpieza.

Fecha: 2026-07-03.

Objeto: copia local de traspaso de `PSI-001`.

## Decision

Se elimina del Laboratorio la copia local de traspaso de `PSI-001`.

La fuente activa de psicologia permanece fuera del Laboratorio, en el proyecto independiente `Psicologia Concordante`.

## Alcance

La decision cubre la eliminacion de los archivos locales `03_Expedientes/PSI-001*` que habian quedado como copia de traspaso despues de `D-2026-07-03-006`.

La decision conserva solo la traza de estado y la decision historica agregada en:

- `05_Estado_Proyecto/DECISIONES.md`
- `05_Estado_Proyecto/ESTADO_ACTUAL.md`
- `CURRENT_STATE.md`
- `README.md`

## No cubre

Esta decision no:

- elimina, modifica ni sustituye el proyecto independiente `Psicologia Concordante`;
- reabre psicologia dentro del Laboratorio;
- abre subfrente patologico, clinico ni canonico;
- habilita uso clinico;
- borra la trazabilidad historica ya registrada en decisiones agregadas;
- convierte material de psicologia en dependencia activa del Laboratorio.

## Consecuencia

`PSI-001` deja de existir como copia local de trabajo o traspaso dentro de `03_Expedientes`.

El Laboratorio puede mencionar `PSI-001` solo como antecedente historico transferido o como dependencia externa, y solo mediante decision puente si se quiere usar contenido sustantivo del proyecto independiente.

## Deudas que permanecen

- Mantener visible que la fuente activa ya no esta en este repositorio.
- No usar referencias antiguas de `PSI-001` como evidencia local vigente.
- Si se necesita continuidad entre Laboratorio y `Psicologia Concordante`, abrir decision puente separada.
- Tratar las advertencias automatizadas por referencias historicas a `PSI-001*` como deuda de detector/historial, no como restauracion implicita de la copia.

## Resultado posterior de automatizacion

Se regeneraron los reportes automatizados con `DO-LAB-RUN-001`.

El resultado global quedo `bloqueado` porque `DO-CHECK-MED-001` y continuidad detectan referencias no materializadas a archivos `PSI-001*` ya eliminados, especialmente en materiales historicos o de registro.

Ese bloqueo no revierte la decision de eliminacion: deja una deuda visible para refinar como se tratan referencias historicas a expedientes transferidos.

## Veredicto

La copia de traspaso de `PSI-001` queda eliminada del Laboratorio.

La psicologia queda fuera del repositorio como proyecto independiente.
