# linInvertHeaderBit

> Category: `LIN` | Type: `function`

## Syntax

```c
dword linInvertHeaderBit(dword byteIndex, dword bitIndex); // form 1
```

## Description

Inverts the specified bit in the next LIN header.

## Return Values

On success, a value unequal to zero, otherwise zero.

## Example

```c
on key 'i'
{
if (0!=linInvertHeaderBit(0, 0, 0))
{
// for the next LIN header invert first bit (it’s the recessive one) of the Sync byte
}
}
```

## Availability

| Since Version |
|---|
