# ARILSetAutoStartParam

> Category: `AUTOSARpduIL` | Type: `function`

## Syntax

```c
long ARILSetAutoStartParam(dword state)
```

## Description

This function influences the start behavior. The function must be called in

on preStart, otherwise it will not have any effect.

## Parameters

| Name | Description |
|---|---|
| state | The value defines the desired start behaviour: 0: IL will start in state waiting (see Interaction Layer State Model). The IL can be activated by calling ARILControlResume. 1: IL will start in state suspended (see Interaction Layer State Model). The IL can be activated by calling ARILControlStart. This is the same effect as calling function ARILControlInit in on preStart. 2: IL will start in state running (see Interaction Layer State Model). PDUs will be sent. This is the default, when the function is not called. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 SP2 | 14 | 14 | — | — |
| Restricted To | — | CAN Ethernet FlexRay | CAN Ethernet FlexRay | CAN Ethernet FlexRay | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | ✔ | — | N/A |
