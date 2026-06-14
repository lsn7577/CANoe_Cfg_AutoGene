# ChkQuery_NumTimedoutRequests

> Category: `Test` | Type: `function`

## Syntax

```c
long ChkQuery_NumTimedoutRequests (dword aCheckId);
```

## Description

Returns the number of requests within the current observation period for which no corresponding response message was observed during the specified timeout.

In the context of a method protocol check, an occurred timeout of tWaitForProcessing1 or tWaitForProcessing2 will also count that request to the number returned by this function, regardless whether the final "Result"/"ResultAck" or "Error"/"ErrorAck" response is observed within tMaxDuration or not.

## Parameters

| Name | Description |
|---|---|
| aCheckId | Reference to check context. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 6.0 7.0 SP5: method | — | — | — | — |
| Restricted To | — | MOST | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
