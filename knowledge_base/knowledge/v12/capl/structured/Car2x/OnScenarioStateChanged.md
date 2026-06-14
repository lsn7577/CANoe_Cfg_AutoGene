# OnScenarioStateChanged

> Category: `Car2x` | Type: `function`

## Syntax

```c
void OnScenarioStateChanged(long newState);
```

## Description

This callback function is called when the state of the scenario was changed in Scenario Manager Window or by calling Scenario API CAPL functions.

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

| Since Version |
|---|
