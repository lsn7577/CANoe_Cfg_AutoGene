# linDeactivateResps

> Category: `LIN` | Type: `function`

## Syntax

```c
long linDeactivateResps(); // form 1
long linDeactivateResps(char nodeName[]); // form 2
```

## Description

This function deactivates frame responses for all frames published by the calling Slave node. The frame responses can be deactivated individually using the function linSetRespCounter().

With form 2 you can deactivate the Slave responses of the selected Slave node (nodeName). If the parameter nodeName is not set or an empty string is given, the Slave responses of the node invoking this function will be deactivated.

## Parameters

| Name | Description |
|---|---|
| nodeName | Slave node |

## Return Values

Number of deactivated frame responses or -1 on failure.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 5.1: form 1 8.5: form 2 | 5.1: form 1 8.5: form 2 | 13.0 | 13.0 | — | 1.0: form 1 2.0: form 2 |
| Restricted To | LIN | LIN | LIN | LIN | — | LIN |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | — | N/A |
