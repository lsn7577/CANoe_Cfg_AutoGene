# SCC_CertChainVerificationInd

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
void SCC_CertChainVerificationInd ( byte SessionId[], char ChainName[], dword ChainIsValid )
```

## Description

The callback is called when a received certificate chain (e.g. ContractSignatureCertChain) is verified. Certificate chains are sent as part of several V2G messages when in PnC mode. The callback may be called multiple times for a V2G message, if that message contains multiple chains.

In case of errors, the specific error cause(s) can be queried with the function SCC_GertCertChainVerificationDetails .

A list of individual verification errors can be queried with:

## Parameters

| Name | Description |
|---|---|
| SessionId | 8-byte long SessionID of SCC connection, range: 0 – 0xFF FF FF FF FF FF FF FF. |
| ChainName | Name of the verified certificate chain inside the V2G message. |
| ChainIsValid | 1 if the chain was verified as valid, 0 if the chain was verified as invalid. |

## Return Values

—

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 15.0 | — | — | — | — |
| Restricted To | — | Ethernet .SmartCharging | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
