# ethGetEthernetPort

> Category: `IP` | Type: `function`

## Syntax

```c
ethernetPort ethGetEthernetPort(long Channel);
```

## Description

Gets the Ethernet port for the current simulation node. The channel needs to be specified and can be used for gateway nodes to differentiate between the ports on different networks.

## Parameters

| Name | Description |
|---|---|
| Channel | Application channel, i.e. Eth 1. |

## Return Values

Ethernet port

## Example

```c
on start
{
  ethernetport ownPort;
  ownPort = ethGetEthernetPort(1);
  // ... do something with ownPort
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
