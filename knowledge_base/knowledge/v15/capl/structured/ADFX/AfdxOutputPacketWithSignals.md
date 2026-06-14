# AfdxOutputPacketWithSignals

> Category: `ADFX` | Type: `function`

## Syntax

```c
long AfdxOutputPacketWithSignals( long packet );
```

## Description

Sends a message and automatically updates the payload with the current Tx-signal values of the SignalServer.

## Parameters

| Name | Description |
|---|---|
| 0 |  |
| other value | error code |

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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2 SP3 | — | — | — | — |
| Restricted To | — | AFDX | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
