# ARILFaultInjectionDisturbSequenceCounter

> Category: `AUTOSARpduIL` | Type: `function`

## Syntax

```c
long ARILFaultInjectionDisturbSequenceCounter (dbMsg dbMessage, long type, long disturbanceMode, long disturbanceCount, long disturbanceValue, long continueMode);
long ARILFaultInjectionDisturbSequenceCounter (dbMsg dbMessage, char signalGroupName[], long type, long disturbanceMode, long disturbanceCount, long disturbanceValue, long continueMode);
```

## Description

Disturbs the SQC or TGL of a PDU or signal group (see Supported Features).

The function without the parameter for the signal group will only disturb SQCs or TGLs that are not part of a signal group.

## Parameters

| Name | Type | Description |
|---|---|---|
| dbMessage |  | The symbolic name of a PDU in the database. |
| signalGroupName |  | The symbolic full name of the signal group. |
| type |  | 0: SQC 1: TGL Others: all other values are reserved |
| Value | Mode | Description |
| 0 | Value | Sets the SQC fix to the value of parameter disturbanceValue. |
| 1 | Freeze | Current signal value is used (disturbanceValue is not used). |
| 2 | Random | Random value is used (disturbanceValue is not used). |
| 3 | Offset | Signal value is increased by value of parameter disturbanceValue. |
| Value | Repetition | Description |
| -1 | Infinite | Disturbance is continuously applied. |
| 0 | Stop | An active disturbance is stopped and the SQC will be calculated again appropriately. |
| n > 0 | Count | Do exactly n disturbances. |
| disturbanceValue |  | According to the disturbance mode the SQC will optionally be set to this value. |
| Value | Mode | Description |
| 0 | Correct Counter | The counter will continue as if there had never been a disturbance: 0, 1, 2, 6, 6, 5, 6 … |
| 1 | Last Valid Counter | The counter will continue by increasing last valid counter: 0, 1, 2, 6, 6, 3, 4 ... |
| 2 | Last Value | The counter will continue by increasing the last transmitted value: 0, 1, 2, 6, 6, 7, 8 ... |

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
