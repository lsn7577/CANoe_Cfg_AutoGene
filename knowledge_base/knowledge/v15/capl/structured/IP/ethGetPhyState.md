# ethGetPhyState

> Category: `IP` | Type: `function`

## Syntax

```c
long ethGetPhyState(long channel ); // form 1
long ethGetPhyState(long channel, long hwChannel ); // form 2
long ethGetPhyState(ethernetPort port ); // form 3
```

## Description

Gets the PHY state.

## Parameters

| Name | Description |
|---|---|
| channel | Ethernet channel number. Value range: 1..32 |
| hwChannel | Hardware channel number. Vector network interface must support more than 1 hardware channel to use.Value range: 1..16 |
| port | Ethernet port. Only supported for network-based configurations and physical measurement ports. |

## Example

```c
/* TC10 testing could be implemented by polling the PhyState of Ports */

on timer myTimer
{
  if (ethGetPhyState(ethernetPort::MyNetworkName::MyPortName) == 1 /*ePhyNormalState*/)
  {
    write("ethernetPort::MyNetworkName::MyPortName's PHY is operational");
  }
  if (ethGetPhyState(ethernetPort::MyNetworkName::MyPortName) == 2 /*ePhySleepState */)
  {
    write("ethernetPort::MyNetworkName::MyPortName's PHY is sleeping");
  }
  if (ethGetPhyState(ethernetPort::MyNetworkName::MyPortName) == 3 /*ePhyPowerOffState */)
  {
    write("ethernetPort::MyNetworkName::MyPortName's PHY is powered-down");
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 12.0 SP3 | 12.0 SP3 | — | — | — | 4.0 SP3 |
| Restricted To | Ethernet | Ethernet | — | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
