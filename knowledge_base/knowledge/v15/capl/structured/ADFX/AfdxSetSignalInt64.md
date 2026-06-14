# AfdxSetSignalInt64

> Category: `ADFX` | Type: `function`

## Syntax

```c
long AfdxSetSignalInt64( long packet, char signalName[], int64 value, long fdsStatus ); // form 1
long AfdxSetSignalInt64( long packet, long offset, int64 value ); // form 2
```

## Description

This function sets the value of a 64-bit integer signal.

## Parameters

| Name | Description |
|---|---|
| packet | Handle of the message. |
| signalName | Name of the signal. Note: The signal and its message need to be defined in the assigned DBC file. |
| offset | The offset value points to the 64-bit integer signal in the AFDX payload area. |
| value | New 64-bit integer value. |
| fdsStatus | 255: The status is not updated valid status enumeration: The functional status is updated with this value. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0 SP3: form 1, 2 | — | — | — | — |
| Restricted To | — | AFDX | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
