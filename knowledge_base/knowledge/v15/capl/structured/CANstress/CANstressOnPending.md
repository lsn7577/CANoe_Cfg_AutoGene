# CANstressOnPending

> Category: `CANstress` | Type: `function`

## Syntax

```c
long CANstressOnPending( char fnctCallback[] );
```

## Description

Registers a CAPL function as callback that is called if CANstress is switched into the state Pending.

## Parameters

| Name | Description |
|---|---|
| Note The callback functions must correspond to the following syntax: long FunctionName( dword ); Should the CAPL function used as callback not longer be called when CANstress changes into the Pending condition, an empty string must be passed as parameter to CANstressOnPending. // delete or switch off present callback CANstressOnPending( " " ); |  |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.0 | — | — | — | 1.1 |
| Restricted To | — | CAN CANstress | — | — | — | CAN CANstress |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
