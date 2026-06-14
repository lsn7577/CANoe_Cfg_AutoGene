# SecurityOfNodeGetFreshness

> Category: `Security` | Type: `function`

## Syntax

```c
long SecurityOfNodeGetFreshness(char nodeName[], char networkName[], char freshnessIdentifierString[], dword freshnessValueId, byte freshnessData[], dword freshnessDataLength)
```

## Description

Gets the freshness value of the specified node on the specified network for the specified Id.

As freshness values differs from Security Source to Security Source you have to refer to the Security Source specific manual to get more information about which values you have to specify as parameters.

You have to call SecurityLocalStartControlSimulationNode before this callback is called.

## Parameters

| Name | Description |
|---|---|
| char nodeName[] | The name of the node. |
| char networkName[] | The name of the network the node is on. |
| char freshnessIdentifierString[] | A string as an identifier for the freshness to get. |
| dword freshnessValueId | A numerical Id for the freshness to get. |
| byte freshnessData[] [In/Out] | The buffer for the freshness to get. |
| dword freshnessDataLength [In/Out] | The length of the buffer for the freshness to get in bytes. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 SP3 | 11.0 SP3 | — | — | — |
| Restricted To | — | CAN CAN FD FlexRay Ethernet | CAN CAN FD FlexRay Ethernet | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
