# ethSetPhyState

> Category: `IP` | Type: `function`

## Syntax

```c
long ethSetPhyState(long channel, long phyState ); // form 1
long ethSetPhyState(long channel, long hwChannel, long phyState ); // form 2
long ethSetPhyState(ethernetPort port, long phyState ); // form 3
```

## Description

Sets the PHY state.

## Parameters

| Name | Description |
|---|---|
| channel | Ethernet channel number. Value range: 1..32 |
| phyState | 1: ePhyNormalState 2: ePhySleepState 3: ePhyPowerOffState |
| hwChannel | Hardware channel number. Vector network interface must support more than 1 hardware channel to use.Value range: 1..16 |
| port | Ethernet port. Only supported for network-based configurations and physical measurement ports. |

## Example

```c
on key 's'
{
  ethSetPhyState(ethernetPort::MyNetworkName::MyPortName, 2 /*ePhySleepState*/);
}

on key 'n'
{
  ethSetPhyState(ethernetPort::MyNetworkName::MyPortName, 1 /*ePhyNormalState*/);
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
