# 22 contraejemplos y trampas

1. M-CBM gana porque recibió cinco veces más etiquetas.
2. G-E2E gana accuracy pero está peor calibrado; un único score oculta el trade-off.
3. P y V se distinguen por palabras usadas en el prompt, no por efectos.
4. Paráfrasis de una familia aparece en train y test.
5. Un anotador impone las categorías y luego evalúa su propia consistencia.
6. Los cinco slots anónimos recuperan el mismo rendimiento: nombres no añaden valor.
7. Cuatro slots igualan todo: al menos un factor es redundante.
8. Seis slots mejoran: cinco no es suficiente/minimal.
9. Una representación continua supera toda partición discreta.
10. MOC mejora interpretación humana pero no predicción; no llamar ventaja predictiva.
11. MOC mejora in-domain y empeora OOD.
12. MOC gana sólo con mayor número de parámetros o trials.
13. El outcome futuro aparece indirectamente en el texto crudo.
14. La intervención fue escogida según el estado posterior: confusión por selección.
15. `do(P)` sólo cambia el texto de P, no el mecanismo supuesto.
16. Eaf se trata como knob arbitrario y el contrafactual es inverosímil.
17. Act se identifica con output/conducta y crea una frontera artificial.
18. V se convierte en reward escalar, alterando la semántica.
19. S mezcla hecho externo y relectura, impidiendo atribución.
20. D-state gana sólo porque duplica información de P/R.
21. D-operación añade complejidad sin mejorar ningún outcome.
22. `p>0.05` se interpreta como equivalencia sin prueba de equivalencia.

Cada uno invalida o rebaja una conclusión favorable si aparece.

