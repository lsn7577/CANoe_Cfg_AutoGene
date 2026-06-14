# C2xGetTokenInt

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xGetTokenInt( long packet, char protocolDesignator[], char tokenDesignator[] ); // form 1
long C2xGetTokenInt( long packet, char protocolDesignatorl[], char tokenDesignator[], long byteOffset, long length, long networkByteOrder ); // form 2
```

## Description

This function requests the integer value of a token.

Form 2 with byte offset returns a part of the token data as integer.

## Parameters

| Name | Description |
|---|---|
| packet | Handle of a packet that has been created with C2xInitPacket |
| protocolDesignator | Name of the protocol, e.g. geo_cnh |
| tokenDesignator | Name of the token, e.g. lpvSpeed |
| byteOffset | Offset from the beginning of the token in byte |
| length | Length of the integer value, must be 1, 2, 3 or 4 byte |
| networkByteOrder | 0: INTEL (little-endian) 1: MOTOROLA (big-endian) |

## Return Values

With C2xGetLastError you can check if the function has been processed successfully.

## Example

Node System - PreStart in CAPL Browser

Node Callback Function in CAPL Browser

```c
on preStart
{
  C2xReceivePacket( "OnC2xPacket" );
}
void OnC2xPacket( long channel, long dir, long radioChannel, long signalStrength, long signalQuality, long packet )
{
  long speed;
  char error[100];

  // get lpvSpeed of the receive packet
  speed = C2xGetTokenInt( packet, "geo_cnh", "lpvSpeed" );
  if (C2xGetLastError() == 0)
  {
    // do something with lpvSpeed
  }
  else
  {
    C2xGetLastErrorText( elCount(error), error );
    write("Error: %s", error );
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.6: form 1, 2 | — | — | — | 2.1 SP3: form 1, 2 |
| Restricted To | — | Car2x | — | — | — | Car2x |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
