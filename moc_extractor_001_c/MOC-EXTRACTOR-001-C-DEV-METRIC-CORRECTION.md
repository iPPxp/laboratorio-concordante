# MOC-EXTRACTOR-001-C — Corrección metodológica de métricas DEV

**Fecha:** 6 de agosto de 2026  
**Banco:** `MOC-EXTRACTOR-001-B_EXP-A-DEV_v3.1.json`  
**Corrida:** `DEV-2026-08-06-v5-frozen`  
**Alcance:** interpretación operativa de resultados; no modifica prompt, parser, banco ni artefactos congelados

## Corrección

La métrica operativa de una tubería ciega a la verdad dorada es la obtenida en el primer intento que supera el contrato estructural y las prohibiciones ejecutables.

En la corrida congelada, el primer intento produjo:

- código de ejecución `0`;
- 0 errores estructurales;
- 0 referencias rotas;
- 0 spans inválidos después del parser determinista;
- 0 violaciones `must_not_produce`;
- 63 hallazgos semánticos contra el banco DEV visible.

Como el objeto era estructuralmente válido y no contenía infractores ejecutables, una tubería de producción sin acceso a anotaciones doradas lo habría aceptado. No existe fundamento operativo ciego para forzar el reintento.

## Métricas oficiales por función

| Resultado | Hallazgos | Función correcta |
|---|---:|---|
| Primer intento | 63 | Resultado operativo actual y real |
| Segundo intento selectivo | 61 | Experimento de calibración |
| Composición por mejor caso | 58 | Diagnóstico asistido por verdad dorada |

La selección por mejor caso utiliza el reporte semántico contra anotaciones esperadas para elegir entre respuestas. Ese mecanismo es útil como diagnóstico de laboratorio, pero no representa el comportamiento desplegable del pipeline y no debe reportarse como rendimiento operativo.

## Consecuencia para MOC-EXTRACTOR-001-D

La taxonomía primaria de `MOC-EXTRACTOR-001-D-REGRESSION` debe construirse sobre los 63 hallazgos individualizados de:

`runs/DEV-2026-08-06-v5-frozen/attempt-01/validation.json`

El segundo intento y la composición final pueden utilizarse únicamente como evidencia secundaria para estudiar recuperabilidad, estabilidad y sensibilidad del prompt. No sustituyen el baseline operativo.

## Invariantes

- `MOC-EXTRACTOR-001-C` permanece congelado.
- RC1 permanece intacto.
- El banco DEV v3.1 permanece intacto.
- No se crean todavía `VAL-30`, `TEST-18`, API ni frentes de seguridad.
- Esta corrección no altera ninguno de los outputs originales de la corrida v5.
