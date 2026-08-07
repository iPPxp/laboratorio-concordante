# MOC-EXTRACTOR-001-C — Prompt y parser de validación

**Estado:** revisión ejecutable en preparación  
**Banco visible autoritativo:** `C:\Users\IximM\Downloads\MOC-EXTRACTOR-001-B_EXP-A-DEV_v3.1.json`  
**SHA-256 obligatorio:** `69e655ccf3ca655d415b2868a072086682ad42a97f7e00c141129967faa64d54`

## Alcance

`MOC-EXTRACTOR-001-C` vuelve ejecutable el contrato observable del banco DEV sin modificarlo ni incorporarlo al repositorio. El frente incluye:

1. esquema exacto de salida;
2. prompt de extracción no clínica;
3. parser JSON estricto y determinista;
4. validación estructural, referencial y de spans Unicode;
5. comparación semántica contra el banco visible;
6. corrida reproducible de primer intento y reintento;
7. reporte por caso, categoría y taxonomía de fallo.

No se construyen conjuntos `VAL`, adversariales ocultos ni `TEST` en este frente.

## Inventario congelado esperado

- 12 casos;
- 35 claims principales;
- 5 restricciones candidatas;
- 4 unknowns explícitos;
- 8 fricciones;
- 44 IDs totales y únicos;
- 21 reglas normativas declarativas.

La carga del banco aborta antes de cualquier ejecución si la huella o el inventario no coinciden.

## Contrato de cierre

Una corrida de `001-C` puede cerrar estructuralmente cuando cumple simultáneamente:

- código final `0` del corredor;
- cero errores estructurales;
- cero referencias rotas;
- cero spans inválidos;
- salida de los 12 casos;
- reporte semántico que separe omisiones, extracciones espurias, normalizaciones incorrectas y violaciones de `must_not_produce`;
- resultados de primer intento y reintento conservados por separado.

El cierre estructural no equivale a validación en conjuntos ocultos ni autoriza uso clínico, diagnóstico o automatización sobre personas.

## Archivos

- `schema/moc_extractor_001_c.schema.json`: esquema de salida por lote.
- `prompts/MOC-EXTRACTOR-001-C_PROMPT.md`: instrucciones del extractor.
- `src/moc_extractor_001_c.py`: carga segura, parser, validador y reporte.
- `src/run_dev.py`: ejecución reproducible con Codex CLI y reintento.
- `tests/test_moc_extractor_001_c.py`: pruebas unitarias del contrato.

## Ejecución

```text
py -3 moc_extractor_001_c/src/moc_extractor_001_c.py inspect-bank \
  --bank "C:\Users\IximM\Downloads\MOC-EXTRACTOR-001-B_EXP-A-DEV_v3.1.json"
```

```text
py -3 moc_extractor_001_c/src/run_dev.py \
  --bank "C:\Users\IximM\Downloads\MOC-EXTRACTOR-001-B_EXP-A-DEV_v3.1.json" \
  --codex-exe "RUTA_AL_CODEX_EXE" \
  --model "MODELO_EXPLICITO" \
  --out-dir moc_extractor_001_c/runs/DEV-2026-08-06
```

El corredor proyecta únicamente `case_id`, `raw_narrative`, el catálogo normativo y el catálogo cerrado de IDs/reglas de fricción. No entrega al modelo claims esperados, restricciones esperadas, unknowns esperados, relaciones esperadas por caso, notas de aceptación ni inferencias prohibidas del banco.

El parser canoniza exclusivamente los límites numéricos de un span cuando el `evidence_span.text` emitido aparece una sola vez, de forma exacta, en la narrativa. Nunca cambia el texto, la superficie, el campo ni la normalización. Si hay cero o varias coincidencias, falla cerrado y conserva el span como inválido.
