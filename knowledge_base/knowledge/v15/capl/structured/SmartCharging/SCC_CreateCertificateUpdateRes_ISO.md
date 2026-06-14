# SCC_CreateCertificateUpdateRes_ISO

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_CreateCertificateUpdateRes_ISO ( byte SessionID[], dword ConfigSection, char ResponseCode[], byte EncryptedPrivateKey[], byte DHParams[], char ContractID[] )
```

## Description

Creates a Certificate Update Response message for sending.

## Parameters

| Name | Description |
|---|---|
| SessionID | 8-byte long SessionID of SCC connection, range: 0 - 0xFF FF FF FF FF FF FF FF. |
| ConfigSection | Number of the section from the test configuration file to use. |
| ResponseCode | Acknowledgement status of the message. |
| EncryptedPrivateKey | The private key that belongs to the new certificate for signature purposes. |
| DHParams | Diffie Hellman parameter string. |
| ContractID | ID string of the contract (eMAID). |
| Index | Name Type Description |
| 0 | RetryCounter long In case of failure, this denotes when the EVCC should try to get the new Certificate again (number of days). |

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
