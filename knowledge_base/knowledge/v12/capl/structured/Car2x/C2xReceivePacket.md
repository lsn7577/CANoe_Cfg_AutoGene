# C2xReceivePacket

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xReceivePacket( char *onPacketCallback );
```

## Description

Use this function to register a CAPL callback to receive WLAN packets. The callback has a packet handle as parameter and the functions to access the tokens can be used. The C2xGetThis-functions can be used to access the payload of the highest interpretable protocol.

The callback must have the following signature:

## Return Values

0 or error code

## Example

Node System - PreStart in CAPL Browser

Node Callback Function in CAPL Browser

```c
on preStart
{
 C2xReceivePacket( "OnC2xPacket");
}
void OnC2xPacket( long channel, long dir, long radioChannel, long signalStrength, long signalQuality, long packet )
{
  byte rx_data[1500];
  byte rx_packet[1500];
  long rx_length;
  long rx_headerLength;

  rx_headerLength = C2xGetTokenData(packet, "wlan", "header", elCount(rx_packet), rx_packet);
  // without Ethernet header
  rx_length = C2xGetTokenData(packet, "eth", "data", elCount(rx_data), rx_data);
  write ("rx_headerLength: %d", rx_headerLength);
  write ("rx_dataLength: %d", rx_length);
  memcpy_off(rx_packet, rx_headerLength, rx_data, 0, rx_length);
  rx_length += rx_headerLength;
  // Always use rx_length to access rx_packet!
  write ("rx_length: %d", rx_length);
}
```

## Availability

| Since Version |
|---|
