# EthInitProtocol

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long EthInitProtocol( long packet, char protocolDesignator[] ); // form 1
```

## Description

The function initializes the protocol for a packet. If necessary further needed lower protocols are initialized, e.g. IPv4. Already initialized higher protocols are deleted.

Protocol fields that are marked as InitProtocol in the protocol overview are initialized.

## Return Values

0 or error code

## Example

```c
LONG packetHandle;

// create packet
packetHandle = EthInitPacket("ipv4");

// init UDP protocol
EthInitProtocol(packetHandle, "udp" );

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
```

## Availability

| Up to Version |
|---|
