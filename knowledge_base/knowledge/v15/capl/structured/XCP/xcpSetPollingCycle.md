# xcpSetPollingCycle

> Category: `XCP` | Type: `function`

## Syntax

```c
long xcpSetPollingCycle(char namespace[], char variable[], long cycleTime); // form 1
long xcpSetPollingCycle(sysvar sysvar, long cycleTime); // form 2
```

## Description

Sets the cycle time of a parameter, if the read mode of the parameter is set to polling.

## Parameters

| Name | Description |
|---|---|
| namespace | Namespace of the corresponding system variable. |
| variable | Name of the corresponding system variable. |
| sysvar | Name of the fully qualified name of the system variable, including all name spaces, separated by "::".The name must be preceded by "sysvar::" |
| cycleTime | Cycle time with which the parameter is measured. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 10.0 SP3 | 13.0 | — | — | 2.2 SP2 |
| Restricted To | — | XCP | XCP | — | — | XCP |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
