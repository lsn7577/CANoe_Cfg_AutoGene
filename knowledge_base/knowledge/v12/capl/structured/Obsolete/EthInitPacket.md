# EthInitPacket

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long EthInitPacket( ); // form 1
```

## Description

This function creates a new Ethernet packet. Other functions can access to the newly created packet with the returned handle.

Protocol fields that are marked as InitProtocol in the protocol description are initialized.

## Return Values

handle of the created packet or 0
With EthGetLastError you can check if the function has been processed successfully.

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

  // set UDP payload
  EthResizeToken( packetHandle, "udp", "data", 5*8 /*bits*/ );
  EthSetTokenData( packetHandle, "udp", "data", 5, "Hello" );

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
