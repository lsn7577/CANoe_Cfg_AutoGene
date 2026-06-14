# AfdxOutputPacketRaw

> Category: `ADFX` | Type: `function`

## Syntax

```c
long AfdxOutputPacketRaw( long packet );
```

## Description

The specified AFDX message is transmitted without considering the internal AFDX software stack.

This call is equivalent to AfdxOutputPacket( packet, SingleShot, NoIPFragmentation, NoAFDXVLScheduling, NoAFDXSeqNoManagement, MACIFRelated ).

## Parameters

| Name | Description |
|---|---|
| packet | handle of the message to send that has been created with AfdxInitPacket. |

## Example

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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0 | — | — | — | — |
| Restricted To | — | AFDX | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
