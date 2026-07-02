# REC-001 - Mapa de reconciliacion Canon/baselines

Estatus: mapa provisional de reconciliacion cerrado por `REC-001_Decision_Cierre.md`.

Fecha: 2026-07-01.

## Lectura general

Las fuentes historicas usan nombres que se parecen a los nombres vigentes, pero no siempre designan el mismo nivel. La reconciliacion evita igualar por etiqueta y compara por funcion.

## Diagnostico por fuente

| Fuente | Capa principal | Relacion con workspace vigente | Dictamen |
| --- | --- | --- | --- |
| `SRC-007` Canon `M-000 v0.1` | nucleo matematico/GDI | no equivalente al `M-000` vigente | conservar como candidato de formalizacion matematica |
| `SRC-008` consolidacion `M-000` | resumen del nucleo matematico | refuerza `SRC-007`; no sustituye Canon actual | conservar como guia de importacion futura |
| `SRC-010` baseline `v1.0.0` | baseline operativo del AAU | parcialmente paralelo a `C-001` y `AUT-001`, pero mas amplio | comparar en expediente tecnico futuro |
| `SRC-012` zip `v1.0.0` | repo historico estructurado | contiene Canon, arquitectura, matematica, protocolos e implementacion | no sobrescribir; extraer por modulos |
| `SRC-013` zip `v1.0.0-fase2` | repo historico con AAU reforzado | relevante para automatizacion media/futura | no ejecutar; comparar con `DO-CHECK-MIN-001` y `C-001` |
| `SRC-023` zip `v1.5` | cierre fundacional historico | contiene reglas, decalogo, hipotesis y registro | descomponer en candidatos separados |

## Mapa funcional

| Elemento historico | Estado en workspace vigente | Reconciliacion |
| --- | --- | --- |
| `M-000 - Auditoria Interna` historico | parcialmente cubierto por `M-001` vigente y `M-000.8` | no importar por nombre; mantener equivalencia funcional parcial |
| `M-001 - Presuncion de Reducibilidad` historico | no canonizado explicitamente | candidato a regla o criterio de admision; requiere expediente |
| `C-001 - Reduccion Conceptual` historico | no canonizado como regla general | candidato metodologico; requiere separarlo del `C-001` vigente, que ya es especificacion del Auditor |
| `C-002 - Criterio de Parada` historico | no incorporado como regla general | candidato para protocolos de reduccion/admisiones |
| `EF-001 - Economia Formal` historico | `EF-001` actual esta cerrado/no reabrir sin decision explicita | no reabrir automaticamente; solo ficha de trazabilidad futura |
| Doble Auditoria | parcialmente reflejada en auditorias internas, no como regla formal | candidato metodologico |
| Clausula de Incompletitud | espiritu presente en no promocion automatica y deudas | candidato a principio explicito |
| Decalogo y Regla VII | mencionado como deuda previa | fuente localizada en `SRC-023`; pendiente de formalizacion separada |
| `AAU v0.1` | no equivalente a `DO-CHECK-MIN-001` | candidato para automatizacion media/futura |
| `Presv`, `Activas(G)`, `Inv(G)`, `Break(Fk)` | no formalizados localmente | candidatos del nucleo ejecutable |
| `R4` historico | problema abierto local | fuente historica util, no definicion vigente |
| `Gamma` / GDI-core | problema abierto local | nucleo matematico pendiente |
| `H-Xi` | ficha local en `03_Expedientes/H-Xi.md` | hipotesis externa materializada, no admitida |
| Concordancia `C-100` | deuda condicionada por `RH-001` y `RH-002` | no abrir sin decision de frente |

## Deudas refinadas

- `REC-DEUDA-001`: decidir separacion formal entre Canon de gobierno vigente y nucleo matematico/GDI historico.
- `REC-DEUDA-002`: evaluar reglas metodologicas historicas: presuncion de reducibilidad, reduccion conceptual, criterio de parada, economia formal, doble auditoria, clausula de incompletitud y Decalogo.
- `REC-DEUDA-003`: comparar AAU `v1.0.0/fase2` contra `C-001`, `DO-CHECK-001` y `DO-CHECK-MIN-001` antes de automatizacion media.
- `REC-DEUDA-004`: abrir formalizacion matematica separada para GDI-core, `R4` y `Gamma` si el siguiente frente es matematico.
- `REC-DEUDA-005`: evaluar `H-Xi`, `P-107` y Concordancia como hipotesis o expedientes de admision si el siguiente frente es conceptual.

## Dictamen

No hay conflicto que obligue a revertir el workspace vigente. La reconciliacion muestra que el workspace actual es una reconstruccion de gobierno operativo, no una importacion literal del cierre `v1.5`.

