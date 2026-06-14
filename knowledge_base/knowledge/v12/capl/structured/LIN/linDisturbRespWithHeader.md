# linDisturbRespWithHeader

> Category: `LIN` | Type: `function`

## Syntax

```c
dword linDisturbRespWithHeader(long disturbedFrameId, dword byteIndex, dword bitIndex, long disturbingFrameId);
```

## Description

Configures the LIN hardware to disturb the specified response with a new header (id=<disturbanceHeaderID>).

## Return Values

On success, a value unequal to zero, otherwise zero.

## Availability

| Since Version |
|---|
