# SCC_GetCertificateChainData

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
void SCC_GetCertificateChainData ( long Target, char IdAttr[], long& SubCertificateCount )
```

## Description

Reads Id (to the output buffer) and number of sub certificates (via reference) of the target certificate chain. The ID is only available for ISO 15118.

## Parameters

| Name | Description |
|---|---|
| Target | Set this according to the type of certificate chain that is queried: 0 = ContractSignatureCertChain 1 = SAProvisioningCertChain (EV and ISO 15118 only) |

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
