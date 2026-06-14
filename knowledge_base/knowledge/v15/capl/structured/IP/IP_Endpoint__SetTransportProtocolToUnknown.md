# IP_Endpoint::SetTransportProtocolToUnknown

> Category: `IP` | Type: `method`

## Syntax

```c
long IP_Endpoint::SetTransportProtocolToUnknown();
```

## Description

Invalidates the transport protocol.

## Example

```c
on start
{
  IP_Endpoint UDP:192.168.1.1:4000 addr;
  addr.SetTransportProtocolToUnknown();
  if (addr.IsTCP())
  {
    write( "Is TCP endpoint" );
  }
  else if (addr.IsUDP())
  {
    write( "Is UDP endpoint" );
  }
  else
  {
    write( "No transport protocol specified for endpoint" );
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 12.0 | 12.0 | 13.0 | — | — | 4.0 |
| Restricted To | Ethernet | Ethernet | Ethernet | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
