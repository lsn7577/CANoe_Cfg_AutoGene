# ethGetLinkStatus

> Category: `IP` | Type: `function`

## Syntax

```c
long ethGetLinkStatus( long channel ); // form 1
long ethGetLinkStatus( long channel, long hwChannel ); // form 2
long ethGetLinkStatus( ethernetPort port ); // form 3
```

## Description

Returns the link status of the channel.

## Parameters

| Name | Description |
|---|---|
| channel | Ethernet channel number. Value range: 1..32 |
| hwChannel | Hardware channel number. Vector network interface must support more than 1 hardware channel to use.Value range: 1..16 |
| port | Ethernet port, described by network name and port name. |

## Example

Example 1

Example 2

```c
on key 'i'
{
  write("Link status has the value: %d", ethGetLinkStatus(1));
}
on key 'i'
{
  write("Link status has the value: %d", ethGetLinkStatus(ethernetPort::MyNetworkName::MyPortName));
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.2: form 1 9.0 SP3: form 2 12.0: form 3 | 8.2: form 1 9.0 SP3: form 2 12.0: form 3 | — | — | — | 2.0 SP2: form 1 2.1 SP3: form 2 4.0: form 3 |
| Restricted To | Ethernet | Ethernet | — | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
