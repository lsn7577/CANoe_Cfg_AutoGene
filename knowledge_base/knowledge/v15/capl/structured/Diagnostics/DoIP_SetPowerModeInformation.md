# DoIP_SetPowerModeInformation

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_SetPowerModeInformation(long powerMode);
```

## Description

Sets the value returned automatically for a Power Mode Information Request.

## Parameters

| Name | Description |
|---|---|
| powerMode | -1: do not send a response for the request0: not ready1: ready2: not supported (default)Others: reserved |

## Return Values

—

## Example

```c
// The ECU simulation will return “ready” if the power mode is requested
DoIP_SetPowerModeInformation( 1);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.1 SP4 | — | — | — | 1.0 SP2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
