# GBT27930IL_OnRxMessage

> Category: `J1939` | Type: `function`

## Syntax

```c
long GBT27930IL_OnRxMessage( pg * rxPG )
```

## Description

This callback function is called from the GBT27930 IL if the GBT27930 IL receives the parameter group, namely before the parameter group is processed by the GBT27930 IL. The message data can be manipulated in the callback method or handling of the message by the IL can be suppressed.

Usage

## Parameters

| Name | Description |
|---|---|
| rxPG | message which is received |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 12.0 | 13.0 | — | — | — |
| Restricted To | — | J1939 and Smart Charging | J1939 and Smart Charging | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
