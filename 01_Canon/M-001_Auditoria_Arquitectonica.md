# M-001 - Auditoria Arquitectonica

Estatus: Canon.

Decision de adopcion de matriz de superficies: `D-2026-07-09-005`.

## Proposito

M-001 define como auditar una intervencion dentro del Laboratorio Concordante.

Una auditoria no busca producir ideas nuevas como prioridad. Busca verificar coherencia, estatus, dependencias, deudas y efectos sobre el repositorio vigente.

## Procedimiento minimo

1. Leer `CURRENT_STATE.md`.
2. Leer `05_Estado_Proyecto/ESTADO_ACTUAL.md`.
3. Leer `M-000`.
4. Identificar documentos y expedientes afectados.
5. Clasificar cada afirmacion relevante.
6. Detectar dependencias no registradas.
7. Registrar deudas conceptuales antes de usarlas como base.
8. Indicar si la intervencion modifica documentos, expedientes, estado o Canon.

## Criterios de hallazgo

Un hallazgo puede ser:

- contradiccion
- ambiguedad
- dependencia no registrada
- hipotesis promovida indebidamente
- problema abierto omitido
- expediente mal ubicado
- decision no trazada
- mejora editorial sin cambio conceptual

## Salida esperada

Toda auditoria debe producir, como minimo:

- alcance
- fuentes leidas
- hallazgos
- impacto
- deudas conceptuales
- recomendacion de cierre, continuacion o reapertura

## Matriz de superficies para intervenciones de nivel sensible

Adopcion oficial acotada por `D-2026-07-09-005`, desde `MOC-CANON-DOC04-APPLY-001`.

Si una auditoria evalua una intervencion que podria afectar Canon, documentos oficiales, Nivel C o un expediente con autoridad vigente, la salida debe separar:

- lo que se propone para Canon;
- lo que se propone para documento oficial;
- lo que queda solo en expediente;
- lo que queda prohibido;
- la deuda conceptual que impide incorporacion.

Una propuesta candidata no equivale a incorporacion oficial ni a permiso material. Toda incorporacion a Canon o documento oficial requiere decision posterior separada, salvo cuando la decision vigente declare expresamente la superficie exacta, el texto adoptado y la verificacion posterior.

Esta matriz no crea autoridad nueva. Solo vuelve obligatoria la separacion de superficies cuando una auditoria toca niveles sensibles.
