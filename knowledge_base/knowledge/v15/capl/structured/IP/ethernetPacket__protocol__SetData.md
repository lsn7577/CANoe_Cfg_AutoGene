# ethernetPacket::protocol::SetData

> Category: `IP` | Type: `method`

## Syntax

```c
word ethernetPacket.<protocol>.SetData( word offset, char[]data, word length ); // form 1
word ethernetPacket.<protocol>.SetData( word offset, byte[]data, word length ); // form 2
word ethernetPacket.<protocol>.SetData( word offset, struct * data); // form 3
word ethernetPacket.<protocol>.SetData( word offset, sysvarStruct data); // form 4
word ethernetPacket.<protocol>.SetData( char[]data, word length ); // form 5
word ethernetPacket.<protocol>.SetData( byte[]data, word length ); // form 6
word ethernetPacket.<protocol>.SetData( struct * data); form // 7
word ethernetPacket.<protocol>.SetData( sysvarStruct data); form // 8
```

## Description

Sets payload data of a protocol within an Ethernet packet.

If <protocol> is not available in the packet, no data is set and 0 is returned.

For form 1-4 (with parameter offset)

If the data is greater than the length of the Ethernet packet, the Ethernet packet is enlarged. If data is smaller as the current length of the payload the length is not changed.

For form 5-8 (without parameter offset)

The length of the data is resized to the given length of the new data.

## Parameters

| Name | Description |
|---|---|
| data | Buffer where the data is copied from. |
| length | Number of bytes to copy to the protocol payload. |
| offset | Byte offset in the payload where it starts to copy data. |

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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 11.0 SP3: form 1-4 12.0: form 5-8 | 11.0 SP3: form 1-4 12: form 5-8 | 13.0 | — | — | 3.0 SP3: form 1-4 4.0: form 5-8 |
| Restricted To | Ethernet | Ethernet | Ethernet | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
