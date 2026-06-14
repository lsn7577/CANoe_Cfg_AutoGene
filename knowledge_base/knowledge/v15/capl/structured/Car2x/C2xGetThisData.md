# C2xGetThisData

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xGetThisData( long offset, long bufferSize, byte buffer[] );
long C2xGetThisData( long offset, long bufferSize, char buffer[] );
long C2xGetThisData( long offset, long bufferSize, struct* buffer );
```

## Description

This function gets the payload data of the highest interpretable protocol.

## Parameters

| Name | Description |
|---|---|
| offset | Byte offset relative to the beginning of the payload |
| bufferSize | Number of requested bytes |
| buffer | buffer in which the requested data are copied |

## Return Values

Number of copied data bytes.

## Example

Node System - PreStart in CAPL Browser

Node Callback Function in CAPL Browser

```c
on preStart
{
  C2xReceivePacket( "OnC2xPacket");
}
void OnC2xPacket( long channel, long dir, long radioChannel, long signalStrength, long signalQuality, long packet )
{
  byte payload[8];
  long len;

  len = C2xGetThisData( 0, 8, payload);
  write( "Receive payload with %d bytes", len );
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
