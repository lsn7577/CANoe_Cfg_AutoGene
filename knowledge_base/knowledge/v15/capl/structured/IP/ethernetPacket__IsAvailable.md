# ethernetPacket::IsAvailable

> Category: `IP` | Type: `method`

## Syntax

```c
byte ethernetPacket.IsAvailable(char protocol[], char field[]);
```

## Description

Checks whether the protocol and the protocol field are present in the Ethernet packet.

## Parameters

| Name | Description |
|---|---|
| protocol | Name of the protocol. |
| field | Name of the field. |

## Example

```c
on ethernetPacket *
{
  if("icmpv4", "echo.identifier"))
  {
    Write("Protocol field icmpv4.echo.idenfifier is available");
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 13.0 SP2 | 13.0 SP2 | 13.0 | — | — | 5.0 SP2 |
| Restricted To | Ethernet | Ethernet | Ethernet | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
