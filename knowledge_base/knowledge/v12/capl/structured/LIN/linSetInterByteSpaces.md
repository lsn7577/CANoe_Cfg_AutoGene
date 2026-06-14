# linSetInterByteSpaces

> Category: `LIN` | Type: `function`

## Syntax

```c
dword linSetInterByteSpaces(dword arrayOfSixteenthBits[])
```

## Description

With the first function it is possible to set the inter-byte spaces [in bit times] for all data byte fields of all published frames (except for diagnostic frame 0x3D) of the calling LIN Slave node.

With the second function it is possible to set the inter-byte spaces [in bit times] for all data byte fields of a specified frame.

Inter-byte space is the period between the end of the stop bit of the preceding byte and the start bit of the following byte.

By default the inter-byte space between all byte fields is 0.

## Return Values

On success, a value unequal to zero, otherwise zero.

## Example

```c
on key 's'
{
int index;
dword arrayOfSixteenthBits[9];
linFrame MotorControl frameMotorControl;
for (index=0; index < 9; ++index)
{
if (index <= frameMotorControl.DLC+1) {
// for all valid data bytes and checksum byte set 
 inter-byte space to 2 bit times
arrayOfSixteenthBits[index] = 32; 
}
else {
// initialize unused array elements
arrayOfSixteenthBits[index] = 0;
}
}
if (linSetInterByteSpaces(0x33, arrayOfSixteenthBits) 
 != 0) {
// the inter-byte spaces successfully set
...
}
}
```

## Availability

| Since Version |
|---|
