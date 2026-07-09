# MOC-EXP-GRAPH-001 - Grafo de experiencia local

Estatus: aceptado como estructura local provisional no canonica.

Fecha: 2026-07-09.

Expediente: `MOC-001`.

Decision asociada: `D-2026-07-09-001`.

## Proposito

`MOC-EXP-GRAPH-001` incorpora al Laboratorio una lectura local del grafo de experiencia detectado en el paquete externo `MOC-GEO-METR-001`.

La incorporacion es estructural y defensiva: el grafo sirve para ordenar casos no clinicos y producir trazas auditables, pero no convierte la notacion externa en Canon, Documento 04, Nivel C ni autoridad general del Laboratorio.

## Fuente externa admitida como evidencia auxiliar

Fuente primaria revisada:

```text
C:\Users\IximM\OneDrive\Documentos\v.1.5.2\psicologia\MOC-GEO-METR-001_Metricas_Geometricas_Casos.md
```

Tipo de evidencia:

```text
evidencia_documental_externa_estructural
```

La fuente permite importar casos y una estructura de grafo como evidencia auxiliar. No permite importar autoridad canonica, diagnostica, clinica, psicologica local o normativa.

## Frontera de alcance

Permitido:

- representar una unidad local de experiencia como grafo;
- evaluar casos sinteticos o documentales no clinicos;
- usar notacion `psi` solo como notacion externa importada;
- producir `operator_trace` local;
- usar la salida como evidencia auxiliar para `MOC/AO`;
- registrar deudas cuando falte evidencia, proyeccion o unidad comparable.

Prohibido:

- admitir `H-Xi`;
- canonizar `Xi`, `Xi_psi`, `Phi_psi` o `TrueSelf_psi`;
- usar el grafo para evaluar personas reales;
- abrir uso clinico, patologico, juridico, financiero o regulado;
- convertir una salida local en consejo practico;
- mantener sin cambios Canon, Documento 04, Nivel C y `C-002`;
- cerrar Confluencia global o Equivalencia global;
- autorizar transformaciones materiales.

## Grafo base

El grafo local queda normalizado como:

```text
Omega_psi -> Xi_psi -> Pi5_psi -> Phi_psi -> C_psi -> Omega_psi'
```

Ramas auxiliares:

```text
Phi_psi(Omega_psi) -> A_psi_prism, V_psi_prism
Xi_psi(Omega_psi, Phi_psi) -> pi_psi, T_psi, E_psi, trayectoria_psi
metric_vector -> R_geo
R_geo -> operator_trace
operator_trace -> ao_bridge
```

## Nodos

| Nodo | Lectura local |
| --- | --- |
| `Omega_psi` | unidad local delimitada de experiencia |
| `Xi_psi` | organizador externo importado; no equivale a `H-Xi` ni a operador canonico |
| `Pi5_psi` | proyeccion estructural de cinco componentes importada como antecedente |
| `Phi_psi` | regimen evaluativo local; no autoridad externa |
| `C_psi` | relacion elegible bajo objeto, limite y criterio |
| `Omega_psi_prime` | unidad recompuesta o salida local |
| `T_psi` | condicion temporal de trayectoria |
| `E_psi` | condicion espacial o campo de transitabilidad |
| `trayectoria_psi` | movimiento posible dentro de `E_psi` bajo `T_psi` |
| `A_psi_prism` | base funcional proyectada |
| `V_psi_prism` | altura proyectada de valores o direccion |
| `Omega_phi_prism` | reconstruccion prismatica auxiliar |
| `A_exp` | apertura de expectativa |
| `R_geo` | salida geometrica local |

## Aristas obligatorias

| Arista | Regla |
| --- | --- |
| `Omega_psi -> Xi_psi` | la unidad local se organiza antes de evaluarse |
| `Xi_psi -> Pi5_psi` | la organizacion produce proyeccion estructural |
| `Pi5_psi -> Phi_psi` | la proyeccion se lee bajo regimen evaluativo |
| `Phi_psi -> C_psi` | el regimen produce relacion elegible o deuda |
| `C_psi -> Omega_psi_prime` | la relacion habilita recomposicion o salida |
| `Phi_psi + Omega_psi -> A_psi_prism, V_psi_prism` | lectura prismatica auxiliar |
| `Xi_psi + Omega_psi + Phi_psi -> T_psi, E_psi, trayectoria_psi` | trayectoria local |
| `metric_vector -> R_geo` | reglas geometricas producen salida local |
| `R_geo -> operator_trace` | la salida queda auditada como regla ganadora |

## Invariantes

1. Toda evaluacion exige objeto, limite y criterio.
2. Toda salida positiva exige evidencia trazable.
3. La unidad evaluada es local, no identidad global.
4. `Xi_psi` no se iguala a `TrueSelf_psi`.
5. `Phi_psi` no funciona como autoridad externa del Laboratorio.
6. `A_exp = 0` bloquea `concordancia_local`.
7. Sin `T_psi` o sin `E_psi` no hay trayectoria valida.
8. El grafo no produce consejo practico para personas reales.

## Salidas permitidas

```text
concordancia_local
friccion_relevante
friccion_desorganizante
discordancia_local
reorganizacion_local_habilitada
disolucion_local
fuera_de_alcance
indeterminado_por_falta_de_evidencia
```

## Relacion con el Laboratorio

`MOC-EXP-GRAPH-001` queda subordinado a `MOC-001` como mantenimiento teorico-operativo. Puede producir evidencia local para `AO-001` mediante `operator_trace`, pero no modifica `MOC-EVAL-001` como autoridad general ni sustituye las compuertas AO ya vigentes.

Nota posterior 2026-07-09-002: `D-2026-07-09-002` autoriza contacto documental preparatorio con Canon y Documento 04. El alcance autorizado es preparar propuestas candidatas y matriz de impacto; la edicion oficial directa sigue no autorizada.
