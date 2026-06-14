# linSetBreakLength

> Category: `LIN` | Type: `function`

## Syntax

```c
dword linSetBreakLength(dword syncBreakLen, dword syncDelLen)
```

## Description

With this function it is possible to change length of break/synch symbol parts. Particularly the length of its synch break (dominant bits) and its synch delimiter (recessive bits).

The version using float parameters allows setting the break and delimiter lengths in increments of 1/16th bits, but the unit still is bit times (i.e. linSetBreakLength(14.5, 2.5) will set a break length of 14 8/16th bit times and a delimiter length of 2 8/16th bit times). Note that setting non-integer break and delimiter lengths is not supported by every hardware.

When LIN hardware is not in Master mode calling this function will have no effect.

## Return Values

On success, a value unequal to zero, otherwise zero.

## Availability

| Since Version |
|---|
