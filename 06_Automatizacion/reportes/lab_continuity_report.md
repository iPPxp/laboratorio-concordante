# LAB_CONTINUITY_REPORT

report_id: DO-LAB-CONTINUITY-20260706-134840
expediente: AUT-001
algoritmo: DO-LAB-CONTINUITY-001
resultado: advertencia
recomendacion: continuar_sin_transformar
transformacion_permitida: false
scope: repo

## Estado operativo

- expediente activo inmediato: `AO-001` queda como frente operativo inmediato para profundizar `AO-PPI-BRIDGE-001`, mantener bloqueada la exportacion general de R4/Gamma, ampliar pruebas heterogeneas de `REPORT_LAYER` solo si una decision futura lo exige, conservar `AO-DOC04-WIDE-TEST-001` como evidencia local no mutante y usar `REPORT-LAYER-C002-GATE-001` solo como compuerta no mutante conforme a `C-002`.
- proximo objetivo: Ampliar `AO-DOC04-WIDE-TEST-001` solo si se requieren casos heterogeneos adicionales de `REPORT_LAYER`, serializacion interfrente o nuevas rutas de `Pi_rep`; la prueba local inicial de 8 casos, la precision de `REPORT_LAYER`, su permanencia local pre-C y la compuerta no mutante `C-002` ya quedaron atendidas por `D-2026-07-06-007`, `D-2026-07-06-014` y `D-2026-07-06-015`.
- ultima decision operativa: `RH-001_Decision_Reconciliacion_PM001.md` (`D-2026-07-06-016`): acepta `RH-PM-REC-001`; `PM-001` queda reconciliado solo como deuda historica condicionada, no como expediente activo ni protocolo materializado.

## Cobertura integrada

- tablero: ok (0 hallazgos)
- chequeo medio: advertencia (401 archivos, 353 hallazgos)
- automatizaciones presentes: 11/7
- hallazgos combinados: 353

## Riesgos

