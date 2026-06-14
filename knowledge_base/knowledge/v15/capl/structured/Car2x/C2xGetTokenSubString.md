# C2xGetTokenSubString

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xGetTokenSubString( long packet, char protocolDesignator[], char tokenDesignator[], long byteOffset, long length, char buffer[] );
```

## Description

This function copies a specified number of characters from a given position inside the token and adds a terminating \0.

## Parameters

| Name | Description |
|---|---|
| packet | Handle of a packet that has been created with C2xInitPacket |
| protocolDesignator | Name of the protocol, e.g. geo_cnh |
| tokenDesignator | Name of the token, e.g. data |
| byteOffset | Offset from the beginning of the token in byte |
| length | Number of characters to be copied |
| buffer | Buffer in which the characters are copied This function adds a terminating \0. Thus, the size of the buffer must be at least one byte larger than length. |

## Return Values

With C2xGetLastError you can check if the function has been processed successfully.

## Example

Node System - PreStart in CAPL Browser

Node Callback Function in CAPL Browser

```c
on preStart
{
  C2xReceivePacket("OnC2xPacket");
}
void OnC2xPacket( long channel, long dir, long radioChannel, long signalStrength, long signalQuality, long packet )
{
  char rx_str[100];
  char error[100];

  // get the payload of the packet
  C2xGetTokenSubString( packet, "geo_cnh", "data", 8, elCount(rx_str), rx_str );
  // would access payload of a cnh packet

  if (C2xGetLastError() == 0)
  {
    write(rx_str);
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
