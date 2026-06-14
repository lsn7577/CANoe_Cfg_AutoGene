# linGetFallingEdgesOfDisturbedByte

> Category: `LIN` | Type: `function`

## Syntax

```c
dword linGetFallingEdgesOfDisturbedByte(int64 fallingEdges[])
```

## Description

With this function it is possible to retrieve time stamps of all falling edges in the disturbed byte or in the pseudo-byte caused by the last bit inversion.

Note, that prior to calling this function the measurement of the falling edges has to be activated and the bit inversion has to be executed (see linInvertRespBit, linInvertHeaderBit)

## Return Values

On successful request returns 1, otherwise 0.

## Availability

| Since Version |
|---|
