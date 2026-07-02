# HXI-001 - Criterios de evaluacion

Estatus: criterios provisionales de expediente.

Fecha: 2026-07-02.

## Proposito

Definir compuertas para evaluar si `H-Xi` aporta valor conceptual al tratamiento de relaciones `R` en `PSI-001`.

Estos criterios no admiten `H-Xi`; solo gobiernan la evaluacion `HXI-001`.

## Criterios para evaluacion favorable

La relacion `H-Xi` / `R` puede evaluarse favorablemente si:

- mantiene `H-Xi` como hipotesis externa, no Canon;
- no usa Registro Historico como autoridad directa;
- explica algo no cubierto trivialmente por `DEF-PSI-ORG-001` o `CRIT-PSI-TR-001`;
- distingue claramente entre cambio de contenido, cambio de relaciones y restriccion de transiciones;
- permite describir al menos un ejemplo de reorganizacion sin uso clinico;
- identifica casos donde `Xi` no aplica o no agrega valor;
- formula pruebas de rechazo, pausa o continuidad;
- conserva `transformacion_permitida = false` para cambios materiales.

## Criterios para pausar

Debe pausarse si:

- depende de material historico no materializado;
- necesita resolver `P-107` antes de evaluar utilidad local;
- confunde admision de `H-Xi` con evaluacion de utilidad;
- no distingue distincion de restriccion;
- no produce pruebas aplicables a `EX-PSI-001` a `EX-PSI-005`.

## Criterios para rechazar

Debe rechazarse o bloquearse si:

- intenta canonizar `H-Xi` por utilidad narrativa;
- modifica Canon o documentos oficiales;
- declara `Xi` operador vigente sin expediente de admision;
- usa casos clinicos o personales reales;
- borra la distincion entre `PSI-001` y `HXI-001`;
- convierte fuentes historicas en autoridad positiva vigente.

## Criterios para continuidad abierta

Puede mantenerse abierto si:

- aporta una distincion util pero todavia no formalizada;
- requiere una matriz de pruebas adicional;
- muestra valor en reorganizacion pero no en transformacion simple;
- requiere decidir si `no auditable` se vuelve salida estable de `PSI-001`.

## Resultado esperado

La evaluacion debe producir una decision posterior con uno de estos resultados:

- continuar evaluacion;
- pausar;
- rechazar la relacion local `H-Xi` / `R`;
- recomendar expediente de admision formal de `H-Xi`;
- mantener `H-Xi` como hipotesis externa sin admision.
