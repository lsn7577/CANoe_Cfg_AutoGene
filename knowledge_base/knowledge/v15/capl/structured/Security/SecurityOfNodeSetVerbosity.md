# SecurityOfNodeSetVerbosity

> Category: `Security` | Type: `function`

## Syntax

```c
void SecurityOfNodeSetVerbosity(char nodeName[], char networkName[], dword level)
```

## Description

Configures the notification level for the specified node on the specified network from low (0) to high (5).

## Parameters

| Name | Description |
|---|---|
| char nodeName[] | The name of the node. |
| char networkName[] | The name of the network the node is on. |
| dword level: Desired notification level. | Range: 0-5 0: Only critical errors are printed. 1: All errors are printed 2: Additionally warnings are printed 3: Information messages are printed too. 4-5: Debug messages are active. |

## Return Values

—

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
