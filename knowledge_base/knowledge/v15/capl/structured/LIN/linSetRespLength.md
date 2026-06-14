# linSetRespLength

> Category: `LIN` | Type: `function`

## Syntax

```c
long linSetRespLength(long frameID, long numberOfBytes);
```

## Description

This function can be used to configure how many data bytes of the frame response should be sent. The frame’s length is not changed by this function.

To send a correct response the numberOfBytes should be set equal to DLC+1 i.e for the frame data bytes and their checksum.

If the numberOfBytes is to set to a value larger than DLC + 1, then a complete response is also sent.

If the numberOfBytes is set to a value smaller than DLC+1, then a receiving error will occur or if numberOfBytes = 0 a transmission error.

## Parameters

| Name | Description |
|---|---|
| frameID | Identifier of the LIN frame to be configured. Value range: 0…63 |
| numberOfBytes | Number of bytes to be sent in the frame response (including checksum). Value range: 0..DLC+1 |

## Return Values

On success, a value unequal to zero, otherwise zero.

## Example

```c
linFrame MotorControl frameMotorControl;
...
if (linSetRespLength (frameMotorControl.ID, frameMotorControl.DLC) != 0) {
   // from now on a receive error notified for the MotorControl frame
...
}
if (linSetRespLength (frameMotorControl.ID, 0) != 0)
{
// from now on a transmission error notified for the MotorControl frame
...
}
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 5.0 | 5.0 | 13.0 | 13.0 | — | 1.0 |
| Restricted To | LIN | LIN | LIN | LIN | — | LIN |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | — | N/A |
