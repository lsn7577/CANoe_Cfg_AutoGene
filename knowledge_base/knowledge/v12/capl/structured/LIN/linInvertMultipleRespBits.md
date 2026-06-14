# linInvertMultipleRespBits

> Category: `LIN` | Type: `function`

## Syntax

```c
dword linInvertMultipleRespBit(long frameID, dword byteIndices[],dword bitIndices[],dword numberOfDisturbedBits[], dword levels[], dword arrSize)
```

## Description

Inverts the multiple bits in specified locations in the next LIN header.

Please note hardware-related restrictions.

## Return Values

On success, a value unequal to zero, otherwise zero.

## Example

```c
// Invert response bits on keyboard event
on key 'i'
{
   dword byteIndices[2] = { 1, 5 };
   dword bitIndices[2]  =  { 0, 1 
 };
   dword numberOfDisturbedBits[2] = { 1, 2 };
   dword levels[2] = { 0, 1 };
   ...
   // Invert first bit 0 of byte 1 to dominant and bits 1 and 2
   // (numberOfDisturbedBits[1] is 2) of byte 5 to recessive
   linInvertMultipleRespBits(0x33, byteIndices, bitIndices, numberOfDisturbedBits, levels, 2);
...
}
```

## Availability

| Since Version |
|---|
