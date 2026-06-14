# ethernetPacket::protocol::GetData

> Category: `IP` | Type: `function`

## Syntax

```c
word ethernetPacket.<protocol>.GetData( word offset, char[] dest, word length );
```

## Description

Gets payload data of a protocol within an Ethernet packet.

The data is copied to a destination buffer of the specified type. If the buffer is too small, the data is truncated.

If specified length is greater than available data, only the available data is copied to dest and the number of copied bytes is returned.

If <protocol> is not available in the packet, 0 is returned.

## Return Values

Number of bytes copied to destination.

## Example

```c
on ethernetPacket *
{
  _align(1) struct MyData
  {
    long value1;
    long value2;
  } buffer;

  if ((this.udp.IsAvailable()) && (this.udp.destination == 0xF123))
  {
    if (this.GetData( 0, buffer, bufferLength  ) == > 0)
    {
      write( "Value1=%d, Value2=%d", buffer.value1, buffer.value2 );
    }
  }
}
```

## Availability

| Since Version |
|---|
