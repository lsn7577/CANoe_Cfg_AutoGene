# ARILControlPDU

> Category: `AUTOSARpduIL` | Type: `function`

## Syntax

```c
long ARILControlPDU (dbMsg, dword Control, dword Flags, dword Param1, dword Param2)
```

## Description

Sets/activates/deactivates a special feature/action for a dedicated PDU.

## Parameters

| Name | Description |
|---|---|
| dbMsg | The symbolic name of a PDU in the database. |
| Control | Determines the action/setting to be applied. |
| Flags | Flags that can be applied to the action/setting. |
| Control | Flags Param1 Param2 Meaning |
| 1 | Reserved (should be set to 0) Reserved (should be set to 0) Reserved (should be set to 0) Enable PDU: corresponds to call of ARILFaultInjectionEnablePDU |
| 2 | Reserved (should be set to 0) Reserved (should be set to 0) Reserved (should be set to 0) Disable PDU: corresponds to call of ARILFaultInjectionDisablePDU |
| other | — — — Reserved – should not be used |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 SP2 | 14 | 14 | — | — |
| Restricted To | — | CAN Ethernet FlexRay | CAN Ethernet FlexRay | CAN Ethernet FlexRay | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | ✔ | — | N/A |
