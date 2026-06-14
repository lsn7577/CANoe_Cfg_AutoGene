# linActivateResps

> Category: `LIN` | Type: `function`

## Syntax

```c
long linActivateResps(); // form 1
long linActivateResps(char nodeName[]); // form 2
```

## Description

Reactivates all frame responses published by the calling Slave node according to the LIN database file (LDF), after having been previously deactivated by linDeactiveResps() or linResetSlave().

Per default all frame responses are activated for Slave nodes on measurement start i.e. it is assumed that Slave nodes have non-volatile memory.

LIN2.0 Slave nodes will automatically activate responses for re-configurable frames on receiving valid reconfiguration commands i.e. AssignFrameID.

Individual frame responses can be activated manually using the function linSetRespCounter.

With form 2 you can activate the Slave responses of the selected Slave node (nodeName). If the parameter nodeName is not set or an empty string is given, the Slave responses of the node invoking this function will be deactivated.

## Parameters

| Name | Description |
|---|---|
| nodeName | Slave node |

## Return Values

Number of activated frame responses or -1 if an error occurs.

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
