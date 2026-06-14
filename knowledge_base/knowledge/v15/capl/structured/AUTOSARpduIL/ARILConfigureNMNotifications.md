# ARILConfigureNMNotifications

> Category: `AUTOSARpduIL` | Type: `function`

## Syntax

```c
dword ARILConfigureNMNotifications (dword dir, dword mode);
```

## Description

This function has impact on the (automatic) coupling between IL and NM on the IL side.

Normally, there exists an automatic notification between IL and NM. This can be broken by implementation of dedicated call-back functions for IL and NM. This function defines to take or ignore those notifications always, regardless of existing callbacks.

Remember, an appropriate function can also be called on NM side!

## Parameters

| Name | Description |
|---|---|
| dir | Defines which direction is to be influenced: 0: IL->NM (Tx notifications of IL) 1: NM -> IL (Rx notifications of NM) Other values are reserved. |
| mode | Defines if the notifications are issued or handled (according to the direction): 0: Notifications are not generated (Tx) or incoming notifications (Rx) are ignored. 1: Notifications will be generated (Tx); regardless of existing callback functions of the IL, and are always handled (Rx). 2: Notifications will be generated (Tx) only when specific callback functions of the IL are not implemented, and are always handled (Rx). This is the default, when the function is not called. |

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
