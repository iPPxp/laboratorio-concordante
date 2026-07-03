# AO-001 - Criterios de uso de R4 y Gamma fuera de AUD-001

Estatus: criterios provisionales aceptados.

Fecha: 2026-07-03.

ID: `AO-R4-GAMMA-USE-001`.

Expediente padre: `AO-001`.

## Proposito

Definir el uso permitido de `R4-FORMAL-AUD-001` y `GAMMA-FORMAL-AUD-001` fuera de `AUD-001` sin exportar su autoridad.

## Fuentes

- `03_Expedientes/AUD-001_R4_Formal_Local.md`
- `03_Expedientes/AUD-001_Gamma_Formal_Local.md`
- `03_Expedientes/AUD-001_Decision_Estatus_R4_Gamma_Formal_Local.md`
- `03_Expedientes/AO-001_Prueba_Gamma_Externa.md`
- `03_Expedientes/AO-001_Casos_Prueba_Algebra_Operacional.md`

## Usos permitidos

### Uso 1 - Referencia formal local

Se puede citar `R4-FORMAL-AUD-001` o `GAMMA-FORMAL-AUD-001` para explicar una estructura formal ya aceptada dentro de `AUD-001`.

La cita no cambia el estatus de la estructura citada.

### Uso 2 - Prueba local controlada

Se puede usar una construccion formal local como parte de una prueba acotada si la prueba declara:

- evidencia;
- contexto;
- testigo;
- restricciones;
- deudas;
- salida segura.

### Uso 3 - Puente de problema

Se puede usar R4/Gamma como puente para formular problemas abiertos, especialmente Confluencia y Equivalencia de proyecciones.

El puente solo puede producir avance local, no cierre global.

## Usos prohibidos

- promocion canonica;
- promocion a Nivel C;
- uso como permiso de transformacion;
- cierre de Confluencia por declaracion;
- cierre de Equivalencia de proyecciones por declaracion;
- sustitucion de auditoria por analogia formal;
- exportacion de autoridad fuera de `AUD-001` o `AO-001`.

## Regla de salida

Toda salida que use R4/Gamma fuera de `AUD-001` debe declarar uno de estos estatus:

- `referencia_formal_local`;
- `prueba_local_controlada`;
- `puente_de_problema`;
- `bloqueado_por_estatus_insuficiente`.

## Veredicto

Los criterios permiten avanzar con R4/Gamma en `AO-001` sin promoverlos.

## Deudas

- definir una interfaz formal comun si se repiten pruebas locales;
- decidir promocion solo mediante expediente separado;
- mantener visible la deuda de implementacion ejecutable si el uso deja de ser documental.
