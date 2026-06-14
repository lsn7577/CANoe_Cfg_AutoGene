# C2xSetTokenString

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xSetTokenString( long packet, char protocolDesignator[], char tokenDesignator[], char data[] );
```

## Description

This function copies the string value to the token without terminating \0.

## Return Values

0 or error code

## Example

```c
long packetHandle;

// create packet
packetHandle = C2xInitPacket( "geo_cnh" );

// set geo_cnh payload
C2xResizeToken( packetHandle, "geo_cnh", "data", 5*8 /*bits*/ );
C2xSetTokenString( packetHandle, "geo_cnh", "data", "Hello" );

// complete and send packet
C2xCompletePacket( packetHandle );
C2xOutputPacket( packetHandle );

// release packet
C2xReleasePacket( packetHandle );
```

## Availability

| Since Version |
|---|
