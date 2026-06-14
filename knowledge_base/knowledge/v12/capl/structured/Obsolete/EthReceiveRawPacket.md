# EthReceiveRawPacket

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long EthReceiveRawPacket( long flags, byte srcMacAddress[6], byte dstMacAddress[6], long ethernetType, char *callback );
```

## Description

Use this function to register a CAPL function to receive Ethernet packets. The callback function is called, if a packet with the specified MAC addresses and Ethernet type is received. Use the flags to ignore the Ethernet type or the MAC address, e.g. flag = 7 receives all packets.

The callback must have the following signature:

## Example

Node System - PreStart in CAPL Browser

Node Callback Function in CAPL Browser

```c
on preStart
{
  BYTE emptyMacAddress[6] = { 0x00,0x00,0x00,0x00,0x00, 0x00};
  EthReceiveRawPacket( 0x7, emptyMacAddress, emptyMacAddress, 0x0000, "OnEthRawPacket" );
}
void OnEthRawPacket( LONG channel, LONG dir, LONG packetLength )
{
  BYTE rx_data[100];
  LONG rx_length;

  // get the raw data of the receive packet
  rx_length = EthGetThisData( 0, elCount(rx_data), rx_data );

  // do something with rx_data
}
```

## Availability

| Up to Version |
|---|
