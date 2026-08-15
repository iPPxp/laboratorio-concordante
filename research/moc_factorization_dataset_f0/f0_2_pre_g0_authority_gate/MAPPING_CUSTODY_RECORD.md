# Registro de custodia separada

```text
CUSTODY_OBJECT = F0_2_SEALED_MAPPING_PAYLOAD
PUBLIC_EXPEDIENT_PAYLOAD = EXCLUDED
PUBLIC_EXPEDIENT_FULL_MANIFEST = EXCLUDED
CUSTODY_STATUS = PRESERVED_OUTSIDE_PUBLIC_EXPEDIENT
RELEASE_AUTHORITY = HUMAN_MOC_REVIEW
AUTOMATIC_RELEASE = NO
```

Los dos artefactos sellados completos permanecen en la superficie de trabajo de custodia y no forman parte de este expediente Git:

```text
research/moc_factorization_dataset_f0_2/SEALED_MAPPING_MANIFEST.json
research/moc_factorization_dataset_f0_2/mapping/MANIFEST.sha256
```

Esta ruta se registra como procedencia local, no como objeto incorporado. Una futura publicación o revelación requiere decisión separada y verificación del digest consignado en `MAPPING_ATTESTATION.md`.
