# LINtp_GetRxData

> Category: `LIN` | Type: `function`

## Syntax

```c
void LINtp_GetRxData(byte data[], long size);
```

## Description

Retrieve data bytes received.

## Return Values

—

## Example

```c
LINtp_DataInd(long count, DWORD nad)
{
  byte rxBuffer[4096];
  LINtp_GetRxData(rxBuffer, count);
  write( "received <%02x ...> from/for node %02x"
  , rxBuffer[0], nad);
}
```

## Availability

| Since Version |
|---|
