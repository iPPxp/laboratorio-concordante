# MOC-001 - Autorizacion interna de derechos para grafo de experiencia

Estatus: autorizacion interna aceptada, preparatoria y no externa.

Fecha: 2026-07-09.

Decision asociada: `D-2026-07-09-002`.

Expediente: `MOC-001`.

## Proposito

Este documento registra la autorizacion interna para que `MOC-EXP-GRAPH-001` pueda preparar propuestas candidatas que dialoguen con Canon y Documento 04.

La autorizacion se apoya en `Licencia_y_Derechos.md`, que reserva derechos a Laboratorio Concordante y permite trabajo interno por personas o agentes autorizados.

## Titular interno

```text
Titular: Laboratorio Concordante
Material: Modelo Operativo Concordante (MOC), Concordante Lab y grafo local de experiencia
Ambito: repositorio local del Laboratorio Concordante
```

## Alcance autorizado

Se autoriza internamente a `MOC-EXP-GRAPH-001` para:

- preparar propuestas candidatas de ajuste para Canon;
- preparar propuestas candidatas de ajuste para Documento 04;
- construir una matriz de impacto sobre `M-000`, `M-001` y `02_Documentos/04_Algebra_Operacional.md`;
- usar `operator_trace` como evidencia local de regla ganadora;
- conservar la notacion del grafo como fuente auxiliar no canonica hasta decision posterior;
- producir reportes no mutantes.

## Alcance no autorizado

Esta autorizacion no permite:

- escribir cambios directos en `01_Canon` o `02_Documentos`;
- declarar incorporacion oficial al Canon;
- declarar incorporacion oficial al Documento 04;
- publicar, redistribuir o relicenciar el grafo fuera del Laboratorio;
- usar el grafo en dominios clinicos, patologicos, juridicos, financieros, laborales, educativos institucionales o regulados;
- evaluar personas reales;
- admitir `H-Xi`;
- canonizar `Xi`, `Xi_psi`, `Phi_psi`, `TrueSelf_psi` o la notacion `psi`;
- cerrar Confluencia global o Equivalencia global;
- promover `REPORT_LAYER`;
- exportar R4/Gamma;
- activar modo mutante.

## Condiciones para una incorporacion futura

Cualquier cambio oficial posterior en Canon o Documento 04 requiere:

1. propuesta candidata separada;
2. matriz de impacto;
3. auditoria formal;
4. prueba no mutante;
5. decision explicita posterior;
6. revision de `Licencia_y_Derechos.md` si el material sale del repositorio local.

## Nota juridica interna

Este documento no sustituye asesoria legal externa. Funciona como registro interno de autorizacion, alcance y restricciones dentro del Laboratorio.

Para publicacion, distribucion, contrato externo, registro formal o uso institucional, debe obtenerse revision legal separada y, si aplica, firma del titular autorizado.

## Salida

```text
autorizacion_interna_preparatoria: true
propuestas_candidatas_canon_doc04: true
edicion_oficial_canon_doc04: false
uso_externo_autorizado: false
modo_mutante_autorizado: false
```

