# Bibliografia y auditoria epistemica

## Fuentes usadas como anclajes

1. **Hales, T. C. (2005).** *A proof of the Kepler conjecture.* Annals of Mathematics 162(3), 1065-1185. DOI: [10.4007/annals.2005.162.1065](https://doi.org/10.4007/annals.2005.162.1065).  
   Uso: resultado clasico sobre cota de densidad global en dimension tres. No se usa como prueba de una transicion local.
2. **Hales, T. et al. (2017).** *A formal proof of the Kepler conjecture.* Forum of Mathematics, Pi. Prepublicacion: [arXiv:1501.02155](https://arxiv.org/abs/1501.02155).  
   Uso: antecedente de formalizacion mecanica; no se afirma que el codigo de este directorio formalice pruebas.
3. **Rankin, R. A. (1955).** *The Closest Packing of Spherical Caps in n Dimensions.* Proceedings of the Glasgow Mathematical Association 2(3), 139-144. DOI: [10.1017/S2040618500033219](https://doi.org/10.1017/S2040618500033219).  
   Uso: antecedente de la formulacion mediante codigos/capas esfericas.
4. **Schutte, K. & van der Waerden, B. L. (1953).** *Das Problem der dreizehn Kugeln.* Mathematische Annalen 125, 325-334.  
   Uso: antecedente historico para el numero de besos tridimensional; requiere obtener y revisar la fuente primaria antes de citar detalle de su prueba.
5. **OpenStax (consulta institucional, 2026-08-09).** *Estructuras de red en los solidos cristalinos.* [Enlace](https://openstax.org/books/qu%C3%ADmica-2ed/pages/10-6-estructuras-de-red-en-los-solidos-cristalinos).  
   Uso: contraste didactico de las distinciones FCC/HCP y coordinacion, nunca como sustituto de una prueba de geometria discreta.

## Afirmaciones y alcance de sus fuentes

| Afirmacion | Etiqueta | Fuente/justificacion | No autoriza |
|---|---|---|---|
| La densidad maxima global de esferas congruentes en \(\mathbb R^3\) es \(\pi/\sqrt{18}\) | RESULTADO_CLASICO | Hales 2005; Hales et al. 2017 | Estabilidad local o transiciones finitas |
| Una capa de centros sobre una esfera se relaciona con codigos esfericos | RESULTADO_CLASICO / DERIVACION_SIMBOLICA | Rankin 1955 y formula incluida | Optimo de cualquier conjunto especifico |
| FCC y HCP tienen coordinacion 12 en el modelo ideal | RESULTADO_CLASICO | Cristalografia estandar; coordenadas verificadas localmente por el codigo | Que FCC y HCP sean la misma red o mismo grafo global |
| Los valores de `data/results_initial.*` | RESULTADO_COMPUTADO | Script y pruebas de este directorio | Demostracion independiente de los teoremas generales |

## Necesidades bibliograficas antes de ampliar las pretensiones

- Fuente primaria revisada para la clasificacion de codigos esfericos pequenos que se vaya a citar.
- Literatura de rigidez/jamming con definicion elegida (local, colectivo, estricto) y comparacion de hipotesis.
- Fuente primaria o monografia verificable para Delaunay/Voronoi en casos degenerados.
- Ningun resultado de optimizacion numerica se clasificara como prueba sin certificado reproducible e independiente.
