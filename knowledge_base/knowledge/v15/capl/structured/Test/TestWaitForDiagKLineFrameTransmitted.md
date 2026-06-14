# TestWaitForDiagKLineFrameTransmitted

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForDiagKLineFrameTransmitted(dword timeout_ms); // form 1
long TestWaitForDiagKLineFrameTransmitted(char ecuQualifier[], dword timeout_ms); // form 2
```

## Description

Waits for the occurrence of a transmitted valid message. Should the message not occur before the expiration of the time timeout_ms, the wait condition is resolved nevertheless.

## Parameters

| Name | Description |
|---|---|
| timeout_ms | Maximum time that should be waited [ms] (Transmission of 0: no timeout controlling) |
| ecuQualifier | Qualifier of the ECU or target as set in the diagnostic configuration dialog for the respective diagnostic description. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0: form 1 9.0 SP3: form 2 | — | — | — | 1.0: form 1 2.1 SP3: form 2 |
| Restricted To | — | K-Line Real bus mode | — | — | — | K-Line Real bus mode |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
