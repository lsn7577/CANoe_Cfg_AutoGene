# C2xIsTokenAvailable

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xIsTokenAvailable( long packet, char protocolDesignator[], char tokenDesignator[] );
```

## Description

This function checks, if the specified token is part of the packet.

## Parameters

| Name | Description |
|---|---|
| packet | Handle of a packet that has been created with C2xInitPacket. |
| protocolDesignator | Name of the protocol. |
| tokenDesignator | Name of the token. |

## Example

```c
long packet;

//create geoNetworking unicast
packet = C2xInitPacket("geoNetworking");

//spvNetAddr is optional but headertype (ht) is unicast per default which contains spvNetAddr
if (!C2xIsTokenAvailable(packet, "geoNetworking","spvNetAddr"))
{
  write("error! spvNetAddr is not available in geoNetworking unicast");
}

//transform packet to geoNetworking broadcast
if (C2xSetTokenInt(packet, "geo_cnh", "ht", 4) != 0)
{
  write("error! C2xSetTokenInt failed");
}
if (C2xResizeToken(packet, "geoNetworking", "header", 384) != 0)
{
  write("error! C2xResizeToken failed");
}

//broadcast does not contain spvNetAddr
if (C2xIsTokenAvailable(packet, "geoNetworking", "spvNetAddr"))
{
write("error! spvNetAddr is available in geoNetworking broadcast");
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0 | — | — | — | 2.1 SP3 |
| Restricted To | — | Car2x | — | — | — | Car2x |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
