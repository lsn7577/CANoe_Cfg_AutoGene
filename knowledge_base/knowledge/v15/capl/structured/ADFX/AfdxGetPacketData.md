# AfdxGetPacketData

> Category: `ADFX` | Type: `function`

## Syntax

```c
long AfdxGetPacketData( long packet, long offset, long length, byte buffer[] );
```

## Description

This function copies the packet content (including protocol header and payload) to a local buffer.

## Parameters

| Name | Description |
|---|---|
| packet | Handle of the message that has been created with AfdxInitPacket or from within a callback. |
| offset | This is the offset from the beginning of the Ethernet frame. If this is 0, data is copied starting at byte 0 frame (destination MAC address). |
| length | This is the number of bytes to be copied from Ethernet frame to the specified buffer. |
| buffer | Buffer in which the requested data are copied. Make sure that the size of the buffer is at least length bytes. |

## Return Values

Number of copied data bytes.
With AfdxGetLastError you can check if the function has been processed successfully.

## Example

```c
void OnAfdxRawPacket( long dir, long line, int64 timestamp, long bag, long afdxFlags, long packet )
{
  byte rawdata[8330];
  long packetLength;
  long rxLength;
  long packetHandle;
  long msgId;

  if (afdxFlags & packetIsReassembled) {
    write( "<%NODE_NAME%> OnAfdxRawPacket: packet is JumboPacket --> skip" );
    return; // don't transfer Jumbo-frames
  }
  if (afdxFlags & packetIsFragmented) {
    write( "<%NODE_NAME%> OnAfdxRawPacket: packet is fragmented" );
  }

  rxLength = AfdxGetPacketData( packet, 0 , elCount(rawdata), rawdata );
  write( "<%NODE_NAME%> AfdxGetPacketData has length: %d", rxLength );

  if (rxLength==0) {
    write ("<%NODE_NAME%> Error empty packet-length at timestamp %u", timestamp / 1000);
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.1 | — | — | — | — |
| Restricted To | — | AFDX | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
