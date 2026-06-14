# testWaitForScopeGetFieldLengthData

> Category: `Test` | Type: `function`

## Syntax

```c
long testWaitForScopeGetFieldLengthData (ScopeAnalyseHandle handle, dword bitNo, ScopeFieldLengthData bitData);
```

## Description

Returns the number of bits are contained within the defined range and the length of this range.

## Parameters

| Name | Type | Description |
|---|---|---|
| Keyword | Description | Type |
| handle | A unique ID | long |
| Note The bit number is 0-based and cannot be greater than the return value of the function testWaitForScopePerformFieldLengthMeasurement. |  |  |
| bitData |  | Returns the information for the bit (see ScopeFieldLengthData). |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 | 13.0 | — | 14 | 3.0 |
| Restricted To | — | FlexRay Scope | FlexRay Scope | — | FlexRay Scope | FlexRay Scope |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
