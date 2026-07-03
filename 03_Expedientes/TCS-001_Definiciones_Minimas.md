# TCS-001 - Definiciones minimas

Estatus: definiciones provisionales de expediente.

Fecha: 2026-07-03.

ID: `TCS-DEF-MIN-001`.

Expediente padre: `TCS-001`.

## Proposito

Fijar un vocabulario minimo para avanzar `TCS-001` sin canonizar la teoria.

Estas definiciones sirven para pruebas y critica, no para modificar Canon ni documentos oficiales.

## Definiciones

### Sistema

Un `System` es un conjunto de componentes, reglas, procesos y registros que produce o transforma afirmaciones bajo algun regimen de autoridad.

### Afirmacion

Un `Claim` es cualquier contenido que el sistema trata como descripcion, estado, senal, reporte, permiso, recomendacion, compromiso o decision propuesta.

### Estatus

Un `Status` es la clasificacion explicita de una afirmacion respecto de su uso permitido.

Estatus minimos:

- `historico`;
- `provisional`;
- `validado`;
- `rechazado`;
- `operativo`;
- `canonico`;
- `indeterminado`.

### Autoridad

`Authority` es la capacidad reconocida por el sistema para asignar estatus, emitir decision o habilitar permiso.

La autoridad puede ser formal, tecnica, epistemica, procedimental, institucional, legal o delegada.

### Permiso

`Permission` es el alcance de accion que una autoridad habilita.

Permisos minimos:

- lectura;
- recomendacion;
- decision;
- ejecucion;
- modificacion;
- cierre;
- promocion;
- reversion.

### Decision

Una `Decision` es una afirmacion emitida por autoridad reconocida que cambia el estatus operativo de otra afirmacion, artefacto o proceso.

### Evidencia

`Evidence` es el conjunto de fuentes, trazas o testigos que permite reconstruir por que una afirmacion recibio un estatus.

### Concordancia

`Concordance` es la preservacion auditable de relaciones coherentes entre afirmaciones, estatus, autoridad, permisos, decisiones, responsabilidades y procesos mientras un sistema cambia.

## Condicion minima

Un sistema tiene concordancia local respecto de una operacion si:

1. las afirmaciones relevantes tienen estatus;
2. la autoridad usada esta declarada;
3. la decision habilitante existe;
4. el permiso tiene alcance acotado;
5. la evidencia es reconstruible;
6. la salida no aumenta autoridad por repeticion;
7. las deudas quedan registradas.

## No cubre

No define una teoria general completa.

No convierte `Concordance` en Canon.

No crea Nivel C.

No modifica `TCS-001_Teoria_Concordante_de_Sistemas.md`.

No resuelve dominios clinicos, juridicos ni institucionales externos.

## Deudas

- definir medicion o grados de concordancia;
- modelar conflicto entre autoridades validas;
- distinguir concordancia local y global;
- probar casos externos fuera del Laboratorio.
