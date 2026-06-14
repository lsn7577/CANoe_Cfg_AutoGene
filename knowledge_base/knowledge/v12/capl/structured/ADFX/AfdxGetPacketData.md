# AfdxGetPacketData

> Category: `ADFX` | Type: `function`

## Syntax

```c
long AfdxGetPacketData( long packet, long offset, long length, byte buffer[] );
```

## Description

This function copies the packet content (including protocol header and payload) to a local buffer.

## Return Values

number of copied data bytes
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

| Since Version |
|---|
