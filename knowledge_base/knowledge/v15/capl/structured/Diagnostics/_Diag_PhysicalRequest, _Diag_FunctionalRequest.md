# _Diag_PhysicalRequest, _Diag_FunctionalRequest

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void _Diag_PhysicalRequest(char target[], byte rawRequest[]);
void _Diag_FunctionalRequest(char target[], byte rawRequest[]);
```

## Description

The given bytes shall be sent as a physical or functional diagnostic request to the ECU or functional group with the given qualifier.

## Parameters

| Name | Description |
|---|---|
| target | Qualifier of the ECU or functional group to send to. |
| rawRequest | Bytes of the raw request that shall be sent. |

## Return Values

—

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 | — | — | — | 3.0 |
| Restricted To | — | Online mode | — | — | — | Online mode |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
