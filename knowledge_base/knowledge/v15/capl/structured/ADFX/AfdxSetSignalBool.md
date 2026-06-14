# AfdxSetSignalBool

> Category: `ADFX` | Type: `function`

## Syntax

```c
long AfdxSetSignalBool( long packet, char signalName[], long value, long fdsStatus ); // form 1
long AfdxSetSignalBool( long packet, long offset, long bitPosition, long value ); // form 2
```

## Description

This function sets the value of a Boolean signal.

## Parameters

| Name | Description |
|---|---|
| packet | Handle of the message. |
| signalName | Name of the signal. Note: The signal and its message need to be defined in the assigned DBC file. |
| value | One of the values 0 or 1 is allowed. |
| fdsStatus | 255: The status is not updated valid status enumeration: The functional status is updated with this value. |
| offset | The offset value points to the starting byte of a 32-bit field in the AFDX payload area. |
| bitPosition | Position [1..32] of a single bit in a 32-bit area pointed to by offset. |

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
