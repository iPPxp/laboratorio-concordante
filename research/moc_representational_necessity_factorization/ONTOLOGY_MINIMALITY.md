# Ontología mínima y no redundancia

## Preguntas separadas

Una factorización puede ser interpretable sin ser mínima, mínima sin ser
predictiva o predictiva por supervisión adicional. Se evaluarán por separado:

- **distinguibilidad:** existen contrafactuales donde cambia un componente y los
  demás permanecen aproximadamente estables;
- **no redundancia:** ningún componente es sustituible por los otros sin pérdida
  fuera de muestra;
- **suficiencia:** los cinco retienen información necesaria para las tareas;
- **minimalidad:** ninguna factorización con menos factores iguala el perfil;
- **estabilidad:** la semántica de factores persiste entre anotadores, tiempos y
  dominios;
- **utilidad causal:** intervenir un factor permite predecir efectos diferenciados.

## Diez fronteras

Para los cinco componentes existen diez pares no ordenados:

\[
\binom 52=10.
\]

Cada frontera exige dos direcciones: A cambia con B estable y B cambia con A
estable. Son 20 contrastes mínimos. La mera posibilidad de etiquetar no cuenta;
deben producir predicciones o efectos diferentes.

## Falsadores de cada componente

Para cada `c` se ejecutan:

1. **drop-one:** eliminar `c`;
2. **merge:** fusionar `c` con cada otro tipo;
3. **permute:** permutar su nombre conservando datos y operaciones;
4. **predict-from-others:** reconstruir `c` desde los otros cuatro;
5. **intervention specificity:** comparar `do(c)` con intervenciones en otros;
6. **domain transfer:** repetir fuera del dominio de anotación.

Un componente es computacionalmente redundante si su eliminación/fusión no
empeora ninguna métrica pre-registrada más allá del margen de equivalencia.

## El número cinco no es evidencia

La secuencia combinatoria `1-5-10-10-5-1` es inevitable para cualquier conjunto
de cinco elementos. No respalda la ontología. El frente acepta 4, 4+1, 5, 5+R o
una representación no discreta si los datos la favorecen.

