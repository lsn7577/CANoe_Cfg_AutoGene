# testWaitScopeShowMask

> Category: `Test` | Type: `function`

## Syntax

```c
long testWaitScopeShowMask (ScopeAnalyseHandle handle, dword msgFieldStart, long startBitNo, long bitCount); // form 1
long testWaitScopeShowMask (ScopeAnalyseHandle handle, frFrame frame, dword msgFieldStart, long startBitNo, long bitCount); // form 2
```

## Description

The defined frame cutout of the previously analyzed frame together with the bit mask is shown in the scope's Diagram view. The enlarged area is automatically scaled in time direction. Only the differential signal will be displayed.

Form 1: Can only be used for CAN bit mask analysis.

Form 2: Can only be used for FlexRay bit mask analysis.

## Parameters

| Name | Type | Description |
|---|---|---|
| Keyword | Description | Type |
| handle | A unique ID | long |
| frFrame |  | The FlexRay frame to be displayed. |
| msgFieldStart, startBitNo |  | The start of the cutout to be displayed. msgFieldStart: see ScopeBitAnalyse.cin startBitNo: A bit index in the message field |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2 | 13.0 | — | — | 1.1 SP2 |
| Restricted To | — | CAN FlexRay Scope | CAN FlexRay Scope | — | — | CAN FlexRay Scope |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
