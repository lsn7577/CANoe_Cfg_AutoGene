# ResetCanEx

> Category: `CAN` | Type: `function`

## Syntax

```c
void ResetCanEx(long channel);
```

## Description

Resets the CAN controller for one specific CAN channel. Can be used to reset the CAN controller after a BUSOFF or to activate configuration changes. Since execution of the function takes a certain amount of time and the CAN controller is disconnected from the bus for a brief period messages may be lost.

## Parameters

| Name | Description |
|---|---|
| channel | CAN channel |

## Return Values

—

## Example

```c
on key 'r' { // After BUSOFF the controller on Channel 2 is reset
resetCanEx(2);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 4.1 | 4.1 | 13.0 | — | — | 1.0 |
| Restricted To | CAN | CAN | CAN | — | — | CAN |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
