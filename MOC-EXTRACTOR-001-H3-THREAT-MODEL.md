# MOC-EXTRACTOR-001-H3 — Modelo de amenaza

## Garantía

La frontera protegida es JSON/API no confiable procesada por las funciones públicas H3. En esa frontera:

- un cliente no puede declarar una fricción verificada;
- proofs, predicados y hechos semánticos externos no sustituyen cálculos;
- toda promoción recalcula claims y predicado;
- toda entrada C no materialmente JSON-array falla cerrada con un código estable.

## Fuera de alcance

Un atacante con ejecución arbitraria de Python dentro del proceso está fuera de esta garantía. Puede invocar internals, alterar memoria o construir objetos sin validación. Nombres privados, clases congeladas y `model_construct` no se presentan como barreras criptográficas.

No se usa ningún secreto embebido ni una firma simulada. SHA-256 acredita identidad de contenido, no autoría, confianza operacional ni procedencia humana.

## Consecuencia

Los objetos internos sólo son autoritativos cuando aparecen como resultado de una llamada pública que completó la recomputación. Su forma aislada, serializada o fabricada no concede autoridad.
