# Iso11783PDDSetParameter

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783PDDSetParameter( dword ecuHandle, char paramName[], float paramValue );
```

## Description

Changes an internal parameter of the PDD API.

## Parameters

| Name | Description |
|---|---|
| ecuHandle | Handle of the ECU. The handle must be created with Iso11783CreateECU beforehand or ZERO for general parameters. |
| Value | Description |
| "debug" | activates debug outputs in the Write Window 1: on 0: off |
| "autoUpdateVariable" | process variable is updated if value command is received 1: auto update 0: process variable has to be updated manually by Iso11783PDDSetValue e.g. in callback function Iso11783PDDOnDataChanged) |
| "version" | supported version of the ISO11783 specification: 1,2 (default), 3, and 4 |
| paramValue | New value for the parameter |

## Example

```c
if (Iso11783PDDSetParameter( ecuHandle, "debug", 1 ) == 0) {
  write( "Debug mode activated" );
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 6.1 | 13.0 | — | — | — |
| Restricted To | — | ISO11783 | ISO11783 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
