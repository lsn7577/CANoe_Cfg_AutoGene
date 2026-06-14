# EthReceivePacket

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long EthReceivePacket( char *onPacketCallback );
```

## Description

Use this function to register a CAPL callback function to receive Ethernet packets. The callback has a packet handle as parameter and the functions to access the tokens can be used. The EthGetThis-functions can be used to access the payload of the highest interpretable protocol.

The callback must have the following signature:

The difference to EthReceiveRawPacket is, that the callback function gets a packet handle as parameter and the EthGetThis-Functions access the payload of the highest protocol instead the raw Ethernet data.

## Example

Node System - PreStart in CAPL Browser

Node Callback Function in CAPL Browser

```c
on preStart
{
  EthReceivePacket( "OnEthPacket");
}
void OnEthPacket( LONG channel, LONG dir, LONG packet )
{
  BYTE rx_data[100];
  LONG rx_length;

  // get the payload of the packet
  rx_length = EthGetThisData( 0, elCount(rx_data), rx_data );

  // do something with rx_data
}
```

## Availability

| Up to Version |
|---|
