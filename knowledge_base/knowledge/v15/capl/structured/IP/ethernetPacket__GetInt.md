# ethernetPacket::GetInt

> Category: `IP` | Type: `method`

## Syntax

```c
int ethernetPacket.GetInt(char protocol[], char field[]);
```

## Description

Returns the value of the specified field as int.

If protocol or field is not contained in the packet, the measurement is stopped with a runtime error. ethernetPacket::IsAvailable can be used to find out if the field is available.

## Parameters

| Name | Description |
|---|---|
| protocol | Name of the protocol. |
| field | Name of the field. |

## Return Values

Value of the field.

## Example

```c
on ethernetPacket *
{
  if(this.IsAvailable("icmpv4", "echo.identifier"))
  {
    Write("icmpv4.echo.identifier has value %d", this.GetInt("icmpv4", "echo.identifier"));
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
