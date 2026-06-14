# linIsBitStreamBusy

> Category: `LIN` | Type: `function`

## Syntax

```c
dword linIsBitStreamBusy(); // form 1
```

## Description

Queries the current LIN bit stream sending status.

## Return Values

Returns 1 if a bit stream is currently being sent, otherwise 0.

## Example

```c
// Make sure that there is no bit stream sending active before a new transmission is started

if (linIsBitStreamBusy() == 0)

{
  linSendBitStream(data, numberOfBits);
}
```

## Availability

| Since Version |
|---|
