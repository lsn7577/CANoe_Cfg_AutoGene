# AfdxOutputPacketRaw

> Category: `ADFX` | Type: `function`

## Syntax

```c
long AfdxOutputPacketRaw( long packet );
```

## Description

The specified AFDX message is transmitted without considering the internal AFDX software stack.

This call is equivalent to AfdxOutputPacket( packet, SingleShot, NoIPFragmentation, NoAFDXVLScheduling, NoAFDXSeqNoManagement, MACIFRelated ).

## Return Values

0 or error code

## Example

Node System - preStart in CAPL Browser

Node Callback Function in CAPL Browser

```c
includes
{
  #include "AFDX/Utils.cin"
}
on preStart
{
  long result;
  result=AfdxRegisterReceiveCallback("OnAfdxRawPacket", BothDirections, NotDropped, EveryFrameAndPacket);
}
void OnAfdxRawPacket( long dir, long line, int64 timestamp, long bag, long afdxFlags, long packet )
{
  long packetHandle;

  if (afdxFlags & packetIsReassembled)
  {
    write( "<%NODE_NAME%> OnAfdxRawPacket  packet is JumboPacket --> skip" );
    return; // don't transfer Jumbo-frames
  }

  if (getBusContext() == gContextAfdx1)
  {
    setBusContext( gContextAfdx2 );
  }
  else
  {
    setBusContext( gContextAfdx1 );
  }

  packetHandle  = AfdxInitPacket( packet);
  if( packetHandle == 0) {
    write( "<%NODE_NAME%> AfdxInitPacket failed" );
    return;
  }

  // modify signals only if not a fragment
  if (!(packetIsFragmented & afdxFlags ))
  {
    // TBD
  }
  else
  {
    // must use direct byte access to manipulate
  }

  AfdxOutputPacketRaw( packetHandle );
  AfdxReleasePacket( packetHandle );
}
```

## Availability

| Since Version |
|---|
