# ethernetPacket::GetProtocolErrorText

> Category: `IP` | Type: `method`

## Syntax

```c
word ethernetPacket.GetProtocolErrorText( char buffer[] );
```

## Description

Copies an error text to the buffer for invalid Ethernet packets. For valid Ethernet packets an empty string is returned.

## Parameters

| Name | Description |
|---|---|
| buffer | Char buffer where the error string is copied to. |

## Return Values

Number of characters copied to buffer.

## Example

```c
on ethernetPacket *
{
  if (this.HasProtocolError())
  {
    char text[100];
    this.GetProtocolError( text );
    write( "Protocol error on Eth %d: %s", this.msgChannel, text );
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 11.0 SP3 | 11.0 SP3 | 13.0 | — | — | 3.0 SP3 |
| Restricted To | Ethernet | Ethernet | Ethernet | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
