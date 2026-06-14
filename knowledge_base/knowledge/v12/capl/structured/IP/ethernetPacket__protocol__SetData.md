# ethernetPacket::protocol::SetData

> Category: `IP` | Type: `function`

## Syntax

```c
word ethernetPacket.<protocol>.SetData( word offset, char[]data, word length ); // form 1
```

## Description

Sets payload data of a protocol within an Ethernet packet.

If <protocol> is not available in the packet, no data is set and 0 is returned.

For form 1-4 (with parameter offset)

If the data is greater than the length of the Ethernet packet, the Ethernet packet is enlarged. If data is smaller as the current length of the payload the length is not changed.

For form 5-8 (without parameter offset)

The length of the data is resized to the given length of the new data.

## Return Values

Number of bytes copied to the Ethernet packet.

## Example

```c
on key '1'
{
  ethernetPacket pkt;
 
  _align(1) struct MyData
  {
    long value1;
    long value2;
  } buffer;

  buffer.value1 = 1;
  buffer.value2 = 2;

  pkt.udp.Init();
  pkt.udp.SetData( 0, buffer );
  pkt.CompletePacket();
  output( pkt );
}
```

## Availability

| Since Version |
|---|
