# AUT-001 - Criterios de Cierre de Fase Media

Estatus: criterios provisionales aceptables para decision posterior.

Fecha: 2026-07-02.

## Objeto

Definir una compuerta clara para decidir si `AUT-001` puede pasar a cierre tecnico provisional o si debe continuar abierto por refinamiento operativo.

## Niveles de cierre

### Cierre tecnico provisional

Puede considerarse cuando:

- existen herramientas no mutantes para chequeo minimo, chequeo medio, tablero, continuidad, clasificacion de riesgos, resumen ejecutivo y corrida unica;
- existen reportes Markdown y JSON conservados para cada capa principal;
- todos los reportes declaran `transformacion_permitida: false`;
- el resumen ejecutivo distingue estado, riesgos y siguiente accion;
- los riesgos altos tienen tratamiento inicial registrado;
- `AUT-001` conserva una deuda explicita de ejecucion directa local pendiente, sin ocultarla.

### Cierre operativo completo

Requiere adicionalmente:

- ejecucion directa local confirmada de `lab_run.py`;
- evidencia conservada de la corrida local;
- decision posterior sobre los riesgos activos altos;
- decision explicita de cierre de `AUT-001`.

## Estado actual contra criterio

- Herramientas no mutantes: cumplido provisionalmente.
- Reportes conservados: cumplido provisionalmente.
- Transformacion permitida: `false` en reportes principales.
- Resumen ejecutivo: cumplido provisionalmente por `DO-LAB-SUMMARY-001`.
- Riesgos altos: pendientes de tratamiento formal en este mismo paquete.
- Ejecucion local directa: pendiente por decision operativa del usuario.

## Decision que habilita

Estos criterios no cierran `AUT-001`. Solo habilitan una decision posterior: cerrar tecnicamente de forma provisional, continuar con refinamiento, o pasar a otro frente conservando `AUT-001` abierto.
