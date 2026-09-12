# Compatibilidad con MOC Base 1.0-RC1

## Baseline usado

```text
ARCHIVE = MOC-Base-1.0-RC1-SECRETS2.tar.gz
ARCHIVE_SHA256 = 6bf2abe1799c31346f1710ab8ffe13cf28e66a1d8d86e5885fde2f4d7a35ef6f
RC1_CLASSIFICATION = functional reference core; not production-ready
FREEZE_RULE = cualquier cambio en un archivo cubierto deja de ser RC1
```

## Estrategia

La extensión es un paquete lateral. No reemplaza `moc_pipeline_impl.py`, no
modifica `MatrixQ`, no altera métricas `v1.3`, no cambia el vault y no interviene
en el flujo de secretos.

```text
RC1 envelope / MatrixQ
        |
        | lectura no mutante + mapping declarado
        v
geometry sidecar report
```

## Contrato de adaptación

1. El llamador entrega una biyección explícita fila→componente.
2. Las claves deben coincidir exactamente con las filas de la matriz.
3. Los vectores originales se conservan sin agregación.
4. La procedencia original se copia como evidencia del dato, no de la semántica.
5. El snapshot inicial no contiene relaciones observadas.
6. El catálogo de diez pares queda separado del estado observado.
7. RC1 no se muta y su freeze conserva su significado histórico.

## Lo aprovechado de RC1

- vectores por fila ya validados;
- confianza y procedencia;
- identificadores de ejecución/candidato;
- estados y transformaciones temporales ya auditables;
- política de fallar de forma cerrada;
- separación entre cálculo y afirmaciones humanas.

## Lo que queda fuera

- extracción automática de `P/Eaf/Act/V/S` desde texto;
- aprobación del mapeo `I/E/A/V/S`;
- semántica definitiva de las diez relaciones;
- eficacia predictiva;
- interpretación clínica o evaluación de personas;
- incorporación a la imagen Docker congelada;
- publicación como RC2 o versión de producción.

## Límite de verificación local

El RC1 importa `fcntl` y su vault es una implementación POSIX. En Windows se
verifica la compatibilidad del adaptador con las clases reales de matriz usando
un sustituto inerte exclusivamente durante la importación. El runtime integral
debe probarse en Linux; en esta materialización no se presume que esa prueba ya
haya ocurrido.
