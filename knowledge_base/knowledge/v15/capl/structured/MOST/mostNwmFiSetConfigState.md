# mostNwmFiSetConfigState

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostNwmFiSetConfigState(long state, long sendConfigStatusMsg);
```

## Description

Forces the network configuration status to be set in CANoe’s NetworkMaster.

Use the function with care since the state machine of the NetworkMaster is not guaranteed to work properly afterwards. (A shutdown of the network will reset the NetworkMaster’s state machine.)

The function is available for CAPL programs assigned to the NetworkMaster block in the Simulation Setup.

## Parameters

| Name | Description |
|---|---|
| state | 0: ConfigNotOk 1: ConfigOK |
| sendConfigStatusMsg | 0: set the configuration status without sending a message 1: set configuration status and broadcast NetworkMaster.Configuration.Status |

## Return Values

See error codes

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.2 | — | — | — | —✔ |
| Restricted To | — | MOST25 MOST50 MOST150 | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | — | ✔ | — | N/A | — | —✔ |
| 64-Bit | — | ✔ | — | — | — | —✔ |
