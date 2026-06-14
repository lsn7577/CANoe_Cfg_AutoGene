# SCC_GetRootCertificateID

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
void SCC_GetRootCertificateID ( long Index, char IdOrIssuer [], byte SerialNumber[], long& SerialNumberLength )
```

## Description

Gets the content of the RootCertificateID element with the specified index.

## Return Values

The content of the RootCertificateID element with the specified index < GetNumberOfRootCertificateIDs().
For ISO 15118:
The X509IssuerName to the buffer IdOrIssuer
The X509SerialNumber to the buffer SerialNumber
The byte length of X509SerialNumber via the referenceo SerialNumberLength
Else:
TheRootCertificateId string to the buffer IdOrIssuer, while the other parameters are unused

## Availability

| Since Version |
|---|
