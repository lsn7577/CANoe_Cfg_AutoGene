# ethernetErrorPacket

> Category: `IP` | Type: `function`

## Syntax

```c
ethernetErrorPacket <errorPacket var>;
```

## Description

Can be use in on ethernetErrorPacket handler to access packet data.

## Parameters

| Name | Description |
|---|---|
| packet var | Character string defining the object’s variable name. |

## Example

```c
on ethernetErrorPacket *
{
  write("Received Ethernet error packet on Eth%d", this.msgChannel );
  output( this ); // only required in CAPL node in measurement setup!
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.5 9.0 SP3: selector hwChannel 12.0 SP4: selector hwPort 13.0: selectors Length, FCS, FrameLen, SOF, Type, Source, Destination | 8.5: form 1 9.0 SP3: selector hwChannel 12.0 SP4: selector hwPort 13.0: selectors Length, FCS, FrameLen, SOF, Type, Source, Destination | 13.0 | — | — | 2.0 SP2: form 1 2.1 SP3: selector hwChannel 5.0: selector hwPort 13.0: selectors Length, FCS, FrameLen, SOF, Type, Source, Destination |
| Restricted To | Ethernet | Ethernet | Ethernet | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
