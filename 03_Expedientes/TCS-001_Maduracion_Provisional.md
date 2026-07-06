# TCS-001 - Maduracion provisional

Estatus: avance teorico provisional.

Fecha: 2026-07-05.

ID: `TCS-MAT-PROV-001`.

Expediente padre: `TCS-001`.

Decision: `D-2026-07-05-010`.

## Proposito

Madurar `TCS-001` mas alla del paquete minimo sin convertirlo en Canon, Nivel C, documento oficial ni teoria completa.

## Componentes aceptables

Este paquete agrega tres componentes de prueba:

- `TCS-METRIC-PROV-001`: metrica cualitativa provisional de concordancia local.
- `TCS-EXT-CASE-001`: casos externos no regulados sobre un paquete de software de juguete.
- `TCS-AUTH-CONF-001`: patron de conflicto entre autoridades validas.

## TCS-METRIC-PROV-001

La concordancia local puede evaluarse por siete ejes:

| Eje | Pregunta |
| --- | --- |
| `claim_status` | Las afirmaciones relevantes tienen estatus declarado? |
| `authority_declared` | La autoridad usada esta declarada? |
| `decision_present` | Existe decision habilitante? |
| `permission_scoped` | El permiso tiene alcance acotado? |
| `evidence_traceable` | La evidencia es reconstruible? |
| `automation_bounded` | La automatizacion queda como asistencia, no como autoridad? |
| `debt_registered` | Las deudas quedan registradas? |

Resultado cualitativo:

```text
concordancia_local si los siete ejes pasan.
concordancia_parcial si algun eje queda como deuda no bloqueante.
bloqueo_de_concordancia si falla autoridad, decision, permiso o evidencia.
discordancia_global si un pase local rompe una restriccion mayor.
```

Esta metrica no es cuantitativa universal.

## TCS-EXT-CASE-001

Dominio: paquete de software de juguete, no regulado.

### Caso externo positivo

Un paquete registra:

- afirmacion: version candidata;
- estatus: candidato de lanzamiento;
- autoridad: mantenedor declarado;
- evidencia: pruebas locales;
- decision: aprobar lanzamiento;
- permiso: publicar solo version menor;
- verificacion: paquete publicado con version esperada;
- deuda: revisar compatibilidad futura.

Resultado esperado: `concordancia_local`.

### Caso externo negativo

Un sistema automatico etiqueta una version como lista y publica sin decision del mantenedor.

Fallas:

- `TCS-F4`: recomendacion como decision;
- `TCS-F5`: decision sin permiso suficiente;
- `TCS-F6`: ejecucion sin verificacion si no hay evidencia posterior.

Resultado esperado: `bloqueo_de_concordancia`.

## TCS-AUTH-CONF-001

Patron: conflicto entre autoridades validas.

Dos autoridades validas producen salidas incompatibles:

- autoridad tecnica aprueba una publicacion por pruebas funcionales;
- autoridad de seguridad bloquea por vulnerabilidad abierta.

Regla provisional:

```text
si autoridad_A y autoridad_B son validas
y decision_A contradice decision_B
y no existe procedimiento de precedencia,
entonces el sistema registra TCS-F9 y bloquea o escala.
```

La concordancia no exige que desaparezca el desacuerdo.

La concordancia exige que el desacuerdo conserve estatus, autoridad, evidencia, decision de alcance y mecanismo de resolucion.

## Lectura local/global

Un subsistema puede mostrar `concordancia_local` y aun asi producir `discordancia_global` si:

- ejecuta un cambio incompatible con una autoridad superior;
- oculta deuda a otro subsistema;
- convierte un pase local en permiso general;
- trata evidencia local como autoridad global.

## No cubre

Este paquete no:

- canoniza `Concordance`;
- crea Nivel C;
- modifica documentos oficiales;
- abre dominios clinicos, juridicos, financieros o institucionales;
- define una metrica matematica cerrada;
- resuelve la relacion con dominios regulados;
- convierte TCS en metodologia o plataforma.

## Deudas abiertas

- formalizar una semantica mas precisa para grados de concordancia;
- ampliar casos externos no regulados;
- probar conflictos de autoridades con trazas mas complejas;
- relacionar `TCS-METRIC-PROV-001` con `AO-001` y `C-001`;
- decidir si TCS requiere documento propio futuro o permanece como expediente teorico.
