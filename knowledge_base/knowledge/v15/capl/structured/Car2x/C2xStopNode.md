# C2xStopNode

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xStopNode(); //form 1
long C2xStopNode(char* nodeName); //form 2
```

## Description

The function stops the transmission of messages for a specified node.

## Parameters

| Name | Description |
|---|---|
| nodeName | Name of the node that stops the transmission. |

## Example

```c
//form 1
C2xStopNode();
//form 2
C2xStopNode(“Node1”);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 13.0 | — | — | — | 5.0 |
| Restricted To | — | Car2x: form 1 Car2x, Testnodes: form 2 | — | — | — | Car2x: form 1 Car2x, Testnodes: form 2 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
