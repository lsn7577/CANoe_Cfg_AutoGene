# AfdxSetSignalStatus

> Category: `ADFX` | Type: `function`

## Syntax

```c
long AfdxSetSignalStatus( long packet, char signalName[], long value ); // form 1
```

## Description

This function sets the functional status (FS) of a signal.

## Return Values

0 or error code

## Example

Create and output an AFDX packet with two signals without DBC

```c
long packet;
long srcIP = 0x0a022600;
long destIP = 0xe0e01a0f;
long srcUdpPort = 0x2b71;
long vlID = 0x1a0f;
long len = 640;

packet = AfdxInitPacket(srcIP, destIP, srcUdpPort, vlID, len );

// set oil temperature 21 to 78 degrees
AfdxSetSignalInt( packet, 8, 78 ); // offset=8

// set corresponding status byte to <NO>
AfdxSetSignalStatus( packet, 4, 3 );

// set oil temp 22 to 52 degree
AfdxSetSignalInt( packet, 12, 52 );  // offset=12

// set corresponding status byte to <NO>
AfdxSetSignalStatus( packet, 5, 3 );

AfdxOutputPacket( packet );
```

## Availability

| Since Version |
|---|
