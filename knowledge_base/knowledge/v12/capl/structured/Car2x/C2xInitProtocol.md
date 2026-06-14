# C2xInitProtocol

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xInitProtocol( long packet, char protocolDesignator[] );
```

## Description

This function initializes the protocol for a packet. If necessary further needed lower protocols are initialized, e.g. IPv4. Already initialized higher protocols are deleted.

Protocol fields that are marked as InitProtocol in the protocol overview are initialized.

## Return Values

0 or error code

## Example

```c
long packetHandle;
char error[100];
byte macAddress[6] = { 0x20, 0x00, 0x00, 0x00, 0x00, 0x01 };

// create packet
packetHandle = C2xInitPacket("wlan");

// init CNH protocol
C2xInitProtocol(packetHandle, "geo_cnh" );

// set protocol fields
C2xSetTokenData( packetHandle, "wlan", "address2", 6, macAddress );
C2xSetTokenData( packetHandle, "eth" , "source" , 6, macAddress );

// set CNH values
C2xSetTokenInt( packetHandle, "geo_cnh", "lpvSpeed" , 100 );
C2xSetTokenInt( packetHandle, "geo_cnh", "lpvHeading" , 1800 );
C2xSetTokenInt( packetHandle, "geo_cnh", "lpvAltitude", 0 );

// Complete and send packet
C2xCompletePacket( packetHandle );
C2xOutputPacket( packetHandle );

// release packet
C2xReleasePacket( packetHandle );
```

## Availability

| Since Version |
|---|
