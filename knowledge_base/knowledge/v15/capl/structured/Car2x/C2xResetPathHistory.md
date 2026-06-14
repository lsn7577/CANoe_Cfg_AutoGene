# C2xResetPathHistory

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xResetPathHistory() // form 1
long C2xResetPathHistory(long routeId) // form 2
```

## Description

This function clears path history data for the current station which was previously stored by periodic C2xAddGeoPos calls.

Call this function when:

By starting a scenario for this station the previous path history will be cleared automatically.

## Parameters

| Name | Description |
|---|---|
| routeId | Unique integer number which identify the path history position data storage from where the position data shall be deleted. This concrete routeId value must be previously used in periodic calls to the CAPL Function C2xAddGeoPos. Valid value range: routeId > 0. If routeId parameter is not used (form 1), all previously known path history data will be deleted. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 13.0: form 1-2 | — | — | — | 5.0: form 1-2 |
| Restricted To | — | Car2x | — | — | — | Car2x |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
