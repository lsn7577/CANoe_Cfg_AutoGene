# C2xInitPacket

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xInitPacket( void );
long C2xInitPacket( char protocolDesignator[] );
long C2xInitPacket( char protocolDesignator[], char packetTypeDesignator[] );
long C2xInitPacket( long packetToCopy );
long C2xInitPacket( long rawDataLength, byte rawData[] );
long C2xInitPacket( long rawDataLength, char rawData[] );
long C2xInitPacket( long rawDataLength, struct * rawDataStruct );
```

## Description

This function creates a new WLAN packet. Other functions can access to the newly created packet with the returned handle.

Protocol fields that are marked as InitProtocol in the protocol description are initialized.

## Parameters

| Name | Description |
|---|---|
| protocolDesignator | Designator of the protocol, which should be used for initialization |
| packetTypeDesignator | Designator of the packet type |
| packetToCopy | Handle of a packet which was created with C2xInitPacket before or handle of a packet which has been received within a callback (<OnC2xPacket>) The header and the data of this packet are copied to the new created packet. |
| rawDataLength | Length of rawData in byte |
| rawData/rawDataStruct | Raw data of a WLAN packet that is used to initialized the new packet |

## Return Values

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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.6 | — | — | — | 2.1 SP3 |
| Restricted To | — | Car2x | — | — | — | Car2x |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
