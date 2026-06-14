# EthSetTokenInt64

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long EthSetTokenInt64( long packet, char protocolDesignatorl[], char tokenDesignator[], int64 value ); // form 1
```

## Description

The function sets the integer value of a token.

Form 2 with byte offset sets a part of the token data as integer.

## Return Values

0 or error code

## Example

```c
long packetHandle;
char error[100];

int64 srcMacId = 0x5826C8FD2421LL;
int64 dstMacId = 0xFFFFFFFFFFFFLL;

// create packet
packetHandle = EthInitPacket("eth");

if (EthGetLastError() == 0)
{
  // set MAC address
  EthSetTokenInt64( packetHandle, "eth", "source"     , srcMacId );
  EthSetTokenInt64( packetHandle, "eth", "destination", dstMacId );

  if (EthInitProtocol( packetHandle, "udp" ) == 0)
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
    }

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
