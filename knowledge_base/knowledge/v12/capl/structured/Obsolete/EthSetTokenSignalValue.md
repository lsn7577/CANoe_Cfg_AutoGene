# EthSetTokenSignalValue

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long EthSetTokenSignalValue( long packet, dbSignal signal, double physValue ); // form 1
```

## Description

Both functions assume that the packet’s payload is described in the database. They writes the signal’s value into the packet’s payload.

Form 2 assumes the passed signal is the first element of an array. The value will be written to the element’s position.

The caller must check itself if the packet’s payload is described by the signal’s database frame.

## Example

```c
LONG packetHandle;
CHAR error[100];

// create packet
packetHandle = EthInitPacket("udp");

if (EthGetLastError() == 0)
{
  // set protocol fields
  EthSetTokenInt( packetHandle, "ipv4", "source", 0xC0A80001 ); // 192.168.0.1
  EthSetTokenInt( packetHandle, "ipv4", "destination", 0xFFFFFFFF ); // 255.255.255.255
  EthSetTokenInt( packetHandle, "udp", "source", 23 );
  EthSetTokenInt( packetHandle, "udp", "destination", 23 ); 
  //this example assumes that a udp payload with destination port 23 is described by the database frame EngineInfo

  // set UDP payload
  EthResizeToken( packetHandle, "udp", "data", EngineInfo.DLC*8 /*bits*/ );
 EthSetTokenSignalValue( packetHandle, EngineInfo::CoolantTemperature, 77.0 );

  // Complete and send packet
  EthCompletePacket( packetHandle );
  EthOutputPacket( packetHandle );

  // release packet
  EthReleasePacket( packetHandle );
}
else
{
  EthGetLastErrorText( elCount(error), error );
  write("Error: %s", error );
}
```

## Availability

| Up to Version |
|---|
