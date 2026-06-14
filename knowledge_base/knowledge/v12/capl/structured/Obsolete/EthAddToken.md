# EthAddToken

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long EthAddToken( long packet, char protocolDesignator[], char tokenDesignator[] );
```

## Description

The function adds an additional token at the end of a protocol header or at a specific position (for details see protocol help).

## Return Values

0 or error code

## Example

```c
LONG packetHandle;
BYTE snameSize = 64;
BYTE fileSize  = 128;
BYTE data[4];

// create packet
packetHandle = EthInitPacket( "ipv4" );

// init dhcpv4 protocol
EthInitProtocol( packetHandle, "dhcpv4" );

// add tokens
EthAddToken( packetHandle, "dhcpv4", "serverName" );
EthAddToken( packetHandle, "dhcpv4", "file" );
EthAddToken( packetHandle, "dhcpv4", "magicCookie" );
EthAddToken(packetHandle, "dhcpv4", "option53" ) ;
EthAddToken( packetHandle, "dhcpv4", "option55" ) ;
EthAddToken( packetHandle, "dhcpv4", "option50" ) ;
EthAddToken( packetHandle, "dhcpv4", "option0" ) ;

// set value of option 53
data[0] = 3;
EthSetTokenData( packetHandle, "dhcpv4", "option55.data", 1, data );

// set IP address of option 55
data[0] = 10;
data[1] = 15;
data[2] = 16;
data[3] = 17;
EthSetTokenData( packetHandle, "dhcpv4", "option50.data", 4, data );

// complete and send packet
EthCompletePacket( packetHandle );
EthOutputPacket( packetHandle );

// remove a token
EthRemoveToken( packetHandle, "dhcpv4", "option50" ) ;

// complete and send packet again
EthCompletePacket( packetHandle );
EthOutputPacket( packetHandle );

// release packet
EthReleasePacket( packetHandle );
```

## Availability

| Up to Version |
|---|
