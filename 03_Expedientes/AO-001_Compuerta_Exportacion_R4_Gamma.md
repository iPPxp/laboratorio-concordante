# AO-001 - Compuerta de exportacion R4/Gamma

Estatus: compuerta provisional aplicada.

Fecha: 2026-07-05.

ID: `AO-R4-GAMMA-EXPORT-GATE-001`.

Expediente padre: `AO-001`.

Artefactos evaluados:

- `R4-FORMAL-AUD-001`;
- `GAMMA-FORMAL-AUD-001`;
- `AO-R4-GAMMA-USE-001`;
- `GAMMA-EXT-AO-001`;
- `AO-EXT-CONF-EXEC-001`.

## Proposito

Evaluar si existe evidencia local suficiente para exportar de forma general `R4-FORMAL-AUD-001` y `GAMMA-FORMAL-AUD-001` fuera de `AUD-001`.

## Resultado

Resultado de compuerta: `exportacion_general_bloqueada`.

Resultado operativo permitido: `perfil_restringido_interoperable`.

## Criterios de compuerta

| Criterio | Resultado | Lectura |
| --- | --- | --- |
| Formalizacion local existente | pasa | `R4-FORMAL-AUD-001` y `GAMMA-FORMAL-AUD-001` existen dentro de `AUD-001`. |
| Uso local controlado fuera de `AUD-001` | pasa | `AO-R4-GAMMA-USE-001` permite referencia, prueba local y puente de problema. |
| Prueba positiva externa local de Gamma | pasa | `GAMMA-EXT-AO-001` existe dentro de `AO-001`. |
| Pruebas externas no reguladas de Confluencia | pasa parcial | `EXT-CONF-001` y `EXT-CONF-002` apoyan `AO-001`, no exportacion general. |
| Dominio global definido | falla | No hay dominio general de aplicacion fuera de `AUD-001`/`AO-001`. |
| Semantica comun independiente del expediente | falla | La autoridad sigue ligada a expedientes locales. |
| Prueba global fuera de trazas/reportes locales | falla | No existe validacion general. |
| Permiso de transformacion general | falla | Esta explicitamente prohibido. |
| Relacion con Confluencia y Equivalencia global | falla | Ambas permanecen abiertas. |

## Perfil restringido interoperable

Hasta nueva decision, R4/Gamma pueden exponerse fuera de `AUD-001` solo como perfil restringido:

```text
RG_Profile = (
  fuente_local,
  contexto,
  testigo,
  estatus,
  invariantes,
  restricciones,
  deudas,
  salida_segura
)
```

Condiciones:

1. `fuente_local` debe citar el expediente de origen.
2. `contexto` debe declarar el dominio acotado.
3. `testigo` debe ser materializable o declararse como deuda.
4. `estatus` solo puede ser local, provisional o de expediente.
5. `invariantes` deben estar trazados.
6. `restricciones` deben incluir no promocion automatica.
7. `deudas` deben conservar Confluencia y Equivalencia abiertas si aplican.
8. `salida_segura` no puede habilitar transformacion.

## Usos permitidos

- referencia formal local;
- prueba local controlada;
- puente de problema;
- perfil restringido interoperable.

## Usos bloqueados

- exportacion general;
- Canon;
- Nivel C;
- teorema global;
- permiso de transformacion;
- cierre de Confluencia global;
- cierre de Equivalencia global;
- sustitucion de auditoria por analogia.

## Deudas

- definir un dominio formal externo si se quiere reintentar exportacion;
- crear casos fuera de `AUD-001` y `AO-001` que no dependan del lenguaje interno;
- probar relacion con Confluencia y Equivalencia global;
- decidir si el perfil restringido pertenece a Documento 04 o a una especificacion posterior;
- conservar `R4-FORMAL-AUD-001` y `GAMMA-FORMAL-AUD-001` como locales hasta nueva compuerta.
