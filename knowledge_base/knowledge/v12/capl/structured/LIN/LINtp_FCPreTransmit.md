# LINtp_FCPreTransmit

> Category: `LIN` | Type: `function`

## Syntax

```c
void LINtp_FCPreTransmit(byte fcData);
```

## Description

When the usage of FlowControl frames has been activated with LINtp_ActivateFCTransmission, each FlowControl frame is forwarded to this callback function before it is sent.

## Return Values

—

## Example

```c
void LINtp_FCPreTransmit( BYTE fcData[])
{
  write( "FlowControl to be sent: %02x %02x %02x %02x (%d byte)"
  , fcData[0] , fcData[1] , fcData[2] , fcData[3], elcount(fcdata));
}
```

## Availability

| Since Version |
|---|
