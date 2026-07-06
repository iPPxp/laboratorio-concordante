# HXI-001 - Evaluacion de compuerta de admision formal

Estatus: evaluacion provisional de compuerta aplicada.

Fecha: 2026-07-05.

Codigo: `HXI-GATE-001`.

Compuerta aplicada: `HXI-001_Criterios_Admision_Formal_H-Xi.md`.

## Pregunta

Determinar que resultado corresponde a `H-Xi` en el estado actual de `HXI-001`, despues de la reapertura operativa `HXI-REOPEN-001`.

## Resultado corto

Resultado de compuerta: `mantener_Xi_eval`.

`H-Xi` permanece como hipotesis externa no admitida.

`Xi_eval` se conserva como herramienta local de expediente, con las salidas `redundante`, `util_acotado`, `limitado`, `no_comparable` y `bloqueado`.

## Evidencia usada

- `HXI-001_Dictamen_Utilidad_Local_Xi.md`: reconoce utilidad local acotada de `Xi`, pero no recomienda admision formal todavia.
- `HXI-001_Notacion_Minima_Xi-R.md`: fija `Xi_eval(R0, R1)` como notacion local no canonica.
- `HXI-001_Reporte_Consistencia_Notacion_Xi-R.md`: muestra consistencia en `HXI-R-001` a `HXI-R-005`.
- `HXI-001_Criterios_Admision_Formal_H-Xi.md`: separa utilidad local de admision formal.
- `HXI-001_Reapertura_Operativa.md`: habilita aplicar la compuerta sin admision automatica.

## Aplicacion de criterios minimos

| Criterio | Lectura | Resultado |
| --- | --- | --- |
| Trazabilidad local completa | Existe fuente historica materializada como `SRC-020`; no se usa Registro Historico como autoridad directa. | cumple |
| Formulacion local estable | Existe formulacion local suficiente para usar `Xi_eval`; no existe aun formulacion formal independiente de `H-Xi` como operador general. | cumple para herramienta local; insuficiente para admision |
| Distincion `H-Xi` / `Xi` / `Xi_eval` | La evidencia distingue hipotesis externa, operador propuesto y evaluador local. | cumple |
| Utilidad no trivial | Hay utilidad local en reorganizacion relacional estable (`HXI-R-002`). | cumple acotadamente |
| Matriz `HXI-R` | `Xi_eval` pasa `HXI-R-001` a `HXI-R-005`. | cumple |
| Controles reales | Se conservan `redundante`, `limitado`, `no_comparable` y `bloqueado`. | cumple |
| Caso positivo no universal | `util_acotado` no se convierte en regla general. | cumple |
| Sin efectos automaticos | No modifica Canon, documentos oficiales ni `PSI-001`. | cumple |
| Sin uso clinico | El caso no declara diagnostico, tratamiento ni consejo profesional. | cumple |
| Tipo de admision | El tipo defensible no es admision de `H-Xi`, sino conservacion de herramienta local. | define `mantener_Xi_eval` |

## Criterios bloqueantes

No se activan bloqueos si el resultado se limita a `mantener_Xi_eval`.

Los bloqueos si se activarian para cualquier intento de:

- canonizar `H-Xi` por utilidad narrativa;
- declarar `Xi` operador vigente;
- transformar `PSI-001` desde `Xi`;
- resolver `P-107` por implicacion indirecta;
- borrar controles negativos o de limite;
- usar casos clinicos, personales reales o no auditables;
- promover `H-Xi` sin expediente posterior.

## Pruebas requeridas

| Prueba requerida | Estado |
| --- | --- |
| Reporte de consistencia de `Xi_eval` | cumplido por `HXI-001_Reporte_Consistencia_Notacion_Xi-R.md` |
| Auditoria del reporte | cumplida por `HXI-001_Auditoria_Reporte_Consistencia.md` |
| Decision de estatus del reporte | cumplida por `HXI-001_Decision_Estatus_Reporte_Consistencia.md` |
| Definicion del tipo de admision pretendida | definida aqui como `mantener_Xi_eval` |
| Auditoria contra `M-000` y `M-001` | no requerida porque no se pretende afectar niveles superiores |

## Por que no `admitir_solo_expediente`

La evidencia actual alcanza para conservar una herramienta local consistente, pero no para admitir `H-Xi` como hipotesis de expediente.

Las razones son:

- la utilidad demostrada sigue siendo local y acotada;
- el dictamen previo recomienda no abrir admision formal todavia;
- faltan pruebas en dominios independientes;
- `P-107` permanece abierto;
- no hay necesidad de convertir la herramienta `Xi_eval` en admision de la hipotesis fuerte `H-Xi`.

## Deudas abiertas

- Formular condiciones adicionales si alguna vez se quiere evaluar `admitir_solo_expediente`.
- Probar dominios independientes antes de cualquier promocion.
- Mantener `P-107` separado y no resuelto.
- Abrir decision puente si alguna dependencia psicologica sustantiva exige material del proyecto independiente.
- Decidir si `HXI-001` queda abierto en mantenimiento local, pausado o cerrado tras conservar `Xi_eval`.

## Resultado

La compuerta queda aplicada con resultado `mantener_Xi_eval`.

`H-Xi` no se admite.

`Xi` no se canoniza ni se declara operador vigente.

`Xi_eval` queda conservado como herramienta local de `HXI-001` para lecturas acotadas de relaciones `R`.
