# GBT27930IL_InitAsBMS

> Category: `J1939` | Type: `function`

## Syntax

```c
long GBT27930IL_InitAsBMS( ); // form 1
long GBT27930IL_InitAsBMS(dbNode node); // form 2
```

## Description

Inits simulated node as a BMS. This function may be called at the earliest in on start, then it is verified whether all necessary messages are entered into the Tx list. Info about all missing messages will be displayed in the Write Window.

## Parameters

| Name | Description |
|---|---|
| node | Simulation node to apply the function. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 12.0 | 13.0 | — | — | 4.0 |
| Restricted To | — | J1939 and Smart Charging | J1939 and Smart Charging | — | — | form 2 J1939 and Smart Charging |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1) | ✔ (form 1) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2) | ✔ (form 2) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2) | ✔ (form 2) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
