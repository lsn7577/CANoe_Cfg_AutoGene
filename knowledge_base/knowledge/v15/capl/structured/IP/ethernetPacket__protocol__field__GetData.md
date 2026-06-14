# ethernetPacket::protocol::field::GetData

> Category: `IP` | Type: `method`

## Syntax

```c
word ethernetPacket.<protocol>.<field>.GetData( word offset, char[] dest, word length ); // from 1
word ethernetPacket.<protocol>.<field>.GetData( word offset, byte[] dest, word length ); // form 2
word ethernetPacket.<protocol>.<field>.GetData( word offset, struct * dest ); // form 3
word ethernetPacket.<protocol>.<field>.GetData( word offset, sysvarStruct dest ); // from4
```

## Description

Gets data of a protocol field within an Ethernet packet.

The data is copied to a destination buffer of the specified type. If the buffer is too small, the data is truncated.

If specified length is greater than available data, only the available data is copied to dest and the number of copied bytes is returned.

If <protocol>.<field> is not available in the packet, 0 is returned.

The method is only available for protocol fields, which are not of type integer.

## Parameters

| Name | Description |
|---|---|
| dest | Buffer where the data is copied to. |
| length | Number of bytes to copy. |
| offset | Byte offset in the payload where it starts to copy data. |

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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 11.0 SP3 | 11.0 SP3 | 13.0 | — | — | 3.0 SP3 |
| Restricted To | Ethernet | Ethernet | Ethernet | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
