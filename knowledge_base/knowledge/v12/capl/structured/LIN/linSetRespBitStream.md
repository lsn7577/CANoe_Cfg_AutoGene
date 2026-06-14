# linSetRespBitStream

> Category: `LIN` | Type: `function`

## Syntax

```c
long linSetRespBitStream (long frameId, byte bitStream[], long numberOfBits)
```

## Description

Sets up a bit stream as the response to the specified frame.

## Return Values

On success, a value unequal to zero, otherwise zero.

## Example

Send LIN response for the frame MotorControl as a bit stream.

```c
// The response consists of 8 data bytes and checksum 
 byte. There are no interbyte spaces.
// Response: [D0=0x1, D1=0x2, D2=0x4, D3=0x8, D4=0x10, D5=0x20, D6=0x40, D7=0x80, CS=0x52]
on key 'r'
{
linFrame MotorControl mMotorControl;
byte bitStream[12];
long numberOfBits;
// binary stream = 0100000001 0010000001 0001000001 0000100001 0000010001
// binary stream (continue) = 0000001001 0000000101 0000000011 0010010101
bitStream[0] = 0x2;
bitStream[1] = 0x12;
bitStream[2] = 0x88;
bitStream[3] = 0x20;
bitStream[4] = 0x84;
bitStream[5] = 0x20;
bitStream[6] = 0x2;
bitStream[7] = 0x9;
bitStream[8] = 0x28;
bitStream[9] = 0xC0;
bitStream[10] = 0xA4;
bitStream[11] = 0x2;
numberOfBits = 90; // Each byte requires 10 bits (start bit + data bits + stop bit)
if (0!=linSetRespBitStream(mMotorControl.id, bitStream, numberOfBits))
{
// for the next response of frame "MotorControl" is as specified
}
}
```

## Availability

| Since Version |
|---|
