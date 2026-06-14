# setWriteDbgLevel

> Category: `Other` | Type: `function`

## Syntax

```c
void setWriteDbgLevel (unsigned int priority);
```

## Description

This function sets the priority level for the writeDbgLevel CAPL function. The output priority must be set for every network node.

## Parameters

| Name | Description |
|---|---|
| 0 | Only write output with a priority of 0 are shown in the Write Window. |
| 5 | Write output with a priority ranging from 0 to 5 are shown. |
| 15 | All outputs are shown. |

## Return Values

—

## Example

```c
int i = 10;
int j = 12;
setWriteDbgLevel(7);
writeDbgLevel (4, "This is shown: h= %lxh",j);
 // Output: This is shown: h= 0ch
writeDbgLevel (9, "This is not shown: d= %ld",i);
 // No output
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 3.0 | 13.0 | — | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
