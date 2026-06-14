# linSendBitStream

> Category: `LIN` | Type: `function`

## Syntax

```c
long linSendBitStream(byte bitStream[], long numberOfBits)
```

## Description

Sends an arbitrary bit stream on the LIN bus.

## Return Values

On success a value unequal to zero, otherwise zero.

## Example

This function sends LIN header as a bit stream

```c
int SendSpecialHeader(int breakLength, int delimiterLength, byte syncByte, byte idByte)
{
byte data[25];
int headerLength;
int currentPosition;
int i;
   // Header consists of Break, Sync and PID bytes
headerLength = breakLength + delimiterLength + 20;
 
if (headerLength > 200)
{
return 0; // maximum is exceeded
}
currentPosition = 0;
for (i = 0; i < 25; ++i)
{
data[i] = 0xff; // initialize 
}
for (i = breakLength; i > 0;) // set sync break
{
if (i >= 8)
{
data[currentPosition >> 3] = 0;
i -= 8;
currentPosition += 8;
}
else
{
data[currentPosition >> 3] &= ~(1 << 
 (currentPosition & 0x7));
--i;
++currentPosition;
}
}
currentPosition += delimiterLength; // set synch delimiter
   // set sync byte
data[currentPosition >> 3] &= ~(1 << (currentPosition & 0x7)); // start bit
++currentPosition;
for (i = 0; i < 8; ++i)
{
if ((syncByte & (1 << i)) == 0) // dominant bit in syncByte
{
data[currentPosition >> 3] &= ~(1 << (currentPosition & 0x7));
}
++currentPosition;
}
++currentPosition; // set recessive stop bit
   // set protected id
data[currentPosition >> 3] &= ~(1 << (currentPosition & 0x7)); // start bit
++currentPosition;
for (i = 0; i < 8; ++i)
{
if ((idByte & (1 << i)) == 0) // dominant bit in idByte
{
data[currentPosition >> 3] &= ~(1 << (currentPosition & 0x7));
}
++currentPosition;
}
++currentPosition; // set recessive stop bit
linSendBitStream(data, headerLength); // send created header
return headerLength;
}
```

## Availability

| Since Version |
|---|
