# ILSetCANFDParam

> Category: `CANoeIL` | Type: `function`

## Syntax

```c
long ILSetCANFDParam(dword ID, int FDF, int BRS, int DLC)
long ILSetCANFDParam(dbMsg msg, int FDF, int BRS, int DLC)
```

## Description

The function allows setting of CAN FD parameters for a specific message.

## Parameters

| Name | Description |
|---|---|
| ID | CAN-ID of message that should be modified. |
| msg | message that should be modified. |
| FDF | -2: reset FDF setting of message according to database-1: do not change FDF setting of message0: FDF off1: FDF onThis parameter has highest priority and will overrule settings for BRS and DLC, i.e. BRS = 0 and max DLC = 8 in case that FDF off. |
| BRS | -2: reset BRS settings of message according to database-1: do not change BRS setting of message0: BRS off1: BRS on |
| DLC | -2: reset DLC settings of message according to database-1: do not change DLC setting of message≥0: set DLC of message to specified value |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.5 SP3 | 14 | 14 | — | — |
| Restricted To | — | CAN | CAN | CAN | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | ✔ | — | N/A |
