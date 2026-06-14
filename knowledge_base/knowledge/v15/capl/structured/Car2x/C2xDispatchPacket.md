# C2xDispatchPacket

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xDispatchPacket( long packet, dword direction );
```

## Description

This function dispatches a packet to CANoe application (analyze), it isn’t given to the hardware driver. The direction (Rx, Tx TxRq) that is displayed e.g. in the Trace Window can be defined.

## Parameters

| Name | Description |
|---|---|
| packet | Handle of a packet that has been initialized and completed (see example). |
| direction | 0 = Rx 1 = Tx 2 = TxRq |

## Example

```c
long packetHandle;
char error[100];
byte macAddress[6] = { 0x20, 0x00, 0x00, 0x00, 0x00, 0x01 };

// create packet
packetHandle = C2xInitPacket("geo_eh");
if (C2xGetLastError() == 0)
{
  // Set protocol fields
  C2xSetTokenData( packetHandle, "wlan", "address2", 6, macAddress );
  C2xSetTokenData( packetHandle, "eth",  "source",   6, macAddress );

  // set EH values
  C2xSetTokenInt( packetHandle, "geo_eh", "lpvSpeed",    100 );
  C2xSetTokenInt( packetHandle, "geo_eh", "lpvHeading",  1800 );
  C2xSetTokenInt( packetHandle, "geo_eh", "lpvAltitude", 0 );

  // Complete and send packet
  C2xCompletePacket( packetHandle );

  // Dispatch the packet in tx direction
  C2xDispatchPacket( packetHandle, 1);

  // Release packet
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
| Since Version | — | 12.0 SP3 | — | — | — | 4.0 SP3 |
| Restricted To | — | Car2x | — | — | — | Car2x |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
