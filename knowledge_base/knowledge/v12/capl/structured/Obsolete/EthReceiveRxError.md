# EthReceiveRxError

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long EthReceiveRxError(char *callback );
```

## Description

Use this function to register a CAPL callback function to receive corrupt Ethernet packets. The callback function is called, if a corrupt packet is received.

The callback must have the following signature:

## Example

Node System - PreStart in CAPL Browser

Node Callback Function in CAPL Browser

```c
on preStart
{
  EthReceiveRxError( "OnCorruptEthernetPacket" );
}
void OnCorruptEthernetPacket( LONG channel, LONG errorCode, LONG packetLength )
{
  BYTE srcMac[6];
  // get source MAC address of the corrupt packet
  EthGetThisData( 6, elCount(srcMac), srcMac );
  write("Corrupt packet received from MAC address %X:%X:%X:%X:%X:%X with error code %d", srcMac[0], srcMac[1], srcMac[2], srcMac[3], srcMac[4], srcMac[5], errorCode);
}
```

## Availability

| Up to Version |
|---|
