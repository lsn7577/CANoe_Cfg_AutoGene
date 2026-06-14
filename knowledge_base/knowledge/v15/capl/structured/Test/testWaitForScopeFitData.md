# testWaitForScopeFitData

> Category: `Test` | Type: `function`

## Syntax

```c
long testWaitForScopeFitData(message aMessage, dword msgFieldStart, dword msgFieldEnd); // form 1
long testWaitForScopeFitData(message aMessage, dword msgFieldStart, dword msgFieldEnd, dword preTimeNs, dword postTimeNs); // form 2
long testWaitForScopeFitData(linFrame aMessage, dword msgFieldStart, dword msgFieldEnd); // form 3
long testWaitForScopeFitData(linFrame aMessage, dword msgFieldStart, dword msgFieldEnd, dword preTimeNs, dword postTimeNs); // form 4
long testWaitForScopeFitData(message aMessage, dword msgFieldStart, dword msgFieldEnd, dword flags); // form 5
```

## Description

The defined frame cutout is shown in the scope's Diagram view. The enlarged area is automatically scaled in time direction.

## Parameters

| Name | Description |
|---|---|
| aMessage | The message to be fitted. |
| msgFieldStart, msgFieldEnd | The start and end of the cutout to be fitted. See ScopeBitAnalyse.cin |
| preTimeNs | Defines the preliminary lead time in [ns] for the defined message field start. |
| postTimeNs | Defines the overtravel time in [ns] for the defined message field end. |
| Bits | Description |
| 0 | 0 - CAN high signal not visible 1 - CAN high signal visible |
| 1 | 0 - CAN low signal not visible 1 - CAN low signal visible |
| 2 | 0 - CAN diff signal not visible 1 - CAN diff signal visible |
| 3 | 0 - CAN CMV signal not visible 1 - CAN CMV signal visible |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2: form 1 9.0: form 2 9.0 SP4: form 3, 4 10.0 SP3: form 5: form 1 | 13.0 | — | — | 1.1 SP2: form 1 2.1: form 2 2.1 SP4: form 3, 4 2.2 SP2: form 5 |
| Restricted To | — | CAN Scope | CAN Scope | — | — | CAN Scope |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
