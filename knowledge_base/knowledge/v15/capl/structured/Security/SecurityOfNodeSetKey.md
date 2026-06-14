# SecurityOfNodeSetKey

> Category: `Security` | Type: `function`

## Syntax

```c
long SecurityOfNodeSetKey(char nodeName[], char networkName[], char keyIdentifierString[], dword keyIdentifierValue, byte newKey[], dword keyLength, dword flags)
```

## Description

Changes a key at the node the specified node on the specified network.

As keys and the key handling differs from Security Source to Security Source you have to refer to the Security Source specific manual to get more information about which values you have to specify as parameters.

You have to call SecurityLocalStartControlSimulationNode before this callback is called.

## Parameters

| Name | Description |
|---|---|
| char nodeName[] | The name of the node. |
| char networkName[] | The name of the network the node is on. |
| char keyIdentifierString[] | A string as an identifier for the key to set. |
| dword keyIdentifierValue | A numerical Id for the key to set. |
| byte newKey[] | The key to set as a byte array. |
| dword keyLength | The length of the new key in bytes. |
| dword flags | Reserved. (set to 0) |

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
