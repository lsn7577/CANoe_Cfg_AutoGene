# IPSetAdapterStatus

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long IPSetAdapterStatus( dword ifIndex, dword status);
```

## Description

With this function it is possible to activate or deactivate a network adapter of the TCP/IP stack.

When the adapter is set down all IP addresses of this adapter will be removed and sending or receiving packets on this adapter will be stopped.

If the default gateway was configured in a network which was configured on this adapter it will also be removed.

When the adapter is set up again the addresses configured in the TCP/IP Stack dialog will be reconfigured and the default gateway is set again.

## Parameters

| Name | Description |
|---|---|
| ifIndex | The 1-based network interface index. |
| status | 0: Set adapter down 1: Set adapter up |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 11.0 | 11.0 | 13.0 | — | — | 3.0 |
| Restricted To | IP | IP | IP | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
