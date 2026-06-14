# C2xLoadScenario

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xLoadScenario(char* scenarioFilePath)
```

## Description

This function loads the scenario from the file specified by scenarioFilePath parameter. If the current scenario is running, it must be stopped via C2xStopScenario() function call or by stopping scenario in Scenario Manager window before calling C2xLoadScenario function. After C2xLoadScenario function call, the new scenario is not instantly available (scenario file loading takes at least 10 milliseconds time). When scenario loading is completed, the OnScenarioStateChanged callback will be called, with newState parameter equal to zero (0). At this time, the loaded scenario is available for further operations, by example scenario starting. The OnScenarioStateChanged callback will not be called if the scenario load fails.

## Parameters

| Name | Description |
|---|---|
| scenarioFilePath | The path to the scenario file, e.g. c:\SomeFolder\NewScenario.scn. The relative file paths are also accepted, with the relation to CANoe configuration folder. |

## Example

```c
on key ’x’
{
    C2xLoadScenario(”c:\SomeFolder\NewScenario.scn”);
    // C2xLoadScenario(”NewScenario2.scn”); // Load from CANoe configuration folder
}

void OnScenarioStateChanged(long newState)
{
  if (newState == 0) // new scenario file was loaded
  {
    C2xStartScenario();
  }
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
