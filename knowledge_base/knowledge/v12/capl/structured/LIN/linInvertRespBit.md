# linInvertRespBit

> Category: `LIN` | Type: `function`

## Syntax

```c
dword linInvertRespBit (long frameID, dword byteIndex, dword bitIndex)
```

## Description

This function inverts the specified bit when the next bus event for the specified ID occurs, provided that the bus event contains the specified data byte.

## Return Values

On success, a value unequal to zero, otherwise zero.

## Example

Invert response bits on keyboard event

```c
on key 'i'
{
...
// Invert first bit of byte field 8 for LIN frame 
 with ID=0x33
linInvertRespBit(0x33, 7, 0);
...
// Invert bit 7 of checksum byte field for LIN frame 
 with ID=0x33
linInvertRespBit(0x33, 8, 6);
...
// Invert stop bit of byte field 8 for LIN frame 
 with ID=0x33
linInvertRespBit(0x33, 7, 8);
...
}
```

## Availability

| Since Version |
|---|
