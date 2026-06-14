# lookupEthernetPort

> Category: `IP` | Type: `function`

## Syntax

```c
ethernetPort lookupEthernetPort(char[] ethernetPortName);
```

## Description

Gets the Ethernet port for a port qualification string.

## Parameters

| Name | Description |
|---|---|
| ethernetPortName | The port qualification string <NetworkName>::<PortName>. |

## Return Values

Ethernet port

## Example

```c
on ethernetPacket *
{
  if (this.hwPort == lookupEthernetPort("Ethernet1::ChatClient1"))
  {
    write("Received a packet on %s", "Ethernet1::ChatClient1");
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 12.0 SP4 | 12.0 SP4 | 13.0 | — | — | 5.0 |
| Restricted To | Ethernet | Ethernet | Ethernet | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
