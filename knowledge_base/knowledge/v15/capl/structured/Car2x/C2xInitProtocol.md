# C2xInitProtocol

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xInitProtocol( long packet, char protocolDesignator[] );
long C2xInitProtocol( long packet, char protocolDesignator[], char packetTypeDesignator[] );
```

## Description

This function initializes the protocol for a packet. If necessary further needed lower protocols are initialized, e.g. IPv4. Already initialized higher protocols are deleted.

Protocol fields that are marked as InitProtocol in the protocol overview are initialized.

## Parameters

| Name | Description |
|---|---|
| packet | Handle of a packet that has been created with C2xInitPacket |
| protocolDesignator | Name of the protocol, taken from the protocol overview |
| packetTypeDesignator | Type of the packet, taken from the protocol overview |

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
