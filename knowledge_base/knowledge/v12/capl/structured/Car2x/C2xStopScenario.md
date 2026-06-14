# C2xStopScenario

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xStopScenario();
```

## Description

This function stops the scenario execution immediately. The values of scenario attributes remain constant after the scenario stop. The scenario can be started again by calling C2xStartScenario() CAPL function or manually in Scenario Manager Window.

## Return Values

1 : Scenario was successfully stopped

## Example

```c
on key 's'
{
  if (C2xStopScenario() == 1)
  {
    write("Scenario stopped");
  }
}

on key 'r'
{
  if (C2xStartScenario() == 1)
  {
    write("Scenario started");
  }
}
```

## Availability

| Since Version |
|---|
