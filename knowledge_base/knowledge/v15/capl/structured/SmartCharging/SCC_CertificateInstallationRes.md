# SCC_CertificateInstallationRes

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
void SCC_CertificateInstallationRes ( byte SessionID[], long ResponseCode, char ContractID[] )
```

## Description

The callback is called as soon as a Certificate Installation Response is received.

Further details that are transmitted in this response can be queried with the following functions:

## Parameters

| Name | Description |
|---|---|
| SessionID | 8-byte long SessionID of SCC connection, range: 0 – 0xFF FF FF FF FF FF FF FF. |
| ResponseCode | 1 if OK, 0 if FAILED |
| ContractID | ID of the contract to which the certificate is assigned, max. 128 character string. (eMAID) |

## Return Values

—

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
