# ILNodeDisturbAllUpdateBits

> Category: `CANoeIL` | Type: `function`

## Syntax

```c
long ILNodeDisturbAllUpdateBits(dbNode aNode, long flags, long disturbanceMode, long disturbanceCount, long disturbanceValue);
long ILNodeDisturbAllUpdateBits(char aNodeName[], long flags, long disturbanceMode, long disturbanceCount, long disturbanceValue);
```

## Description

Modifies all update bits of signals/signal groups of a node. Different fault injections are possible.This function influences a simulation node with an assigned CANoe interaction layer.

## Parameters

| Name | Type | Description |
|---|---|---|
| aNode |  | The symbolic name of a node in the database, whose update bits will be disturbed. |
| aNodeName |  | The name of a node in the database, whose update bits will be disturbed. |
| 0 |  | Update bits of signals and signal groups are disturbed. |
| 1 |  | Only signal update bits are disturbed. |
| 2 |  | Only signal group update bits are disturbed. |
| 0 | Value | The disturbance uses the value in disturbanceValue as update bit. |
| 1 | Freeze | The current update bit value is transmitted. |
| 2 | Random | A random value is transmitted as update bit. |
| -1 |  | Infinite. |
| 0 |  | Stops the disturbance, e.g.a infinite disturbance. |
| n |  | Number of disturbances. |
| disturbanceValue |  | This value is used in combination with the disturbanceMode. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2 SP4 | 14 | 14 | — | — |
| Restricted To | — | CAN FlexRay | CAN FlexRay | CAN FlexRay | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | ✔ | — | N/A |
