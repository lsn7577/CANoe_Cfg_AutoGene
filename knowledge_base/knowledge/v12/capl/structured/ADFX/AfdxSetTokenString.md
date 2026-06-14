# AfdxSetTokenString

> Category: `ADFX` | Type: `function`

## Syntax

```c
long AfdxSetTokenString( long packet, long protocolDesignator[], long tokenDesignator[], long offset, char data[] );
```

## Description

This function copies the string value to the token without terminating "\0".

## Example

```c
long packetHandle;

// create packet
packetHandle = AfdxInitPacket( "afdx" );

// set afdx payload
AfdxResizeToken( packetHandle, "afdx", "data", 5*8 /*bits*/ );
AfdxSetTokenString( packetHandle, "afdx", "data", "Hello" );

// Complete and send packet
AfdxCompletePacket( packetHandle );
AfdxOutputPacket( packetHandle );

// release packet
AfdxReleasePacket( packetHandle );
```

## Availability

| Since Version |
|---|
