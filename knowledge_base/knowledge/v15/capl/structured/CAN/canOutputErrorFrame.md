# canOutputErrorFrame

> Category: `CAN` | Type: `function`

## Syntax

```c
long canOutputErrorFrame(errorFrame, long dominant, long recessive);
```

## Description

Outputs an Error Frame to the CAN bus. The number of dominant bits and the number of trailing recessive bits are given as arguments.

## Parameters

| Name | Description |
|---|---|
| errorFrame | Variable of type errorFrame. |
| dominant | Number of dominant bits. |
| recessive | Number of recessive bits. |

## Example

```c
canOutputErrorFrame(errorFrame, 12, 0); //output Error Frame with 12 dominant bits on CAN1
canOutputErrorFrame(CAN2.errorFrame, 6, 0); //output Error Frame with 6 dominant bits on CAN2
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.1 | 13.0 | — | — | 1.0 |
| Restricted To | — | CAN | CAN | — | — | CAN |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
