# testWaitForScopeShowEdges

> Category: `Test` | Type: `function`

## Syntax

```c
long testWaitForScopeShowEdges(linFrame aMessage, dword msgFieldStart,long bitNo, long noOfBits, dword flags, ScopeanalyseHandle handle);
```

## Description

The defined frame cutout of the previously transition time measurement frame together with a bit mask is shown in the scope's Diagram view. The bit mask is only shown if the parameter flags is correct defined. The enlarged area is automatically scaled in time direction.

## Parameters

| Name | Description |
|---|---|
| aMessage | The message to be fitted. |
| msgFieldStart | The start of the cutout to be displayed. See ScopeBitAnalyse.cin |
| startBitNo | A bit index in the message field. |
| noOfBits | Count of bits to be displayed. |
| Bits | Description |
| 0 | Bit visible for analyzed edges0 = Without bit mask1 = With bit mask |
| handle | A unique ID. Must be the same handle was used by the call of the function testGetWaitScopeSignalTransitionTime. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 SP4 | 13.0 | — | — | 2.0 SP4 |
| Restricted To | — | LIN Scope | LIN Scope | — | — | LIN Scope |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
