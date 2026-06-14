# C2xInitPacket

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xInitPacket( void );
```

## Description

This function creates a new WLAN packet. Other functions can access to the newly created packet with the returned handle.

Protocol fields that are marked as InitProtocol in the protocol description are initialized.

## Return Values

Handle of the created packet or 0
With C2xGetLastError you can check if the function has been processed successfully.

## Example

```c
long packetHandle;
char error[100];
byte macAddress[6] = { 0x20, 0x00, 0x00, 0x00, 0x00, 0x01 };

// create packet
packetHandle = C2xInitPacket("geo_cnh");
if (C2xGetLastError() == 0)
{
  // set protocol fields
  C2xSetTokenData( packetHandle, "wlan", "address2", 6, macAddress );
  C2xSetTokenData( packetHandle, "eth", "source", 6, macAddress );

  // set CNH values
  C2xSetTokenInt( packetHandle, "geo_cnh", "lpvSpeed", 100 );
  C2xSetTokenInt( packetHandle, "geo_cnh", "lpvHeading", 1800 );
  C2xSetTokenInt( packetHandle, "geo_cnh", "lpvAltitude", 0 );

  // Complete and send packet
  C2xCompletePacket( packetHandle );
  C2xOutputPacket( packetHandle );

  // release packet
  C2xReleasePacket( packetHandle );
}
else
{
  C2xGetLastErrorText( elCount(error), error );
  write("Error: %s", error );
}
```

## Availability

| Since Version |
|---|
