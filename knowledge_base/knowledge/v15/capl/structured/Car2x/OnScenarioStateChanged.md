# OnScenarioStateChanged

> Category: `Car2x` | Type: `function`

## Syntax

```c
void OnScenarioStateChanged(long newState);
```

## Description

This callback function is called when the state of the scenario was changed in Scenario Manager Window or by calling Scenario API CAPL functions.

## Parameters

| Name | Description |
|---|---|
| newState | Actual state of the scenario 0: Loaded – The scenario file was successfully loaded as a result of C2xLoadScenario() CAPL function call 1: Started – Scenario was started (in Scenario Manager window or by C2xStartScenario() function call) 2: Stopped - Scenario was stopped (in Scenario Manager or by C2xStopScenario() function call) 3: Completed – Scenario has reached the end of its timeline defined in the scenario file. |

## Return Values

—

## Example

```c
void OnScenarioStateChanged(long newState)
{
  write ("New state %d", newState);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 SP2 | — | — | — | 3.0 SP2 |
| Restricted To | — | Car2x | — | — | — | Car2x |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
