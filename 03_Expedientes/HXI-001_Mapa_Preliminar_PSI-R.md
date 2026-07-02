# HXI-001 - Mapa preliminar H-Xi / relaciones R

Estatus: mapa preliminar operativo de expediente.

Fecha: 2026-07-02.

## Proposito

Explorar de forma preliminar si `H-Xi` puede mapearse a los cambios de relaciones `R` definidos por `CRIT-PSI-TR-001`.

Este mapa no admite `H-Xi` y no declara `Xi` como operador vigente.

## Traduccion provisional

En `PSI-001`, `R` nombra relaciones relevantes entre contenidos, distinciones, relevancias, afectos, memoria, atencion, narrativa y disposiciones de accion.

En `H-Xi`, la formulacion historica propone dos operaciones acopladas:

- `distincion`: separar alternativas posibles dentro de un espacio considerado;
- `restriccion`: hacer que algunas transiciones queden permitidas, privilegiadas, bloqueadas o no disponibles.

Traduccion candidata:

```text
R0 = relaciones relevantes en E0
R1 = relaciones relevantes en E1
Dist(R) = alternativas relacionales distinguibles
Res(R0 -> R1) = restricciones sobre transiciones entre relaciones
Xi(R0, R1) = acoplamiento candidato entre Dist(R) y Res(R0 -> R1)
```

## Lectura por ejemplos de PSI-001

### EX-PSI-001 - Transformacion por cambio de contenido

Relevancia de `H-Xi`: baja.

Razon: cambia el contenido, pero `R` permanece estable. `Xi` podria distinguir alternativas de contenido, pero no parece necesario para explicar el caso.

### EX-PSI-002 - Reorganizacion por cambio relacional estable

Relevancia de `H-Xi`: alta como hipotesis de evaluacion.

Razon: `R` cambia de hito-recuerdo-ruta a posicion-regla-ruta. La idea distincion/restriccion podria representar alternativas relacionales y transiciones permitidas entre modos de orientacion.

### EX-PSI-003 - Desorganizacion por perdida de estabilidad relacional

Relevancia de `H-Xi`: media.

Razon: hay fragmentos de `R`, pero no nueva estabilidad. `Xi` podria ayudar a describir restricciones incompatibles o transiciones no estabilizadas, aunque tambien podria no aportar nada mas que vocabulario extra.

### EX-PSI-004 - Disolucion por perdida de unidad minima

Relevancia de `H-Xi`: baja o limite.

Razon: si no hay continuidad minima de unidad, `R0 -> R1` deja de ser comparable. `Xi` podria marcar el limite, pero no explicar la continuidad perdida.

### EX-PSI-005 - No auditable

Relevancia de `H-Xi`: nula dentro de `PSI-001`.

Razon: el caso sale del alcance no clinico. Ningun operador puede usarse para convertirlo en evaluacion valida.

## Dictamen preliminar

La relacion `H-Xi` / `R` merece evaluacion separada porque parece potencialmente util en casos de reorganizacion relacional, especialmente `EX-PSI-002`.

La utilidad no esta demostrada. Tambien podria resultar redundante, insuficiente o demasiado fuerte para `PSI-001`.

## Pruebas necesarias

- Probar si `Xi` distingue transformacion simple de reorganizacion sin agregar ruido.
- Probar si `Xi` explica desorganizacion como restriccion incompatible o si solo renombra el problema.
- Probar si `Xi` reconoce el limite de disolucion sin forzar continuidad inexistente.
- Probar si la formalizacion puede rechazar el caso `no auditable`.
- Decidir si `Xi` es necesario, redundante o prematuro para `PSI-001`.

## Resultado

Mapa preliminar operativo aceptado por `HXI-001_Decision_Estatus_Mapa_Preliminar.md`; favorable para continuar evaluacion mediante pruebas, no para admitir `H-Xi`.
