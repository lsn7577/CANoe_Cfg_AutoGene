# mostGenerateBusloadCtrl

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostGenerateBusloadCtrl (long channel, long msgs);
```

## Description

The function sends cyclical messages to the control channel. Use the mostConfigureBusloadCtrl() function to specify the send parameters and contents of the message.

## Parameters

| Name | Description |
|---|---|
| channel | Channel of the connected MOST hardware. |
| 0 | Stops the busload generation |
| >0 | Sends the given number of packets |
| -1 | Sends continual packets |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 5.2 | 5.2 | — | — | — | —✔ |
| Restricted To | MOST25 MOST50 MOST150 After measurement start Not in Stopmeasurement | MOST25 MOST50 MOST150 After measurement start Not in Stopmeasurement | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | ✔ | ✔ | — | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | — | — | — | —✔ |
