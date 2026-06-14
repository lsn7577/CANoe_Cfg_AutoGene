# AfdxIsPacketValid

> Category: `ADFX` | Type: `function`

## Syntax

```c
long AfdxIsPacketValid( long packet );
```

## Description

This function checks, if a received packet has a protocol error. Packets with a protocol error are marked with an error icon in the Trace Window.

## Example

Node System - PreStart in CAPL Browser

Node Callback Function in CAPL Browser

```c
on preStart
{
  AfdxRegisterReceiveCallback ( "OnAfdxPacket");
}
void OnAfdxPacket( long dir, long line, int64 time, long bag, long afdxFlags, long packet )
{
  if (AfdxIsPacketValid(handle) != 0)
  {
    write( "Receive packet with protocol error" );
  }
}
```

## Availability

| Since Version |
|---|
