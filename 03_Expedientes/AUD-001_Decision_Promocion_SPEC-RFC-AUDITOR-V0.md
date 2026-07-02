# AUD-001 - Decision de promocion de SPEC-RFC-AUDITOR-V0

Estatus: decision de expediente con efecto documental.

ID: `PROM-SPEC-RFC-AUDITOR-V0`.

Fecha: 2026-07-02.

Objeto: decidir si `SPEC-RFC-AUDITOR-V0` se promueve a documento oficial de Nivel C.

## Decision

Se promueve `SPEC-RFC-AUDITOR-V0` a documento oficial de Nivel C en formato tipo RFC.

Destino documental:

```text
02_Documentos/C-002_RFC_Operativo_Auditor_v0.md
```

Nombre oficial: `C-002 - RFC Operativo del Auditor v0`.

## Fundamento

La promocion se funda en:

- `NIVEL-C-001`, que define condiciones locales de especificaciones tecnicas;
- `D-AUD-V0-001`, que acepta completitud documental/operativa v0 del Auditor;
- `AUD-001_SPEC-RFC-AUDITOR-V0_Candidata.md`, candidata con alcance exportable;
- `AUD-001_Validaciones_SPEC-RFC-AUDITOR-V0.md`, validacion favorable de contenido;
- `AUD-001_Auditoria_SPEC-RFC-AUDITOR-V0_NIVEL-C.md`, auditoria favorable contra Nivel C;
- `M-000` y `M-001`, por separacion de niveles y auditoria minima.

## Alcance oficial aprobado

El documento oficial cubre:

- uso operativo no mutante del Auditor;
- lenguaje normativo local;
- modelo de reportes y decisiones;
- frontera entre recomendacion, decision y ejecucion;
- permisos para transformacion acotada;
- criterios de conformidad;
- matriz minima de pruebas;
- limites y deudas vivas.

## Deudas fuera de promocion

La promocion no resuelve:

- Regla R4 formal;
- `Gamma` formal;
- implementacion ejecutable completa;
- parser real;
- reversion material;
- cuarentena materializada;
- promocion de `REPORT_LAYER` a Nivel C;
- cierre de `H-B.6` o `H-B.7`.

## Efectos

- `C-002_RFC_Operativo_Auditor_v0.md` queda como documento oficial de Nivel C.
- `C-002` complementa `C-001`; no lo reemplaza.
- `AUD-001` conserva deudas formales y rutas posteriores.
- Cualquier implementacion futura debe declarar conformidad contra `C-002`.

## Restricciones

La existencia de `C-002` no autoriza cambios reales sin `PERMISO-ACT-001`.

Tampoco modifica Canon, documentos marco, expedientes cerrados ni deudas fuera de alcance.
