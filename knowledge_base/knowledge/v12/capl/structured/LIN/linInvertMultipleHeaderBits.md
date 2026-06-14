# linInvertMultipleHeaderBits

> Category: `LIN` | Type: `function`

## Syntax

```c
dword linInvertMultipleHeaderBits(dword byteIndices[],dword bitIndices[],dword numberOfDisturbedBits[],dword levels[],dword arrSize)
```

## Description

Inverts the multiple bits in specified locations in the next LIN header.

Some driver versions only support inverting multiple (consecutive) bits in one position (arrSize == 1).

## Return Values

On success, a value unequal to zero, otherwise zero.

## Example

```c
on key 'i'
{
   dword byteIndices[2] = { 0, 1}; // invert in sync field and in id-byte
   dword bitIndices[2]   = { 0, 0 }; // invert the first data bits in each byte
   dword numberOfDisturbedBits[2] = { 1, 2 }; // invert 1 bit in sync field, 2 bits in id-byte
   ,dword levels[2] = { 0, 1 }; // push sync field bit to dominant, id-byte bits to recessive
   if (0!=linInvertMultipleHeaderBits(byteIndices, bitIndices, numberOfDisturbedBits, levels, 2))
   {
   }
}
```

## Availability

| Since Version |
|---|
