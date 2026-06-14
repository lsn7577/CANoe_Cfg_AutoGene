# C2xLoadScenario

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xLoadScenario(char* scenarioFilePath)
```

## Description

This function loads the scenario from the file specified by scenarioFilePath parameter. If the current scenario is running, it must be stopped via C2xStopScenario() function call or by stopping scenario in Scenario Manager window before calling C2xLoadScenario function. After C2xLoadScenario function call, the new scenario is not instantly available (scenario file loading takes at least 10 milliseconds time). When scenario loading is completed, the OnScenarioStateChanged callback will be called, with newState parameter equal to zero (0). At this time, the loaded scenario is available for further operations, by example scenario starting. The OnScenarioStateChanged callback will not be called if the scenario load fails.

## Return Values

1: Scenario load request successfully accepted. The scenario is now loaded in the background. Once the scenario load is completed, the OnScenarioStateChanged will be called with the parameter 0 (scenario load succeded). In the case, when scenario load fails, the OnScenarioStateChanged callback function will not be called.

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

| Since Version |
|---|
