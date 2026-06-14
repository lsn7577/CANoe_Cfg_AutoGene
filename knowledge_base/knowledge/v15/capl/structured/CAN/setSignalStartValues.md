# setSignalStartValues

> Category: `CAN` | Type: `function`

## Syntax

```c
setSignalStartValues(message msg); // form 1
setSignalStartValues(multiplexed_message msg); // form 2
setSignalStartValues(frFrame frame); // form 3
setSignalStartValues(frFrame frame, byte uninitializedData); // form 4
setSignalStartValues(frPDU pdu); // form 5
setSignalStartValues(frPDU pdu, byte uninitializedData); // form 6
setSignalStartValues(pg paramGroup); // form 7
setSignalStartValues(j1587Param param); // form 8
setSignalStartValues(linFrame msg); // form 9
```

## Description

Sets the values of the signals in the parameter to the start values defined in the database.

## Parameters

| Name | Description |
|---|---|
| msg, frame, pdu, paramGroup, parameter | Objects where the signals shall be set. |
| uninitializedData (Form 4, Form 6) | Value to which the bytes in the frame / PDU shall be set which are not used by signals. |

## Example

```c
message LightState msg;
setSignalStartValues(msg);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.1 | 7.1 | 13.0 | — | — | 1.0 |
| Restricted To | CAN | CAN | CAN | — | — | CAN |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
