# on ethernetStatus

> Category: `IP` | Type: `event`

## Description

The event procedure is called on the change of the status of the Ethernet link.

To access the control information you would use selectors.

The key word this is available within an on ethernetStatus procedure, to access the information of the link status.

## Example

```c
on ethernetStatus *
{
  switch(this.status)
  {
    case 0:
      write("Ethernet link on Eth%d is down", this.msgChannel );
      break;
    case 1:
      write("Ethernet link on Eth%d is up with %dbit/sec", this.msgChannel , this.bitrate );
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.5: form 1-2 9.0 SP3: selector hwChannel 11.0: selector time_ns 12.0 SP4: selector hwPort 13.0: form 3 | 8.5: form 1-2 9.0 SP3: selector hwChannel 11.0: selector time_ns 12.0 SP4: selector hwPort 13.0: form 3 | 13.0 | — | — | 2.0 SP2: form 1 2.1 SP3: selector hwChannel 3.0: selector time_ns 5.0: selector hwPort 5.0: form 3 |
| Restricted To | Ethernet | Ethernet | Ethernet | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |

## Selectors

| Selector | Type | Access Limitation |
|---|---|---|
| status 0: Link down 1: Link up | long | Read only |
| bitrate Bit rate in kBit/sec | dword | Read only |
| msgChannel Application channel, i.e. Eth 1 | word |  |
| hwChannel Hardware channel. If not supported by network interface, value is 1. | word | Only with Vector Interfaces, i.e. VN5640, with operation mode with more than 1 hardware channel. Channel-based network access only |
| hwPort Port used for network-based access. | ethernetPort | network-based access only |
| time_ns Timestamp of the status change | int64 | read only |
| network-based | ../../../CANoeCANalyzer/Ethernet/EthernetPortBasedNetworkAccess.htm |  |
