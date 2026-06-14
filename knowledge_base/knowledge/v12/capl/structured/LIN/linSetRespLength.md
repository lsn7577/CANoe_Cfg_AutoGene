# linSetRespLength

> Category: `LIN` | Type: `function`

## Syntax

```c
long linSetRespLength(long frameID, long numberOfBytes)
```

## Description

This function can be used to configure how many data bytes of the frame response should be sent. The frame’s length is not changed by this function.

To send a correct response the numberOfBytes should be set equal to DLC+1 i.e for the frame data bytes and their checksum.

If the numberOfBytes is to set to a value larger than DLC + 1, then a complete response is also sent.

If the numberOfBytes is set to a value smaller than DLC+1, then a receiving error will occur or if numberOfBytes = 0 a transmission error.

This function can be used to simulate collisions during sending of a frame response e.g. after receiving an event triggered frame.

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

| Since Version |
|---|
