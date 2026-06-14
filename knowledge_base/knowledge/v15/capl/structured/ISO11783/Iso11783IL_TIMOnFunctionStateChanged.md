# Iso11783IL_TIMOnFunctionStateChanged

> Category: `ISO11783` | Type: `function`

## Syntax

```c
void Iso11783IL_TIMOnFunctionStateChanged(dword functionID, dword newState)
```

## Description

This callback function is called if the state of a TIM function has been changed. If this callback function is used by a TIM client the function is only called if the TIM function is assigned by the client.

You can also use the function Iso11783IL_TIMConnectSysVarToFunctionState if you are interested in the state of a function.

## Parameters

| Name | Description |
|---|---|
| Function ID | Description |
| 1-32 (1h-20h) | Auxiliary Value 1 – 32 |
| 64 (40h) | Front PTO |
| 65 (41h) | Rear PTO |
| 66 (42h) | Front hitch |
| 67 (43h) | Rear hitch |
| 68 (44h) | Vehicle speed |
| 70 (46h) | External guidance |
| State | Description |
| 0 | Automation unavailable |
| 1 | Automation not ready |
| 2 | Automation ready to enable |
| 3 | Automation enabled |
| 4 | Automation pending |
| 5 | Active, not limited |
| 6 | Active, limited high |
| 7 | Active, limited low |
| 14 | Non-recoverable fault |
| 15 | Not available (parameter not supported or not configured for TIM) |

## Return Values

—

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 | 13.0 | — | — | — |
| Restricted To | — | ISO11783 | ISO11783 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
