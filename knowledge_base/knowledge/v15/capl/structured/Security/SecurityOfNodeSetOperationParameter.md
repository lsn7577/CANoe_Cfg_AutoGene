# SecurityOfNodeSetOperationParameter

> Category: `Security` | Type: `function`

## Syntax

```c
long SecurityOfNodeSetOperationParameter(char nodeName[], char networkName[], long key, qword value)
```

## Description

Sets the operation parameter value of the specified key at the specified node and network. You have to call SecurityLocalStartControlSimulationNode before this callback is called. Which and how many operation parameters exist, which values are valid for an operation parameter differs from Security Source to Security Source.

Refer to the Security Source specific manual to get more information about operation parameters. The manual can be opened from the Vector Security Manager on the OEM specific ribbon page.

## Parameters

| Name | Description |
|---|---|
| char nodeName[] | Name of the node. |
| char networkName[] | Name of the network in which the node is located. |
| long key | Numeric identifier of the operation parameter. |
| qword value | New value of the operation parameter. |

## Return Values

A Value of 1 means that the action was successful. A value less than or equal to 0 means error.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 SP4 | 11.0 SP4 | — | — | — |
| Restricted To | — | CAN CAN FD FlexRay Ethernet | CAN CAN FD FlexRay Ethernet | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
