# OnIpReceivePrepare

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long OnIpReceivePrepare(ethernetPacket * packet);
```

## Description

If the CAPL program implements this callback it is called right before a received packet will be dispatched to the TCP/IP stack.

It is possible to manipulate the content of the packet or to block the receiving of the package from the bus.

## Parameters

| Name | Description |
|---|---|
| packet | The received Ethernet packet. |

## Example

```c
long OnIpReceivePrepare(ethernetPacket * packet)
{
  // block all packets with a broadcast destination MAC id
  if(packet.destination == 0xFFFFFFFFFFFFLL)
  {
    write("packet blocked");
    return 0;
  }
  write("packet passed to tcp/ip stack");
  return 1;
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 10.0 | 10.0 | 13.0 | — | — | 2.2 |
| Restricted To | IP | IP | IP | — | — | IP |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
