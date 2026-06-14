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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 SP3 | — | — | — | 3.0 SP3 |
| Restricted To | — | Ethernet .SmartCharging | — | — | — | Ethernet .SmartCharging |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
