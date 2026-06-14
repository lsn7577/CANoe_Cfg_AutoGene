# linSetChecksumError

> Category: `LIN` | Type: `function`

## Syntax

```c
long linSetChecksumError(long frameId, long activate);
```

## Description

Sets/resets a checksum error of a LIN frame. The activated checksum error is then constant and will not be affected by changes in the frame data.

## Parameters

| Name | Description |
|---|---|
| frameId | LIN frame identifier in the range 0 .. 63. |
| activate | 0: deactivate checksum error 1: activate checksum error |

## Return Values

On success, a value unequal to zero, otherwise zero.

## Example

Cause check sum error for all LIN frames on the bus

```c
on linFrame *
{
linSetChecksumError(this.id, 1);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 6.0 | — | — | — | 1.0 |
| Restricted To | — | LIN Real bus mode | — | — | — | LIN Real bus mode |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
