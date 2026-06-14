# EthConfigurePacketGenerator

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long EthConfigurePacketGenerator( long packet, dword transmissionRate );
```

## Description

This function configures the Ethernet packet that can be sent continuously by the hardware.

To start the transmission you have to call EthStartPacketGenerator.

## Return Values

0 or error code

## Example

```c
on start
{
  LONG packetHandle;
  char error[255];

  // create packet and start packet generator
  packetHandle = EthInitPacket("udp");

  if (EthGetLastError() == 0)
  {
  // set protocol fields
  EthSetTokenInt( packetHandle, "ipv4", "source", 0xC0A80001 ); // 192.168.0.1
  EthSetTokenInt( packetHandle, "ipv4", "destination", 0xFFFFFFFF ); // 255.255.255.255
  EthSetTokenInt( packetHandle, "udp", "source", 23 );
  EthSetTokenInt( packetHandle, "udp", "destination", 23 );

  // set UDP payload
  EthResizeToken( packetHandle, "udp", "data", 12*8 ); /*8 byte text, 4 byte   counter*/
  EthSetTokenData( packetHandle, "udp", "data", 5, "Counter " );

  // complete
  EthCompletePacket( packetHandle );

  // configure generator
 EthConfigurePacketGenerator(packetHandle, 10000, 38); //10000 fps

  // release packet
  EthReleasePacket( packetHandle );
  }
  else
  {
  EthGetLastErrorText( elCount(error), error );
  write("Error: %s", error );
  }
}

on key '1'
{
  // start generator
 EthStartPacketGenerator(1000000); //one million packets, should run about 100s
}

on key '2'
{
  // stop generator before it is finished
 EthStopPacketGenerator();
}
```

## Availability

| Up to Version |
|---|
