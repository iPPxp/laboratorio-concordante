# Contrato condicional para un futuro G0

```text
ARTIFACT_STATUS = CONDITIONAL_NOT_AUTHORIZED
G0_AUTHORIZED = NO
G0_MANUAL_CALIBRATION = NOT_RUN
```

Este contrato sólo podrá activarse mediante una decisión distinta de la aprobación semántica.

## Alcance propuesto

- entre 10 y 20 fragmentos narrativos sintéticos;
- ningún fragmento reutilizado de F0/F0.1/F0.2;
- positivos, ausencias afirmativas, ambigüedad y desconocimiento;
- al menos dos casos de frontera por componente;
- vecinos negativos y señuelos sin depender de palabras gatillo;
- piloto desechable, excluido de entrenamiento, validación, test y benchmark.

## Dos pasadas independientes

Si sólo participa una persona humana:

1. congelar textos, orden y manual;
2. realizar una primera pasada;
3. cerrar y ocultar sus respuestas;
4. esperar el intervalo aprobado por el protocolo;
5. reordenar los casos de forma preregistrada;
6. realizar una segunda pasada sin consultar la primera;
7. registrar acuerdo y desacuerdos intrapersonales;
8. usar el piloto únicamente para calibrar el manual;
9. descartar el piloto del corpus evaluable.

## Pregunta exclusiva de G0

```text
¿Las reglas aprobadas permiten aplicar las categorías de manera suficientemente estable?
```

Un `PASS` no valida verdad, minimalidad, universalidad, causalidad, factorización ni poder predictivo de MOC. Sólo permite considerar un G1 nuevo.
