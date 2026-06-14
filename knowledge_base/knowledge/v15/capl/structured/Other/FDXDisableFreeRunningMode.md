# FDXDisableFreeRunningMode

> Category: `Other` | Type: `function`

## Syntax

```c
long FDXDisableFreeRunningMode(long fdxClientHandle, word groupID);
```

## Description

This function disables the Free Running mode for the specified FDX client. The behavior of the function corresponds to the reception of a FreeRunningCancel command via the CANoeFDX protocol.

You can find further information about the Free Running mode in the manual CANoe_FDX_Protocol_EN.pdf.

## Parameters

| Name | Description |
|---|---|
| fdxClientHandle | FDX Client for which the FreeRunningMode should be activated. |
| groupID | Identifies the data group inside the FDX description file. |

## Example

Coupling of two CANoe Instances using the FDX Protocol

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 10.0 SP3 | 13.0 | — | 14 | 2.2 SP2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
