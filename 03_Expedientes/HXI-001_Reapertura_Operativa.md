# HXI-001 - Reapertura operativa controlada

Estatus: reapertura operativa de expediente.

Fecha: 2026-07-05.

Codigo: `HXI-REOPEN-001`.

## Proposito

Reabrir `HXI-001` como frente activo inmediato de evaluacion, despues de la pausa operativa registrada en `HXI-001_Decision_Pausa_Operativa.md`.

La reapertura no admite `H-Xi`, no canoniza `Xi` y no declara `Xi` como operador vigente.

## Base aceptada

La reapertura se apoya solo en evidencia local ya aceptada dentro de `HXI-001`:

- `HXI-001_Dictamen_Utilidad_Local_Xi.md`: utilidad local acotada de `Xi`.
- `HXI-001_Notacion_Minima_Xi-R.md`: notacion local `Xi_eval(R0, R1)`.
- `HXI-001_Criterios_Admision_Formal_H-Xi.md`: compuerta provisional de admision formal posterior.
- `HXI-001_Reporte_Consistencia_Notacion_Xi-R.md`: cinco salidas consistentes para `HXI-R-001` a `HXI-R-005`.
- `HXI-001_Decision_Pausa_Operativa.md`: pausa anterior que ahora queda superada solo para continuar evaluacion.

## Ruta reabierta

`HXI-001` queda reabierto para aplicar la compuerta provisional de admision formal posterior.

La pregunta operativa inmediata es:

```text
Que resultado de la compuerta corresponde a H-Xi en el estado actual?
```

Los resultados posibles siguen siendo los fijados por `HXI-001_Criterios_Admision_Formal_H-Xi.md`:

- `no_admitir`;
- `pausar_admision`;
- `admitir_solo_expediente`;
- `mantener_Xi_eval`;
- `abrir_promocion_separada`.

## Alcance

La reapertura permite:

- tratar `HXI-001` como frente activo inmediato;
- usar `Xi_eval` solo como herramienta local de expediente;
- aplicar los criterios de admision formal posterior a la evidencia ya aceptada;
- decidir si la utilidad local de `Xi` basta para algun estatus de expediente;
- registrar deudas o bloqueos si la evidencia actual no alcanza.

## Dependencia PSI

`PSI-001` permanece transferido al proyecto independiente `Psicologia Concordante` y sin copia local de traspaso dentro del Laboratorio.

Las referencias a ejemplos, criterios o matrices PSI usadas historicamente por `HXI-001` funcionan como antecedentes ya absorbidos por los artefactos HXI aceptados. No reabren `PSI-001` ni restauran archivos eliminados.

Si una evaluacion posterior necesita contenido psicologico sustantivo nuevo, debe abrirse una decision puente hacia el proyecto independiente.

## No cubre

Esta reapertura no cubre:

- admision de `H-Xi`;
- canonizacion de `Xi`;
- declaracion de `Xi` como operador vigente;
- modificacion de Canon o documentos oficiales;
- reapertura de `PSI-001` dentro del Laboratorio;
- uso clinico, diagnostico, tratamiento o consejo profesional;
- resolucion de `P-107`;
- reconstruccion del sistema desde `Xi`;
- promocion documental o formal;
- transformaciones materiales del repositorio.

## Deudas que permanecen abiertas

- Determinar el resultado de la compuerta de admision formal posterior.
- Precisar si `H-Xi` busca estatus de hipotesis de expediente, herramienta local o promocion separada.
- Mantener `P-107` como problema no resuelto.
- Validar dominios independientes si se quisiera superar la utilidad local.
- Abrir decision puente si aparece dependencia sustantiva de psicologia externa.
- Separar cualquier futura promocion formal de la mera consistencia de `Xi_eval`.

## Resultado

`HXI-001` queda reabierto operativamente para evaluacion controlada.

La siguiente accion limpia es aplicar `HXI-001_Criterios_Admision_Formal_H-Xi.md` contra la evidencia aceptada y emitir una decision de resultado, sin admision automatica.
