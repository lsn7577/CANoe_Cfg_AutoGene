# ARILFaultInjectionDisturbChecksum

> Category: `AUTOSARpduIL` | Type: `function`

## Syntax

```c
long ARILFaultInjectionDisturbChecksum (dbMsg dbMessage, long type, long disturbanceMode, long disturbanceCount, long disturbanceValue);
long ARILFaultInjectionDisturbChecksum (dbMsg dbMessage, char signalGroupName[], long type, long disturbanceMode, long disturbanceCount, long disturbanceValue);
```

## Description

Disturbs the CRC of a PDU or signal group (see CRC Value). The function without the parameter for the signal group will only disturb CRCs that are not part of a signal group.

## Parameters

| Name | Type | Description |
|---|---|---|
| dbMessage |  | The symbolic name of a PDU in the database. |
| signalGroupName |  | The symbolic full name of the signal group. |
| type |  | reserved (should be set to 0). |
| Value | Mode | Description |
| 0 | Value | Sets the CRC fix to the value of parameter disturbanceValue. |
| 1 | Freeze | Current signal value is used (disturbanceValue is not used). |
| 2 | Random | Random value is used (disturbanceValue is not used). |
| 3 | Offset | Signal value is increased by value of parameter disturbanceValue. |
| Value | Repetition | Description |
| -1 | Infinite | Disturbance is continuously applied. |
| 0 | Stop | An active disturbance is stopped and the CRC will be calculated again appropriately. |
| n > 0 | Count | Do exactly n disturbances. |
| disturbanceValue |  | According to the disturbance mode the CRC will optionally be set to this value. |

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
