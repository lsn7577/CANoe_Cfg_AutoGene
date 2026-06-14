# AfdxOutputPacketWithSignals

> Category: `ADFX` | Type: `function`

## Syntax

```c
long AfdxOutputPacketWithSignals( long packet );
```

## Description

Sends a message and automatically updates the payload with the current Tx-signal values of the SignalServer.

Note: There are conceptually two distinct ways to apply send specific signal values:

Note: During PreStart-phase the SignalServer is not yet initialized

## Example

```c
variables
{
  long packet;
}

on preStart
{
  // initialize the frame header, don’t care for the payload
  packet  = AfdxInitPacket(0, "TESTMSG_ALLTYPES", 0 );
  if (packet == 0)
  {
    write( "<%NODE_NAME%> AfdxInitPacket failed due to:%s", errTxt );
  }
}

on key ‚1‘
{
  // update payload with current tx-signal values from
  // signal server and then send the frame out
  AfdxOutputPacketWithSignals(packet);
}
```

## Availability

| Since Version |
|---|
