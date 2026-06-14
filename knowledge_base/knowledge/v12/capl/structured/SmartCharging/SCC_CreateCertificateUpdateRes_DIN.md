# SCC_CreateCertificateUpdateRes_DIN

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_CreateCertificateUpdateRes_DIN ( byte SessionID[], dword ConfigSection, char ResponseCode[], char EncryptedPrivateKey[], char DHParams[], char ContractID[], long RetryCounter, char MessageID[] )
```

## Description

Creates a Certificate Installation Response message for sending.

## Return Values

1 if successful

## Availability

| Since Version |
|---|
