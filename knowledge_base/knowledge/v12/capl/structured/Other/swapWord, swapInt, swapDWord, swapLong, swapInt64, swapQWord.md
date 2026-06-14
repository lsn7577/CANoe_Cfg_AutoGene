# swapWord, swapInt, swapDWord, swapLong, swapInt64, swapQWord

> Category: `Other` | Type: `function`

## Syntax

```c
word swapWord(word x); // form 1
```

## Description

Swaps bytes of parameters. CAPL arithmetics follows the "little-endian-format" (Intel). The swap-functions serve for swapping bytes for the transition to and from the "big-endian-format" (Motorola).

## Return Values

Value with swapped bytes.

## Example

```c
bigEndian = swapInt(1234); // create constant 1234 for Motorola processors
```

## Availability

| Since Version |
|---|
