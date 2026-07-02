# HB-001 - Deuda viva de H-B

Estatus: deuda conceptual viva de alcance.

ID: `DEUDA-HB-001`.

Relacion: `H-B.6` y `H-B.7`.

## Proposito

Registrar la deuda viva asociada a las hipotesis activas `H-B.6` y `H-B.7`.

Este archivo no reabre `B-001`, no descongela `B-001.5` y no promueve ninguna hipotesis a Canon, documento oficial o Nivel C.

Su funcion es impedir que `H-B.6` y `H-B.7` queden como etiquetas activas sin superficie local de trabajo.

## Fuentes locales

- `03_Expedientes/B-001.md`
- `03_Expedientes/B-001.5.md`
- `03_Expedientes/B-001.5_Decision_Clasificacion.md`
- `05_Estado_Proyecto/ESTADO_ACTUAL.md`
- `05_Estado_Proyecto/DECISION_Siguiente_Frente_Activo_P-PI.md`
- `03_Expedientes/RH-001.md`
- `03_Expedientes/HB-001_Ficha_Alcance_H-B.6.md`
- `03_Expedientes/HB-001_Ficha_Alcance_H-B.7.md`
- `03_Expedientes/HB-001_Decision_Fichas_Alcance_H-B.md`

## Estado local actual

| Elemento | Estado vigente | Lectura operativa |
| --- | --- | --- |
| `B-001` | cerrado | Nivel B queda estabilizado como referencia, no como frente abierto |
| `B-001.5` | congelado | traza sin material local suficiente para trabajo sustantivo |
| `H-B.6` | hipotesis activa con ficha de alcance minimo | deuda viva sustantiva |
| `H-B.7` | hipotesis activa con ficha de alcance minimo | deuda viva sustantiva |

## Deuda viva

La deuda no es demostrar, refutar ni desarrollar todavia `H-B.6` o `H-B.7`.

La deuda viva es precisar:

- que afirma cada hipotesis;
- de que fuente local procede;
- si pertenece todavia a Nivel B;
- si fue absorbida por otro expediente;
- si debe quedar congelada, cerrada, mantenida como hipotesis activa o convertida en expediente propio.

## Regla de lectura

Despues de `D-HB-ALC-001`, `H-B.6` y `H-B.7` pueden citarse solo como:

```text
hipotesis activas de Nivel B con alcance local minimo; contenido sustantivo no materializado
```

No pueden usarse como:

- fundamento para modificar Canon;
- fundamento para modificar documentos oficiales;
- puente directo hacia Nivel C;
- premisa para `REPORT_LAYER`;
- premisa para R4 formal o `Gamma`;
- cierre de problemas abiertos.

## Condiciones para resolver la deuda

La deuda puede resolverse por cualquiera de estas rutas:

| Ruta | Resultado | Requisito minimo |
| --- | --- | --- |
| Ficha de alcance | `H-B.6` y `H-B.7` quedan definidos localmente | fuente local y estatus declarado |
| Congelamiento | las hipotesis quedan pausadas como etiquetas historicas | decision explicita |
| Absorcion | pasan a otro expediente ya abierto | mapa de correspondencia y decision |
| Cierre | dejan de ser hipotesis activas | auditoria o decision de cierre |
| Apertura de expediente | se crea frente propio `HB-*` | motivo, fuentes y alcance |

## Alcance permitido ahora

Se permite:

- registrar esta deuda como deuda viva de alcance;
- buscar material local sobre `H-B.6` y `H-B.7`;
- preparar una ficha separada si aparece contenido suficiente;
- mantener `B-001` cerrado y `B-001.5` congelado.

## Alcance no permitido

No se permite:

- inferir contenido desde el nombre de las hipotesis;
- reabrir `B-001` por conveniencia;
- absorber `B-001.5` sin decision;
- usar Registro Historico como autoridad directa;
- mover las hipotesis a Nivel C sin expediente, auditoria y decision.

## Veredicto

`H-B.6` y `H-B.7` quedan registradas como deuda viva de alcance.

El frente Nivel B permanece sin reapertura.

## Resultado posterior

Las fichas de alcance fueron creadas y aceptadas por `D-HB-ALC-001`.

El siguiente paso ya no es precisar alcance minimo. Es buscar fuente local sustantiva o decidir explicitamente congelamiento, absorcion, cierre o apertura de expediente propio.
