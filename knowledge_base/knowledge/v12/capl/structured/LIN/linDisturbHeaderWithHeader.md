# linDisturbHeaderWithHeader

> Category: `LIN` | Type: `function`

## Syntax

```c
dword linDisturbHeaderWithHeader(dword byteIndex, dword bitIndex, long disturbingFrameId);
```

## Description

Configures the LIN hardware to disturb the next header with a new header (id=<disturbanceHeaderID>).

## Return Values

On success, a value unequal to zero, otherwise zero.

## Availability

| Since Version |
|---|
