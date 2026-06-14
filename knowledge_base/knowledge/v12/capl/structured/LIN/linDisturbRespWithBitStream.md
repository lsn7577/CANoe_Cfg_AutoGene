# linDisturbRespWithBitStream

> Category: `LIN` | Type: `function`

## Syntax

```c
dword linDisturbRespWithBitStream(long disturbedFrameId, dword byteIndex, dword bitIndex, byte bitStream[], dword numberOfBits, dword timeoutPrevention);
```

## Description

Configures the LIN hardware to disturb the specified response with a bit stream.

## Return Values

On success, a value unequal to zero, otherwise zero.

## Availability

| Since Version |
|---|
