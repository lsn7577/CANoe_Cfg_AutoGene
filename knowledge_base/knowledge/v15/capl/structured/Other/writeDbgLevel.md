# writeDbgLevel

> Category: `Other` | Type: `function`

## Syntax

```c
long writeDbgLevel(unsigned int priority, char format1[], char format2[], ...);
```

## Description

Outputs a message to the Write Window with the specified priority. This function can be used for debugging to vary the output to the Write Window. This function is especially useful if nodelayer-DLL’s are used. In this case the debug output can be controlled using a global priority parameter.

In the simulation tree the priority level can be set for every network node using the setWriteDbgLevel function.

## Parameters

| Name | Description |
|---|---|
| priority | Output priority from 0 to 15. |
| format | Format string, variables or expressions |

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