- [warning] DO-CHECK-MED-001 CHANGELOG.md - referencia_historica_transferida: Referencia a PSI-001 transferido fuera del Laboratorio; no exige restaurar copia local. | evidencia: PSI-001_Criterios_Admision.md
- [warning] DO-CHECK-MED-001 CHANGELOG.md - referencia_historica_transferida: Referencia a PSI-001 transferido fuera del Laboratorio; no exige restaurar copia local. | evidencia: PSI-001_Decision_Apertura.md
- [warning] DO-CHECK-MED-001 CHANGELOG.md - referencia_historica_transferida: Referencia a PSI-001 transferido fuera del Laboratorio; no exige restaurar copia local. | evidencia: PSI-001_Auditoria_A-PSI-001.md
- [warning] DO-CHECK-MED-001 CHANGELOG.md - referencia_historica_transferida: Referencia a PSI-001 transferido fuera del Laboratorio; no exige restaurar copia local. | evidencia: PSI-001_Decision_Estatus_A-PSI-001.md
- [warning] DO-CHECK-MED-001 CHANGELOG.md - referencia_historica_transferida: Referencia a PSI-001 transferido fuera del Laboratorio; no exige restaurar copia local. | evidencia: PSI-001_Definicion_Organizacion_Experiencia_Psicologica.md
- [warning] DO-CHECK-MED-001 CHANGELOG.md - referencia_historica_transferida: Referencia a PSI-001 transferido fuera del Laboratorio; no exige restaurar copia local. | evidencia: PSI-001_Auditoria_Definicion_Organizacion.md
- [warning] DO-CHECK-MED-001 CHANGELOG.md - referencia_historica_transferida: Referencia a PSI-001 transferido fuera del Laboratorio; no exige restaurar copia local. | evidencia: PSI-001_Decision_Estatus_Definicion_Organizacion.md
- [warning] DO-CHECK-MED-001 CHANGELOG.md - referencia_historica_transferida: Referencia a PSI-001 transferido fuera del Laboratorio; no exige restaurar copia local. | evidencia: PSI-001_Criterio_Transformacion_Experiencia_Psicologica.md
- [warning] DO-CHECK-MED-001 CHANGELOG.md - referencia_historica_transferida: Referencia a PSI-001 transferido fuera del Laboratorio; no exige restaurar copia local. | evidencia: PSI-001_Auditoria_Criterio_Transformacion.md
- [warning] DO-CHECK-MED-001 CHANGELOG.md - referencia_historica_transferida: Referencia a PSI-001 transferido fuera del Laboratorio; no exige restaurar copia local. | evidencia: PSI-001_Decision_Estatus_Criterio_Transformacion.md
- [warning] DO-CHECK-MED-001 CHANGELOG.md - referencia_historica_transferida: Referencia a PSI-001 transferido fuera del Laboratorio; no exige restaurar copia local. | evidencia: PSI-001_Ejemplos_Conceptuales_No_Clinicos.md
- [warning] DO-CHECK-MED-001 CHANGELOG.md - referencia_historica_transferida: Referencia a PSI-001 transferido fuera del Laboratorio; no exige restaurar copia local. | evidencia: PSI-001_Auditoria_Ejemplos_Conceptuales.md
- [warning] DO-CHECK-MED-001 CHANGELOG.md - referencia_historica_transferida: Referencia a PSI-001 transferido fuera del Laboratorio; no exige restaurar copia local. | evidencia: PSI-001_Decision_Estatus_Ejemplos_Conceptuales.md
- [warning] DO-CHECK-MED-001 CHANGELOG.md - referencia_historica_transferida: Referencia a PSI-001 transferido fuera del Laboratorio; no exige restaurar copia local. | evidencia: PSI-001_Mapa_Continuidad_Conceptual.md
- [warning] DO-CHECK-MED-001 CHANGELOG.md - referencia_historica_transferida: Referencia a PSI-001 transferido fuera del Laboratorio; no exige restaurar copia local. | evidencia: PSI-001_Casos_Transformacion_No_Clinicos.md
- [warning] DO-CHECK-MED-001 CHANGELOG.md - referencia_historica_transferida: Referencia a PSI-001 transferido fuera del Laboratorio; no exige restaurar copia local. | evidencia: PSI-001_Auditoria_Casos_Transformacion_No_Clinicos.md
- [warning] DO-CHECK-MED-001 CHANGELOG.md - referencia_historica_transferida: Referencia a PSI-001 transferido fuera del Laboratorio; no exige restaurar copia local. | evidencia: PSI-001_Decision_Estatus_Casos_Transformacion_No_Clinicos.md
- [warning] DO-CHECK-MED-001 CHANGELOG.md - referencia_historica_transferida: Referencia a PSI-001 transferido fuera del Laboratorio; no exige restaurar copia local. | evidencia: PSI-001_Matriz_Patrones_Transformacion_No_Clinica.md
- [warning] DO-CHECK-MED-001 CHANGELOG.md - referencia_historica_transferida: Referencia a PSI-001 transferido fuera del Laboratorio; no exige restaurar copia local. | evidencia: PSI-001_Auditoria_Matriz_Patrones_Transformacion_No_Clinica.md
- [warning] DO-CHECK-MED-001 CHANGELOG.md - referencia_historica_transferida: Referencia a PSI-001 transferido fuera del Laboratorio; no exige restaurar copia local. | evidencia: PSI-001_Decision_Estatus_Matriz_Patrones_Transformacion_No_Clinica.md
- [warning] DO-CHECK-MED-001 CHANGELOG.md - referencia_no_materializada: 06_Automatizacion/lab_run.py --scope claves --format md
- [warning] DO-CHECK-MED-001 CHANGELOG.md - referencia_no_materializada: MOC/TCS
- [warning] DO-CHECK-MED-001 CHANGELOG.md - referencia_no_materializada: MOC/AO
- [warning] DO-CHECK-MED-001 CHANGELOG.md - referencia_no_materializada: MOC/C-001/C-002
- [warning] DO-CHECK-MED-001 CHANGELOG.md - referencia_no_materializada: MOC/C-001/C-002
- [warning] DO-CHECK-MED-001 CHANGELOG.md - accion_de_nivel_sensible: La linea parece tocar Canon, documento oficial, expediente cerrado o hipotesis. | evidencia: - Actualizado el estado del proyecto: el siguiente objetivo es decidir si `SPEC-AUD-001_Candidata` se promueve a documento oficial de Nivel C.
- [warning] DO-CHECK-MED-001 CHANGELOG.md - accion_de_nivel_sensible: La linea parece tocar Canon, documento oficial, expediente cerrado o hipotesis. | evidencia: - Creada `DO-001_Decision_Promocion_SPEC-AUD-001.md` con `PROM-SPEC-AUD-001`: se promueve `SPEC-AUD-001_Candidata` a documento oficial de Nivel C.
- [warning] DO-CHECK-MED-001 CHANGELOG.md - expediente_cerrado_afectado: La linea parece afectar expediente cerrado: HXI-001 | evidencia: - Creado `HXI-001_Reapertura_Operativa.md` como `HXI-REOPEN-001`: `HXI-001` se reabre como frente activo inmediato para aplicar la compuerta de admision formal posterior.
- [warning] DO-CHECK-MED-001 CURRENT_STATE.md - referencia_no_materializada: MOC/AO
- [warning] DO-CHECK-MED-001 CURRENT_STATE.md - referencia_no_materializada: MOC/AO
- [warning] DO-CHECK-MED-001 CURRENT_STATE.md - referencia_no_materializada: MOC/TCS
- [warning] DO-CHECK-MED-001 CURRENT_STATE.md - referencia_no_materializada: MOC/TCS
- [warning] DO-CHECK-MED-001 CURRENT_STATE.md - referencia_no_materializada: MOC/TCS
- [warning] DO-CHECK-MED-001 CURRENT_STATE.md - referencia_no_materializada: MOC/AO
- [warning] DO-CHECK-MED-001 CURRENT_STATE.md - referencia_no_materializada: MOC/AO
- [warning] DO-CHECK-MED-001 CURRENT_STATE.md - referencia_no_materializada: MOC/C-001/C-002
- [warning] DO-CHECK-MED-001 CURRENT_STATE.md - referencia_no_materializada: MOC/C-001/C-002
- [warning] DO-CHECK-MED-001 CURRENT_STATE.md - referencia_no_materializada: MOC/AO
- [warning] DO-CHECK-MED-001 CURRENT_STATE.md - referencia_no_materializada: MOC/TCS
- [warning] DO-CHECK-MED-001 CURRENT_STATE.md - referencia_no_materializada: MOC/AO
- ... 313 hallazgos adicionales en JSON.

## Siguientes acciones

- Separar advertencias heredadas de riesgos operativos nuevos.
- Separar advertencias historicas conocidas de riesgos operativos nuevos.
- Mantener transformacion_permitida en false hasta decision explicita.
