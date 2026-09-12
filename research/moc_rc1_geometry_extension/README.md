# MOC RC1 — extensión geométrica relacional candidata

```text
EXTENSION_ID = MOC-RC1-GEOMETRY-EXTENSION-001
STATUS = CANDIDATE
RC1_MUTATED = NO
SEMANTIC_AUTHORITY = MOC_HUMAN_AUTHORITY_ONLY
COMPUTATIONAL_AUTHORITY = VALIDATION_AND_REPRESENTATION_ONLY
SCIENTIFIC_VALIDATION = NOT_TESTED
CANONIZATION = NO
ACTIVATION = NO
```

Esta carpeta contiene una extensión opcional y no mutante para **MOC Base
1.0-RC1**. RC1 está congelado por huella; por tanto, cualquier modificación de
sus archivos dejaría de ser RC1. La extensión se ejecuta como *sidecar* sobre
un `ExtractionEnvelope` o `MatrixQ` ya producido por RC1.

## Qué incorpora

- cinco observaciones tipadas: `P`, `Eaf`, `Act`, `V`, `S`;
- presencia separada de cambio;
- atribución, evidencia, incertidumbre y procedencia;
- relaciones dirigidas y tipadas, sin activarlas automáticamente;
- comparación temporal de configuraciones;
- inventario combinatorio `5,10,10,5,1`;
- dualidad elemento ↔ cuaterna complementaria;
- proyección 2D sólo mediante matriz declarada, con colisiones y distorsión;
- adaptador de `MatrixQ` que exige un mapeo humano explícito.

## Qué no incorpora

- no presupone que `I` de RC1 signifique `P`;
- no convierte la matriz `I/E/A/V/S` en semántica MOC sin mapeo;
- no añade `conducta` como sexto componente;
- no declara que las diez relaciones candidatas sean verdaderas;
- no interpreta distancia como semejanza semántica;
- no interpreta simetría como concordancia;
- no interpreta centroide como estado ideal;
- no convierte una proyección 2D en representación completa;
- no autoriza G0, entrenamiento, canonización ni activación.

## Uso mínimo

```python
from moc_geometry_extension import analyze_rc1_envelope

report = analyze_rc1_envelope(
    envelope,
    row_mapping={"I": "P", "E": "Eaf", "A": "Act", "V": "V", "S": "S"},
    source_id="declared-human-mapping-001",
)
```

El ejemplo muestra la forma del contrato, no aprueba ese mapeo. Quien llama al
adaptador asume la responsabilidad de declarar y documentar la correspondencia.

## Verificación

```text
python -m unittest -v test_moc_geometry_extension.py
python verify_rc1_adapter.py <directorio-RC1-extraído>
```

La segunda orden comprueba el adaptador contra las clases reales `MatrixQ` y
`MatrixRow`. En Windows utiliza un sustituto inerte de `fcntl` únicamente para
importar esas clases; no prueba el vault POSIX ni el runtime integral.

## Empaquetado reproducible

```text
python build_extension_package.py \
  --rc1-archive <MOC-Base-1.0-RC1-SECRETS2.tar.gz> \
  --output-dir <directorio-de-salida>
```

El paquete resultante es un *overlay* candidato. Incluye la huella SHA-256 del
RC1 de base, no duplica sus bytes y no cambia su identidad congelada.

Véase [MOC-RC1-GEOMETRY-EXTENSION-001.md](MOC-RC1-GEOMETRY-EXTENSION-001.md)
para el contrato y [RC1_COMPATIBILITY.md](RC1_COMPATIBILITY.md) para la frontera
con el RC1 congelado.
