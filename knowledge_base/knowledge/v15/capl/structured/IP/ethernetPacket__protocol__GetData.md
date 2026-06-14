# ethernetPacket::protocol::GetData

> Category: `IP` | Type: `method`

## Syntax

```c
word ethernetPacket.<protocol>.GetData( word offset, char[] dest, word length ); // from 1
word ethernetPacket.<protocol>.GetData( word offset, byte[] dest, word length ); // from 2
word ethernetPacket.<protocol>.GetData( word offset, struct * dest ); // from 3
word ethernetPacket.<protocol>.GetData( word offset, sysvarStruct dest ); // from 4
```

## Description

Gets payload data of a protocol within an Ethernet packet.

The data is copied to a destination buffer of the specified type. If the buffer is too small, the data is truncated.

If specified length is greater than available data, only the available data is copied to dest and the number of copied bytes is returned.

If <protocol> is not available in the packet, 0 is returned.

## Parameters

| Name | Description |
|---|---|
| dest | buffer where the data is copied to. |
| length | Number of bytes to copy. |
| offset | Byte offset in the payload where it starts to copy data. |

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
    if (this.GetData( 0, buffer ) == > 0)
    {
      write( "Value1=%d, Value2=%d", buffer.value1, buffer.value2 );
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
