# MOC-001 - Semantica provisional

ID: `MOC-SEM-PROV-001`.

Ruta: `MOC-ROUTE-008`.

Fecha: 2026-07-06.

Estatus: propuesta semantica provisional, no canonica.

Decision asociada: `D-2026-07-06-004`.

## Proposito

Proponer una semantica operativa local para el Modelo Operativo de Concordancia.

La semantica convierte formulas conceptuales en una cadena de operadores con entradas, prioridades, salida unica y deuda conservada. No convierte el MOC en Canon, no crea Nivel C, no autoriza piloto empirico real y no modifica `Documento 04`.

## Idea central

El MOC no interpreta una relacion como verdad directa. Interpreta una relacion como un caso evaluable bajo restricciones.

Forma conceptual:

```text
V + D + E + contexto -> conducta
```

Forma operativa provisional:

```text
caso_normalizado -> Xi_eval -> TCS -> estado_MOC -> traza -> respuesta
```

La salida no es una conducta humana ni una verdad canonica. Es un estado local de concordancia, con regla ganadora, deuda y frontera de uso.

## Objetos semanticos

| Objeto | Definicion local | Uso |
| --- | --- | --- |
| `C` | caso sintetico normalizado | unidad minima de evaluacion |
| `R0` | configuracion relacional inicial | punto de partida |
| `R1` | configuracion relacional candidata | punto de comparacion |
| `Dist(R0,R1)` | diferencia declarada | testigo de cambio |
| `Res(R0 -> R1)` | restriccion o trayectoria declarada | limite de paso |
| `A` | alcance | dominio permitido |
| `E` | evidencia | testigos auditables |
| `K` | restricciones | prohibiciones, deuda, permisos |
| `X` | salida `Xi_eval` | lectura relacional |
| `T` | lectura TCS | lectura de concordancia minima |
| `S` | estado MOC | salida ordinal cualitativa |
| `Q` | traza operativa | regla ganadora y deuda |
| `Y` | respuesta de evaluador | clasificacion reportable |

## Dominio permitido

La semantica solo opera sobre:

- casos sinteticos no clinicos;
- datos ficticios o abstractos;
- tareas de clasificacion documental;
- salidas ordinales/cualitativas;
- reportes sin datos personales.

## Dominio prohibido

La semantica no opera sobre:

- personas reales;
- datos personales;
- salud mental, diagnostico, tratamiento, patologia o psicologia clinica;
- dominios juridicos, financieros, laborales, educativos reales o institucionales regulados;
- decisiones materiales o transformaciones de repositorio;
- Canon, Nivel C o `Documento 04`.

## Relacion semantica principal

La relacion semantica local es:

```text
Eval_MOC(C) = <X, T, S, Q, Y, deuda>
```

Donde:

- `X = OP_MOC_XI(C)`;
- `T = OP_MOC_TCS(C)`;
- `S = OP_MOC_STATE(X, T, flags)`;
- `Q = OP_MOC_TRACE(X, T, S)`;
- `Y = OP_MOC_RESPONSE(C, S, Q)`.

La salida `S` queda dominada por reglas de seguridad. Si falta alcance, evidencia, autoridad minima o aparece dominio prohibido, no se promedia con evidencia positiva.

## Principio de prioridad

La prioridad semantica local es:

```text
seguridad > comparabilidad > conflicto_global > friccion_local > concordancia
```

Esto implica:

- un bloqueo domina sobre una reorganizacion util;
- una perdida de unidad minima detiene la comparacion;
- una discordancia global conserva el problema abierto;
- una friccion local exige deuda o revision;
- una concordancia local solo vale dentro del alcance y con testigo.

## Principio de no mutacion

Ningun operador MOC produce cambio material.

Toda salida es de lectura, clasificacion o reporte. Incluso una salida `concordancia_local` no autoriza modificacion de documentos, Canon, Nivel C, `Documento 04`, repositorio o agenda empirica.

## Principio de deuda visible

La deuda no se borra por alcanzar una salida positiva.

Toda respuesta debe conservar:

- regla ganadora;
- evidencia usada;
- estado MOC;
- deuda asociada;
- frontera de uso;
- condicion que impediria promocion.

## Resultado provisional

`MOC-SEM-PROV-001` queda como propuesta local para ordenar los operadores de `MOC-001`.

No valida empiricamente el MOC, no ejecuta piloto, no reemplaza evaluadores, no admite `H-Xi`, no canoniza `Xi` y no cierra Confluencia global ni Equivalencia global de proyecciones.
