# linSetValidBreakLimits

> Category: `LIN` | Type: `function`

## Syntax

```c
dword linSetValidBreakLimits(dword breakMin16thBits, dword breakMax16thBits, dword delMin16thBits, dword delMax16thBits)
```

## Description

Sets limits for the accepted sync break and delimiter lengths. Any sync break and delimiter outside of this range is considered invalid, resulting in a receive error. Note that this function does not change the current sync break and delimiter length sent by a simulated master. This function can also be called in slave mode to test an external master.

This function does not change the header length restrictions of 47.6 bit times for LIN 2.x and 49 bit times for LIN 1.x. This means that a header can still be invalid even if the modified sync break and delimiter limits are met.

## Return Values

On success, a value unequal to zero, otherwise zero.

## Availability

| Since Version |
|---|
