# AfdxSetSignalStatus

> Category: `ADFX` | Type: `function`

## Syntax

```c
long AfdxSetSignalStatus( long packet, char signalName[], long value ); // form 1
long AfdxSetSignalStatus( long packet, long offset, long value ); // form 2
```

## Description

This function sets the functional status (FS) of a signal.

## Parameters

| Name | Description |
|---|---|
| packet | Handle of the message. |
| signalName | Name of the signal. Note: The signal and its message need to be defined in the assigned DBC file. |
| offset | The offset value points to a single byte in the 32-bit functional status area. |
| value | Valid status enumeration: This functional status is updated with this value. |

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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0 SP3: form 1, 2 | — | — | — | — |
| Restricted To | — | AFDX | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
