# ILNodeControlSimulationOff

> Category: `CANoeIL` | Type: `function`

## Syntax

```c
long ILNodeControlSimulationOff(char aNodeName[])
```

## Description

Stops the simulation of the interaction layer of the specified simulation node. In this state the interaction layer does not react on any function besides turning the simulation on again. The specified node must be in the current bus context. In all other cases the function has no effect and will return with an error.

## Parameters

| Name | Description |
|---|---|
| aNodeName | Name of the node of which the interaction layer should be turned off. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2 SP3 | 14 | 14 | — | — |
| Restricted To | — | CAN FlexRay | CAN FlexRay | CAN FlexRay | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | ✔ | — | N/A |
