# OnSerialError

> Category: `VTSystem` | Type: `method`

## Syntax

```c
void <OnSerialError> (dword errorFlags);
```

## Description

The function is called when an error has occurred in an operation on a serial port of the VT7001 module.

## Parameters

| Name | Description |
|---|---|
| Note Several error bits may be set at the same time. Some error flags are up to the driver manufacturer what they mean and when they are issued. |  |

## Return Values

—

## Example

See example SerialConfigure

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.2 SP3 | 13.0 | — | — | 1.0 |
| Restricted To | — | Main method of test nodes | Main method of test nodes VT offline | — | — | Main method |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
