# MOC-GEO-METR-LAB-001 - Metrica geometrica local

Estatus: aceptada como capa local provisional no canonica.

Fecha: 2026-07-09.

Expediente: `MOC-001`.

Decision asociada: `D-2026-07-09-001`.

## Proposito

`MOC-GEO-METR-LAB-001` traduce la metrica geometrica externa de `MOC-GEO-METR-001` a una capa local del Laboratorio.

La metrica es ordinal, cualitativa y acotada a casos no clinicos. No mide identidad, no mide personas y no produce diagnosticos.

## Vector local

El vector validado por el Laboratorio queda:

```text
MOC_GEO_CASE_VECTOR =
<G_scope, G_olc, G_embed, G_T, G_E, G_path,
 G_Aprism, G_Vprism, G_OmegaPhi, G_tau_fit,
 G_adapt, G_unity, G_Aexp, G_Cpsi, G_phi,
 G_evid, R_geo>
```

## Escala

| Valor | Lectura |
| --- | --- |
| `0` | ausente, invalido o bloqueante |
| `1` | parcial, ambiguo o degradado |
| `2` | suficiente para lectura local |

La escala no es una metrica universal ni cuantitativa. Solo ordena condiciones locales de evaluacion.

## Campos

| Campo | Pregunta local |
| --- | --- |
| `G_scope` | el caso es local, no clinico y no regulado |
| `G_olc` | hay objeto, limite y criterio |
| `G_embed` | la proyeccion desde `Pi5_psi` esta declarada |
| `G_T` | el tiempo sostiene secuencia, demora o ritmo |
| `G_E` | el espacio sostiene campo, contorno o disponibilidad |
| `G_path` | hay trayectoria posible bajo `T_psi` y `E_psi` |
| `G_Aprism` | la base proyectada queda organizada |
| `G_Vprism` | la altura de valores o direccion orienta sin rigidez |
| `G_OmegaPhi` | la reconstruccion prismatica es usable |
| `G_tau_fit` | la tension puede organizarse localmente |
| `G_adapt` | se preserva adaptacion local |
| `G_unity` | se preserva unidad minima de experiencia |
| `G_Aexp` | hay apertura de expectativa |
| `G_Cpsi` | se distingue relacion elegible |
| `G_phi` | el regimen evaluativo no se vuelve autoridad externa |
| `G_evid` | la evidencia sostiene el vector |

## Reglas predictivas locales

### G0 - Alcance

Si `G_scope = 0`, entonces:

```text
R_geo = fuera_de_alcance
```

### G1 - Evidencia o proyeccion minima ausente

Si alguno de estos campos es `0`:

```text
G_olc
G_embed
G_phi
G_evid
```

entonces:

```text
R_geo = indeterminado_por_falta_de_evidencia
```

### G2 - Disolucion local

Si alguno de estos minimos geometricos es `0`:

```text
G_T
G_E
G_path
G_Aprism
G_Vprism
G_OmegaPhi
G_unity
```

entonces:

```text
R_geo = disolucion_local
```

La salida no es diagnostico. Solo indica que la unidad local no sostiene una proyeccion prismatica usable.

### G3 - Discordancia local

Si hay unidad y trayectoria, pero existe conflicto de direccion declarado:

```text
G_unity >= 1
G_path >= 1
conflicto_direccion = true
```

entonces:

```text
R_geo = discordancia_local
```

### G4 - Friccion por expectativa fija

Si `G_Aexp = 0`, entonces `R_geo` no puede ser `concordancia_local`.

La salida local es:

```text
friccion_relevante
```

o, si la tension bloquea transitabilidad:

```text
friccion_desorganizante
```

### G5 - Reorganizacion local habilitada

Si:

```text
G_path >= 1
G_OmegaPhi >= 1
G_Cpsi >= 1
G_unity >= 1
G_Aexp >= 1
recomposicion_local = true
```

entonces:

```text
R_geo = reorganizacion_local_habilitada
```

### G6 - Concordancia local

Si:

```text
G_scope = 2
G_olc = 2
G_embed = 2
G_T >= 1
G_E >= 1
G_path >= 1
G_Aprism >= 1
G_Vprism >= 1
G_OmegaPhi >= 1
G_tau_fit >= 1
G_adapt >= 1
G_unity = 2
G_Aexp = 2
G_Cpsi >= 1
G_phi = 2
G_evid >= 1
conflicto_direccion = false
```

entonces:

```text
R_geo = concordancia_local
```

### G7 - Friccion residual

Si el caso no cae por alcance, evidencia, disolucion, discordancia o reorganizacion, pero alguna metrica central queda en `1`, entonces:

```text
R_geo = friccion_relevante
```

## Casos importados

| Caso | Regimen | Salida esperada |
| --- | --- | --- |
| `036A` | continuidad situada | `concordancia_local` |
| `036B` | mandato de pasion | `friccion_relevante` |
| `037A` | eleccion honesta de costo | `discordancia_local` |
| `037B` | entusiasmo como autojustificacion | `discordancia_local` |
| `038A` | pausa con borde | `reorganizacion_local_habilitada` |
| `038B` | certeza total | `disolucion_local` |
| `039A` | reconocimiento como apertura | `reorganizacion_local_habilitada` |
| `039B` | insight como solucion total | `friccion_relevante` |
| `040A` | compromiso abierto | `concordancia_local` |
| `040B` | control de resultado | `friccion_relevante` |
| `041A` | gusto pequeno disponible | `concordancia_local` |
| `041B` | solo cuenta lo intenso | `friccion_relevante` |
| `042A` | recuperar unidad minima | `reorganizacion_local_habilitada` |
| `042B` | explicar identidad total | `fuera_de_alcance` |
| `043A` | siguiente paso transitable | `reorganizacion_local_habilitada` |
| `043B` | solucion total | `friccion_relevante` |

## Falsadores conservados

La capa falla si:

1. trata la formula prismatica como volumen fisico, clinico o literal;
2. mide identidad global en vez de unidad local;
3. produce concordancia sin objeto, limite y criterio;
4. produce concordancia sin proyeccion declarada;
5. usa `E_psi` como emocion en vez de espacio;
6. usa `Eaf_psi` como espacio en vez de afecto situado;
7. trata conducta como sexto vertice;
8. convierte `V_psi_prism` en mandato moral;
9. permite concordancia con `A_exp = 0`;
10. permite trayectoria sin `T_psi` o sin `E_psi`;
11. iguala `Xi_psi` con `TrueSelf_psi`;
12. convierte una salida local en consejo practico para una persona real.

