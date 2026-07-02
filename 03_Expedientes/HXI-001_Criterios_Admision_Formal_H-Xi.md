# HXI-001 - Criterios de admision formal de H-Xi

Estatus: criterios provisionales de expediente.

Fecha: 2026-07-02.

## Proposito

Definir una compuerta separada para evaluar en el futuro si `H-Xi` podria ser admitida formalmente desde `HXI-001`.

Estos criterios no admiten `H-Xi`. Solo indican que tendria que cumplirse antes de una decision formal de admision.

## Principio de separacion

Utilidad local no equivale a admision formal.

`HXI-001_Dictamen_Utilidad_Local_Xi.md` reconoce utilidad acotada de `Xi`, pero esa utilidad solo habilita esta compuerta. No decide la admision.

## Criterios minimos para considerar admision

`H-Xi` solo podria considerarse para admision formal si cumple todos estos criterios:

1. Mantiene trazabilidad local completa desde fuente historica materializada, sin usar Registro Historico como autoridad directa.
2. Tiene formulacion local estable que no dependa de ambiguedades conversacionales.
3. Distingue claramente `H-Xi`, `Xi`, `Xi_eval` y cualquier futuro operador.
4. Muestra utilidad no trivial mas alla de `DEF-PSI-ORG-001` y `CRIT-PSI-TR-001`.
5. Supera la matriz `HXI-R` sin borrar salidas negativas o de limite.
6. Conserva salidas `redundante`, `limitado`, `no_comparable` y `bloqueado` como controles reales.
7. No convierte un caso positivo de reorganizacion en regla universal.
8. No modifica Canon, documentos oficiales ni `PSI-001` como efecto automatico.
9. No declara uso clinico, diagnostico, tratamiento ni consejo profesional.
10. Define que tipo de admision se busca: hipotesis admitida de expediente, herramienta conceptual local, documento candidato o futura promocion formal.

## Criterios bloqueantes

La admision formal debe bloquearse si:

- se intenta canonizar `H-Xi` por utilidad narrativa;
- se declara `Xi` operador vigente sin expediente posterior;
- se usa material historico no procesado como autoridad directa;
- se ignoran controles negativos de la matriz;
- se transforma `PSI-001` desde `Xi` sin decision separada;
- se usa un caso clinico, personal real o no auditable;
- se pretende resolver `P-107` por implicacion indirecta;
- se borran deudas de formalizacion por decision de conveniencia.

## Pruebas requeridas antes de admision

Antes de una decision de admision formal debe existir:

- reporte de consistencia de `HXI-001_Notacion_Minima_Xi-R.md` sobre `HXI-R-001` a `HXI-R-005` cumplido por `HXI-001_Reporte_Consistencia_Notacion_Xi-R.md`;
- auditoria del reporte de consistencia;
- decision de estatus del reporte;
- definicion del tipo de admision pretendida;
- auditoria especifica contra `M-000` y `M-001` si la admision pretende afectar niveles superiores.

## Resultados posibles al aplicar estos criterios

Una evaluacion posterior puede concluir:

- `no_admitir`: `H-Xi` queda como hipotesis externa;
- `pausar_admision`: faltan pruebas o formulacion estable;
- `admitir_solo_expediente`: `H-Xi` queda admitida solo como hipotesis de expediente;
- `mantener_Xi_eval`: solo se conserva la herramienta local `Xi_eval`;
- `abrir_promocion_separada`: se abre otro expediente para posible promocion documental o formal.

## Resultado

Criterios provisionales para admision formal posterior de `H-Xi`, aceptados por `HXI-001_Decision_Estatus_Criterios_Admision_Formal.md`.

No autorizan admision, canonizacion, operador vigente, modificacion documental, cierre de `PSI-001`, uso clinico ni transformaciones materiales.
