# C2xGetTokenData

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xGetTokenData( long packet, char protocolDesignator[], char tokenDesignator[], long length, char buffer[] );
long C2xGetTokenData( long packet, char protocolDesignator[], char tokenDesignatorl[], long length, byte buffer[] );
long C2xGetTokenData( long packet, char protocolDesignator[], char tokenDesignator[], long length, struct bufferStruct );
long C2xGetTokenData( long packet, char protocolDesignator[], char tokenDesignator[], long byteOffset, long length, char buffer[] );
long C2xGetTokenData( long packet, char protocolDesignator[], char tokenDesignator[], long byteOffset, long length, byte buffer[] );
long C2xGetTokenData( long packet, char protocolDesignator[], char tokenDesignator[], long byteOffset, long length, struct bufferStruct );
```

## Description

This function requests the data or a part of date of a token.

## Parameters

| Name | Description |
|---|---|
| packet | Handle of a packet that has been created with C2xInitPacket |
| protocolDesignator | Name of the protocol, e.g. geo_cnh |
| tokenDesignator | Name of the token, e.g. data |
| byteOffset | Offset from the beginning of the token in byte |
| length | Number of bytes to be copied Make sure size of destination (buffer or bufferStruct) is equal or larger than length. |
| buffer | Buffer in which the data are copied |
| bufferStruct | Struct in which the data are copied |

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
  byte data[5];
  char error[100];

  // get payload of the receive packet
  C2xGetTokenData( packet, "geo_cnh", "data", 5, data );
  if (C2xGetLastError() == 0)
  {
    // do something with data
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
