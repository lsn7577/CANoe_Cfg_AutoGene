# AREthSetMulticastReceiverEndpoints

> Category: `IP` | Type: `function`

## Syntax

```c
long AREthSetMulticastReceiverEndpoints(dword cevgHandle, dword multicastIPv4Address, dword udpPort) // form 1
long AREthSetMulticastReceiverEndpoints(dword cevgHandle, byte multicastIPv6Address[], dword udpPort) // form 2
long AREthSetMulticastReceiverEndpoints(dword cevgHandle, IP_Endpoint multicastIPEndpoint); // form 3
```

## Description

Sets the multicast endpoint that is used for the consumed event group to receive field/event notification per multicast.

## Parameters

| Name | Description |
|---|---|
| cevgHandle | Consumed event group handle (may be retrieved by AREthGetConsumedObjectHandle). |
| multicastIPv4Address | Multicast IPv4 address receiving the events/fields. In network byte order. |
| multicastIPv6Address | Multicast IPv6 address receiving the events/fields. |
| udpPort | An UDP port number receiving the events/fields. May be zero if the events/fields shall not be received by multicast anymore. |
| multicastIPEndpoint | Object of type IP_Endpoint that contains the address/port of the multicast endpoint. An IP_Endpoint with port number zero may be passed to delete a previously set IP_Endpoint. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 SP3: form 1-2 12.0 SP2: form 3 | — | — | — | 3.0 SP3: form 1-2 4.0 SP2: form 3 |
| Restricted To | — | Ethernet | — | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
