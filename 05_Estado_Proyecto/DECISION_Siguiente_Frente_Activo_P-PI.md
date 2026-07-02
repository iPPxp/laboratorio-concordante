# Decision - Siguiente frente activo P-PI

Estatus: decision operativa de prioridad.

ID: `FRENTE-ACTIVO-P-PI-001`.

Fecha: 2026-07-01.

Objeto decidido: siguiente frente activo del Laboratorio despues de congelar `B-001.5`.

Documento posterior asociado: `03_Expedientes/P-PI_Criterios_Cierre.md`.

## Decision

Se elige el frente `P-PI.0` / `P-PI.1` como siguiente frente activo inmediato.

Alcance del frente:

```text
definir criterios de cierre para P-PI.0 y P-PI.1
```

Esta decision no cierra `P-PI.0` ni `P-PI.1`; solo fija que la definicion de criterios de cierre es el proximo trabajo activo.

## Motivo

`P-PI.0` y `P-PI.1` existen como expedientes abiertos locales y ambos declaran que su criterio de cierre debe definirse antes de cualquier cierre.

El frente es acotado: no exige resolver confluencia ni equivalencia de proyecciones, solo definir que condiciones tendrian que cumplirse para cerrar o pausar esos expedientes responsablemente.

Otros frentes de alto nivel permanecen abiertos, pero dependen de importaciones o definiciones mas pesadas:

- documentos 00 a 03 requieren fuentes previas no incorporadas
- `ROADMAP.md`, Canon v0.1, Decalogo y Regla VII requieren importacion o formalizacion de material no local
- `R4` formal y `Gamma` siguen bloqueados por falta de definicion local
- `H-B.6` y `H-B.7` requieren alcance, pero no tienen archivo local propio visible en el estado actual
- `AUD-001` queda en pausa operativa y no debe reactivarse por inercia

Definir criterios de cierre para `P-PI.0` y `P-PI.1` reduce deuda operativa sin fingir una solucion matematica.

## Alcance permitido

La decision permite:

- tratar `P-PI.0` y `P-PI.1` como frente activo de criterios de cierre
- leer `03_Expedientes/P-PI.0.md` y `03_Expedientes/P-PI.1.md` como fuentes locales principales
- redactar criterios de cierre separados o compartidos para ambos expedientes
- actualizar el estado del proyecto segun los criterios definidos

## Alcance no permitido

La decision no permite:

- cerrar `P-PI.0` o `P-PI.1`
- resolver confluencia o equivalencia de proyecciones por declaracion
- importar contenido historico no disponible
- modificar Canon o documentos oficiales
- reactivar `AUD-001`

## Consecuencia operativa

Objetivo cumplido posteriormente por `03_Expedientes/P-PI_Criterios_Cierre.md`.

## Veredicto

Frente activo inmediato: `P-PI.0` / `P-PI.1`.

Accion siguiente: definir criterios de cierre.
