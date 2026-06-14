# EthSetTokenString

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long EthSetTokenString( long packet, char protocolDesignator[], char tokenDesignator[], char data[] );
```

## Description

The function copies the string value to the token without terminating "\0".

## Example

```c
LONG packetHandle;

// create packet
packetHandle = EthInitPacket( "udp" );

// set protocol fields
EthSetTokenInt( packetHandle, "ipv4", "source", 0xC0A80001 ); // 192.168.0.1
EthSetTokenInt( packetHandle, "ipv4", "destination", 0xFFFFFFFF ); // 255.255.255.255
EthSetTokenInt( packetHandle, "udp", "source", 23 );
EthSetTokenInt( packetHandle, "udp", "destination", 23 );

// set UDP payload
EthResizeToken( packetHandle, "udp", "data", 5*8 /*bits*/ );
EthSetTokenString( packetHandle, "udp", "data", "Hello" );

// Complete and send packet
EthCompletePacket( packetHandle );
EthOutputPacket( packetHandle );

// release packet
EthReleasePacket( packetHandle );
```

## Availability

| Up to Version |
|---|
