# TestJoinEthernetLinkStatus

> Category: `Test` | Type: `function`

## Syntax

```c
long TestJoinEthernetLinkStatus(long channel, long status); // form 1
long TestJoinEthernetLinkStatus(long channel, Int64 hwChannel, long status); // form 2
long TestJoinEthernetLinkStatus(ethernetport hwport, long status); // form 3
```

## Description

Completes the current set of joined events with the transmitted event. This function does not wait.

## Parameters

| Name | Description |
|---|---|
| channel | Ethernet channel number.Value range: 1..32 |
| hwChannel | Ethernet hardware channel number.Value range: 1..64 |
| hwPort | Hardware port qualifier. |
| Status | Wait for this status: 0 = link down 1 = link up |
| aTimeout | Maximum time that should be waited [ms] (Transmission of 0: no timeout controlling). |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 12.0 SP3 | 13.0 | — | — | 4.0 SP3 |
| Restricted To | — | Ethernet | Ethernet | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
