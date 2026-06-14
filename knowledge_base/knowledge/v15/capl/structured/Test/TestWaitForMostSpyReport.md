# TestWaitForMostSpyReport

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForMostSpyReport(int aFBlockId, int aInstanceId, int aFunctionId, unsigned long aTimeout);
long TestWaitForMostSpyReport(char[] aSymbolicMessage, int aInstanceId, unsigned long aTimeout);
long TestWaitForMostSpyReport(char[] aSymbolicMessage, unsigned long aTimeout);
```

## Description

Waits for the occurrence of the spy response message (report, op-type > 8) of the specified MOST message.

The first arriving control message, which fulfills the specified conditions, resolves the wait point, irregardless of whether it is part of a segmented transmission. TelId is not included in this process.

If the message does not occur by the time the aTimeout expires, the wait condition is still resolved.

## Parameters

| Name | Description |
|---|---|
| Note For parameters aFBlockId, aInstanceId and aFunctionId the following applies: If -1 is given, the corresponding field can get any value. This is also the standard for not explicit set values. |  |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.2 | — | — | — | — |
| Restricted To | — | MOST25, MOST50, MOST150 | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
