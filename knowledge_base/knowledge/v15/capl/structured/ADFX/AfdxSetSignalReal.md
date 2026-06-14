# AfdxSetSignalReal

> Category: `ADFX` | Type: `function`

## Syntax

```c
long AfdxSetSignalReal( long packet, char signalName[], float value, long fdsStatus ); // form 1
long AfdxSetSignalReal( long packet, long offset, long isDouble, float value ); // form 2
```

## Description

This function sets the value of a 32-bit or 64-bit float signal (IEEE 754).

## Parameters

| Name | Description |
|---|---|
| packet | handle of the message |
| signalName | name of the signal Note: The signal and its message need to be defined in the assigned DBC file. |
| offset | The offset value points to the float signal in the AFDX payload area. |
| isDouble | 0: set 32-bit float value 1: set 64-bit float value |
| value | new float value |
| fdsStatus | 255: The status is not updated valid status enumeration: The functional status is updated with this value. |

## Return Values

0 or error code

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0 SP3 | — | — | — | — |
| Restricted To | — | AFDX | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
