# ethernetPort::<NetworkName>::<PortName>

> Category: `IP` | Type: `function`

## Syntax

```c
ethernetPort ethernetPort.<NetworkName>.<PortName>;
```

## Description

Initializes a variable of type ethernetPort with a port qualification.

## Parameters

| Name | Description |
|---|---|
| NetworkName | Name of the Ethernet network. |
| PortName | Name of the port. |

## Example

```c
on start
{
  ethernetport clientPort;
  clientPort=ethernetport::Ethernet1::ChatClient1;
  // ... do something with clientPort
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 12.0 SP4 15 (selectors) | 12.0 SP4 15 (selectors) | 13.0 15 (selectors) | — | — | 5.0 6 (selectors) |
| Restricted To | Ethernet | Ethernet | Ethernet | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
