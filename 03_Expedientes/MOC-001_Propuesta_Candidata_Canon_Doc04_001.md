# MOC-001 - Propuesta candidata Canon/Documento 04

Estatus: propuesta candidata aplicada parcialmente por decision posterior.

Fecha: 2026-07-09.

Expediente: `MOC-001`.

Ruta: `MOC-CANON-DOC04-IMPACT-001`.

Base: `MOC-001_Matriz_Impacto_Canon_Doc04_001.md`.

## Dictamen de incorporacion

Esta propuesta fue preparada sin editar Canon ni Documento 04. Posteriormente, `D-2026-07-09-005` aplico oficialmente la parte acotada para `M-001` y Documento 04. `M-000` se conserva sin cambio textual.

## Propuesta candidata para `M-000`

No se propone cambio textual en `M-000` por ahora.

Razon:

- `M-000.1` ya bloquea modificacion de nivel superior desde expediente.
- `M-000.2` ya exige estatus.
- `M-000.3` ya bloquea promocion automatica.
- `M-000.4` ya exige trazabilidad.
- `M-000.6` ya cubre deuda conceptual.

Accion candidata:

```text
Sin cambio textual en M-000. Usar M-000 como limite rector de la ruta.
```

## Propuesta candidata para `M-001`

Ubicacion sugerida:

```text
01_Canon/M-001_Auditoria_Arquitectonica.md
Despues de "Salida esperada".
```

Texto candidato:

```text
## Matriz de superficies para intervenciones de nivel sensible

Si una auditoria evalua una intervencion que podria afectar Canon,
documentos oficiales, Nivel C o un expediente con autoridad vigente,
la salida debe separar:

- lo que se propone para Canon;
- lo que se propone para documento oficial;
- lo que queda solo en expediente;
- lo que queda prohibido;
- la deuda conceptual que impide incorporacion.

Una propuesta candidata no equivale a incorporacion oficial ni a permiso
material. Toda incorporacion a Canon o documento oficial requiere decision
posterior separada.
```

Justificacion:

No autoriza edicion oficial: `M-001` ya exige indicar impacto sobre documentos, expedientes, estado o Canon, y esta propuesta solo vuelve mas precisa la salida cuando una auditoria registra contacto preparatorio con superficies de nivel superior.

## Propuesta candidata para Documento 04

Ubicacion sugerida:

```text
02_Documentos/04_Algebra_Operacional.md
Dentro de "Formalizacion operacional amplia v0",
despues de "Proyecciones operacionales" o como subseccion posterior.
```

Texto candidato:

```text
### Entrada auxiliar por traza local de grafo

Una estructura local de grafo aceptada por expediente puede entrar a
Algebra Operacional solo como evidencia auxiliar si produce una traza de
operador.

Forma minima:

operator_trace_graph =
  <operator_id, case_id, metric_vector, regla_ganadora,
   salida_emitida, salida_segura, evidencia, bloqueos, deuda>

Uso permitido:

- alimentar `Pi_op` como evidencia local de regla ganadora;
- comparar salidas bajo testigo declarado;
- registrar deuda, bloqueo o candidata provisional;
- conservar separacion de niveles.

Uso prohibido:

- crear permiso de transformacion;
- cerrar equivalencia o confluencia global;
- promover notacion local a Canon;
- convertir una salida geometrica en diagnostico, consejo practico
  o autoridad externa.

Si falta contexto, testigo, evidencia, estatus o permiso material,
la salida correcta es `B`, `registrar_deuda`,
`registrar_problema_abierto` o `emitir_candidata_provisional`,
no `ejecutar_cambio_acotado`.
```

Justificacion:

Documento 04 ya reconoce `operator_trace` y `Pi_op`. La propuesta solo define una entrada auxiliar restringida para grafos locales, sin importar terminologia `psi` al documento oficial.

## Contenido que no debe incorporarse

No debe incorporarse a Canon ni Documento 04:

- `Omega_psi`, `Xi_psi`, `Pi5_psi`, `Phi_psi`, `C_psi`, `Omega_psi_prime` como vocabulario oficial;
- `TrueSelf_psi`;
- lectura clinica, patologica, juridica, financiera o institucional;
- casos 036-043 como muestra empirica real;
- metrica 0/1/2 como metrica cuantitativa universal;
- cualquier autorizacion de modo mutante.

## Condicion para decision futura

Para incorporar cualquier parte adicional de esta propuesta se requiere una decision posterior separada que:

- cite esta propuesta candidata;
- declare superficie exacta;
- incluya auditoria de `M-001`;
- conserve `M-000`;
- confirme que no se habilitan dominios prohibidos;
- ejecute verificacion no mutante posterior.

Nota posterior 2026-07-09-005: la incorporacion acotada ya ejecutada queda limitada a `M-001` y Documento 04. No se incorporan `Omega_psi`, `Xi_psi`, `Pi5_psi`, `Phi_psi`, `C_psi`, `TrueSelf_psi`, casos como muestra empirica real ni autorizacion de modo mutante.
