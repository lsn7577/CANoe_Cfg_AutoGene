# linInvertHeaderBitEx

> Category: `LIN` | Type: `function`

## Syntax

```c
dword linInvertHeaderBitEx(dword byteIndex, dword bitIndex, dword bitOffsetInSixteenthBits, dword distLengthInSixteenthBits, dword level)
```

## Description

Inverts the specified number of 1/16th bits at the specified position in the next LIN header.

Partial bit disturbances require the activation of the flash mode in order to get the edges of the disturbance fast enough. Call linActivateFlashMode for that purpose.

## Return Values

On success, a value unequal to zero, otherwise zero.

## Example

```c
on key 'i'
{
   if (0!=linInvertHeaderBitEx(0, 0, 8, 8, 0))
   {
   // for the next LIN header invert the second half of the first bit (it’s the recessive one) of the Sync byte
   }
}
```

## Availability

| Since Version |
|---|
