# testWaitForScopePerformFieldLengthMeasurement

> Category: `Test` | Type: `function`

## Syntax

```c
long testWaitForScopePerformFieldLengthMeasurement (frFrame msg, dword msgFieldStart, dword msgFieldEnd, dword bitStartNo, dword bitEndNo, qword fieldLength ScopeAnalyseHandle handle);
```

## Description

Returns the number of bits are contained within the defined range and the length of this range.

## Parameters

| Name | Type | Description |
|---|---|---|
| msg |  | The message where the field length should be measured. |
| msgFieldStart |  | Defines the start of the measurement range. |
| msgFieldEnd |  | Defines the end of the measurement range. |
| bitStartNo |  | The bit within the start field where the measurement starts. |
| bitEndNo |  | The bit within the end field where the measurement ends. |
| fieldLength |  | Returns the length of the defined range. |
| Keyword | Description | Type |
| handle | A unique ID | long |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 | 13.0 | — | — | 3.0 |
| Restricted To | — | LIN Scope | LIN Scope | — | — | LIN Scope |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
