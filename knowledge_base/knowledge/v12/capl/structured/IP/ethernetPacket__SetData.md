# ethernetPacket::SetData

> Category: `IP` | Type: `function`

## Syntax

```c
word ethernetPacket.SetData(word offset, char source[], word length); // form 1
```

## Description

Copies bytes from a char array, byte array, CAPL struct or system variable struct to the data of an Ethernet packet.

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

| Since Version |
|---|
