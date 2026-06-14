# ethernetPacket::protocol::field::GetData

> Category: `IP` | Type: `function`

## Syntax

```c
word ethernetPacket.<protocol>.<field>.GetData( word offset, char[] dest, word length );
```

## Description

Gets data of a protocol field within an Ethernet packet.

The data is copied to a destination buffer of the specified type. If the buffer is too small, the data is truncated.

If specified length is greater than available data, only the available data is copied to dest and the number of copied bytes is returned.

If <protocol>.<field> is not available in the packet, 0 is returned.

The method is only available for protocol fields, which are not of type integer.

## Return Values

Number of bytes copied to dest.

## Example

```c
on ethernetPacket *
{
  if (this.ipv6.IsAvailable())
  {
    byte ipv6AddrData[16];
    long ipv6AddrDataLength;
    char ipv6AddrStr[40];

    ipv6AddrDataLength = this.ipv6.source.GetData( 0, ipv6AddrData, elcount(ipv6AddrData) );

    if (ipv6AddrDataLength == 16)
    {
      ipGetAddressAsString( ipv6AddrData, ipv6AddrStr, elcount      (ipv6AddrStr) );
      writeLineEx( kWritSink, 0, "Received IPv6 packet from %s", ipv6AddrStr );
    }
  }
}
```

## Availability

| Since Version |
|---|
