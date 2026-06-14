# linDisturbHeaderWithVariableBitStream

> Category: `LIN` | Type: `function`

## Syntax

```c
dword linDisturbHeaderWithVariableBitStream(dword byteIndex, dword bitIndex, byte dataBuffer[], int64 lengthInNS[], dword numberOfBits, dword roundUp, dword timeoutPrevention);
```

## Description

Configures the LIN hardware to disturb the next header with a variable bit stream.

## Return Values

On success, a value unequal to zero, otherwise zero.

## Availability

| Since Version |
|---|
