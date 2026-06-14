# ethernetPacket::SetData

> Category: `IP` | Type: `method`

## Syntax

```c
Syntax;
```

## Description

Copies bytes from a char array, byte array, CAPL struct or system variable struct to the data of an Ethernet packet.

## Parameters

| Name | Description |
|---|---|
| offset | Byte offset of the data in the ethernetPacket. Offset 0 is the byte directly after the Ethertype. |
| source | Source where the data is copied from. |
| length | Number of bytes to copy. |

## Return Values

Number of bytes copied to the ethernetPacket.

## Example

```c
on key '1'
{
  _align(1) struct MyMsgLayout
  {
    word  valueA;
    dword valueB;
  };

  ethernetPacket pkt;
  struct MyMsgLayout myData;

  myData.valueA = 1;
  myData.valueB = 2;

  pkt.source      = ethGetMacAddressAsNumber( "20:00:00:00:00:01" );
  pkt.destination = ethGetMacAddressAsNumber( "FF:FF:FF:FF:FF:FF" );
  pkt.type        = 0xF123; // proprietary Ethertype
  pkt.Length      = __size_of(struct MyMsgLayout);
  pkt.SetData( 0, myData );

  output( pkt );
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 10.0 | 10.0 | 13.0 | — | — | 2.2 |
| Restricted To | Ethernet | Ethernet | Ethernet | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
