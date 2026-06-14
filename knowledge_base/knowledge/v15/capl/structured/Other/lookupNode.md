# lookupNode

> Category: `Other` | Type: `function`

## Syntax

```c
dbNode * lookupNode(char nodeName[]);
```

## Description

Searches for a node definition in the database(s). If the node is not found or if the name is not unique, test modules/units report an error in test system while simulation/analysis nodes write a warning into the Write Window, and the function returns an invalid dbNode.

## Parameters

| Name | Description |
|---|---|
| nodeName | The qualified name of the node. The syntax is [NetworkName::]NodeName, i.e. the network name is optional. |

## Return Values

The found unique node definition or an invalid object.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 10.0 | 10.0 | 13.0 | — | — | 2.2 |
| Restricted To | CAN | CAN | CAN | — | — | CAN |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
