# testWaitForScopeFitDataFr

> Category: `Test` | Type: `function`

## Syntax

```c
long testWaitForScopeFitDataFr(frFrame aMessage, dword msgFieldStart, dword msgFieldEnd); // form 1
long testWaitForScopeFitDataFr(frFrame aMessage, dword msgFieldStart, dword msgFieldEnd, dword preTimeNs, dword postTimeNs); // form 2
```

## Description

The defined frame cutout is shown in the scope's Diagram view. The enlarged area is automatically scaled in time direction.

## Parameters

| Name | Description |
|---|---|
| aMessage | The frame to be fitted. |
| msgFieldStart, msgFieldEnd | The start and end of the cutout to be fitted. See ScopeBitAnalyse.cin |
| preTimeNs | Defines the preliminary lead time in [ns] for the defined message field start. |
| postTimeNs | Defines the overtravel time in [ns] for the defined message field end. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2: form 1 9.0: form 2 | 13.0 | — | — | 1.1 SP2: form 1 2.1: form 2 |
| Restricted To | — | FlexRay Scope | FlexRay Scope | — | — | FlexRay Scope |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
